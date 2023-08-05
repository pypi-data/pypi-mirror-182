# based on the files generated by CMake's write_basic_package_version_file

# SDL2 CMake version configuration file:
# This file is meant to be placed in a cmake subfolder of SDL2-devel-2.x.y-VC

if(NOT EXISTS "${CMAKE_CURRENT_LIST_DIR}/../include/SDL_version.h")
    message(AUTHOR_WARNING "Could not find SDL_version.h. This script is meant to be placed in the root of SDL2-devel-2.x.y-VC")
    return()
endif()

file(READ "${CMAKE_CURRENT_LIST_DIR}/../include/SDL_version.h" _sdl_version_h)
string(REGEX MATCH "#define[ \t]+SDL_MAJOR_VERSION[ \t]+([0-9]+)" _sdl_major_re "${_sdl_version_h}")
set(_sdl_major "${CMAKE_MATCH_1}")
string(REGEX MATCH "#define[ \t]+SDL_MINOR_VERSION[ \t]+([0-9]+)" _sdl_minor_re "${_sdl_version_h}")
set(_sdl_minor "${CMAKE_MATCH_1}")
string(REGEX MATCH "#define[ \t]+SDL_PATCHLEVEL[ \t]+([0-9]+)" _sdl_patch_re "${_sdl_version_h}")
set(_sdl_patch "${CMAKE_MATCH_1}")
if(_sdl_major_re AND _sdl_minor_re AND _sdl_patch_re)
    set(PACKAGE_VERSION "${_sdl_major}.${_sdl_minor}.${_sdl_patch}")
else()
    message(AUTHOR_WARNING "Could not extract version from SDL_version.h.")
    return()
endif()

if(PACKAGE_FIND_VERSION_RANGE)
    # Package version must be in the requested version range
    if ((PACKAGE_FIND_VERSION_RANGE_MIN STREQUAL "INCLUDE" AND PACKAGE_VERSION VERSION_LESS PACKAGE_FIND_VERSION_MIN)
        OR ((PACKAGE_FIND_VERSION_RANGE_MAX STREQUAL "INCLUDE" AND PACKAGE_VERSION VERSION_GREATER PACKAGE_FIND_VERSION_MAX)
        OR (PACKAGE_FIND_VERSION_RANGE_MAX STREQUAL "EXCLUDE" AND PACKAGE_VERSION VERSION_GREATER_EQUAL PACKAGE_FIND_VERSION_MAX)))
        set(PACKAGE_VERSION_COMPATIBLE FALSE)
    else()
        set(PACKAGE_VERSION_COMPATIBLE TRUE)
    endif()
else()
    if(PACKAGE_VERSION VERSION_LESS PACKAGE_FIND_VERSION)
        set(PACKAGE_VERSION_COMPATIBLE FALSE)
    else()
        set(PACKAGE_VERSION_COMPATIBLE TRUE)
        if(PACKAGE_FIND_VERSION STREQUAL PACKAGE_VERSION)
            set(PACKAGE_VERSION_EXACT TRUE)
        endif()
    endif()
endif()

# if the using project doesn't have CMAKE_SIZEOF_VOID_P set, fail.
if("${CMAKE_SIZEOF_VOID_P}" STREQUAL "")
    set(PACKAGE_VERSION_UNSUITABLE TRUE)
endif()

# check that the installed version has the same 32/64bit-ness as the one which is currently searching:
if(NOT (CMAKE_SIZEOF_VOID_P STREQUAL "8" OR CMAKE_SIZEOF_VOID_P STREQUAL "4"))
    set(PACKAGE_VERSION "${PACKAGE_VERSION} (32+64bit)")
    set(PACKAGE_VERSION_UNSUITABLE TRUE)
endif()
