"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_debugger-extension_lib_index_js"],{

/***/ "../../packages/debugger-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/debugger-extension/lib/index.js ***!
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
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/console */ "webpack/sharing/consume/default/@jupyterlab/console/@jupyterlab/console");
/* harmony import */ var _jupyterlab_console__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_console__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/debugger */ "webpack/sharing/consume/default/@jupyterlab/debugger/@jupyterlab/debugger");
/* harmony import */ var _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/fileeditor */ "webpack/sharing/consume/default/@jupyterlab/fileeditor/@jupyterlab/fileeditor");
/* harmony import */ var _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/logconsole */ "webpack/sharing/consume/default/@jupyterlab/logconsole/@jupyterlab/logconsole");
/* harmony import */ var _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module debugger-extension
 */













/**
 * A plugin that provides visual debugging support for consoles.
 */
const consoles = {
    id: '@jupyterlab/debugger-extension:consoles',
    autoStart: false,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_console__WEBPACK_IMPORTED_MODULE_3__.IConsoleTracker],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, debug, consoleTracker, labShell) => {
        const handler = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Handler({
            type: 'console',
            shell: app.shell,
            service: debug
        });
        const updateHandlerAndCommands = async (widget) => {
            const { sessionContext } = widget;
            await sessionContext.ready;
            await handler.updateContext(widget, sessionContext);
            app.commands.notifyCommandChanged();
        };
        if (labShell) {
            labShell.currentChanged.connect((_, update) => {
                const widget = update.newValue;
                if (widget instanceof _jupyterlab_console__WEBPACK_IMPORTED_MODULE_3__.ConsolePanel) {
                    void updateHandlerAndCommands(widget);
                }
            });
        }
        else {
            consoleTracker.currentChanged.connect((_, consolePanel) => {
                if (consolePanel) {
                    void updateHandlerAndCommands(consolePanel);
                }
            });
        }
    }
};
/**
 * A plugin that provides visual debugging support for file editors.
 */
const files = {
    id: '@jupyterlab/debugger-extension:files',
    autoStart: false,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, debug, editorTracker, labShell) => {
        const handler = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Handler({
            type: 'file',
            shell: app.shell,
            service: debug
        });
        const activeSessions = {};
        const updateHandlerAndCommands = async (widget) => {
            const sessions = app.serviceManager.sessions;
            try {
                const model = await sessions.findByPath(widget.context.path);
                if (!model) {
                    return;
                }
                let session = activeSessions[model.id];
                if (!session) {
                    // Use `connectTo` only if the session does not exist.
                    // `connectTo` sends a kernel_info_request on the shell
                    // channel, which blocks the debug session restore when waiting
                    // for the kernel to be ready
                    session = sessions.connectTo({ model });
                    activeSessions[model.id] = session;
                }
                await handler.update(widget, session);
                app.commands.notifyCommandChanged();
            }
            catch (_a) {
                return;
            }
        };
        if (labShell) {
            labShell.currentChanged.connect((_, update) => {
                const widget = update.newValue;
                if (widget instanceof _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_6__.DocumentWidget) {
                    const { content } = widget;
                    if (content instanceof _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.FileEditor) {
                        void updateHandlerAndCommands(widget);
                    }
                }
            });
        }
        else {
            editorTracker.currentChanged.connect((_, documentWidget) => {
                if (documentWidget) {
                    void updateHandlerAndCommands(documentWidget);
                }
            });
        }
    }
};
/**
 * A plugin that provides visual debugging support for notebooks.
 */
const notebooks = {
    id: '@jupyterlab/debugger-extension:notebooks',
    autoStart: false,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.INotebookTracker, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    provides: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerHandler,
    activate: (app, service, notebookTracker, translator, labShell, palette) => {
        const handler = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Handler({
            type: 'notebook',
            shell: app.shell,
            service
        });
        const trans = translator.load('jupyterlab');
        app.commands.addCommand(_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.CommandIDs.restartDebug, {
            label: trans.__('Restart Kernel and Debug…'),
            caption: trans.__('Restart Kernel and Debug…'),
            isEnabled: () => service.isStarted,
            execute: async () => {
                const state = service.getDebuggerState();
                await service.stop();
                const widget = notebookTracker.currentWidget;
                if (!widget) {
                    return;
                }
                const { content, sessionContext } = widget;
                const restarted = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.sessionContextDialogs.restart(sessionContext);
                if (!restarted) {
                    return;
                }
                await service.restoreDebuggerState(state);
                await handler.updateWidget(widget, sessionContext.session);
                await _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.NotebookActions.runAll(content, sessionContext);
            }
        });
        const updateHandlerAndCommands = async (widget) => {
            if (widget) {
                const { sessionContext } = widget;
                await sessionContext.ready;
                await handler.updateContext(widget, sessionContext);
            }
            app.commands.notifyCommandChanged();
        };
        if (labShell) {
            labShell.currentChanged.connect((_, update) => {
                const widget = update.newValue;
                if (widget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.NotebookPanel) {
                    void updateHandlerAndCommands(widget);
                }
            });
        }
        else {
            notebookTracker.currentChanged.connect((_, notebookPanel) => {
                if (notebookPanel) {
                    void updateHandlerAndCommands(notebookPanel);
                }
            });
        }
        if (palette) {
            palette.addItem({
                category: 'Notebook Operations',
                command: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.CommandIDs.restartDebug
            });
        }
        return handler;
    }
};
/**
 * A plugin that provides a debugger service.
 */
const service = {
    id: '@jupyterlab/debugger-extension:service',
    autoStart: false,
    provides: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerConfig],
    optional: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerSources, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__.ITranslator],
    activate: (app, config, debuggerSources, translator) => new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Service({
        config,
        debuggerSources,
        specsManager: app.serviceManager.kernelspecs,
        translator
    })
};
/**
 * A plugin that provides a configuration with hash method.
 */
const configuration = {
    id: '@jupyterlab/debugger-extension:config',
    provides: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerConfig,
    autoStart: false,
    activate: () => new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Config()
};
/**
 * A plugin that provides source/editor functionality for debugging.
 */
const sources = {
    id: '@jupyterlab/debugger-extension:sources',
    autoStart: false,
    provides: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerSources,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerConfig, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices],
    optional: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.INotebookTracker, _jupyterlab_console__WEBPACK_IMPORTED_MODULE_3__.IConsoleTracker, _jupyterlab_fileeditor__WEBPACK_IMPORTED_MODULE_7__.IEditorTracker],
    activate: (app, config, editorServices, notebookTracker, consoleTracker, editorTracker) => {
        return new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Sources({
            config,
            shell: app.shell,
            editorServices,
            notebookTracker,
            consoleTracker,
            editorTracker
        });
    }
};
/*
 * A plugin to open detailed views for variables.
 */
const variables = {
    id: '@jupyterlab/debugger-extension:variables',
    autoStart: false,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerHandler, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager, _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10__.IRenderMimeRegistry],
    activate: (app, service, handler, translator, themeManager, rendermime) => {
        const trans = translator.load('jupyterlab');
        const { commands, shell } = app;
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'debugger/inspect-variable'
        });
        const trackerMime = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'debugger/render-variable'
        });
        const CommandIDs = _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.CommandIDs;
        // Add commands
        commands.addCommand(CommandIDs.inspectVariable, {
            label: trans.__('Inspect Variable'),
            caption: trans.__('Inspect Variable'),
            isEnabled: args => {
                var _a, _b, _c, _d;
                return !!((_a = service.session) === null || _a === void 0 ? void 0 : _a.isStarted) &&
                    ((_d = (_b = args.variableReference) !== null && _b !== void 0 ? _b : (_c = service.model.variables.selectedVariable) === null || _c === void 0 ? void 0 : _c.variablesReference) !== null && _d !== void 0 ? _d : 0) > 0;
            },
            execute: async (args) => {
                var _a, _b, _c, _d;
                let { variableReference, name } = args;
                if (!variableReference) {
                    variableReference =
                        (_a = service.model.variables.selectedVariable) === null || _a === void 0 ? void 0 : _a.variablesReference;
                }
                if (!name) {
                    name = (_b = service.model.variables.selectedVariable) === null || _b === void 0 ? void 0 : _b.name;
                }
                const id = `jp-debugger-variable-${name}`;
                if (!name ||
                    !variableReference ||
                    tracker.find(widget => widget.id === id)) {
                    return;
                }
                const variables = await service.inspectVariable(variableReference);
                if (!variables || variables.length === 0) {
                    return;
                }
                const model = service.model.variables;
                const widget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({
                    content: new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.VariablesGrid({
                        model,
                        commands,
                        scopes: [{ name, variables }],
                        themeManager
                    })
                });
                widget.addClass('jp-DebuggerVariables');
                widget.id = id;
                widget.title.icon = _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.variableIcon;
                widget.title.label = `${(_d = (_c = service.session) === null || _c === void 0 ? void 0 : _c.connection) === null || _d === void 0 ? void 0 : _d.name} - ${name}`;
                void tracker.add(widget);
                const disposeWidget = () => {
                    widget.dispose();
                    model.changed.disconnect(disposeWidget);
                };
                model.changed.connect(disposeWidget);
                shell.add(widget, 'main', {
                    mode: tracker.currentWidget ? 'split-right' : 'split-bottom',
                    activate: false,
                    type: 'Debugger Variables'
                });
            }
        });
        commands.addCommand(CommandIDs.renderMimeVariable, {
            label: trans.__('Render Variable'),
            caption: trans.__('Render variable according to its mime type'),
            isEnabled: () => { var _a; return !!((_a = service.session) === null || _a === void 0 ? void 0 : _a.isStarted); },
            isVisible: () => service.model.hasRichVariableRendering &&
                (rendermime !== null || handler.activeWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.NotebookPanel),
            execute: args => {
                var _a, _b, _c, _d, _e, _f, _g, _h;
                let { name, frameId } = args;
                if (!name) {
                    name = (_a = service.model.variables.selectedVariable) === null || _a === void 0 ? void 0 : _a.name;
                }
                if (!frameId) {
                    frameId = (_b = service.model.callstack.frame) === null || _b === void 0 ? void 0 : _b.id;
                }
                const activeWidget = handler.activeWidget;
                let activeRendermime = activeWidget instanceof _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_9__.NotebookPanel
                    ? activeWidget.content.rendermime
                    : rendermime;
                if (!activeRendermime) {
                    return;
                }
                const id = `jp-debugger-variable-mime-${name}-${(_d = (_c = service.session) === null || _c === void 0 ? void 0 : _c.connection) === null || _d === void 0 ? void 0 : _d.path.replace('/', '-')}`;
                if (!name || // Name is mandatory
                    trackerMime.find(widget => widget.id === id) || // Widget already exists
                    (!frameId && service.hasStoppedThreads()) // frame id missing on breakpoint
                ) {
                    return;
                }
                const variablesModel = service.model.variables;
                const widget = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.VariableRenderer({
                    dataLoader: () => service.inspectRichVariable(name, frameId),
                    rendermime: activeRendermime,
                    translator
                });
                widget.addClass('jp-DebuggerRichVariable');
                widget.id = id;
                widget.title.icon = _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.variableIcon;
                widget.title.label = `${name} - ${(_f = (_e = service.session) === null || _e === void 0 ? void 0 : _e.connection) === null || _f === void 0 ? void 0 : _f.name}`;
                widget.title.caption = `${name} - ${(_h = (_g = service.session) === null || _g === void 0 ? void 0 : _g.connection) === null || _h === void 0 ? void 0 : _h.path}`;
                void trackerMime.add(widget);
                const disposeWidget = () => {
                    widget.dispose();
                    variablesModel.changed.disconnect(refreshWidget);
                    activeWidget === null || activeWidget === void 0 ? void 0 : activeWidget.disposed.disconnect(disposeWidget);
                };
                const refreshWidget = () => {
                    // Refresh the widget only if the active element is the same.
                    if (handler.activeWidget === activeWidget) {
                        void widget.refresh();
                    }
                };
                widget.disposed.connect(disposeWidget);
                variablesModel.changed.connect(refreshWidget);
                activeWidget === null || activeWidget === void 0 ? void 0 : activeWidget.disposed.connect(disposeWidget);
                shell.add(widget, 'main', {
                    mode: trackerMime.currentWidget ? 'split-right' : 'split-bottom',
                    activate: false,
                    type: 'Debugger Variables'
                });
            }
        });
    }
};
/**
 * Debugger sidebar provider plugin.
 */
const sidebar = {
    id: '@jupyterlab/debugger-extension:sidebar',
    provides: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerSidebar,
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_11__.ISettingRegistry],
    autoStart: false,
    activate: async (app, service, editorServices, translator, themeManager, settingRegistry) => {
        const { commands } = app;
        const CommandIDs = _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.CommandIDs;
        const callstackCommands = {
            registry: commands,
            continue: CommandIDs.debugContinue,
            terminate: CommandIDs.terminate,
            next: CommandIDs.next,
            stepIn: CommandIDs.stepIn,
            stepOut: CommandIDs.stepOut,
            evaluate: CommandIDs.evaluate
        };
        const breakpointsCommands = {
            registry: commands,
            pause: CommandIDs.pause
        };
        const sidebar = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Sidebar({
            service,
            callstackCommands,
            breakpointsCommands,
            editorServices,
            themeManager,
            translator
        });
        if (settingRegistry) {
            const setting = await settingRegistry.load(main.id);
            const updateSettings = () => {
                var _a, _b, _c, _d;
                const filters = setting.get('variableFilters').composite;
                const kernel = (_d = (_c = (_b = (_a = service.session) === null || _a === void 0 ? void 0 : _a.connection) === null || _b === void 0 ? void 0 : _b.kernel) === null || _c === void 0 ? void 0 : _c.name) !== null && _d !== void 0 ? _d : '';
                if (kernel && filters[kernel]) {
                    sidebar.variables.filter = new Set(filters[kernel]);
                }
                const kernelSourcesFilter = setting.get('defaultKernelSourcesFilter')
                    .composite;
                sidebar.kernelSources.filter = kernelSourcesFilter;
            };
            updateSettings();
            setting.changed.connect(updateSettings);
            service.sessionChanged.connect(updateSettings);
        }
        return sidebar;
    }
};
/**
 * The main debugger UI plugin.
 */
const main = {
    id: '@jupyterlab/debugger-extension:main',
    requires: [_jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebugger, _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerSidebar, _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_2__.IEditorServices, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_12__.ITranslator],
    optional: [
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette,
        _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.IDebuggerSources,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_8__.ILoggerRegistry
    ],
    autoStart: false,
    activate: async (app, service, sidebar, editorServices, translator, palette, debuggerSources, labShell, restorer, loggerRegistry) => {
        var _a;
        const trans = translator.load('jupyterlab');
        const { commands, shell, serviceManager } = app;
        const { kernelspecs } = serviceManager;
        const CommandIDs = _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.CommandIDs;
        // First check if there is a PageConfig override for the extension visibility
        const alwaysShowDebuggerExtension = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.PageConfig.getOption('alwaysShowDebuggerExtension').toLowerCase() ===
            'true';
        if (!alwaysShowDebuggerExtension) {
            // hide the debugger sidebar if no kernel with support for debugging is available
            await kernelspecs.ready;
            const specs = (_a = kernelspecs.specs) === null || _a === void 0 ? void 0 : _a.kernelspecs;
            if (!specs) {
                return;
            }
            const enabled = Object.keys(specs).some(name => { var _a, _b, _c; return !!((_c = (_b = (_a = specs[name]) === null || _a === void 0 ? void 0 : _a.metadata) === null || _b === void 0 ? void 0 : _b['debugger']) !== null && _c !== void 0 ? _c : false); });
            if (!enabled) {
                return;
            }
        }
        // get the mime type of the kernel language for the current debug session
        const getMimeType = async () => {
            var _a, _b, _c;
            const kernel = (_b = (_a = service.session) === null || _a === void 0 ? void 0 : _a.connection) === null || _b === void 0 ? void 0 : _b.kernel;
            if (!kernel) {
                return '';
            }
            const info = (await kernel.info).language_info;
            const name = info.name;
            const mimeType = (_c = editorServices === null || editorServices === void 0 ? void 0 : editorServices.mimeTypeService.getMimeTypeByLanguage({ name })) !== null && _c !== void 0 ? _c : '';
            return mimeType;
        };
        const rendermime = new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10__.RenderMimeRegistry({ initialFactories: _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_10__.standardRendererFactories });
        commands.addCommand(CommandIDs.evaluate, {
            label: trans.__('Evaluate Code'),
            caption: trans.__('Evaluate Code'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.evaluateIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                var _a, _b, _c;
                const mimeType = await getMimeType();
                const result = await _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Dialogs.getCode({
                    title: trans.__('Evaluate Code'),
                    okLabel: trans.__('Evaluate'),
                    cancelLabel: trans.__('Cancel'),
                    mimeType,
                    rendermime
                });
                const code = result.value;
                if (!result.button.accept || !code) {
                    return;
                }
                const reply = await service.evaluate(code);
                if (reply) {
                    const data = reply.result;
                    const path = (_b = (_a = service === null || service === void 0 ? void 0 : service.session) === null || _a === void 0 ? void 0 : _a.connection) === null || _b === void 0 ? void 0 : _b.path;
                    const logger = path ? (_c = loggerRegistry === null || loggerRegistry === void 0 ? void 0 : loggerRegistry.getLogger) === null || _c === void 0 ? void 0 : _c.call(loggerRegistry, path) : undefined;
                    if (logger) {
                        // print to log console of the notebook currently being debugged
                        logger.log({ type: 'text', data, level: logger.level });
                    }
                    else {
                        // fallback to printing to devtools console
                        console.debug(data);
                    }
                }
            }
        });
        commands.addCommand(CommandIDs.debugContinue, {
            label: trans.__('Continue'),
            caption: trans.__('Continue'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.continueIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                await service.continue();
                commands.notifyCommandChanged();
            }
        });
        commands.addCommand(CommandIDs.terminate, {
            label: trans.__('Terminate'),
            caption: trans.__('Terminate'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.terminateIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                await service.restart();
                commands.notifyCommandChanged();
            }
        });
        commands.addCommand(CommandIDs.next, {
            label: trans.__('Next'),
            caption: trans.__('Next'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.stepOverIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                await service.next();
            }
        });
        commands.addCommand(CommandIDs.stepIn, {
            label: trans.__('Step In'),
            caption: trans.__('Step In'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.stepIntoIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                await service.stepIn();
            }
        });
        commands.addCommand(CommandIDs.stepOut, {
            label: trans.__('Step Out'),
            caption: trans.__('Step Out'),
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.stepOutIcon,
            isEnabled: () => service.hasStoppedThreads(),
            execute: async () => {
                await service.stepOut();
            }
        });
        commands.addCommand(CommandIDs.pause, {
            label: trans.__('Enable / Disable pausing on exceptions'),
            caption: () => service.isStarted
                ? service.pauseOnExceptionsIsValid()
                    ? service.isPausingOnExceptions
                        ? trans.__('Disable pausing on exceptions')
                        : trans.__('Enable pausing on exceptions')
                    : trans.__('Kernel does not support pausing on exceptions.')
                : trans.__('Enable / Disable pausing on exceptions'),
            className: 'jp-PauseOnExceptions',
            icon: _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.Icons.pauseOnExceptionsIcon,
            isToggled: () => {
                return service.isPausingOnExceptions;
            },
            isEnabled: () => service.pauseOnExceptionsIsValid(),
            execute: async () => {
                await service.pauseOnExceptions(!service.isPausingOnExceptions);
                commands.notifyCommandChanged();
            }
        });
        service.eventMessage.connect((_, event) => {
            commands.notifyCommandChanged();
            if (labShell && event.event === 'initialized') {
                labShell.activateById(sidebar.id);
            }
        });
        service.sessionChanged.connect(_ => {
            commands.notifyCommandChanged();
        });
        if (restorer) {
            restorer.add(sidebar, 'debugger-sidebar');
        }
        sidebar.node.setAttribute('role', 'region');
        sidebar.node.setAttribute('aria-label', trans.__('Debugger section'));
        sidebar.title.caption = trans.__('Debugger');
        shell.add(sidebar, 'right', { type: 'Debugger' });
        commands.addCommand(CommandIDs.showPanel, {
            label: translator.load('jupyterlab').__('Debugger Panel'),
            execute: () => {
                shell.activateById(sidebar.id);
            }
        });
        if (palette) {
            const category = trans.__('Debugger');
            [
                CommandIDs.debugContinue,
                CommandIDs.terminate,
                CommandIDs.next,
                CommandIDs.stepIn,
                CommandIDs.stepOut,
                CommandIDs.evaluate,
                CommandIDs.pause
            ].forEach(command => {
                palette.addItem({ command, category });
            });
        }
        if (debuggerSources) {
            const { model } = service;
            const readOnlyEditorFactory = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.ReadOnlyEditorFactory({
                editorServices
            });
            const onCurrentFrameChanged = (_, frame) => {
                var _a, _b, _c, _d, _e, _f, _g, _h, _j;
                debuggerSources
                    .find({
                    focus: true,
                    kernel: (_d = (_c = (_b = (_a = service.session) === null || _a === void 0 ? void 0 : _a.connection) === null || _b === void 0 ? void 0 : _b.kernel) === null || _c === void 0 ? void 0 : _c.name) !== null && _d !== void 0 ? _d : '',
                    path: (_g = (_f = (_e = service.session) === null || _e === void 0 ? void 0 : _e.connection) === null || _f === void 0 ? void 0 : _f.path) !== null && _g !== void 0 ? _g : '',
                    source: (_j = (_h = frame === null || frame === void 0 ? void 0 : frame.source) === null || _h === void 0 ? void 0 : _h.path) !== null && _j !== void 0 ? _j : ''
                })
                    .forEach(editor => {
                    requestAnimationFrame(() => {
                        _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.EditorHandler.showCurrentLine(editor, frame.line);
                    });
                });
            };
            const onSourceOpened = (_, source, breakpoint) => {
                var _a, _b, _c, _d, _e, _f, _g;
                if (!source) {
                    return;
                }
                const { content, mimeType, path } = source;
                const results = debuggerSources.find({
                    focus: true,
                    kernel: (_d = (_c = (_b = (_a = service.session) === null || _a === void 0 ? void 0 : _a.connection) === null || _b === void 0 ? void 0 : _b.kernel) === null || _c === void 0 ? void 0 : _c.name) !== null && _d !== void 0 ? _d : '',
                    path: (_g = (_f = (_e = service.session) === null || _e === void 0 ? void 0 : _e.connection) === null || _f === void 0 ? void 0 : _f.path) !== null && _g !== void 0 ? _g : '',
                    source: path
                });
                if (results.length > 0) {
                    if (breakpoint && typeof breakpoint.line !== 'undefined') {
                        results.forEach(editor => {
                            editor.revealPosition({
                                line: breakpoint.line - 1,
                                column: breakpoint.column || 0
                            });
                        });
                    }
                    return;
                }
                const editorWrapper = readOnlyEditorFactory.createNewEditor({
                    content,
                    mimeType,
                    path
                });
                const editor = editorWrapper.editor;
                const editorHandler = new _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.EditorHandler({
                    debuggerService: service,
                    editor,
                    path
                });
                editorWrapper.disposed.connect(() => editorHandler.dispose());
                debuggerSources.open({
                    label: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_4__.PathExt.basename(path),
                    caption: path,
                    editorWrapper
                });
                const frame = service.model.callstack.frame;
                if (frame) {
                    _jupyterlab_debugger__WEBPACK_IMPORTED_MODULE_5__.Debugger.EditorHandler.showCurrentLine(editor, frame.line);
                }
            };
            const onKernelSourceOpened = (_, source, breakpoint) => {
                if (!source) {
                    return;
                }
                onSourceOpened(null, source, breakpoint);
            };
            model.callstack.currentFrameChanged.connect(onCurrentFrameChanged);
            model.sources.currentSourceOpened.connect(onSourceOpened);
            model.kernelSources.kernelSourceOpened.connect(onKernelSourceOpened);
            model.breakpoints.clicked.connect(async (_, breakpoint) => {
                var _a;
                const path = (_a = breakpoint.source) === null || _a === void 0 ? void 0 : _a.path;
                const source = await service.getSource({
                    sourceReference: 0,
                    path
                });
                onSourceOpened(null, source, breakpoint);
            });
        }
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [
    service,
    consoles,
    files,
    notebooks,
    variables,
    sidebar,
    main,
    sources,
    configuration
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZGVidWdnZXItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy4xYTc2MWU1NWVlOWFiYTg4ZTUyOC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQU84QjtBQU9IO0FBQzJCO0FBQ1c7QUFDUjtBQVE5QjtBQUMyQjtBQUNXO0FBQ1g7QUFLM0I7QUFLRTtBQUUrQjtBQUNUO0FBRXREOztHQUVHO0FBQ0gsTUFBTSxRQUFRLEdBQWdDO0lBQzVDLEVBQUUsRUFBRSx5Q0FBeUM7SUFDN0MsU0FBUyxFQUFFLEtBQUs7SUFDaEIsUUFBUSxFQUFFLENBQUMsMkRBQVMsRUFBRSxnRUFBZSxDQUFDO0lBQ3RDLFFBQVEsRUFBRSxDQUFDLDhEQUFTLENBQUM7SUFDckIsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsS0FBZ0IsRUFDaEIsY0FBK0IsRUFDL0IsUUFBMEIsRUFDMUIsRUFBRTtRQUNGLE1BQU0sT0FBTyxHQUFHLElBQUksa0VBQWdCLENBQUM7WUFDbkMsSUFBSSxFQUFFLFNBQVM7WUFDZixLQUFLLEVBQUUsR0FBRyxDQUFDLEtBQUs7WUFDaEIsT0FBTyxFQUFFLEtBQUs7U0FDZixDQUFDLENBQUM7UUFFSCxNQUFNLHdCQUF3QixHQUFHLEtBQUssRUFDcEMsTUFBb0IsRUFDTCxFQUFFO1lBQ2pCLE1BQU0sRUFBRSxjQUFjLEVBQUUsR0FBRyxNQUFNLENBQUM7WUFDbEMsTUFBTSxjQUFjLENBQUMsS0FBSyxDQUFDO1lBQzNCLE1BQU0sT0FBTyxDQUFDLGFBQWEsQ0FBQyxNQUFNLEVBQUUsY0FBYyxDQUFDLENBQUM7WUFDcEQsR0FBRyxDQUFDLFFBQVEsQ0FBQyxvQkFBb0IsRUFBRSxDQUFDO1FBQ3RDLENBQUMsQ0FBQztRQUVGLElBQUksUUFBUSxFQUFFO1lBQ1osUUFBUSxDQUFDLGNBQWMsQ0FBQyxPQUFPLENBQUMsQ0FBQyxDQUFDLEVB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QUFLLENBQUMsU0FBUyxDQUFDLG1CQUFtQixDQUFDLE9BQU8sQ0FBQyxxQkFBcUIsQ0FBQyxDQUFDO1lBQ25FLEtBQUssQ0FBQyxPQUFPLENBQUMsbUJBQW1CLENBQUMsT0FBTyxDQUFDLGNBQWMsQ0FBQyxDQUFDO1lBQzFELEtBQUssQ0FBQyxhQUFhLENBQUMsa0JBQWtCLENBQUMsT0FBTyxDQUFDLG9CQUFvQixDQUFDLENBQUM7WUFDckUsS0FBSyxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLEtBQUssRUFBRSxDQUFDLEVBQUUsVUFBVSxFQUFFLEVBQUU7O2dCQUN4RCxNQUFNLElBQUksR0FBRyxnQkFBVSxDQUFDLE1BQU0sMENBQUUsSUFBSSxDQUFDO2dCQUNyQyxNQUFNLE1BQU0sR0FBRyxNQUFNLE9BQU8sQ0FBQyxTQUFTLENBQUM7b0JBQ3JDLGVBQWUsRUFBRSxDQUFDO29CQUNsQixJQUFJO2lCQUNMLENBQUMsQ0FBQztnQkFDSCxjQUFjLENBQUMsSUFBSSxFQUFFLE1BQU0sRUFBRSxVQUFVLENBQUMsQ0FBQztZQUMzQyxDQUFDLENBQUMsQ0FBQztTQUNKO0lBQ0gsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFpQztJQUM1QyxPQUFPO0lBQ1AsUUFBUTtJQUNSLEtBQUs7SUFDTCxTQUFTO0lBQ1QsU0FBUztJQUNULE9BQU87SUFDUCxJQUFJO0lBQ0osT0FBTztJQUNQLGFBQWE7Q0FDZCxDQUFDO0FBRUYsaUVBQWUsT0FBTyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RlYnVnZ2VyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgZGVidWdnZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIElDb21tYW5kUGFsZXR0ZSxcbiAgSVRoZW1lTWFuYWdlcixcbiAgTWFpbkFyZWFXaWRnZXQsXG4gIHNlc3Npb25Db250ZXh0RGlhbG9ncyxcbiAgV2lkZ2V0VHJhY2tlclxufSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJRWRpdG9yU2VydmljZXMgfSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7IENvbnNvbGVQYW5lbCwgSUNvbnNvbGVUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29uc29sZSc7XG5pbXBvcnQgeyBQYWdlQ29uZmlnLCBQYXRoRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIERlYnVnZ2VyLFxuICBJRGVidWdnZXIsXG4gIElEZWJ1Z2dlckNvbmZpZyxcbiAgSURlYnVnZ2VySGFuZGxlcixcbiAgSURlYnVnZ2VyU2lkZWJhcixcbiAgSURlYnVnZ2VyU291cmNlc1xufSBmcm9tICdAanVweXRlcmxhYi9kZWJ1Z2dlcic7XG5pbXBvcnQgeyBEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IEZpbGVFZGl0b3IsIElFZGl0b3JUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvZmlsZWVkaXRvcic7XG5pbXBvcnQgeyBJTG9nZ2VyUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9sb2djb25zb2xlJztcbmltcG9ydCB7XG4gIElOb3RlYm9va1RyYWNrZXIsXG4gIE5vdGVib29rQWN0aW9ucyxcbiAgTm90ZWJvb2tQYW5lbFxufSBmcm9tICdAanVweXRlcmxhYi9ub3RlYm9vayc7XG5pbXBvcnQge1xuICBzdGFuZGFyZFJlbmRlcmVyRmFjdG9yaWVzIGFzIGluaXRpYWxGYWN0b3JpZXMsXG4gIElSZW5kZXJNaW1lUmVnaXN0cnksXG4gIFJlbmRlck1pbWVSZWdpc3RyeVxufSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IFNlc3Npb24gfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIEEgcGx1Z2luIHRoYXQgcHJvdmlkZXMgdmlzdWFsIGRlYnVnZ2luZyBzdXBwb3J0IGZvciBjb25zb2xlcy5cbiAqL1xuY29uc3QgY29uc29sZXM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9kZWJ1Z2dlci1leHRlbnNpb246Y29uc29sZXMnLFxuICBhdXRvU3RhcnQ6IGZhbHNlLFxuICByZXF1aXJlczogW0lEZWJ1Z2dlciwgSUNvbnNvbGVUcmFja2VyXSxcbiAgb3B0aW9uYWw6IFtJTGFiU2hlbGxdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGRlYnVnOiBJRGVidWdnZXIsXG4gICAgY29uc29sZVRyYWNrZXI6IElDb25zb2xlVHJhY2tlcixcbiAgICBsYWJTaGVsbDogSUxhYlNoZWxsIHwgbnVsbFxuICApID0+IHtcbiAgICBjb25zdCBoYW5kbGVyID0gbmV3IERlYnVnZ2VyLkhhbmRsZXIoe1xuICAgICAgdHlwZTogJ2NvbnNvbGUnLFxuICAgICAgc2hlbGw6IGFwcC5zaGVsbCxcbiAgICAgIHNlcnZpY2U6IGRlYnVnXG4gICAgfSk7XG5cbiAgICBjb25zdCB1cGRhdGVIYW5kbGVyQW5kQ29tbWFuZHMgPSBhc3luYyAoXG4gICAgICB3aWRnZXQ6IENvbnNvbGVQYW5lbFxuICAgICk6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgICAgY29uc3QgeyBzZXNzaW9uQ29udGV4dCB9ID0gd2lkZ2V0O1xuICAgICAgYXdhaXQgc2Vzc2lvbkNvbnRleHQucmVhZHk7XG4gICAgICBhd2FpdCBoYW5kbGVyLnVwZGF0ZUNvbnRleHQod2lkZ2V0LCBzZXNzaW9uQ29udGV4dCk7XG4gICAgICBhcHAuY29tbWFuZHMubm90aWZ5Q29tbWFuZENoYW5nZWQoKTtcbiAgICB9O1xuXG4gICAgaWYgKGxhYlNoZWxsKSB7XG4gICAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KChfLCB1cGRhdGUpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdXBkYXRlLm5ld1ZhbHVlO1xuICAgICAgICBpZiAod2lkZ2V0IGluc3RhbmNlb2YgQ29uc29sZVBhbmVsKSB7XG4gICAgICAgICAgdm9pZCB1cGRhdGVIYW5kbGVyQW5kQ29tbWFuZHMod2lkZ2V0KTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIGNvbnNvbGVUcmFja2VyLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QoKF8sIGNvbnNvbGVQYW5lbCkgPT4ge1xuICAgICAgICBpZiAoY29uc29sZVBhbmVsKSB7XG4gICAgICAgICAgdm9pZCB1cGRhdGVIYW5kbGVyQW5kQ29tbWFuZHMoY29uc29sZVBhbmVsKTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuICB9XG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHRoYXQgcHJvdmlkZXMgdmlzdWFsIGRlYnVnZ2luZyBzdXBwb3J0IGZvciBmaWxlIGVkaXRvcnMuXG4gKi9cbmNvbnN0IGZpbGVzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZGVidWdnZXItZXh0ZW5zaW9uOmZpbGVzJyxcbiAgYXV0b1N0YXJ0OiBmYWxzZSxcbiAgcmVxdWlyZXM6IFtJRGVidWdnZXIsIElFZGl0b3JUcmFja2VyXSxcbiAgb3B0aW9uYWw6IFtJTGFiU2hlbGxdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGRlYnVnOiBJRGVidWdnZXIsXG4gICAgZWRpdG9yVHJhY2tlcjogSUVkaXRvclRyYWNrZXIsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgaGFuZGxlciA9IG5ldyBEZWJ1Z2dlci5IYW5kbGVyKHtcbiAgICAgIHR5cGU6ICdmaWxlJyxcbiAgICAgIHNoZWxsOiBhcHAuc2hlbGwsXG4gICAgICBzZXJ2aWNlOiBkZWJ1Z1xuICAgIH0pO1xuXG4gICAgY29uc3QgYWN0aXZlU2Vzc2lvbnM6IHtcbiAgICAgIFtpZDogc3RyaW5nXTogU2Vzc2lvbi5JU2Vzc2lvbkNvbm5lY3Rpb247XG4gICAgfSA9IHt9O1xuXG4gICAgY29uc3QgdXBkYXRlSGFuZGxlckFuZENvbW1hbmRzID0gYXN5bmMgKFxuICAgICAgd2lkZ2V0OiBEb2N1bWVudFdpZGdldFxuICAgICk6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgICAgY29uc3Qgc2Vzc2lvbnMgPSBhcHAuc2VydmljZU1hbmFnZXIuc2Vzc2lvbnM7XG4gICAgICB0cnkge1xuICAgICAgICBjb25zdCBtb2RlbCA9IGF3YWl0IHNlc3Npb25zLmZpbmRCeVBhdGgod2lkZ2V0LmNvbnRleHQucGF0aCk7XG4gICAgICAgIGlmICghbW9kZWwpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgbGV0IHNlc3Npb24gPSBhY3RpdmVTZXNzaW9uc1ttb2RlbC5pZF07XG4gICAgICAgIGlmICghc2Vzc2lvbikge1xuICAgICAgICAgIC8vIFVzZSBgY29ubmVjdFRvYCBvbmx5IGlmIHRoZSBzZXNzaW9uIGRvZXMgbm90IGV4aXN0LlxuICAgICAgICAgIC8vIGBjb25uZWN0VG9gIHNlbmRzIGEga2VybmVsX2luZm9fcmVxdWVzdCBvbiB0aGUgc2hlbGxcbiAgICAgICAgICAvLyBjaGFubmVsLCB3aGljaCBibG9ja3MgdGhlIGRlYnVnIHNlc3Npb24gcmVzdG9yZSB3aGVuIHdhaXRpbmdcbiAgICAgICAgICAvLyBmb3IgdGhlIGtlcm5lbCB0byBiZSByZWFkeVxuICAgICAgICAgIHNlc3Npb24gPSBzZXNzaW9ucy5jb25uZWN0VG8oeyBtb2RlbCB9KTtcbiAgICAgICAgICBhY3RpdmVTZXNzaW9uc1ttb2RlbC5pZF0gPSBzZXNzaW9uO1xuICAgICAgICB9XG4gICAgICAgIGF3YWl0IGhhbmRsZXIudXBkYXRlKHdpZGdldCwgc2Vzc2lvbik7XG4gICAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgICAgfSBjYXRjaCB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICB9O1xuXG4gICAgaWYgKGxhYlNoZWxsKSB7XG4gICAgICBsYWJTaGVsbC5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KChfLCB1cGRhdGUpID0+IHtcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gdXBkYXRlLm5ld1ZhbHVlO1xuICAgICAgICBpZiAod2lkZ2V0IGluc3RhbmNlb2YgRG9jdW1lbnRXaWRnZXQpIHtcbiAgICAgICAgICBjb25zdCB7IGNvbnRlbnQgfSA9IHdpZGdldDtcbiAgICAgICAgICBpZiAoY29udGVudCBpbnN0YW5jZW9mIEZpbGVFZGl0b3IpIHtcbiAgICAgICAgICAgIHZvaWQgdXBkYXRlSGFuZGxlckFuZENvbW1hbmRzKHdpZGdldCk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9IGVsc2Uge1xuICAgICAgZWRpdG9yVHJhY2tlci5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KChfLCBkb2N1bWVudFdpZGdldCkgPT4ge1xuICAgICAgICBpZiAoZG9jdW1lbnRXaWRnZXQpIHtcbiAgICAgICAgICB2b2lkIHVwZGF0ZUhhbmRsZXJBbmRDb21tYW5kcyhcbiAgICAgICAgICAgIGRvY3VtZW50V2lkZ2V0IGFzIHVua25vd24gYXMgRG9jdW1lbnRXaWRnZXRcbiAgICAgICAgICApO1xuICAgICAgICB9XG4gICAgICB9KTtcbiAgICB9XG4gIH1cbn07XG5cbi8qKlxuICogQSBwbHVnaW4gdGhhdCBwcm92aWRlcyB2aXN1YWwgZGVidWdnaW5nIHN1cHBvcnQgZm9yIG5vdGVib29rcy5cbiAqL1xuY29uc3Qgbm90ZWJvb2tzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SURlYnVnZ2VyLklIYW5kbGVyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9kZWJ1Z2dlci1leHRlbnNpb246bm90ZWJvb2tzJyxcbiAgYXV0b1N0YXJ0OiBmYWxzZSxcbiAgcmVxdWlyZXM6IFtJRGVidWdnZXIsIElOb3RlYm9va1RyYWNrZXIsIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJTGFiU2hlbGwsIElDb21tYW5kUGFsZXR0ZV0sXG4gIHByb3ZpZGVzOiBJRGVidWdnZXJIYW5kbGVyLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHNlcnZpY2U6IElEZWJ1Z2dlcixcbiAgICBub3RlYm9va1RyYWNrZXI6IElOb3RlYm9va1RyYWNrZXIsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgbGFiU2hlbGw6IElMYWJTaGVsbCB8IG51bGwsXG4gICAgcGFsZXR0ZTogSUNvbW1hbmRQYWxldHRlIHwgbnVsbFxuICApOiBEZWJ1Z2dlci5IYW5kbGVyID0+IHtcbiAgICBjb25zdCBoYW5kbGVyID0gbmV3IERlYnVnZ2VyLkhhbmRsZXIoe1xuICAgICAgdHlwZTogJ25vdGVib29rJyxcbiAgICAgIHNoZWxsOiBhcHAuc2hlbGwsXG4gICAgICBzZXJ2aWNlXG4gICAgfSk7XG5cbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKERlYnVnZ2VyLkNvbW1hbmRJRHMucmVzdGFydERlYnVnLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1Jlc3RhcnQgS2VybmVsIGFuZCBEZWJ1Z+KApicpLFxuICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ1Jlc3RhcnQgS2VybmVsIGFuZCBEZWJ1Z+KApicpLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBzZXJ2aWNlLmlzU3RhcnRlZCxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgY29uc3Qgc3RhdGUgPSBzZXJ2aWNlLmdldERlYnVnZ2VyU3RhdGUoKTtcbiAgICAgICAgYXdhaXQgc2VydmljZS5zdG9wKCk7XG5cbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gbm90ZWJvb2tUcmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgeyBjb250ZW50LCBzZXNzaW9uQ29udGV4dCB9ID0gd2lkZ2V0O1xuICAgICAgICBjb25zdCByZXN0YXJ0ZWQgPSBhd2FpdCBzZXNzaW9uQ29udGV4dERpYWxvZ3MucmVzdGFydChzZXNzaW9uQ29udGV4dCk7XG4gICAgICAgIGlmICghcmVzdGFydGVkKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgYXdhaXQgc2VydmljZS5yZXN0b3JlRGVidWdnZXJTdGF0ZShzdGF0ZSk7XG4gICAgICAgIGF3YWl0IGhhbmRsZXIudXBkYXRlV2lkZ2V0KHdpZGdldCwgc2Vzc2lvbkNvbnRleHQuc2Vzc2lvbik7XG4gICAgICAgIGF3YWl0IE5vdGVib29rQWN0aW9ucy5ydW5BbGwoY29udGVudCwgc2Vzc2lvbkNvbnRleHQpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29uc3QgdXBkYXRlSGFuZGxlckFuZENvbW1hbmRzID0gYXN5bmMgKFxuICAgICAgd2lkZ2V0OiBOb3RlYm9va1BhbmVsXG4gICAgKTogUHJvbWlzZTx2b2lkPiA9PiB7XG4gICAgICBpZiAod2lkZ2V0KSB7XG4gICAgICAgIGNvbnN0IHsgc2Vzc2lvbkNvbnRleHQgfSA9IHdpZGdldDtcbiAgICAgICAgYXdhaXQgc2Vzc2lvbkNvbnRleHQucmVhZHk7XG4gICAgICAgIGF3YWl0IGhhbmRsZXIudXBkYXRlQ29udGV4dCh3aWRnZXQsIHNlc3Npb25Db250ZXh0KTtcbiAgICAgIH1cbiAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgIH07XG5cbiAgICBpZiAobGFiU2hlbGwpIHtcbiAgICAgIGxhYlNoZWxsLmN1cnJlbnRDaGFuZ2VkLmNvbm5lY3QoKF8sIHVwZGF0ZSkgPT4ge1xuICAgICAgICBjb25zdCB3aWRnZXQgPSB1cGRhdGUubmV3VmFsdWU7XG4gICAgICAgIGlmICh3aWRnZXQgaW5zdGFuY2VvZiBOb3RlYm9va1BhbmVsKSB7XG4gICAgICAgICAgdm9pZCB1cGRhdGVIYW5kbGVyQW5kQ29tbWFuZHMod2lkZ2V0KTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIG5vdGVib29rVHJhY2tlci5jdXJyZW50Q2hhbmdlZC5jb25uZWN0KChfLCBub3RlYm9va1BhbmVsKSA9PiB7XG4gICAgICAgIGlmIChub3RlYm9va1BhbmVsKSB7XG4gICAgICAgICAgdm9pZCB1cGRhdGVIYW5kbGVyQW5kQ29tbWFuZHMobm90ZWJvb2tQYW5lbCk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH1cblxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICBwYWxldHRlLmFkZEl0ZW0oe1xuICAgICAgICBjYXRlZ29yeTogJ05vdGVib29rIE9wZXJhdGlvbnMnLFxuICAgICAgICBjb21tYW5kOiBEZWJ1Z2dlci5Db21tYW5kSURzLnJlc3RhcnREZWJ1Z1xuICAgICAgfSk7XG4gICAgfVxuXG4gICAgcmV0dXJuIGhhbmRsZXI7XG4gIH1cbn07XG5cbi8qKlxuICogQSBwbHVnaW4gdGhhdCBwcm92aWRlcyBhIGRlYnVnZ2VyIHNlcnZpY2UuXG4gKi9cbmNvbnN0IHNlcnZpY2U6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJRGVidWdnZXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RlYnVnZ2VyLWV4dGVuc2lvbjpzZXJ2aWNlJyxcbiAgYXV0b1N0YXJ0OiBmYWxzZSxcbiAgcHJvdmlkZXM6IElEZWJ1Z2dlcixcbiAgcmVxdWlyZXM6IFtJRGVidWdnZXJDb25maWddLFxuICBvcHRpb25hbDogW0lEZWJ1Z2dlclNvdXJjZXMsIElUcmFuc2xhdG9yXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBjb25maWc6IElEZWJ1Z2dlci5JQ29uZmlnLFxuICAgIGRlYnVnZ2VyU291cmNlczogSURlYnVnZ2VyLklTb3VyY2VzIHwgbnVsbCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKSA9PlxuICAgIG5ldyBEZWJ1Z2dlci5TZXJ2aWNlKHtcbiAgICAgIGNvbmZpZyxcbiAgICAgIGRlYnVnZ2VyU291cmNlcyxcbiAgICAgIHNwZWNzTWFuYWdlcjogYXBwLnNlcnZpY2VNYW5hZ2VyLmtlcm5lbHNwZWNzLFxuICAgICAgdHJhbnNsYXRvclxuICAgIH0pXG59O1xuXG4vKipcbiAqIEEgcGx1Z2luIHRoYXQgcHJvdmlkZXMgYSBjb25maWd1cmF0aW9uIHdpdGggaGFzaCBtZXRob2QuXG4gKi9cbmNvbnN0IGNvbmZpZ3VyYXRpb246IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJRGVidWdnZXIuSUNvbmZpZz4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZGVidWdnZXItZXh0ZW5zaW9uOmNvbmZpZycsXG4gIHByb3ZpZGVzOiBJRGVidWdnZXJDb25maWcsXG4gIGF1dG9TdGFydDogZmFsc2UsXG4gIGFjdGl2YXRlOiAoKSA9PiBuZXcgRGVidWdnZXIuQ29uZmlnKClcbn07XG5cbi8qKlxuICogQSBwbHVnaW4gdGhhdCBwcm92aWRlcyBzb3VyY2UvZWRpdG9yIGZ1bmN0aW9uYWxpdHkgZm9yIGRlYnVnZ2luZy5cbiAqL1xuY29uc3Qgc291cmNlczogSnVweXRlckZyb250RW5kUGx1Z2luPElEZWJ1Z2dlci5JU291cmNlcz4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZGVidWdnZXItZXh0ZW5zaW9uOnNvdXJjZXMnLFxuICBhdXRvU3RhcnQ6IGZhbHNlLFxuICBwcm92aWRlczogSURlYnVnZ2VyU291cmNlcyxcbiAgcmVxdWlyZXM6IFtJRGVidWdnZXJDb25maWcsIElFZGl0b3JTZXJ2aWNlc10sXG4gIG9wdGlvbmFsOiBbSU5vdGVib29rVHJhY2tlciwgSUNvbnNvbGVUcmFja2VyLCBJRWRpdG9yVHJhY2tlcl0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgY29uZmlnOiBJRGVidWdnZXIuSUNvbmZpZyxcbiAgICBlZGl0b3JTZXJ2aWNlczogSUVkaXRvclNlcnZpY2VzLFxuICAgIG5vdGVib29rVHJhY2tlcjogSU5vdGVib29rVHJhY2tlciB8IG51bGwsXG4gICAgY29uc29sZVRyYWNrZXI6IElDb25zb2xlVHJhY2tlciB8IG51bGwsXG4gICAgZWRpdG9yVHJhY2tlcjogSUVkaXRvclRyYWNrZXIgfCBudWxsXG4gICk6IElEZWJ1Z2dlci5JU291cmNlcyA9PiB7XG4gICAgcmV0dXJuIG5ldyBEZWJ1Z2dlci5Tb3VyY2VzKHtcbiAgICAgIGNvbmZpZyxcbiAgICAgIHNoZWxsOiBhcHAuc2hlbGwsXG4gICAgICBlZGl0b3JTZXJ2aWNlcyxcbiAgICAgIG5vdGVib29rVHJhY2tlcixcbiAgICAgIGNvbnNvbGVUcmFja2VyLFxuICAgICAgZWRpdG9yVHJhY2tlclxuICAgIH0pO1xuICB9XG59O1xuLypcbiAqIEEgcGx1Z2luIHRvIG9wZW4gZGV0YWlsZWQgdmlld3MgZm9yIHZhcmlhYmxlcy5cbiAqL1xuY29uc3QgdmFyaWFibGVzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZGVidWdnZXItZXh0ZW5zaW9uOnZhcmlhYmxlcycsXG4gIGF1dG9TdGFydDogZmFsc2UsXG4gIHJlcXVpcmVzOiBbSURlYnVnZ2VyLCBJRGVidWdnZXJIYW5kbGVyLCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSVRoZW1lTWFuYWdlciwgSVJlbmRlck1pbWVSZWdpc3RyeV0sXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgc2VydmljZTogSURlYnVnZ2VyLFxuICAgIGhhbmRsZXI6IERlYnVnZ2VyLkhhbmRsZXIsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gICAgdGhlbWVNYW5hZ2VyOiBJVGhlbWVNYW5hZ2VyIHwgbnVsbCxcbiAgICByZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5IHwgbnVsbFxuICApID0+IHtcbiAgICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHsgY29tbWFuZHMsIHNoZWxsIH0gPSBhcHA7XG4gICAgY29uc3QgdHJhY2tlciA9IG5ldyBXaWRnZXRUcmFja2VyPE1haW5BcmVhV2lkZ2V0PERlYnVnZ2VyLlZhcmlhYmxlc0dyaWQ+Pih7XG4gICAgICBuYW1lc3BhY2U6ICdkZWJ1Z2dlci9pbnNwZWN0LXZhcmlhYmxlJ1xuICAgIH0pO1xuICAgIGNvbnN0IHRyYWNrZXJNaW1lID0gbmV3IFdpZGdldFRyYWNrZXI8RGVidWdnZXIuVmFyaWFibGVSZW5kZXJlcj4oe1xuICAgICAgbmFtZXNwYWNlOiAnZGVidWdnZXIvcmVuZGVyLXZhcmlhYmxlJ1xuICAgIH0pO1xuICAgIGNvbnN0IENvbW1hbmRJRHMgPSBEZWJ1Z2dlci5Db21tYW5kSURzO1xuXG4gICAgLy8gQWRkIGNvbW1hbmRzXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmluc3BlY3RWYXJpYWJsZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdJbnNwZWN0IFZhcmlhYmxlJyksXG4gICAgICBjYXB0aW9uOiB0cmFucy5fXygnSW5zcGVjdCBWYXJpYWJsZScpLFxuICAgICAgaXNFbmFibGVkOiBhcmdzID0+XG4gICAgICAgICEhc2VydmljZS5zZXNzaW9uPy5pc1N0YXJ0ZWQgJiZcbiAgICAgICAgKGFyZ3MudmFyaWFibGVSZWZlcmVuY2UgPz9cbiAgICAgICAgICBzZXJ2aWNlLm1vZGVsLnZhcmlhYmxlcy5zZWxlY3RlZFZhcmlhYmxlPy52YXJpYWJsZXNSZWZlcmVuY2UgPz9cbiAgICAgICAgICAwKSA+IDAsXG4gICAgICBleGVjdXRlOiBhc3luYyBhcmdzID0+IHtcbiAgICAgICAgbGV0IHsgdmFyaWFibGVSZWZlcmVuY2UsIG5hbWUgfSA9IGFyZ3MgYXMge1xuICAgICAgICAgIHZhcmlhYmxlUmVmZXJlbmNlPzogbnVtYmVyO1xuICAgICAgICAgIG5hbWU/OiBzdHJpbmc7XG4gICAgICAgIH07XG5cbiAgICAgICAgaWYgKCF2YXJpYWJsZVJlZmVyZW5jZSkge1xuICAgICAgICAgIHZhcmlhYmxlUmVmZXJlbmNlID1cbiAgICAgICAgICAgIHNlcnZpY2UubW9kZWwudmFyaWFibGVzLnNlbGVjdGVkVmFyaWFibGU/LnZhcmlhYmxlc1JlZmVyZW5jZTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoIW5hbWUpIHtcbiAgICAgICAgICBuYW1lID0gc2VydmljZS5tb2RlbC52YXJpYWJsZXMuc2VsZWN0ZWRWYXJpYWJsZT8ubmFtZTtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGlkID0gYGpwLWRlYnVnZ2VyLXZhcmlhYmxlLSR7bmFtZX1gO1xuICAgICAgICBpZiAoXG4gICAgICAgICAgIW5hbWUgfHxcbiAgICAgICAgICAhdmFyaWFibGVSZWZlcmVuY2UgfHxcbiAgICAgICAgICB0cmFja2VyLmZpbmQod2lkZ2V0ID0+IHdpZGdldC5pZCA9PT0gaWQpXG4gICAgICAgICkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IHZhcmlhYmxlcyA9IGF3YWl0IHNlcnZpY2UuaW5zcGVjdFZhcmlhYmxlKFxuICAgICAgICAgIHZhcmlhYmxlUmVmZXJlbmNlIGFzIG51bWJlclxuICAgICAgICApO1xuICAgICAgICBpZiAoIXZhcmlhYmxlcyB8fCB2YXJpYWJsZXMubGVuZ3RoID09PSAwKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgbW9kZWwgPSBzZXJ2aWNlLm1vZGVsLnZhcmlhYmxlcztcbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gbmV3IE1haW5BcmVhV2lkZ2V0PERlYnVnZ2VyLlZhcmlhYmxlc0dyaWQ+KHtcbiAgICAgICAgICBjb250ZW50OiBuZXcgRGVidWdnZXIuVmFyaWFibGVzR3JpZCh7XG4gICAgICAgICAgICBtb2RlbCxcbiAgICAgICAgICAgIGNvbW1hbmRzLFxuICAgICAgICAgICAgc2NvcGVzOiBbeyBuYW1lLCB2YXJpYWJsZXMgfV0sXG4gICAgICAgICAgICB0aGVtZU1hbmFnZXJcbiAgICAgICAgICB9KVxuICAgICAgICB9KTtcbiAgICAgICAgd2lkZ2V0LmFkZENsYXNzKCdqcC1EZWJ1Z2dlclZhcmlhYmxlcycpO1xuICAgICAgICB3aWRnZXQuaWQgPSBpZDtcbiAgICAgICAgd2lkZ2V0LnRpdGxlLmljb24gPSBEZWJ1Z2dlci5JY29ucy52YXJpYWJsZUljb247XG4gICAgICAgIHdpZGdldC50aXRsZS5sYWJlbCA9IGAke3NlcnZpY2Uuc2Vzc2lvbj8uY29ubmVjdGlvbj8ubmFtZX0gLSAke25hbWV9YDtcbiAgICAgICAgdm9pZCB0cmFja2VyLmFkZCh3aWRnZXQpO1xuICAgICAgICBjb25zdCBkaXNwb3NlV2lkZ2V0ID0gKCkgPT4ge1xuICAgICAgICAgIHdpZGdldC5kaXNwb3NlKCk7XG4gICAgICAgICAgbW9kZWwuY2hhbmdlZC5kaXNjb25uZWN0KGRpc3Bvc2VXaWRnZXQpO1xuICAgICAgICB9O1xuICAgICAgICBtb2RlbC5jaGFuZ2VkLmNvbm5lY3QoZGlzcG9zZVdpZGdldCk7XG4gICAgICAgIHNoZWxsLmFkZCh3aWRnZXQsICdtYWluJywge1xuICAgICAgICAgIG1vZGU6IHRyYWNrZXIuY3VycmVudFdpZGdldCA/ICdzcGxpdC1yaWdodCcgOiAnc3BsaXQtYm90dG9tJyxcbiAgICAgICAgICBhY3RpdmF0ZTogZmFsc2UsXG4gICAgICAgICAgdHlwZTogJ0RlYnVnZ2VyIFZhcmlhYmxlcydcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMucmVuZGVyTWltZVZhcmlhYmxlLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1JlbmRlciBWYXJpYWJsZScpLFxuICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ1JlbmRlciB2YXJpYWJsZSBhY2NvcmRpbmcgdG8gaXRzIG1pbWUgdHlwZScpLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiAhIXNlcnZpY2Uuc2Vzc2lvbj8uaXNTdGFydGVkLFxuICAgICAgaXNWaXNpYmxlOiAoKSA9PlxuICAgICAgICBzZXJ2aWNlLm1vZGVsLmhhc1JpY2hWYXJpYWJsZVJlbmRlcmluZyAmJlxuICAgICAgICAocmVuZGVybWltZSAhPT0gbnVsbCB8fCBoYW5kbGVyLmFjdGl2ZVdpZGdldCBpbnN0YW5jZW9mIE5vdGVib29rUGFuZWwpLFxuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGxldCB7IG5hbWUsIGZyYW1lSWQgfSA9IGFyZ3MgYXMge1xuICAgICAgICAgIGZyYW1lSWQ/OiBudW1iZXI7XG4gICAgICAgICAgbmFtZT86IHN0cmluZztcbiAgICAgICAgfTtcblxuICAgICAgICBpZiAoIW5hbWUpIHtcbiAgICAgICAgICBuYW1lID0gc2VydmljZS5tb2RlbC52YXJpYWJsZXMuc2VsZWN0ZWRWYXJpYWJsZT8ubmFtZTtcbiAgICAgICAgfVxuICAgICAgICBpZiAoIWZyYW1lSWQpIHtcbiAgICAgICAgICBmcmFtZUlkID0gc2VydmljZS5tb2RlbC5jYWxsc3RhY2suZnJhbWU/LmlkO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgYWN0aXZlV2lkZ2V0ID0gaGFuZGxlci5hY3RpdmVXaWRnZXQ7XG4gICAgICAgIGxldCBhY3RpdmVSZW5kZXJtaW1lID1cbiAgICAgICAgICBhY3RpdmVXaWRnZXQgaW5zdGFuY2VvZiBOb3RlYm9va1BhbmVsXG4gICAgICAgICAgICA/IGFjdGl2ZVdpZGdldC5jb250ZW50LnJlbmRlcm1pbWVcbiAgICAgICAgICAgIDogcmVuZGVybWltZTtcblxuICAgICAgICBpZiAoIWFjdGl2ZVJlbmRlcm1pbWUpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBjb25zdCBpZCA9IGBqcC1kZWJ1Z2dlci12YXJpYWJsZS1taW1lLSR7bmFtZX0tJHtzZXJ2aWNlLnNlc3Npb24/LmNvbm5lY3Rpb24/LnBhdGgucmVwbGFjZShcbiAgICAgICAgICAnLycsXG4gICAgICAgICAgJy0nXG4gICAgICAgICl9YDtcbiAgICAgICAgaWYgKFxuICAgICAgICAgICFuYW1lIHx8IC8vIE5hbWUgaXMgbWFuZGF0b3J5XG4gICAgICAgICAgdHJhY2tlck1pbWUuZmluZCh3aWRnZXQgPT4gd2lkZ2V0LmlkID09PSBpZCkgfHwgLy8gV2lkZ2V0IGFscmVhZHkgZXhpc3RzXG4gICAgICAgICAgKCFmcmFtZUlkICYmIHNlcnZpY2UuaGFzU3RvcHBlZFRocmVhZHMoKSkgLy8gZnJhbWUgaWQgbWlzc2luZyBvbiBicmVha3BvaW50XG4gICAgICAgICkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IHZhcmlhYmxlc01vZGVsID0gc2VydmljZS5tb2RlbC52YXJpYWJsZXM7XG5cbiAgICAgICAgY29uc3Qgd2lkZ2V0ID0gbmV3IERlYnVnZ2VyLlZhcmlhYmxlUmVuZGVyZXIoe1xuICAgICAgICAgIGRhdGFMb2FkZXI6ICgpID0+IHNlcnZpY2UuaW5zcGVjdFJpY2hWYXJpYWJsZShuYW1lISwgZnJhbWVJZCksXG4gICAgICAgICAgcmVuZGVybWltZTogYWN0aXZlUmVuZGVybWltZSxcbiAgICAgICAgICB0cmFuc2xhdG9yXG4gICAgICAgIH0pO1xuICAgICAgICB3aWRnZXQuYWRkQ2xhc3MoJ2pwLURlYnVnZ2VyUmljaFZhcmlhYmxlJyk7XG4gICAgICAgIHdpZGdldC5pZCA9IGlkO1xuICAgICAgICB3aWRnZXQudGl0bGUuaWNvbiA9IERlYnVnZ2VyLkljb25zLnZhcmlhYmxlSWNvbjtcbiAgICAgICAgd2lkZ2V0LnRpdGxlLmxhYmVsID0gYCR7bmFtZX0gLSAke3NlcnZpY2Uuc2Vzc2lvbj8uY29ubmVjdGlvbj8ubmFtZX1gO1xuICAgICAgICB3aWRnZXQudGl0bGUuY2FwdGlvbiA9IGAke25hbWV9IC0gJHtzZXJ2aWNlLnNlc3Npb24/LmNvbm5lY3Rpb24/LnBhdGh9YDtcbiAgICAgICAgdm9pZCB0cmFja2VyTWltZS5hZGQod2lkZ2V0KTtcbiAgICAgICAgY29uc3QgZGlzcG9zZVdpZGdldCA9ICgpID0+IHtcbiAgICAgICAgICB3aWRnZXQuZGlzcG9zZSgpO1xuICAgICAgICAgIHZhcmlhYmxlc01vZGVsLmNoYW5nZWQuZGlzY29ubmVjdChyZWZyZXNoV2lkZ2V0KTtcbiAgICAgICAgICBhY3RpdmVXaWRnZXQ/LmRpc3Bvc2VkLmRpc2Nvbm5lY3QoZGlzcG9zZVdpZGdldCk7XG4gICAgICAgIH07XG4gICAgICAgIGNvbnN0IHJlZnJlc2hXaWRnZXQgPSAoKSA9PiB7XG4gICAgICAgICAgLy8gUmVmcmVzaCB0aGUgd2lkZ2V0IG9ubHkgaWYgdGhlIGFjdGl2ZSBlbGVtZW50IGlzIHRoZSBzYW1lLlxuICAgICAgICAgIGlmIChoYW5kbGVyLmFjdGl2ZVdpZGdldCA9PT0gYWN0aXZlV2lkZ2V0KSB7XG4gICAgICAgICAgICB2b2lkIHdpZGdldC5yZWZyZXNoKCk7XG4gICAgICAgICAgfVxuICAgICAgICB9O1xuICAgICAgICB3aWRnZXQuZGlzcG9zZWQuY29ubmVjdChkaXNwb3NlV2lkZ2V0KTtcbiAgICAgICAgdmFyaWFibGVzTW9kZWwuY2hhbmdlZC5jb25uZWN0KHJlZnJlc2hXaWRnZXQpO1xuICAgICAgICBhY3RpdmVXaWRnZXQ/LmRpc3Bvc2VkLmNvbm5lY3QoZGlzcG9zZVdpZGdldCk7XG5cbiAgICAgICAgc2hlbGwuYWRkKHdpZGdldCwgJ21haW4nLCB7XG4gICAgICAgICAgbW9kZTogdHJhY2tlck1pbWUuY3VycmVudFdpZGdldCA/ICdzcGxpdC1yaWdodCcgOiAnc3BsaXQtYm90dG9tJyxcbiAgICAgICAgICBhY3RpdmF0ZTogZmFsc2UsXG4gICAgICAgICAgdHlwZTogJ0RlYnVnZ2VyIFZhcmlhYmxlcydcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogRGVidWdnZXIgc2lkZWJhciBwcm92aWRlciBwbHVnaW4uXG4gKi9cbmNvbnN0IHNpZGViYXI6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJRGVidWdnZXIuSVNpZGViYXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RlYnVnZ2VyLWV4dGVuc2lvbjpzaWRlYmFyJyxcbiAgcHJvdmlkZXM6IElEZWJ1Z2dlclNpZGViYXIsXG4gIHJlcXVpcmVzOiBbSURlYnVnZ2VyLCBJRWRpdG9yU2VydmljZXMsIElUcmFuc2xhdG9yXSxcbiAgb3B0aW9uYWw6IFtJVGhlbWVNYW5hZ2VyLCBJU2V0dGluZ1JlZ2lzdHJ5XSxcbiAgYXV0b1N0YXJ0OiBmYWxzZSxcbiAgYWN0aXZhdGU6IGFzeW5jIChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBzZXJ2aWNlOiBJRGVidWdnZXIsXG4gICAgZWRpdG9yU2VydmljZXM6IElFZGl0b3JTZXJ2aWNlcyxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcixcbiAgICB0aGVtZU1hbmFnZXI6IElUaGVtZU1hbmFnZXIgfCBudWxsLFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSB8IG51bGxcbiAgKTogUHJvbWlzZTxJRGVidWdnZXIuSVNpZGViYXI+ID0+IHtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgY29uc3QgQ29tbWFuZElEcyA9IERlYnVnZ2VyLkNvbW1hbmRJRHM7XG5cbiAgICBjb25zdCBjYWxsc3RhY2tDb21tYW5kcyA9IHtcbiAgICAgIHJlZ2lzdHJ5OiBjb21tYW5kcyxcbiAgICAgIGNvbnRpbnVlOiBDb21tYW5kSURzLmRlYnVnQ29udGludWUsXG4gICAgICB0ZXJtaW5hdGU6IENvbW1hbmRJRHMudGVybWluYXRlLFxuICAgICAgbmV4dDogQ29tbWFuZElEcy5uZXh0LFxuICAgICAgc3RlcEluOiBDb21tYW5kSURzLnN0ZXBJbixcbiAgICAgIHN0ZXBPdXQ6IENvbW1hbmRJRHMuc3RlcE91dCxcbiAgICAgIGV2YWx1YXRlOiBDb21tYW5kSURzLmV2YWx1YXRlXG4gICAgfTtcblxuICAgIGNvbnN0IGJyZWFrcG9pbnRzQ29tbWFuZHMgPSB7XG4gICAgICByZWdpc3RyeTogY29tbWFuZHMsXG4gICAgICBwYXVzZTogQ29tbWFuZElEcy5wYXVzZVxuICAgIH07XG5cbiAgICBjb25zdCBzaWRlYmFyID0gbmV3IERlYnVnZ2VyLlNpZGViYXIoe1xuICAgICAgc2VydmljZSxcbiAgICAgIGNhbGxzdGFja0NvbW1hbmRzLFxuICAgICAgYnJlYWtwb2ludHNDb21tYW5kcyxcbiAgICAgIGVkaXRvclNlcnZpY2VzLFxuICAgICAgdGhlbWVNYW5hZ2VyLFxuICAgICAgdHJhbnNsYXRvclxuICAgIH0pO1xuXG4gICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgY29uc3Qgc2V0dGluZyA9IGF3YWl0IHNldHRpbmdSZWdpc3RyeS5sb2FkKG1haW4uaWQpO1xuICAgICAgY29uc3QgdXBkYXRlU2V0dGluZ3MgPSAoKTogdm9pZCA9PiB7XG4gICAgICAgIGNvbnN0IGZpbHRlcnMgPSBzZXR0aW5nLmdldCgndmFyaWFibGVGaWx0ZXJzJykuY29tcG9zaXRlIGFzIHtcbiAgICAgICAgICBba2V5OiBzdHJpbmddOiBzdHJpbmdbXTtcbiAgICAgICAgfTtcbiAgICAgICAgY29uc3Qga2VybmVsID0gc2VydmljZS5zZXNzaW9uPy5jb25uZWN0aW9uPy5rZXJuZWw/Lm5hbWUgPz8gJyc7XG4gICAgICAgIGlmIChrZXJuZWwgJiYgZmlsdGVyc1trZXJuZWxdKSB7XG4gICAgICAgICAgc2lkZWJhci52YXJpYWJsZXMuZmlsdGVyID0gbmV3IFNldDxzdHJpbmc+KGZpbHRlcnNba2VybmVsXSk7XG4gICAgICAgIH1cbiAgICAgICAgY29uc3Qga2VybmVsU291cmNlc0ZpbHRlciA9IHNldHRpbmcuZ2V0KCdkZWZhdWx0S2VybmVsU291cmNlc0ZpbHRlcicpXG4gICAgICAgICAgLmNvbXBvc2l0ZSBhcyBzdHJpbmc7XG4gICAgICAgIHNpZGViYXIua2VybmVsU291cmNlcy5maWx0ZXIgPSBrZXJuZWxTb3VyY2VzRmlsdGVyO1xuICAgICAgfTtcbiAgICAgIHVwZGF0ZVNldHRpbmdzKCk7XG4gICAgICBzZXR0aW5nLmNoYW5nZWQuY29ubmVjdCh1cGRhdGVTZXR0aW5ncyk7XG4gICAgICBzZXJ2aWNlLnNlc3Npb25DaGFuZ2VkLmNvbm5lY3QodXBkYXRlU2V0dGluZ3MpO1xuICAgIH1cblxuICAgIHJldHVybiBzaWRlYmFyO1xuICB9XG59O1xuXG4vKipcbiAqIFRoZSBtYWluIGRlYnVnZ2VyIFVJIHBsdWdpbi5cbiAqL1xuY29uc3QgbWFpbjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RlYnVnZ2VyLWV4dGVuc2lvbjptYWluJyxcbiAgcmVxdWlyZXM6IFtJRGVidWdnZXIsIElEZWJ1Z2dlclNpZGViYXIsIElFZGl0b3JTZXJ2aWNlcywgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW1xuICAgIElDb21tYW5kUGFsZXR0ZSxcbiAgICBJRGVidWdnZXJTb3VyY2VzLFxuICAgIElMYWJTaGVsbCxcbiAgICBJTGF5b3V0UmVzdG9yZXIsXG4gICAgSUxvZ2dlclJlZ2lzdHJ5XG4gIF0sXG4gIGF1dG9TdGFydDogZmFsc2UsXG4gIGFjdGl2YXRlOiBhc3luYyAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgc2VydmljZTogSURlYnVnZ2VyLFxuICAgIHNpZGViYXI6IElEZWJ1Z2dlci5JU2lkZWJhcixcbiAgICBlZGl0b3JTZXJ2aWNlczogSUVkaXRvclNlcnZpY2VzLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gICAgZGVidWdnZXJTb3VyY2VzOiBJRGVidWdnZXIuSVNvdXJjZXMgfCBudWxsLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwgfCBudWxsLFxuICAgIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICAgIGxvZ2dlclJlZ2lzdHJ5OiBJTG9nZ2VyUmVnaXN0cnkgfCBudWxsXG4gICk6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgeyBjb21tYW5kcywgc2hlbGwsIHNlcnZpY2VNYW5hZ2VyIH0gPSBhcHA7XG4gICAgY29uc3QgeyBrZXJuZWxzcGVjcyB9ID0gc2VydmljZU1hbmFnZXI7XG4gICAgY29uc3QgQ29tbWFuZElEcyA9IERlYnVnZ2VyLkNvbW1hbmRJRHM7XG5cbiAgICAvLyBGaXJzdCBjaGVjayBpZiB0aGVyZSBpcyBhIFBhZ2VDb25maWcgb3ZlcnJpZGUgZm9yIHRoZSBleHRlbnNpb24gdmlzaWJpbGl0eVxuICAgIGNvbnN0IGFsd2F5c1Nob3dEZWJ1Z2dlckV4dGVuc2lvbiA9XG4gICAgICBQYWdlQ29uZmlnLmdldE9wdGlvbignYWx3YXlzU2hvd0RlYnVnZ2VyRXh0ZW5zaW9uJykudG9Mb3dlckNhc2UoKSA9PT1cbiAgICAgICd0cnVlJztcbiAgICBpZiAoIWFsd2F5c1Nob3dEZWJ1Z2dlckV4dGVuc2lvbikge1xuICAgICAgLy8gaGlkZSB0aGUgZGVidWdnZXIgc2lkZWJhciBpZiBubyBrZXJuZWwgd2l0aCBzdXBwb3J0IGZvciBkZWJ1Z2dpbmcgaXMgYXZhaWxhYmxlXG4gICAgICBhd2FpdCBrZXJuZWxzcGVjcy5yZWFkeTtcbiAgICAgIGNvbnN0IHNwZWNzID0ga2VybmVsc3BlY3Muc3BlY3M/Lmtlcm5lbHNwZWNzO1xuICAgICAgaWYgKCFzcGVjcykge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCBlbmFibGVkID0gT2JqZWN0LmtleXMoc3BlY3MpLnNvbWUoXG4gICAgICAgIG5hbWUgPT4gISEoc3BlY3NbbmFtZV0/Lm1ldGFkYXRhPy5bJ2RlYnVnZ2VyJ10gPz8gZmFsc2UpXG4gICAgICApO1xuICAgICAgaWYgKCFlbmFibGVkKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAvLyBnZXQgdGhlIG1pbWUgdHlwZSBvZiB0aGUga2VybmVsIGxhbmd1YWdlIGZvciB0aGUgY3VycmVudCBkZWJ1ZyBzZXNzaW9uXG4gICAgY29uc3QgZ2V0TWltZVR5cGUgPSBhc3luYyAoKTogUHJvbWlzZTxzdHJpbmc+ID0+IHtcbiAgICAgIGNvbnN0IGtlcm5lbCA9IHNlcnZpY2Uuc2Vzc2lvbj8uY29ubmVjdGlvbj8ua2VybmVsO1xuICAgICAgaWYgKCFrZXJuZWwpIHtcbiAgICAgICAgcmV0dXJuICcnO1xuICAgICAgfVxuICAgICAgY29uc3QgaW5mbyA9IChhd2FpdCBrZXJuZWwuaW5mbykubGFuZ3VhZ2VfaW5mbztcbiAgICAgIGNvbnN0IG5hbWUgPSBpbmZvLm5hbWU7XG4gICAgICBjb25zdCBtaW1lVHlwZSA9XG4gICAgICAgIGVkaXRvclNlcnZpY2VzPy5taW1lVHlwZVNlcnZpY2UuZ2V0TWltZVR5cGVCeUxhbmd1YWdlKHsgbmFtZSB9KSA/PyAnJztcbiAgICAgIHJldHVybiBtaW1lVHlwZTtcbiAgICB9O1xuXG4gICAgY29uc3QgcmVuZGVybWltZSA9IG5ldyBSZW5kZXJNaW1lUmVnaXN0cnkoeyBpbml0aWFsRmFjdG9yaWVzIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmV2YWx1YXRlLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0V2YWx1YXRlIENvZGUnKSxcbiAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdFdmFsdWF0ZSBDb2RlJyksXG4gICAgICBpY29uOiBEZWJ1Z2dlci5JY29ucy5ldmFsdWF0ZUljb24sXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHNlcnZpY2UuaGFzU3RvcHBlZFRocmVhZHMoKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgY29uc3QgbWltZVR5cGUgPSBhd2FpdCBnZXRNaW1lVHlwZSgpO1xuICAgICAgICBjb25zdCByZXN1bHQgPSBhd2FpdCBEZWJ1Z2dlci5EaWFsb2dzLmdldENvZGUoe1xuICAgICAgICAgIHRpdGxlOiB0cmFucy5fXygnRXZhbHVhdGUgQ29kZScpLFxuICAgICAgICAgIG9rTGFiZWw6IHRyYW5zLl9fKCdFdmFsdWF0ZScpLFxuICAgICAgICAgIGNhbmNlbExhYmVsOiB0cmFucy5fXygnQ2FuY2VsJyksXG4gICAgICAgICAgbWltZVR5cGUsXG4gICAgICAgICAgcmVuZGVybWltZVxuICAgICAgICB9KTtcbiAgICAgICAgY29uc3QgY29kZSA9IHJlc3VsdC52YWx1ZTtcbiAgICAgICAgaWYgKCFyZXN1bHQuYnV0dG9uLmFjY2VwdCB8fCAhY29kZSkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCByZXBseSA9IGF3YWl0IHNlcnZpY2UuZXZhbHVhdGUoY29kZSk7XG4gICAgICAgIGlmIChyZXBseSkge1xuICAgICAgICAgIGNvbnN0IGRhdGEgPSByZXBseS5yZXN1bHQ7XG4gICAgICAgICAgY29uc3QgcGF0aCA9IHNlcnZpY2U/LnNlc3Npb24/LmNvbm5lY3Rpb24/LnBhdGg7XG4gICAgICAgICAgY29uc3QgbG9nZ2VyID0gcGF0aCA/IGxvZ2dlclJlZ2lzdHJ5Py5nZXRMb2dnZXI/LihwYXRoKSA6IHVuZGVmaW5lZDtcblxuICAgICAgICAgIGlmIChsb2dnZXIpIHtcbiAgICAgICAgICAgIC8vIHByaW50IHRvIGxvZyBjb25zb2xlIG9mIHRoZSBub3RlYm9vayBjdXJyZW50bHkgYmVpbmcgZGVidWdnZWRcbiAgICAgICAgICAgIGxvZ2dlci5sb2coeyB0eXBlOiAndGV4dCcsIGRhdGEsIGxldmVsOiBsb2dnZXIubGV2ZWwgfSk7XG4gICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgIC8vIGZhbGxiYWNrIHRvIHByaW50aW5nIHRvIGRldnRvb2xzIGNvbnNvbGVcbiAgICAgICAgICAgIGNvbnNvbGUuZGVidWcoZGF0YSk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuZGVidWdDb250aW51ZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdDb250aW51ZScpLFxuICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ0NvbnRpbnVlJyksXG4gICAgICBpY29uOiBEZWJ1Z2dlci5JY29ucy5jb250aW51ZUljb24sXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHNlcnZpY2UuaGFzU3RvcHBlZFRocmVhZHMoKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgYXdhaXQgc2VydmljZS5jb250aW51ZSgpO1xuICAgICAgICBjb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRlcm1pbmF0ZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdUZXJtaW5hdGUnKSxcbiAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdUZXJtaW5hdGUnKSxcbiAgICAgIGljb246IERlYnVnZ2VyLkljb25zLnRlcm1pbmF0ZUljb24sXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+IHNlcnZpY2UuaGFzU3RvcHBlZFRocmVhZHMoKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgYXdhaXQgc2VydmljZS5yZXN0YXJ0KCk7XG4gICAgICAgIGNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubmV4dCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdOZXh0JyksXG4gICAgICBjYXB0aW9uOiB0cmFucy5fXygnTmV4dCcpLFxuICAgICAgaWNvbjogRGVidWdnZXIuSWNvbnMuc3RlcE92ZXJJY29uLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBzZXJ2aWNlLmhhc1N0b3BwZWRUaHJlYWRzKCksXG4gICAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAgIGF3YWl0IHNlcnZpY2UubmV4dCgpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnN0ZXBJbiwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTdGVwIEluJyksXG4gICAgICBjYXB0aW9uOiB0cmFucy5fXygnU3RlcCBJbicpLFxuICAgICAgaWNvbjogRGVidWdnZXIuSWNvbnMuc3RlcEludG9JY29uLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PiBzZXJ2aWNlLmhhc1N0b3BwZWRUaHJlYWRzKCksXG4gICAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAgIGF3YWl0IHNlcnZpY2Uuc3RlcEluKCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc3RlcE91dCwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdTdGVwIE91dCcpLFxuICAgICAgY2FwdGlvbjogdHJhbnMuX18oJ1N0ZXAgT3V0JyksXG4gICAgICBpY29uOiBEZWJ1Z2dlci5JY29ucy5zdGVwT3V0SWNvbixcbiAgICAgIGlzRW5hYmxlZDogKCkgPT4gc2VydmljZS5oYXNTdG9wcGVkVGhyZWFkcygpLFxuICAgICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgICBhd2FpdCBzZXJ2aWNlLnN0ZXBPdXQoKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5wYXVzZSwge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdFbmFibGUgLyBEaXNhYmxlIHBhdXNpbmcgb24gZXhjZXB0aW9ucycpLFxuICAgICAgY2FwdGlvbjogKCkgPT5cbiAgICAgICAgc2VydmljZS5pc1N0YXJ0ZWRcbiAgICAgICAgICA/IHNlcnZpY2UucGF1c2VPbkV4Y2VwdGlvbnNJc1ZhbGlkKClcbiAgICAgICAgICAgID8gc2VydmljZS5pc1BhdXNpbmdPbkV4Y2VwdGlvbnNcbiAgICAgICAgICAgICAgPyB0cmFucy5fXygnRGlzYWJsZSBwYXVzaW5nIG9uIGV4Y2VwdGlvbnMnKVxuICAgICAgICAgICAgICA6IHRyYW5zLl9fKCdFbmFibGUgcGF1c2luZyBvbiBleGNlcHRpb25zJylcbiAgICAgICAgICAgIDogdHJhbnMuX18oJ0tlcm5lbCBkb2VzIG5vdCBzdXBwb3J0IHBhdXNpbmcgb24gZXhjZXB0aW9ucy4nKVxuICAgICAgICAgIDogdHJhbnMuX18oJ0VuYWJsZSAvIERpc2FibGUgcGF1c2luZyBvbiBleGNlcHRpb25zJyksXG4gICAgICBjbGFzc05hbWU6ICdqcC1QYXVzZU9uRXhjZXB0aW9ucycsXG4gICAgICBpY29uOiBEZWJ1Z2dlci5JY29ucy5wYXVzZU9uRXhjZXB0aW9uc0ljb24sXG4gICAgICBpc1RvZ2dsZWQ6ICgpID0+IHtcbiAgICAgICAgcmV0dXJuIHNlcnZpY2UuaXNQYXVzaW5nT25FeGNlcHRpb25zO1xuICAgICAgfSxcbiAgICAgIGlzRW5hYmxlZDogKCkgPT4gc2VydmljZS5wYXVzZU9uRXhjZXB0aW9uc0lzVmFsaWQoKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgYXdhaXQgc2VydmljZS5wYXVzZU9uRXhjZXB0aW9ucyghc2VydmljZS5pc1BhdXNpbmdPbkV4Y2VwdGlvbnMpO1xuICAgICAgICBjb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgc2VydmljZS5ldmVudE1lc3NhZ2UuY29ubmVjdCgoXywgZXZlbnQpOiB2b2lkID0+IHtcbiAgICAgIGNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKCk7XG4gICAgICBpZiAobGFiU2hlbGwgJiYgZXZlbnQuZXZlbnQgPT09ICdpbml0aWFsaXplZCcpIHtcbiAgICAgICAgbGFiU2hlbGwuYWN0aXZhdGVCeUlkKHNpZGViYXIuaWQpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgc2VydmljZS5zZXNzaW9uQ2hhbmdlZC5jb25uZWN0KF8gPT4ge1xuICAgICAgY29tbWFuZHMubm90aWZ5Q29tbWFuZENoYW5nZWQoKTtcbiAgICB9KTtcblxuICAgIGlmIChyZXN0b3Jlcikge1xuICAgICAgcmVzdG9yZXIuYWRkKHNpZGViYXIsICdkZWJ1Z2dlci1zaWRlYmFyJyk7XG4gICAgfVxuXG4gICAgc2lkZWJhci5ub2RlLnNldEF0dHJpYnV0ZSgncm9sZScsICdyZWdpb24nKTtcbiAgICBzaWRlYmFyLm5vZGUuc2V0QXR0cmlidXRlKCdhcmlhLWxhYmVsJywgdHJhbnMuX18oJ0RlYnVnZ2VyIHNlY3Rpb24nKSk7XG5cbiAgICBzaWRlYmFyLnRpdGxlLmNhcHRpb24gPSB0cmFucy5fXygnRGVidWdnZXInKTtcblxuICAgIHNoZWxsLmFkZChzaWRlYmFyLCAncmlnaHQnLCB7IHR5cGU6ICdEZWJ1Z2dlcicgfSk7XG5cbiAgICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuc2hvd1BhbmVsLCB7XG4gICAgICBsYWJlbDogdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJykuX18oJ0RlYnVnZ2VyIFBhbmVsJyksXG4gICAgICBleGVjdXRlOiAoKSA9PiB7XG4gICAgICAgIHNoZWxsLmFjdGl2YXRlQnlJZChzaWRlYmFyLmlkKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIGlmIChwYWxldHRlKSB7XG4gICAgICBjb25zdCBjYXRlZ29yeSA9IHRyYW5zLl9fKCdEZWJ1Z2dlcicpO1xuICAgICAgW1xuICAgICAgICBDb21tYW5kSURzLmRlYnVnQ29udGludWUsXG4gICAgICAgIENvbW1hbmRJRHMudGVybWluYXRlLFxuICAgICAgICBDb21tYW5kSURzLm5leHQsXG4gICAgICAgIENvbW1hbmRJRHMuc3RlcEluLFxuICAgICAgICBDb21tYW5kSURzLnN0ZXBPdXQsXG4gICAgICAgIENvbW1hbmRJRHMuZXZhbHVhdGUsXG4gICAgICAgIENvbW1hbmRJRHMucGF1c2VcbiAgICAgIF0uZm9yRWFjaChjb21tYW5kID0+IHtcbiAgICAgICAgcGFsZXR0ZS5hZGRJdGVtKHsgY29tbWFuZCwgY2F0ZWdvcnkgfSk7XG4gICAgICB9KTtcbiAgICB9XG5cbiAgICBpZiAoZGVidWdnZXJTb3VyY2VzKSB7XG4gICAgICBjb25zdCB7IG1vZGVsIH0gPSBzZXJ2aWNlO1xuICAgICAgY29uc3QgcmVhZE9ubHlFZGl0b3JGYWN0b3J5ID0gbmV3IERlYnVnZ2VyLlJlYWRPbmx5RWRpdG9yRmFjdG9yeSh7XG4gICAgICAgIGVkaXRvclNlcnZpY2VzXG4gICAgICB9KTtcblxuICAgICAgY29uc3Qgb25DdXJyZW50RnJhbWVDaGFuZ2VkID0gKFxuICAgICAgICBfOiBJRGVidWdnZXIuTW9kZWwuSUNhbGxzdGFjayxcbiAgICAgICAgZnJhbWU6IElEZWJ1Z2dlci5JU3RhY2tGcmFtZVxuICAgICAgKTogdm9pZCA9PiB7XG4gICAgICAgIGRlYnVnZ2VyU291cmNlc1xuICAgICAgICAgIC5maW5kKHtcbiAgICAgICAgICAgIGZvY3VzOiB0cnVlLFxuICAgICAgICAgICAga2VybmVsOiBzZXJ2aWNlLnNlc3Npb24/LmNvbm5lY3Rpb24/Lmtlcm5lbD8ubmFtZSA/PyAnJyxcbiAgICAgICAgICAgIHBhdGg6IHNlcnZpY2Uuc2Vzc2lvbj8uY29ubmVjdGlvbj8ucGF0aCA/PyAnJyxcbiAgICAgICAgICAgIHNvdXJjZTogZnJhbWU/LnNvdXJjZT8ucGF0aCA/PyAnJ1xuICAgICAgICAgIH0pXG4gICAgICAgICAgLmZvckVhY2goZWRpdG9yID0+IHtcbiAgICAgICAgICAgIHJlcXVlc3RBbmltYXRpb25GcmFtZSgoKSA9PiB7XG4gICAgICAgICAgICAgIERlYnVnZ2VyLkVkaXRvckhhbmRsZXIuc2hvd0N1cnJlbnRMaW5lKGVkaXRvciwgZnJhbWUubGluZSk7XG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICB9KTtcbiAgICAgIH07XG5cbiAgICAgIGNvbnN0IG9uU291cmNlT3BlbmVkID0gKFxuICAgICAgICBfOiBJRGVidWdnZXIuTW9kZWwuSVNvdXJjZXMgfCBudWxsLFxuICAgICAgICBzb3VyY2U6IElEZWJ1Z2dlci5Tb3VyY2UsXG4gICAgICAgIGJyZWFrcG9pbnQ/OiBJRGVidWdnZXIuSUJyZWFrcG9pbnRcbiAgICAgICk6IHZvaWQgPT4ge1xuICAgICAgICBpZiAoIXNvdXJjZSkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCB7IGNvbnRlbnQsIG1pbWVUeXBlLCBwYXRoIH0gPSBzb3VyY2U7XG4gICAgICAgIGNvbnN0IHJlc3VsdHMgPSBkZWJ1Z2dlclNvdXJjZXMuZmluZCh7XG4gICAgICAgICAgZm9jdXM6IHRydWUsXG4gICAgICAgICAga2VybmVsOiBzZXJ2aWNlLnNlc3Npb24/LmNvbm5lY3Rpb24/Lmtlcm5lbD8ubmFtZSA/PyAnJyxcbiAgICAgICAgICBwYXRoOiBzZXJ2aWNlLnNlc3Npb24/LmNvbm5lY3Rpb24/LnBhdGggPz8gJycsXG4gICAgICAgICAgc291cmNlOiBwYXRoXG4gICAgICAgIH0pO1xuICAgICAgICBpZiAocmVzdWx0cy5sZW5ndGggPiAwKSB7XG4gICAgICAgICAgaWYgKGJyZWFrcG9pbnQgJiYgdHlwZW9mIGJyZWFrcG9pbnQubGluZSAhPT0gJ3VuZGVmaW5lZCcpIHtcbiAgICAgICAgICAgIHJlc3VsdHMuZm9yRWFjaChlZGl0b3IgPT4ge1xuICAgICAgICAgICAgICBlZGl0b3IucmV2ZWFsUG9zaXRpb24oe1xuICAgICAgICAgICAgICAgIGxpbmU6IChicmVha3BvaW50LmxpbmUgYXMgbnVtYmVyKSAtIDEsXG4gICAgICAgICAgICAgICAgY29sdW1uOiBicmVha3BvaW50LmNvbHVtbiB8fCAwXG4gICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgfVxuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBlZGl0b3JXcmFwcGVyID0gcmVhZE9ubHlFZGl0b3JGYWN0b3J5LmNyZWF0ZU5ld0VkaXRvcih7XG4gICAgICAgICAgY29udGVudCxcbiAgICAgICAgICBtaW1lVHlwZSxcbiAgICAgICAgICBwYXRoXG4gICAgICAgIH0pO1xuICAgICAgICBjb25zdCBlZGl0b3IgPSBlZGl0b3JXcmFwcGVyLmVkaXRvcjtcbiAgICAgICAgY29uc3QgZWRpdG9ySGFuZGxlciA9IG5ldyBEZWJ1Z2dlci5FZGl0b3JIYW5kbGVyKHtcbiAgICAgICAgICBkZWJ1Z2dlclNlcnZpY2U6IHNlcnZpY2UsXG4gICAgICAgICAgZWRpdG9yLFxuICAgICAgICAgIHBhdGhcbiAgICAgICAgfSk7XG4gICAgICAgIGVkaXRvcldyYXBwZXIuZGlzcG9zZWQuY29ubmVjdCgoKSA9PiBlZGl0b3JIYW5kbGVyLmRpc3Bvc2UoKSk7XG5cbiAgICAgICAgZGVidWdnZXJTb3VyY2VzLm9wZW4oe1xuICAgICAgICAgIGxhYmVsOiBQYXRoRXh0LmJhc2VuYW1lKHBhdGgpLFxuICAgICAgICAgIGNhcHRpb246IHBhdGgsXG4gICAgICAgICAgZWRpdG9yV3JhcHBlclxuICAgICAgICB9KTtcblxuICAgICAgICBjb25zdCBmcmFtZSA9IHNlcnZpY2UubW9kZWwuY2FsbHN0YWNrLmZyYW1lO1xuICAgICAgICBpZiAoZnJhbWUpIHtcbiAgICAgICAgICBEZWJ1Z2dlci5FZGl0b3JIYW5kbGVyLnNob3dDdXJyZW50TGluZShlZGl0b3IsIGZyYW1lLmxpbmUpO1xuICAgICAgICB9XG4gICAgICB9O1xuXG4gICAgICBjb25zdCBvbktlcm5lbFNvdXJjZU9wZW5lZCA9IChcbiAgICAgICAgXzogSURlYnVnZ2VyLk1vZGVsLklLZXJuZWxTb3VyY2VzIHwgbnVsbCxcbiAgICAgICAgc291cmNlOiBJRGVidWdnZXIuU291cmNlLFxuICAgICAgICBicmVha3BvaW50PzogSURlYnVnZ2VyLklCcmVha3BvaW50XG4gICAgICApOiB2b2lkID0+IHtcbiAgICAgICAgaWYgKCFzb3VyY2UpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgb25Tb3VyY2VPcGVuZWQobnVsbCwgc291cmNlLCBicmVha3BvaW50KTtcbiAgICAgIH07XG5cbiAgICAgIG1vZGVsLmNhbGxzdGFjay5jdXJyZW50RnJhbWVDaGFuZ2VkLmNvbm5lY3Qob25DdXJyZW50RnJhbWVDaGFuZ2VkKTtcbiAgICAgIG1vZGVsLnNvdXJjZXMuY3VycmVudFNvdXJjZU9wZW5lZC5jb25uZWN0KG9uU291cmNlT3BlbmVkKTtcbiAgICAgIG1vZGVsLmtlcm5lbFNvdXJjZXMua2VybmVsU291cmNlT3BlbmVkLmNvbm5lY3Qob25LZXJuZWxTb3VyY2VPcGVuZWQpO1xuICAgICAgbW9kZWwuYnJlYWtwb2ludHMuY2xpY2tlZC5jb25uZWN0KGFzeW5jIChfLCBicmVha3BvaW50KSA9PiB7XG4gICAgICAgIGNvbnN0IHBhdGggPSBicmVha3BvaW50LnNvdXJjZT8ucGF0aDtcbiAgICAgICAgY29uc3Qgc291cmNlID0gYXdhaXQgc2VydmljZS5nZXRTb3VyY2Uoe1xuICAgICAgICAgIHNvdXJjZVJlZmVyZW5jZTogMCxcbiAgICAgICAgICBwYXRoXG4gICAgICAgIH0pO1xuICAgICAgICBvblNvdXJjZU9wZW5lZChudWxsLCBzb3VyY2UsIGJyZWFrcG9pbnQpO1xuICAgICAgfSk7XG4gICAgfVxuICB9XG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2lucyBhcyBkZWZhdWx0LlxuICovXG5jb25zdCBwbHVnaW5zOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48YW55PltdID0gW1xuICBzZXJ2aWNlLFxuICBjb25zb2xlcyxcbiAgZmlsZXMsXG4gIG5vdGVib29rcyxcbiAgdmFyaWFibGVzLFxuICBzaWRlYmFyLFxuICBtYWluLFxuICBzb3VyY2VzLFxuICBjb25maWd1cmF0aW9uXG5dO1xuXG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9