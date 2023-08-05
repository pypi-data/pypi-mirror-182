/*
  Simple DirectMedia Layer
  Copyright (C) 1997-2022 Sam Lantinga <slouken@libsdl.org>

  This software is provided 'as-is', without any express or implied
  warranty.  In no event will the authors be held liable for any damages
  arising from the use of this software.

  Permission is granted to anyone to use this software for any purpose,
  including commercial applications, and to alter it and redistribute it
  freely, subject to the following restrictions:

  1. The origin of this software must not be misrepresented; you must not
     claim that you wrote the original software. If you use this software
     in a product, an acknowledgment in the product documentation would be
     appreciated but is not required.
  2. Altered source versions must be plainly marked as such, and must not be
     misrepresented as being the original software.
  3. This notice may not be removed or altered from any source distribution.
*/

#include "../../SDL_internal.h"

#ifndef _SDL_ngagevideo_h
#define _SDL_ngagevideo_h

#include "../SDL_sysvideo.h"

#include <e32std.h>
#include <e32svr.h>
#include <bitdev.h>
#include <w32std.h>

class CFbsDrawDevice : public CBase
{
public:
public:
    IMPORT_C static CFbsDrawDevice* NewScreenDeviceL(TScreenInfoV01 aInfo,TDisplayMode aDispMode);
public:
    virtual void Update() {}
    virtual void UpdateRegion(const TRect&) {}
};

#define _THIS SDL_VideoDevice *_this

typedef struct SDL_VideoData
{
    /* Epoc window server info */
    RWsSession       NGAGE_WsSession;
    RWindowGroup     NGAGE_WsWindowGroup;
    TInt             NGAGE_WsWindowGroupID;
    RWindow          NGAGE_WsWindow;
    CWsScreenDevice* NGAGE_WsScreen;
    CWindowGc*       NGAGE_WindowGc;
    TRequestStatus   NGAGE_WsEventStatus;
    TRequestStatus   NGAGE_RedrawEventStatus;
    TWsEvent         NGAGE_WsEvent;
    CFbsDrawDevice*  NGAGE_DrawDevice;
    TBool            NGAGE_IsWindowFocused; /* Not used yet */

    /* Screen hardware frame buffer info */
    TBool            NGAGE_HasFrameBuffer;
    TInt             NGAGE_BytesPerPixel;
    TInt             NGAGE_BytesPerScanLine;
    TInt             NGAGE_BytesPerScreen;
    TDisplayMode     NGAGE_DisplayMode;
    TSize            NGAGE_ScreenSize;
    TUint8*          NGAGE_FrameBuffer;
    TPoint           NGAGE_ScreenOffset;

    CFbsBitGc::TGraphicsOrientation NGAGE_ScreenOrientation;

} SDL_VideoData;

#endif /* _SDL_ngagevideo_h */

/* vi: set ts=4 sw=4 expandtab: */
