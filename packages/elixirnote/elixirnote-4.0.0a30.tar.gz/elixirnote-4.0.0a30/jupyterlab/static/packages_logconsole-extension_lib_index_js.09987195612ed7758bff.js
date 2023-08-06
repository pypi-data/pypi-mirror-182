"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_logconsole-extension_lib_index_js"],{

/***/ "../../packages/logconsole-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/logconsole-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LogLevelSwitcher": () => (/* binding */ LogLevelSwitcher),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/logconsole */ "webpack/sharing/consume/default/@jupyterlab/logconsole/@jupyterlab/logconsole");
/* harmony import */ var _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_9___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _status__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./status */ "../../packages/logconsole-extension/lib/status.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module logconsole-extension
 */












const LOG_CONSOLE_PLUGIN_ID = '@jupyterlab/logconsole-extension:plugin';
/**
 * The command IDs used by the plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.addCheckpoint = 'logconsole:add-checkpoint';
    CommandIDs.clear = 'logconsole:clear';
    CommandIDs.open = 'logconsole:open';
    CommandIDs.setLevel = 'logconsole:set-level';
})(CommandIDs || (CommandIDs = {}));
/**
 * The Log Console extension.
 */
const logConsolePlugin = {
    activate: activateLogConsole,
    id: LOG_CONSOLE_PLUGIN_ID,
    provides: _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2__.ILoggerRegistry,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.IRenderMimeRegistry, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__.INotebookTracker, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry, _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_6__.IStatusBar],
    autoStart: true
};
/**
 * Activate the Log Console extension.
 */
function activateLogConsole(app, labShell, rendermime, nbtracker, translator, palette, restorer, settingRegistry, statusBar) {
    const trans = translator.load('jupyterlab');
    let logConsoleWidget = null;
    let logConsolePanel = null;
    const loggerRegistry = new _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2__.LoggerRegistry({
        defaultRendermime: rendermime,
        // The maxLength is reset below from settings
        maxLength: 1000
    });
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'logconsole'
    });
    if (restorer) {
        void restorer.restore(tracker, {
            command: CommandIDs.open,
            name: () => 'logconsole'
        });
    }
    const status = new _status__WEBPACK_IMPORTED_MODULE_11__.LogConsoleStatus({
        loggerRegistry: loggerRegistry,
        handleClick: () => {
            var _a;
            if (!logConsoleWidget) {
                createLogConsoleWidget({
                    insertMode: 'split-bottom',
                    ref: (_a = app.shell.currentWidget) === null || _a === void 0 ? void 0 : _a.id
                });
            }
            else {
                app.shell.activateById(logConsoleWidget.id);
            }
        },
        translator
    });
    const createLogConsoleWidget = (options = {}) => {
        logConsolePanel = new _jupyterlab_logconsole__WEBPACK_IMPORTED_MODULE_2__.LogConsolePanel(loggerRegistry, translator);
        logConsolePanel.source =
            options.source !== undefined
                ? options.source
                : nbtracker.currentWidget
                    ? nbtracker.currentWidget.context.path
                    : null;
        logConsoleWidget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget({ content: logConsolePanel });
        logConsoleWidget.addClass('jp-LogConsole');
        logConsoleWidget.title.closable = true;
        logConsoleWidget.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.listIcon;
        logConsoleWidget.title.label = trans.__('Log Console');
        const addCheckpointButton = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.CommandToolbarButton({
            commands: app.commands,
            id: CommandIDs.addCheckpoint
        });
        const clearButton = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.CommandToolbarButton({
            commands: app.commands,
            id: CommandIDs.clear
        });
        logConsoleWidget.toolbar.addItem('lab-log-console-add-checkpoint', addCheckpointButton);
        logConsoleWidget.toolbar.addItem('lab-log-console-clear', clearButton);
        logConsoleWidget.toolbar.addItem('level', new LogLevelSwitcher(logConsoleWidget.content, translator));
        logConsolePanel.sourceChanged.connect(() => {
            app.commands.notifyCommandChanged();
        });
        logConsolePanel.sourceDisplayed.connect((panel, { source, version }) => {
            status.model.sourceDisplayed(source, version);
        });
        logConsoleWidget.disposed.connect(() => {
            logConsoleWidget = null;
            logConsolePanel = null;
            app.commands.notifyCommandChanged();
        });
        app.shell.add(logConsoleWidget, 'down', {
            ref: options.ref,
            mode: options.insertMode,
            type: 'Log Console'
        });
        void tracker.add(logConsoleWidget);
        app.shell.activateById(logConsoleWidget.id);
        logConsoleWidget.update();
        app.commands.notifyCommandChanged();
    };
    app.commands.addCommand(CommandIDs.open, {
        label: trans.__('Show Log Console'),
        execute: (options = {}) => {
            // Toggle the display
            if (logConsoleWidget) {
                logConsoleWidget.dispose();
            }
            else {
                createLogConsoleWidget(options);
            }
        },
        isToggled: () => {
            return logConsoleWidget !== null;
        }
    });
    app.commands.addCommand(CommandIDs.addCheckpoint, {
        execute: () => {
            var _a;
            (_a = logConsolePanel === null || logConsolePanel === void 0 ? void 0 : logConsolePanel.logger) === null || _a === void 0 ? void 0 : _a.checkpoint();
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.addIcon,
        isEnabled: () => !!logConsolePanel && logConsolePanel.source !== null,
        label: trans.__('Add Checkpoint')
    });
    app.commands.addCommand(CommandIDs.clear, {
        execute: () => {
            var _a;
            (_a = logConsolePanel === null || logConsolePanel === void 0 ? void 0 : logConsolePanel.logger) === null || _a === void 0 ? void 0 : _a.clear();
        },
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.clearIcon,
        isEnabled: () => !!logConsolePanel && logConsolePanel.source !== null,
        label: trans.__('Clear Log')
    });
    function toTitleCase(value) {
        return value.length === 0 ? value : value[0].toUpperCase() + value.slice(1);
    }
    app.commands.addCommand(CommandIDs.setLevel, {
        // TODO: find good icon class
        execute: (args) => {
            if (logConsolePanel === null || logConsolePanel === void 0 ? void 0 : logConsolePanel.logger) {
                logConsolePanel.logger.level = args.level;
            }
        },
        isEnabled: () => !!logConsolePanel && logConsolePanel.source !== null,
        label: args => args['level']
            ? trans.__('Set Log Level to %1', toTitleCase(args.level))
            : trans.__('Set log level to `level`.')
    });
    if (palette) {
        palette.addItem({
            command: CommandIDs.open,
            category: trans.__('Main Area')
        });
    }
    if (statusBar) {
        statusBar.registerStatusItem('@jupyterlab/logconsole-extension:status', {
            item: status,
            align: 'left',
            isActive: () => { var _a; return ((_a = status.model) === null || _a === void 0 ? void 0 : _a.version) > 0; },
            activeStateChanged: status.model.stateChanged
        });
    }
    function setSource(newValue) {
        if (logConsoleWidget && newValue === logConsoleWidget) {
            // Do not change anything if we are just focusing on ourselves
            return;
        }
        let source;
        if (newValue && nbtracker.has(newValue)) {
            source = newValue.context.path;
        }
        else {
            source = null;
        }
        if (logConsolePanel) {
            logConsolePanel.source = source;
        }
        status.model.source = source;
    }
    void app.restored.then(() => {
        // Set source only after app is restored in order to allow restorer to
        // restore previous source first, which may set the renderer
        setSource(labShell.currentWidget);
        labShell.currentChanged.connect((_, { newValue }) => setSource(newValue));
    });
    if (settingRegistry) {
        const updateSettings = (settings) => {
            loggerRegistry.maxLength = settings.get('maxLogEntries')
                .composite;
            status.model.flashEnabled = settings.get('flash').composite;
        };
        Promise.all([settingRegistry.load(LOG_CONSOLE_PLUGIN_ID), app.restored])
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
    return loggerRegistry;
}
/**
 * A toolbar widget that switches log levels.
 */
class LogLevelSwitcher extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.ReactWidget {
    /**
     * Construct a new cell type switcher.
     */
    constructor(widget, translator) {
        super();
        /**
         * Handle `change` events for the HTMLSelect component.
         */
        this.handleChange = (event) => {
            if (this._logConsole.logger) {
                this._logConsole.logger.level = event.target.value;
            }
            this.update();
        };
        /**
         * Handle `keydown` events for the HTMLSelect component.
         */
        this.handleKeyDown = (event) => {
            if (event.keyCode === 13) {
                this._logConsole.activate();
            }
        };
        this._id = `level-${_lumino_coreutils__WEBPACK_IMPORTED_MODULE_9__.UUID.uuid4()}`;
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.addClass('jp-LogConsole-toolbarLogLevel');
        this._logConsole = widget;
        if (widget.source) {
            this.update();
        }
        widget.sourceChanged.connect(this._updateSource, this);
    }
    _updateSource(sender, { oldValue, newValue }) {
        // Transfer stateChanged handler to new source logger
        if (oldValue !== null) {
            const logger = sender.loggerRegistry.getLogger(oldValue);
            logger.stateChanged.disconnect(this.update, this);
        }
        if (newValue !== null) {
            const logger = sender.loggerRegistry.getLogger(newValue);
            logger.stateChanged.connect(this.update, this);
        }
        this.update();
    }
    render() {
        const logger = this._logConsole.logger;
        return (react__WEBPACK_IMPORTED_MODULE_10__.createElement(react__WEBPACK_IMPORTED_MODULE_10__.Fragment, null,
            react__WEBPACK_IMPORTED_MODULE_10__.createElement("label", { htmlFor: this._id, className: logger === null
                    ? 'jp-LogConsole-toolbarLogLevel-disabled'
                    : undefined }, this._trans.__('Log Level:')),
            react__WEBPACK_IMPORTED_MODULE_10__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_8__.HTMLSelect, { id: this._id, className: "jp-LogConsole-toolbarLogLevelDropdown", onChange: this.handleChange, onKeyDown: this.handleKeyDown, value: logger === null || logger === void 0 ? void 0 : logger.level, "aria-label": this._trans.__('Log level'), disabled: logger === null, options: logger === null
                    ? []
                    : [
                        [this._trans.__('Critical'), 'Critical'],
                        [this._trans.__('Error'), 'Error'],
                        [this._trans.__('Warning'), 'Warning'],
                        [this._trans.__('Info'), 'Info'],
                        [this._trans.__('Debug'), 'Debug']
                    ].map(data => ({
                        label: data[0],
                        value: data[1].toLowerCase()
                    })) })));
    }
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (logConsolePlugin);


/***/ }),

/***/ "../../packages/logconsole-extension/lib/status.js":
/*!*********************************************************!*\
  !*** ../../packages/logconsole-extension/lib/status.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LogConsoleStatus": () => (/* binding */ LogConsoleStatus)
/* harmony export */ });
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * A pure functional component for a Log Console status item.
 *
 * @param props - the props for the component.
 *
 * @returns a tsx component for rendering the Log Console status.
 */
function LogConsoleStatusComponent(props) {
    const translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
    const trans = translator.load('jupyterlab');
    let title = '';
    if (props.newMessages > 0) {
        title = trans.__('%1 new messages, %2 log entries for %3', props.newMessages, props.logEntries, props.source);
    }
    else {
        title += trans.__('%1 log entries for %2', props.logEntries, props.source);
    }
    return (react__WEBPACK_IMPORTED_MODULE_4___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.GroupItem, { spacing: 0, onClick: props.handleClick, title: title },
        react__WEBPACK_IMPORTED_MODULE_4___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.listIcon.react, { top: '2px', stylesheet: 'statusBar' }),
        props.newMessages > 0 ? react__WEBPACK_IMPORTED_MODULE_4___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.TextItem, { source: props.newMessages }) : react__WEBPACK_IMPORTED_MODULE_4___default().createElement((react__WEBPACK_IMPORTED_MODULE_4___default().Fragment), null)));
}
/**
 * A VDomRenderer widget for displaying the status of Log Console logs.
 */
class LogConsoleStatus extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Construct the log console status widget.
     *
     * @param options - The status widget initialization options.
     */
    constructor(options) {
        super(new LogConsoleStatus.Model(options.loggerRegistry));
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this._handleClick = options.handleClick;
        this.addClass(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.interactiveItem);
        this.addClass('jp-LogConsoleStatusItem');
    }
    /**
     * Render the log console status item.
     */
    render() {
        if (this.model === null || this.model.version === 0) {
            return null;
        }
        const { flashEnabled, messages, source, version, versionDisplayed, versionNotified } = this.model;
        if (source !== null && flashEnabled && version > versionNotified) {
            this._flashHighlight();
            this.model.sourceNotified(source, version);
        }
        else if (source !== null && flashEnabled && version > versionDisplayed) {
            this._showHighlighted();
        }
        else {
            this._clearHighlight();
        }
        return (react__WEBPACK_IMPORTED_MODULE_4___default().createElement(LogConsoleStatusComponent, { handleClick: this._handleClick, logEntries: messages, newMessages: version - versionDisplayed, source: this.model.source, translator: this.translator }));
    }
    _flashHighlight() {
        this._showHighlighted();
        // To make sure the browser triggers the animation, we remove the class,
        // wait for an animation frame, then add it back
        this.removeClass('jp-LogConsole-flash');
        requestAnimationFrame(() => {
            this.addClass('jp-LogConsole-flash');
        });
    }
    _showHighlighted() {
        this.addClass('jp-mod-selected');
    }
    _clearHighlight() {
        this.removeClass('jp-LogConsole-flash');
        this.removeClass('jp-mod-selected');
    }
}
/**
 * A namespace for Log Console log status.
 */
(function (LogConsoleStatus) {
    /**
     * A VDomModel for the LogConsoleStatus item.
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
        /**
         * Create a new LogConsoleStatus model.
         *
         * @param loggerRegistry - The logger registry providing the logs.
         */
        constructor(loggerRegistry) {
            super();
            /**
             * A signal emitted when the flash enablement changes.
             */
            this.flashEnabledChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
            this._flashEnabled = true;
            this._source = null;
            /**
             * The view status of each source.
             *
             * #### Notes
             * Keys are source names, value is a list of two numbers. The first
             * represents the version of the messages that was last displayed to the
             * user, the second represents the version that we last notified the user
             * about.
             */
            this._sourceVersion = new Map();
            this._loggerRegistry = loggerRegistry;
            this._loggerRegistry.registryChanged.connect(this._handleLogRegistryChange, this);
            this._handleLogRegistryChange();
        }
        /**
         * Number of messages currently in the current source.
         */
        get messages() {
            if (this._source === null) {
                return 0;
            }
            const logger = this._loggerRegistry.getLogger(this._source);
            return logger.length;
        }
        /**
         * The number of messages ever stored by the current source.
         */
        get version() {
            if (this._source === null) {
                return 0;
            }
            const logger = this._loggerRegistry.getLogger(this._source);
            return logger.version;
        }
        /**
         * The name of the active log source
         */
        get source() {
            return this._source;
        }
        set source(name) {
            if (this._source === name) {
                return;
            }
            this._source = name;
            // refresh rendering
            this.stateChanged.emit();
        }
        /**
         * The last source version that was displayed.
         */
        get versionDisplayed() {
            var _a, _b;
            if (this._source === null) {
                return 0;
            }
            return (_b = (_a = this._sourceVersion.get(this._source)) === null || _a === void 0 ? void 0 : _a.lastDisplayed) !== null && _b !== void 0 ? _b : 0;
        }
        /**
         * The last source version we notified the user about.
         */
        get versionNotified() {
            var _a, _b;
            if (this._source === null) {
                return 0;
            }
            return (_b = (_a = this._sourceVersion.get(this._source)) === null || _a === void 0 ? void 0 : _a.lastNotified) !== null && _b !== void 0 ? _b : 0;
        }
        /**
         * Flag to toggle flashing when new logs added.
         */
        get flashEnabled() {
            return this._flashEnabled;
        }
        set flashEnabled(enabled) {
            if (this._flashEnabled === enabled) {
                return;
            }
            this._flashEnabled = enabled;
            this.flashEnabledChanged.emit();
            // refresh rendering
            this.stateChanged.emit();
        }
        /**
         * Record the last source version displayed to the user.
         *
         * @param source - The name of the log source.
         * @param version - The version of the log that was displayed.
         *
         * #### Notes
         * This will also update the last notified version so that the last
         * notified version is always at least the last displayed version.
         */
        sourceDisplayed(source, version) {
            if (source === null || version === null) {
                return;
            }
            const versions = this._sourceVersion.get(source);
            let change = false;
            if (versions.lastDisplayed < version) {
                versions.lastDisplayed = version;
                change = true;
            }
            if (versions.lastNotified < version) {
                versions.lastNotified = version;
                change = true;
            }
            if (change && source === this._source) {
                this.stateChanged.emit();
            }
        }
        /**
         * Record a source version we notified the user about.
         *
         * @param source - The name of the log source.
         * @param version - The version of the log.
         */
        sourceNotified(source, version) {
            if (source === null) {
                return;
            }
            const versions = this._sourceVersion.get(source);
            if (versions.lastNotified < version) {
                versions.lastNotified = version;
                if (source === this._source) {
                    this.stateChanged.emit();
                }
            }
        }
        _handleLogRegistryChange() {
            const loggers = this._loggerRegistry.getLoggers();
            for (const logger of loggers) {
                if (!this._sourceVersion.has(logger.source)) {
                    logger.contentChanged.connect(this._handleLogContentChange, this);
                    this._sourceVersion.set(logger.source, {
                        lastDisplayed: 0,
                        lastNotified: 0
                    });
                }
            }
        }
        _handleLogContentChange({ source }, change) {
            if (source === this._source) {
                this.stateChanged.emit();
            }
        }
    }
    LogConsoleStatus.Model = Model;
})(LogConsoleStatus || (LogConsoleStatus = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbG9nY29uc29sZS1leHRlbnNpb25fbGliX2luZGV4X2pzLjA5OTg3MTk1NjEyZWQ3NzU4YmZmLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQU84QjtBQUtIO0FBT0U7QUFDdUM7QUFDVjtBQUNFO0FBQ1o7QUFLbEI7QUFRRTtBQUNNO0FBRVY7QUFDYTtBQUU1QyxNQUFNLHFCQUFxQixHQUFHLHlDQUF5QyxDQUFDO0FBRXhFOztHQUVHO0FBQ0gsSUFBVSxVQUFVLENBS25CO0FBTEQsV0FBVSxVQUFVO0lBQ0wsd0JBQWEsR0FBRywyQkFBMkIsQ0FBQztJQUM1QyxnQkFBSyxHQUFHLGtCQUFrQixDQUFDO0lBQzNCLGVBQUksR0FBRyxpQkFBaUIsQ0FBQztJQUN6QixtQkFBUSxHQUFHLHNCQUFzQixDQUFDO0FBQ2pELENBQUMsRUFMUyxVQUFVLEtBQVYsVUFBVSxRQUtuQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxnQkFBZ0IsR0FBMkM7SUFDL0QsUUFBUSxFQUFFLGtCQUFrQjtJQUM1QixFQUFFLEVBQUUscUJBQXFCO0lBQ3pCLFFBQVEsRUFBRSxtRUFBZTtJQUN6QixRQUFRLEVBQUUsQ0FBQyw4REFBUyxFQUFFLHVFQUFtQixFQUFFLGtFQUFnQixFQUFFLGdFQUFXLENBQUM7SUFDekUsUUFBUSxFQUFFLENBQUMsaUVBQWUsRUFBRSxvRUFBZSxFQUFFLHlFQUFnQixFQUFFLDZEQUFVLENBQUM7SUFDMUUsU0FBUyxFQUFFLElBQUk7Q0FDaEIsQ0FBQztBQUVGOztHQUVHO0FBQ0gsU0FBUyxrQkFBa0IsQ0FDekIsR0FBb0IsRUFDcEIsUUFBbUIsRUFDbkIsVUFBK0IsRUFDL0IsU0FBMkIsRUFDM0IsVUFBdUIsRUFDdkIsT0FBK0IsRUFDL0IsUUFBZ0MsRUFDaEMsZUFBd0MsRUFDeEMsU0FBNEI7SUFFNUIsTUFBTSxLQUFLLEdBQUcsVUFB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QixJQUFJLENBQUMsSUFBSSxDQUFDLGNBQWMsQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQyxFQUFFO29CQUMzQyxNQUFNLENBQUMsY0FBYyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsdUJBQXVCLEVBQUUsSUFBSSxDQUFDLENBQUM7b0JBQ2xFLElBQUksQ0FBQyxjQUFjLENBQUMsR0FBRyxDQUFDLE1BQU0sQ0FBQyxNQUFNLEVBQUU7d0JBQ3JDLGFBQWEsRUFBRSxDQUFDO3dCQUNoQixZQUFZLEVBQUUsQ0FBQztxQkFDaEIsQ0FBQyxDQUFDO2lCQUNKO2FBQ0Y7UUFDSCxDQUFDO1FBRU8sdUJBQXVCLENBQzdCLEVBQUUsTUFBTSxFQUFXLEVBQ25CLE1BQXNCO1lBRXRCLElBQUksTUFBTSxLQUFLLElBQUksQ0FBQyxPQUFPLEVBQUU7Z0JBQzNCLElBQUksQ0FBQyxZQUFZLENBQUMsSUFBSSxFQUFFLENBQUM7YUFDMUI7UUFDSCxDQUFDO0tBbUJGO0lBdkxZLHNCQUFLLFFBdUxqQjtBQTJCSCxDQUFDLEVBdE5nQixnQkFBZ0IsS0FBaEIsZ0JBQWdCLFFBc05oQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9sb2djb25zb2xlLWV4dGVuc2lvbi9zcmMvaW5kZXgudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9sb2djb25zb2xlLWV4dGVuc2lvbi9zcmMvc3RhdHVzLnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBsb2djb25zb2xlLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYWJTaGVsbCxcbiAgSUxheW91dFJlc3RvcmVyLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBJQ29tbWFuZFBhbGV0dGUsXG4gIE1haW5BcmVhV2lkZ2V0LFxuICBXaWRnZXRUcmFja2VyXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElDaGFuZ2VkQXJncyB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQge1xuICBJTG9nZ2VyUmVnaXN0cnksXG4gIExvZ0NvbnNvbGVQYW5lbCxcbiAgTG9nZ2VyUmVnaXN0cnksXG4gIExvZ0xldmVsXG59IGZyb20gJ0BqdXB5dGVybGFiL2xvZ2NvbnNvbGUnO1xuaW1wb3J0IHsgSU5vdGVib29rVHJhY2tlciwgTm90ZWJvb2tQYW5lbCB9IGZyb20gJ0BqdXB5dGVybGFiL25vdGVib29rJztcbmltcG9ydCB7IElSZW5kZXJNaW1lUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVN0YXR1c0JhciB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXR1c2Jhcic7XG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7XG4gIGFkZEljb24sXG4gIGNsZWFySWNvbixcbiAgQ29tbWFuZFRvb2xiYXJCdXR0b24sXG4gIEhUTUxTZWxlY3QsXG4gIGxpc3RJY29uLFxuICBSZWFjdFdpZGdldFxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFVVSUQgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBEb2NrTGF5b3V0LCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgTG9nQ29uc29sZVN0YXR1cyB9IGZyb20gJy4vc3RhdHVzJztcblxuY29uc3QgTE9HX0NPTlNPTEVfUExVR0lOX0lEID0gJ0BqdXB5dGVybGFiL2xvZ2NvbnNvbGUtZXh0ZW5zaW9uOnBsdWdpbic7XG5cbi8qKlxuICogVGhlIGNvbW1hbmQgSURzIHVzZWQgYnkgdGhlIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgYWRkQ2hlY2twb2ludCA9ICdsb2djb25zb2xlOmFkZC1jaGVja3BvaW50JztcbiAgZXhwb3J0IGNvbnN0IGNsZWFyID0gJ2xvZ2NvbnNvbGU6Y2xlYXInO1xuICBleHBvcnQgY29uc3Qgb3BlbiA9ICdsb2djb25zb2xlOm9wZW4nO1xuICBleHBvcnQgY29uc3Qgc2V0TGV2ZWwgPSAnbG9nY29uc29sZTpzZXQtbGV2ZWwnO1xufVxuXG4vKipcbiAqIFRoZSBMb2cgQ29uc29sZSBleHRlbnNpb24uXG4gKi9cbmNvbnN0IGxvZ0NvbnNvbGVQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJTG9nZ2VyUmVnaXN0cnk+ID0ge1xuICBhY3RpdmF0ZTogYWN0aXZhdGVMb2dDb25zb2xlLFxuICBpZDogTE9HX0NPTlNPTEVfUExVR0lOX0lELFxuICBwcm92aWRlczogSUxvZ2dlclJlZ2lzdHJ5LFxuICByZXF1aXJlczogW0lMYWJTaGVsbCwgSVJlbmRlck1pbWVSZWdpc3RyeSwgSU5vdGVib29rVHJhY2tlciwgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lDb21tYW5kUGFsZXR0ZSwgSUxheW91dFJlc3RvcmVyLCBJU2V0dGluZ1JlZ2lzdHJ5LCBJU3RhdHVzQmFyXSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEFjdGl2YXRlIHRoZSBMb2cgQ29uc29sZSBleHRlbnNpb24uXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlTG9nQ29uc29sZShcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIGxhYlNoZWxsOiBJTGFiU2hlbGwsXG4gIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnksXG4gIG5idHJhY2tlcjogSU5vdGVib29rVHJhY2tlcixcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSB8IG51bGwsXG4gIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsLFxuICBzdGF0dXNCYXI6IElTdGF0dXNCYXIgfCBudWxsXG4pOiBJTG9nZ2VyUmVnaXN0cnkge1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBsZXQgbG9nQ29uc29sZVdpZGdldDogTWFpbkFyZWFXaWRnZXQ8TG9nQ29uc29sZVBhbmVsPiB8IG51bGwgPSBudWxsO1xuICBsZXQgbG9nQ29uc29sZVBhbmVsOiBMb2dDb25zb2xlUGFuZWwgfCBudWxsID0gbnVsbDtcblxuICBjb25zdCBsb2dnZXJSZWdpc3RyeSA9IG5ldyBMb2dnZXJSZWdpc3RyeSh7XG4gICAgZGVmYXVsdFJlbmRlcm1pbWU6IHJlbmRlcm1pbWUsXG4gICAgLy8gVGhlIG1heExlbmd0aCBpcyByZXNldCBiZWxvdyBmcm9tIHNldHRpbmdzXG4gICAgbWF4TGVuZ3RoOiAxMDAwXG4gIH0pO1xuXG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxNYWluQXJlYVdpZGdldDxMb2dDb25zb2xlUGFuZWw+Pih7XG4gICAgbmFtZXNwYWNlOiAnbG9nY29uc29sZSdcbiAgfSk7XG5cbiAgaWYgKHJlc3RvcmVyKSB7XG4gICAgdm9pZCByZXN0b3Jlci5yZXN0b3JlKHRyYWNrZXIsIHtcbiAgICAgIGNvbW1hbmQ6IENvbW1hbmRJRHMub3BlbixcbiAgICAgIG5hbWU6ICgpID0+ICdsb2djb25zb2xlJ1xuICAgIH0pO1xuICB9XG5cbiAgY29uc3Qgc3RhdHVzID0gbmV3IExvZ0NvbnNvbGVTdGF0dXMoe1xuICAgIGxvZ2dlclJlZ2lzdHJ5OiBsb2dnZXJSZWdpc3RyeSxcbiAgICBoYW5kbGVDbGljazogKCkgPT4ge1xuICAgICAgaWYgKCFsb2dDb25zb2xlV2lkZ2V0KSB7XG4gICAgICAgIGNyZWF0ZUxvZ0NvbnNvbGVXaWRnZXQoe1xuICAgICAgICAgIGluc2VydE1vZGU6ICdzcGxpdC1ib3R0b20nLFxuICAgICAgICAgIHJlZjogYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXQ/LmlkXG4gICAgICAgIH0pO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgYXBwLnNoZWxsLmFjdGl2YXRlQnlJZChsb2dDb25zb2xlV2lkZ2V0LmlkKTtcbiAgICAgIH1cbiAgICB9LFxuICAgIHRyYW5zbGF0b3JcbiAgfSk7XG5cbiAgaW50ZXJmYWNlIElMb2dDb25zb2xlT3B0aW9ucyB7XG4gICAgc291cmNlPzogc3RyaW5nO1xuICAgIGluc2VydE1vZGU/OiBEb2NrTGF5b3V0Lkluc2VydE1vZGU7XG4gICAgcmVmPzogc3RyaW5nO1xuICB9XG5cbiAgY29uc3QgY3JlYXRlTG9nQ29uc29sZVdpZGdldCA9IChvcHRpb25zOiBJTG9nQ29uc29sZU9wdGlvbnMgPSB7fSkgPT4ge1xuICAgIGxvZ0NvbnNvbGVQYW5lbCA9IG5ldyBMb2dDb25zb2xlUGFuZWwobG9nZ2VyUmVnaXN0cnksIHRyYW5zbGF0b3IpO1xuXG4gICAgbG9nQ29uc29sZVBhbmVsLnNvdXJjZSA9XG4gICAgICBvcHRpb25zLnNvdXJjZSAhPT0gdW5kZWZpbmVkXG4gICAgICAgID8gb3B0aW9ucy5zb3VyY2VcbiAgICAgICAgOiBuYnRyYWNrZXIuY3VycmVudFdpZGdldFxuICAgICAgICA/IG5idHJhY2tlci5jdXJyZW50V2lkZ2V0LmNvbnRleHQucGF0aFxuICAgICAgICA6IG51bGw7XG5cbiAgICBsb2dDb25zb2xlV2lkZ2V0ID0gbmV3IE1haW5BcmVhV2lkZ2V0KHsgY29udGVudDogbG9nQ29uc29sZVBhbmVsIH0pO1xuICAgIGxvZ0NvbnNvbGVXaWRnZXQuYWRkQ2xhc3MoJ2pwLUxvZ0NvbnNvbGUnKTtcbiAgICBsb2dDb25zb2xlV2lkZ2V0LnRpdGxlLmNsb3NhYmxlID0gdHJ1ZTtcbiAgICBsb2dDb25zb2xlV2lkZ2V0LnRpdGxlLmljb24gPSBsaXN0SWNvbjtcbiAgICBsb2dDb25zb2xlV2lkZ2V0LnRpdGxlLmxhYmVsID0gdHJhbnMuX18oJ0xvZyBDb25zb2xlJyk7XG5cbiAgICBjb25zdCBhZGRDaGVja3BvaW50QnV0dG9uID0gbmV3IENvbW1hbmRUb29sYmFyQnV0dG9uKHtcbiAgICAgIGNvbW1hbmRzOiBhcHAuY29tbWFuZHMsXG4gICAgICBpZDogQ29tbWFuZElEcy5hZGRDaGVja3BvaW50XG4gICAgfSk7XG5cbiAgICBjb25zdCBjbGVhckJ1dHRvbiA9IG5ldyBDb21tYW5kVG9vbGJhckJ1dHRvbih7XG4gICAgICBjb21tYW5kczogYXBwLmNvbW1hbmRzLFxuICAgICAgaWQ6IENvbW1hbmRJRHMuY2xlYXJcbiAgICB9KTtcblxuICAgIGxvZ0NvbnNvbGVXaWRnZXQudG9vbGJhci5hZGRJdGVtKFxuICAgICAgJ2xhYi1sb2ctY29uc29sZS1hZGQtY2hlY2twb2ludCcsXG4gICAgICBhZGRDaGVja3BvaW50QnV0dG9uXG4gICAgKTtcbiAgICBsb2dDb25zb2xlV2lkZ2V0LnRvb2xiYXIuYWRkSXRlbSgnbGFiLWxvZy1jb25zb2xlLWNsZWFyJywgY2xlYXJCdXR0b24pO1xuXG4gICAgbG9nQ29uc29sZVdpZGdldC50b29sYmFyLmFkZEl0ZW0oXG4gICAgICAnbGV2ZWwnLFxuICAgICAgbmV3IExvZ0xldmVsU3dpdGNoZXIobG9nQ29uc29sZVdpZGdldC5jb250ZW50LCB0cmFuc2xhdG9yKVxuICAgICk7XG5cbiAgICBsb2dDb25zb2xlUGFuZWwuc291cmNlQ2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgIH0pO1xuXG4gICAgbG9nQ29uc29sZVBhbmVsLnNvdXJjZURpc3BsYXllZC5jb25uZWN0KChwYW5lbCwgeyBzb3VyY2UsIHZlcnNpb24gfSkgPT4ge1xuICAgICAgc3RhdHVzLm1vZGVsLnNvdXJjZURpc3BsYXllZChzb3VyY2UsIHZlcnNpb24pO1xuICAgIH0pO1xuXG4gICAgbG9nQ29uc29sZVdpZGdldC5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIGxvZ0NvbnNvbGVXaWRnZXQgPSBudWxsO1xuICAgICAgbG9nQ29uc29sZVBhbmVsID0gbnVsbDtcbiAgICAgIGFwcC5jb21tYW5kcy5ub3RpZnlDb21tYW5kQ2hhbmdlZCgpO1xuICAgIH0pO1xuXG4gICAgYXBwLnNoZWxsLmFkZChsb2dDb25zb2xlV2lkZ2V0LCAnZG93bicsIHtcbiAgICAgIHJlZjogb3B0aW9ucy5yZWYsXG4gICAgICBtb2RlOiBvcHRpb25zLmluc2VydE1vZGUsXG4gICAgICB0eXBlOiAnTG9nIENvbnNvbGUnXG4gICAgfSk7XG4gICAgdm9pZCB0cmFja2VyLmFkZChsb2dDb25zb2xlV2lkZ2V0KTtcbiAgICBhcHAuc2hlbGwuYWN0aXZhdGVCeUlkKGxvZ0NvbnNvbGVXaWRnZXQuaWQpO1xuXG4gICAgbG9nQ29uc29sZVdpZGdldC51cGRhdGUoKTtcbiAgICBhcHAuY29tbWFuZHMubm90aWZ5Q29tbWFuZENoYW5nZWQoKTtcbiAgfTtcblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm9wZW4sIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgTG9nIENvbnNvbGUnKSxcbiAgICBleGVjdXRlOiAob3B0aW9uczogSUxvZ0NvbnNvbGVPcHRpb25zID0ge30pID0+IHtcbiAgICAgIC8vIFRvZ2dsZSB0aGUgZGlzcGxheVxuICAgICAgaWYgKGxvZ0NvbnNvbGVXaWRnZXQpIHtcbiAgICAgICAgbG9nQ29uc29sZVdpZGdldC5kaXNwb3NlKCk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBjcmVhdGVMb2dDb25zb2xlV2lkZ2V0KG9wdGlvbnMpO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNUb2dnbGVkOiAoKSA9PiB7XG4gICAgICByZXR1cm4gbG9nQ29uc29sZVdpZGdldCAhPT0gbnVsbDtcbiAgICB9XG4gIH0pO1xuXG4gIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuYWRkQ2hlY2twb2ludCwge1xuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGxvZ0NvbnNvbGVQYW5lbD8ubG9nZ2VyPy5jaGVja3BvaW50KCk7XG4gICAgfSxcbiAgICBpY29uOiBhZGRJY29uLFxuICAgIGlzRW5hYmxlZDogKCkgPT4gISFsb2dDb25zb2xlUGFuZWwgJiYgbG9nQ29uc29sZVBhbmVsLnNvdXJjZSAhPT0gbnVsbCxcbiAgICBsYWJlbDogdHJhbnMuX18oJ0FkZCBDaGVja3BvaW50JylcbiAgfSk7XG5cbiAgYXBwLmNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5jbGVhciwge1xuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGxvZ0NvbnNvbGVQYW5lbD8ubG9nZ2VyPy5jbGVhcigpO1xuICAgIH0sXG4gICAgaWNvbjogY2xlYXJJY29uLFxuICAgIGlzRW5hYmxlZDogKCkgPT4gISFsb2dDb25zb2xlUGFuZWwgJiYgbG9nQ29uc29sZVBhbmVsLnNvdXJjZSAhPT0gbnVsbCxcbiAgICBsYWJlbDogdHJhbnMuX18oJ0NsZWFyIExvZycpXG4gIH0pO1xuXG4gIGZ1bmN0aW9uIHRvVGl0bGVDYXNlKHZhbHVlOiBzdHJpbmcpIHtcbiAgICByZXR1cm4gdmFsdWUubGVuZ3RoID09PSAwID8gdmFsdWUgOiB2YWx1ZVswXS50b1VwcGVyQ2FzZSgpICsgdmFsdWUuc2xpY2UoMSk7XG4gIH1cblxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnNldExldmVsLCB7XG4gICAgLy8gVE9ETzogZmluZCBnb29kIGljb24gY2xhc3NcbiAgICBleGVjdXRlOiAoYXJnczogeyBsZXZlbDogTG9nTGV2ZWwgfSkgPT4ge1xuICAgICAgaWYgKGxvZ0NvbnNvbGVQYW5lbD8ubG9nZ2VyKSB7XG4gICAgICAgIGxvZ0NvbnNvbGVQYW5lbC5sb2dnZXIubGV2ZWwgPSBhcmdzLmxldmVsO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkOiAoKSA9PiAhIWxvZ0NvbnNvbGVQYW5lbCAmJiBsb2dDb25zb2xlUGFuZWwuc291cmNlICE9PSBudWxsLFxuICAgIGxhYmVsOiBhcmdzID0+XG4gICAgICBhcmdzWydsZXZlbCddXG4gICAgICAgID8gdHJhbnMuX18oJ1NldCBMb2cgTGV2ZWwgdG8gJTEnLCB0b1RpdGxlQ2FzZShhcmdzLmxldmVsIGFzIHN0cmluZykpXG4gICAgICAgIDogdHJhbnMuX18oJ1NldCBsb2cgbGV2ZWwgdG8gYGxldmVsYC4nKVxuICB9KTtcblxuICBpZiAocGFsZXR0ZSkge1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLm9wZW4sXG4gICAgICBjYXRlZ29yeTogdHJhbnMuX18oJ01haW4gQXJlYScpXG4gICAgfSk7XG4gIH1cbiAgaWYgKHN0YXR1c0Jhcikge1xuICAgIHN0YXR1c0Jhci5yZWdpc3RlclN0YXR1c0l0ZW0oJ0BqdXB5dGVybGFiL2xvZ2NvbnNvbGUtZXh0ZW5zaW9uOnN0YXR1cycsIHtcbiAgICAgIGl0ZW06IHN0YXR1cyxcbiAgICAgIGFsaWduOiAnbGVmdCcsXG4gICAgICBpc0FjdGl2ZTogKCkgPT4gc3RhdHVzLm1vZGVsPy52ZXJzaW9uID4gMCxcbiAgICAgIGFjdGl2ZVN0YXRlQ2hhbmdlZDogc3RhdHVzLm1vZGVsIS5zdGF0ZUNoYW5nZWRcbiAgICB9KTtcbiAgfVxuXG4gIGZ1bmN0aW9uIHNldFNvdXJjZShuZXdWYWx1ZTogV2lkZ2V0IHwgbnVsbCkge1xuICAgIGlmIChsb2dDb25zb2xlV2lkZ2V0ICYmIG5ld1ZhbHVlID09PSBsb2dDb25zb2xlV2lkZ2V0KSB7XG4gICAgICAvLyBEbyBub3QgY2hhbmdlIGFueXRoaW5nIGlmIHdlIGFyZSBqdXN0IGZvY3VzaW5nIG9uIG91cnNlbHZlc1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGxldCBzb3VyY2U6IHN0cmluZyB8IG51bGw7XG4gICAgaWYgKG5ld1ZhbHVlICYmIG5idHJhY2tlci5oYXMobmV3VmFsdWUpKSB7XG4gICAgICBzb3VyY2UgPSAobmV3VmFsdWUgYXMgTm90ZWJvb2tQYW5lbCkuY29udGV4dC5wYXRoO1xuICAgIH0gZWxzZSB7XG4gICAgICBzb3VyY2UgPSBudWxsO1xuICAgIH1cbiAgICBpZiAobG9nQ29uc29sZVBhbmVsKSB7XG4gICAgICBsb2dDb25zb2xlUGFuZWwuc291cmNlID0gc291cmNlO1xuICAgIH1cbiAgICBzdGF0dXMubW9kZWwuc291cmNlID0gc291cmNlO1xuICB9XG4gIHZvaWQgYXBwLnJlc3RvcmVkLnRoZW4oKCkgPT4ge1xuICAgIC8vIFNldCBzb3VyY2Ugb25seSBhZnRlciBhcHAgaXMgcmVzdG9yZWQgaW4gb3JkZXIgdG8gYWxsb3cgcmVzdG9yZXIgdG9cbiAgICAvLyByZXN0b3JlIHByZXZpb3VzIHNvdXJjZSBmaXJzdCwgd2hpY2ggbWF5IHNldCB0aGUgcmVuZGVyZXJcbiAgICBzZXRTb3VyY2UobGFiU2hlbGwuY3VycmVudFdpZGdldCk7XG4gICAgbGFiU2hlbGwuY3VycmVudENoYW5nZWQuY29ubmVjdCgoXywgeyBuZXdWYWx1ZSB9KSA9PiBzZXRTb3VyY2UobmV3VmFsdWUpKTtcbiAgfSk7XG5cbiAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgIGNvbnN0IHVwZGF0ZVNldHRpbmdzID0gKHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyk6IHZvaWQgPT4ge1xuICAgICAgbG9nZ2VyUmVnaXN0cnkubWF4TGVuZ3RoID0gc2V0dGluZ3MuZ2V0KCdtYXhMb2dFbnRyaWVzJylcbiAgICAgICAgLmNvbXBvc2l0ZSBhcyBudW1iZXI7XG4gICAgICBzdGF0dXMubW9kZWwuZmxhc2hFbmFibGVkID0gc2V0dGluZ3MuZ2V0KCdmbGFzaCcpLmNvbXBvc2l0ZSBhcyBib29sZWFuO1xuICAgIH07XG5cbiAgICBQcm9taXNlLmFsbChbc2V0dGluZ1JlZ2lzdHJ5LmxvYWQoTE9HX0NPTlNPTEVfUExVR0lOX0lEKSwgYXBwLnJlc3RvcmVkXSlcbiAgICAgIC50aGVuKChbc2V0dGluZ3NdKSA9PiB7XG4gICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgICAgc2V0dGluZ3MuY2hhbmdlZC5jb25uZWN0KHNldHRpbmdzID0+IHtcbiAgICAgICAgICB1cGRhdGVTZXR0aW5ncyhzZXR0aW5ncyk7XG4gICAgICAgIH0pO1xuICAgICAgfSlcbiAgICAgIC5jYXRjaCgocmVhc29uOiBFcnJvcikgPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKHJlYXNvbi5tZXNzYWdlKTtcbiAgICAgIH0pO1xuICB9XG5cbiAgcmV0dXJuIGxvZ2dlclJlZ2lzdHJ5O1xufVxuXG4vKipcbiAqIEEgdG9vbGJhciB3aWRnZXQgdGhhdCBzd2l0Y2hlcyBsb2cgbGV2ZWxzLlxuICovXG5leHBvcnQgY2xhc3MgTG9nTGV2ZWxTd2l0Y2hlciBleHRlbmRzIFJlYWN0V2lkZ2V0IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBjZWxsIHR5cGUgc3dpdGNoZXIuXG4gICAqL1xuICBjb25zdHJ1Y3Rvcih3aWRnZXQ6IExvZ0NvbnNvbGVQYW5lbCwgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLnRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLmFkZENsYXNzKCdqcC1Mb2dDb25zb2xlLXRvb2xiYXJMb2dMZXZlbCcpO1xuICAgIHRoaXMuX2xvZ0NvbnNvbGUgPSB3aWRnZXQ7XG4gICAgaWYgKHdpZGdldC5zb3VyY2UpIHtcbiAgICAgIHRoaXMudXBkYXRlKCk7XG4gICAgfVxuICAgIHdpZGdldC5zb3VyY2VDaGFuZ2VkLmNvbm5lY3QodGhpcy5fdXBkYXRlU291cmNlLCB0aGlzKTtcbiAgfVxuXG4gIHByaXZhdGUgX3VwZGF0ZVNvdXJjZShcbiAgICBzZW5kZXI6IExvZ0NvbnNvbGVQYW5lbCxcbiAgICB7IG9sZFZhbHVlLCBuZXdWYWx1ZSB9OiBJQ2hhbmdlZEFyZ3M8c3RyaW5nIHwgbnVsbD5cbiAgKSB7XG4gICAgLy8gVHJhbnNmZXIgc3RhdGVDaGFuZ2VkIGhhbmRsZXIgdG8gbmV3IHNvdXJjZSBsb2dnZXJcbiAgICBpZiAob2xkVmFsdWUgIT09IG51bGwpIHtcbiAgICAgIGNvbnN0IGxvZ2dlciA9IHNlbmRlci5sb2dnZXJSZWdpc3RyeS5nZXRMb2dnZXIob2xkVmFsdWUpO1xuICAgICAgbG9nZ2VyLnN0YXRlQ2hhbmdlZC5kaXNjb25uZWN0KHRoaXMudXBkYXRlLCB0aGlzKTtcbiAgICB9XG4gICAgaWYgKG5ld1ZhbHVlICE9PSBudWxsKSB7XG4gICAgICBjb25zdCBsb2dnZXIgPSBzZW5kZXIubG9nZ2VyUmVnaXN0cnkuZ2V0TG9nZ2VyKG5ld1ZhbHVlKTtcbiAgICAgIGxvZ2dlci5zdGF0ZUNoYW5nZWQuY29ubmVjdCh0aGlzLnVwZGF0ZSwgdGhpcyk7XG4gICAgfVxuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBjaGFuZ2VgIGV2ZW50cyBmb3IgdGhlIEhUTUxTZWxlY3QgY29tcG9uZW50LlxuICAgKi9cbiAgaGFuZGxlQ2hhbmdlID0gKGV2ZW50OiBSZWFjdC5DaGFuZ2VFdmVudDxIVE1MU2VsZWN0RWxlbWVudD4pOiB2b2lkID0+IHtcbiAgICBpZiAodGhpcy5fbG9nQ29uc29sZS5sb2dnZXIpIHtcbiAgICAgIHRoaXMuX2xvZ0NvbnNvbGUubG9nZ2VyLmxldmVsID0gZXZlbnQudGFyZ2V0LnZhbHVlIGFzIExvZ0xldmVsO1xuICAgIH1cbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgYGtleWRvd25gIGV2ZW50cyBmb3IgdGhlIEhUTUxTZWxlY3QgY29tcG9uZW50LlxuICAgKi9cbiAgaGFuZGxlS2V5RG93biA9IChldmVudDogUmVhY3QuS2V5Ym9hcmRFdmVudCk6IHZvaWQgPT4ge1xuICAgIGlmIChldmVudC5rZXlDb2RlID09PSAxMykge1xuICAgICAgdGhpcy5fbG9nQ29uc29sZS5hY3RpdmF0ZSgpO1xuICAgIH1cbiAgfTtcblxuICByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgIGNvbnN0IGxvZ2dlciA9IHRoaXMuX2xvZ0NvbnNvbGUubG9nZ2VyO1xuICAgIHJldHVybiAoXG4gICAgICA8PlxuICAgICAgICA8bGFiZWxcbiAgICAgICAgICBodG1sRm9yPXt0aGlzLl9pZH1cbiAgICAgICAgICBjbGFzc05hbWU9e1xuICAgICAgICAgICAgbG9nZ2VyID09PSBudWxsXG4gICAgICAgICAgICAgID8gJ2pwLUxvZ0NvbnNvbGUtdG9vbGJhckxvZ0xldmVsLWRpc2FibGVkJ1xuICAgICAgICAgICAgICA6IHVuZGVmaW5lZFxuICAgICAgICAgIH1cbiAgICAgICAgPlxuICAgICAgICAgIHt0aGlzLl90cmFucy5fXygnTG9nIExldmVsOicpfVxuICAgICAgICA8L2xhYmVsPlxuICAgICAgICA8SFRNTFNlbGVjdFxuICAgICAgICAgIGlkPXt0aGlzLl9pZH1cbiAgICAgICAgICBjbGFzc05hbWU9XCJqcC1Mb2dDb25zb2xlLXRvb2xiYXJMb2dMZXZlbERyb3Bkb3duXCJcbiAgICAgICAgICBvbkNoYW5nZT17dGhpcy5oYW5kbGVDaGFuZ2V9XG4gICAgICAgICAgb25LZXlEb3duPXt0aGlzLmhhbmRsZUtleURvd259XG4gICAgICAgICAgdmFsdWU9e2xvZ2dlcj8ubGV2ZWx9XG4gICAgICAgICAgYXJpYS1sYWJlbD17dGhpcy5fdHJhbnMuX18oJ0xvZyBsZXZlbCcpfVxuICAgICAgICAgIGRpc2FibGVkPXtsb2dnZXIgPT09IG51bGx9XG4gICAgICAgICAgb3B0aW9ucz17XG4gICAgICAgICAgICBsb2dnZXIgPT09IG51bGxcbiAgICAgICAgICAgICAgPyBbXVxuICAgICAgICAgICAgICA6IFtcbiAgICAgICAgICAgICAgICAgIFt0aGlzLl90cmFucy5fXygnQ3JpdGljYWwnKSwgJ0NyaXRpY2FsJ10sXG4gICAgICAgICAgICAgICAgICBbdGhpcy5fdHJhbnMuX18oJ0Vycm9yJyksICdFcnJvciddLFxuICAgICAgICAgICAgICAgICAgW3RoaXMuX3RyYW5zLl9fKCdXYXJuaW5nJyksICdXYXJuaW5nJ10sXG4gICAgICAgICAgICAgICAgICBbdGhpcy5fdHJhbnMuX18oJ0luZm8nKSwgJ0luZm8nXSxcbiAgICAgICAgICAgICAgICAgIFt0aGlzLl90cmFucy5fXygnRGVidWcnKSwgJ0RlYnVnJ11cbiAgICAgICAgICAgICAgICBdLm1hcChkYXRhID0+ICh7XG4gICAgICAgICAgICAgICAgICBsYWJlbDogZGF0YVswXSxcbiAgICAgICAgICAgICAgICAgIHZhbHVlOiBkYXRhWzFdLnRvTG93ZXJDYXNlKClcbiAgICAgICAgICAgICAgICB9KSlcbiAgICAgICAgICB9XG4gICAgICAgIC8+XG4gICAgICA8Lz5cbiAgICApO1xuICB9XG5cbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIHByaXZhdGUgX2xvZ0NvbnNvbGU6IExvZ0NvbnNvbGVQYW5lbDtcbiAgcHJpdmF0ZSBfaWQgPSBgbGV2ZWwtJHtVVUlELnV1aWQ0KCl9YDtcbn1cblxuZXhwb3J0IGRlZmF1bHQgbG9nQ29uc29sZVBsdWdpbjtcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHtcbiAgSUNvbnRlbnRDaGFuZ2UsXG4gIElMb2dnZXIsXG4gIElMb2dnZXJSZWdpc3RyeVxufSBmcm9tICdAanVweXRlcmxhYi9sb2djb25zb2xlJztcbmltcG9ydCB7IEdyb3VwSXRlbSwgaW50ZXJhY3RpdmVJdGVtLCBUZXh0SXRlbSB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXR1c2Jhcic7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBsaXN0SWNvbiwgVkRvbU1vZGVsLCBWRG9tUmVuZGVyZXIgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5cbi8qKlxuICogQSBwdXJlIGZ1bmN0aW9uYWwgY29tcG9uZW50IGZvciBhIExvZyBDb25zb2xlIHN0YXR1cyBpdGVtLlxuICpcbiAqIEBwYXJhbSBwcm9wcyAtIHRoZSBwcm9wcyBmb3IgdGhlIGNvbXBvbmVudC5cbiAqXG4gKiBAcmV0dXJucyBhIHRzeCBjb21wb25lbnQgZm9yIHJlbmRlcmluZyB0aGUgTG9nIENvbnNvbGUgc3RhdHVzLlxuICovXG5mdW5jdGlvbiBMb2dDb25zb2xlU3RhdHVzQ29tcG9uZW50KFxuICBwcm9wczogTG9nQ29uc29sZVN0YXR1c0NvbXBvbmVudC5JUHJvcHNcbik6IFJlYWN0LlJlYWN0RWxlbWVudDxMb2dDb25zb2xlU3RhdHVzQ29tcG9uZW50LklQcm9wcz4ge1xuICBjb25zdCB0cmFuc2xhdG9yID0gcHJvcHMudHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgbGV0IHRpdGxlID0gJyc7XG4gIGlmIChwcm9wcy5uZXdNZXNzYWdlcyA+IDApIHtcbiAgICB0aXRsZSA9IHRyYW5zLl9fKFxuICAgICAgJyUxIG5ldyBtZXNzYWdlcywgJTIgbG9nIGVudHJpZXMgZm9yICUzJyxcbiAgICAgIHByb3BzLm5ld01lc3NhZ2VzLFxuICAgICAgcHJvcHMubG9nRW50cmllcyxcbiAgICAgIHByb3BzLnNvdXJjZVxuICAgICk7XG4gIH0gZWxzZSB7XG4gICAgdGl0bGUgKz0gdHJhbnMuX18oJyUxIGxvZyBlbnRyaWVzIGZvciAlMicsIHByb3BzLmxvZ0VudHJpZXMsIHByb3BzLnNvdXJjZSk7XG4gIH1cbiAgcmV0dXJuIChcbiAgICA8R3JvdXBJdGVtIHNwYWNpbmc9ezB9IG9uQ2xpY2s9e3Byb3BzLmhhbmRsZUNsaWNrfSB0aXRsZT17dGl0bGV9PlxuICAgICAgPGxpc3RJY29uLnJlYWN0IHRvcD17JzJweCd9IHN0eWxlc2hlZXQ9eydzdGF0dXNCYXInfSAvPlxuICAgICAge3Byb3BzLm5ld01lc3NhZ2VzID4gMCA/IDxUZXh0SXRlbSBzb3VyY2U9e3Byb3BzLm5ld01lc3NhZ2VzfSAvPiA6IDw+PC8+fVxuICAgIDwvR3JvdXBJdGVtPlxuICApO1xufVxuXG4vKlxuICogQSBuYW1lc3BhY2UgZm9yIExvZ0NvbnNvbGVTdGF0dXNDb21wb25lbnQuXG4gKi9cbm5hbWVzcGFjZSBMb2dDb25zb2xlU3RhdHVzQ29tcG9uZW50IHtcbiAgLyoqXG4gICAqIFRoZSBwcm9wcyBmb3IgdGhlIExvZ0NvbnNvbGVTdGF0dXNDb21wb25lbnQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gICAgLyoqXG4gICAgICogQSBjbGljayBoYW5kbGVyIGZvciB0aGUgaXRlbS4gQnkgZGVmYXVsdFxuICAgICAqIExvZyBDb25zb2xlIHBhbmVsIGlzIGxhdW5jaGVkLlxuICAgICAqL1xuICAgIGhhbmRsZUNsaWNrOiAoKSA9PiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogTnVtYmVyIG9mIGxvZyBlbnRyaWVzLlxuICAgICAqL1xuICAgIGxvZ0VudHJpZXM6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIE51bWJlciBvZiBuZXcgbG9nIG1lc3NhZ2VzLlxuICAgICAqL1xuICAgIG5ld01lc3NhZ2VzOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBMb2cgc291cmNlIG5hbWVcbiAgICAgKi9cbiAgICBzb3VyY2U6IHN0cmluZyB8IG51bGw7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYXBwbGljYXRpb24gbGFuZ3VhZ2UgdHJhbnNsYXRvclxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxufVxuXG4vKipcbiAqIEEgVkRvbVJlbmRlcmVyIHdpZGdldCBmb3IgZGlzcGxheWluZyB0aGUgc3RhdHVzIG9mIExvZyBDb25zb2xlIGxvZ3MuXG4gKi9cbmV4cG9ydCBjbGFzcyBMb2dDb25zb2xlU3RhdHVzIGV4dGVuZHMgVkRvbVJlbmRlcmVyPExvZ0NvbnNvbGVTdGF0dXMuTW9kZWw+IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCB0aGUgbG9nIGNvbnNvbGUgc3RhdHVzIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMgLSBUaGUgc3RhdHVzIHdpZGdldCBpbml0aWFsaXphdGlvbiBvcHRpb25zLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogTG9nQ29uc29sZVN0YXR1cy5JT3B0aW9ucykge1xuICAgIHN1cGVyKG5ldyBMb2dDb25zb2xlU3RhdHVzLk1vZGVsKG9wdGlvbnMubG9nZ2VyUmVnaXN0cnkpKTtcbiAgICB0aGlzLnRyYW5zbGF0b3IgPSBvcHRpb25zLnRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgdGhpcy5faGFuZGxlQ2xpY2sgPSBvcHRpb25zLmhhbmRsZUNsaWNrO1xuICAgIHRoaXMuYWRkQ2xhc3MoaW50ZXJhY3RpdmVJdGVtKTtcbiAgICB0aGlzLmFkZENsYXNzKCdqcC1Mb2dDb25zb2xlU3RhdHVzSXRlbScpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbmRlciB0aGUgbG9nIGNvbnNvbGUgc3RhdHVzIGl0ZW0uXG4gICAqL1xuICByZW5kZXIoKTogSlNYLkVsZW1lbnQgfCBudWxsIHtcbiAgICBpZiAodGhpcy5tb2RlbCA9PT0gbnVsbCB8fCB0aGlzLm1vZGVsLnZlcnNpb24gPT09IDApIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cblxuICAgIGNvbnN0IHtcbiAgICAgIGZsYXNoRW5hYmxlZCxcbiAgICAgIG1lc3NhZ2VzLFxuICAgICAgc291cmNlLFxuICAgICAgdmVyc2lvbixcbiAgICAgIHZlcnNpb25EaXNwbGF5ZWQsXG4gICAgICB2ZXJzaW9uTm90aWZpZWRcbiAgICB9ID0gdGhpcy5tb2RlbDtcbiAgICBpZiAoc291cmNlICE9PSBudWxsICYmIGZsYXNoRW5hYmxlZCAmJiB2ZXJzaW9uID4gdmVyc2lvbk5vdGlmaWVkKSB7XG4gICAgICB0aGlzLl9mbGFzaEhpZ2hsaWdodCgpO1xuICAgICAgdGhpcy5tb2RlbC5zb3VyY2VOb3RpZmllZChzb3VyY2UsIHZlcnNpb24pO1xuICAgIH0gZWxzZSBpZiAoc291cmNlICE9PSBudWxsICYmIGZsYXNoRW5hYmxlZCAmJiB2ZXJzaW9uID4gdmVyc2lvbkRpc3BsYXllZCkge1xuICAgICAgdGhpcy5fc2hvd0hpZ2hsaWdodGVkKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMuX2NsZWFySGlnaGxpZ2h0KCk7XG4gICAgfVxuXG4gICAgcmV0dXJuIChcbiAgICAgIDxMb2dDb25zb2xlU3RhdHVzQ29tcG9uZW50XG4gICAgICAgIGhhbmRsZUNsaWNrPXt0aGlzLl9oYW5kbGVDbGlja31cbiAgICAgICAgbG9nRW50cmllcz17bWVzc2FnZXN9XG4gICAgICAgIG5ld01lc3NhZ2VzPXt2ZXJzaW9uIC0gdmVyc2lvbkRpc3BsYXllZH1cbiAgICAgICAgc291cmNlPXt0aGlzLm1vZGVsLnNvdXJjZX1cbiAgICAgICAgdHJhbnNsYXRvcj17dGhpcy50cmFuc2xhdG9yfVxuICAgICAgLz5cbiAgICApO1xuICB9XG5cbiAgcHJpdmF0ZSBfZmxhc2hIaWdobGlnaHQoKSB7XG4gICAgdGhpcy5fc2hvd0hpZ2hsaWdodGVkKCk7XG5cbiAgICAvLyBUbyBtYWtlIHN1cmUgdGhlIGJyb3dzZXIgdHJpZ2dlcnMgdGhlIGFuaW1hdGlvbiwgd2UgcmVtb3ZlIHRoZSBjbGFzcyxcbiAgICAvLyB3YWl0IGZvciBhbiBhbmltYXRpb24gZnJhbWUsIHRoZW4gYWRkIGl0IGJhY2tcbiAgICB0aGlzLnJlbW92ZUNsYXNzKCdqcC1Mb2dDb25zb2xlLWZsYXNoJyk7XG4gICAgcmVxdWVzdEFuaW1hdGlvbkZyYW1lKCgpID0+IHtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLUxvZ0NvbnNvbGUtZmxhc2gnKTtcbiAgICB9KTtcbiAgfVxuXG4gIHByaXZhdGUgX3Nob3dIaWdobGlnaHRlZCgpIHtcbiAgICB0aGlzLmFkZENsYXNzKCdqcC1tb2Qtc2VsZWN0ZWQnKTtcbiAgfVxuXG4gIHByaXZhdGUgX2NsZWFySGlnaGxpZ2h0KCkge1xuICAgIHRoaXMucmVtb3ZlQ2xhc3MoJ2pwLUxvZ0NvbnNvbGUtZmxhc2gnKTtcbiAgICB0aGlzLnJlbW92ZUNsYXNzKCdqcC1tb2Qtc2VsZWN0ZWQnKTtcbiAgfVxuXG4gIHJlYWRvbmx5IHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF9oYW5kbGVDbGljazogKCkgPT4gdm9pZDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgTG9nIENvbnNvbGUgbG9nIHN0YXR1cy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBMb2dDb25zb2xlU3RhdHVzIHtcbiAgLyoqXG4gICAqIEEgVkRvbU1vZGVsIGZvciB0aGUgTG9nQ29uc29sZVN0YXR1cyBpdGVtLlxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIE1vZGVsIGV4dGVuZHMgVkRvbU1vZGVsIHtcbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSBuZXcgTG9nQ29uc29sZVN0YXR1cyBtb2RlbC5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBsb2dnZXJSZWdpc3RyeSAtIFRoZSBsb2dnZXIgcmVnaXN0cnkgcHJvdmlkaW5nIHRoZSBsb2dzLlxuICAgICAqL1xuICAgIGNvbnN0cnVjdG9yKGxvZ2dlclJlZ2lzdHJ5OiBJTG9nZ2VyUmVnaXN0cnkpIHtcbiAgICAgIHN1cGVyKCk7XG5cbiAgICAgIHRoaXMuX2xvZ2dlclJlZ2lzdHJ5ID0gbG9nZ2VyUmVnaXN0cnk7XG4gICAgICB0aGlzLl9sb2dnZXJSZWdpc3RyeS5yZWdpc3RyeUNoYW5nZWQuY29ubmVjdChcbiAgICAgICAgdGhpcy5faGFuZGxlTG9nUmVnaXN0cnlDaGFuZ2UsXG4gICAgICAgIHRoaXNcbiAgICAgICk7XG4gICAgICB0aGlzLl9oYW5kbGVMb2dSZWdpc3RyeUNoYW5nZSgpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIE51bWJlciBvZiBtZXNzYWdlcyBjdXJyZW50bHkgaW4gdGhlIGN1cnJlbnQgc291cmNlLlxuICAgICAqL1xuICAgIGdldCBtZXNzYWdlcygpOiBudW1iZXIge1xuICAgICAgaWYgKHRoaXMuX3NvdXJjZSA9PT0gbnVsbCkge1xuICAgICAgICByZXR1cm4gMDtcbiAgICAgIH1cbiAgICAgIGNvbnN0IGxvZ2dlciA9IHRoaXMuX2xvZ2dlclJlZ2lzdHJ5LmdldExvZ2dlcih0aGlzLl9zb3VyY2UpO1xuICAgICAgcmV0dXJuIGxvZ2dlci5sZW5ndGg7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIG51bWJlciBvZiBtZXNzYWdlcyBldmVyIHN0b3JlZCBieSB0aGUgY3VycmVudCBzb3VyY2UuXG4gICAgICovXG4gICAgZ2V0IHZlcnNpb24oKTogbnVtYmVyIHtcbiAgICAgIGlmICh0aGlzLl9zb3VyY2UgPT09IG51bGwpIHtcbiAgICAgICAgcmV0dXJuIDA7XG4gICAgICB9XG4gICAgICBjb25zdCBsb2dnZXIgPSB0aGlzLl9sb2dnZXJSZWdpc3RyeS5nZXRMb2dnZXIodGhpcy5fc291cmNlKTtcbiAgICAgIHJldHVybiBsb2dnZXIudmVyc2lvbjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbmFtZSBvZiB0aGUgYWN0aXZlIGxvZyBzb3VyY2VcbiAgICAgKi9cbiAgICBnZXQgc291cmNlKCk6IHN0cmluZyB8IG51bGwge1xuICAgICAgcmV0dXJuIHRoaXMuX3NvdXJjZTtcbiAgICB9XG5cbiAgICBzZXQgc291cmNlKG5hbWU6IHN0cmluZyB8IG51bGwpIHtcbiAgICAgIGlmICh0aGlzLl9zb3VyY2UgPT09IG5hbWUpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuXG4gICAgICB0aGlzLl9zb3VyY2UgPSBuYW1lO1xuXG4gICAgICAvLyByZWZyZXNoIHJlbmRlcmluZ1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBsYXN0IHNvdXJjZSB2ZXJzaW9uIHRoYXQgd2FzIGRpc3BsYXllZC5cbiAgICAgKi9cbiAgICBnZXQgdmVyc2lvbkRpc3BsYXllZCgpOiBudW1iZXIge1xuICAgICAgaWYgKHRoaXMuX3NvdXJjZSA9PT0gbnVsbCkge1xuICAgICAgICByZXR1cm4gMDtcbiAgICAgIH1cbiAgICAgIHJldHVybiB0aGlzLl9zb3VyY2VWZXJzaW9uLmdldCh0aGlzLl9zb3VyY2UpPy5sYXN0RGlzcGxheWVkID8/IDA7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIGxhc3Qgc291cmNlIHZlcnNpb24gd2Ugbm90aWZpZWQgdGhlIHVzZXIgYWJvdXQuXG4gICAgICovXG4gICAgZ2V0IHZlcnNpb25Ob3RpZmllZCgpOiBudW1iZXIge1xuICAgICAgaWYgKHRoaXMuX3NvdXJjZSA9PT0gbnVsbCkge1xuICAgICAgICByZXR1cm4gMDtcbiAgICAgIH1cbiAgICAgIHJldHVybiB0aGlzLl9zb3VyY2VWZXJzaW9uLmdldCh0aGlzLl9zb3VyY2UpPy5sYXN0Tm90aWZpZWQgPz8gMDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBGbGFnIHRvIHRvZ2dsZSBmbGFzaGluZyB3aGVuIG5ldyBsb2dzIGFkZGVkLlxuICAgICAqL1xuICAgIGdldCBmbGFzaEVuYWJsZWQoKTogYm9vbGVhbiB7XG4gICAgICByZXR1cm4gdGhpcy5fZmxhc2hFbmFibGVkO1xuICAgIH1cblxuICAgIHNldCBmbGFzaEVuYWJsZWQoZW5hYmxlZDogYm9vbGVhbikge1xuICAgICAgaWYgKHRoaXMuX2ZsYXNoRW5hYmxlZCA9PT0gZW5hYmxlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG5cbiAgICAgIHRoaXMuX2ZsYXNoRW5hYmxlZCA9IGVuYWJsZWQ7XG4gICAgICB0aGlzLmZsYXNoRW5hYmxlZENoYW5nZWQuZW1pdCgpO1xuXG4gICAgICAvLyByZWZyZXNoIHJlbmRlcmluZ1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFJlY29yZCB0aGUgbGFzdCBzb3VyY2UgdmVyc2lvbiBkaXNwbGF5ZWQgdG8gdGhlIHVzZXIuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gc291cmNlIC0gVGhlIG5hbWUgb2YgdGhlIGxvZyBzb3VyY2UuXG4gICAgICogQHBhcmFtIHZlcnNpb24gLSBUaGUgdmVyc2lvbiBvZiB0aGUgbG9nIHRoYXQgd2FzIGRpc3BsYXllZC5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGlzIHdpbGwgYWxzbyB1cGRhdGUgdGhlIGxhc3Qgbm90aWZpZWQgdmVyc2lvbiBzbyB0aGF0IHRoZSBsYXN0XG4gICAgICogbm90aWZpZWQgdmVyc2lvbiBpcyBhbHdheXMgYXQgbGVhc3QgdGhlIGxhc3QgZGlzcGxheWVkIHZlcnNpb24uXG4gICAgICovXG4gICAgc291cmNlRGlzcGxheWVkKHNvdXJjZTogc3RyaW5nIHwgbnVsbCwgdmVyc2lvbjogbnVtYmVyIHwgbnVsbCk6IHZvaWQge1xuICAgICAgaWYgKHNvdXJjZSA9PT0gbnVsbCB8fCB2ZXJzaW9uID09PSBudWxsKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHZlcnNpb25zID0gdGhpcy5fc291cmNlVmVyc2lvbi5nZXQoc291cmNlKSE7XG4gICAgICBsZXQgY2hhbmdlID0gZmFsc2U7XG4gICAgICBpZiAodmVyc2lvbnMubGFzdERpc3BsYXllZCA8IHZlcnNpb24pIHtcbiAgICAgICAgdmVyc2lvbnMubGFzdERpc3BsYXllZCA9IHZlcnNpb247XG4gICAgICAgIGNoYW5nZSA9IHRydWU7XG4gICAgICB9XG4gICAgICBpZiAodmVyc2lvbnMubGFzdE5vdGlmaWVkIDwgdmVyc2lvbikge1xuICAgICAgICB2ZXJzaW9ucy5sYXN0Tm90aWZpZWQgPSB2ZXJzaW9uO1xuICAgICAgICBjaGFuZ2UgPSB0cnVlO1xuICAgICAgfVxuICAgICAgaWYgKGNoYW5nZSAmJiBzb3VyY2UgPT09IHRoaXMuX3NvdXJjZSkge1xuICAgICAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KCk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogUmVjb3JkIGEgc291cmNlIHZlcnNpb24gd2Ugbm90aWZpZWQgdGhlIHVzZXIgYWJvdXQuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gc291cmNlIC0gVGhlIG5hbWUgb2YgdGhlIGxvZyBzb3VyY2UuXG4gICAgICogQHBhcmFtIHZlcnNpb24gLSBUaGUgdmVyc2lvbiBvZiB0aGUgbG9nLlxuICAgICAqL1xuICAgIHNvdXJjZU5vdGlmaWVkKHNvdXJjZTogc3RyaW5nIHwgbnVsbCwgdmVyc2lvbjogbnVtYmVyKTogdm9pZCB7XG4gICAgICBpZiAoc291cmNlID09PSBudWxsKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHZlcnNpb25zID0gdGhpcy5fc291cmNlVmVyc2lvbi5nZXQoc291cmNlKTtcbiAgICAgIGlmICh2ZXJzaW9ucyEubGFzdE5vdGlmaWVkIDwgdmVyc2lvbikge1xuICAgICAgICB2ZXJzaW9ucyEubGFzdE5vdGlmaWVkID0gdmVyc2lvbjtcbiAgICAgICAgaWYgKHNvdXJjZSA9PT0gdGhpcy5fc291cmNlKSB7XG4gICAgICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuXG4gICAgcHJpdmF0ZSBfaGFuZGxlTG9nUmVnaXN0cnlDaGFuZ2UoKSB7XG4gICAgICBjb25zdCBsb2dnZXJzID0gdGhpcy5fbG9nZ2VyUmVnaXN0cnkuZ2V0TG9nZ2VycygpO1xuICAgICAgZm9yIChjb25zdCBsb2dnZXIgb2YgbG9nZ2Vycykge1xuICAgICAgICBpZiAoIXRoaXMuX3NvdXJjZVZlcnNpb24uaGFzKGxvZ2dlci5zb3VyY2UpKSB7XG4gICAgICAgICAgbG9nZ2VyLmNvbnRlbnRDaGFuZ2VkLmNvbm5lY3QodGhpcy5faGFuZGxlTG9nQ29udGVudENoYW5nZSwgdGhpcyk7XG4gICAgICAgICAgdGhpcy5fc291cmNlVmVyc2lvbi5zZXQobG9nZ2VyLnNvdXJjZSwge1xuICAgICAgICAgICAgbGFzdERpc3BsYXllZDogMCxcbiAgICAgICAgICAgIGxhc3ROb3RpZmllZDogMFxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuXG4gICAgcHJpdmF0ZSBfaGFuZGxlTG9nQ29udGVudENoYW5nZShcbiAgICAgIHsgc291cmNlIH06IElMb2dnZXIsXG4gICAgICBjaGFuZ2U6IElDb250ZW50Q2hhbmdlXG4gICAgKSB7XG4gICAgICBpZiAoc291cmNlID09PSB0aGlzLl9zb3VyY2UpIHtcbiAgICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgICAgfVxuICAgIH1cblxuICAgIC8qKlxuICAgICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgZmxhc2ggZW5hYmxlbWVudCBjaGFuZ2VzLlxuICAgICAqL1xuICAgIHB1YmxpYyBmbGFzaEVuYWJsZWRDaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCB2b2lkPih0aGlzKTtcbiAgICBwcml2YXRlIF9mbGFzaEVuYWJsZWQ6IGJvb2xlYW4gPSB0cnVlO1xuICAgIHByaXZhdGUgX2xvZ2dlclJlZ2lzdHJ5OiBJTG9nZ2VyUmVnaXN0cnk7XG4gICAgcHJpdmF0ZSBfc291cmNlOiBzdHJpbmcgfCBudWxsID0gbnVsbDtcbiAgICAvKipcbiAgICAgKiBUaGUgdmlldyBzdGF0dXMgb2YgZWFjaCBzb3VyY2UuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogS2V5cyBhcmUgc291cmNlIG5hbWVzLCB2YWx1ZSBpcyBhIGxpc3Qgb2YgdHdvIG51bWJlcnMuIFRoZSBmaXJzdFxuICAgICAqIHJlcHJlc2VudHMgdGhlIHZlcnNpb24gb2YgdGhlIG1lc3NhZ2VzIHRoYXQgd2FzIGxhc3QgZGlzcGxheWVkIHRvIHRoZVxuICAgICAqIHVzZXIsIHRoZSBzZWNvbmQgcmVwcmVzZW50cyB0aGUgdmVyc2lvbiB0aGF0IHdlIGxhc3Qgbm90aWZpZWQgdGhlIHVzZXJcbiAgICAgKiBhYm91dC5cbiAgICAgKi9cbiAgICBwcml2YXRlIF9zb3VyY2VWZXJzaW9uOiBNYXA8c3RyaW5nLCBJVmVyc2lvbkluZm8+ID0gbmV3IE1hcCgpO1xuICB9XG5cbiAgaW50ZXJmYWNlIElWZXJzaW9uSW5mbyB7XG4gICAgbGFzdERpc3BsYXllZDogbnVtYmVyO1xuICAgIGxhc3ROb3RpZmllZDogbnVtYmVyO1xuICB9XG5cbiAgLyoqXG4gICAqIE9wdGlvbnMgZm9yIGNyZWF0aW5nIGEgbmV3IExvZ0NvbnNvbGVTdGF0dXMgaXRlbVxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGxvZ2dlciByZWdpc3RyeSBwcm92aWRpbmcgdGhlIGxvZ3MuXG4gICAgICovXG4gICAgbG9nZ2VyUmVnaXN0cnk6IElMb2dnZXJSZWdpc3RyeTtcblxuICAgIC8qKlxuICAgICAqIEEgY2xpY2sgaGFuZGxlciBmb3IgdGhlIGl0ZW0uIEJ5IGRlZmF1bHRcbiAgICAgKiBMb2cgQ29uc29sZSBwYW5lbCBpcyBsYXVuY2hlZC5cbiAgICAgKi9cbiAgICBoYW5kbGVDbGljazogKCkgPT4gdm9pZDtcblxuICAgIC8qKlxuICAgICAqIExhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAgICovXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=