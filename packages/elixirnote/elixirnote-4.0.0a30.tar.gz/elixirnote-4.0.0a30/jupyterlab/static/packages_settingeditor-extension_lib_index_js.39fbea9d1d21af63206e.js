"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_settingeditor-extension_lib_index_js"],{

/***/ "../../packages/settingeditor-extension/lib/index.js":
/*!***********************************************************!*\
  !*** ../../packages/settingeditor-extension/lib/index.js ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingeditor_lib_tokens__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/settingeditor/lib/tokens */ "../../packages/settingeditor/lib/tokens.js");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module settingeditor-extension
 */










/**
 * The command IDs used by the setting editor.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.open = 'settingeditor:open';
    CommandIDs.openJSON = 'settingeditor:open-json';
    CommandIDs.revert = 'settingeditor:revert';
    CommandIDs.save = 'settingeditor:save';
})(CommandIDs || (CommandIDs = {}));
/**
 * The default setting editor extension.
 */
const plugin = {
    id: '@jupyterlab/settingeditor-extension:form-ui',
    requires: [
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__.IStateDB,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator,
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.IFormComponentRegistry,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus
    ],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_settingeditor_lib_tokens__WEBPACK_IMPORTED_MODULE_8__.IJSONSettingEditorTracker],
    autoStart: true,
    provides: _jupyterlab_settingeditor_lib_tokens__WEBPACK_IMPORTED_MODULE_8__.ISettingEditorTracker,
    activate
};
/**
 * Activate the setting editor extension.
 */
function activate(app, registry, state, translator, editorRegistry, status, restorer, palette, jsonEditor) {
    const trans = translator.load('jupyterlab');
    const { commands, shell } = app;
    const namespace = 'setting-editor';
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace
    });
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: CommandIDs.open,
            args: widget => ({}),
            name: widget => namespace
        });
    }
    const openUi = async (args) => {
        if (tracker.currentWidget && !tracker.currentWidget.isDisposed) {
            if (!tracker.currentWidget.isAttached) {
                shell.add(tracker.currentWidget, 'main', { type: 'Settings' });
            }
            shell.activateById(tracker.currentWidget.id);
            return;
        }
        const key = plugin.id;
        const { SettingsEditor } = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_jupyterlab_settingeditor_jupyterlab_settingeditor").then(__webpack_require__.t.bind(__webpack_require__, /*! @jupyterlab/settingeditor */ "webpack/sharing/consume/default/@jupyterlab/settingeditor/@jupyterlab/settingeditor", 23));
        const editor = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
            content: new SettingsEditor({
                editorRegistry,
                key,
                registry,
                state,
                commands,
                toSkip: [
                    '@jupyterlab/application-extension:context-menu',
                    '@jupyterlab/mainmenu-extension:plugin'
                ],
                translator,
                status,
                query: args.query
            })
        });
        if (jsonEditor) {
            editor.toolbar.addItem('spacer', _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.Toolbar.createSpacerItem());
            editor.toolbar.addItem('open-json-editor', new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.CommandToolbarButton({
                commands,
                id: CommandIDs.openJSON,
                icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.launchIcon,
                label: trans.__('JSON Settings Editor')
            }));
        }
        editor.id = namespace;
        editor.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.settingsIcon;
        editor.title.label = trans.__('Settings');
        editor.title.closable = true;
        void tracker.add(editor);
        shell.add(editor, 'main', { type: 'Settings' });
    };
    commands.addCommand(CommandIDs.open, {
        execute: async (args) => {
            void registry.load(plugin.id).then(settings => {
                var _a, _b;
                ((_a = args.settingEditorType) !== null && _a !== void 0 ? _a : settings.get('settingEditorType').composite ===
                    'json')
                    ? void commands.execute(CommandIDs.openJSON)
                    : void openUi({ query: (_b = args.query) !== null && _b !== void 0 ? _b : '' });
            });
        },
        label: args => {
            if (args.label) {
                return args.label;
            }
            return trans.__('Settings Editor');
        }
    });
    if (palette) {
        palette.addItem({
            category: trans.__('Settings'),
            command: CommandIDs.open,
            args: { settingEditorType: 'ui' }
        });
    }
    return tracker;
}
/**
 * The default setting editor extension.
 */
const jsonPlugin = {
    id: '@jupyterlab/settingeditor-extension:plugin',
    requires: [
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices,
        _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_6__.IStateDB,
        _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.IRenderMimeRegistry,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator
    ],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    autoStart: true,
    provides: _jupyterlab_settingeditor_lib_tokens__WEBPACK_IMPORTED_MODULE_8__.IJSONSettingEditorTracker,
    activate: activateJSON
};
/**
 * Activate the setting editor extension.
 */
function activateJSON(app, registry, editorServices, state, rendermime, status, translator, restorer, palette) {
    const trans = translator.load('jupyterlab');
    const { commands, shell } = app;
    const namespace = 'json-setting-editor';
    const factoryService = editorServices.factoryService;
    const editorFactory = factoryService.newInlineEditor;
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace
    });
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: CommandIDs.openJSON,
            args: widget => ({}),
            name: widget => namespace
        });
    }
    commands.addCommand(CommandIDs.openJSON, {
        execute: async () => {
            if (tracker.currentWidget && !tracker.currentWidget.isDisposed) {
                if (!tracker.currentWidget.isAttached) {
                    shell.add(tracker.currentWidget, 'main', {
                        type: 'Advanced Settings'
                    });
                }
                shell.activateById(tracker.currentWidget.id);
                return;
            }
            const key = plugin.id;
            const when = app.restored;
            const { JsonSettingEditor } = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_jupyterlab_settingeditor_jupyterlab_settingeditor").then(__webpack_require__.t.bind(__webpack_require__, /*! @jupyterlab/settingeditor */ "webpack/sharing/consume/default/@jupyterlab/settingeditor/@jupyterlab/settingeditor", 23));
            const editor = new JsonSettingEditor({
                commands: {
                    registry: commands,
                    revert: CommandIDs.revert,
                    save: CommandIDs.save
                },
                editorFactory,
                key,
                registry,
                rendermime,
                state,
                translator,
                when
            });
            let disposable = null;
            // Notify the command registry when the visibility status of the setting
            // editor's commands change. The setting editor toolbar listens for this
            // signal from the command registry.
            editor.commandsChanged.connect((sender, args) => {
                args.forEach(id => {
                    commands.notifyCommandChanged(id);
                });
                if (editor.canSaveRaw) {
                    if (!disposable) {
                        disposable = status.setDirty();
                    }
                }
                else if (disposable) {
                    disposable.dispose();
                    disposable = null;
                }
                editor.disposed.connect(() => {
                    if (disposable) {
                        disposable.dispose();
                    }
                });
            });
            const container = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
                content: editor
            });
            container.id = namespace;
            container.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.settingsIcon;
            container.title.label = trans.__('Advanced Settings Editor');
            container.title.closable = true;
            void tracker.add(container);
            shell.add(container, 'main', { type: 'Advanced Settings' });
        },
        label: trans.__('Advanced Settings Editor')
    });
    if (palette) {
        palette.addItem({
            category: trans.__('Settings'),
            command: CommandIDs.openJSON
        });
    }
    commands.addCommand(CommandIDs.revert, {
        execute: () => {
            var _a;
            (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.revert();
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.undoIcon,
        label: trans.__('Revert User Settings'),
        isEnabled: () => { var _a, _b; return (_b = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.canRevertRaw) !== null && _b !== void 0 ? _b : false; }
    });
    commands.addCommand(CommandIDs.save, {
        execute: () => { var _a; return (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.save(); },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.saveIcon,
        label: trans.__('Save User Settings'),
        isEnabled: () => { var _a, _b; return (_b = (_a = tracker.currentWidget) === null || _a === void 0 ? void 0 : _a.content.canSaveRaw) !== null && _b !== void 0 ? _b : false; }
    });
    return tracker;
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([plugin, jsonPlugin]);


/***/ }),

/***/ "../../packages/settingeditor/lib/tokens.js":
/*!**************************************************!*\
  !*** ../../packages/settingeditor/lib/tokens.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IJSONSettingEditorTracker": () => (/* binding */ IJSONSettingEditorTracker),
/* harmony export */   "ISettingEditorTracker": () => (/* binding */ ISettingEditorTracker)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The setting editor tracker token.
 */
const ISettingEditorTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/settingeditor:ISettingEditorTracker');
/**
 * The setting editor tracker token.
 */
const IJSONSettingEditorTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/settingeditor:IJSONSettingEditorTracker');


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfc2V0dGluZ2VkaXRvci1leHRlbnNpb25fbGliX2luZGV4X2pzLjM5ZmJlYTlkMWQyMWFmNjMyMDZlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQU84QjtBQUtIO0FBQzJCO0FBTXRCO0FBQzBCO0FBSWY7QUFLaUI7QUFDaEI7QUFDTztBQUN1QjtBQUc3RTs7R0FFRztBQUNILElBQVUsVUFBVSxDQVFuQjtBQVJELFdBQVUsVUFBVTtJQUNMLGVBQUksR0FBRyxvQkFBb0IsQ0FBQztJQUU1QixtQkFBUSxHQUFHLHlCQUF5QixDQUFDO0lBRXJDLGlCQUFNLEdBQUcsc0JBQXNCLENBQUM7SUFFaEMsZUFBSSxHQUFHLG9CQUFvQixDQUFDO0FBQzNDLENBQUMsRUFSUyxVQUFVLEtBQVYsVUFBVSxRQVFuQjtBQUlEOztHQUVHO0FBQ0gsTUFBTSxNQUFNLEdBQWlEO0lBQzNELEVBQUUsRUFBRSw2Q0FBNkM7SUFDakQsUUFBUSxFQUFFO1FBQ1IseUVBQWdCO1FBQ2hCLHlEQUFRO1FBQ1IsZ0VBQVc7UUFDWCw2RUFBc0I7UUFDdEIsK0RBQVU7S0FDWDtJQUNELFFBQVEsRUFBRSxDQUFDLG9FQUFlLEVBQUUsaUVBQWUsRUFBRSwyRkFBeUIsQ0FBQztJQUN2RSxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSx1RkFBcUI7SUFDL0IsUUFBUTtDQUNULENBQUM7QUFFRjs7R0FFRztBQUNILFNBQVMsUUFBUSxDQUNmLEdBQW9CLEVBQ3BCLFFBQTBCLEVBQzFCLEtBQWUsRUFDZixVQUF1QixFQUN2QixjQUFzQyxFQUN0QyxNQUFrQixFQUNsQixRQUFnQyxFQUNoQyxPQUErQixFQUMvQixVQUE0QztJQUU1QyxNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sRUFBRSxRQUFRLEVBQUUsS0FBSyxFQUFFLEdBQUcsR0FB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QUFPLENBQUMsTUFBTSxFQUFFLENBQUM7UUFDMUMsQ0FBQztRQUNELElBQUksRUFBRSwrREFBUTtRQUNkLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHNCQUFzQixDQUFDO1FBQ3ZDLFNBQVMsRUFBRSxHQUFHLEVBQUUsZUFBQywwQkFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDLFlBQVksbUNBQUksS0FBSztLQUN0RSxDQUFDLENBQUM7SUFFSCxRQUFRLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxJQUFJLEVBQUU7UUFDbkMsT0FBTyxFQUFFLEdBQUcsRUFBRSxXQUFDLG9CQUFPLENBQUMsYUFBYSwwQ0FBRSxPQUFPLENBQUMsSUFBSSxFQUFFO1FBQ3BELElBQUksRUFBRSwrREFBUTtRQUNkLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG9CQUFvQixDQUFDO1FBQ3JDLFNBQVMsRUFBRSxHQUFHLEVBQUUsZUFBQywwQkFBTyxDQUFDLGFBQWEsMENBQUUsT0FBTyxDQUFDLFVBQVUsbUNBQUksS0FBSztLQUNwRSxDQUFDLENBQUM7SUFFSCxPQUFPLE9BQU8sQ0FBQztBQUNqQixDQUFDO0FBRUQsaUVBQWUsQ0FBQyxNQUFNLEVBQUUsVUFBVSxDQUFDLEVBQUM7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQy9VcEMsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUdqQjtBQUkxQzs7R0FFRztBQUNJLE1BQU0scUJBQXFCLEdBQUcsSUFBSSxvREFBSyxDQUM1QyxpREFBaUQsQ0FDbEQsQ0FBQztBQUVGOztHQUVHO0FBQ0ksTUFBTSx5QkFBeUIsR0FBRyxJQUFJLG9EQUFLLENBQ2hELHFEQUFxRCxDQUN0RCxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3NldHRpbmdlZGl0b3ItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc2V0dGluZ2VkaXRvci9zcmMvdG9rZW5zLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgc2V0dGluZ2VkaXRvci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGFiU3RhdHVzLFxuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgTWFpbkFyZWFXaWRnZXQsXG4gIFdpZGdldFRyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgSUVkaXRvclNlcnZpY2VzIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZWVkaXRvcic7XG5pbXBvcnQge1xuICBDb21tYW5kVG9vbGJhckJ1dHRvbixcbiAgSUZvcm1Db21wb25lbnRSZWdpc3RyeSxcbiAgbGF1bmNoSWNvbixcbiAgVG9vbGJhclxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IElSZW5kZXJNaW1lUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7XG4gIElKU09OU2V0dGluZ0VkaXRvclRyYWNrZXIsXG4gIElTZXR0aW5nRWRpdG9yVHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5nZWRpdG9yL2xpYi90b2tlbnMnO1xuaW1wb3J0IHR5cGUge1xuICBKc29uU2V0dGluZ0VkaXRvcixcbiAgU2V0dGluZ3NFZGl0b3Jcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvcic7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElTdGF0ZURCIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdGVkYic7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IHNhdmVJY29uLCBzZXR0aW5nc0ljb24sIHVuZG9JY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIHNldHRpbmcgZWRpdG9yLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBvcGVuID0gJ3NldHRpbmdlZGl0b3I6b3Blbic7XG5cbiAgZXhwb3J0IGNvbnN0IG9wZW5KU09OID0gJ3NldHRpbmdlZGl0b3I6b3Blbi1qc29uJztcblxuICBleHBvcnQgY29uc3QgcmV2ZXJ0ID0gJ3NldHRpbmdlZGl0b3I6cmV2ZXJ0JztcblxuICBleHBvcnQgY29uc3Qgc2F2ZSA9ICdzZXR0aW5nZWRpdG9yOnNhdmUnO1xufVxuXG50eXBlIFNldHRpbmdFZGl0b3JUeXBlID0gJ3VpJyB8ICdqc29uJztcblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBzZXR0aW5nIGVkaXRvciBleHRlbnNpb24uXG4gKi9cbmNvbnN0IHBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPElTZXR0aW5nRWRpdG9yVHJhY2tlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvci1leHRlbnNpb246Zm9ybS11aScsXG4gIHJlcXVpcmVzOiBbXG4gICAgSVNldHRpbmdSZWdpc3RyeSxcbiAgICBJU3RhdGVEQixcbiAgICBJVHJhbnNsYXRvcixcbiAgICBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5LFxuICAgIElMYWJTdGF0dXNcbiAgXSxcbiAgb3B0aW9uYWw6IFtJTGF5b3V0UmVzdG9yZXIsIElDb21tYW5kUGFsZXR0ZSwgSUpTT05TZXR0aW5nRWRpdG9yVHJhY2tlcl0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElTZXR0aW5nRWRpdG9yVHJhY2tlcixcbiAgYWN0aXZhdGVcbn07XG5cbi8qKlxuICogQWN0aXZhdGUgdGhlIHNldHRpbmcgZWRpdG9yIGV4dGVuc2lvbi5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICByZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgc3RhdGU6IElTdGF0ZURCLFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgZWRpdG9yUmVnaXN0cnk6IElGb3JtQ29tcG9uZW50UmVnaXN0cnksXG4gIHN0YXR1czogSUxhYlN0YXR1cyxcbiAgcmVzdG9yZXI6IElMYXlvdXRSZXN0b3JlciB8IG51bGwsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gIGpzb25FZGl0b3I6IElKU09OU2V0dGluZ0VkaXRvclRyYWNrZXIgfCBudWxsXG4pOiBJU2V0dGluZ0VkaXRvclRyYWNrZXIge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICBjb25zdCBuYW1lc3BhY2UgPSAnc2V0dGluZy1lZGl0b3InO1xuICBjb25zdCB0cmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8TWFpbkFyZWFXaWRnZXQ8U2V0dGluZ3NFZGl0b3I+Pih7XG4gICAgbmFtZXNwYWNlXG4gIH0pO1xuXG4gIC8vIEhhbmRsZSBzdGF0ZSByZXN0b3JhdGlvbi5cbiAgaWYgKHJlc3RvcmVyKSB7XG4gICAgdm9pZCByZXN0b3Jlci5yZXN0b3JlKHRyYWNrZXIsIHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlbixcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoe30pLFxuICAgICAgbmFtZTogd2lkZ2V0ID0+IG5hbWVzcGFjZVxuICAgIH0pO1xuICB9XG5cbiAgY29uc3Qgb3BlblVpID0gYXN5bmMgKGFyZ3M6IHsgcXVlcnk6IHN0cmluZyB9KSA9PiB7XG4gICAgaWYgKHRyYWNrZXIuY3VycmVudFdpZGdldCAmJiAhdHJhY2tlci5jdXJyZW50V2lkZ2V0LmlzRGlzcG9zZWQpIHtcbiAgICAgIGlmICghdHJhY2tlci5jdXJyZW50V2lkZ2V0LmlzQXR0YWNoZWQpIHtcbiAgICAgICAgc2hlbGwuYWRkKHRyYWNrZXIuY3VycmVudFdpZGdldCwgJ21haW4nLCB7IHR5cGU6ICdTZXR0aW5ncycgfSk7XG4gICAgICB9XG4gICAgICBzaGVsbC5hY3RpdmF0ZUJ5SWQodHJhY2tlci5jdXJyZW50V2lkZ2V0LmlkKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBrZXkgPSBwbHVnaW4uaWQ7XG5cbiAgICBjb25zdCB7IFNldHRpbmdzRWRpdG9yIH0gPSBhd2FpdCBpbXBvcnQoJ0BqdXB5dGVybGFiL3NldHRpbmdlZGl0b3InKTtcblxuICAgIGNvbnN0IGVkaXRvciA9IG5ldyBNYWluQXJlYVdpZGdldDxTZXR0aW5nc0VkaXRvcj4oe1xuICAgICAgY29udGVudDogbmV3IFNldHRpbmdzRWRpdG9yKHtcbiAgICAgICAgZWRpdG9yUmVnaXN0cnksXG4gICAgICAgIGtleSxcbiAgICAgICAgcmVnaXN0cnksXG4gICAgICAgIHN0YXRlLFxuICAgICAgICBjb21tYW5kcyxcbiAgICAgICAgdG9Ta2lwOiBbXG4gICAgICAgICAgJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLWV4dGVuc2lvbjpjb250ZXh0LW1lbnUnLFxuICAgICAgICAgICdAanVweXRlcmxhYi9tYWlubWVudS1leHRlbnNpb246cGx1Z2luJ1xuICAgICAgICBdLFxuICAgICAgICB0cmFuc2xhdG9yLFxuICAgICAgICBzdGF0dXMsXG4gICAgICAgIHF1ZXJ5OiBhcmdzLnF1ZXJ5IGFzIHN0cmluZ1xuICAgICAgfSlcbiAgICB9KTtcblxuICAgIGlmIChqc29uRWRpdG9yKSB7XG4gICAgICBlZGl0b3IudG9vbGJhci5hZGRJdGVtKCdzcGFjZXInLCBUb29sYmFyLmNyZWF0ZVNwYWNlckl0ZW0oKSk7XG4gICAgICBlZGl0b3IudG9vbGJhci5hZGRJdGVtKFxuICAgICAgICAnb3Blbi1qc29uLWVkaXRvcicsXG4gICAgICAgIG5ldyBDb21tYW5kVG9vbGJhckJ1dHRvbih7XG4gICAgICAgICAgY29tbWFuZHMsXG4gICAgICAgICAgaWQ6IENvbW1hbmRJRHMub3BlbkpTT04sXG4gICAgICAgICAgaWNvbjogbGF1bmNoSWNvbixcbiAgICAgICAgICBsYWJlbDogdHJhbnMuX18oJ0pTT04gU2V0dGluZ3MgRWRpdG9yJylcbiAgICAgICAgfSlcbiAgICAgICk7XG4gICAgfVxuXG4gICAgZWRpdG9yLmlkID0gbmFtZXNwYWNlO1xuICAgIGVkaXRvci50aXRsZS5pY29uID0gc2V0dGluZ3NJY29uO1xuICAgIGVkaXRvci50aXRsZS5sYWJlbCA9IHRyYW5zLl9fKCdTZXR0aW5ncycpO1xuICAgIGVkaXRvci50aXRsZS5jbG9zYWJsZSA9IHRydWU7XG5cbiAgICB2b2lkIHRyYWNrZXIuYWRkKGVkaXRvcik7XG4gICAgc2hlbGwuYWRkKGVkaXRvciwgJ21haW4nLCB7IHR5cGU6ICdTZXR0aW5ncycgfSk7XG4gIH07XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW4sIHtcbiAgICBleGVjdXRlOiBhc3luYyAoYXJnczoge1xuICAgICAgcXVlcnk/OiBzdHJpbmc7XG4gICAgICBzZXR0aW5nRWRpdG9yVHlwZT86IFNldHRpbmdFZGl0b3JUeXBlO1xuICAgIH0pID0+IHtcbiAgICAgIHZvaWQgcmVnaXN0cnkubG9hZChwbHVnaW4uaWQpLnRoZW4oc2V0dGluZ3MgPT4ge1xuICAgICAgICBhcmdzLnNldHRpbmdFZGl0b3JUeXBlID8/XG4gICAgICAgIChzZXR0aW5ncy5nZXQoJ3NldHRpbmdFZGl0b3JUeXBlJykuY29tcG9zaXRlIGFzIFNldHRpbmdFZGl0b3JUeXBlKSA9PT1cbiAgICAgICAgICAnanNvbidcbiAgICAgICAgICA/IHZvaWQgY29tbWFuZHMuZXhlY3V0ZShDb21tYW5kSURzLm9wZW5KU09OKVxuICAgICAgICAgIDogdm9pZCBvcGVuVWkoeyBxdWVyeTogYXJncy5xdWVyeSA/PyAnJyB9KTtcbiAgICAgIH0pO1xuICAgIH0sXG4gICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgaWYgKGFyZ3MubGFiZWwpIHtcbiAgICAgICAgcmV0dXJuIGFyZ3MubGFiZWwgYXMgc3RyaW5nO1xuICAgICAgfVxuICAgICAgcmV0dXJuIHRyYW5zLl9fKCdTZXR0aW5ncyBFZGl0b3InKTtcbiAgICB9XG4gIH0pO1xuXG4gIGlmIChwYWxldHRlKSB7XG4gICAgcGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgIGNhdGVnb3J5OiB0cmFucy5fXygnU2V0dGluZ3MnKSxcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlbixcbiAgICAgIGFyZ3M6IHsgc2V0dGluZ0VkaXRvclR5cGU6ICd1aScgfVxuICAgIH0pO1xuICB9XG5cbiAgcmV0dXJuIHRyYWNrZXI7XG59XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgc2V0dGluZyBlZGl0b3IgZXh0ZW5zaW9uLlxuICovXG5jb25zdCBqc29uUGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUpTT05TZXR0aW5nRWRpdG9yVHJhY2tlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvci1leHRlbnNpb246cGx1Z2luJyxcbiAgcmVxdWlyZXM6IFtcbiAgICBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIElFZGl0b3JTZXJ2aWNlcyxcbiAgICBJU3RhdGVEQixcbiAgICBJUmVuZGVyTWltZVJlZ2lzdHJ5LFxuICAgIElMYWJTdGF0dXMsXG4gICAgSVRyYW5zbGF0b3JcbiAgXSxcbiAgb3B0aW9uYWw6IFtJTGF5b3V0UmVzdG9yZXIsIElDb21tYW5kUGFsZXR0ZV0sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElKU09OU2V0dGluZ0VkaXRvclRyYWNrZXIsXG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUpTT05cbn07XG5cbi8qKlxuICogQWN0aXZhdGUgdGhlIHNldHRpbmcgZWRpdG9yIGV4dGVuc2lvbi5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGVKU09OKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgcmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gIGVkaXRvclNlcnZpY2VzOiBJRWRpdG9yU2VydmljZXMsXG4gIHN0YXRlOiBJU3RhdGVEQixcbiAgcmVuZGVybWltZTogSVJlbmRlck1pbWVSZWdpc3RyeSxcbiAgc3RhdHVzOiBJTGFiU3RhdHVzLFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgcmVzdG9yZXI6IElMYXlvdXRSZXN0b3JlciB8IG51bGwsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGxcbik6IElKU09OU2V0dGluZ0VkaXRvclRyYWNrZXIge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICBjb25zdCBuYW1lc3BhY2UgPSAnanNvbi1zZXR0aW5nLWVkaXRvcic7XG4gIGNvbnN0IGZhY3RvcnlTZXJ2aWNlID0gZWRpdG9yU2VydmljZXMuZmFjdG9yeVNlcnZpY2U7XG4gIGNvbnN0IGVkaXRvckZhY3RvcnkgPSBmYWN0b3J5U2VydmljZS5uZXdJbmxpbmVFZGl0b3I7XG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxNYWluQXJlYVdpZGdldDxKc29uU2V0dGluZ0VkaXRvcj4+KHtcbiAgICBuYW1lc3BhY2VcbiAgfSk7XG5cbiAgLy8gSGFuZGxlIHN0YXRlIHJlc3RvcmF0aW9uLlxuICBpZiAocmVzdG9yZXIpIHtcbiAgICB2b2lkIHJlc3RvcmVyLnJlc3RvcmUodHJhY2tlciwge1xuICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5vcGVuSlNPTixcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoe30pLFxuICAgICAgbmFtZTogd2lkZ2V0ID0+IG5hbWVzcGFjZVxuICAgIH0pO1xuICB9XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW5KU09OLCB7XG4gICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgaWYgKHRyYWNrZXIuY3VycmVudFdpZGdldCAmJiAhdHJhY2tlci5jdXJyZW50V2lkZ2V0LmlzRGlzcG9zZWQpIHtcbiAgICAgICAgaWYgKCF0cmFja2VyLmN1cnJlbnRXaWRnZXQuaXNBdHRhY2hlZCkge1xuICAgICAgICAgIHNoZWxsLmFkZCh0cmFja2VyLmN1cnJlbnRXaWRnZXQsICdtYWluJywge1xuICAgICAgICAgICAgdHlwZTogJ0FkdmFuY2VkIFNldHRpbmdzJ1xuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICAgIHNoZWxsLmFjdGl2YXRlQnlJZCh0cmFja2VyLmN1cnJlbnRXaWRnZXQuaWQpO1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIGNvbnN0IGtleSA9IHBsdWdpbi5pZDtcbiAgICAgIGNvbnN0IHdoZW4gPSBhcHAucmVzdG9yZWQ7XG5cbiAgICAgIGNvbnN0IHsgSnNvblNldHRpbmdFZGl0b3IgfSA9IGF3YWl0IGltcG9ydCgnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvcicpO1xuXG4gICAgICBjb25zdCBlZGl0b3IgPSBuZXcgSnNvblNldHRpbmdFZGl0b3Ioe1xuICAgICAgICBjb21tYW5kczoge1xuICAgICAgICAgIHJlZ2lzdHJ5OiBjb21tYW5kcyxcbiAgICAgICAgICByZXZlcnQ6IENvbW1hbmRJRHMucmV2ZXJ0LFxuICAgICAgICAgIHNhdmU6IENvbW1hbmRJRHMuc2F2ZVxuICAgICAgICB9LFxuICAgICAgICBlZGl0b3JGYWN0b3J5LFxuICAgICAgICBrZXksXG4gICAgICAgIHJlZ2lzdHJ5LFxuICAgICAgICByZW5kZXJtaW1lLFxuICAgICAgICBzdGF0ZSxcbiAgICAgICAgdHJhbnNsYXRvcixcbiAgICAgICAgd2hlblxuICAgICAgfSk7XG5cbiAgICAgIGxldCBkaXNwb3NhYmxlOiBJRGlzcG9zYWJsZSB8IG51bGwgPSBudWxsO1xuICAgICAgLy8gTm90aWZ5IHRoZSBjb21tYW5kIHJlZ2lzdHJ5IHdoZW4gdGhlIHZpc2liaWxpdHkgc3RhdHVzIG9mIHRoZSBzZXR0aW5nXG4gICAgICAvLyBlZGl0b3IncyBjb21tYW5kcyBjaGFuZ2UuIFRoZSBzZXR0aW5nIGVkaXRvciB0b29sYmFyIGxpc3RlbnMgZm9yIHRoaXNcbiAgICAgIC8vIHNpZ25hbCBmcm9tIHRoZSBjb21tYW5kIHJlZ2lzdHJ5LlxuICAgICAgZWRpdG9yLmNvbW1hbmRzQ2hhbmdlZC5jb25uZWN0KChzZW5kZXI6IGFueSwgYXJnczogc3RyaW5nW10pID0+IHtcbiAgICAgICAgYXJncy5mb3JFYWNoKGlkID0+IHtcbiAgICAgICAgICBjb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZChpZCk7XG4gICAgICAgIH0pO1xuICAgICAgICBpZiAoZWRpdG9yLmNhblNhdmVSYXcpIHtcbiAgICAgICAgICBpZiAoIWRpc3Bvc2FibGUpIHtcbiAgICAgICAgICAgIGRpc3Bvc2FibGUgPSBzdGF0dXMuc2V0RGlydHkoKTtcbiAgICAgICAgICB9XG4gICAgICAgIH0gZWxzZSBpZiAoZGlzcG9zYWJsZSkge1xuICAgICAgICAgIGRpc3Bvc2FibGUuZGlzcG9zZSgpO1xuICAgICAgICAgIGRpc3Bvc2FibGUgPSBudWxsO1xuICAgICAgICB9XG4gICAgICAgIGVkaXRvci5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgICBpZiAoZGlzcG9zYWJsZSkge1xuICAgICAgICAgICAgZGlzcG9zYWJsZS5kaXNwb3NlKCk7XG4gICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICAgIH0pO1xuXG4gICAgICBjb25zdCBjb250YWluZXIgPSBuZXcgTWFpbkFyZWFXaWRnZXQ8SnNvblNldHRpbmdFZGl0b3I+KHtcbiAgICAgICAgY29udGVudDogZWRpdG9yXG4gICAgICB9KTtcblxuICAgICAgY29udGFpbmVyLmlkID0gbmFtZXNwYWNlO1xuICAgICAgY29udGFpbmVyLnRpdGxlLmljb24gPSBzZXR0aW5nc0ljb247XG4gICAgICBjb250YWluZXIudGl0bGUubGFiZWwgPSB0cmFucy5fXygnQWR2YW5jZWQgU2V0dGluZ3MgRWRpdG9yJyk7XG4gICAgICBjb250YWluZXIudGl0bGUuY2xvc2FibGUgPSB0cnVlO1xuXG4gICAgICB2b2lkIHRyYWNrZXIuYWRkKGNvbnRhaW5lcik7XG4gICAgICBzaGVsbC5hZGQoY29udGFpbmVyLCAnbWFpbicsIHsgdHlwZTogJ0FkdmFuY2VkIFNldHRpbmdzJyB9KTtcbiAgICB9LFxuICAgIGxhYmVsOiB0cmFucy5fXygnQWR2YW5jZWQgU2V0dGluZ3MgRWRpdG9yJylcbiAgfSk7XG4gIGlmIChwYWxldHRlKSB7XG4gICAgcGFsZXR0ZS5hZGRJdGVtKHtcbiAgICAgIGNhdGVnb3J5OiB0cmFucy5fXygnU2V0dGluZ3MnKSxcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlbkpTT05cbiAgICB9KTtcbiAgfVxuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXZlcnQsIHtcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQucmV2ZXJ0KCk7XG4gICAgfSxcbiAgICBpY29uOiB1bmRvSWNvbixcbiAgICBsYWJlbDogdHJhbnMuX18oJ1JldmVydCBVc2VyIFNldHRpbmdzJyksXG4gICAgaXNFbmFibGVkOiAoKSA9PiB0cmFja2VyLmN1cnJlbnRXaWRnZXQ/LmNvbnRlbnQuY2FuUmV2ZXJ0UmF3ID8/IGZhbHNlXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zYXZlLCB7XG4gICAgZXhlY3V0ZTogKCkgPT4gdHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50LnNhdmUoKSxcbiAgICBpY29uOiBzYXZlSWNvbixcbiAgICBsYWJlbDogdHJhbnMuX18oJ1NhdmUgVXNlciBTZXR0aW5ncycpLFxuICAgIGlzRW5hYmxlZDogKCkgPT4gdHJhY2tlci5jdXJyZW50V2lkZ2V0Py5jb250ZW50LmNhblNhdmVSYXcgPz8gZmFsc2VcbiAgfSk7XG5cbiAgcmV0dXJuIHRyYWNrZXI7XG59XG5cbmV4cG9ydCBkZWZhdWx0IFtwbHVnaW4sIGpzb25QbHVnaW5dO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJV2lkZ2V0VHJhY2tlciwgTWFpbkFyZWFXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IEpzb25TZXR0aW5nRWRpdG9yIGFzIEpTT05TZXR0aW5nRWRpdG9yIH0gZnJvbSAnLi9qc29uc2V0dGluZ2VkaXRvcic7XG5pbXBvcnQgeyBTZXR0aW5nc0VkaXRvciB9IGZyb20gJy4vc2V0dGluZ3NlZGl0b3InO1xuXG4vKipcbiAqIFRoZSBzZXR0aW5nIGVkaXRvciB0cmFja2VyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVNldHRpbmdFZGl0b3JUcmFja2VyID0gbmV3IFRva2VuPElTZXR0aW5nRWRpdG9yVHJhY2tlcj4oXG4gICdAanVweXRlcmxhYi9zZXR0aW5nZWRpdG9yOklTZXR0aW5nRWRpdG9yVHJhY2tlcidcbik7XG5cbi8qKlxuICogVGhlIHNldHRpbmcgZWRpdG9yIHRyYWNrZXIgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJSlNPTlNldHRpbmdFZGl0b3JUcmFja2VyID0gbmV3IFRva2VuPElKU09OU2V0dGluZ0VkaXRvclRyYWNrZXI+KFxuICAnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvcjpJSlNPTlNldHRpbmdFZGl0b3JUcmFja2VyJ1xuKTtcblxuLyoqXG4gKiBBIGNsYXNzIHRoYXQgdHJhY2tzIHRoZSBzZXR0aW5nIGVkaXRvci5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJSlNPTlNldHRpbmdFZGl0b3JUcmFja2VyXG4gIGV4dGVuZHMgSVdpZGdldFRyYWNrZXI8TWFpbkFyZWFXaWRnZXQ8SlNPTlNldHRpbmdFZGl0b3I+PiB7fVxuXG4vKipcbiAqIEEgY2xhc3MgdGhhdCB0cmFja3MgdGhlIHNldHRpbmcgZWRpdG9yLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElTZXR0aW5nRWRpdG9yVHJhY2tlclxuICBleHRlbmRzIElXaWRnZXRUcmFja2VyPE1haW5BcmVhV2lkZ2V0PFNldHRpbmdzRWRpdG9yPj4ge31cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==