"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_console-extension_lib_index_js"],{

/***/ "../../packages/console-extension/lib/foreign.js":
/*!*******************************************************!*\
  !*** ../../packages/console-extension/lib/foreign.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "foreign": () => (/* binding */ foreign)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/properties */ "webpack/sharing/consume/default/@lumino/properties/@lumino/properties");
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_properties__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * The console widget tracker provider.
 */
const foreign = {
    id: '@jupyterlab/console-extension:foreign',
    requires: [_jupyterlab_console__WEBPACK_IMPORTED_MODULE_1__.IConsoleTracker, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette],
    activate: activateForeign,
    autoStart: true
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (foreign);
function activateForeign(app, tracker, settingRegistry, translator, palette) {
    const trans = translator.load('jupyterlab');
    const { shell } = app;
    tracker.widgetAdded.connect((sender, widget) => {
        const console = widget.console;
        const handler = new _jupyterlab_console__WEBPACK_IMPORTED_MODULE_1__.ForeignHandler({
            sessionContext: console.sessionContext,
            parent: console
        });
        Private.foreignHandlerProperty.set(console, handler);
        // Property showAllKernelActivity configures foreign handler enabled on start.
        void settingRegistry
            .get('@jupyterlab/console-extension:tracker', 'showAllKernelActivity')
            .then(({ composite }) => {
            const showAllKernelActivity = composite;
            handler.enabled = showAllKernelActivity;
        });
        console.disposed.connect(() => {
            handler.dispose();
        });
    });
    const { commands } = app;
    const category = trans.__('Console');
    const toggleShowAllActivity = 'console:toggle-show-all-kernel-activity';
    // Get the current widget and activate unless the args specify otherwise.
    function getCurrent(args) {
        const widget = tracker.currentWidget;
        const activate = args['activate'] !== false;
        if (activate && widget) {
            shell.activateById(widget.id);
        }
        return widget;
    }
    commands.addCommand(toggleShowAllActivity, {
        label: args => trans.__('Show All Kernel Activity'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            const handler = Private.foreignHandlerProperty.get(current.console);
            if (handler) {
                handler.enabled = !handler.enabled;
            }
        },
        isToggled: () => {
            var _a;
            return tracker.currentWidget !== null &&
                !!((_a = Private.foreignHandlerProperty.get(tracker.currentWidget.console)) === null || _a === void 0 ? void 0 : _a.enabled);
        },
        isEnabled: () => tracker.currentWidget !== null &&
            tracker.currentWidget === shell.currentWidget
    });
    if (palette) {
        palette.addItem({
            command: toggleShowAllActivity,
            category,
            args: { isPalette: true }
        });
    }
}
/*
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * An attached property for a console's foreign handler.
     */
    Private.foreignHandlerProperty = new _lumino_properties__WEBPACK_IMPORTED_MODULE_4__.AttachedProperty({
        name: 'foreignHandler',
        create: () => undefined
    });
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/console-extension/lib/index.js":
/*!*****************************************************!*\
  !*** ../../packages/console-extension/lib/index.js ***!
  \*****************************************************/
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
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/completer */ "webpack/sharing/consume/default/@jupyterlab/completer/@jupyterlab/completer");
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_12__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_13__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var _foreign__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./foreign */ "../../packages/console-extension/lib/foreign.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module console-extension
 */
















/**
 * The command IDs used by the console plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.autoClosingBrackets = 'console:toggle-autoclosing-brackets';
    CommandIDs.create = 'console:create';
    CommandIDs.clear = 'console:clear';
    CommandIDs.runUnforced = 'console:run-unforced';
    CommandIDs.runForced = 'console:run-forced';
    CommandIDs.linebreak = 'console:linebreak';
    CommandIDs.interrupt = 'console:interrupt-kernel';
    CommandIDs.restart = 'console:restart-kernel';
    CommandIDs.closeAndShutdown = 'console:close-and-shutdown';
    CommandIDs.open = 'console:open';
    CommandIDs.inject = 'console:inject';
    CommandIDs.changeKernel = 'console:change-kernel';
    CommandIDs.getKernel = 'console:get-kernel';
    CommandIDs.enterToExecute = 'console:enter-to-execute';
    CommandIDs.shiftEnterToExecute = 'console:shift-enter-to-execute';
    CommandIDs.interactionMode = 'console:interaction-mode';
    CommandIDs.replaceSelection = 'console:replace-selection';
    CommandIDs.shutdown = 'console:shutdown';
    CommandIDs.invokeCompleter = 'completer:invoke-console';
    CommandIDs.selectCompleter = 'completer:select-console';
})(CommandIDs || (CommandIDs = {}));
/**
 * The console widget tracker provider.
 */
const tracker = {
    id: '@jupyterlab/console-extension:tracker',
    provides: _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.IConsoleTracker,
    requires: [
        _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.ConsolePanel.IContentFactory,
        _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices,
        _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_8__.IRenderMimeRegistry,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_9__.ISettingRegistry,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__.ITranslator
    ],
    optional: [
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_5__.IFileBrowserFactory,
        _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_7__.IMainMenu,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette,
        _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_6__.ILauncher,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabStatus,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ISessionContextDialogs
    ],
    activate: activateConsole,
    autoStart: true
};
/**
 * The console widget content factory.
 */
const factory = {
    id: '@jupyterlab/console-extension:factory',
    provides: _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.ConsolePanel.IContentFactory,
    requires: [_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices],
    autoStart: true,
    activate: (app, editorServices) => {
        const editorFactory = editorServices.factoryService.newInlineEditor;
        return new _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.ConsolePanel.ContentFactory({ editorFactory });
    }
};
/**
 * Kernel status indicator.
 */
const kernelStatus = {
    id: '@jupyterlab/console-extension:kernel-status',
    autoStart: true,
    requires: [_jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.IConsoleTracker, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IKernelStatusModel],
    activate: (app, tracker, kernelStatus) => {
        const provider = (widget) => {
            let session = null;
            if (widget && tracker.has(widget)) {
                return widget.sessionContext;
            }
            return session;
        };
        kernelStatus.addSessionProvider(provider);
    }
};
/**
 * Cursor position.
 */
const lineColStatus = {
    id: '@jupyterlab/console-extension:cursor-position',
    autoStart: true,
    requires: [_jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.IConsoleTracker, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IPositionModel],
    activate: (app, tracker, positionModel) => {
        let previousWidget = null;
        const provider = (widget) => {
            var _a, _b, _c, _d;
            let editor = null;
            if (widget !== previousWidget) {
                previousWidget === null || previousWidget === void 0 ? void 0 : previousWidget.console.promptCellCreated.disconnect(positionModel.update);
                previousWidget = null;
                if (widget && tracker.has(widget)) {
                    widget.console.promptCellCreated.connect(positionModel.update);
                    editor = (_b = (_a = widget.console.promptCell) === null || _a === void 0 ? void 0 : _a.editor) !== null && _b !== void 0 ? _b : null;
                    previousWidget = widget;
                }
            }
            else if (widget) {
                editor = (_d = (_c = widget.console.promptCell) === null || _c === void 0 ? void 0 : _c.editor) !== null && _d !== void 0 ? _d : null;
            }
            return editor;
        };
        positionModel.addEditorProvider(provider);
    }
};
const completerPlugin = {
    id: '@jupyterlab/console-extension:completer',
    autoStart: true,
    requires: [_jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.IConsoleTracker],
    optional: [_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_3__.ICompletionProviderManager],
    activate: activateConsoleCompleterService
};
/**
 * Export the plugins as the default.
 */
const plugins = [
    factory,
    tracker,
    _foreign__WEBPACK_IMPORTED_MODULE_15__["default"],
    kernelStatus,
    lineColStatus,
    completerPlugin
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * Activate the console extension.
 */
async function activateConsole(app, contentFactory, editorServices, rendermime, settingRegistry, translator, restorer, browserFactory, mainMenu, palette, launcher, status, sessionDialogs) {
    const trans = translator.load('jupyterlab');
    const manager = app.serviceManager;
    const { commands, shell } = app;
    const category = trans.__('Console');
    sessionDialogs = sessionDialogs !== null && sessionDialogs !== void 0 ? sessionDialogs : _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.sessionContextDialogs;
    // Create a widget tracker for all console panels.
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'console'
    });
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: CommandIDs.create,
            args: widget => {
                const { path, name, kernelPreference } = widget.console.sessionContext;
                return {
                    path,
                    name,
                    kernelPreference: Object.assign({}, kernelPreference)
                };
            },
            name: widget => { var _a; return (_a = widget.console.sessionContext.path) !== null && _a !== void 0 ? _a : _lumino_coreutils__WEBPACK_IMPORTED_MODULE_13__.UUID.uuid4(); },
            when: manager.ready
        });
    }
    // Add a launcher item if the launcher is available.
    if (launcher) {
        void manager.ready.then(() => {
            let disposables = null;
            const onSpecsChanged = () => {
                if (disposables) {
                    disposables.dispose();
                    disposables = null;
                }
                const specs = manager.kernelspecs.specs;
                if (!specs) {
                    return;
                }
                disposables = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_14__.DisposableSet();
                for (const name in specs.kernelspecs) {
                    const rank = name === specs.default ? 0 : Infinity;
                    const spec = specs.kernelspecs[name];
                    let kernelIconUrl = spec.resources['logo-64x64'];
                    disposables.add(launcher.add({
                        command: CommandIDs.create,
                        args: { isLauncher: true, kernelPreference: { name } },
                        category: trans.__('Console'),
                        rank,
                        kernelIconUrl,
                        metadata: {
                            kernel: _lumino_coreutils__WEBPACK_IMPORTED_MODULE_13__.JSONExt.deepCopy(spec.metadata || {})
                        }
                    }));
                }
            };
            onSpecsChanged();
            manager.kernelspecs.specsChanged.connect(onSpecsChanged);
        });
    }
    /**
     * Create a console for a given path.
     */
    async function createConsole(options) {
        var _a, _b;
        await manager.ready;
        const panel = new _jupyterlab_console__WEBPACK_IMPORTED_MODULE_4__.ConsolePanel(Object.assign({ manager,
            contentFactory, mimeTypeService: editorServices.mimeTypeService, rendermime,
            translator, setBusy: (_a = (status && (() => status.setBusy()))) !== null && _a !== void 0 ? _a : undefined }, options));
        const interactionMode = (await settingRegistry.get('@jupyterlab/console-extension:tracker', 'interactionMode')).composite;
        panel.console.node.dataset.jpInteractionMode = interactionMode;
        // Add the console panel to the tracker. We want the panel to show up before
        // any kernel selection dialog, so we do not await panel.session.ready;
        await tracker.add(panel);
        panel.sessionContext.propertyChanged.connect(() => {
            void tracker.save(panel);
        });
        shell.add(panel, 'main', {
            ref: options.ref,
            mode: options.insertMode,
            activate: options.activate !== false,
            type: (_b = options.type) !== null && _b !== void 0 ? _b : 'Console'
        });
        return panel;
    }
    const mapOption = (editor, config, option) => {
        if (config[option] === undefined) {
            return;
        }
        switch (option) {
            case 'autoClosingBrackets':
                editor.setOption('autoClosingBrackets', config['autoClosingBrackets']);
                break;
            case 'cursorBlinkRate':
                editor.setOption('cursorBlinkRate', config['cursorBlinkRate']);
                break;
            case 'fontFamily':
                editor.setOption('fontFamily', config['fontFamily']);
                break;
            case 'fontSize':
                editor.setOption('fontSize', config['fontSize']);
                break;
            case 'lineHeight':
                editor.setOption('lineHeight', config['lineHeight']);
                break;
            case 'lineNumbers':
                editor.setOption('lineNumbers', config['lineNumbers']);
                break;
            case 'lineWrap':
                editor.setOption('lineWrap', config['lineWrap']);
                break;
            case 'matchBrackets':
                editor.setOption('matchBrackets', config['matchBrackets']);
                break;
            case 'readOnly':
                editor.setOption('readOnly', config['readOnly']);
                break;
            case 'insertSpaces':
                editor.setOption('insertSpaces', config['insertSpaces']);
                break;
            case 'tabSize':
                editor.setOption('tabSize', config['tabSize']);
                break;
            case 'wordWrapColumn':
                editor.setOption('wordWrapColumn', config['wordWrapColumn']);
                break;
            case 'rulers':
                editor.setOption('rulers', config['rulers']);
                break;
            case 'codeFolding':
                editor.setOption('codeFolding', config['codeFolding']);
                break;
        }
    };
    const setOption = (editor, config) => {
        if (editor === undefined) {
            return;
        }
        mapOption(editor, config, 'autoClosingBrackets');
        mapOption(editor, config, 'cursorBlinkRate');
        mapOption(editor, config, 'fontFamily');
        mapOption(editor, config, 'fontSize');
        mapOption(editor, config, 'lineHeight');
        mapOption(editor, config, 'lineNumbers');
        mapOption(editor, config, 'lineWrap');
        mapOption(editor, config, 'matchBrackets');
        mapOption(editor, config, 'readOnly');
        mapOption(editor, config, 'insertSpaces');
        mapOption(editor, config, 'tabSize');
        mapOption(editor, config, 'wordWrapColumn');
        mapOption(editor, config, 'rulers');
        mapOption(editor, config, 'codeFolding');
    };
    const pluginId = '@jupyterlab/console-extension:tracker';
    let interactionMode;
    let promptCellConfig;
    /**
     * Update settings for one console or all consoles.
     *
     * @param panel Optional - single console to update.
     */
    async function updateSettings(panel) {
        interactionMode = (await settingRegistry.get(pluginId, 'interactionMode'))
            .composite;
        promptCellConfig = (await settingRegistry.get(pluginId, 'promptCellConfig'))
            .composite;
        const setWidgetOptions = (widget) => {
            var _a;
            widget.console.node.dataset.jpInteractionMode = interactionMode;
            // Update future promptCells
            widget.console.editorConfig = promptCellConfig;
            // Update promptCell already on screen
            setOption((_a = widget.console.promptCell) === null || _a === void 0 ? void 0 : _a.editor, promptCellConfig);
        };
        if (panel) {
            setWidgetOptions(panel);
        }
        else {
            tracker.forEach(setWidgetOptions);
        }
    }
    settingRegistry.pluginChanged.connect((sender, plugin) => {
        if (plugin === pluginId) {
            void updateSettings();
        }
    });
    await updateSettings();
    // Apply settings when a console is created.
    tracker.widgetAdded.connect((sender, panel) => {
        void updateSettings(panel);
    });
    commands.addCommand(CommandIDs.autoClosingBrackets, {
        execute: async (args) => {
            var _a;
            promptCellConfig.autoClosingBrackets = !!((_a = args['force']) !== null && _a !== void 0 ? _a : !promptCellConfig.autoClosingBrackets);
            await settingRegistry.set(pluginId, 'promptCellConfig', promptCellConfig);
        },
        label: trans.__('Auto Close Brackets for Code Console Prompt'),
        isToggled: () => promptCellConfig.autoClosingBrackets
    });
    /**
     * Whether there is an active console.
     */
    function isEnabled() {
        return (tracker.currentWidget !== null &&
            tracker.currentWidget === shell.currentWidget);
    }
    let command = CommandIDs.open;
    commands.addCommand(command, {
        label: trans.__('Open a console for the provided `path`.'),
        execute: (args) => {
            const path = args['path'];
            const widget = tracker.find(value => {
                var _a;
                return ((_a = value.console.sessionContext.session) === null || _a === void 0 ? void 0 : _a.path) === path;
            });
            if (widget) {
                if (args.activate !== false) {
                    shell.activateById(widget.id);
                }
                return widget;
            }
            else {
                return manager.ready.then(() => {
                    const model = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_12__.find)(manager.sessions.running(), item => {
                        return item.path === path;
                    });
                    if (model) {
                        return createConsole(args);
                    }
                    return Promise.reject(`No running kernel session for path: ${path}`);
                });
            }
        }
    });
    command = CommandIDs.create;
    commands.addCommand(command, {
        label: args => {
            var _a, _b, _c, _d;
            if (args['isPalette']) {
                return trans.__('New Console');
            }
            else if (args['isLauncher'] && args['kernelPreference']) {
                const kernelPreference = args['kernelPreference'];
                // TODO: Lumino command functions should probably be allowed to return undefined?
                return ((_d = (_c = (_b = (_a = manager.kernelspecs) === null || _a === void 0 ? void 0 : _a.specs) === null || _b === void 0 ? void 0 : _b.kernelspecs[kernelPreference.name || '']) === null || _c === void 0 ? void 0 : _c.display_name) !== null && _d !== void 0 ? _d : '');
            }
            return trans.__('Console');
        },
        icon: args => (args['isPalette'] ? undefined : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_11__.consoleIcon),
        execute: args => {
            var _a;
            const basePath = (_a = (args['basePath'] ||
                args['cwd'] ||
                (browserFactory === null || browserFactory === void 0 ? void 0 : browserFactory.defaultBrowser.model.path))) !== null && _a !== void 0 ? _a : '';
            return createConsole(Object.assign({ basePath }, args));
        }
    });
    // Get the current widget and activate unless the args specify otherwise.
    function getCurrent(args) {
        const widget = tracker.currentWidget;
        const activate = args['activate'] !== false;
        if (activate && widget) {
            shell.activateById(widget.id);
        }
        return widget !== null && widget !== void 0 ? widget : null;
    }
    commands.addCommand(CommandIDs.clear, {
        label: trans.__('Clear Console Cells'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            current.console.clear();
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.runUnforced, {
        label: trans.__('Run Cell (unforced)'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return current.console.execute();
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.runForced, {
        label: trans.__('Run Cell (forced)'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return current.console.execute(true);
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.linebreak, {
        label: trans.__('Insert Line Break'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            current.console.insertLinebreak();
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.replaceSelection, {
        label: trans.__('Replace Selection in Console'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            const text = args['text'] || '';
            current.console.replaceSelection(text);
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.interrupt, {
        label: trans.__('Interrupt Kernel'),
        execute: args => {
            var _a;
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            const kernel = (_a = current.console.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
            if (kernel) {
                return kernel.interrupt();
            }
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.restart, {
        label: trans.__('Restart Kernel…'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return sessionDialogs.restart(current.console.sessionContext, translator);
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.shutdown, {
        label: trans.__('Shut Down'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return current.console.sessionContext.shutdown();
        }
    });
    commands.addCommand(CommandIDs.closeAndShutdown, {
        label: trans.__('Close and Shut Down…'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                title: trans.__('Shut down the console?'),
                body: trans.__('Are you sure you want to close "%1"?', current.title.label),
                buttons: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton(), _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.warnButton()]
            }).then(result => {
                if (result.button.accept) {
                    return commands
                        .execute(CommandIDs.shutdown, { activate: false })
                        .then(() => {
                        current.dispose();
                        return true;
                    });
                }
                else {
                    return false;
                }
            });
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.inject, {
        label: trans.__('Inject some code in a console.'),
        execute: args => {
            const path = args['path'];
            tracker.find(widget => {
                var _a;
                if (((_a = widget.console.sessionContext.session) === null || _a === void 0 ? void 0 : _a.path) === path) {
                    if (args['activate'] !== false) {
                        shell.activateById(widget.id);
                    }
                    void widget.console.inject(args['code'], args['metadata']);
                    return true;
                }
                return false;
            });
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.changeKernel, {
        label: trans.__('Change Kernel…'),
        execute: args => {
            const current = getCurrent(args);
            if (!current) {
                return;
            }
            return sessionDialogs.selectKernel(current.console.sessionContext, translator);
        },
        isEnabled
    });
    commands.addCommand(CommandIDs.getKernel, {
        label: trans.__('Get Kernel'),
        execute: args => {
            var _a;
            const current = getCurrent(Object.assign({ activate: false }, args));
            if (!current) {
                return;
            }
            return (_a = current.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        },
        isEnabled
    });
    if (palette) {
        // Add command palette items
        [
            CommandIDs.create,
            CommandIDs.linebreak,
            CommandIDs.clear,
            CommandIDs.runUnforced,
            CommandIDs.runForced,
            CommandIDs.restart,
            CommandIDs.interrupt,
            CommandIDs.changeKernel,
            CommandIDs.closeAndShutdown
        ].forEach(command => {
            palette.addItem({ command, category, args: { isPalette: true } });
        });
    }
    if (mainMenu) {
        // Add a close and shutdown command to the file menu.
        mainMenu.fileMenu.closeAndCleaners.add({
            id: CommandIDs.closeAndShutdown,
            isEnabled
        });
        // Add a kernel user to the Kernel menu
        mainMenu.kernelMenu.kernelUsers.changeKernel.add({
            id: CommandIDs.changeKernel,
            isEnabled
        });
        mainMenu.kernelMenu.kernelUsers.clearWidget.add({
            id: CommandIDs.clear,
            isEnabled
        });
        mainMenu.kernelMenu.kernelUsers.interruptKernel.add({
            id: CommandIDs.interrupt,
            isEnabled
        });
        mainMenu.kernelMenu.kernelUsers.restartKernel.add({
            id: CommandIDs.restart,
            isEnabled
        });
        mainMenu.kernelMenu.kernelUsers.shutdownKernel.add({
            id: CommandIDs.shutdown,
            isEnabled
        });
        // Add a code runner to the Run menu.
        mainMenu.runMenu.codeRunners.run.add({
            id: CommandIDs.runForced,
            isEnabled
        });
        // Add a clearer to the edit menu
        mainMenu.editMenu.clearers.clearCurrent.add({
            id: CommandIDs.clear,
            isEnabled
        });
        // Add kernel information to the application help menu.
        mainMenu.helpMenu.getKernel.add({
            id: CommandIDs.getKernel,
            isEnabled
        });
    }
    // For backwards compatibility and clarity, we explicitly label the run
    // keystroke with the actual effected change, rather than the generic
    // "notebook" or "terminal" interaction mode. When this interaction mode
    // affects more than just the run keystroke, we can make this menu title more
    // generic.
    const runShortcutTitles = {
        notebook: trans.__('Execute with Shift+Enter'),
        terminal: trans.__('Execute with Enter')
    };
    // Add the execute keystroke setting submenu.
    commands.addCommand(CommandIDs.interactionMode, {
        label: args => {
            var _a;
            return (_a = runShortcutTitles[args['interactionMode']]) !== null && _a !== void 0 ? _a : 'Set the console interaction mode.';
        },
        execute: async (args) => {
            const key = 'keyMap';
            try {
                await settingRegistry.set(pluginId, 'interactionMode', args['interactionMode']);
            }
            catch (reason) {
                console.error(`Failed to set ${pluginId}:${key} - ${reason.message}`);
            }
        },
        isToggled: args => args['interactionMode'] === interactionMode
    });
    return tracker;
}
/**
 * Activate the completer service for console.
 */
function activateConsoleCompleterService(app, consoles, manager, translator) {
    if (!manager) {
        return;
    }
    const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_10__.nullTranslator).load('jupyterlab');
    app.commands.addCommand(CommandIDs.invokeCompleter, {
        label: trans.__('Display the completion helper.'),
        execute: () => {
            const id = consoles.currentWidget && consoles.currentWidget.id;
            if (id) {
                return manager.invoke(id);
            }
        }
    });
    app.commands.addCommand(CommandIDs.selectCompleter, {
        label: trans.__('Select the completion suggestion.'),
        execute: () => {
            const id = consoles.currentWidget && consoles.currentWidget.id;
            if (id) {
                return manager.select(id);
            }
        }
    });
    app.commands.addKeyBinding({
        command: CommandIDs.selectCompleter,
        keys: ['Enter'],
        selector: '.jp-ConsolePanel .jp-mod-completer-active'
    });
    const updateCompleter = async (_, consolePanel) => {
        var _a, _b;
        const completerContext = {
            editor: (_b = (_a = consolePanel.console.promptCell) === null || _a === void 0 ? void 0 : _a.editor) !== null && _b !== void 0 ? _b : null,
            session: consolePanel.console.sessionContext.session,
            widget: consolePanel
        };
        await manager.updateCompleter(completerContext);
        consolePanel.console.promptCellCreated.connect((codeConsole, cell) => {
            const newContext = {
                editor: cell.editor,
                session: codeConsole.sessionContext.session,
                widget: consolePanel
            };
            manager.updateCompleter(newContext).catch(console.error);
        });
        consolePanel.console.sessionContext.sessionChanged.connect(() => {
            var _a, _b;
            const newContext = {
                editor: (_b = (_a = consolePanel.console.promptCell) === null || _a === void 0 ? void 0 : _a.editor) !== null && _b !== void 0 ? _b : null,
                session: consolePanel.console.sessionContext.session,
                widget: consolePanel
            };
            manager.updateCompleter(newContext).catch(console.error);
        });
    };
    consoles.widgetAdded.connect(updateCompleter);
    manager.activeProvidersChanged.connect(() => {
        consoles.forEach(consoleWidget => {
            updateCompleter(undefined, consoleWidget).catch(e => console.error(e));
        });
    });
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29uc29sZS1leHRlbnNpb25fbGliX2luZGV4X2pzLjY2YTIwZTc5MzI4YjUzY2Q2YWM3LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFNSjtBQU0xQjtBQUNrQztBQUNUO0FBRUE7QUFFdEQ7O0dBRUc7QUFDSSxNQUFNLE9BQU8sR0FBZ0M7SUFDbEQsRUFBRSxFQUFFLHVDQUF1QztJQUMzQyxRQUFRLEVBQUUsQ0FBQyxnRUFBZSxFQUFFLHlFQUFnQixFQUFFLGdFQUFXLENBQUM7SUFDMUQsUUFBUSxFQUFFLENBQUMsaUVBQWUsQ0FBQztJQUMzQixRQUFRLEVBQUUsZUFBZTtJQUN6QixTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUYsaUVBQWUsT0FBTyxFQUFDO0FBRXZCLFNBQVMsZUFBZSxDQUN0QixHQUFvQixFQUNwQixPQUF3QixFQUN4QixlQUFpQyxFQUNqQyxVQUF1QixFQUN2QixPQUErQjtJQUUvQixNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sRUFBRSxLQUFLLEVBQUUsR0FBRyxHQUFHLENBQUM7SUFDdEIsT0FBTyxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsQ0FBQyxNQUFNLEVBQUUsTUFBTSxFQUFFLEVBQUU7UUFDN0MsTUFBTSxPQUFPLEdBQUcsTUFBTSxDQUFDLE9BQU8sQ0FBQztRQUUvQixNQUFNLE9BQU8sR0FBRyxJQUFJLCtEQUFjLENBQUM7WUFDakMsY0FBYyxFQUFFLE9BQU8sQ0FBQyxjQUFjO1lBQ3RDLE1BQU0sRUFBRSxPQUFPO1NBQ2hCLENBQUMsQ0FBQztRQUNILE9BQU8sQ0FBQyxzQkFBc0IsQ0FBQyxHQUFHLENBQUMsT0FBTyxFQUFFLE9BQU8sQ0FBQyxDQUFDO1FBRXJELDhFQUE4RTtRQUM5RSxLQUFLLGVBQWU7YUFDakIsR0FBRyxDQUFDLHVDQUF1QyxFQUFFLHVCQUF1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TCxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvbnNvbGUtZXh0ZW5zaW9uL3NyYy9mb3JlaWduLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb25zb2xlLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQge1xuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBJQ29tbWFuZFBhbGV0dGUgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQge1xuICBDb2RlQ29uc29sZSxcbiAgQ29uc29sZVBhbmVsLFxuICBGb3JlaWduSGFuZGxlcixcbiAgSUNvbnNvbGVUcmFja2VyXG59IGZyb20gJ0BqdXB5dGVybGFiL2NvbnNvbGUnO1xuaW1wb3J0IHsgSVNldHRpbmdSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3NldHRpbmdyZWdpc3RyeSc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3QgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBBdHRhY2hlZFByb3BlcnR5IH0gZnJvbSAnQGx1bWluby9wcm9wZXJ0aWVzJztcblxuLyoqXG4gKiBUaGUgY29uc29sZSB3aWRnZXQgdHJhY2tlciBwcm92aWRlci5cbiAqL1xuZXhwb3J0IGNvbnN0IGZvcmVpZ246IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb25zb2xlLWV4dGVuc2lvbjpmb3JlaWduJyxcbiAgcmVxdWlyZXM6IFtJQ29uc29sZVRyYWNrZXIsIElTZXR0aW5nUmVnaXN0cnksIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJQ29tbWFuZFBhbGV0dGVdLFxuICBhY3RpdmF0ZTogYWN0aXZhdGVGb3JlaWduLFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbmV4cG9ydCBkZWZhdWx0IGZvcmVpZ247XG5cbmZ1bmN0aW9uIGFjdGl2YXRlRm9yZWlnbihcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHRyYWNrZXI6IElDb25zb2xlVHJhY2tlcixcbiAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuKTogdm9pZCB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IHsgc2hlbGwgfSA9IGFwcDtcbiAgdHJhY2tlci53aWRnZXRBZGRlZC5jb25uZWN0KChzZW5kZXIsIHdpZGdldCkgPT4ge1xuICAgIGNvbnN0IGNvbnNvbGUgPSB3aWRnZXQuY29uc29sZTtcblxuICAgIGNvbnN0IGhhbmRsZXIgPSBuZXcgRm9yZWlnbkhhbmRsZXIoe1xuICAgICAgc2Vzc2lvbkNvbnRleHQ6IGNvbnNvbGUuc2Vzc2lvbkNvbnRleHQsXG4gICAgICBwYXJlbnQ6IGNvbnNvbGVcbiAgICB9KTtcbiAgICBQcml2YXRlLmZvcmVpZ25IYW5kbGVyUHJvcGVydHkuc2V0KGNvbnNvbGUsIGhhbmRsZXIpO1xuXG4gICAgLy8gUHJvcGVydHkgc2hvd0FsbEtlcm5lbEFjdGl2aXR5IGNvbmZpZ3VyZXMgZm9yZWlnbiBoYW5kbGVyIGVuYWJsZWQgb24gc3RhcnQuXG4gICAgdm9pZCBzZXR0aW5nUmVnaXN0cnlcbiAgICAgIC5nZXQoJ0BqdXB5dGVybGFiL2NvbnNvbGUtZXh0ZW5zaW9uOnRyYWNrZXInLCAnc2hvd0FsbEtlcm5lbEFjdGl2aXR5JylcbiAgICAgIC50aGVuKCh7IGNvbXBvc2l0ZSB9KSA9PiB7XG4gICAgICAgIGNvbnN0IHNob3dBbGxLZXJuZWxBY3Rpdml0eSA9IGNvbXBvc2l0ZSBhcyBib29sZWFuO1xuICAgICAgICBoYW5kbGVyLmVuYWJsZWQgPSBzaG93QWxsS2VybmVsQWN0aXZpdHk7XG4gICAgICB9KTtcblxuICAgIGNvbnNvbGUuZGlzcG9zZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICBoYW5kbGVyLmRpc3Bvc2UoKTtcbiAgICB9KTtcbiAgfSk7XG5cbiAgY29uc3QgeyBjb21tYW5kcyB9ID0gYXBwO1xuICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdDb25zb2xlJyk7XG4gIGNvbnN0IHRvZ2dsZVNob3dBbGxBY3Rpdml0eSA9ICdjb25zb2xlOnRvZ2dsZS1zaG93LWFsbC1rZXJuZWwtYWN0aXZpdHknO1xuXG4gIC8vIEdldCB0aGUgY3VycmVudCB3aWRnZXQgYW5kIGFjdGl2YXRlIHVubGVzcyB0aGUgYXJncyBzcGVjaWZ5IG90aGVyd2lzZS5cbiAgZnVuY3Rpb24gZ2V0Q3VycmVudChhcmdzOiBSZWFkb25seVBhcnRpYWxKU09OT2JqZWN0KTogQ29uc29sZVBhbmVsIHwgbnVsbCB7XG4gICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgIGNvbnN0IGFjdGl2YXRlID0gYXJnc1snYWN0aXZhdGUnXSAhPT0gZmFsc2U7XG4gICAgaWYgKGFjdGl2YXRlICYmIHdpZGdldCkge1xuICAgICAgc2hlbGwuYWN0aXZhdGVCeUlkKHdpZGdldC5pZCk7XG4gICAgfVxuICAgIHJldHVybiB3aWRnZXQ7XG4gIH1cblxuICBjb21tYW5kcy5hZGRDb21tYW5kKHRvZ2dsZVNob3dBbGxBY3Rpdml0eSwge1xuICAgIGxhYmVsOiBhcmdzID0+IHRyYW5zLl9fKCdTaG93IEFsbCBLZXJuZWwgQWN0aXZpdHknKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KGFyZ3MpO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGhhbmRsZXIgPSBQcml2YXRlLmZvcmVpZ25IYW5kbGVyUHJvcGVydHkuZ2V0KGN1cnJlbnQuY29uc29sZSk7XG4gICAgICBpZiAoaGFuZGxlcikge1xuICAgICAgICBoYW5kbGVyLmVuYWJsZWQgPSAhaGFuZGxlci5lbmFibGVkO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNUb2dnbGVkOiAoKSA9PlxuICAgICAgdHJhY2tlci5jdXJyZW50V2lkZ2V0ICE9PSBudWxsICYmXG4gICAgICAhIVByaXZhdGUuZm9yZWlnbkhhbmRsZXJQcm9wZXJ0eS5nZXQodHJhY2tlci5jdXJyZW50V2lkZ2V0LmNvbnNvbGUpXG4gICAgICAgID8uZW5hYmxlZCxcbiAgICBpc0VuYWJsZWQ6ICgpID0+XG4gICAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQgIT09IG51bGwgJiZcbiAgICAgIHRyYWNrZXIuY3VycmVudFdpZGdldCA9PT0gc2hlbGwuY3VycmVudFdpZGdldFxuICB9KTtcblxuICBpZiAocGFsZXR0ZSkge1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiB0b2dnbGVTaG93QWxsQWN0aXZpdHksXG4gICAgICBjYXRlZ29yeSxcbiAgICAgIGFyZ3M6IHsgaXNQYWxldHRlOiB0cnVlIH1cbiAgICB9KTtcbiAgfVxufVxuXG4vKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQW4gYXR0YWNoZWQgcHJvcGVydHkgZm9yIGEgY29uc29sZSdzIGZvcmVpZ24gaGFuZGxlci5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBmb3JlaWduSGFuZGxlclByb3BlcnR5ID0gbmV3IEF0dGFjaGVkUHJvcGVydHk8XG4gICAgQ29kZUNvbnNvbGUsXG4gICAgRm9yZWlnbkhhbmRsZXIgfCB1bmRlZmluZWRcbiAgPih7XG4gICAgbmFtZTogJ2ZvcmVpZ25IYW5kbGVyJyxcbiAgICBjcmVhdGU6ICgpID0+IHVuZGVmaW5lZFxuICB9KTtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNvbnNvbGUtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlN0YXR1cyxcbiAgSUxheW91dFJlc3RvcmVyLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBEaWFsb2csXG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSUtlcm5lbFN0YXR1c01vZGVsLFxuICBJU2Vzc2lvbkNvbnRleHQsXG4gIElTZXNzaW9uQ29udGV4dERpYWxvZ3MsXG4gIHNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgc2hvd0RpYWxvZyxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQge1xuICBDb2RlRWRpdG9yLFxuICBJRWRpdG9yU2VydmljZXMsXG4gIElQb3NpdGlvbk1vZGVsXG59IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0IHsgSUNvbXBsZXRpb25Qcm92aWRlck1hbmFnZXIgfSBmcm9tICdAanVweXRlcmxhYi9jb21wbGV0ZXInO1xuaW1wb3J0IHsgQ29uc29sZVBhbmVsLCBJQ29uc29sZVRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9jb25zb2xlJztcbmltcG9ydCB7IElGaWxlQnJvd3NlckZhY3RvcnkgfSBmcm9tICdAanVweXRlcmxhYi9maWxlYnJvd3Nlcic7XG5pbXBvcnQgeyBJTGF1bmNoZXIgfSBmcm9tICdAanVweXRlcmxhYi9sYXVuY2hlcic7XG5pbXBvcnQgeyBJTWFpbk1lbnUgfSBmcm9tICdAanVweXRlcmxhYi9tYWlubWVudSc7XG5pbXBvcnQgeyBJUmVuZGVyTWltZVJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGNvbnNvbGVJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBmaW5kIH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHtcbiAgSlNPTkV4dCxcbiAgSlNPTk9iamVjdCxcbiAgUmVhZG9ubHlKU09OVmFsdWUsXG4gIFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3QsXG4gIFVVSURcbn0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgRGlzcG9zYWJsZVNldCB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBEb2NrTGF5b3V0LCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IGZvcmVpZ24gZnJvbSAnLi9mb3JlaWduJztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgY29uc29sZSBwbHVnaW4uXG4gKi9cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IGF1dG9DbG9zaW5nQnJhY2tldHMgPSAnY29uc29sZTp0b2dnbGUtYXV0b2Nsb3NpbmctYnJhY2tldHMnO1xuXG4gIGV4cG9ydCBjb25zdCBjcmVhdGUgPSAnY29uc29sZTpjcmVhdGUnO1xuXG4gIGV4cG9ydCBjb25zdCBjbGVhciA9ICdjb25zb2xlOmNsZWFyJztcblxuICBleHBvcnQgY29uc3QgcnVuVW5mb3JjZWQgPSAnY29uc29sZTpydW4tdW5mb3JjZWQnO1xuXG4gIGV4cG9ydCBjb25zdCBydW5Gb3JjZWQgPSAnY29uc29sZTpydW4tZm9yY2VkJztcblxuICBleHBvcnQgY29uc3QgbGluZWJyZWFrID0gJ2NvbnNvbGU6bGluZWJyZWFrJztcblxuICBleHBvcnQgY29uc3QgaW50ZXJydXB0ID0gJ2NvbnNvbGU6aW50ZXJydXB0LWtlcm5lbCc7XG5cbiAgZXhwb3J0IGNvbnN0IHJlc3RhcnQgPSAnY29uc29sZTpyZXN0YXJ0LWtlcm5lbCc7XG5cbiAgZXhwb3J0IGNvbnN0IGNsb3NlQW5kU2h1dGRvd24gPSAnY29uc29sZTpjbG9zZS1hbmQtc2h1dGRvd24nO1xuXG4gIGV4cG9ydCBjb25zdCBvcGVuID0gJ2NvbnNvbGU6b3Blbic7XG5cbiAgZXhwb3J0IGNvbnN0IGluamVjdCA9ICdjb25zb2xlOmluamVjdCc7XG5cbiAgZXhwb3J0IGNvbnN0IGNoYW5nZUtlcm5lbCA9ICdjb25zb2xlOmNoYW5nZS1rZXJuZWwnO1xuXG4gIGV4cG9ydCBjb25zdCBnZXRLZXJuZWwgPSAnY29uc29sZTpnZXQta2VybmVsJztcblxuICBleHBvcnQgY29uc3QgZW50ZXJUb0V4ZWN1dGUgPSAnY29uc29sZTplbnRlci10by1leGVjdXRlJztcblxuICBleHBvcnQgY29uc3Qgc2hpZnRFbnRlclRvRXhlY3V0ZSA9ICdjb25zb2xlOnNoaWZ0LWVudGVyLXRvLWV4ZWN1dGUnO1xuXG4gIGV4cG9ydCBjb25zdCBpbnRlcmFjdGlvbk1vZGUgPSAnY29uc29sZTppbnRlcmFjdGlvbi1tb2RlJztcblxuICBleHBvcnQgY29uc3QgcmVwbGFjZVNlbGVjdGlvbiA9ICdjb25zb2xlOnJlcGxhY2Utc2VsZWN0aW9uJztcblxuICBleHBvcnQgY29uc3Qgc2h1dGRvd24gPSAnY29uc29sZTpzaHV0ZG93bic7XG5cbiAgZXhwb3J0IGNvbnN0IGludm9rZUNvbXBsZXRlciA9ICdjb21wbGV0ZXI6aW52b2tlLWNvbnNvbGUnO1xuXG4gIGV4cG9ydCBjb25zdCBzZWxlY3RDb21wbGV0ZXIgPSAnY29tcGxldGVyOnNlbGVjdC1jb25zb2xlJztcbn1cblxuLyoqXG4gKiBUaGUgY29uc29sZSB3aWRnZXQgdHJhY2tlciBwcm92aWRlci5cbiAqL1xuY29uc3QgdHJhY2tlcjogSnVweXRlckZyb250RW5kUGx1Z2luPElDb25zb2xlVHJhY2tlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29uc29sZS1leHRlbnNpb246dHJhY2tlcicsXG4gIHByb3ZpZGVzOiBJQ29uc29sZVRyYWNrZXIsXG4gIHJlcXVpcmVzOiBbXG4gICAgQ29uc29sZVBhbmVsLklDb250ZW50RmFjdG9yeSxcbiAgICBJRWRpdG9yU2VydmljZXMsXG4gICAgSVJlbmRlck1pbWVSZWdpc3RyeSxcbiAgICBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIElUcmFuc2xhdG9yXG4gIF0sXG4gIG9wdGlvbmFsOiBbXG4gICAgSUxheW91dFJlc3RvcmVyLFxuICAgIElGaWxlQnJvd3NlckZhY3RvcnksXG4gICAgSU1haW5NZW51LFxuICAgIElDb21tYW5kUGFsZXR0ZSxcbiAgICBJTGF1bmNoZXIsXG4gICAgSUxhYlN0YXR1cyxcbiAgICBJU2Vzc2lvbkNvbnRleHREaWFsb2dzXG4gIF0sXG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUNvbnNvbGUsXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBUaGUgY29uc29sZSB3aWRnZXQgY29udGVudCBmYWN0b3J5LlxuICovXG5jb25zdCBmYWN0b3J5OiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48Q29uc29sZVBhbmVsLklDb250ZW50RmFjdG9yeT4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29uc29sZS1leHRlbnNpb246ZmFjdG9yeScsXG4gIHByb3ZpZGVzOiBDb25zb2xlUGFuZWwuSUNvbnRlbnRGYWN0b3J5LFxuICByZXF1aXJlczogW0lFZGl0b3JTZXJ2aWNlc10sXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgYWN0aXZhdGU6IChhcHA6IEp1cHl0ZXJGcm9udEVuZCwgZWRpdG9yU2VydmljZXM6IElFZGl0b3JTZXJ2aWNlcykgPT4ge1xuICAgIGNvbnN0IGVkaXRvckZhY3RvcnkgPSBlZGl0b3JTZXJ2aWNlcy5mYWN0b3J5U2VydmljZS5uZXdJbmxpbmVFZGl0b3I7XG4gICAgcmV0dXJuIG5ldyBDb25zb2xlUGFuZWwuQ29udGVudEZhY3RvcnkoeyBlZGl0b3JGYWN0b3J5IH0pO1xuICB9XG59O1xuXG4vKipcbiAqIEtlcm5lbCBzdGF0dXMgaW5kaWNhdG9yLlxuICovXG5jb25zdCBrZXJuZWxTdGF0dXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb25zb2xlLWV4dGVuc2lvbjprZXJuZWwtc3RhdHVzJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lDb25zb2xlVHJhY2tlciwgSUtlcm5lbFN0YXR1c01vZGVsXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0cmFja2VyOiBJQ29uc29sZVRyYWNrZXIsXG4gICAga2VybmVsU3RhdHVzOiBJS2VybmVsU3RhdHVzTW9kZWxcbiAgKSA9PiB7XG4gICAgY29uc3QgcHJvdmlkZXIgPSAod2lkZ2V0OiBXaWRnZXQgfCBudWxsKSA9PiB7XG4gICAgICBsZXQgc2Vzc2lvbjogSVNlc3Npb25Db250ZXh0IHwgbnVsbCA9IG51bGw7XG5cbiAgICAgIGlmICh3aWRnZXQgJiYgdHJhY2tlci5oYXMod2lkZ2V0KSkge1xuICAgICAgICByZXR1cm4gKHdpZGdldCBhcyBDb25zb2xlUGFuZWwpLnNlc3Npb25Db250ZXh0O1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gc2Vzc2lvbjtcbiAgICB9O1xuXG4gICAga2VybmVsU3RhdHVzLmFkZFNlc3Npb25Qcm92aWRlcihwcm92aWRlcik7XG4gIH1cbn07XG5cbi8qKlxuICogQ3Vyc29yIHBvc2l0aW9uLlxuICovXG5jb25zdCBsaW5lQ29sU3RhdHVzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY29uc29sZS1leHRlbnNpb246Y3Vyc29yLXBvc2l0aW9uJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICByZXF1aXJlczogW0lDb25zb2xlVHJhY2tlciwgSVBvc2l0aW9uTW9kZWxdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYWNrZXI6IElDb25zb2xlVHJhY2tlcixcbiAgICBwb3NpdGlvbk1vZGVsOiBJUG9zaXRpb25Nb2RlbFxuICApID0+IHtcbiAgICBsZXQgcHJldmlvdXNXaWRnZXQ6IENvbnNvbGVQYW5lbCB8IG51bGwgPSBudWxsO1xuXG4gICAgY29uc3QgcHJvdmlkZXIgPSAod2lkZ2V0OiBXaWRnZXQgfCBudWxsKSA9PiB7XG4gICAgICBsZXQgZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsID0gbnVsbDtcbiAgICAgIGlmICh3aWRnZXQgIT09IHByZXZpb3VzV2lkZ2V0KSB7XG4gICAgICAgIHByZXZpb3VzV2lkZ2V0Py5jb25zb2xlLnByb21wdENlbGxDcmVhdGVkLmRpc2Nvbm5lY3QoXG4gICAgICAgICAgcG9zaXRpb25Nb2RlbC51cGRhdGVcbiAgICAgICAgKTtcblxuICAgICAgICBwcmV2aW91c1dpZGdldCA9IG51bGw7XG4gICAgICAgIGlmICh3aWRnZXQgJiYgdHJhY2tlci5oYXMod2lkZ2V0KSkge1xuICAgICAgICAgICh3aWRnZXQgYXMgQ29uc29sZVBhbmVsKS5jb25zb2xlLnByb21wdENlbGxDcmVhdGVkLmNvbm5lY3QoXG4gICAgICAgICAgICBwb3NpdGlvbk1vZGVsLnVwZGF0ZVxuICAgICAgICAgICk7XG4gICAgICAgICAgZWRpdG9yID0gKHdpZGdldCBhcyBDb25zb2xlUGFuZWwpLmNvbnNvbGUucHJvbXB0Q2VsbD8uZWRpdG9yID8/IG51bGw7XG4gICAgICAgICAgcHJldmlvdXNXaWRnZXQgPSB3aWRnZXQgYXMgQ29uc29sZVBhbmVsO1xuICAgICAgICB9XG4gICAgICB9IGVsc2UgaWYgKHdpZGdldCkge1xuICAgICAgICBlZGl0b3IgPSAod2lkZ2V0IGFzIENvbnNvbGVQYW5lbCkuY29uc29sZS5wcm9tcHRDZWxsPy5lZGl0b3IgPz8gbnVsbDtcbiAgICAgIH1cbiAgICAgIHJldHVybiBlZGl0b3I7XG4gICAgfTtcblxuICAgIHBvc2l0aW9uTW9kZWwuYWRkRWRpdG9yUHJvdmlkZXIocHJvdmlkZXIpO1xuICB9XG59O1xuXG5jb25zdCBjb21wbGV0ZXJQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb25zb2xlLWV4dGVuc2lvbjpjb21wbGV0ZXInLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSUNvbnNvbGVUcmFja2VyXSxcbiAgb3B0aW9uYWw6IFtJQ29tcGxldGlvblByb3ZpZGVyTWFuYWdlcl0sXG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUNvbnNvbGVDb21wbGV0ZXJTZXJ2aWNlXG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2lucyBhcyB0aGUgZGVmYXVsdC5cbiAqL1xuY29uc3QgcGx1Z2luczogSnVweXRlckZyb250RW5kUGx1Z2luPGFueT5bXSA9IFtcbiAgZmFjdG9yeSxcbiAgdHJhY2tlcixcbiAgZm9yZWlnbixcbiAga2VybmVsU3RhdHVzLFxuICBsaW5lQ29sU3RhdHVzLFxuICBjb21wbGV0ZXJQbHVnaW5cbl07XG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuXG4vKipcbiAqIEFjdGl2YXRlIHRoZSBjb25zb2xlIGV4dGVuc2lvbi5cbiAqL1xuYXN5bmMgZnVuY3Rpb24gYWN0aXZhdGVDb25zb2xlKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgY29udGVudEZhY3Rvcnk6IENvbnNvbGVQYW5lbC5JQ29udGVudEZhY3RvcnksXG4gIGVkaXRvclNlcnZpY2VzOiBJRWRpdG9yU2VydmljZXMsXG4gIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnksXG4gIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICBicm93c2VyRmFjdG9yeTogSUZpbGVCcm93c2VyRmFjdG9yeSB8IG51bGwsXG4gIG1haW5NZW51OiBJTWFpbk1lbnUgfCBudWxsLFxuICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsLFxuICBsYXVuY2hlcjogSUxhdW5jaGVyIHwgbnVsbCxcbiAgc3RhdHVzOiBJTGFiU3RhdHVzIHwgbnVsbCxcbiAgc2Vzc2lvbkRpYWxvZ3M6IElTZXNzaW9uQ29udGV4dERpYWxvZ3MgfCBudWxsXG4pOiBQcm9taXNlPElDb25zb2xlVHJhY2tlcj4ge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCBtYW5hZ2VyID0gYXBwLnNlcnZpY2VNYW5hZ2VyO1xuICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdDb25zb2xlJyk7XG4gIHNlc3Npb25EaWFsb2dzID0gc2Vzc2lvbkRpYWxvZ3MgPz8gc2Vzc2lvbkNvbnRleHREaWFsb2dzO1xuXG4gIC8vIENyZWF0ZSBhIHdpZGdldCB0cmFja2VyIGZvciBhbGwgY29uc29sZSBwYW5lbHMuXG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxDb25zb2xlUGFuZWw+KHtcbiAgICBuYW1lc3BhY2U6ICdjb25zb2xlJ1xuICB9KTtcblxuICAvLyBIYW5kbGUgc3RhdGUgcmVzdG9yYXRpb24uXG4gIGlmIChyZXN0b3Jlcikge1xuICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLmNyZWF0ZSxcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiB7XG4gICAgICAgIGNvbnN0IHsgcGF0aCwgbmFtZSwga2VybmVsUHJlZmVyZW5jZSB9ID0gd2lkZ2V0LmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQ7XG4gICAgICAgIHJldHVybiB7XG4gICAgICAgICAgcGF0aCxcbiAgICAgICAgICBuYW1lLFxuICAgICAgICAgIGtlcm5lbFByZWZlcmVuY2U6IHsgLi4ua2VybmVsUHJlZmVyZW5jZSB9XG4gICAgICAgIH07XG4gICAgICB9LFxuICAgICAgbmFtZTogd2lkZ2V0ID0+IHdpZGdldC5jb25zb2xlLnNlc3Npb25Db250ZXh0LnBhdGggPz8gVVVJRC51dWlkNCgpLFxuICAgICAgd2hlbjogbWFuYWdlci5yZWFkeVxuICAgIH0pO1xuICB9XG5cbiAgLy8gQWRkIGEgbGF1bmNoZXIgaXRlbSBpZiB0aGUgbGF1bmNoZXIgaXMgYXZhaWxhYmxlLlxuICBpZiAobGF1bmNoZXIpIHtcbiAgICB2b2lkIG1hbmFnZXIucmVhZHkudGhlbigoKSA9PiB7XG4gICAgICBsZXQgZGlzcG9zYWJsZXM6IERpc3Bvc2FibGVTZXQgfCBudWxsID0gbnVsbDtcbiAgICAgIGNvbnN0IG9uU3BlY3NDaGFuZ2VkID0gKCkgPT4ge1xuICAgICAgICBpZiAoZGlzcG9zYWJsZXMpIHtcbiAgICAgICAgICBkaXNwb3NhYmxlcy5kaXNwb3NlKCk7XG4gICAgICAgICAgZGlzcG9zYWJsZXMgPSBudWxsO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHNwZWNzID0gbWFuYWdlci5rZXJuZWxzcGVjcy5zcGVjcztcbiAgICAgICAgaWYgKCFzcGVjcykge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBkaXNwb3NhYmxlcyA9IG5ldyBEaXNwb3NhYmxlU2V0KCk7XG4gICAgICAgIGZvciAoY29uc3QgbmFtZSBpbiBzcGVjcy5rZXJuZWxzcGVjcykge1xuICAgICAgICAgIGNvbnN0IHJhbmsgPSBuYW1lID09PSBzcGVjcy5kZWZhdWx0ID8gMCA6IEluZmluaXR5O1xuICAgICAgICAgIGNvbnN0IHNwZWMgPSBzcGVjcy5rZXJuZWxzcGVjc1tuYW1lXSE7XG4gICAgICAgICAgbGV0IGtlcm5lbEljb25VcmwgPSBzcGVjLnJlc291cmNlc1snbG9nby02NHg2NCddO1xuICAgICAgICAgIGRpc3Bvc2FibGVzLmFkZChcbiAgICAgICAgICAgIGxhdW5jaGVyLmFkZCh7XG4gICAgICAgICAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuY3JlYXRlLFxuICAgICAgICAgICAgICBhcmdzOiB7IGlzTGF1bmNoZXI6IHRydWUsIGtlcm5lbFByZWZlcmVuY2U6IHsgbmFtZSB9IH0sXG4gICAgICAgICAgICAgIGNhdGVnb3J5OiB0cmFucy5fXygnQ29uc29sZScpLFxuICAgICAgICAgICAgICByYW5rLFxuICAgICAgICAgICAgICBrZXJuZWxJY29uVXJsLFxuICAgICAgICAgICAgICBtZXRhZGF0YToge1xuICAgICAgICAgICAgICAgIGtlcm5lbDogSlNPTkV4dC5kZWVwQ29weShcbiAgICAgICAgICAgICAgICAgIHNwZWMubWV0YWRhdGEgfHwge31cbiAgICAgICAgICAgICAgICApIGFzIFJlYWRvbmx5SlNPTlZhbHVlXG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0pXG4gICAgICAgICAgKTtcbiAgICAgICAgfVxuICAgICAgfTtcbiAgICAgIG9uU3BlY3NDaGFuZ2VkKCk7XG4gICAgICBtYW5hZ2VyLmtlcm5lbHNwZWNzLnNwZWNzQ2hhbmdlZC5jb25uZWN0KG9uU3BlY3NDaGFuZ2VkKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhIHdpZGdldC5cbiAgICovXG4gIGludGVyZmFjZSBJQ3JlYXRlT3B0aW9ucyBleHRlbmRzIFBhcnRpYWw8Q29uc29sZVBhbmVsLklPcHRpb25zPiB7XG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBhY3RpdmF0ZSB0aGUgd2lkZ2V0LiAgRGVmYXVsdHMgdG8gYHRydWVgLlxuICAgICAqL1xuICAgIGFjdGl2YXRlPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSByZWZlcmVuY2Ugd2lkZ2V0IGlkIGZvciB0aGUgaW5zZXJ0IGxvY2F0aW9uLlxuICAgICAqXG4gICAgICogVGhlIGRlZmF1bHQgaXMgYG51bGxgLlxuICAgICAqL1xuICAgIHJlZj86IHN0cmluZyB8IG51bGw7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdGFiIGluc2VydCBtb2RlLlxuICAgICAqXG4gICAgICogQW4gaW5zZXJ0IG1vZGUgaXMgdXNlZCB0byBzcGVjaWZ5IGhvdyBhIHdpZGdldCBzaG91bGQgYmUgYWRkZWRcbiAgICAgKiB0byB0aGUgbWFpbiBhcmVhIHJlbGF0aXZlIHRvIGEgcmVmZXJlbmNlIHdpZGdldC5cbiAgICAgKi9cbiAgICBpbnNlcnRNb2RlPzogRG9ja0xheW91dC5JbnNlcnRNb2RlO1xuXG4gICAgLyoqXG4gICAgICogVHlwZSBvZiB3aWRnZXQgdG8gb3BlblxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoaXMgaXMgdGhlIGtleSB1c2VkIHRvIGxvYWQgdXNlciBsYXlvdXQgY3VzdG9taXphdGlvbi5cbiAgICAgKiBJdHMgdHlwaWNhbCB2YWx1ZSBpczogYSBmYWN0b3J5IG5hbWUgb3IgdGhlIHdpZGdldCBpZCAoaWYgc2luZ2xldG9uKVxuICAgICAqL1xuICAgIHR5cGU/OiBzdHJpbmc7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgY29uc29sZSBmb3IgYSBnaXZlbiBwYXRoLlxuICAgKi9cbiAgYXN5bmMgZnVuY3Rpb24gY3JlYXRlQ29uc29sZShvcHRpb25zOiBJQ3JlYXRlT3B0aW9ucyk6IFByb21pc2U8Q29uc29sZVBhbmVsPiB7XG4gICAgYXdhaXQgbWFuYWdlci5yZWFkeTtcblxuICAgIGNvbnN0IHBhbmVsID0gbmV3IENvbnNvbGVQYW5lbCh7XG4gICAgICBtYW5hZ2VyLFxuICAgICAgY29udGVudEZhY3RvcnksXG4gICAgICBtaW1lVHlwZVNlcnZpY2U6IGVkaXRvclNlcnZpY2VzLm1pbWVUeXBlU2VydmljZSxcbiAgICAgIHJlbmRlcm1pbWUsXG4gICAgICB0cmFuc2xhdG9yLFxuICAgICAgc2V0QnVzeTogKHN0YXR1cyAmJiAoKCkgPT4gc3RhdHVzLnNldEJ1c3koKSkpID8/IHVuZGVmaW5lZCxcbiAgICAgIC4uLihvcHRpb25zIGFzIFBhcnRpYWw8Q29uc29sZVBhbmVsLklPcHRpb25zPilcbiAgICB9KTtcblxuICAgIGNvbnN0IGludGVyYWN0aW9uTW9kZTogc3RyaW5nID0gKFxuICAgICAgYXdhaXQgc2V0dGluZ1JlZ2lzdHJ5LmdldChcbiAgICAgICAgJ0BqdXB5dGVybGFiL2NvbnNvbGUtZXh0ZW5zaW9uOnRyYWNrZXInLFxuICAgICAgICAnaW50ZXJhY3Rpb25Nb2RlJ1xuICAgICAgKVxuICAgICkuY29tcG9zaXRlIGFzIHN0cmluZztcbiAgICBwYW5lbC5jb25zb2xlLm5vZGUuZGF0YXNldC5qcEludGVyYWN0aW9uTW9kZSA9IGludGVyYWN0aW9uTW9kZTtcblxuICAgIC8vIEFkZCB0aGUgY29uc29sZSBwYW5lbCB0byB0aGUgdHJhY2tlci4gV2Ugd2FudCB0aGUgcGFuZWwgdG8gc2hvdyB1cCBiZWZvcmVcbiAgICAvLyBhbnkga2VybmVsIHNlbGVjdGlvbiBkaWFsb2csIHNvIHdlIGRvIG5vdCBhd2FpdCBwYW5lbC5zZXNzaW9uLnJlYWR5O1xuICAgIGF3YWl0IHRyYWNrZXIuYWRkKHBhbmVsKTtcbiAgICBwYW5lbC5zZXNzaW9uQ29udGV4dC5wcm9wZXJ0eUNoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB2b2lkIHRyYWNrZXIuc2F2ZShwYW5lbCk7XG4gICAgfSk7XG5cbiAgICBzaGVsbC5hZGQocGFuZWwsICdtYWluJywge1xuICAgICAgcmVmOiBvcHRpb25zLnJlZixcbiAgICAgIG1vZGU6IG9wdGlvbnMuaW5zZXJ0TW9kZSxcbiAgICAgIGFjdGl2YXRlOiBvcHRpb25zLmFjdGl2YXRlICE9PSBmYWxzZSxcbiAgICAgIHR5cGU6IG9wdGlvbnMudHlwZSA/PyAnQ29uc29sZSdcbiAgICB9KTtcbiAgICByZXR1cm4gcGFuZWw7XG4gIH1cblxuICB0eXBlIGxpbmVXcmFwX3R5cGUgPSAnb2ZmJyB8ICdvbicgfCAnd29yZFdyYXBDb2x1bW4nIHwgJ2JvdW5kZWQnO1xuXG4gIGNvbnN0IG1hcE9wdGlvbiA9IChcbiAgICBlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvcixcbiAgICBjb25maWc6IEpTT05PYmplY3QsXG4gICAgb3B0aW9uOiBzdHJpbmdcbiAgKSA9PiB7XG4gICAgaWYgKGNvbmZpZ1tvcHRpb25dID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgc3dpdGNoIChvcHRpb24pIHtcbiAgICAgIGNhc2UgJ2F1dG9DbG9zaW5nQnJhY2tldHMnOlxuICAgICAgICBlZGl0b3Iuc2V0T3B0aW9uKFxuICAgICAgICAgICdhdXRvQ2xvc2luZ0JyYWNrZXRzJyxcbiAgICAgICAgICBjb25maWdbJ2F1dG9DbG9zaW5nQnJhY2tldHMnXSBhcyBib29sZWFuXG4gICAgICAgICk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnY3Vyc29yQmxpbmtSYXRlJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbihcbiAgICAgICAgICAnY3Vyc29yQmxpbmtSYXRlJyxcbiAgICAgICAgICBjb25maWdbJ2N1cnNvckJsaW5rUmF0ZSddIGFzIG51bWJlclxuICAgICAgICApO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2ZvbnRGYW1pbHknOlxuICAgICAgICBlZGl0b3Iuc2V0T3B0aW9uKCdmb250RmFtaWx5JywgY29uZmlnWydmb250RmFtaWx5J10gYXMgc3RyaW5nIHwgbnVsbCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnZm9udFNpemUnOlxuICAgICAgICBlZGl0b3Iuc2V0T3B0aW9uKCdmb250U2l6ZScsIGNvbmZpZ1snZm9udFNpemUnXSBhcyBudW1iZXIgfCBudWxsKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdsaW5lSGVpZ2h0JzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbignbGluZUhlaWdodCcsIGNvbmZpZ1snbGluZUhlaWdodCddIGFzIG51bWJlciB8IG51bGwpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2xpbmVOdW1iZXJzJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbignbGluZU51bWJlcnMnLCBjb25maWdbJ2xpbmVOdW1iZXJzJ10gYXMgYm9vbGVhbik7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbGluZVdyYXAnOlxuICAgICAgICBlZGl0b3Iuc2V0T3B0aW9uKCdsaW5lV3JhcCcsIGNvbmZpZ1snbGluZVdyYXAnXSBhcyBsaW5lV3JhcF90eXBlKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdtYXRjaEJyYWNrZXRzJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbignbWF0Y2hCcmFja2V0cycsIGNvbmZpZ1snbWF0Y2hCcmFja2V0cyddIGFzIGJvb2xlYW4pO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ3JlYWRPbmx5JzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbigncmVhZE9ubHknLCBjb25maWdbJ3JlYWRPbmx5J10gYXMgYm9vbGVhbik7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnaW5zZXJ0U3BhY2VzJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbignaW5zZXJ0U3BhY2VzJywgY29uZmlnWydpbnNlcnRTcGFjZXMnXSBhcyBib29sZWFuKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICd0YWJTaXplJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbigndGFiU2l6ZScsIGNvbmZpZ1sndGFiU2l6ZSddIGFzIG51bWJlcik7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnd29yZFdyYXBDb2x1bW4nOlxuICAgICAgICBlZGl0b3Iuc2V0T3B0aW9uKCd3b3JkV3JhcENvbHVtbicsIGNvbmZpZ1snd29yZFdyYXBDb2x1bW4nXSBhcyBudW1iZXIpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ3J1bGVycyc6XG4gICAgICAgIGVkaXRvci5zZXRPcHRpb24oJ3J1bGVycycsIGNvbmZpZ1sncnVsZXJzJ10gYXMgbnVtYmVyW10pO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2NvZGVGb2xkaW5nJzpcbiAgICAgICAgZWRpdG9yLnNldE9wdGlvbignY29kZUZvbGRpbmcnLCBjb25maWdbJ2NvZGVGb2xkaW5nJ10gYXMgYm9vbGVhbik7XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfTtcblxuICBjb25zdCBzZXRPcHRpb24gPSAoXG4gICAgZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3IgfCB1bmRlZmluZWQsXG4gICAgY29uZmlnOiBKU09OT2JqZWN0XG4gICkgPT4ge1xuICAgIGlmIChlZGl0b3IgPT09IHVuZGVmaW5lZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICdhdXRvQ2xvc2luZ0JyYWNrZXRzJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAnY3Vyc29yQmxpbmtSYXRlJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAnZm9udEZhbWlseScpO1xuICAgIG1hcE9wdGlvbihlZGl0b3IsIGNvbmZpZywgJ2ZvbnRTaXplJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAnbGluZUhlaWdodCcpO1xuICAgIG1hcE9wdGlvbihlZGl0b3IsIGNvbmZpZywgJ2xpbmVOdW1iZXJzJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAnbGluZVdyYXAnKTtcbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICdtYXRjaEJyYWNrZXRzJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAncmVhZE9ubHknKTtcbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICdpbnNlcnRTcGFjZXMnKTtcbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICd0YWJTaXplJyk7XG4gICAgbWFwT3B0aW9uKGVkaXRvciwgY29uZmlnLCAnd29yZFdyYXBDb2x1bW4nKTtcbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICdydWxlcnMnKTtcbiAgICBtYXBPcHRpb24oZWRpdG9yLCBjb25maWcsICdjb2RlRm9sZGluZycpO1xuICB9O1xuXG4gIGNvbnN0IHBsdWdpbklkID0gJ0BqdXB5dGVybGFiL2NvbnNvbGUtZXh0ZW5zaW9uOnRyYWNrZXInO1xuICBsZXQgaW50ZXJhY3Rpb25Nb2RlOiBzdHJpbmc7XG4gIGxldCBwcm9tcHRDZWxsQ29uZmlnOiBKU09OT2JqZWN0O1xuXG4gIC8qKlxuICAgKiBVcGRhdGUgc2V0dGluZ3MgZm9yIG9uZSBjb25zb2xlIG9yIGFsbCBjb25zb2xlcy5cbiAgICpcbiAgICogQHBhcmFtIHBhbmVsIE9wdGlvbmFsIC0gc2luZ2xlIGNvbnNvbGUgdG8gdXBkYXRlLlxuICAgKi9cbiAgYXN5bmMgZnVuY3Rpb24gdXBkYXRlU2V0dGluZ3MocGFuZWw/OiBDb25zb2xlUGFuZWwpIHtcbiAgICBpbnRlcmFjdGlvbk1vZGUgPSAoYXdhaXQgc2V0dGluZ1JlZ2lzdHJ5LmdldChwbHVnaW5JZCwgJ2ludGVyYWN0aW9uTW9kZScpKVxuICAgICAgLmNvbXBvc2l0ZSBhcyBzdHJpbmc7XG4gICAgcHJvbXB0Q2VsbENvbmZpZyA9IChhd2FpdCBzZXR0aW5nUmVnaXN0cnkuZ2V0KHBsdWdpbklkLCAncHJvbXB0Q2VsbENvbmZpZycpKVxuICAgICAgLmNvbXBvc2l0ZSBhcyBKU09OT2JqZWN0O1xuXG4gICAgY29uc3Qgc2V0V2lkZ2V0T3B0aW9ucyA9ICh3aWRnZXQ6IENvbnNvbGVQYW5lbCkgPT4ge1xuICAgICAgd2lkZ2V0LmNvbnNvbGUubm9kZS5kYXRhc2V0LmpwSW50ZXJhY3Rpb25Nb2RlID0gaW50ZXJhY3Rpb25Nb2RlO1xuICAgICAgLy8gVXBkYXRlIGZ1dHVyZSBwcm9tcHRDZWxsc1xuICAgICAgd2lkZ2V0LmNvbnNvbGUuZWRpdG9yQ29uZmlnID0gcHJvbXB0Q2VsbENvbmZpZztcbiAgICAgIC8vIFVwZGF0ZSBwcm9tcHRDZWxsIGFscmVhZHkgb24gc2NyZWVuXG4gICAgICBzZXRPcHRpb24od2lkZ2V0LmNvbnNvbGUucHJvbXB0Q2VsbD8uZWRpdG9yLCBwcm9tcHRDZWxsQ29uZmlnKTtcbiAgICB9O1xuXG4gICAgaWYgKHBhbmVsKSB7XG4gICAgICBzZXRXaWRnZXRPcHRpb25zKHBhbmVsKTtcbiAgICB9IGVsc2Uge1xuICAgICAgdHJhY2tlci5mb3JFYWNoKHNldFdpZGdldE9wdGlvbnMpO1xuICAgIH1cbiAgfVxuXG4gIHNldHRpbmdSZWdpc3RyeS5wbHVnaW5DaGFuZ2VkLmNvbm5lY3QoKHNlbmRlciwgcGx1Z2luKSA9PiB7XG4gICAgaWYgKHBsdWdpbiA9PT0gcGx1Z2luSWQpIHtcbiAgICAgIHZvaWQgdXBkYXRlU2V0dGluZ3MoKTtcbiAgICB9XG4gIH0pO1xuICBhd2FpdCB1cGRhdGVTZXR0aW5ncygpO1xuXG4gIC8vIEFwcGx5IHNldHRpbmdzIHdoZW4gYSBjb25zb2xlIGlzIGNyZWF0ZWQuXG4gIHRyYWNrZXIud2lkZ2V0QWRkZWQuY29ubmVjdCgoc2VuZGVyLCBwYW5lbCkgPT4ge1xuICAgIHZvaWQgdXBkYXRlU2V0dGluZ3MocGFuZWwpO1xuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYXV0b0Nsb3NpbmdCcmFja2V0cywge1xuICAgIGV4ZWN1dGU6IGFzeW5jIGFyZ3MgPT4ge1xuICAgICAgcHJvbXB0Q2VsbENvbmZpZy5hdXRvQ2xvc2luZ0JyYWNrZXRzID0gISEoXG4gICAgICAgIGFyZ3NbJ2ZvcmNlJ10gPz8gIXByb21wdENlbGxDb25maWcuYXV0b0Nsb3NpbmdCcmFja2V0c1xuICAgICAgKTtcbiAgICAgIGF3YWl0IHNldHRpbmdSZWdpc3RyeS5zZXQocGx1Z2luSWQsICdwcm9tcHRDZWxsQ29uZmlnJywgcHJvbXB0Q2VsbENvbmZpZyk7XG4gICAgfSxcbiAgICBsYWJlbDogdHJhbnMuX18oJ0F1dG8gQ2xvc2UgQnJhY2tldHMgZm9yIENvZGUgQ29uc29sZSBQcm9tcHQnKSxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IHByb21wdENlbGxDb25maWcuYXV0b0Nsb3NpbmdCcmFja2V0cyBhcyBib29sZWFuXG4gIH0pO1xuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZXJlIGlzIGFuIGFjdGl2ZSBjb25zb2xlLlxuICAgKi9cbiAgZnVuY3Rpb24gaXNFbmFibGVkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiAoXG4gICAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQgIT09IG51bGwgJiZcbiAgICAgIHRyYWNrZXIuY3VycmVudFdpZGdldCA9PT0gc2hlbGwuY3VycmVudFdpZGdldFxuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdXNlZCB0byBvcGVuIGEgY29uc29sZS5cbiAgICovXG4gIGludGVyZmFjZSBJT3Blbk9wdGlvbnMgZXh0ZW5kcyBQYXJ0aWFsPENvbnNvbGVQYW5lbC5JT3B0aW9ucz4ge1xuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gYWN0aXZhdGUgdGhlIGNvbnNvbGUuICBEZWZhdWx0cyB0byBgdHJ1ZWAuXG4gICAgICovXG4gICAgYWN0aXZhdGU/OiBib29sZWFuO1xuICB9XG5cbiAgbGV0IGNvbW1hbmQgPSBDb21tYW5kSURzLm9wZW47XG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoY29tbWFuZCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnT3BlbiBhIGNvbnNvbGUgZm9yIHRoZSBwcm92aWRlZCBgcGF0aGAuJyksXG4gICAgZXhlY3V0ZTogKGFyZ3M6IElPcGVuT3B0aW9ucykgPT4ge1xuICAgICAgY29uc3QgcGF0aCA9IGFyZ3NbJ3BhdGgnXTtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuZmluZCh2YWx1ZSA9PiB7XG4gICAgICAgIHJldHVybiB2YWx1ZS5jb25zb2xlLnNlc3Npb25Db250ZXh0LnNlc3Npb24/LnBhdGggPT09IHBhdGg7XG4gICAgICB9KTtcbiAgICAgIGlmICh3aWRnZXQpIHtcbiAgICAgICAgaWYgKGFyZ3MuYWN0aXZhdGUgIT09IGZhbHNlKSB7XG4gICAgICAgICAgc2hlbGwuYWN0aXZhdGVCeUlkKHdpZGdldC5pZCk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHdpZGdldDtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHJldHVybiBtYW5hZ2VyLnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgICAgIGNvbnN0IG1vZGVsID0gZmluZChtYW5hZ2VyLnNlc3Npb25zLnJ1bm5pbmcoKSwgaXRlbSA9PiB7XG4gICAgICAgICAgICByZXR1cm4gaXRlbS5wYXRoID09PSBwYXRoO1xuICAgICAgICAgIH0pO1xuICAgICAgICAgIGlmIChtb2RlbCkge1xuICAgICAgICAgICAgcmV0dXJuIGNyZWF0ZUNvbnNvbGUoYXJncyk7XG4gICAgICAgICAgfVxuICAgICAgICAgIHJldHVybiBQcm9taXNlLnJlamVjdChgTm8gcnVubmluZyBrZXJuZWwgc2Vzc2lvbiBmb3IgcGF0aDogJHtwYXRofWApO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xuXG4gIGNvbW1hbmQgPSBDb21tYW5kSURzLmNyZWF0ZTtcbiAgY29tbWFuZHMuYWRkQ29tbWFuZChjb21tYW5kLCB7XG4gICAgbGFiZWw6IGFyZ3MgPT4ge1xuICAgICAgaWYgKGFyZ3NbJ2lzUGFsZXR0ZSddKSB7XG4gICAgICAgIHJldHVybiB0cmFucy5fXygnTmV3IENvbnNvbGUnKTtcbiAgICAgIH0gZWxzZSBpZiAoYXJnc1snaXNMYXVuY2hlciddICYmIGFyZ3NbJ2tlcm5lbFByZWZlcmVuY2UnXSkge1xuICAgICAgICBjb25zdCBrZXJuZWxQcmVmZXJlbmNlID0gYXJnc1tcbiAgICAgICAgICAna2VybmVsUHJlZmVyZW5jZSdcbiAgICAgICAgXSBhcyBJU2Vzc2lvbkNvbnRleHQuSUtlcm5lbFByZWZlcmVuY2U7XG4gICAgICAgIC8vIFRPRE86IEx1bWlubyBjb21tYW5kIGZ1bmN0aW9ucyBzaG91bGQgcHJvYmFibHkgYmUgYWxsb3dlZCB0byByZXR1cm4gdW5kZWZpbmVkP1xuICAgICAgICByZXR1cm4gKFxuICAgICAgICAgIG1hbmFnZXIua2VybmVsc3BlY3M/LnNwZWNzPy5rZXJuZWxzcGVjc1trZXJuZWxQcmVmZXJlbmNlLm5hbWUgfHwgJyddXG4gICAgICAgICAgICA/LmRpc3BsYXlfbmFtZSA/PyAnJ1xuICAgICAgICApO1xuICAgICAgfVxuICAgICAgcmV0dXJuIHRyYW5zLl9fKCdDb25zb2xlJyk7XG4gICAgfSxcbiAgICBpY29uOiBhcmdzID0+IChhcmdzWydpc1BhbGV0dGUnXSA/IHVuZGVmaW5lZCA6IGNvbnNvbGVJY29uKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGJhc2VQYXRoID1cbiAgICAgICAgKChhcmdzWydiYXNlUGF0aCddIGFzIHN0cmluZykgfHxcbiAgICAgICAgICAoYXJnc1snY3dkJ10gYXMgc3RyaW5nKSB8fFxuICAgICAgICAgIGJyb3dzZXJGYWN0b3J5Py5kZWZhdWx0QnJvd3Nlci5tb2RlbC5wYXRoKSA/P1xuICAgICAgICAnJztcbiAgICAgIHJldHVybiBjcmVhdGVDb25zb2xlKHsgYmFzZVBhdGgsIC4uLmFyZ3MgfSk7XG4gICAgfVxuICB9KTtcblxuICAvLyBHZXQgdGhlIGN1cnJlbnQgd2lkZ2V0IGFuZCBhY3RpdmF0ZSB1bmxlc3MgdGhlIGFyZ3Mgc3BlY2lmeSBvdGhlcndpc2UuXG4gIGZ1bmN0aW9uIGdldEN1cnJlbnQoYXJnczogUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdCk6IENvbnNvbGVQYW5lbCB8IG51bGwge1xuICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICBjb25zdCBhY3RpdmF0ZSA9IGFyZ3NbJ2FjdGl2YXRlJ10gIT09IGZhbHNlO1xuICAgIGlmIChhY3RpdmF0ZSAmJiB3aWRnZXQpIHtcbiAgICAgIHNoZWxsLmFjdGl2YXRlQnlJZCh3aWRnZXQuaWQpO1xuICAgIH1cbiAgICByZXR1cm4gd2lkZ2V0ID8/IG51bGw7XG4gIH1cblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2xlYXIsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0NsZWFyIENvbnNvbGUgQ2VsbHMnKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KGFyZ3MpO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGN1cnJlbnQuY29uc29sZS5jbGVhcigpO1xuICAgIH0sXG4gICAgaXNFbmFibGVkXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5ydW5VbmZvcmNlZCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnUnVuIENlbGwgKHVuZm9yY2VkKScpLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgY3VycmVudCA9IGdldEN1cnJlbnQoYXJncyk7XG4gICAgICBpZiAoIWN1cnJlbnQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgcmV0dXJuIGN1cnJlbnQuY29uc29sZS5leGVjdXRlKCk7XG4gICAgfSxcbiAgICBpc0VuYWJsZWRcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnJ1bkZvcmNlZCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnUnVuIENlbGwgKGZvcmNlZCknKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KGFyZ3MpO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIHJldHVybiBjdXJyZW50LmNvbnNvbGUuZXhlY3V0ZSh0cnVlKTtcbiAgICB9LFxuICAgIGlzRW5hYmxlZFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubGluZWJyZWFrLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdJbnNlcnQgTGluZSBCcmVhaycpLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgY3VycmVudCA9IGdldEN1cnJlbnQoYXJncyk7XG4gICAgICBpZiAoIWN1cnJlbnQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY3VycmVudC5jb25zb2xlLmluc2VydExpbmVicmVhaygpO1xuICAgIH0sXG4gICAgaXNFbmFibGVkXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXBsYWNlU2VsZWN0aW9uLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdSZXBsYWNlIFNlbGVjdGlvbiBpbiBDb25zb2xlJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50ID0gZ2V0Q3VycmVudChhcmdzKTtcbiAgICAgIGlmICghY3VycmVudCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCB0ZXh0OiBzdHJpbmcgPSAoYXJnc1sndGV4dCddIGFzIHN0cmluZykgfHwgJyc7XG4gICAgICBjdXJyZW50LmNvbnNvbGUucmVwbGFjZVNlbGVjdGlvbih0ZXh0KTtcbiAgICB9LFxuICAgIGlzRW5hYmxlZFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuaW50ZXJydXB0LCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdJbnRlcnJ1cHQgS2VybmVsJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50ID0gZ2V0Q3VycmVudChhcmdzKTtcbiAgICAgIGlmICghY3VycmVudCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCBrZXJuZWwgPSBjdXJyZW50LmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQuc2Vzc2lvbj8ua2VybmVsO1xuICAgICAgaWYgKGtlcm5lbCkge1xuICAgICAgICByZXR1cm4ga2VybmVsLmludGVycnVwdCgpO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5yZXN0YXJ0LCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdSZXN0YXJ0IEtlcm5lbOKApicpLFxuICAgIGV4ZWN1dGU6IGFyZ3MgPT4ge1xuICAgICAgY29uc3QgY3VycmVudCA9IGdldEN1cnJlbnQoYXJncyk7XG4gICAgICBpZiAoIWN1cnJlbnQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgcmV0dXJuIHNlc3Npb25EaWFsb2dzIS5yZXN0YXJ0KFxuICAgICAgICBjdXJyZW50LmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQsXG4gICAgICAgIHRyYW5zbGF0b3JcbiAgICAgICk7XG4gICAgfSxcbiAgICBpc0VuYWJsZWRcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNodXRkb3duLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24nKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KGFyZ3MpO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cblxuICAgICAgcmV0dXJuIGN1cnJlbnQuY29uc29sZS5zZXNzaW9uQ29udGV4dC5zaHV0ZG93bigpO1xuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmNsb3NlQW5kU2h1dGRvd24sIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0Nsb3NlIGFuZCBTaHV0IERvd27igKYnKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KGFyZ3MpO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIHJldHVybiBzaG93RGlhbG9nKHtcbiAgICAgICAgdGl0bGU6IHRyYW5zLl9fKCdTaHV0IGRvd24gdGhlIGNvbnNvbGU/JyksXG4gICAgICAgIGJvZHk6IHRyYW5zLl9fKFxuICAgICAgICAgICdBcmUgeW91IHN1cmUgeW91IHdhbnQgdG8gY2xvc2UgXCIlMVwiPycsXG4gICAgICAgICAgY3VycmVudC50aXRsZS5sYWJlbFxuICAgICAgICApLFxuICAgICAgICBidXR0b25zOiBbRGlhbG9nLmNhbmNlbEJ1dHRvbigpLCBEaWFsb2cud2FybkJ1dHRvbigpXVxuICAgICAgfSkudGhlbihyZXN1bHQgPT4ge1xuICAgICAgICBpZiAocmVzdWx0LmJ1dHRvbi5hY2NlcHQpIHtcbiAgICAgICAgICByZXR1cm4gY29tbWFuZHNcbiAgICAgICAgICAgIC5leGVjdXRlKENvbW1hbmRJRHMuc2h1dGRvd24sIHsgYWN0aXZhdGU6IGZhbHNlIH0pXG4gICAgICAgICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgICAgICAgIGN1cnJlbnQuZGlzcG9zZSgpO1xuICAgICAgICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfSxcbiAgICBpc0VuYWJsZWRcbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmluamVjdCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnSW5qZWN0IHNvbWUgY29kZSBpbiBhIGNvbnNvbGUuJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBwYXRoID0gYXJnc1sncGF0aCddO1xuICAgICAgdHJhY2tlci5maW5kKHdpZGdldCA9PiB7XG4gICAgICAgIGlmICh3aWRnZXQuY29uc29sZS5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5wYXRoID09PSBwYXRoKSB7XG4gICAgICAgICAgaWYgKGFyZ3NbJ2FjdGl2YXRlJ10gIT09IGZhbHNlKSB7XG4gICAgICAgICAgICBzaGVsbC5hY3RpdmF0ZUJ5SWQod2lkZ2V0LmlkKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgdm9pZCB3aWRnZXQuY29uc29sZS5pbmplY3QoXG4gICAgICAgICAgICBhcmdzWydjb2RlJ10gYXMgc3RyaW5nLFxuICAgICAgICAgICAgYXJnc1snbWV0YWRhdGEnXSBhcyBKU09OT2JqZWN0XG4gICAgICAgICAgKTtcbiAgICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9KTtcbiAgICB9LFxuICAgIGlzRW5hYmxlZFxuICB9KTtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuY2hhbmdlS2VybmVsLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdDaGFuZ2UgS2VybmVs4oCmJyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBjdXJyZW50ID0gZ2V0Q3VycmVudChhcmdzKTtcbiAgICAgIGlmICghY3VycmVudCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICByZXR1cm4gc2Vzc2lvbkRpYWxvZ3MhLnNlbGVjdEtlcm5lbChcbiAgICAgICAgY3VycmVudC5jb25zb2xlLnNlc3Npb25Db250ZXh0LFxuICAgICAgICB0cmFuc2xhdG9yXG4gICAgICApO1xuICAgIH0sXG4gICAgaXNFbmFibGVkXG4gIH0pO1xuXG4gIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5nZXRLZXJuZWwsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0dldCBLZXJuZWwnKSxcbiAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSBnZXRDdXJyZW50KHsgYWN0aXZhdGU6IGZhbHNlLCAuLi5hcmdzIH0pO1xuICAgICAgaWYgKCFjdXJyZW50KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIHJldHVybiBjdXJyZW50LnNlc3Npb25Db250ZXh0LnNlc3Npb24/Lmtlcm5lbDtcbiAgICB9LFxuICAgIGlzRW5hYmxlZFxuICB9KTtcblxuICBpZiAocGFsZXR0ZSkge1xuICAgIC8vIEFkZCBjb21tYW5kIHBhbGV0dGUgaXRlbXNcbiAgICBbXG4gICAgICBDb21tYW5kSURzLmNyZWF0ZSxcbiAgICAgIENvbW1hbmRJRHMubGluZWJyZWFrLFxuICAgICAgQ29tbWFuZElEcy5jbGVhcixcbiAgICAgIENvbW1hbmRJRHMucnVuVW5mb3JjZWQsXG4gICAgICBDb21tYW5kSURzLnJ1bkZvcmNlZCxcbiAgICAgIENvbW1hbmRJRHMucmVzdGFydCxcbiAgICAgIENvbW1hbmRJRHMuaW50ZXJydXB0LFxuICAgICAgQ29tbWFuZElEcy5jaGFuZ2VLZXJuZWwsXG4gICAgICBDb21tYW5kSURzLmNsb3NlQW5kU2h1dGRvd25cbiAgICBdLmZvckVhY2goY29tbWFuZCA9PiB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oeyBjb21tYW5kLCBjYXRlZ29yeSwgYXJnczogeyBpc1BhbGV0dGU6IHRydWUgfSB9KTtcbiAgICB9KTtcbiAgfVxuXG4gIGlmIChtYWluTWVudSkge1xuICAgIC8vIEFkZCBhIGNsb3NlIGFuZCBzaHV0ZG93biBjb21tYW5kIHRvIHRoZSBmaWxlIG1lbnUuXG4gICAgbWFpbk1lbnUuZmlsZU1lbnUuY2xvc2VBbmRDbGVhbmVycy5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMuY2xvc2VBbmRTaHV0ZG93bixcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuXG4gICAgLy8gQWRkIGEga2VybmVsIHVzZXIgdG8gdGhlIEtlcm5lbCBtZW51XG4gICAgbWFpbk1lbnUua2VybmVsTWVudS5rZXJuZWxVc2Vycy5jaGFuZ2VLZXJuZWwuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLmNoYW5nZUtlcm5lbCxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1haW5NZW51Lmtlcm5lbE1lbnUua2VybmVsVXNlcnMuY2xlYXJXaWRnZXQuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLmNsZWFyLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG4gICAgbWFpbk1lbnUua2VybmVsTWVudS5rZXJuZWxVc2Vycy5pbnRlcnJ1cHRLZXJuZWwuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLmludGVycnVwdCxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1haW5NZW51Lmtlcm5lbE1lbnUua2VybmVsVXNlcnMucmVzdGFydEtlcm5lbC5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMucmVzdGFydCxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICAgIG1haW5NZW51Lmtlcm5lbE1lbnUua2VybmVsVXNlcnMuc2h1dGRvd25LZXJuZWwuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLnNodXRkb3duLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG5cbiAgICAvLyBBZGQgYSBjb2RlIHJ1bm5lciB0byB0aGUgUnVuIG1lbnUuXG4gICAgbWFpbk1lbnUucnVuTWVudS5jb2RlUnVubmVycy5ydW4uYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLnJ1bkZvcmNlZCxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuXG4gICAgLy8gQWRkIGEgY2xlYXJlciB0byB0aGUgZWRpdCBtZW51XG4gICAgbWFpbk1lbnUuZWRpdE1lbnUuY2xlYXJlcnMuY2xlYXJDdXJyZW50LmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy5jbGVhcixcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuXG4gICAgLy8gQWRkIGtlcm5lbCBpbmZvcm1hdGlvbiB0byB0aGUgYXBwbGljYXRpb24gaGVscCBtZW51LlxuICAgIG1haW5NZW51LmhlbHBNZW51LmdldEtlcm5lbC5hZGQoe1xuICAgICAgaWQ6IENvbW1hbmRJRHMuZ2V0S2VybmVsLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG4gIH1cblxuICAvLyBGb3IgYmFja3dhcmRzIGNvbXBhdGliaWxpdHkgYW5kIGNsYXJpdHksIHdlIGV4cGxpY2l0bHkgbGFiZWwgdGhlIHJ1blxuICAvLyBrZXlzdHJva2Ugd2l0aCB0aGUgYWN0dWFsIGVmZmVjdGVkIGNoYW5nZSwgcmF0aGVyIHRoYW4gdGhlIGdlbmVyaWNcbiAgLy8gXCJub3RlYm9va1wiIG9yIFwidGVybWluYWxcIiBpbnRlcmFjdGlvbiBtb2RlLiBXaGVuIHRoaXMgaW50ZXJhY3Rpb24gbW9kZVxuICAvLyBhZmZlY3RzIG1vcmUgdGhhbiBqdXN0IHRoZSBydW4ga2V5c3Ryb2tlLCB3ZSBjYW4gbWFrZSB0aGlzIG1lbnUgdGl0bGUgbW9yZVxuICAvLyBnZW5lcmljLlxuICBjb25zdCBydW5TaG9ydGN1dFRpdGxlczogeyBbaW5kZXg6IHN0cmluZ106IHN0cmluZyB9ID0ge1xuICAgIG5vdGVib29rOiB0cmFucy5fXygnRXhlY3V0ZSB3aXRoIFNoaWZ0K0VudGVyJyksXG4gICAgdGVybWluYWw6IHRyYW5zLl9fKCdFeGVjdXRlIHdpdGggRW50ZXInKVxuICB9O1xuXG4gIC8vIEFkZCB0aGUgZXhlY3V0ZSBrZXlzdHJva2Ugc2V0dGluZyBzdWJtZW51LlxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuaW50ZXJhY3Rpb25Nb2RlLCB7XG4gICAgbGFiZWw6IGFyZ3MgPT5cbiAgICAgIHJ1blNob3J0Y3V0VGl0bGVzW2FyZ3NbJ2ludGVyYWN0aW9uTW9kZSddIGFzIHN0cmluZ10gPz9cbiAgICAgICdTZXQgdGhlIGNvbnNvbGUgaW50ZXJhY3Rpb24gbW9kZS4nLFxuICAgIGV4ZWN1dGU6IGFzeW5jIGFyZ3MgPT4ge1xuICAgICAgY29uc3Qga2V5ID0gJ2tleU1hcCc7XG4gICAgICB0cnkge1xuICAgICAgICBhd2FpdCBzZXR0aW5nUmVnaXN0cnkuc2V0KFxuICAgICAgICAgIHBsdWdpbklkLFxuICAgICAgICAgICdpbnRlcmFjdGlvbk1vZGUnLFxuICAgICAgICAgIGFyZ3NbJ2ludGVyYWN0aW9uTW9kZSddIGFzIHN0cmluZ1xuICAgICAgICApO1xuICAgICAgfSBjYXRjaCAocmVhc29uKSB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBzZXQgJHtwbHVnaW5JZH06JHtrZXl9IC0gJHtyZWFzb24ubWVzc2FnZX1gKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIGlzVG9nZ2xlZDogYXJncyA9PiBhcmdzWydpbnRlcmFjdGlvbk1vZGUnXSA9PT0gaW50ZXJhY3Rpb25Nb2RlXG4gIH0pO1xuXG4gIHJldHVybiB0cmFja2VyO1xufVxuXG4vKipcbiAqIEFjdGl2YXRlIHRoZSBjb21wbGV0ZXIgc2VydmljZSBmb3IgY29uc29sZS5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGVDb25zb2xlQ29tcGxldGVyU2VydmljZShcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIGNvbnNvbGVzOiBJQ29uc29sZVRyYWNrZXIsXG4gIG1hbmFnZXI6IElDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyIHwgbnVsbCxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IgfCBudWxsXG4pOiB2b2lkIHtcbiAgaWYgKCFtYW5hZ2VyKSB7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgY29uc3QgdHJhbnMgPSAodHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvcikubG9hZCgnanVweXRlcmxhYicpO1xuXG4gIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuaW52b2tlQ29tcGxldGVyLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdEaXNwbGF5IHRoZSBjb21wbGV0aW9uIGhlbHBlci4nKSxcbiAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICBjb25zdCBpZCA9IGNvbnNvbGVzLmN1cnJlbnRXaWRnZXQgJiYgY29uc29sZXMuY3VycmVudFdpZGdldC5pZDtcblxuICAgICAgaWYgKGlkKSB7XG4gICAgICAgIHJldHVybiBtYW5hZ2VyLmludm9rZShpZCk7XG4gICAgICB9XG4gICAgfVxuICB9KTtcblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNlbGVjdENvbXBsZXRlciwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnU2VsZWN0IHRoZSBjb21wbGV0aW9uIHN1Z2dlc3Rpb24uJyksXG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3QgaWQgPSBjb25zb2xlcy5jdXJyZW50V2lkZ2V0ICYmIGNvbnNvbGVzLmN1cnJlbnRXaWRnZXQuaWQ7XG5cbiAgICAgIGlmIChpZCkge1xuICAgICAgICByZXR1cm4gbWFuYWdlci5zZWxlY3QoaWQpO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG5cbiAgYXBwLmNvbW1hbmRzLmFkZEtleUJpbmRpbmcoe1xuICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMuc2VsZWN0Q29tcGxldGVyLFxuICAgIGtleXM6IFsnRW50ZXInXSxcbiAgICBzZWxlY3RvcjogJy5qcC1Db25zb2xlUGFuZWwgLmpwLW1vZC1jb21wbGV0ZXItYWN0aXZlJ1xuICB9KTtcbiAgY29uc3QgdXBkYXRlQ29tcGxldGVyID0gYXN5bmMgKF86IGFueSwgY29uc29sZVBhbmVsOiBDb25zb2xlUGFuZWwpID0+IHtcbiAgICBjb25zdCBjb21wbGV0ZXJDb250ZXh0ID0ge1xuICAgICAgZWRpdG9yOiBjb25zb2xlUGFuZWwuY29uc29sZS5wcm9tcHRDZWxsPy5lZGl0b3IgPz8gbnVsbCxcbiAgICAgIHNlc3Npb246IGNvbnNvbGVQYW5lbC5jb25zb2xlLnNlc3Npb25Db250ZXh0LnNlc3Npb24sXG4gICAgICB3aWRnZXQ6IGNvbnNvbGVQYW5lbFxuICAgIH07XG4gICAgYXdhaXQgbWFuYWdlci51cGRhdGVDb21wbGV0ZXIoY29tcGxldGVyQ29udGV4dCk7XG4gICAgY29uc29sZVBhbmVsLmNvbnNvbGUucHJvbXB0Q2VsbENyZWF0ZWQuY29ubmVjdCgoY29kZUNvbnNvbGUsIGNlbGwpID0+IHtcbiAgICAgIGNvbnN0IG5ld0NvbnRleHQgPSB7XG4gICAgICAgIGVkaXRvcjogY2VsbC5lZGl0b3IsXG4gICAgICAgIHNlc3Npb246IGNvZGVDb25zb2xlLnNlc3Npb25Db250ZXh0LnNlc3Npb24sXG4gICAgICAgIHdpZGdldDogY29uc29sZVBhbmVsXG4gICAgICB9O1xuICAgICAgbWFuYWdlci51cGRhdGVDb21wbGV0ZXIobmV3Q29udGV4dCkuY2F0Y2goY29uc29sZS5lcnJvcik7XG4gICAgfSk7XG4gICAgY29uc29sZVBhbmVsLmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQuc2Vzc2lvbkNoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICBjb25zdCBuZXdDb250ZXh0ID0ge1xuICAgICAgICBlZGl0b3I6IGNvbnNvbGVQYW5lbC5jb25zb2xlLnByb21wdENlbGw/LmVkaXRvciA/PyBudWxsLFxuICAgICAgICBzZXNzaW9uOiBjb25zb2xlUGFuZWwuY29uc29sZS5zZXNzaW9uQ29udGV4dC5zZXNzaW9uLFxuICAgICAgICB3aWRnZXQ6IGNvbnNvbGVQYW5lbFxuICAgICAgfTtcbiAgICAgIG1hbmFnZXIudXBkYXRlQ29tcGxldGVyKG5ld0NvbnRleHQpLmNhdGNoKGNvbnNvbGUuZXJyb3IpO1xuICAgIH0pO1xuICB9O1xuICBjb25zb2xlcy53aWRnZXRBZGRlZC5jb25uZWN0KHVwZGF0ZUNvbXBsZXRlcik7XG4gIG1hbmFnZXIuYWN0aXZlUHJvdmlkZXJzQ2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICBjb25zb2xlcy5mb3JFYWNoKGNvbnNvbGVXaWRnZXQgPT4ge1xuICAgICAgdXBkYXRlQ29tcGxldGVyKHVuZGVmaW5lZCwgY29uc29sZVdpZGdldCkuY2F0Y2goZSA9PiBjb25zb2xlLmVycm9yKGUpKTtcbiAgICB9KTtcbiAgfSk7XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=