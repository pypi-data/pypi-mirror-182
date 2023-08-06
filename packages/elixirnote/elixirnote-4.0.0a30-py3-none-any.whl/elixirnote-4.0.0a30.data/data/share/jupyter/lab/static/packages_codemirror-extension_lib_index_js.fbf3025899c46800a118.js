"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_codemirror-extension_lib_index_js"],{

/***/ "../../packages/codemirror-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/codemirror-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "editorSyntaxStatus": () => (/* binding */ editorSyntaxStatus),
/* harmony export */   "lineColItem": () => (/* binding */ lineColItem)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/fileeditor */ "webpack/sharing/consume/default/@jupyterlab/fileeditor/@jupyterlab/fileeditor");
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _codemirror_search__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @codemirror/search */ "webpack/sharing/consume/default/@codemirror/search/@codemirror/search");
/* harmony import */ var _codemirror_search__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_codemirror_search__WEBPACK_IMPORTED_MODULE_8__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module codemirror-extension
 */









/**
 * The command IDs used by the codemirror plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.changeKeyMap = 'codemirror:change-keymap';
    CommandIDs.changeTheme = 'codemirror:change-theme';
    CommandIDs.changeMode = 'codemirror:change-mode';
    CommandIDs.find = 'codemirror:find';
    CommandIDs.goToLine = 'codemirror:go-to-line';
})(CommandIDs || (CommandIDs = {}));
/**
 * The editor services.
 */
const services = {
    id: '@jupyterlab/codemirror-extension:services',
    provides: _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.IEditorServices,
    activate: activateEditorServices
};
/**
 * The editor commands.
 */
const commands = {
    id: '@jupyterlab/codemirror-extension:commands',
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__.IEditorTracker, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__.IMainMenu],
    activate: activateEditorCommands,
    autoStart: true
};
/**
 * The JupyterLab plugin for the EditorSyntax status item.
 */
const editorSyntaxStatus = {
    id: '@jupyterlab/codemirror-extension:editor-syntax-status',
    autoStart: true,
    requires: [_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_3__.IEditorTracker, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar],
    activate: (app, tracker, labShell, translator, statusBar) => {
        if (!statusBar) {
            // Automatically disable if statusbar missing
            return;
        }
        const item = new _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.EditorSyntaxStatus({ commands: app.commands, translator });
        labShell.currentChanged.connect(() => {
            const current = labShell.currentWidget;
            if (current && tracker.has(current) && item.model) {
                item.model.editor = current.content.editor;
            }
        });
        statusBar.registerStatusItem('@jupyterlab/codemirror-extension:editor-syntax-status', {
            item,
            align: 'left',
            rank: 0,
            isActive: () => !!labShell.currentWidget &&
                !!tracker.currentWidget &&
                labShell.currentWidget === tracker.currentWidget
        });
    }
};
/**
 * A plugin providing a line/column status item to the application.
 */
const lineColItem = {
    id: '@jupyterlab/codemirror-extension:line-col-status',
    autoStart: true,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar],
    provides: _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.IPositionModel,
    activate: (app, translator, labShell, statusBar) => {
        const item = new _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_1__.LineCol(translator);
        const providers = new Set();
        if (statusBar) {
            // Add the status item to the status bar.
            statusBar.registerStatusItem(lineColItem.id, {
                item,
                align: 'right',
                rank: 2,
                isActive: () => !!item.model.editor
            });
        }
        const addEditorProvider = (provider) => {
            providers.add(provider);
            if (app.shell.currentWidget) {
                updateEditor(app.shell, {
                    newValue: app.shell.currentWidget,
                    oldValue: null
                });
            }
        };
        const update = () => {
            updateEditor(app.shell, {
                oldValue: app.shell.currentWidget,
                newValue: app.shell.currentWidget
            });
        };
        function updateEditor(shell, changes) {
            var _a;
            item.model.editor =
                (_a = [...providers]
                    .map(provider => provider(changes.newValue))
                    .filter(editor => editor !== null)[0]) !== null && _a !== void 0 ? _a : null;
        }
        if (labShell) {
            labShell.currentChanged.connect(updateEditor);
        }
        return { addEditorProvider, update };
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [
    commands,
    services,
    editorSyntaxStatus,
    lineColItem
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * The plugin ID used as the key in the setting registry.
 */
const id = commands.id;
/**
 * Set up the editor services.
 */
function activateEditorServices(app) {
    _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.CodeMirrorEditor.prototype.save = () => {
        void app.commands.execute('docmanager:save');
    };
    return _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.editorServices;
}
/**
 * Set up the editor widget menu and commands.
 */
function activateEditorCommands(app, tracker, settingRegistry, translator, mainMenu) {
    var _a;
    const trans = translator.load('jupyterlab');
    const { commands, restored } = app;
    let { theme, keyMap, scrollPastEnd, styleActiveLine, styleSelectedText, selectionPointer, lineWiseCopyCut } = _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.CodeMirrorEditor.defaultConfig;
    /**
     * Update the setting values.
     */
    async function updateSettings(settings) {
        var _a, _b, _c, _d, _e;
        keyMap = settings.get('keyMap').composite || keyMap;
        theme = settings.get('theme').composite || theme;
        scrollPastEnd =
            (_a = settings.get('scrollPastEnd').composite) !== null && _a !== void 0 ? _a : scrollPastEnd;
        styleActiveLine =
            (_b = settings.get('styleActiveLine').composite) !== null && _b !== void 0 ? _b : styleActiveLine;
        styleSelectedText =
            (_c = settings.get('styleSelectedText').composite) !== null && _c !== void 0 ? _c : styleSelectedText;
        selectionPointer =
            (_d = settings.get('selectionPointer').composite) !== null && _d !== void 0 ? _d : selectionPointer;
        lineWiseCopyCut =
            (_e = settings.get('lineWiseCopyCut').composite) !== null && _e !== void 0 ? _e : lineWiseCopyCut;
    }
    /**
     * Update the settings of the current tracker instances.
     */
    function updateTracker() {
        const editorOptions = {
            keyMap,
            theme,
            scrollPastEnd,
            styleActiveLine,
            styleSelectedText,
            selectionPointer,
            lineWiseCopyCut
        };
        tracker.forEach(widget => {
            if (widget.content.editor instanceof _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.CodeMirrorEditor) {
                widget.content.editor.setOptions(editorOptions);
            }
        });
    }
    // Fetch the initial state of the settings.
    Promise.all([settingRegistry.load(id), restored])
        .then(async ([settings]) => {
        await updateSettings(settings);
        updateTracker();
        settings.changed.connect(async () => {
            await updateSettings(settings);
            updateTracker();
        });
    })
        .catch((reason) => {
        console.error(reason.message);
        updateTracker();
    });
    /**
     * Handle the settings of new widgets.
     */
    tracker.widgetAdded.connect((sender, widget) => {
        const editorOptions = {
            keyMap,
            theme,
            scrollPastEnd,
            styleActiveLine,
            styleSelectedText,
            selectionPointer,
            lineWiseCopyCut
        };
        if (widget.content.editor instanceof _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.CodeMirrorEditor) {
            widget.content.editor.setOptions(editorOptions);
        }
    });
    /**
     * A test for whether the tracker has an active widget.
     */
    function isEnabled() {
        return (tracker.currentWidget !== null &&
            tracker.currentWidget === app.shell.currentWidget);
    }
    /**
     * Create a menu for the editor.
     */
    commands.addCommand(CommandIDs.changeTheme, {
        label: args => { var _a; return (_a = args.theme) !== null && _a !== void 0 ? _a : theme; },
        execute: args => {
            var _a;
            const key = 'theme';
            const value = (theme = (_a = args['theme']) !== null && _a !== void 0 ? _a : theme);
            return settingRegistry.set(id, key, value).catch((reason) => {
                console.error(`Failed to set ${id}:${key} - ${reason.message}`);
            });
        },
        isToggled: args => args['theme'] === theme
    });
    commands.addCommand(CommandIDs.changeKeyMap, {
        label: args => {
            var _a;
            const theKeyMap = (_a = args['keyMap']) !== null && _a !== void 0 ? _a : keyMap;
            return theKeyMap === 'sublime'
                ? trans.__('Sublime Text')
                : trans.__(theKeyMap);
        },
        execute: args => {
            var _a;
            const key = 'keyMap';
            const value = (keyMap = (_a = args['keyMap']) !== null && _a !== void 0 ? _a : keyMap);
            return settingRegistry.set(id, key, value).catch((reason) => {
                console.error(`Failed to set ${id}:${key} - ${reason.message}`);
            });
        },
        isToggled: args => args['keyMap'] === keyMap
    });
    commands.addCommand(CommandIDs.find, {
        label: trans.__('Find…'),
        execute: () => {
            const widget = tracker.currentWidget;
            if (!widget) {
                return;
            }
            const editor = widget.content.editor;
            editor.execCommand(_codemirror_search__WEBPACK_IMPORTED_MODULE_8__.findNext);
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.goToLine, {
        label: trans.__('Go to Line…'),
        execute: args => {
            const widget = tracker.currentWidget;
            if (!widget) {
                return;
            }
            const editor = widget.content.editor;
            const line = args['line'];
            const column = args['column'];
            if (line !== undefined || column !== undefined) {
                editor.setCursorPosition({
                    line: (line !== null && line !== void 0 ? line : 1) - 1,
                    column: (column !== null && column !== void 0 ? column : 1) - 1
                });
            }
            else {
                editor.execCommand(_codemirror_search__WEBPACK_IMPORTED_MODULE_8__.gotoLine);
            }
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.changeMode, {
        label: args => {
            var _a;
            return (_a = args['name']) !== null && _a !== void 0 ? _a : trans.__('Change editor mode to the provided `name`.');
        },
        execute: args => {
            const name = args['name'];
            const widget = tracker.currentWidget;
            if (name && widget) {
                const spec = _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.Mode.findByName(name);
                if (spec) {
                    widget.content.model.mimeType = spec.mime;
                }
            }
        },
        isEnabled,
        isToggled: args => {
            const widget = tracker.currentWidget;
            if (!widget) {
                return false;
            }
            const mime = widget.content.model.mimeType;
            const spec = _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.Mode.findByMIME(mime);
            const name = spec && spec.name;
            return args['name'] === name;
        }
    });
    if (mainMenu) {
        const modeMenu = (_a = mainMenu.viewMenu.items.find(item => {
            var _a;
            return item.type === 'submenu' &&
                ((_a = item.submenu) === null || _a === void 0 ? void 0 : _a.id) === 'jp-mainmenu-view-codemirror-theme';
        })) === null || _a === void 0 ? void 0 : _a.submenu;
        if (modeMenu) {
            _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_2__.Mode.getModeInfo()
                .sort((a, b) => {
                const aName = a.name || '';
                const bName = b.name || '';
                return aName.localeCompare(bName);
            })
                .forEach(spec => {
                // Avoid mode name with a curse word.
                if (spec.name.indexOf('brainf') === 0) {
                    return;
                }
                modeMenu.addItem({
                    command: CommandIDs.changeMode,
                    args: Object.assign({}, spec) // TODO: Casting to `any` until lumino typings are fixed
                });
            });
        }
        // Add go to line capabilities to the edit menu.
        mainMenu.editMenu.goToLiners.add({
            id: CommandIDs.goToLine,
            isEnabled: (w) => tracker.currentWidget !== null && tracker.has(w)
        });
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29kZW1pcnJvci1leHRlbnNpb25fbGliX2luZGV4X2pzLmZiZjMwMjU4OTljNDY4MDBhMTE4LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTThCO0FBTUQ7QUFNQTtBQUVvQztBQUNuQjtBQUNjO0FBQ1o7QUFDRztBQUVFO0FBRXhEOztHQUVHO0FBQ0gsSUFBVSxVQUFVLENBVW5CO0FBVkQsV0FBVSxVQUFVO0lBQ0wsdUJBQVksR0FBRywwQkFBMEIsQ0FBQztJQUUxQyxzQkFBVyxHQUFHLHlCQUF5QixDQUFDO0lBRXhDLHFCQUFVLEdBQUcsd0JBQXdCLENBQUM7SUFFdEMsZUFBSSxHQUFHLGlCQUFpQixDQUFDO0lBRXpCLG1CQUFRLEdBQUcsdUJBQXVCLENBQUM7QUFDbEQsQ0FBQyxFQVZTLFVBQVUsS0FBVixVQUFVLFFBVW5CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLFFBQVEsR0FBMkM7SUFDdkQsRUFBRSxFQUFFLDJDQUEyQztJQUMvQyxRQUFRLEVBQUUsbUVBQWU7SUFDekIsUUFBUSxFQUFFLHNCQUFzQjtDQUNqQyxDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLFFBQVEsR0FBZ0M7SUFDNUMsRUFBRSxFQUFFLDJDQUEyQztJQUMvQyxRQUFRLEVBQUUsQ0FBQyxrRUFBYyxFQUFFLHlFQUFnQixFQUFFLGdFQUFXLENBQUM7SUFDekQsUUFBUSxFQUFFLENBQUMsMkRBQVMsQ0FBQztJQUNyQixRQUFRLEVBQUUsc0JBQXNCO0lBQ2hDLFNBQVMsRUFBRSxJQUFJO0NBQ2hCLENBQUM7QUFFRjs7R0FFRztBQUNJLE1BQU0sa0JBQWtCLEdBQWdDO0lBQzdELEVBQUUsRUFBRSx1REFBdUQ7SUFDM0QsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxrRUFBYyxFQUFFLDhEQUFTLEVBQUUsZ0VBQVcsQ0FBQztJQUNsRCxRQUFRLEVB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LElBQUksRUFBRSxDQUFDO2dCQUMzQixNQUFNLEtBQUssR0FBRyxDQUFDLENBQUMsSUFBSSxJQUFJLEVBQUUsQ0FBQztnQkFDM0IsT0FBTyxLQUFLLENBQUMsYUFBYSxDQUFDLEtBQUssQ0FBQyxDQUFDO1lBQ3BDLENBQUMsQ0FBQztpQkFDRCxPQUFPLENBQUMsSUFBSSxDQUFDLEVBQUU7Z0JBQ2QscUNBQXFDO2dCQUNyQyxJQUFJLElBQUksQ0FBQyxJQUFJLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBQyxLQUFLLENBQUMsRUFBRTtvQkFDckMsT0FBTztpQkFDUjtnQkFDRCxRQUFRLENBQUMsT0FBTyxDQUFDO29CQUNmLE9BQU8sRUFBRSxVQUFVLENBQUMsVUFBVTtvQkFDOUIsSUFBSSxFQUFFLGtCQUFLLElBQUksQ0FBUyxDQUFDLHdEQUF3RDtpQkFDbEYsQ0FBQyxDQUFDO1lBQ0wsQ0FBQyxDQUFDLENBQUM7U0FDTjtRQUNELGdEQUFnRDtRQUNoRCxRQUFRLENBQUMsUUFBUSxDQUFDLFVBQVUsQ0FBQyxHQUFHLENBQUM7WUFDL0IsRUFBRSxFQUFFLFVBQVUsQ0FBQyxRQUFRO1lBQ3ZCLFNBQVMsRUFBRSxDQUFDLENBQVMsRUFBRSxFQUFFLENBQUMsT0FBTyxDQUFDLGFBQWEsS0FBSyxJQUFJLElBQUksT0FBTyxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUM7U0FDM0UsQ0FBQyxDQUFDO0tBQ0o7QUFDSCxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvZGVtaXJyb3ItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBjb2RlbWlycm9yLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYWJTaGVsbCxcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHtcbiAgQ29kZUVkaXRvcixcbiAgSUVkaXRvclNlcnZpY2VzLFxuICBJUG9zaXRpb25Nb2RlbCxcbiAgTGluZUNvbFxufSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7XG4gIENvZGVNaXJyb3JFZGl0b3IsXG4gIGVkaXRvclNlcnZpY2VzLFxuICBFZGl0b3JTeW50YXhTdGF0dXMsXG4gIE1vZGVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZW1pcnJvcic7XG5pbXBvcnQgeyBJRG9jdW1lbnRXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBGaWxlRWRpdG9yLCBJRWRpdG9yVHJhY2tlciB9IGZyb20gJ0BqdXB5dGVybGFiL2ZpbGVlZGl0b3InO1xuaW1wb3J0IHsgSU1haW5NZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvbWFpbm1lbnUnO1xuaW1wb3J0IHsgSVNldHRpbmdSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3NldHRpbmdyZWdpc3RyeSc7XG5pbXBvcnQgeyBJU3RhdHVzQmFyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdHVzYmFyJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IGZpbmROZXh0LCBnb3RvTGluZSB9IGZyb20gJ0Bjb2RlbWlycm9yL3NlYXJjaCc7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIGNvZGVtaXJyb3IgcGx1Z2luLlxuICovXG5uYW1lc3BhY2UgQ29tbWFuZElEcyB7XG4gIGV4cG9ydCBjb25zdCBjaGFuZ2VLZXlNYXAgPSAnY29kZW1pcnJvcjpjaGFuZ2Uta2V5bWFwJztcblxuICBleHBvcnQgY29uc3QgY2hhbmdlVGhlbWUgPSAnY29kZW1pcnJvcjpjaGFuZ2UtdGhlbWUnO1xuXG4gIGV4cG9ydCBjb25zdCBjaGFuZ2VNb2RlID0gJ2NvZGVtaXJyb3I6Y2hhbmdlLW1vZGUnO1xuXG4gIGV4cG9ydCBjb25zdCBmaW5kID0gJ2NvZGVtaXJyb3I6ZmluZCc7XG5cbiAgZXhwb3J0IGNvbnN0IGdvVG9MaW5lID0gJ2NvZGVtaXJyb3I6Z28tdG8tbGluZSc7XG59XG5cbi8qKlxuICogVGhlIGVkaXRvciBzZXJ2aWNlcy5cbiAqL1xuY29uc3Qgc2VydmljZXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJRWRpdG9yU2VydmljZXM+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2NvZGVtaXJyb3ItZXh0ZW5zaW9uOnNlcnZpY2VzJyxcbiAgcHJvdmlkZXM6IElFZGl0b3JTZXJ2aWNlcyxcbiAgYWN0aXZhdGU6IGFjdGl2YXRlRWRpdG9yU2VydmljZXNcbn07XG5cbi8qKlxuICogVGhlIGVkaXRvciBjb21tYW5kcy5cbiAqL1xuY29uc3QgY29tbWFuZHM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb2RlbWlycm9yLWV4dGVuc2lvbjpjb21tYW5kcycsXG4gIHJlcXVpcmVzOiBbSUVkaXRvclRyYWNrZXIsIElTZXR0aW5nUmVnaXN0cnksIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJTWFpbk1lbnVdLFxuICBhY3RpdmF0ZTogYWN0aXZhdGVFZGl0b3JDb21tYW5kcyxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIFRoZSBKdXB5dGVyTGFiIHBsdWdpbiBmb3IgdGhlIEVkaXRvclN5bnRheCBzdGF0dXMgaXRlbS5cbiAqL1xuZXhwb3J0IGNvbnN0IGVkaXRvclN5bnRheFN0YXR1czogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2NvZGVtaXJyb3ItZXh0ZW5zaW9uOmVkaXRvci1zeW50YXgtc3RhdHVzJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lFZGl0b3JUcmFja2VyLCBJTGFiU2hlbGwsIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJU3RhdHVzQmFyXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFja2VyOiBJRWRpdG9yVHJhY2tlcixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHN0YXR1c0JhcjogSVN0YXR1c0JhciB8IG51bGxcbiAgKSA9PiB7XG4gICAgaWYgKCFzdGF0dXNCYXIpIHtcbiAgICAgIC8vIEF1dG9tYXRpY2FsbHkgZGlzYWJsZSBpZiBzdGF0dXNiYXIgbWlzc2luZ1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBpdGVtID0gbmV3IEVkaXRvclN5bnRheFN0YXR1cyh7IGNvbW1hbmRzOiBhcHAuY29tbWFuZHMsIHRyYW5zbGF0b3IgfSk7XG4gICAgbGFiU2hlbGwuY3VycmVudENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50ID0gbGFiU2hlbGwuY3VycmVudFdpZGdldDtcbiAgICAgIGlmIChjdXJyZW50ICYmIHRyYWNrZXIuaGFzKGN1cnJlbnQpICYmIGl0ZW0ubW9kZWwpIHtcbiAgICAgICAgaXRlbS5tb2RlbC5lZGl0b3IgPSAoXG4gICAgICAgICAgY3VycmVudCBhcyBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj5cbiAgICAgICAgKS5jb250ZW50LmVkaXRvcjtcbiAgICAgIH1cbiAgICB9KTtcbiAgICBzdGF0dXNCYXIucmVnaXN0ZXJTdGF0dXNJdGVtKFxuICAgICAgJ0BqdXB5dGVybGFiL2NvZGVtaXJyb3ItZXh0ZW5zaW9uOmVkaXRvci1zeW50YXgtc3RhdHVzJyxcbiAgICAgIHtcbiAgICAgICAgaXRlbSxcbiAgICAgICAgYWxpZ246ICdsZWZ0JyxcbiAgICAgICAgcmFuazogMCxcbiAgICAgICAgaXNBY3RpdmU6ICgpID0+XG4gICAgICAgICAgISFsYWJTaGVsbC5jdXJyZW50V2lkZ2V0ICYmXG4gICAgICAgICAgISF0cmFja2VyLmN1cnJlbnRXaWRnZXQgJiZcbiAgICAgICAgICBsYWJTaGVsbC5jdXJyZW50V2lkZ2V0ID09PSB0cmFja2VyLmN1cnJlbnRXaWRnZXRcbiAgICAgIH1cbiAgICApO1xuICB9XG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHByb3ZpZGluZyBhIGxpbmUvY29sdW1uIHN0YXR1cyBpdGVtIHRvIHRoZSBhcHBsaWNhdGlvbi5cbiAqL1xuZXhwb3J0IGNvbnN0IGxpbmVDb2xJdGVtOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVBvc2l0aW9uTW9kZWw+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2NvZGVtaXJyb3ItZXh0ZW5zaW9uOmxpbmUtY29sLXN0YXR1cycsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsLCBJU3RhdHVzQmFyXSxcbiAgcHJvdmlkZXM6IElQb3NpdGlvbk1vZGVsLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwgfCBudWxsLFxuICAgIHN0YXR1c0JhcjogSVN0YXR1c0JhciB8IG51bGxcbiAgKTogSVBvc2l0aW9uTW9kZWwgPT4ge1xuICAgIGNvbnN0IGl0ZW0gPSBuZXcgTGluZUNvbCh0cmFuc2xhdG9yKTtcblxuICAgIGNvbnN0IHByb3ZpZGVycyA9IG5ldyBTZXQ8XG4gICAgICAod2lkZ2V0OiBXaWRnZXQgfCBudWxsKSA9PiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsXG4gICAgPigpO1xuXG4gICAgaWYgKHN0YXR1c0Jhcikge1xuICAgICAgLy8gQWRkIHRoZSBzdGF0dXMgaXRlbSB0byB0aGUgc3RhdHVzIGJhci5cbiAgICAgIHN0YXR1c0Jhci5yZWdpc3RlclN0YXR1c0l0ZW0obGluZUNvbEl0ZW0uaWQsIHtcbiAgICAgICAgaXRlbSxcbiAgICAgICAgYWxpZ246ICdyaWdodCcsXG4gICAgICAgIHJhbms6IDIsXG4gICAgICAgIGlzQWN0aXZlOiAoKSA9PiAhIWl0ZW0ubW9kZWwuZWRpdG9yXG4gICAgICB9KTtcbiAgICB9XG5cbiAgICBjb25zdCBhZGRFZGl0b3JQcm92aWRlciA9IChcbiAgICAgIHByb3ZpZGVyOiAod2lkZ2V0OiBXaWRnZXQgfCBudWxsKSA9PiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsXG4gICAgKTogdm9pZCA9PiB7XG4gICAgICBwcm92aWRlcnMuYWRkKHByb3ZpZGVyKTtcblxuICAgICAgaWYgKGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0KSB7XG4gICAgICAgIHVwZGF0ZUVkaXRvcihhcHAuc2hlbGwsIHtcbiAgICAgICAgICBuZXdWYWx1ZTogYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXQsXG4gICAgICAgICAgb2xkVmFsdWU6IG51bGxcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfTtcblxuICAgIGNvbnN0IHVwZGF0ZSA9ICgpOiB2b2lkID0+IHtcbiAgICAgIHVwZGF0ZUVkaXRvcihhcHAuc2hlbGwsIHtcbiAgICAgICAgb2xkVmFsdWU6IGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0LFxuICAgICAgICBuZXdWYWx1ZTogYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXRcbiAgICAgIH0pO1xuICAgIH07XG5cbiAgICBmdW5jdGlvbiB1cGRhdGVFZGl0b3IoXG4gICAgICBzaGVsbDogSnVweXRlckZyb250RW5kLklTaGVsbCxcbiAgICAgIGNoYW5nZXM6IElMYWJTaGVsbC5JQ2hhbmdlZEFyZ3NcbiAgICApIHtcbiAgICAgIGl0ZW0ubW9kZWwuZWRpdG9yID1cbiAgICAgICAgWy4uLnByb3ZpZGVyc11cbiAgICAgICAgICAubWFwKHByb3ZpZGVyID0+IHByb3ZpZGVyKGNoYW5nZXMubmV3VmFsdWUpKVxuICAgICAgICAgIC5maWx0ZXIoZWRpdG9yID0+IGVkaXRvciAhPT0gbnVsbClbMF0gPz8gbnVsbDtcbiAgICB9XG5cbiAgICBpZiAobGFiU2hlbGwpIHtcbiAgICAgIGxhYlNoZWxsLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QodXBkYXRlRWRpdG9yKTtcbiAgICB9XG5cbiAgICByZXR1cm4geyBhZGRFZGl0b3JQcm92aWRlciwgdXBkYXRlIH07XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbXG4gIGNvbW1hbmRzLFxuICBzZXJ2aWNlcyxcbiAgZWRpdG9yU3ludGF4U3RhdHVzLFxuICBsaW5lQ29sSXRlbVxuXTtcbmV4cG9ydCBkZWZhdWx0IHBsdWdpbnM7XG5cbi8qKlxuICogVGhlIHBsdWdpbiBJRCB1c2VkIGFzIHRoZSBrZXkgaW4gdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gKi9cbmNvbnN0IGlkID0gY29tbWFuZHMuaWQ7XG5cbi8qKlxuICogU2V0IHVwIHRoZSBlZGl0b3Igc2VydmljZXMuXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlRWRpdG9yU2VydmljZXMoYXBwOiBKdXB5dGVyRnJvbnRFbmQpOiBJRWRpdG9yU2VydmljZXMge1xuICBDb2RlTWlycm9yRWRpdG9yLnByb3RvdHlwZS5zYXZlID0gKCkgPT4ge1xuICAgIHZvaWQgYXBwLmNvbW1hbmRzLmV4ZWN1dGUoJ2RvY21hbmFnZXI6c2F2ZScpO1xuICB9O1xuICByZXR1cm4gZWRpdG9yU2VydmljZXM7XG59XG5cbi8qKlxuICogU2V0IHVwIHRoZSBlZGl0b3Igd2lkZ2V0IG1lbnUgYW5kIGNvbW1hbmRzLlxuICovXG5mdW5jdGlvbiBhY3RpdmF0ZUVkaXRvckNvbW1hbmRzKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgdHJhY2tlcjogSUVkaXRvclRyYWNrZXIsXG4gIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIG1haW5NZW51OiBJTWFpbk1lbnUgfCBudWxsXG4pOiB2b2lkIHtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgY29uc3QgeyBjb21tYW5kcywgcmVzdG9yZWQgfSA9IGFwcDtcbiAgbGV0IHtcbiAgICB0aGVtZSxcbiAgICBrZXlNYXAsXG4gICAgc2Nyb2xsUGFzdEVuZCxcbiAgICBzdHlsZUFjdGl2ZUxpbmUsXG4gICAgc3R5bGVTZWxlY3RlZFRleHQsXG4gICAgc2VsZWN0aW9uUG9pbnRlcixcbiAgICBsaW5lV2lzZUNvcHlDdXRcbiAgfSA9IENvZGVNaXJyb3JFZGl0b3IuZGVmYXVsdENvbmZpZztcblxuICAvKipcbiAgICogVXBkYXRlIHRoZSBzZXR0aW5nIHZhbHVlcy5cbiAgICovXG4gIGFzeW5jIGZ1bmN0aW9uIHVwZGF0ZVNldHRpbmdzKFxuICAgIHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5nc1xuICApOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBrZXlNYXAgPSAoc2V0dGluZ3MuZ2V0KCdrZXlNYXAnKS5jb21wb3NpdGUgYXMgc3RyaW5nIHwgbnVsbCkgfHwga2V5TWFwO1xuXG4gICAgdGhlbWUgPSAoc2V0dGluZ3MuZ2V0KCd0aGVtZScpLmNvbXBvc2l0ZSBhcyBzdHJpbmcgfCBudWxsKSB8fCB0aGVtZTtcblxuICAgIHNjcm9sbFBhc3RFbmQgPVxuICAgICAgKHNldHRpbmdzLmdldCgnc2Nyb2xsUGFzdEVuZCcpLmNvbXBvc2l0ZSBhcyBib29sZWFuIHwgbnVsbCkgPz9cbiAgICAgIHNjcm9sbFBhc3RFbmQ7XG4gICAgc3R5bGVBY3RpdmVMaW5lID1cbiAgICAgIChzZXR0aW5ncy5nZXQoJ3N0eWxlQWN0aXZlTGluZScpLmNvbXBvc2l0ZSBhcyBib29sZWFuKSA/PyBzdHlsZUFjdGl2ZUxpbmU7XG4gICAgc3R5bGVTZWxlY3RlZFRleHQgPVxuICAgICAgKHNldHRpbmdzLmdldCgnc3R5bGVTZWxlY3RlZFRleHQnKS5jb21wb3NpdGUgYXMgYm9vbGVhbikgPz9cbiAgICAgIHN0eWxlU2VsZWN0ZWRUZXh0O1xuICAgIHNlbGVjdGlvblBvaW50ZXIgPVxuICAgICAgKHNldHRpbmdzLmdldCgnc2VsZWN0aW9uUG9pbnRlcicpLmNvbXBvc2l0ZSBhcyBib29sZWFuIHwgc3RyaW5nKSA/P1xuICAgICAgc2VsZWN0aW9uUG9pbnRlcjtcbiAgICBsaW5lV2lzZUNvcHlDdXQgPVxuICAgICAgKHNldHRpbmdzLmdldCgnbGluZVdpc2VDb3B5Q3V0JykuY29tcG9zaXRlIGFzIGJvb2xlYW4pID8/IGxpbmVXaXNlQ29weUN1dDtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGRhdGUgdGhlIHNldHRpbmdzIG9mIHRoZSBjdXJyZW50IHRyYWNrZXIgaW5zdGFuY2VzLlxuICAgKi9cbiAgZnVuY3Rpb24gdXBkYXRlVHJhY2tlcigpOiB2b2lkIHtcbiAgICBjb25zdCBlZGl0b3JPcHRpb25zOiBhbnkgPSB7XG4gICAgICBrZXlNYXAsXG4gICAgICB0aGVtZSxcbiAgICAgIHNjcm9sbFBhc3RFbmQsXG4gICAgICBzdHlsZUFjdGl2ZUxpbmUsXG4gICAgICBzdHlsZVNlbGVjdGVkVGV4dCxcbiAgICAgIHNlbGVjdGlvblBvaW50ZXIsXG4gICAgICBsaW5lV2lzZUNvcHlDdXRcbiAgICB9O1xuICAgIHRyYWNrZXIuZm9yRWFjaCh3aWRnZXQgPT4ge1xuICAgICAgaWYgKHdpZGdldC5jb250ZW50LmVkaXRvciBpbnN0YW5jZW9mIENvZGVNaXJyb3JFZGl0b3IpIHtcbiAgICAgICAgd2lkZ2V0LmNvbnRlbnQuZWRpdG9yLnNldE9wdGlvbnMoZWRpdG9yT3B0aW9ucyk7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICAvLyBGZXRjaCB0aGUgaW5pdGlhbCBzdGF0ZSBvZiB0aGUgc2V0dGluZ3MuXG4gIFByb21pc2UuYWxsKFtzZXR0aW5nUmVnaXN0cnkubG9hZChpZCksIHJlc3RvcmVkXSlcbiAgICAudGhlbihhc3luYyAoW3NldHRpbmdzXSkgPT4ge1xuICAgICAgYXdhaXQgdXBkYXRlU2V0dGluZ3Moc2V0dGluZ3MpO1xuICAgICAgdXBkYXRlVHJhY2tlcigpO1xuICAgICAgc2V0dGluZ3MuY2hhbmdlZC5jb25uZWN0KGFzeW5jICgpID0+IHtcbiAgICAgICAgYXdhaXQgdXBkYXRlU2V0dGluZ3Moc2V0dGluZ3MpO1xuICAgICAgICB1cGRhdGVUcmFja2VyKCk7XG4gICAgICB9KTtcbiAgICB9KVxuICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgY29uc29sZS5lcnJvcihyZWFzb24ubWVzc2FnZSk7XG4gICAgICB1cGRhdGVUcmFja2VyKCk7XG4gICAgfSk7XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgc2V0dGluZ3Mgb2YgbmV3IHdpZGdldHMuXG4gICAqL1xuICB0cmFja2VyLndpZGdldEFkZGVkLmNvbm5lY3QoKHNlbmRlciwgd2lkZ2V0KSA9PiB7XG4gICAgY29uc3QgZWRpdG9yT3B0aW9uczogYW55ID0ge1xuICAgICAga2V5TWFwLFxuICAgICAgdGhlbWUsXG4gICAgICBzY3JvbGxQYXN0RW5kLFxuICAgICAgc3R5bGVBY3RpdmVMaW5lLFxuICAgICAgc3R5bGVTZWxlY3RlZFRleHQsXG4gICAgICBzZWxlY3Rpb25Qb2ludGVyLFxuICAgICAgbGluZVdpc2VDb3B5Q3V0XG4gICAgfTtcbiAgICBpZiAod2lkZ2V0LmNvbnRlbnQuZWRpdG9yIGluc3RhbmNlb2YgQ29kZU1pcnJvckVkaXRvcikge1xuICAgICAgd2lkZ2V0LmNvbnRlbnQuZWRpdG9yLnNldE9wdGlvbnMoZWRpdG9yT3B0aW9ucyk7XG4gICAgfVxuICB9KTtcblxuICAvKipcbiAgICogQSB0ZXN0IGZvciB3aGV0aGVyIHRoZSB0cmFja2VyIGhhcyBhbiBhY3RpdmUgd2lkZ2V0LlxuICAgKi9cbiAgZnVuY3Rpb24gaXNFbmFibGVkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiAoXG4gICAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQgIT09IG51bGwgJiZcbiAgICAgIHRyYWNrZXIuY3VycmVudFdpZGdldCA9PT0gYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXRcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG1lbnUgZm9yIHRoZSBlZGl0b3IuXG4gICAqL1xuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2hhbmdlVGhlbWUsIHtcbiAgICBsYWJlbDogYXJncyA9PiAoYXJncy50aGVtZSBhcyBzdHJpbmcpID8/IHRoZW1lLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3Qga2V5ID0gJ3RoZW1lJztcbiAgICAgIGNvbnN0IHZhbHVlID0gKHRoZW1lID0gKGFyZ3NbJ3RoZW1lJ10gYXMgc3RyaW5nKSA/PyB0aGVtZSk7XG5cbiAgICAgIHJldHVybiBzZXR0aW5nUmVnaXN0cnkuc2V0KGlkLCBrZXksIHZhbHVlKS5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gc2V0ICR7aWR9OiR7a2V5fSAtICR7cmVhc29uLm1lc3NhZ2V9YCk7XG4gICAgICB9KTtcbiAgICB9LFxuICAgIGlzVG9nZ2xlZDogYXJncyA9PiBhcmdzWyd0aGVtZSddID09PSB0aGVtZVxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2hhbmdlS2V5TWFwLCB7XG4gICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgdGhlS2V5TWFwID0gKGFyZ3NbJ2tleU1hcCddIGFzIHN0cmluZykgPz8ga2V5TWFwO1xuICAgICAgcmV0dXJuIHRoZUtleU1hcCA9PT0gJ3N1YmxpbWUnXG4gICAgICAgID8gdHJhbnMuX18oJ1N1YmxpbWUgVGV4dCcpXG4gICAgICAgIDogdHJhbnMuX18odGhlS2V5TWFwKTtcbiAgICB9LFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3Qga2V5ID0gJ2tleU1hcCc7XG4gICAgICBjb25zdCB2YWx1ZSA9IChrZXlNYXAgPSAoYXJnc1sna2V5TWFwJ10gYXMgc3RyaW5nKSA/PyBrZXlNYXApO1xuXG4gICAgICByZXR1cm4gc2V0dGluZ1JlZ2lzdHJ5LnNldChpZCwga2V5LCB2YWx1ZSkuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIHNldCAke2lkfToke2tleX0gLSAke3JlYXNvbi5tZXNzYWdlfWApO1xuICAgICAgfSk7XG4gICAgfSxcbiAgICBpc1RvZ2dsZWQ6IGFyZ3MgPT4gYXJnc1sna2V5TWFwJ10gPT09IGtleU1hcFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZmluZCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnRmluZOKApicpLFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGVkaXRvciA9IHdpZGdldC5jb250ZW50LmVkaXRvciBhcyBDb2RlTWlycm9yRWRpdG9yO1xuICAgICAgZWRpdG9yLmV4ZWNDb21tYW5kKGZpbmROZXh0KTtcbiAgICB9LFxuICAgIGlzRW5hYmxlZFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZ29Ub0xpbmUsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0dvIHRvIExpbmXigKYnKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGVkaXRvciA9IHdpZGdldC5jb250ZW50LmVkaXRvciBhcyBDb2RlTWlycm9yRWRpdG9yO1xuXG4gICAgICBjb25zdCBsaW5lID0gYXJnc1snbGluZSddIGFzIG51bWJlciB8IHVuZGVmaW5lZDtcbiAgICAgIGNvbnN0IGNvbHVtbiA9IGFyZ3NbJ2NvbHVtbiddIGFzIG51bWJlciB8IHVuZGVmaW5lZDtcbiAgICAgIGlmIChsaW5lICE9PSB1bmRlZmluZWQgfHwgY29sdW1uICE9PSB1bmRlZmluZWQpIHtcbiAgICAgICAgZWRpdG9yLnNldEN1cnNvclBvc2l0aW9uKHtcbiAgICAgICAgICBsaW5lOiAobGluZSA/PyAxKSAtIDEsXG4gICAgICAgICAgY29sdW1uOiAoY29sdW1uID8/IDEpIC0gMVxuICAgICAgICB9KTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGVkaXRvci5leGVjQ29tbWFuZChnb3RvTGluZSk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpc0VuYWJsZWRcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNoYW5nZU1vZGUsIHtcbiAgICBsYWJlbDogYXJncyA9PlxuICAgICAgKGFyZ3NbJ25hbWUnXSBhcyBzdHJpbmcpID8/XG4gICAgICB0cmFucy5fXygnQ2hhbmdlIGVkaXRvciBtb2RlIHRvIHRoZSBwcm92aWRlZCBgbmFtZWAuJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBuYW1lID0gYXJnc1snbmFtZSddIGFzIHN0cmluZztcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIGlmIChuYW1lICYmIHdpZGdldCkge1xuICAgICAgICBjb25zdCBzcGVjID0gTW9kZS5maW5kQnlOYW1lKG5hbWUpO1xuICAgICAgICBpZiAoc3BlYykge1xuICAgICAgICAgIHdpZGdldC5jb250ZW50Lm1vZGVsLm1pbWVUeXBlID0gc3BlYy5taW1lIGFzIHN0cmluZztcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkLFxuICAgIGlzVG9nZ2xlZDogYXJncyA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG4gICAgICBjb25zdCBtaW1lID0gd2lkZ2V0LmNvbnRlbnQubW9kZWwubWltZVR5cGU7XG4gICAgICBjb25zdCBzcGVjID0gTW9kZS5maW5kQnlNSU1FKG1pbWUpO1xuICAgICAgY29uc3QgbmFtZSA9IHNwZWMgJiYgc3BlYy5uYW1lO1xuICAgICAgcmV0dXJuIGFyZ3NbJ25hbWUnXSA9PT0gbmFtZTtcbiAgICB9XG4gIH0pO1xuXG4gIGlmIChtYWluTWVudSkge1xuICAgIGNvbnN0IG1vZGVNZW51ID0gbWFpbk1lbnUudmlld01lbnUuaXRlbXMuZmluZChcbiAgICAgIGl0ZW0gPT5cbiAgICAgICAgaXRlbS50eXBlID09PSAnc3VibWVudScgJiZcbiAgICAgICAgaXRlbS5zdWJtZW51Py5pZCA9PT0gJ2pwLW1haW5tZW51LXZpZXctY29kZW1pcnJvci10aGVtZSdcbiAgICApPy5zdWJtZW51O1xuXG4gICAgaWYgKG1vZGVNZW51KSB7XG4gICAgICBNb2RlLmdldE1vZGVJbmZvKClcbiAgICAgICAgLnNvcnQoKGEsIGIpID0+IHtcbiAgICAgICAgICBjb25zdCBhTmFtZSA9IGEubmFtZSB8fCAnJztcbiAgICAgICAgICBjb25zdCBiTmFtZSA9IGIubmFtZSB8fCAnJztcbiAgICAgICAgICByZXR1cm4gYU5hbWUubG9jYWxlQ29tcGFyZShiTmFtZSk7XG4gICAgICAgIH0pXG4gICAgICAgIC5mb3JFYWNoKHNwZWMgPT4ge1xuICAgICAgICAgIC8vIEF2b2lkIG1vZGUgbmFtZSB3aXRoIGEgY3Vyc2Ugd29yZC5cbiAgICAgICAgICBpZiAoc3BlYy5uYW1lLmluZGV4T2YoJ2JyYWluZicpID09PSAwKSB7XG4gICAgICAgICAgICByZXR1cm47XG4gICAgICAgICAgfVxuICAgICAgICAgIG1vZGVNZW51LmFkZEl0ZW0oe1xuICAgICAgICAgICAgY29tbWFuZDogQ29tbWFuZElEcy5jaGFuZ2VNb2RlLFxuICAgICAgICAgICAgYXJnczogeyAuLi5zcGVjIH0gYXMgYW55IC8vIFRPRE86IENhc3RpbmcgdG8gYGFueWAgdW50aWwgbHVtaW5vIHR5cGluZ3MgYXJlIGZpeGVkXG4gICAgICAgICAgfSk7XG4gICAgICAgIH0pO1xuICAgIH1cbiAgICAvLyBBZGQgZ28gdG8gbGluZSBjYXBhYmlsaXRpZXMgdG8gdGhlIGVkaXQgbWVudS5cbiAgICBtYWluTWVudS5lZGl0TWVudS5nb1RvTGluZXJzLmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy5nb1RvTGluZSxcbiAgICAgIGlzRW5hYmxlZDogKHc6IFdpZGdldCkgPT4gdHJhY2tlci5jdXJyZW50V2lkZ2V0ICE9PSBudWxsICYmIHRyYWNrZXIuaGFzKHcpXG4gICAgfSk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==