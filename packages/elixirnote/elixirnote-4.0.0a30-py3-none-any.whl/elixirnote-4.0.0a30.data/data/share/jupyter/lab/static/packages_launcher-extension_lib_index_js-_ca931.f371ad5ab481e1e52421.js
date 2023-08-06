"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_launcher-extension_lib_index_js-_ca931"],{

/***/ "../../packages/launcher-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/launcher-extension/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module launcher-extension
 */







/**
 * The command IDs used by the launcher plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.create = 'launcher:create';
})(CommandIDs || (CommandIDs = {}));
/**
 * A service providing an interface to the the launcher.
 */
const plugin = {
    activate,
    id: '@jupyterlab/launcher-extension:plugin',
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_2__.IFileBrowserFactory],
    provides: _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__.ILauncher,
    autoStart: true
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * Activate the launcher.
 */
function activate(app, translator, labShell, palette, factory) {
    const { commands, shell } = app;
    const trans = translator.load('jupyterlab');
    const model = new _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__.LauncherModel();
    commands.addCommand(CommandIDs.create, {
        label: trans.__('New Launcher'),
        icon: args => (args.toolbar ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.addIcon : undefined),
        execute: (args) => {
            var _a, _b;
            const cwd = (_b = (_a = args['cwd']) !== null && _a !== void 0 ? _a : factory === null || factory === void 0 ? void 0 : factory.defaultBrowser.model.path) !== null && _b !== void 0 ? _b : '';
            const id = `launcher-${Private.id++}`;
            const callback = (item) => {
                // If widget is attached to the main area replace the launcher
                if ((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__.find)(shell.widgets('main'), w => w === item)) {
                    shell.add(item, 'main', { ref: id });
                    launcher.dispose();
                }
            };
            const launcher = new _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_3__.Launcher({
                model,
                cwd,
                callback,
                commands,
                translator
            });
            launcher.model = model;
            launcher.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.launcherIcon;
            launcher.title.label = trans.__('Launcher');
            const main = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content: launcher });
            // If there are any other widgets open, remove the launcher close icon.
            main.title.closable = !!(0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__.toArray)(shell.widgets('main')).length;
            main.id = id;
            shell.add(main, 'main', {
                activate: args['activate'],
                ref: args['ref']
            });
            if (labShell) {
                labShell.layoutModified.connect(() => {
                    // If there is only a launcher open, remove the close icon.
                    main.title.closable = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_6__.toArray)(labShell.widgets('main')).length > 1;
                }, main);
            }
            if (factory) {
                const onPathChanged = (model) => {
                    launcher.cwd = model.path;
                };
                factory.defaultBrowser.model.pathChanged.connect(onPathChanged);
                launcher.disposed.connect(() => {
                    factory.defaultBrowser.model.pathChanged.disconnect(onPathChanged);
                });
            }
            return main;
        }
    });
    if (labShell) {
        void Promise.all([
            app.restored,
            factory === null || factory === void 0 ? void 0 : factory.defaultBrowser.model.restored
        ]).then(() => {
            function maybeCreate() {
                // Create a launcher if there are no open items.
                if (labShell.isEmpty('main')) {
                    void commands.execute(CommandIDs.create);
                }
            }
            maybeCreate();
            // When layout is modified, create a launcher if there are no open items.
            labShell.layoutModified.connect(() => {
                maybeCreate();
            });
        });
    }
    if (palette) {
        palette.addItem({
            command: CommandIDs.create,
            category: trans.__('Launcher')
        });
    }
    if (labShell) {
        labShell.addButtonEnabled = true;
        labShell.addRequested.connect((sender, arg) => {
            var _a;
            // Get the ref for the current tab of the tabbar which the add button was clicked
            const ref = ((_a = arg.currentTitle) === null || _a === void 0 ? void 0 : _a.owner.id) ||
                arg.titles[arg.titles.length - 1].owner.id;
            return commands.execute(CommandIDs.create, { ref });
        });
    }
    return model;
}
/**
 * The namespace for module private data.
 */
var Private;
(function (Private) {
    /**
     * The incrementing id used for launcher widgets.
     */
    Private.id = 0;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbGF1bmNoZXItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fY2E5MzEuZjM3MWFkNWFiNDgxZTFlNTI0MjEuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFNOEI7QUFDc0M7QUFDUztBQUNOO0FBQ3BCO0FBQ1k7QUFDaEI7QUFJbEQ7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0FFbkI7QUFGRCxXQUFVLFVBQVU7SUFDTCxpQkFBTSxHQUFHLGlCQUFpQixDQUFDO0FBQzFDLENBQUMsRUFGUyxVQUFVLEtBQVYsVUFBVSxRQUVuQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxNQUFNLEdBQXFDO0lBQy9DLFFBQVE7SUFDUixFQUFFLEVBQUUsdUNBQXVDO0lBQzNDLFFBQVEsRUFBRSxDQUFDLGdFQUFXLENBQUM7SUFDdkIsUUFBUSxFQUFFLENBQUMsOERBQVMsRUFBRSxpRUFBZSxFQUFFLHdFQUFtQixDQUFDO0lBQzNELFFBQVEsRUFBRSwyREFBUztJQUNuQixTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxpRUFBZSxNQUFNLEVBQUM7QUFFdEI7O0dBRUc7QUFDSCxTQUFTLFFBQVEsQ0FDZixHQUFvQixFQUNwQixVQUF1QixFQUN2QixRQUEwQixFQUMxQixPQUErQixFQUMvQixPQUFtQztJQUVuQyxNQUFNLEVBQUUsUUFBUSxFQUFFLEtBQUssRUFBRSxHQUFHLEdBQUcsQ0FBQztJQUNoQyxNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sS0FBSyxHQUFHLElBQUksK0RBQWEsRUFBRSxDQUFDO0lBRWxDLFFBQVEsQ0FBQyxVQUFVLENBQUMsVUFBVSxDQUFDLE1BQU0sRUFBRTtRQUNyQyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxjQUFjLENBQUM7UUFDL0IsSUFBSSxF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LENBQUMsQ0FBQyxLQUFLLENBQUMsRUFBRSxDQUFDO1lBRTdDLE9BQU8sUUFBUSxDQUFDLE9BQU8sQ0FBQyxVQUFVLENBQUMsTUFBTSxFQUFFLEVBQUUsR0FBRyxFQUFFLENBQUMsQ0FBQztRQUN0RCxDQUFDLENBQUMsQ0FBQztLQUNKO0lBRUQsT0FBTyxLQUFLLENBQUM7QUFDZixDQUFDO0FBRUQ7O0dBRUc7QUFDSCxJQUFVLE9BQU8sQ0FLaEI7QUFMRCxXQUFVLE9BQU87SUFDZjs7T0FFRztJQUNRLFVBQUUsR0FBRyxDQUFDLENBQUM7QUFDcEIsQ0FBQyxFQUxTLE9BQU8sS0FBUCxPQUFPLFFBS2hCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2xhdW5jaGVyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgbGF1bmNoZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBJQ29tbWFuZFBhbGV0dGUsIE1haW5BcmVhV2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgRmlsZUJyb3dzZXJNb2RlbCwgSUZpbGVCcm93c2VyRmFjdG9yeSB9IGZyb20gJ0BqdXB5dGVybGFiL2ZpbGVicm93c2VyJztcbmltcG9ydCB7IElMYXVuY2hlciwgTGF1bmNoZXIsIExhdW5jaGVyTW9kZWwgfSBmcm9tICdAanVweXRlcmxhYi9sYXVuY2hlcic7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGFkZEljb24sIGxhdW5jaGVySWNvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgZmluZCwgdG9BcnJheSB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IEpTT05PYmplY3QgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBEb2NrUGFuZWwsIFRhYkJhciwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgbGF1bmNoZXIgcGx1Z2luLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBjcmVhdGUgPSAnbGF1bmNoZXI6Y3JlYXRlJztcbn1cblxuLyoqXG4gKiBBIHNlcnZpY2UgcHJvdmlkaW5nIGFuIGludGVyZmFjZSB0byB0aGUgdGhlIGxhdW5jaGVyLlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJTGF1bmNoZXI+ID0ge1xuICBhY3RpdmF0ZSxcbiAgaWQ6ICdAanVweXRlcmxhYi9sYXVuY2hlci1leHRlbnNpb246cGx1Z2luJyxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsLCBJQ29tbWFuZFBhbGV0dGUsIElGaWxlQnJvd3NlckZhY3RvcnldLFxuICBwcm92aWRlczogSUxhdW5jaGVyLFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW4gYXMgZGVmYXVsdC5cbiAqL1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2luO1xuXG4vKipcbiAqIEFjdGl2YXRlIHRoZSBsYXVuY2hlci5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gIGZhY3Rvcnk6IElGaWxlQnJvd3NlckZhY3RvcnkgfCBudWxsXG4pOiBJTGF1bmNoZXIge1xuICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCBtb2RlbCA9IG5ldyBMYXVuY2hlck1vZGVsKCk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNyZWF0ZSwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnTmV3IExhdW5jaGVyJyksXG4gICAgaWNvbjogYXJncyA9PiAoYXJncy50b29sYmFyID8gYWRkSWNvbiA6IHVuZGVmaW5lZCksXG4gICAgZXhlY3V0ZTogKGFyZ3M6IEpTT05PYmplY3QpID0+IHtcbiAgICAgIGNvbnN0IGN3ZCA9XG4gICAgICAgIChhcmdzWydjd2QnXSBhcyBzdHJpbmcpID8/IGZhY3Rvcnk/LmRlZmF1bHRCcm93c2VyLm1vZGVsLnBhdGggPz8gJyc7XG4gICAgICBjb25zdCBpZCA9IGBsYXVuY2hlci0ke1ByaXZhdGUuaWQrK31gO1xuICAgICAgY29uc3QgY2FsbGJhY2sgPSAoaXRlbTogV2lkZ2V0KSA9PiB7XG4gICAgICAgIC8vIElmIHdpZGdldCBpcyBhdHRhY2hlZCB0byB0aGUgbWFpbiBhcmVhIHJlcGxhY2UgdGhlIGxhdW5jaGVyXG4gICAgICAgIGlmIChmaW5kKHNoZWxsLndpZGdldHMoJ21haW4nKSwgdyA9PiB3ID09PSBpdGVtKSkge1xuICAgICAgICAgIHNoZWxsLmFkZChpdGVtLCAnbWFpbicsIHsgcmVmOiBpZCB9KTtcbiAgICAgICAgICBsYXVuY2hlci5kaXNwb3NlKCk7XG4gICAgICAgIH1cbiAgICAgIH07XG4gICAgICBjb25zdCBsYXVuY2hlciA9IG5ldyBMYXVuY2hlcih7XG4gICAgICAgIG1vZGVsLFxuICAgICAgICBjd2QsXG4gICAgICAgIGNhbGxiYWNrLFxuICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgdHJhbnNsYXRvclxuICAgICAgfSk7XG5cbiAgICAgIGxhdW5jaGVyLm1vZGVsID0gbW9kZWw7XG4gICAgICBsYXVuY2hlci50aXRsZS5pY29uID0gbGF1bmNoZXJJY29uO1xuICAgICAgbGF1bmNoZXIudGl0bGUubGFiZWwgPSB0cmFucy5fXygnTGF1bmNoZXInKTtcblxuICAgICAgY29uc3QgbWFpbiA9IG5ldyBNYWluQXJlYVdpZGdldCh7IGNvbnRlbnQ6IGxhdW5jaGVyIH0pO1xuXG4gICAgICAvLyBJZiB0aGVyZSBhcmUgYW55IG90aGVyIHdpZGdldHMgb3BlbiwgcmVtb3ZlIHRoZSBsYXVuY2hlciBjbG9zZSBpY29uLlxuICAgICAgbWFpbi50aXRsZS5jbG9zYWJsZSA9ICEhdG9BcnJheShzaGVsbC53aWRnZXRzKCdtYWluJykpLmxlbmd0aDtcbiAgICAgIG1haW4uaWQgPSBpZDtcblxuICAgICAgc2hlbGwuYWRkKG1haW4sICdtYWluJywge1xuICAgICAgICBhY3RpdmF0ZTogYXJnc1snYWN0aXZhdGUnXSBhcyBib29sZWFuLFxuICAgICAgICByZWY6IGFyZ3NbJ3JlZiddIGFzIHN0cmluZ1xuICAgICAgfSk7XG5cbiAgICAgIGlmIChsYWJTaGVsbCkge1xuICAgICAgICBsYWJTaGVsbC5sYXlvdXRNb2RpZmllZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgICAvLyBJZiB0aGVyZSBpcyBvbmx5IGEgbGF1bmNoZXIgb3BlbiwgcmVtb3ZlIHRoZSBjbG9zZSBpY29uLlxuICAgICAgICAgIG1haW4udGl0bGUuY2xvc2FibGUgPSB0b0FycmF5KGxhYlNoZWxsLndpZGdldHMoJ21haW4nKSkubGVuZ3RoID4gMTtcbiAgICAgICAgfSwgbWFpbik7XG4gICAgICB9XG5cbiAgICAgIGlmIChmYWN0b3J5KSB7XG4gICAgICAgIGNvbnN0IG9uUGF0aENoYW5nZWQgPSAobW9kZWw6IEZpbGVCcm93c2VyTW9kZWwpID0+IHtcbiAgICAgICAgICBsYXVuY2hlci5jd2QgPSBtb2RlbC5wYXRoO1xuICAgICAgICB9O1xuICAgICAgICBmYWN0b3J5LmRlZmF1bHRCcm93c2VyLm1vZGVsLnBhdGhDaGFuZ2VkLmNvbm5lY3Qob25QYXRoQ2hhbmdlZCk7XG4gICAgICAgIGxhdW5jaGVyLmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICAgIGZhY3RvcnkuZGVmYXVsdEJyb3dzZXIubW9kZWwucGF0aENoYW5nZWQuZGlzY29ubmVjdChvblBhdGhDaGFuZ2VkKTtcbiAgICAgICAgfSk7XG4gICAgICB9XG5cbiAgICAgIHJldHVybiBtYWluO1xuICAgIH1cbiAgfSk7XG5cbiAgaWYgKGxhYlNoZWxsKSB7XG4gICAgdm9pZCBQcm9taXNlLmFsbChbXG4gICAgICBhcHAucmVzdG9yZWQsXG4gICAgICBmYWN0b3J5Py5kZWZhdWx0QnJvd3Nlci5tb2RlbC5yZXN0b3JlZFxuICAgIF0pLnRoZW4oKCkgPT4ge1xuICAgICAgZnVuY3Rpb24gbWF5YmVDcmVhdGUoKSB7XG4gICAgICAgIC8vIENyZWF0ZSBhIGxhdW5jaGVyIGlmIHRoZXJlIGFyZSBubyBvcGVuIGl0ZW1zLlxuICAgICAgICBpZiAobGFiU2hlbGwhLmlzRW1wdHkoJ21haW4nKSkge1xuICAgICAgICAgIHZvaWQgY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLmNyZWF0ZSk7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICAgIG1heWJlQ3JlYXRlKCk7XG4gICAgICAvLyBXaGVuIGxheW91dCBpcyBtb2RpZmllZCwgY3JlYXRlIGEgbGF1bmNoZXIgaWYgdGhlcmUgYXJlIG5vIG9wZW4gaXRlbXMuXG4gICAgICBsYWJTaGVsbC5sYXlvdXRNb2RpZmllZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgbWF5YmVDcmVhdGUoKTtcbiAgICAgIH0pO1xuICAgIH0pO1xuICB9XG5cbiAgaWYgKHBhbGV0dGUpIHtcbiAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5jcmVhdGUsXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ0xhdW5jaGVyJylcbiAgICB9KTtcbiAgfVxuXG4gIGlmIChsYWJTaGVsbCkge1xuICAgIGxhYlNoZWxsLmFkZEJ1dHRvbkVuYWJsZWQgPSB0cnVlO1xuICAgIGxhYlNoZWxsLmFkZFJlcXVlc3RlZC5jb25uZWN0KChzZW5kZXI6IERvY2tQYW5lbCwgYXJnOiBUYWJCYXI8V2lkZ2V0PikgPT4ge1xuICAgICAgLy8gR2V0IHRoZSByZWYgZm9yIHRoZSBjdXJyZW50IHRhYiBvZiB0aGUgdGFiYmFyIHdoaWNoIHRoZSBhZGQgYnV0dG9uIHdhcyBjbGlja2VkXG4gICAgICBjb25zdCByZWYgPVxuICAgICAgICBhcmcuY3VycmVudFRpdGxlPy5vd25lci5pZCB8fFxuICAgICAgICBhcmcudGl0bGVzW2FyZy50aXRsZXMubGVuZ3RoIC0gMV0ub3duZXIuaWQ7XG5cbiAgICAgIHJldHVybiBjb21tYW5kcy5leGVjdXRlKENvbW1hbmRJRHMuY3JlYXRlLCB7IHJlZiB9KTtcbiAgICB9KTtcbiAgfVxuXG4gIHJldHVybiBtb2RlbDtcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBtb2R1bGUgcHJpdmF0ZSBkYXRhLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBUaGUgaW5jcmVtZW50aW5nIGlkIHVzZWQgZm9yIGxhdW5jaGVyIHdpZGdldHMuXG4gICAqL1xuICBleHBvcnQgbGV0IGlkID0gMDtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==