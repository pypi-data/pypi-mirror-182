"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_collaboration-extension_lib_index_js-_aa170"],{

/***/ "../../packages/collaboration-extension/lib/index.js":
/*!***********************************************************!*\
  !*** ../../packages/collaboration-extension/lib/index.js ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var yjs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! yjs */ "webpack/sharing/consume/default/yjs/yjs");
/* harmony import */ var yjs__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(yjs__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var y_protocols_awareness__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! y-protocols/awareness */ "../../node_modules/y-protocols/awareness.js");
/* harmony import */ var y_websocket__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! y-websocket */ "webpack/sharing/consume/default/y-websocket/y-websocket");
/* harmony import */ var y_websocket__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(y_websocket__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/collaboration */ "webpack/sharing/consume/default/@jupyterlab/collaboration/@jupyterlab/collaboration");
/* harmony import */ var _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module collaboration-extension
 */












/**
 * Jupyter plugin providing the ICurrentUser.
 */
const userPlugin = {
    id: '@jupyterlab/collaboration-extension:user',
    autoStart: true,
    provides: _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.ICurrentUser,
    activate: (app) => {
        return new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.User();
    }
};
/**
 * Jupyter plugin providing the IUserMenu.
 */
const userMenuPlugin = {
    id: '@jupyterlab/collaboration-extension:userMenu',
    autoStart: true,
    requires: [_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.ICurrentUser],
    provides: _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.IUserMenu,
    activate: (app, user) => {
        const { commands } = app;
        return new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.UserMenu({ commands, user });
    }
};
/**
 * Jupyter plugin adding the IUserMenu to the menu bar if collaborative flag enabled.
 */
const menuBarPlugin = {
    id: '@jupyterlab/collaboration-extension:userMenuBar',
    autoStart: true,
    requires: [_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.ICurrentUser, _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.IUserMenu],
    activate: (app, user, menu) => {
        const { shell } = app;
        if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getOption('collaborative') !== 'true') {
            return;
        }
        const menuBar = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_7__.MenuBar({
            forceItemsPosition: {
                forceX: false,
                forceY: false
            },
            renderer: new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.RendererUserMenu(user)
        });
        menuBar.id = 'jp-UserMenu';
        user.changed.connect(() => menuBar.update());
        menuBar.addMenu(menu);
        shell.add(menuBar, 'top', { rank: 1000 });
    }
};
/**
 * Jupyter plugin creating a global awareness for RTC.
 */
const rtcGlobalAwarenessPlugin = {
    id: '@jupyterlab/collaboration-extension:rtcGlobalAwareness',
    autoStart: true,
    requires: [_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.ICurrentUser, _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_9__.IStateDB],
    provides: _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.IGlobalAwareness,
    activate: (app, currentUser, state) => {
        const ydoc = new yjs__WEBPACK_IMPORTED_MODULE_0__.Doc();
        if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getOption('collaborative') !== 'true') {
            return new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.AwarenessMock(ydoc);
        }
        const awareness = new y_protocols_awareness__WEBPACK_IMPORTED_MODULE_1__.Awareness(ydoc);
        const server = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_8__.ServerConnection.makeSettings();
        const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.URLExt.join(server.wsUrl, 'api/yjs');
        new y_websocket__WEBPACK_IMPORTED_MODULE_2__.WebsocketProvider(url, 'JupyterLab:globalAwareness', ydoc, {
            awareness: awareness
        });
        const userChanged = () => {
            const name = currentUser.displayName !== ''
                ? currentUser.displayName
                : currentUser.name;
            awareness.setLocalStateField('user', Object.assign(Object.assign({}, currentUser.toJSON()), { name }));
        };
        if (currentUser.isReady) {
            userChanged();
        }
        currentUser.ready.connect(userChanged);
        currentUser.changed.connect(userChanged);
        state.changed.connect(async () => {
            var _a, _b;
            const data = await state.toJSON();
            const current = ((_b = (_a = data['layout-restorer:data']) === null || _a === void 0 ? void 0 : _a.main) === null || _b === void 0 ? void 0 : _b.current) || '';
            if (current.startsWith('editor') || current.startsWith('notebook')) {
                awareness.setLocalStateField('current', current);
            }
            else {
                awareness.setLocalStateField('current', null);
            }
        });
        return awareness;
    }
};
/**
 * Jupyter plugin adding the RTC information to the application left panel if collaborative flag enabled.
 */
const rtcPanelPlugin = {
    id: '@jupyterlab/collaboration-extension:rtcPanel',
    autoStart: true,
    requires: [_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.ICurrentUser, _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.IGlobalAwareness, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__.ITranslator],
    activate: (app, currentUser, awareness, translator) => {
        if (_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getOption('collaborative') !== 'true') {
            return;
        }
        const trans = translator.load('jupyterlab');
        const userPanel = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_6__.SidePanel();
        userPanel.id = _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_4__.DOMUtils.createDomID();
        userPanel.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_6__.usersIcon;
        userPanel.addClass('jp-RTCPanel');
        app.shell.add(userPanel, 'left', { rank: 300 });
        const currentUserPanel = new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.UserInfoPanel(currentUser);
        currentUserPanel.title.label = trans.__('User info');
        currentUserPanel.title.caption = trans.__('User information');
        userPanel.addWidget(currentUserPanel);
        const fileopener = (path) => {
            void app.commands.execute('docmanager:open', { path });
        };
        const collaboratorsPanel = new _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_5__.CollaboratorsPanel(currentUser, awareness, fileopener);
        collaboratorsPanel.title.label = trans.__('Online Collaborators');
        userPanel.addWidget(collaboratorsPanel);
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [
    userPlugin,
    userMenuPlugin,
    menuBarPlugin,
    rtcGlobalAwarenessPlugin,
    rtcPanelPlugin
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29sbGFib3JhdGlvbi1leHRlbnNpb25fbGliX2luZGV4X2pzLV9hYTE3MC4yNzZkN2VhMjFjOTM2M2Y4OGQ4NC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFFc0I7QUFDeUI7QUFDRjtBQU1HO0FBQ0g7QUFZYjtBQUM4QjtBQUNqQjtBQUNEO0FBQ1M7QUFDQTtBQUNGO0FBRXREOztHQUVHO0FBQ0gsTUFBTSxVQUFVLEdBQXdDO0lBQ3RELEVBQUUsRUFBRSwwQ0FBMEM7SUFDOUMsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsbUVBQVk7SUFDdEIsUUFBUSxFQUFFLENBQUMsR0FBb0IsRUFBZ0IsRUFBRTtRQUMvQyxPQUFPLElBQUksMkRBQUksRUFBRSxDQUFDO0lBQ3BCLENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLGNBQWMsR0FBcUM7SUFDdkQsRUFBRSxFQUFFLDhDQUE4QztJQUNsRCxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUFDLG1FQUFZLENBQUM7SUFDeEIsUUFBUSxFQUFFLGdFQUFTO0lBQ25CLFFBQVEsRUFBRSxDQUFDLEdBQW9CLEVBQUUsSUFBa0IsRUFBYSxFQUFFO1FBQ2hFLE1BQU0sRUFBRSxRQUFRLEVBQUUsR0FBRyxHQUFHLENBQUM7UUFDekIsT0FBTyxJQUFJLCtEQUFRLENBQUMsRUFBRSxRQUFRLEVBQUUsSUFBSSxFQUFFLENBQUMsQ0FBQztJQUMxQyxDQUFDO0NBQ0YsQ0FBQztBQUVGOztHQUVHO0FBQ0gsTUFBTSxhQUFhLEdBQWdDO0lBQ2pELEVBQUUsRUFBRSxpREFBaUQ7SUFDckQsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxtRUFBWSxFQUFFLGdFQUFTLENBQUM7SUFDbkMsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsSUFBa0IsRUFDbEIsSUFBZSxFQUNULEVBQUU7UUFDUixNQUFNLEVBQUUsS0FBSyxFQUFFLEdBQUcsR0FBRyxDQUFDO1FBRXRCLElBQUksdUVBQW9CLENBQUMsZUFBZSxDQUFDLEtBQUssTUFBTSxFQUFFO1lBQ3BELE9BQU87U0FDUjtRQUVELE1BQU0sT0FBTyxHQUFHLElBQUksb0RBQU8sQ0FBQztZQUMxQixrQkFBa0IsRUFBRTtnQkFDbEIsTUFBTSxFQUFFLEtBQUs7Z0JBQ2IsTUFBTSxFQUFFLEtBQUs7YUFDZDtZQUNELFFBQVEsRUFBRSxJQUFJLHVFQUFnQixDQUFDLElBQUksQ0FBQztTQUNyQyxDQUFDLENBQUM7UUFDSCxPQUFPLENBQUMsRUFBRSxHQUFHLGFBQWEsQ0FBQztRQUMzQixJQUFJLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUUsQ0FBQyxPQUFPLENBQUMsTUFBTSxFQUFFLENBQUMsQ0FBQztRQUM3QyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQVksQ0FBQyxDQUFDO1FBQzlCLEtBQUssQ0FBQyxHQUFHLENBQUMsT0FBTyxFQUFFLEtBQUssRUFBRSxFQUFFLElBQUksRUFBRSxJQUFJLEVBQUUsQ0FBQyxDQUFDO0lBQzVDLENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLHdCQUF3QixHQUFzQztJQUNsRSxFQUFFLEVBQUUsd0RBQXdEO0lBQzVELFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsbUVBQVksRUFBRSx5REFBUSxDQUFDO0lBQ2xDLFFBQVEsRUFBRSx1RUFBZ0I7SUFDMUIsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsV0FBaUIsRUFDakIsS0FBYyxFQUNGLEVBQUU7UUFDZCxNQUFNLElBQUksR0FBRyxJQUFJLG9DQUFLLEVBQUUsQ0FBQztRQUV6QixJQUFJLHVFQUFvQixDQUFDLGVBQWUsQ0FBQyxLQUFLLE1BQU0sRUFBRTtZQUNwRCxPQUFPLElBQUksb0VBQWEsQ0FBQyxJQUFJLENBQUMsQ0FBQztTQUNoQztRQUVELE1BQU0sU0FBUyxHQUFHLElBQUksNERBQVMsQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUV0QyxNQUFNLE1BQU0sR0FBRywrRUFBNkIsRUFBRSxDQUFDO1FBQy9DLE1BQU0sR0FBRyxHQUFHLDhEQUFXLENBQUMsTUFBTSxDQUFDLEtBQUssRUFBRSxTQUFTLENBQUMsQ0FBQztRQUVqRCxJQUFJLDBEQUFpQixDQUFDLEdBQUcsRUFBRSw0QkFBNEIsRUFBRSxJQUFJLEVBQUU7WUFDN0QsU0FBUyxFQUFFLFNBQVM7U0FDckIsQ0FBQyxDQUFDO1FBRUgsTUFBTSxXQUFXLEdBQUcsR0FBRyxFQUFFO1lBQ3ZCLE1BQU0sSUFBSSxHQUNSLFdBQVcsQ0FBQyxXQUFXLEtBQUssRUFBRTtnQkFDNUIsQ0FBQyxDQUFDLFdBQVcsQ0FBQyxXQUFXO2dCQUN6QixDQUFDLENBQUMsV0FBVyxDQUFDLElBQUksQ0FBQztZQUN2QixTQUFTLENBQUMsa0JBQWtCLENBQUMsTUFBTSxrQ0FBTyxXQUFXLENBQUMsTUFBTSxFQUFFLEtBQUUsSUFBSSxJQUFHLENBQUM7UUFDMUUsQ0FBQyxDQUFDO1FBQ0YsSUFBSSxXQUFXLENBQUMsT0FBTyxFQUFFO1lBQ3ZCLFdBQVcsRUFBRSxDQUFDO1NBQ2Y7UUFDRCxXQUFXLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxXQUFXLENBQUMsQ0FBQztRQUN2QyxXQUFXLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxXQUFXLENBQUMsQ0FBQztRQUV6QyxLQUFLLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxLQUFLLElBQUksRUFBRTs7WUFDL0IsTUFBTSxJQUFJLEdBQVEsTUFBTSxLQUFLLENBQUMsTUFBTSxFQUFFLENBQUM7WUFDdkMsTUFBTSxPQUFPLEdBQUcsaUJBQUksQ0FBQyxzQkFBc0IsQ0FBQywwQ0FBRSxJQUFJLDBDQUFFLE9BQU8sS0FBSSxFQUFFLENBQUM7WUFFbEUsSUFBSSxPQUFPLENBQUMsVUFBVSxDQUFDLFFBQVEsQ0FBQyxJQUFJLE9BQU8sQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLEVBQUU7Z0JBQ2xFLFNBQVMsQ0FBQyxrQkFBa0IsQ0FBQyxTQUFTLEVBQUUsT0FBTyxDQUFDLENBQUM7YUFDbEQ7aUJBQU07Z0JBQ0wsU0FBUyxDQUFDLGtCQUFrQixDQUFDLFNBQVMsRUFBRSxJQUFJLENBQUMsQ0FBQzthQUMvQztRQUNILENBQUMsQ0FBQyxDQUFDO1FBRUgsT0FBTyxTQUFTLENBQUM7SUFDbkIsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sY0FBYyxHQUFnQztJQUNsRCxFQUFFLEVBQUUsOENBQThDO0lBQ2xELFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsbUVBQVksRUFBRSx1RUFBZ0IsRUFBRSxpRUFBVyxDQUFDO0lBQ3ZELFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFdBQWlCLEVBQ2pCLFNBQW9CLEVBQ3BCLFVBQXVCLEVBQ2pCLEVBQUU7UUFDUixJQUFJLHVFQUFvQixDQUFDLGVBQWUsQ0FBQyxLQUFLLE1BQU0sRUFBRTtZQUNwRCxPQUFPO1NBQ1I7UUFFRCxNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBRTVDLE1BQU0sU0FBUyxHQUFHLElBQUksZ0VBQVMsRUFBRSxDQUFDO1FBQ2xDLFNBQVMsQ0FBQyxFQUFFLEdBQUcsc0VBQW9CLEVBQUUsQ0FBQztRQUN0QyxTQUFTLENBQUMsS0FBSyxDQUFDLElBQUksR0FBRyxnRUFBUyxDQUFDO1FBQ2pDLFNBQVMsQ0FBQyxRQUFRLENBQUMsYUFBYSxDQUFDLENBQUM7UUFDbEMsR0FBRyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsU0FBUyxFQUFFLE1BQU0sRUFBRSxFQUFFLElBQUksRUFBRSxHQUFHLEVBQUUsQ0FBQyxDQUFDO1FBRWhELE1BQU0sZ0JBQWdCLEdBQUcsSUFBSSxvRUFBYSxDQUFDLFdBQVcsQ0FBQyxDQUFDO1FBQ3hELGdCQUFnQixDQUFDLEtBQUssQ0FBQyxLQUFLLEdBQUcsS0FBSyxDQUFDLEVBQUUsQ0FBQyxXQUFXLENBQUMsQ0FBQztRQUNyRCxnQkFBZ0IsQ0FBQyxLQUFLLENBQUMsT0FBTyxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQUMsa0JBQWtCLENBQUMsQ0FBQztRQUM5RCxTQUFTLENBQUMsU0FBUyxDQUFDLGdCQUFnQixDQUFDLENBQUM7UUFFdEMsTUFBTSxVQUFVLEdBQUcsQ0FBQyxJQUFZLEVBQUUsRUFBRTtZQUNsQyxLQUFLLEdBQUcsQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLGlCQUFpQixFQUFFLEVBQUUsSUFBSSxFQUFFLENBQUMsQ0FBQztRQUN6RCxDQUFDLENBQUM7UUFFRixNQUFNLGtCQUFrQixHQUFHLElBQUkseUVBQWtCLENBQy9DLFdBQVcsRUFDWCxTQUFTLEVBQ1QsVUFBVSxDQUNYLENBQUM7UUFDRixrQkFBa0IsQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLEtBQUssQ0FBQyxFQUFFLENBQUMsc0JBQXNCLENBQUMsQ0FBQztRQUNsRSxTQUFTLENBQUMsU0FBUyxDQUFDLGtCQUFrQixDQUFDLENBQUM7SUFDMUMsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFpQztJQUM1QyxVQUFVO0lBQ1YsY0FBYztJQUNkLGFBQWE7SUFDYix3QkFBd0I7SUFDeEIsY0FBYztDQUNmLENBQUM7QUFFRixpRUFBZSxPQUFPLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNvbGxhYm9yYXRpb24tZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0ICogYXMgWSBmcm9tICd5anMnO1xuaW1wb3J0IHsgQXdhcmVuZXNzIH0gZnJvbSAneS1wcm90b2NvbHMvYXdhcmVuZXNzJztcbmltcG9ydCB7IFdlYnNvY2tldFByb3ZpZGVyIH0gZnJvbSAneS13ZWJzb2NrZXQnO1xuXG5pbXBvcnQge1xuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBQYWdlQ29uZmlnIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7IERPTVV0aWxzIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHtcbiAgQXdhcmVuZXNzTW9jayxcbiAgQ29sbGFib3JhdG9yc1BhbmVsLFxuICBJQXdhcmVuZXNzLFxuICBJQ3VycmVudFVzZXIsXG4gIElHbG9iYWxBd2FyZW5lc3MsXG4gIElVc2VyTWVudSxcbiAgUmVuZGVyZXJVc2VyTWVudSxcbiAgVXNlcixcbiAgVXNlckluZm9QYW5lbCxcbiAgVXNlck1lbnVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbic7XG5pbXBvcnQgeyBTaWRlUGFuZWwsIHVzZXJzSWNvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgTWVudSwgTWVudUJhciB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBVUkxFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgU2VydmVyQ29ubmVjdGlvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IElTdGF0ZURCLCBTdGF0ZURCIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdGVkYic7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcblxuLyoqXG4gKiBKdXB5dGVyIHBsdWdpbiBwcm92aWRpbmcgdGhlIElDdXJyZW50VXNlci5cbiAqL1xuY29uc3QgdXNlclBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPElDdXJyZW50VXNlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbi1leHRlbnNpb246dXNlcicsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElDdXJyZW50VXNlcixcbiAgYWN0aXZhdGU6IChhcHA6IEp1cHl0ZXJGcm9udEVuZCk6IElDdXJyZW50VXNlciA9PiB7XG4gICAgcmV0dXJuIG5ldyBVc2VyKCk7XG4gIH1cbn07XG5cbi8qKlxuICogSnVweXRlciBwbHVnaW4gcHJvdmlkaW5nIHRoZSBJVXNlck1lbnUuXG4gKi9cbmNvbnN0IHVzZXJNZW51UGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVVzZXJNZW51PiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb2xsYWJvcmF0aW9uLWV4dGVuc2lvbjp1c2VyTWVudScsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJQ3VycmVudFVzZXJdLFxuICBwcm92aWRlczogSVVzZXJNZW51LFxuICBhY3RpdmF0ZTogKGFwcDogSnVweXRlckZyb250RW5kLCB1c2VyOiBJQ3VycmVudFVzZXIpOiBJVXNlck1lbnUgPT4ge1xuICAgIGNvbnN0IHsgY29tbWFuZHMgfSA9IGFwcDtcbiAgICByZXR1cm4gbmV3IFVzZXJNZW51KHsgY29tbWFuZHMsIHVzZXIgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogSnVweXRlciBwbHVnaW4gYWRkaW5nIHRoZSBJVXNlck1lbnUgdG8gdGhlIG1lbnUgYmFyIGlmIGNvbGxhYm9yYXRpdmUgZmxhZyBlbmFibGVkLlxuICovXG5jb25zdCBtZW51QmFyUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbi1leHRlbnNpb246dXNlck1lbnVCYXInLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUN1cnJlbnRVc2VyLCBJVXNlck1lbnVdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHVzZXI6IElDdXJyZW50VXNlcixcbiAgICBtZW51OiBJVXNlck1lbnVcbiAgKTogdm9pZCA9PiB7XG4gICAgY29uc3QgeyBzaGVsbCB9ID0gYXBwO1xuXG4gICAgaWYgKFBhZ2VDb25maWcuZ2V0T3B0aW9uKCdjb2xsYWJvcmF0aXZlJykgIT09ICd0cnVlJykge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGNvbnN0IG1lbnVCYXIgPSBuZXcgTWVudUJhcih7XG4gICAgICBmb3JjZUl0ZW1zUG9zaXRpb246IHtcbiAgICAgICAgZm9yY2VYOiBmYWxzZSxcbiAgICAgICAgZm9yY2VZOiBmYWxzZVxuICAgICAgfSxcbiAgICAgIHJlbmRlcmVyOiBuZXcgUmVuZGVyZXJVc2VyTWVudSh1c2VyKVxuICAgIH0pO1xuICAgIG1lbnVCYXIuaWQgPSAnanAtVXNlck1lbnUnO1xuICAgIHVzZXIuY2hhbmdlZC5jb25uZWN0KCgpID0+IG1lbnVCYXIudXBkYXRlKCkpO1xuICAgIG1lbnVCYXIuYWRkTWVudShtZW51IGFzIE1lbnUpO1xuICAgIHNoZWxsLmFkZChtZW51QmFyLCAndG9wJywgeyByYW5rOiAxMDAwIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIEp1cHl0ZXIgcGx1Z2luIGNyZWF0aW5nIGEgZ2xvYmFsIGF3YXJlbmVzcyBmb3IgUlRDLlxuICovXG5jb25zdCBydGNHbG9iYWxBd2FyZW5lc3NQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJQXdhcmVuZXNzPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb2xsYWJvcmF0aW9uLWV4dGVuc2lvbjpydGNHbG9iYWxBd2FyZW5lc3MnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUN1cnJlbnRVc2VyLCBJU3RhdGVEQl0sXG4gIHByb3ZpZGVzOiBJR2xvYmFsQXdhcmVuZXNzLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGN1cnJlbnRVc2VyOiBVc2VyLFxuICAgIHN0YXRlOiBTdGF0ZURCXG4gICk6IElBd2FyZW5lc3MgPT4ge1xuICAgIGNvbnN0IHlkb2MgPSBuZXcgWS5Eb2MoKTtcblxuICAgIGlmIChQYWdlQ29uZmlnLmdldE9wdGlvbignY29sbGFib3JhdGl2ZScpICE9PSAndHJ1ZScpIHtcbiAgICAgIHJldHVybiBuZXcgQXdhcmVuZXNzTW9jayh5ZG9jKTtcbiAgICB9XG5cbiAgICBjb25zdCBhd2FyZW5lc3MgPSBuZXcgQXdhcmVuZXNzKHlkb2MpO1xuXG4gICAgY29uc3Qgc2VydmVyID0gU2VydmVyQ29ubmVjdGlvbi5tYWtlU2V0dGluZ3MoKTtcbiAgICBjb25zdCB1cmwgPSBVUkxFeHQuam9pbihzZXJ2ZXIud3NVcmwsICdhcGkveWpzJyk7XG5cbiAgICBuZXcgV2Vic29ja2V0UHJvdmlkZXIodXJsLCAnSnVweXRlckxhYjpnbG9iYWxBd2FyZW5lc3MnLCB5ZG9jLCB7XG4gICAgICBhd2FyZW5lc3M6IGF3YXJlbmVzc1xuICAgIH0pO1xuXG4gICAgY29uc3QgdXNlckNoYW5nZWQgPSAoKSA9PiB7XG4gICAgICBjb25zdCBuYW1lID1cbiAgICAgICAgY3VycmVudFVzZXIuZGlzcGxheU5hbWUgIT09ICcnXG4gICAgICAgICAgPyBjdXJyZW50VXNlci5kaXNwbGF5TmFtZVxuICAgICAgICAgIDogY3VycmVudFVzZXIubmFtZTtcbiAgICAgIGF3YXJlbmVzcy5zZXRMb2NhbFN0YXRlRmllbGQoJ3VzZXInLCB7IC4uLmN1cnJlbnRVc2VyLnRvSlNPTigpLCBuYW1lIH0pO1xuICAgIH07XG4gICAgaWYgKGN1cnJlbnRVc2VyLmlzUmVhZHkpIHtcbiAgICAgIHVzZXJDaGFuZ2VkKCk7XG4gICAgfVxuICAgIGN1cnJlbnRVc2VyLnJlYWR5LmNvbm5lY3QodXNlckNoYW5nZWQpO1xuICAgIGN1cnJlbnRVc2VyLmNoYW5nZWQuY29ubmVjdCh1c2VyQ2hhbmdlZCk7XG5cbiAgICBzdGF0ZS5jaGFuZ2VkLmNvbm5lY3QoYXN5bmMgKCkgPT4ge1xuICAgICAgY29uc3QgZGF0YTogYW55ID0gYXdhaXQgc3RhdGUudG9KU09OKCk7XG4gICAgICBjb25zdCBjdXJyZW50ID0gZGF0YVsnbGF5b3V0LXJlc3RvcmVyOmRhdGEnXT8ubWFpbj8uY3VycmVudCB8fCAnJztcblxuICAgICAgaWYgKGN1cnJlbnQuc3RhcnRzV2l0aCgnZWRpdG9yJykgfHwgY3VycmVudC5zdGFydHNXaXRoKCdub3RlYm9vaycpKSB7XG4gICAgICAgIGF3YXJlbmVzcy5zZXRMb2NhbFN0YXRlRmllbGQoJ2N1cnJlbnQnLCBjdXJyZW50KTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGF3YXJlbmVzcy5zZXRMb2NhbFN0YXRlRmllbGQoJ2N1cnJlbnQnLCBudWxsKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHJldHVybiBhd2FyZW5lc3M7XG4gIH1cbn07XG5cbi8qKlxuICogSnVweXRlciBwbHVnaW4gYWRkaW5nIHRoZSBSVEMgaW5mb3JtYXRpb24gdG8gdGhlIGFwcGxpY2F0aW9uIGxlZnQgcGFuZWwgaWYgY29sbGFib3JhdGl2ZSBmbGFnIGVuYWJsZWQuXG4gKi9cbmNvbnN0IHJ0Y1BhbmVsUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbi1leHRlbnNpb246cnRjUGFuZWwnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUN1cnJlbnRVc2VyLCBJR2xvYmFsQXdhcmVuZXNzLCBJVHJhbnNsYXRvcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgY3VycmVudFVzZXI6IFVzZXIsXG4gICAgYXdhcmVuZXNzOiBBd2FyZW5lc3MsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3JcbiAgKTogdm9pZCA9PiB7XG4gICAgaWYgKFBhZ2VDb25maWcuZ2V0T3B0aW9uKCdjb2xsYWJvcmF0aXZlJykgIT09ICd0cnVlJykge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICBjb25zdCB1c2VyUGFuZWwgPSBuZXcgU2lkZVBhbmVsKCk7XG4gICAgdXNlclBhbmVsLmlkID0gRE9NVXRpbHMuY3JlYXRlRG9tSUQoKTtcbiAgICB1c2VyUGFuZWwudGl0bGUuaWNvbiA9IHVzZXJzSWNvbjtcbiAgICB1c2VyUGFuZWwuYWRkQ2xhc3MoJ2pwLVJUQ1BhbmVsJyk7XG4gICAgYXBwLnNoZWxsLmFkZCh1c2VyUGFuZWwsICdsZWZ0JywgeyByYW5rOiAzMDAgfSk7XG5cbiAgICBjb25zdCBjdXJyZW50VXNlclBhbmVsID0gbmV3IFVzZXJJbmZvUGFuZWwoY3VycmVudFVzZXIpO1xuICAgIGN1cnJlbnRVc2VyUGFuZWwudGl0bGUubGFiZWwgPSB0cmFucy5fXygnVXNlciBpbmZvJyk7XG4gICAgY3VycmVudFVzZXJQYW5lbC50aXRsZS5jYXB0aW9uID0gdHJhbnMuX18oJ1VzZXIgaW5mb3JtYXRpb24nKTtcbiAgICB1c2VyUGFuZWwuYWRkV2lkZ2V0KGN1cnJlbnRVc2VyUGFuZWwpO1xuXG4gICAgY29uc3QgZmlsZW9wZW5lciA9IChwYXRoOiBzdHJpbmcpID0+IHtcbiAgICAgIHZvaWQgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6b3BlbicsIHsgcGF0aCB9KTtcbiAgICB9O1xuXG4gICAgY29uc3QgY29sbGFib3JhdG9yc1BhbmVsID0gbmV3IENvbGxhYm9yYXRvcnNQYW5lbChcbiAgICAgIGN1cnJlbnRVc2VyLFxuICAgICAgYXdhcmVuZXNzLFxuICAgICAgZmlsZW9wZW5lclxuICAgICk7XG4gICAgY29sbGFib3JhdG9yc1BhbmVsLnRpdGxlLmxhYmVsID0gdHJhbnMuX18oJ09ubGluZSBDb2xsYWJvcmF0b3JzJyk7XG4gICAgdXNlclBhbmVsLmFkZFdpZGdldChjb2xsYWJvcmF0b3JzUGFuZWwpO1xuICB9XG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2lucyBhcyBkZWZhdWx0LlxuICovXG5jb25zdCBwbHVnaW5zOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48YW55PltdID0gW1xuICB1c2VyUGx1Z2luLFxuICB1c2VyTWVudVBsdWdpbixcbiAgbWVudUJhclBsdWdpbixcbiAgcnRjR2xvYmFsQXdhcmVuZXNzUGx1Z2luLFxuICBydGNQYW5lbFBsdWdpblxuXTtcblxuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==