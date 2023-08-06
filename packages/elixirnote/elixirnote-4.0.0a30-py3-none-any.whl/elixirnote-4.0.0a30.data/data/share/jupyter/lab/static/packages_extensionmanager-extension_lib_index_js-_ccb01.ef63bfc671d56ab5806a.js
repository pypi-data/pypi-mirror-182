"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_extensionmanager-extension_lib_index_js-_ccb01"],{

/***/ "../../packages/extensionmanager-extension/lib/index.js":
/*!**************************************************************!*\
  !*** ../../packages/extensionmanager-extension/lib/index.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_extensionmanager__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/extensionmanager */ "webpack/sharing/consume/default/@jupyterlab/extensionmanager/@jupyterlab/extensionmanager");
/* harmony import */ var _jupyterlab_extensionmanager__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_extensionmanager__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module extensionmanager-extension
 */






const PLUGIN_ID = '@jupyterlab/extensionmanager-extension:plugin';
/**
 * IDs of the commands added by this extension.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.showPanel = 'extensionmanager:show-panel';
    CommandIDs.toggle = 'extensionmanager:toggle';
})(CommandIDs || (CommandIDs = {}));
/**
 * The extension manager plugin.
 */
const plugin = {
    id: PLUGIN_ID,
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: async (app, registry, translator, labShell, restorer, palette) => {
        const trans = translator.load('jupyterlab');
        const settings = await registry.load(plugin.id);
        let enabled = settings.composite['enabled'] === true;
        const { commands, serviceManager } = app;
        let view;
        const createView = () => {
            const v = new _jupyterlab_extensionmanager__WEBPACK_IMPORTED_MODULE_2__.ExtensionView(app, serviceManager, settings, translator);
            v.id = 'extensionmanager.main-view';
            v.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.extensionIcon;
            v.title.caption = trans.__('Extension Manager');
            if (restorer) {
                restorer.add(v, v.id);
            }
            return v;
        };
        if (enabled && labShell) {
            view = createView();
            view.node.setAttribute('role', 'region');
            view.node.setAttribute('aria-label', trans.__('Extension Manager section'));
            labShell.add(view, 'left', { rank: 1000, type: 'Extension Manager' });
        }
        // If the extension is enabled or disabled,
        // add or remove it from the left area.
        Promise.all([app.restored, registry.load(PLUGIN_ID)])
            .then(([, settings]) => {
            settings.changed.connect(async () => {
                enabled = settings.composite['enabled'] === true;
                if (enabled && !(view === null || view === void 0 ? void 0 : view.isAttached)) {
                    const accepted = await Private.showWarning(trans);
                    if (!accepted) {
                        void settings.set('enabled', false);
                        return;
                    }
                    view = view || createView();
                    view.node.setAttribute('role', 'region');
                    view.node.setAttribute('aria-label', trans.__('Extension Manager section'));
                    if (labShell) {
                        labShell.add(view, 'left', {
                            rank: 1000,
                            type: 'Extension Manager'
                        });
                    }
                }
                else if (!enabled && (view === null || view === void 0 ? void 0 : view.isAttached)) {
                    app.commands.notifyCommandChanged(CommandIDs.toggle);
                    view.close();
                }
            });
        })
            .catch(reason => {
            console.error(`Something went wrong when reading the settings.\n${reason}`);
        });
        commands.addCommand(CommandIDs.showPanel, {
            label: trans.__('Extension Manager'),
            execute: () => {
                if (view) {
                    labShell === null || labShell === void 0 ? void 0 : labShell.activateById(view.id);
                }
            },
            isVisible: () => enabled && labShell !== null
        });
        commands.addCommand(CommandIDs.toggle, {
            label: trans.__('Enable Extension Manager'),
            execute: () => {
                if (registry) {
                    void registry.set(plugin.id, 'enabled', !enabled);
                }
            },
            isToggled: () => enabled,
            isEnabled: () => serviceManager.builder.isAvailable
        });
        const category = trans.__('Extension Manager');
        const command = CommandIDs.toggle;
        if (palette) {
            palette.addItem({ command, category });
        }
    }
};
/**
 * Export the plugin as the default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * A namespace for module-private functions.
 */
var Private;
(function (Private) {
    /**
     * Show a warning dialog about extension security.
     *
     * @returns whether the user accepted the dialog.
     */
    async function showWarning(trans) {
        return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
            title: trans.__('Enable Extension Manager?'),
            body: trans.__(`Thanks for trying out JupyterLab's extension manager.
The JupyterLab development team is excited to have a robust
third-party extension community.
However, we cannot vouch for every extension,
and some may introduce security risks.
Do you want to continue?`),
            buttons: [
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton({ label: trans.__('Disable') }),
                _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton({ label: trans.__('Enable') })
            ]
        }).then(result => {
            return result.button.accept;
        });
    }
    Private.showWarning = showWarning;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZXh0ZW5zaW9ubWFuYWdlci1leHRlbnNpb25fbGliX2luZGV4X2pzLV9jY2IwMS5lZjYzYmZjNjcxZDU2YWI1ODA2YS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFPOEI7QUFDMEM7QUFDZDtBQUNFO0FBQ1U7QUFDZjtBQUUxRCxNQUFNLFNBQVMsR0FBRywrQ0FBK0MsQ0FBQztBQUVsRTs7R0FFRztBQUNILElBQVUsVUFBVSxDQUduQjtBQUhELFdBQVUsVUFBVTtJQUNMLG9CQUFTLEdBQUcsNkJBQTZCLENBQUM7SUFDMUMsaUJBQU0sR0FBRyx5QkFBeUIsQ0FBQztBQUNsRCxDQUFDLEVBSFMsVUFBVSxLQUFWLFVBQVUsUUFHbkI7QUFFRDs7R0FFRztBQUNILE1BQU0sTUFBTSxHQUFnQztJQUMxQyxFQUFFLEVBQUUsU0FBUztJQUNiLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMseUVBQWdCLEVBQUUsZ0VBQVcsQ0FBQztJQUN6QyxRQUFRLEVBQUUsQ0FBQyw4REFBUyxFQUFFLG9FQUFlLEVBQUUsaUVBQWUsQ0FBQztJQUN2RCxRQUFRLEVBQUUsS0FBSyxFQUNiLEdBQW9CLEVBQ3BCLFFBQTBCLEVBQzFCLFVBQXVCLEVBQ3ZCLFFBQTBCLEVBQzFCLFFBQWdDLEVBQ2hDLE9BQStCLEVBQy9CLEVBQUU7UUFDRixNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO1FBQzVDLE1BQU0sUUFBUSxHQUFHLE1BQU0sUUFBUSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsRUFBRSxDQUFDLENBQUM7UUFDaEQsSUFBSSxPQUFPLEdBQUcsUUFBUSxDQUFDLFNBQVMsQ0FBQyxTQUFTLENBQUMsS0FBSyxJQUFJLENBQUM7UUFFckQsTUFBTSxFQUFFLFFBQVEsRUFBRSxjQUFjLEVBQUUsR0FBRyxHQUFHLENBQUM7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QUUsQ0FBQyxDQUFDO1NBQ3hDO0lBQ0gsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILGlFQUFlLE1BQU0sRUFBQztBQUV0Qjs7R0FFRztBQUNILElBQVUsT0FBTyxDQXlCaEI7QUF6QkQsV0FBVSxPQUFPO0lBQ2Y7Ozs7T0FJRztJQUNJLEtBQUssVUFBVSxXQUFXLENBQy9CLEtBQXdCO1FBRXhCLE9BQU8sZ0VBQVUsQ0FBQztZQUNoQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQywyQkFBMkIsQ0FBQztZQUM1QyxJQUFJLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQzs7Ozs7eUJBS0ksQ0FBQztZQUNwQixPQUFPLEVBQUU7Z0JBQ1AscUVBQW1CLENBQUMsRUFBRSxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxTQUFTLENBQUMsRUFBRSxDQUFDO2dCQUNuRCxtRUFBaUIsQ0FBQyxFQUFFLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLFFBQVEsQ0FBQyxFQUFFLENBQUM7YUFDakQ7U0FDRixDQUFDLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxFQUFFO1lBQ2YsT0FBTyxNQUFNLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQztRQUM5QixDQUFDLENBQUMsQ0FBQztJQUNMLENBQUM7SUFsQnFCLG1CQUFXLGNBa0JoQztBQUNILENBQUMsRUF6QlMsT0FBTyxLQUFQLE9BQU8sUUF5QmhCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2V4dGVuc2lvbm1hbmFnZXItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBleHRlbnNpb25tYW5hZ2VyLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYWJTaGVsbCxcbiAgSUxheW91dFJlc3RvcmVyLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBEaWFsb2csIElDb21tYW5kUGFsZXR0ZSwgc2hvd0RpYWxvZyB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IEV4dGVuc2lvblZpZXcgfSBmcm9tICdAanVweXRlcmxhYi9leHRlbnNpb25tYW5hZ2VyJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIFRyYW5zbGF0aW9uQnVuZGxlIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgZXh0ZW5zaW9uSWNvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuXG5jb25zdCBQTFVHSU5fSUQgPSAnQGp1cHl0ZXJsYWIvZXh0ZW5zaW9ubWFuYWdlci1leHRlbnNpb246cGx1Z2luJztcblxuLyoqXG4gKiBJRHMgb2YgdGhlIGNvbW1hbmRzIGFkZGVkIGJ5IHRoaXMgZXh0ZW5zaW9uLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBzaG93UGFuZWwgPSAnZXh0ZW5zaW9ubWFuYWdlcjpzaG93LXBhbmVsJztcbiAgZXhwb3J0IGNvbnN0IHRvZ2dsZSA9ICdleHRlbnNpb25tYW5hZ2VyOnRvZ2dsZSc7XG59XG5cbi8qKlxuICogVGhlIGV4dGVuc2lvbiBtYW5hZ2VyIHBsdWdpbi5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiBQTFVHSU5fSUQsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJU2V0dGluZ1JlZ2lzdHJ5LCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsLCBJTGF5b3V0UmVzdG9yZXIsIElDb21tYW5kUGFsZXR0ZV0sXG4gIGFjdGl2YXRlOiBhc3luYyAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgcmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gICAgcmVzdG9yZXI6IElMYXlvdXRSZXN0b3JlciB8IG51bGwsXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuICApID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHNldHRpbmdzID0gYXdhaXQgcmVnaXN0cnkubG9hZChwbHVnaW4uaWQpO1xuICAgIGxldCBlbmFibGVkID0gc2V0dGluZ3MuY29tcG9zaXRlWydlbmFibGVkJ10gPT09IHRydWU7XG5cbiAgICBjb25zdCB7IGNvbW1hbmRzLCBzZXJ2aWNlTWFuYWdlciB9ID0gYXBwO1xuICAgIGxldCB2aWV3OiBFeHRlbnNpb25WaWV3IHwgdW5kZWZpbmVkO1xuXG4gICAgY29uc3QgY3JlYXRlVmlldyA9ICgpID0+IHtcbiAgICAgIGNvbnN0IHYgPSBuZXcgRXh0ZW5zaW9uVmlldyhhcHAsIHNlcnZpY2VNYW5hZ2VyLCBzZXR0aW5ncywgdHJhbnNsYXRvcik7XG4gICAgICB2LmlkID0gJ2V4dGVuc2lvbm1hbmFnZXIubWFpbi12aWV3JztcbiAgICAgIHYudGl0bGUuaWNvbiA9IGV4dGVuc2lvbkljb247XG4gICAgICB2LnRpdGxlLmNhcHRpb24gPSB0cmFucy5fXygnRXh0ZW5zaW9uIE1hbmFnZXInKTtcbiAgICAgIGlmIChyZXN0b3Jlcikge1xuICAgICAgICByZXN0b3Jlci5hZGQodiwgdi5pZCk7XG4gICAgICB9XG4gICAgICByZXR1cm4gdjtcbiAgICB9O1xuXG4gICAgaWYgKGVuYWJsZWQgJiYgbGFiU2hlbGwpIHtcbiAgICAgIHZpZXcgPSBjcmVhdGVWaWV3KCk7XG4gICAgICB2aWV3Lm5vZGUuc2V0QXR0cmlidXRlKCdyb2xlJywgJ3JlZ2lvbicpO1xuICAgICAgdmlldy5ub2RlLnNldEF0dHJpYnV0ZShcbiAgICAgICAgJ2FyaWEtbGFiZWwnLFxuICAgICAgICB0cmFucy5fXygnRXh0ZW5zaW9uIE1hbmFnZXIgc2VjdGlvbicpXG4gICAgICApO1xuICAgICAgbGFiU2hlbGwuYWRkKHZpZXcsICdsZWZ0JywgeyByYW5rOiAxMDAwLCB0eXBlOiAnRXh0ZW5zaW9uIE1hbmFnZXInIH0pO1xuICAgIH1cblxuICAgIC8vIElmIHRoZSBleHRlbnNpb24gaXMgZW5hYmxlZCBvciBkaXNhYmxlZCxcbiAgICAvLyBhZGQgb3IgcmVtb3ZlIGl0IGZyb20gdGhlIGxlZnQgYXJlYS5cbiAgICBQcm9taXNlLmFsbChbYXBwLnJlc3RvcmVkLCByZWdpc3RyeS5sb2FkKFBMVUdJTl9JRCldKVxuICAgICAgLnRoZW4oKFssIHNldHRpbmdzXSkgPT4ge1xuICAgICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoYXN5bmMgKCkgPT4ge1xuICAgICAgICAgIGVuYWJsZWQgPSBzZXR0aW5ncy5jb21wb3NpdGVbJ2VuYWJsZWQnXSA9PT0gdHJ1ZTtcbiAgICAgICAgICBpZiAoZW5hYmxlZCAmJiAhdmlldz8uaXNBdHRhY2hlZCkge1xuICAgICAgICAgICAgY29uc3QgYWNjZXB0ZWQgPSBhd2FpdCBQcml2YXRlLnNob3dXYXJuaW5nKHRyYW5zKTtcbiAgICAgICAgICAgIGlmICghYWNjZXB0ZWQpIHtcbiAgICAgICAgICAgICAgdm9pZCBzZXR0aW5ncy5zZXQoJ2VuYWJsZWQnLCBmYWxzZSk7XG4gICAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHZpZXcgPSB2aWV3IHx8IGNyZWF0ZVZpZXcoKTtcbiAgICAgICAgICAgIHZpZXcubm9kZS5zZXRBdHRyaWJ1dGUoJ3JvbGUnLCAncmVnaW9uJyk7XG4gICAgICAgICAgICB2aWV3Lm5vZGUuc2V0QXR0cmlidXRlKFxuICAgICAgICAgICAgICAnYXJpYS1sYWJlbCcsXG4gICAgICAgICAgICAgIHRyYW5zLl9fKCdFeHRlbnNpb24gTWFuYWdlciBzZWN0aW9uJylcbiAgICAgICAgICAgICk7XG4gICAgICAgICAgICBpZiAobGFiU2hlbGwpIHtcbiAgICAgICAgICAgICAgbGFiU2hlbGwuYWRkKHZpZXcsICdsZWZ0Jywge1xuICAgICAgICAgICAgICAgIHJhbms6IDEwMDAsXG4gICAgICAgICAgICAgICAgdHlwZTogJ0V4dGVuc2lvbiBNYW5hZ2VyJ1xuICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9IGVsc2UgaWYgKCFlbmFibGVkICYmIHZpZXc/LmlzQXR0YWNoZWQpIHtcbiAgICAgICAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZChDb21tYW5kSURzLnRvZ2dsZSk7XG4gICAgICAgICAgICB2aWV3LmNsb3NlKCk7XG4gICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihcbiAgICAgICAgICBgU29tZXRoaW5nIHdlbnQgd3Jvbmcgd2hlbiByZWFkaW5nIHRoZSBzZXR0aW5ncy5cXG4ke3JlYXNvbn1gXG4gICAgICAgICk7XG4gICAgICB9KTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zaG93UGFuZWwsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnRXh0ZW5zaW9uIE1hbmFnZXInKSxcbiAgICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgICAgaWYgKHZpZXcpIHtcbiAgICAgICAgICBsYWJTaGVsbD8uYWN0aXZhdGVCeUlkKHZpZXcuaWQpO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgaXNWaXNpYmxlOiAoKSA9PiBlbmFibGVkICYmIGxhYlNoZWxsICE9PSBudWxsXG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMudG9nZ2xlLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0VuYWJsZSBFeHRlbnNpb24gTWFuYWdlcicpLFxuICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICBpZiAocmVnaXN0cnkpIHtcbiAgICAgICAgICB2b2lkIHJlZ2lzdHJ5LnNldChwbHVnaW4uaWQsICdlbmFibGVkJywgIWVuYWJsZWQpO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgaXNUb2dnbGVkOiAoKSA9PiBlbmFibGVkLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBzZXJ2aWNlTWFuYWdlci5idWlsZGVyLmlzQXZhaWxhYmxlXG4gICAgfSk7XG5cbiAgICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdFeHRlbnNpb24gTWFuYWdlcicpO1xuICAgIGNvbnN0IGNvbW1hbmQgPSBDb21tYW5kSURzLnRvZ2dsZTtcbiAgICBpZiAocGFsZXR0ZSkge1xuICAgICAgcGFsZXR0ZS5hZGRJdGVtKHsgY29tbWFuZCwgY2F0ZWdvcnkgfSk7XG4gICAgfVxuICB9XG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2luIGFzIHRoZSBkZWZhdWx0LlxuICovXG5leHBvcnQgZGVmYXVsdCBwbHVnaW47XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIG1vZHVsZS1wcml2YXRlIGZ1bmN0aW9ucy5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogU2hvdyBhIHdhcm5pbmcgZGlhbG9nIGFib3V0IGV4dGVuc2lvbiBzZWN1cml0eS5cbiAgICpcbiAgICogQHJldHVybnMgd2hldGhlciB0aGUgdXNlciBhY2NlcHRlZCB0aGUgZGlhbG9nLlxuICAgKi9cbiAgZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIHNob3dXYXJuaW5nKFxuICAgIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZVxuICApOiBQcm9taXNlPGJvb2xlYW4+IHtcbiAgICByZXR1cm4gc2hvd0RpYWxvZyh7XG4gICAgICB0aXRsZTogdHJhbnMuX18oJ0VuYWJsZSBFeHRlbnNpb24gTWFuYWdlcj8nKSxcbiAgICAgIGJvZHk6IHRyYW5zLl9fKGBUaGFua3MgZm9yIHRyeWluZyBvdXQgSnVweXRlckxhYidzIGV4dGVuc2lvbiBtYW5hZ2VyLlxuVGhlIEp1cHl0ZXJMYWIgZGV2ZWxvcG1lbnQgdGVhbSBpcyBleGNpdGVkIHRvIGhhdmUgYSByb2J1c3RcbnRoaXJkLXBhcnR5IGV4dGVuc2lvbiBjb21tdW5pdHkuXG5Ib3dldmVyLCB3ZSBjYW5ub3Qgdm91Y2ggZm9yIGV2ZXJ5IGV4dGVuc2lvbixcbmFuZCBzb21lIG1heSBpbnRyb2R1Y2Ugc2VjdXJpdHkgcmlza3MuXG5EbyB5b3Ugd2FudCB0byBjb250aW51ZT9gKSxcbiAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgRGlhbG9nLmNhbmNlbEJ1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnRGlzYWJsZScpIH0pLFxuICAgICAgICBEaWFsb2cud2FybkJ1dHRvbih7IGxhYmVsOiB0cmFucy5fXygnRW5hYmxlJykgfSlcbiAgICAgIF1cbiAgICB9KS50aGVuKHJlc3VsdCA9PiB7XG4gICAgICByZXR1cm4gcmVzdWx0LmJ1dHRvbi5hY2NlcHQ7XG4gICAgfSk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==