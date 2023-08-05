#!/usr/bin/env python3

import os
from sys import version_info
import typing
import time

# Global settings
THIS_DIR = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
REPO_DIR = os.path.realpath(THIS_DIR + "/../..").replace("\\", "/")
ALL_IN_ONE_DIR = f"{REPO_DIR}/src_all_in_one"
AUTOGENERATED_HEADER = "// THIS FILE WAS GENERATED AUTOMATICALLY. DO NOT EDIT.\n"


def fread_lines(filename):
    """
    Python 2 & 3 agnostic fopen + readlines
    """
    if version_info[0] >= 3:
        f = open(filename, "r", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "r")
    return f.readlines()


def fread_content(filename):
    """
    Python 2 & 3 agnostic fopen + readlines
    """
    if version_info[0] >= 3:
        f = open(filename, "r", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "r")
    return f.read()


def fwrite_content(filename, content):
    """
    Python 2 & 3 agnostic fopen + write
    This function will not overwrite the file (and thus not update its modification date)
    if the new content is unchanged
    """
    if os.path.isfile(filename):
        old_content = fread_content(filename)
        if old_content == content:
            return

    if version_info[0] >= 3:
        f = open(filename, "w", encoding="utf-8", errors="ignore")
    else:
        f = open(filename, "w")
    f.write(content)
    f.close()


def is_local_include_line(code_line):
    """
    Tests whether or not a C++ code line is a include statement that concerns a fplus header,
    (i.e this will *exclude* lines like "#include <vector>")
    """
    possible_include_paths = ["immvision/", "immdebug/", "immvision_gl_loader/"]
    result = False
    for possible_include_path in possible_include_paths:
        if code_line.startswith(f"#include <{possible_include_path}"):
            result = True
        if code_line.startswith(f'#include "{possible_include_path}'):
            result = True
    return result


def is_external_include_line(code_line):
    if not code_line.startswith("#include "):
        return False
    if is_local_include_line(code_line):
        return False
    return True


def extract_local_include_file(code_line):
    """
    Extracts the included file path from an include statement
    """
    result = code_line.replace('#include "', "").replace('"', "").replace(">", "")[:-1]
    # possible_include_paths = [ 'immvision/', 'immdebug/']
    # for possible_include_path in possible_include_paths:
    #     result = result.replace(possible_include_path, "")
    return result


def extract_external_include_file(code_line):
    result: str = code_line.replace("#include ", "").replace("\n", "")
    if "#" in result:
        result = result[: result.index("#")]
    return result


def decorate_code_info(info):
    separator_line = "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    middle_line = f"//                       {info}".ljust(len(separator_line) - 2) + "//"
    result = f"""
{separator_line}
{middle_line}
{separator_line}
"""
    return result


def amalgamate_one_file(
    included_filename, including_filename, already_included_local_files, already_included_external_files
):
    """
    Recursive function that will create an amalgamation for a given header file.
    """
    filename_orig = included_filename
    if not os.path.isfile(included_filename):
        included_filename = f"{REPO_DIR}/{filename_orig}"
    if not os.path.isfile(included_filename):
        included_filename = f"{REPO_DIR}/src/{filename_orig}"
    if not os.path.isfile(included_filename):
        raise FileNotFoundError(included_filename)

    if included_filename in already_included_local_files:
        return ""

    already_included_local_files.append(included_filename)

    included_filename_relative = included_filename.replace(REPO_DIR + "/", "")

    if len(including_filename) > 0:
        header = decorate_code_info(f"{included_filename_relative} included by {including_filename}")
    else:
        header = decorate_code_info(included_filename_relative)
    parsed_result = header

    lines = fread_lines(included_filename)
    was_file_interrupted_by_include = False
    for code_line in lines:
        if was_file_interrupted_by_include and len(code_line.strip()) > 0:
            parsed_result = parsed_result + decorate_code_info(included_filename_relative + " continued")
            was_file_interrupted_by_include = False
        if is_external_include_line(code_line):
            external_file = extract_external_include_file(code_line)
            if external_file not in already_included_external_files:
                parsed_result = parsed_result + code_line
                already_included_external_files.append(external_file)
        elif is_local_include_line(code_line):
            new_file = extract_local_include_file(code_line)
            include_addition = amalgamate_one_file(
                new_file, included_filename_relative, already_included_local_files, already_included_external_files
            )
            if len(include_addition) > 0:
                parsed_result = parsed_result + include_addition
                was_file_interrupted_by_include = True
        else:
            if not "#pragma once" in code_line:
                parsed_result = parsed_result + code_line

    is_code_composed_of_only_blank_lines = True
    for line in parsed_result.split("\n"):
        if len(line.strip()) != 0:
            is_code_composed_of_only_blank_lines = False
    if is_code_composed_of_only_blank_lines:
        return ""

    return parsed_result


def write_amalgamate_header_file(src_header_file, dst_file):
    content = amalgamate_one_file(src_header_file, "", [], [])
    content = AUTOGENERATED_HEADER + content
    fwrite_content(dst_file, content)


def amalgamate_cpp_files_content(folder, cpp_files: typing.List[str]):
    cpp_files = sorted(cpp_files)
    content = ""
    already_included_local_files = []
    already_included_external_files = []
    for cpp_file in cpp_files:
        content = content + amalgamate_one_file(
            folder + "/" + cpp_file, "", already_included_local_files, already_included_external_files
        )
        content = content + "\n"
    return content


def find_all_files_of_extension(folder, extension):
    found_files = []
    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            if name.endswith(extension):
                found_file = root + "/" + name
                found_file = found_file.replace("\\", "/")
                found_file = found_file.replace(folder + "/", "")
                found_files.append(found_file)
    return found_files


def write_amalgamate_cpp_files(folder, dst_file):
    folder = f"{REPO_DIR}/{folder}"
    cpp_files = find_all_files_of_extension(folder, ".cpp")
    content = amalgamate_cpp_files_content(folder, cpp_files)
    content = AUTOGENERATED_HEADER + content
    fwrite_content(dst_file, content)


def generate_src_all_in_one():
    start = time.time()
    write_amalgamate_header_file("src/immvision/immvision.h", f"{ALL_IN_ONE_DIR}/immvision/immvision.h")
    write_amalgamate_cpp_files("src/immvision", f"{ALL_IN_ONE_DIR}/immvision/immvision.cpp")
    elapsed = time.time() - start
    print(f"  generate_src_all_in_one (took {elapsed:.2f}s)")


if __name__ == "__main__":
    generate_src_all_in_one()
