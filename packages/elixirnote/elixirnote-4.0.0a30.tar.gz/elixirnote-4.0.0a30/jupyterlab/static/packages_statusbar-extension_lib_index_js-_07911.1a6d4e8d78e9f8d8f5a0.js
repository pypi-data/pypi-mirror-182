"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_statusbar-extension_lib_index_js-_07911"],{

/***/ "../../packages/statusbar-extension/lib/index.js":
/*!*******************************************************!*\
  !*** ../../packages/statusbar-extension/lib/index.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "STATUSBAR_PLUGIN_ID": () => (/* binding */ STATUSBAR_PLUGIN_ID),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module statusbar-extension
 */





const STATUSBAR_PLUGIN_ID = '@jupyterlab/statusbar-extension:plugin';
/**
 * Initialization data for the statusbar extension.
 */
const statusBar = {
    id: STATUSBAR_PLUGIN_ID,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    provides: _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__.IStatusBar,
    autoStart: true,
    activate: (app, translator, labShell, settingRegistry, palette) => {
        const trans = translator.load('jupyterlab');
        const statusBar = new _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_3__.StatusBar();
        statusBar.id = 'jp-main-statusbar';
        app.shell.add(statusBar, 'bottom');
        // If available, connect to the shell's layout modified signal.
        if (labShell) {
            labShell.layoutModified.connect(() => {
                statusBar.update();
            });
        }
        const category = trans.__('Main Area');
        const command = 'statusbar:toggle';
        app.commands.addCommand(command, {
            label: trans.__('Show Status Bar'),
            execute: () => {
                statusBar.setHidden(statusBar.isVisible);
                if (settingRegistry) {
                    void settingRegistry.set(STATUSBAR_PLUGIN_ID, 'visible', statusBar.isVisible);
                }
            },
            isToggled: () => statusBar.isVisible
        });
        app.commands.commandExecuted.connect((registry, executed) => {
            if (executed.id === 'application:reset-layout' && !statusBar.isVisible) {
                app.commands.execute(command).catch(reason => {
                    console.error('Failed to show the status bar.', reason);
                });
            }
        });
        if (palette) {
            palette.addItem({ command, category });
        }
        if (settingRegistry) {
            const loadSettings = settingRegistry.load(STATUSBAR_PLUGIN_ID);
            const updateSettings = (settings) => {
                const visible = settings.get('visible').composite;
                statusBar.setHidden(!visible);
            };
            Promise.all([loadSettings, app.restored])
                .then(([settings]) => {
                updateSettings(settings);
                settings.changed.connect(settings => {
                    updateSettings(settings);
                });
            })
                .catch((reason) => {
                console.error(reason.message);
            });
        }
        return statusBar;
    },
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette]
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (statusBar);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfc3RhdHVzYmFyLWV4dGVuc2lvbl9saWJfaW5kZXhfanMtXzA3OTExLjFhNmQ0ZThkNzhlOWY4ZDhmNWEwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTThCO0FBQ3NCO0FBQ1E7QUFDRDtBQUNSO0FBRS9DLE1BQU0sbUJBQW1CLEdBQUcsd0NBQXdDLENBQUM7QUFFNUU7O0dBRUc7QUFDSCxNQUFNLFNBQVMsR0FBc0M7SUFDbkQsRUFBRSxFQUFFLG1CQUFtQjtJQUN2QixRQUFRLEVBQUUsQ0FBQyxnRUFBVyxDQUFDO0lBQ3ZCLFFBQVEsRUFBRSw2REFBVTtJQUNwQixTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQXVCLEVBQ3ZCLFFBQTBCLEVBQzFCLGVBQXdDLEVBQ3hDLE9BQStCLEVBQy9CLEVBQUU7UUFDRixNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBQzVDLE1BQU0sU0FBUyxHQUFHLElBQUksNERBQVMsRUFBRSxDQUFDO1FBQ2xDLFNBQVMsQ0FBQyxFQUFFLEdBQUcsbUJBQW1CLENBQUM7UUFDbkMsR0FBRyxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsU0FBUyxFQUFFLFFBQVEsQ0FBQyxDQUFDO1FBRW5DLCtEQUErRDtRQUMvRCxJQUFJLFFBQVEsRUFBRTtZQUNaLFFBQVEsQ0FBQyxjQUFjLENBQUMsT0FBTyxDQUFDLEdBQUcsRUFBRTtnQkFDbkMsU0FBUyxDQUFDLE1BQU0sRUFBRSxDQUFDO1lBQ3JCLENBQUMsQ0FBQyxDQUFDO1NBQ0o7UUFFRCxNQUFNLFFBQVEsR0FBVyxLQUFLLENBQUMsRUFBRSxDQUFDLFdBQVcsQ0FBQyxDQUFDO1FBQy9DLE1BQU0sT0FBTyxHQUFXLGtCQUFrQixDQUFDO1FBRTNDLEdBQUcsQ0FBQyxRQUFRLENBQUMsVUFBVSxDQUFDLE9BQU8sRUFBRTtZQUMvQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxpQkFBaUIsQ0FBQztZQUNsQyxPQUFPLEVBQUUsR0FBRyxFQUFFO2dCQUNaLFNBQVMsQ0FBQyxTQUFTLENBQUMsU0FBUyxDQUFDLFNBQVMsQ0FBQyxDQUFDO2dCQUN6QyxJQUFJLGVBQWUsRUFBRTtvQkFDbkIsS0FBSyxlQUFlLENBQUMsR0FBRyxDQUN0QixtQkFBbUIsRUFDbkIsU0FBUyxFQUNULFNBQVMsQ0FBQyxTQUFTLENBQ3BCLENBQUM7aUJBQ0g7WUFDSCxDQUFDO1lBQ0QsU0FBUyxFQUFFLEdBQUcsRUFBRSxDQUFDLFNBQVMsQ0FBQyxTQUFTO1NBQ3JDLENBQUMsQ0FBQztRQUVILEdBQUcsQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLE9BQU8sQ0FBQyxDQUFDLFFBQVEsRUFBRSxRQUFRLEVBQUUsRUFBRTtZQUMxRCxJQUFJLFFBQVEsQ0FBQyxFQUFFLEtBQUssMEJBQTBCLElBQUksQ0FBQyxTQUFTLENBQUMsU0FBUyxFQUFFO2dCQUN0RSxHQUFHLENBQUMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUMsQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLEVBQUU7b0JBQzNDLE9BQU8sQ0FBQyxLQUFLLENBQUMsZ0NBQWdDLEVBQUUsTUFBTSxDQUFDLENBQUM7Z0JBQzFELENBQUMsQ0FBQyxDQUFDO2FBQ0o7UUFDSCxDQUFDLENBQUMsQ0FBQztRQUVILElBQUksT0FBTyxFQUFFO1lBQ1gsT0FBTyxDQUFDLE9BQU8sQ0FBQyxFQUFFLE9BQU8sRUFBRSxRQUFRLEVBQUUsQ0FBQyxDQUFDO1NBQ3hDO1FBRUQsSUFBSSxlQUFlLEVBQUU7WUFDbkIsTUFBTSxZQUFZLEdBQUcsZUFBZSxDQUFDLElBQUksQ0FBQyxtQkFBbUIsQ0FBQyxDQUFDO1lBQy9ELE1BQU0sY0FBYyxHQUFHLENBQUMsUUFBb0MsRUFBUSxFQUFFO2dCQUNwRSxNQUFNLE9BQU8sR0FBRyxRQUFRLENBQUMsR0FBRyxDQUFDLFNBQVMsQ0FBQyxDQUFDLFNBQW9CLENBQUM7Z0JBQzdELFNBQVMsQ0FBQyxTQUFTLENBQUMsQ0FBQyxPQUFPLENBQUMsQ0FBQztZQUNoQyxDQUFDLENBQUM7WUFFRixPQUFPLENBQUMsR0FBRyxDQUFDLENBQUMsWUFBWSxFQUFFLEdBQUcsQ0FBQyxRQUFRLENBQUMsQ0FBQztpQkFDdEMsSUFBSSxDQUFDLENBQUMsQ0FBQyxRQUFRLENBQUMsRUFBRSxFQUFFO2dCQUNuQixjQUFjLENBQUMsUUFBUSxDQUFDLENBQUM7Z0JBQ3pCLFFBQVEsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBQyxFQUFFO29CQUNsQyxjQUFjLENBQUMsUUFBUSxDQUFDLENBQUM7Z0JBQzNCLENBQUMsQ0FBQyxDQUFDO1lBQ0wsQ0FBQyxDQUFDO2lCQUNELEtBQUssQ0FBQyxDQUFDLE1BQWEsRUFBRSxFQUFFO2dCQUN2QixPQUFPLENBQUMsS0FBSyxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsQ0FBQztZQUNoQyxDQUFDLENBQUMsQ0FBQztTQUNOO1FBRUQsT0FBTyxTQUFTLENBQUM7SUFDbkIsQ0FBQztJQUNELFFBQVEsRUFBRSxDQUFDLDhEQUFTLEVBQUUseUVBQWdCLEVBQUUsaUVBQWUsQ0FBQztDQUN6RCxDQUFDO0FBRUYsaUVBQWUsU0FBUyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3N0YXR1c2Jhci1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHN0YXR1c2Jhci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGFiU2hlbGwsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IElDb21tYW5kUGFsZXR0ZSB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVN0YXR1c0JhciwgU3RhdHVzQmFyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdHVzYmFyJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG5leHBvcnQgY29uc3QgU1RBVFVTQkFSX1BMVUdJTl9JRCA9ICdAanVweXRlcmxhYi9zdGF0dXNiYXItZXh0ZW5zaW9uOnBsdWdpbic7XG5cbi8qKlxuICogSW5pdGlhbGl6YXRpb24gZGF0YSBmb3IgdGhlIHN0YXR1c2JhciBleHRlbnNpb24uXG4gKi9cbmNvbnN0IHN0YXR1c0JhcjogSnVweXRlckZyb250RW5kUGx1Z2luPElTdGF0dXNCYXI+ID0ge1xuICBpZDogU1RBVFVTQkFSX1BMVUdJTl9JRCxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIHByb3ZpZGVzOiBJU3RhdHVzQmFyLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gICAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5IHwgbnVsbCxcbiAgICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3Qgc3RhdHVzQmFyID0gbmV3IFN0YXR1c0JhcigpO1xuICAgIHN0YXR1c0Jhci5pZCA9ICdqcC1tYWluLXN0YXR1c2Jhcic7XG4gICAgYXBwLnNoZWxsLmFkZChzdGF0dXNCYXIsICdib3R0b20nKTtcblxuICAgIC8vIElmIGF2YWlsYWJsZSwgY29ubmVjdCB0byB0aGUgc2hlbGwncyBsYXlvdXQgbW9kaWZpZWQgc2lnbmFsLlxuICAgIGlmIChsYWJTaGVsbCkge1xuICAgICAgbGFiU2hlbGwubGF5b3V0TW9kaWZpZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICAgIHN0YXR1c0Jhci51cGRhdGUoKTtcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIGNvbnN0IGNhdGVnb3J5OiBzdHJpbmcgPSB0cmFucy5fXygnTWFpbiBBcmVhJyk7XG4gICAgY29uc3QgY29tbWFuZDogc3RyaW5nID0gJ3N0YXR1c2Jhcjp0b2dnbGUnO1xuXG4gICAgYXBwLmNvbW1hbmRzLmFkZENvbW1hbmQoY29tbWFuZCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTaG93IFN0YXR1cyBCYXInKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgc3RhdHVzQmFyLnNldEhpZGRlbihzdGF0dXNCYXIuaXNWaXNpYmxlKTtcbiAgICAgICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgICAgIHZvaWQgc2V0dGluZ1JlZ2lzdHJ5LnNldChcbiAgICAgICAgICAgIFNUQVRVU0JBUl9QTFVHSU5fSUQsXG4gICAgICAgICAgICAndmlzaWJsZScsXG4gICAgICAgICAgICBzdGF0dXNCYXIuaXNWaXNpYmxlXG4gICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgfSxcbiAgICAgIGlzVG9nZ2xlZDogKCkgPT4gc3RhdHVzQmFyLmlzVmlzaWJsZVxuICAgIH0pO1xuXG4gICAgYXBwLmNvbW1hbmRzLmNvbW1hbmRFeGVjdXRlZC5jb25uZWN0KChyZWdpc3RyeSwgZXhlY3V0ZWQpID0+IHtcbiAgICAgIGlmIChleGVjdXRlZC5pZCA9PT0gJ2FwcGxpY2F0aW9uOnJlc2V0LWxheW91dCcgJiYgIXN0YXR1c0Jhci5pc1Zpc2libGUpIHtcbiAgICAgICAgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoY29tbWFuZCkuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gc2hvdyB0aGUgc3RhdHVzIGJhci4nLCByZWFzb24pO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oeyBjb21tYW5kLCBjYXRlZ29yeSB9KTtcbiAgICB9XG5cbiAgICBpZiAoc2V0dGluZ1JlZ2lzdHJ5KSB7XG4gICAgICBjb25zdCBsb2FkU2V0dGluZ3MgPSBzZXR0aW5nUmVnaXN0cnkubG9hZChTVEFUVVNCQVJfUExVR0lOX0lEKTtcbiAgICAgIGNvbnN0IHVwZGF0ZVNldHRpbmdzID0gKHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyk6IHZvaWQgPT4ge1xuICAgICAgICBjb25zdCB2aXNpYmxlID0gc2V0dGluZ3MuZ2V0KCd2aXNpYmxlJykuY29tcG9zaXRlIGFzIGJvb2xlYW47XG4gICAgICAgIHN0YXR1c0Jhci5zZXRIaWRkZW4oIXZpc2libGUpO1xuICAgICAgfTtcblxuICAgICAgUHJvbWlzZS5hbGwoW2xvYWRTZXR0aW5ncywgYXBwLnJlc3RvcmVkXSlcbiAgICAgICAgLnRoZW4oKFtzZXR0aW5nc10pID0+IHtcbiAgICAgICAgICB1cGRhdGVTZXR0aW5ncyhzZXR0aW5ncyk7XG4gICAgICAgICAgc2V0dGluZ3MuY2hhbmdlZC5jb25uZWN0KHNldHRpbmdzID0+IHtcbiAgICAgICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgICAgICB9KTtcbiAgICAgICAgfSlcbiAgICAgICAgLmNhdGNoKChyZWFzb246IEVycm9yKSA9PiB7XG4gICAgICAgICAgY29uc29sZS5lcnJvcihyZWFzb24ubWVzc2FnZSk7XG4gICAgICAgIH0pO1xuICAgIH1cblxuICAgIHJldHVybiBzdGF0dXNCYXI7XG4gIH0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsLCBJU2V0dGluZ1JlZ2lzdHJ5LCBJQ29tbWFuZFBhbGV0dGVdXG59O1xuXG5leHBvcnQgZGVmYXVsdCBzdGF0dXNCYXI7XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=