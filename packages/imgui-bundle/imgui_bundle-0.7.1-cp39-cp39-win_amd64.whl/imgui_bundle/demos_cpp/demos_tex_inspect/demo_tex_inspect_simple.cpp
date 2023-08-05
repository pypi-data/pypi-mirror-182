// Demo imgui_tex_inspect
// See equivalent python program: bindings/imgui_bundle/demos/demos_tex_inspect/demo_tex_inspect.py

#include "hello_imgui/hello_imgui_assets.h"
#include "immapp/immapp.h"
#include "imgui_tex_inspect/imgui_tex_inspect.h"
#include "imgui_tex_inspect/imgui_tex_inspect_demo.h"

#include "demo_utils/api_demos.h"


// This returns a closure function that will later be invoked to run the app
GuiFunction make_gui()
{
    auto gui = [=]() mutable // mutable => this is a closure
    {
        static ImTextureID textureId = 0;
        static ImVec2 textureSize(512.f, 512.f);
        if (textureId == 0)
            textureId = HelloImGui::ImTextureIdFromAsset("images/bear_transparent.png");

        {
            ImGui::Text("Simple Demo");
            ImGuiTexInspect::InspectorFlags  flags = 0;
            ImGuiTexInspect::SizeIncludingBorder inspectorSize(ImmApp::EmToVec2(40.f, 40.f));

            if (ImGuiTexInspect::BeginInspectorPanel(
                "Texture inspector",
                textureId,
                textureSize, flags,
                inspectorSize))
            {
                ImGuiTexInspect::EndInspectorPanel();
            }
        }
    };
    return gui;
}


#ifndef IMGUI_BUNDLE_BUILD_DEMO_AS_LIBRARY
int main()
{
    auto gui = make_gui();
    HelloImGui::SimpleRunnerParams runnerParams{.guiFunction = gui, .windowSize={1000, 1000}};
    ImmApp::AddOnsParams addOnsParams;
    addOnsParams.withTexInspect = true;
    ImmApp::Run(runnerParams, addOnsParams);
    return 0;
}
#endif
