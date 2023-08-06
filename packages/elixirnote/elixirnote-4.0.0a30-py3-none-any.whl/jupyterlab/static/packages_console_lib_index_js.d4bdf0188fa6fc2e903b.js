"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_console_lib_index_js"],{

/***/ "../../packages/console/lib/foreign.js":
/*!*********************************************!*\
  !*** ../../packages/console/lib/foreign.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ForeignHandler": () => (/* binding */ ForeignHandler)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

const FOREIGN_CELL_CLASS = 'jp-CodeConsole-foreignCell';
/**
 * A handler for capturing API messages from other sessions that should be
 * rendered in a given parent.
 */
class ForeignHandler {
    /**
     * Construct a new foreign message handler.
     */
    constructor(options) {
        this._enabled = false;
        this._isDisposed = false;
        this.sessionContext = options.sessionContext;
        this.sessionContext.iopubMessage.connect(this.onIOPubMessage, this);
        this._parent = options.parent;
    }
    /**
     * Set whether the handler is able to inject foreign cells into a console.
     */
    get enabled() {
        return this._enabled;
    }
    set enabled(value) {
        this._enabled = value;
    }
    /**
     * The foreign handler's parent receiver.
     */
    get parent() {
        return this._parent;
    }
    /**
     * Test whether the handler is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose the resources held by the handler.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal.clearData(this);
    }
    /**
     * Handler IOPub messages.
     *
     * @returns `true` if the message resulted in a new cell injection or a
     * previously injected cell being updated and `false` for all other messages.
     */
    onIOPubMessage(sender, msg) {
        var _a;
        // Only process messages if foreign cell injection is enabled.
        if (!this._enabled) {
            return false;
        }
        const kernel = (_a = this.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if (!kernel) {
            return false;
        }
        // Check whether this message came from an external session.
        const parent = this._parent;
        const session = msg.parent_header.session;
        if (session === kernel.clientId) {
            return false;
        }
        const msgType = msg.header.msg_type;
        const parentHeader = msg.parent_header;
        const parentMsgId = parentHeader.msg_id;
        let cell;
        switch (msgType) {
            case 'execute_input': {
                const inputMsg = msg;
                cell = this._newCell(parentMsgId);
                const model = cell.model;
                model.executionCount = inputMsg.content.execution_count;
                model.value.text = inputMsg.content.code;
                model.trusted = true;
                parent.update();
                return true;
            }
            case 'execute_result':
            case 'display_data':
            case 'stream':
            case 'error': {
                cell = this._parent.getCell(parentMsgId);
                if (!cell) {
                    return false;
                }
                const output = Object.assign(Object.assign({}, msg.content), { output_type: msgType });
                cell.model.outputs.add(output);
                parent.update();
                return true;
            }
            case 'clear_output': {
                const wait = msg.content.wait;
                cell = this._parent.getCell(parentMsgId);
                if (cell) {
                    cell.model.outputs.clear(wait);
                }
                return true;
            }
            default:
                return false;
        }
    }
    /**
     * Create a new code cell for an input originated from a foreign session.
     */
    _newCell(parentMsgId) {
        const cell = this.parent.createCodeCell();
        cell.addClass(FOREIGN_CELL_CLASS);
        this._parent.addCell(cell, parentMsgId);
        return cell;
    }
}


/***/ }),

/***/ "../../packages/console/lib/history.js":
/*!*********************************************!*\
  !*** ../../packages/console/lib/history.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ConsoleHistory": () => (/* binding */ ConsoleHistory)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * A console history manager object.
 */
class ConsoleHistory {
    /**
     * Construct a new console history object.
     */
    constructor(options) {
        this._cursor = 0;
        this._hasSession = false;
        this._history = [];
        this._placeholder = '';
        this._setByHistory = false;
        this._isDisposed = false;
        this._editor = null;
        this._filtered = [];
        const { sessionContext } = options;
        if (sessionContext) {
            this.sessionContext = sessionContext;
            void this._handleKernel();
            this.sessionContext.kernelChanged.connect(this._handleKernel, this);
        }
    }
    /**
     * The current editor used by the history manager.
     */
    get editor() {
        return this._editor;
    }
    set editor(value) {
        if (this._editor === value) {
            return;
        }
        const prev = this._editor;
        if (prev) {
            prev.edgeRequested.disconnect(this.onEdgeRequest, this);
            prev.model.value.changed.disconnect(this.onTextChange, this);
        }
        this._editor = value;
        if (value) {
            value.edgeRequested.connect(this.onEdgeRequest, this);
            value.model.value.changed.connect(this.onTextChange, this);
        }
    }
    /**
     * The placeholder text that a history session began with.
     */
    get placeholder() {
        return this._placeholder;
    }
    /**
     * Get whether the console history manager is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources held by the console history manager.
     */
    dispose() {
        this._isDisposed = true;
        this._history.length = 0;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal.clearData(this);
    }
    /**
     * Get the previous item in the console history.
     *
     * @param placeholder - The placeholder string that gets temporarily added
     * to the history only for the duration of one history session. If multiple
     * placeholders are sent within a session, only the first one is accepted.
     *
     * @returns A Promise for console command text or `undefined` if unavailable.
     */
    back(placeholder) {
        if (!this._hasSession) {
            this._hasSession = true;
            this._placeholder = placeholder;
            // Filter the history with the placeholder string.
            this.setFilter(placeholder);
            this._cursor = this._filtered.length - 1;
        }
        --this._cursor;
        this._cursor = Math.max(0, this._cursor);
        const content = this._filtered[this._cursor];
        return Promise.resolve(content);
    }
    /**
     * Get the next item in the console history.
     *
     * @param placeholder - The placeholder string that gets temporarily added
     * to the history only for the duration of one history session. If multiple
     * placeholders are sent within a session, only the first one is accepted.
     *
     * @returns A Promise for console command text or `undefined` if unavailable.
     */
    forward(placeholder) {
        if (!this._hasSession) {
            this._hasSession = true;
            this._placeholder = placeholder;
            // Filter the history with the placeholder string.
            this.setFilter(placeholder);
            this._cursor = this._filtered.length;
        }
        ++this._cursor;
        this._cursor = Math.min(this._filtered.length - 1, this._cursor);
        const content = this._filtered[this._cursor];
        return Promise.resolve(content);
    }
    /**
     * Add a new item to the bottom of history.
     *
     * @param item The item being added to the bottom of history.
     *
     * #### Notes
     * If the item being added is undefined or empty, it is ignored. If the item
     * being added is the same as the last item in history, it is ignored as well
     * so that the console's history will consist of no contiguous repetitions.
     */
    push(item) {
        if (item && item !== this._history[this._history.length - 1]) {
            this._history.push(item);
        }
        this.reset();
    }
    /**
     * Reset the history navigation state, i.e., start a new history session.
     */
    reset() {
        this._cursor = this._history.length;
        this._hasSession = false;
        this._placeholder = '';
    }
    /**
     * Populate the history collection on history reply from a kernel.
     *
     * @param value The kernel message history reply.
     *
     * #### Notes
     * History entries have the shape:
     * [session: number, line: number, input: string]
     * Contiguous duplicates are stripped out of the API response.
     */
    onHistory(value) {
        this._history.length = 0;
        let last = '';
        let current = '';
        if (value.content.status === 'ok') {
            for (let i = 0; i < value.content.history.length; i++) {
                current = value.content.history[i][2];
                if (current !== last) {
                    this._history.push((last = current));
                }
            }
        }
        // Reset the history navigation cursor back to the bottom.
        this._cursor = this._history.length;
    }
    /**
     * Handle a text change signal from the editor.
     */
    onTextChange() {
        if (this._setByHistory) {
            this._setByHistory = false;
            return;
        }
        this.reset();
    }
    /**
     * Handle an edge requested signal.
     */
    onEdgeRequest(editor, location) {
        const model = editor.model;
        const source = model.value.text;
        if (location === 'top' || location === 'topLine') {
            void this.back(source).then(value => {
                if (this.isDisposed || !value) {
                    return;
                }
                if (model.value.text === value) {
                    return;
                }
                this._setByHistory = true;
                model.value.text = value;
                let columnPos = 0;
                columnPos = value.indexOf('\n');
                if (columnPos < 0) {
                    columnPos = value.length;
                }
                editor.setCursorPosition({ line: 0, column: columnPos });
            });
        }
        else {
            void this.forward(source).then(value => {
                if (this.isDisposed) {
                    return;
                }
                const text = value || this.placeholder;
                if (model.value.text === text) {
                    return;
                }
                this._setByHistory = true;
                model.value.text = text;
                const pos = editor.getPositionAt(text.length);
                if (pos) {
                    editor.setCursorPosition(pos);
                }
            });
        }
    }
    /**
     * Handle the current kernel changing.
     */
    async _handleKernel() {
        var _a, _b;
        const kernel = (_b = (_a = this.sessionContext) === null || _a === void 0 ? void 0 : _a.session) === null || _b === void 0 ? void 0 : _b.kernel;
        if (!kernel) {
            this._history.length = 0;
            return;
        }
        return kernel.requestHistory(Private.initialRequest).then(v => {
            this.onHistory(v);
        });
    }
    /**
     * Set the filter data.
     *
     * @param filterStr - The string to use when filtering the data.
     */
    setFilter(filterStr = '') {
        // Apply the new filter and remove contiguous duplicates.
        this._filtered.length = 0;
        let last = '';
        let current = '';
        for (let i = 0; i < this._history.length; i++) {
            current = this._history[i];
            if (current !== last &&
                filterStr === current.slice(0, filterStr.length)) {
                this._filtered.push((last = current));
            }
        }
        this._filtered.push(filterStr);
    }
}
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    Private.initialRequest = {
        output: false,
        raw: true,
        hist_access_type: 'tail',
        n: 500
    };
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/console/lib/index.js":
/*!*******************************************!*\
  !*** ../../packages/console/lib/index.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeConsole": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_4__.CodeConsole),
/* harmony export */   "ConsoleHistory": () => (/* reexport safe */ _history__WEBPACK_IMPORTED_MODULE_1__.ConsoleHistory),
/* harmony export */   "ConsolePanel": () => (/* reexport safe */ _panel__WEBPACK_IMPORTED_MODULE_2__.ConsolePanel),
/* harmony export */   "ForeignHandler": () => (/* reexport safe */ _foreign__WEBPACK_IMPORTED_MODULE_0__.ForeignHandler),
/* harmony export */   "IConsoleTracker": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_3__.IConsoleTracker)
/* harmony export */ });
/* harmony import */ var _foreign__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./foreign */ "../../packages/console/lib/foreign.js");
/* harmony import */ var _history__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./history */ "../../packages/console/lib/history.js");
/* harmony import */ var _panel__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./panel */ "../../packages/console/lib/panel.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./tokens */ "../../packages/console/lib/tokens.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widget */ "../../packages/console/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module console
 */







/***/ }),

/***/ "../../packages/console/lib/panel.js":
/*!*******************************************!*\
  !*** ../../packages/console/lib/panel.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ConsolePanel": () => (/* binding */ ConsolePanel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./widget */ "../../packages/console/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.








/**
 * The class name added to console panels.
 */
const PANEL_CLASS = 'jp-ConsolePanel';
/**
 * A panel which contains a console and the ability to add other children.
 */
class ConsolePanel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget {
    /**
     * Construct a console panel.
     */
    constructor(options) {
        super({ content: new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Panel() });
        this._executed = null;
        this._connected = null;
        this.addClass(PANEL_CLASS);
        let { rendermime, mimeTypeService, path, basePath, name, manager, modelFactory, sessionContext, translator } = options;
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator;
        const trans = this.translator.load('jupyterlab');
        const contentFactory = (this.contentFactory =
            options.contentFactory || ConsolePanel.defaultContentFactory);
        const count = Private.count++;
        if (!path) {
            path = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.URLExt.join(basePath || '', `console-${count}-${_lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__.UUID.uuid4()}`);
        }
        sessionContext = this._sessionContext =
            sessionContext ||
                new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.SessionContext({
                    sessionManager: manager.sessions,
                    specsManager: manager.kernelspecs,
                    path,
                    name: name || trans.__('Console %1', count),
                    type: 'console',
                    kernelPreference: options.kernelPreference,
                    setBusy: options.setBusy
                });
        const resolver = new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.RenderMimeRegistry.UrlResolver({
            session: sessionContext,
            contents: manager.contents
        });
        rendermime = rendermime.clone({ resolver });
        this.console = contentFactory.createConsole({
            rendermime,
            sessionContext: sessionContext,
            mimeTypeService,
            contentFactory,
            modelFactory
        });
        this.content.addWidget(this.console);
        void sessionContext.initialize().then(async (value) => {
            if (value) {
                await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.sessionContextDialogs.selectKernel(sessionContext);
            }
            this._connected = new Date();
            this._updateTitlePanel();
        });
        this.console.executed.connect(this._onExecuted, this);
        this._updateTitlePanel();
        sessionContext.kernelChanged.connect(this._updateTitlePanel, this);
        sessionContext.propertyChanged.connect(this._updateTitlePanel, this);
        this.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.consoleIcon;
        this.title.closable = true;
        this.id = `console-${count}`;
    }
    /**
     * The session used by the panel.
     */
    get sessionContext() {
        return this._sessionContext;
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        this.sessionContext.dispose();
        this.console.dispose();
        super.dispose();
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        const prompt = this.console.promptCell;
        if (prompt) {
            prompt.editor.focus();
        }
    }
    /**
     * Handle `'close-request'` messages.
     */
    onCloseRequest(msg) {
        super.onCloseRequest(msg);
        this.dispose();
    }
    /**
     * Handle a console execution.
     */
    _onExecuted(sender, args) {
        this._executed = args;
        this._updateTitlePanel();
    }
    /**
     * Update the console panel title.
     */
    _updateTitlePanel() {
        Private.updateTitle(this, this._connected, this._executed, this.translator);
    }
}
/**
 * A namespace for ConsolePanel statics.
 */
(function (ConsolePanel) {
    /**
     * Default implementation of `IContentFactory`.
     */
    class ContentFactory extends _widget__WEBPACK_IMPORTED_MODULE_7__.CodeConsole.ContentFactory {
        /**
         * Create a new console panel.
         */
        createConsole(options) {
            return new _widget__WEBPACK_IMPORTED_MODULE_7__.CodeConsole(options);
        }
    }
    ConsolePanel.ContentFactory = ContentFactory;
    /**
     * A default code console content factory.
     */
    ConsolePanel.defaultContentFactory = new ContentFactory();
    /**
     * The console renderer token.
     */
    ConsolePanel.IContentFactory = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__.Token('@jupyterlab/console:IContentFactory');
})(ConsolePanel || (ConsolePanel = {}));
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * The counter for new consoles.
     */
    Private.count = 1;
    /**
     * Update the title of a console panel.
     */
    function updateTitle(panel, connected, executed, translator) {
        translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator;
        const trans = translator.load('jupyterlab');
        const sessionContext = panel.console.sessionContext.session;
        if (sessionContext) {
            // FIXME:
            let caption = trans.__('Name: %1\n', sessionContext.name) +
                trans.__('Directory: %1\n', _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.PathExt.dirname(sessionContext.path)) +
                trans.__('Kernel: %1', panel.console.sessionContext.kernelDisplayName);
            if (connected) {
                caption += trans.__('\nConnected: %1', _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.Time.format(connected.toISOString()));
            }
            if (executed) {
                caption += trans.__('\nLast Execution: %1');
            }
            panel.title.label = sessionContext.name;
            panel.title.caption = caption;
        }
        else {
            panel.title.label = trans.__('Console');
            panel.title.caption = '';
        }
    }
    Private.updateTitle = updateTitle;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/console/lib/tokens.js":
/*!********************************************!*\
  !*** ../../packages/console/lib/tokens.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IConsoleTracker": () => (/* binding */ IConsoleTracker)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The console tracker token.
 */
const IConsoleTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/console:IConsoleTracker');


/***/ }),

/***/ "../../packages/console/lib/widget.js":
/*!********************************************!*\
  !*** ../../packages/console/lib/widget.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeConsole": () => (/* binding */ CodeConsole)
/* harmony export */ });
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/cells */ "webpack/sharing/consume/default/@jupyterlab/cells/@jupyterlab/cells");
/* harmony import */ var _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_dragdrop__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/dragdrop */ "webpack/sharing/consume/default/@lumino/dragdrop/@lumino/dragdrop");
/* harmony import */ var _lumino_dragdrop__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_dragdrop__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _history__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./history */ "../../packages/console/lib/history.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.








/**
 * The data attribute added to a widget that has an active kernel.
 */
const KERNEL_USER = 'jpKernelUser';
/**
 * The data attribute added to a widget can run code.
 */
const CODE_RUNNER = 'jpCodeRunner';
/**
 * The class name added to console widgets.
 */
const CONSOLE_CLASS = 'jp-CodeConsole';
/**
 * The class added to console cells
 */
const CONSOLE_CELL_CLASS = 'jp-Console-cell';
/**
 * The class name added to the console banner.
 */
const BANNER_CLASS = 'jp-CodeConsole-banner';
/**
 * The class name of the active prompt cell.
 */
const PROMPT_CLASS = 'jp-CodeConsole-promptCell';
/**
 * The class name of the panel that holds cell content.
 */
const CONTENT_CLASS = 'jp-CodeConsole-content';
/**
 * The class name of the panel that holds prompts.
 */
const INPUT_CLASS = 'jp-CodeConsole-input';
/**
 * The timeout in ms for execution requests to the kernel.
 */
const EXECUTION_TIMEOUT = 250;
/**
 * The mimetype used for Jupyter cell data.
 */
const JUPYTER_CELL_MIME = 'application/vnd.jupyter.cells';
/**
 * A widget containing a Jupyter console.
 *
 * #### Notes
 * The CodeConsole class is intended to be used within a ConsolePanel
 * instance. Under most circumstances, it is not instantiated by user code.
 */
class CodeConsole extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
    /**
     * Construct a console widget.
     */
    constructor(options) {
        super();
        this._banner = null;
        this._executed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        this._mimetype = 'text/x-ipython';
        this._msgIds = new Map();
        this._msgIdCells = new Map();
        this._promptCellCreated = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        this._dragData = null;
        this._drag = null;
        this._focusedCell = null;
        this.addClass(CONSOLE_CLASS);
        this.node.dataset[KERNEL_USER] = 'true';
        this.node.dataset[CODE_RUNNER] = 'true';
        this.node.tabIndex = -1; // Allow the widget to take focus.
        // Create the panels that hold the content and input.
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.PanelLayout());
        this._cells = new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__.ObservableList();
        this._content = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Panel();
        this._input = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Panel();
        this.contentFactory =
            options.contentFactory || CodeConsole.defaultContentFactory;
        this.modelFactory = options.modelFactory || CodeConsole.defaultModelFactory;
        this.rendermime = options.rendermime;
        this.sessionContext = options.sessionContext;
        this._mimeTypeService = options.mimeTypeService;
        // Add top-level CSS classes.
        this._content.addClass(CONTENT_CLASS);
        this._input.addClass(INPUT_CLASS);
        // Insert the content and input panes into the widget.
        layout.addWidget(this._content);
        layout.addWidget(this._input);
        this._history = new _history__WEBPACK_IMPORTED_MODULE_7__.ConsoleHistory({
            sessionContext: this.sessionContext
        });
        void this._onKernelChanged();
        this.sessionContext.kernelChanged.connect(this._onKernelChanged, this);
        this.sessionContext.statusChanged.connect(this._onKernelStatusChanged, this);
    }
    /**
     * A signal emitted when the console finished executing its prompt cell.
     */
    get executed() {
        return this._executed;
    }
    /**
     * A signal emitted when a new prompt cell is created.
     */
    get promptCellCreated() {
        return this._promptCellCreated;
    }
    /**
     * The list of content cells in the console.
     *
     * #### Notes
     * This list does not include the current banner or the prompt for a console.
     * It may include previous banners as raw cells.
     */
    get cells() {
        return this._cells;
    }
    /*
     * The console input prompt cell.
     */
    get promptCell() {
        const inputLayout = this._input.layout;
        return inputLayout.widgets[0] || null;
    }
    /**
     * Add a new cell to the content panel.
     *
     * @param cell - The code cell widget being added to the content panel.
     *
     * @param msgId - The optional execution message id for the cell.
     *
     * #### Notes
     * This method is meant for use by outside classes that want to add cells to a
     * console. It is distinct from the `inject` method in that it requires
     * rendered code cell widgets and does not execute them (though it can store
     * the execution message id).
     */
    addCell(cell, msgId) {
        cell.addClass(CONSOLE_CELL_CLASS);
        this._content.addWidget(cell);
        this._cells.push(cell);
        if (msgId) {
            this._msgIds.set(msgId, cell);
            this._msgIdCells.set(cell, msgId);
        }
        cell.disposed.connect(this._onCellDisposed, this);
        this.update();
    }
    /**
     * Add a banner cell.
     */
    addBanner() {
        if (this._banner) {
            // An old banner just becomes a normal cell now.
            const cell = this._banner;
            this._cells.push(this._banner);
            cell.disposed.connect(this._onCellDisposed, this);
        }
        // Create the banner.
        const model = this.modelFactory.createRawCell({});
        model.value.text = '...';
        const banner = (this._banner = new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.RawCell({
            model,
            contentFactory: this.contentFactory,
            placeholder: false
        })).initializeState();
        banner.addClass(BANNER_CLASS);
        banner.readOnly = true;
        this._content.addWidget(banner);
    }
    /**
     * Clear the code cells.
     */
    clear() {
        // Dispose all the content cells
        const cells = this._cells;
        while (cells.length > 0) {
            cells.get(0).dispose();
        }
    }
    /**
     * Create a new cell with the built-in factory.
     */
    createCodeCell() {
        const factory = this.contentFactory;
        const options = this._createCodeCellOptions();
        const cell = factory.createCodeCell(options);
        cell.readOnly = true;
        cell.model.mimeType = this._mimetype;
        return cell;
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        // Do nothing if already disposed.
        if (this.isDisposed) {
            return;
        }
        this._cells.clear();
        this._msgIdCells = null;
        this._msgIds = null;
        this._history.dispose();
        super.dispose();
    }
    /**
     * Execute the current prompt.
     *
     * @param force - Whether to force execution without checking code
     * completeness.
     *
     * @param timeout - The length of time, in milliseconds, that the execution
     * should wait for the API to determine whether code being submitted is
     * incomplete before attempting submission anyway. The default value is `250`.
     */
    async execute(force = false, timeout = EXECUTION_TIMEOUT) {
        var _a, _b;
        if (((_b = (_a = this.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) === null || _b === void 0 ? void 0 : _b.status) === 'dead') {
            return;
        }
        const promptCell = this.promptCell;
        if (!promptCell) {
            throw new Error('Cannot execute without a prompt cell');
        }
        promptCell.model.trusted = true;
        if (force) {
            // Create a new prompt cell before kernel execution to allow typeahead.
            this.newPromptCell();
            await this._execute(promptCell);
            return;
        }
        // Check whether we should execute.
        const shouldExecute = await this._shouldExecute(timeout);
        if (this.isDisposed) {
            return;
        }
        if (shouldExecute) {
            // Create a new prompt cell before kernel execution to allow typeahead.
            this.newPromptCell();
            this.promptCell.editor.focus();
            await this._execute(promptCell);
        }
        else {
            // add a newline if we shouldn't execute
            promptCell.editor.newIndentedLine();
        }
    }
    /**
     * Get a cell given a message id.
     *
     * @param msgId - The message id.
     */
    getCell(msgId) {
        return this._msgIds.get(msgId);
    }
    /**
     * Inject arbitrary code for the console to execute immediately.
     *
     * @param code - The code contents of the cell being injected.
     *
     * @returns A promise that indicates when the injected cell's execution ends.
     */
    inject(code, metadata = {}) {
        const cell = this.createCodeCell();
        cell.model.value.text = code;
        for (const key of Object.keys(metadata)) {
            cell.model.metadata.set(key, metadata[key]);
        }
        this.addCell(cell);
        return this._execute(cell);
    }
    /**
     * Insert a line break in the prompt cell.
     */
    insertLinebreak() {
        const promptCell = this.promptCell;
        if (!promptCell) {
            return;
        }
        promptCell.editor.newIndentedLine();
    }
    /**
     * Replaces the selected text in the prompt cell.
     *
     * @param text - The text to replace the selection.
     */
    replaceSelection(text) {
        var _a, _b;
        const promptCell = this.promptCell;
        if (!promptCell) {
            return;
        }
        (_b = (_a = promptCell.editor).replaceSelection) === null || _b === void 0 ? void 0 : _b.call(_a, text);
    }
    /**
     * Serialize the output.
     *
     * #### Notes
     * This only serializes the code cells and the prompt cell if it exists, and
     * skips any old banner cells.
     */
    serialize() {
        const cells = [];
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.each)(this._cells, cell => {
            const model = cell.model;
            if ((0,_jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.isCodeCellModel)(model)) {
                cells.push(model.toJSON());
            }
        });
        if (this.promptCell) {
            cells.push(this.promptCell.model.toJSON());
        }
        return cells;
    }
    /**
     * Handle `mousedown` events for the widget.
     */
    _evtMouseDown(event) {
        const { button, shiftKey } = event;
        // We only handle main or secondary button actions.
        if (!(button === 0 || button === 2) ||
            // Shift right-click gives the browser default behavior.
            (shiftKey && button === 2)) {
            return;
        }
        let target = event.target;
        const cellFilter = (node) => node.classList.contains(CONSOLE_CELL_CLASS);
        let cellIndex = _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CellDragUtils.findCell(target, this._cells, cellFilter);
        if (cellIndex === -1) {
            // `event.target` sometimes gives an orphaned node in
            // Firefox 57, which can have `null` anywhere in its parent line. If we fail
            // to find a cell using `event.target`, try again using a target
            // reconstructed from the position of the click event.
            target = document.elementFromPoint(event.clientX, event.clientY);
            cellIndex = _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CellDragUtils.findCell(target, this._cells, cellFilter);
        }
        if (cellIndex === -1) {
            return;
        }
        const cell = this._cells.get(cellIndex);
        const targetArea = _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CellDragUtils.detectTargetArea(cell, event.target);
        if (targetArea === 'prompt') {
            this._dragData = {
                pressX: event.clientX,
                pressY: event.clientY,
                index: cellIndex
            };
            this._focusedCell = cell;
            document.addEventListener('mouseup', this, true);
            document.addEventListener('mousemove', this, true);
            event.preventDefault();
        }
    }
    /**
     * Handle `mousemove` event of widget
     */
    _evtMouseMove(event) {
        const data = this._dragData;
        if (data &&
            _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CellDragUtils.shouldStartDrag(data.pressX, data.pressY, event.clientX, event.clientY)) {
            void this._startDrag(data.index, event.clientX, event.clientY);
        }
    }
    /**
     * Start a drag event
     */
    _startDrag(index, clientX, clientY) {
        const cellModel = this._focusedCell.model;
        const selected = [cellModel.toJSON()];
        const dragImage = _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CellDragUtils.createCellDragImage(this._focusedCell, selected);
        this._drag = new _lumino_dragdrop__WEBPACK_IMPORTED_MODULE_4__.Drag({
            mimeData: new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__.MimeData(),
            dragImage,
            proposedAction: 'copy',
            supportedActions: 'copy',
            source: this
        });
        this._drag.mimeData.setData(JUPYTER_CELL_MIME, selected);
        const textContent = cellModel.value.text;
        this._drag.mimeData.setData('text/plain', textContent);
        this._focusedCell = null;
        document.removeEventListener('mousemove', this, true);
        document.removeEventListener('mouseup', this, true);
        return this._drag.start(clientX, clientY).then(() => {
            if (this.isDisposed) {
                return;
            }
            this._drag = null;
            this._dragData = null;
        });
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event -The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the notebook panel's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        switch (event.type) {
            case 'keydown':
                this._evtKeyDown(event);
                break;
            case 'mousedown':
                this._evtMouseDown(event);
                break;
            case 'mousemove':
                this._evtMouseMove(event);
                break;
            case 'mouseup':
                this._evtMouseUp(event);
                break;
            default:
                break;
        }
    }
    /**
     * Handle `after_attach` messages for the widget.
     */
    onAfterAttach(msg) {
        const node = this.node;
        node.addEventListener('keydown', this, true);
        node.addEventListener('click', this);
        node.addEventListener('mousedown', this);
        // Create a prompt if necessary.
        if (!this.promptCell) {
            this.newPromptCell();
        }
        else {
            this.promptCell.editor.focus();
            this.update();
        }
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        const node = this.node;
        node.removeEventListener('keydown', this, true);
        node.removeEventListener('click', this);
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        const editor = this.promptCell && this.promptCell.editor;
        if (editor) {
            editor.focus();
        }
        this.update();
    }
    /**
     * Make a new prompt cell.
     */
    newPromptCell() {
        let promptCell = this.promptCell;
        const input = this._input;
        // Make the last prompt read-only, clear its signals, and move to content.
        if (promptCell) {
            promptCell.readOnly = true;
            promptCell.removeClass(PROMPT_CLASS);
            _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal.clearData(promptCell.editor);
            const child = input.widgets[0];
            child.parent = null;
            this.addCell(promptCell);
        }
        // Create the new prompt cell.
        const factory = this.contentFactory;
        const options = this._createCodeCellOptions();
        promptCell = factory.createCodeCell(options);
        promptCell.model.mimeType = this._mimetype;
        promptCell.addClass(PROMPT_CLASS);
        // Add the prompt cell to the DOM, making `this.promptCell` valid again.
        this._input.addWidget(promptCell);
        // Suppress the default "Enter" key handling.
        const editor = promptCell.editor;
        editor.addKeydownHandler(this._onEditorKeydown);
        this._history.editor = editor;
        this._promptCellCreated.emit(promptCell);
    }
    /**
     * Handle `update-request` messages.
     */
    onUpdateRequest(msg) {
        Private.scrollToBottom(this._content.node);
    }
    /**
     * Handle the `'keydown'` event for the widget.
     */
    _evtKeyDown(event) {
        const editor = this.promptCell && this.promptCell.editor;
        if (!editor) {
            return;
        }
        if (event.keyCode === 13 && !editor.hasFocus()) {
            event.preventDefault();
            editor.focus();
        }
        else if (event.keyCode === 27 && editor.hasFocus()) {
            // Set to command mode
            event.preventDefault();
            event.stopPropagation();
            this.node.focus();
        }
    }
    /**
     * Handle the `'mouseup'` event for the widget.
     */
    _evtMouseUp(event) {
        if (this.promptCell &&
            this.promptCell.node.contains(event.target)) {
            this.promptCell.editor.focus();
        }
    }
    /**
     * Execute the code in the current prompt cell.
     */
    _execute(cell) {
        const source = cell.model.value.text;
        this._history.push(source);
        // If the source of the console is just "clear", clear the console as we
        // do in IPython or QtConsole.
        if (source === 'clear' || source === '%clear') {
            this.clear();
            return Promise.resolve(void 0);
        }
        cell.model.contentChanged.connect(this.update, this);
        const onSuccess = (value) => {
            if (this.isDisposed) {
                return;
            }
            if (value && value.content.status === 'ok') {
                const content = value.content;
                // Use deprecated payloads for backwards compatibility.
                if (content.payload && content.payload.length) {
                    const setNextInput = content.payload.filter(i => {
                        return i.source === 'set_next_input';
                    })[0];
                    if (setNextInput) {
                        const text = setNextInput.text;
                        // Ignore the `replace` value and always set the next cell.
                        cell.model.value.text = text;
                    }
                }
            }
            else if (value && value.content.status === 'error') {
                (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.each)(this._cells, (cell) => {
                    if (cell.model.executionCount === null) {
                        cell.setPrompt('');
                    }
                });
            }
            cell.model.contentChanged.disconnect(this.update, this);
            this.update();
            this._executed.emit(new Date());
        };
        const onFailure = () => {
            if (this.isDisposed) {
                return;
            }
            cell.model.contentChanged.disconnect(this.update, this);
            this.update();
        };
        return _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CodeCell.execute(cell, this.sessionContext).then(onSuccess, onFailure);
    }
    /**
     * Update the console based on the kernel info.
     */
    _handleInfo(info) {
        if (info.status !== 'ok') {
            this._banner.model.value.text = 'Error in getting kernel banner';
            return;
        }
        this._banner.model.value.text = info.banner;
        const lang = info.language_info;
        this._mimetype = this._mimeTypeService.getMimeTypeByLanguage(lang);
        if (this.promptCell) {
            this.promptCell.model.mimeType = this._mimetype;
        }
    }
    /**
     * Create the options used to initialize a code cell widget.
     */
    _createCodeCellOptions() {
        const contentFactory = this.contentFactory;
        const modelFactory = this.modelFactory;
        const model = modelFactory.createCodeCell({});
        const rendermime = this.rendermime;
        const editorConfig = this.editorConfig;
        return {
            model,
            rendermime,
            contentFactory,
            editorConfig,
            placeholder: false
        };
    }
    /**
     * Handle cell disposed signals.
     */
    _onCellDisposed(sender, args) {
        if (!this.isDisposed) {
            this._cells.removeValue(sender);
            const msgId = this._msgIdCells.get(sender);
            if (msgId) {
                this._msgIdCells.delete(sender);
                this._msgIds.delete(msgId);
            }
        }
    }
    /**
     * Test whether we should execute the prompt cell.
     */
    _shouldExecute(timeout) {
        const promptCell = this.promptCell;
        if (!promptCell) {
            return Promise.resolve(false);
        }
        const model = promptCell.model;
        const code = model.value.text;
        return new Promise((resolve, reject) => {
            var _a;
            const timer = setTimeout(() => {
                resolve(true);
            }, timeout);
            const kernel = (_a = this.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
            if (!kernel) {
                resolve(false);
                return;
            }
            kernel
                .requestIsComplete({ code })
                .then(isComplete => {
                clearTimeout(timer);
                if (this.isDisposed) {
                    resolve(false);
                }
                if (isComplete.content.status !== 'incomplete') {
                    resolve(true);
                    return;
                }
                resolve(false);
            })
                .catch(() => {
                resolve(true);
            });
        });
    }
    /**
     * Handle a keydown event on an editor.
     */
    _onEditorKeydown(editor, event) {
        // Suppress "Enter" events.
        return event.keyCode === 13;
    }
    /**
     * Handle a change to the kernel.
     */
    async _onKernelChanged() {
        var _a;
        this.clear();
        if (this._banner) {
            this._banner.dispose();
            this._banner = null;
        }
        this.addBanner();
        if ((_a = this.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel) {
            this._handleInfo(await this.sessionContext.session.kernel.info);
        }
    }
    /**
     * Handle a change to the kernel status.
     */
    async _onKernelStatusChanged() {
        var _a;
        const kernel = (_a = this.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if ((kernel === null || kernel === void 0 ? void 0 : kernel.status) === 'restarting') {
            this.addBanner();
            this._handleInfo(await (kernel === null || kernel === void 0 ? void 0 : kernel.info));
        }
    }
}
/**
 * A namespace for CodeConsole statics.
 */
(function (CodeConsole) {
    /**
     * Default implementation of `IContentFactory`.
     */
    class ContentFactory extends _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.Cell.ContentFactory {
        /**
         * Create a new code cell widget.
         *
         * #### Notes
         * If no cell content factory is passed in with the options, the one on the
         * notebook content factory is used.
         */
        createCodeCell(options) {
            if (!options.contentFactory) {
                options.contentFactory = this;
            }
            return new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CodeCell(options).initializeState();
        }
        /**
         * Create a new raw cell widget.
         *
         * #### Notes
         * If no cell content factory is passed in with the options, the one on the
         * notebook content factory is used.
         */
        createRawCell(options) {
            if (!options.contentFactory) {
                options.contentFactory = this;
            }
            return new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.RawCell(options).initializeState();
        }
    }
    CodeConsole.ContentFactory = ContentFactory;
    /**
     * A default content factory for the code console.
     */
    CodeConsole.defaultContentFactory = new ContentFactory();
    /**
     * The default implementation of an `IModelFactory`.
     */
    class ModelFactory {
        /**
         * Create a new cell model factory.
         */
        constructor(options = {}) {
            this.codeCellContentFactory =
                options.codeCellContentFactory || _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CodeCellModel.defaultContentFactory;
        }
        /**
         * Create a new code cell.
         *
         * @param source - The data to use for the original source data.
         *
         * @returns A new code cell. If a source cell is provided, the
         *   new cell will be initialized with the data from the source.
         *   If the contentFactory is not provided, the instance
         *   `codeCellContentFactory` will be used.
         */
        createCodeCell(options) {
            if (!options.contentFactory) {
                options.contentFactory = this.codeCellContentFactory;
            }
            return new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.CodeCellModel(options);
        }
        /**
         * Create a new raw cell.
         *
         * @param source - The data to use for the original source data.
         *
         * @returns A new raw cell. If a source cell is provided, the
         *   new cell will be initialized with the data from the source.
         */
        createRawCell(options) {
            return new _jupyterlab_cells__WEBPACK_IMPORTED_MODULE_0__.RawCellModel(options);
        }
    }
    CodeConsole.ModelFactory = ModelFactory;
    /**
     * The default `ModelFactory` instance.
     */
    CodeConsole.defaultModelFactory = new ModelFactory({});
})(CodeConsole || (CodeConsole = {}));
/**
 * A namespace for console widget private data.
 */
var Private;
(function (Private) {
    /**
     * Jump to the bottom of a node.
     *
     * @param node - The scrollable element.
     */
    function scrollToBottom(node) {
        node.scrollTop = node.scrollHeight - node.clientHeight;
    }
    Private.scrollToBottom = scrollToBottom;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29uc29sZV9saWJfaW5kZXhfanMuZDRiZGYwMTg4ZmE2ZmMyZTkwM2IuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQU9oQjtBQUUzQyxNQUFNLGtCQUFrQixHQUFHLDRCQUE0QixDQUFDO0FBRXhEOzs7R0FHRztBQUNJLE1BQU0sY0FBYztJQUN6Qjs7T0FFRztJQUNILFlBQVksT0FBZ0M7UUE2SHBDLGFBQVEsR0FBRyxLQUFLLENBQUM7UUFFakIsZ0JBQVcsR0FBRyxLQUFLLENBQUM7UUE5SDFCLElBQUksQ0FBQyxjQUFjLEdBQUcsT0FBTyxDQUFDLGNBQWMsQ0FBQztRQUM3QyxJQUFJLENBQUMsY0FBYyxDQUFDLFlBQVksQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGNBQWMsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUNwRSxJQUFJLENBQUMsT0FBTyxHQUFHLE9BQU8sQ0FBQyxNQUFNLENBQUM7SUFDaEMsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxPQUFPO1FBQ1QsT0FBTyxJQUFJLENBQUMsUUFBUSxDQUFDO0lBQ3ZCLENBQUM7SUFDRCxJQUFJLE9BQU8sQ0FBQyxLQUFjO1FBQ3hCLElBQUksQ0FBQyxRQUFRLEdBQUcsS0FBSyxDQUFDO0lBQ3hCLENBQUM7SUFPRDs7T0FFRztJQUNILElBQUksTUFBTTtRQUNSLE9BQU8sSUFBSSxDQUFDLE9BQU8sQ0FBQztJQUN0QixDQUFDO0lBRUQ7O09BRUc7SUFDSCxJQUFJLFVBQVU7UUFDWixPQUFPLElBQUksQ0FBQyxXQUFXLENBQUM7SUFDMUIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsT0FBTztRQUNMLElBQUksSUFBSSxDQUFDLFVBQVUsRUFBRTtZQUNuQixPQUFPO1NBQ1I7UUFDRCxJQUFJLENBQUMsV0FBVyxHQUFHLElBQUksQ0FBQztRQUN4QiwrREFBZ0IsQ0FBQyxJQUFJLENBQUMsQ0FBQztJQUN6QixDQUFDO0lBRUQ7Ozs7O09BS0c7SUFD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Q0FBQztLQUNGO0lBMUNZLHdCQUFZLGVBMEN4QjtJQVlEOztPQUVHO0lBQ1UsK0JBQW1CLEdBQUcsSUFBSSxZQUFZLENBQUMsRUFBRSxDQUFDLENBQUM7QUFDMUQsQ0FBQyxFQTVMZ0IsV0FBVyxLQUFYLFdBQVcsUUE0TDNCO0FBRUQ7O0dBRUc7QUFDSCxJQUFVLE9BQU8sQ0FTaEI7QUFURCxXQUFVLE9BQU87SUFDZjs7OztPQUlHO0lBQ0gsU0FBZ0IsY0FBYyxDQUFDLElBQWlCO1FBQzlDLElBQUksQ0FBQyxTQUFTLEdBQUcsSUFBSSxDQUFDLFlBQVksR0FBRyxJQUFJLENBQUMsWUFBWSxDQUFDO0lBQ3pELENBQUM7SUFGZSxzQkFBYyxpQkFFN0I7QUFDSCxDQUFDLEVBVFMsT0FBTyxLQUFQLE9BQU8sUUFTaEIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29uc29sZS9zcmMvZm9yZWlnbi50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29uc29sZS9zcmMvaGlzdG9yeS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29uc29sZS9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvbnNvbGUvc3JjL3BhbmVsLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb25zb2xlL3NyYy90b2tlbnMudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvbnNvbGUvc3JjL3dpZGdldC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZXNzaW9uQ29udGV4dCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IENvZGVDZWxsIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY2VsbHMnO1xuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuaW1wb3J0IHsgS2VybmVsTWVzc2FnZSB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcblxuY29uc3QgRk9SRUlHTl9DRUxMX0NMQVNTID0gJ2pwLUNvZGVDb25zb2xlLWZvcmVpZ25DZWxsJztcblxuLyoqXG4gKiBBIGhhbmRsZXIgZm9yIGNhcHR1cmluZyBBUEkgbWVzc2FnZXMgZnJvbSBvdGhlciBzZXNzaW9ucyB0aGF0IHNob3VsZCBiZVxuICogcmVuZGVyZWQgaW4gYSBnaXZlbiBwYXJlbnQuXG4gKi9cbmV4cG9ydCBjbGFzcyBGb3JlaWduSGFuZGxlciBpbXBsZW1lbnRzIElEaXNwb3NhYmxlIHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBmb3JlaWduIG1lc3NhZ2UgaGFuZGxlci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IEZvcmVpZ25IYW5kbGVyLklPcHRpb25zKSB7XG4gICAgdGhpcy5zZXNzaW9uQ29udGV4dCA9IG9wdGlvbnMuc2Vzc2lvbkNvbnRleHQ7XG4gICAgdGhpcy5zZXNzaW9uQ29udGV4dC5pb3B1Yk1lc3NhZ2UuY29ubmVjdCh0aGlzLm9uSU9QdWJNZXNzYWdlLCB0aGlzKTtcbiAgICB0aGlzLl9wYXJlbnQgPSBvcHRpb25zLnBhcmVudDtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgd2hldGhlciB0aGUgaGFuZGxlciBpcyBhYmxlIHRvIGluamVjdCBmb3JlaWduIGNlbGxzIGludG8gYSBjb25zb2xlLlxuICAgKi9cbiAgZ2V0IGVuYWJsZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2VuYWJsZWQ7XG4gIH1cbiAgc2V0IGVuYWJsZWQodmFsdWU6IGJvb2xlYW4pIHtcbiAgICB0aGlzLl9lbmFibGVkID0gdmFsdWU7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNsaWVudCBzZXNzaW9uIHVzZWQgYnkgdGhlIGZvcmVpZ24gaGFuZGxlci5cbiAgICovXG4gIHJlYWRvbmx5IHNlc3Npb25Db250ZXh0OiBJU2Vzc2lvbkNvbnRleHQ7XG5cbiAgLyoqXG4gICAqIFRoZSBmb3JlaWduIGhhbmRsZXIncyBwYXJlbnQgcmVjZWl2ZXIuXG4gICAqL1xuICBnZXQgcGFyZW50KCk6IEZvcmVpZ25IYW5kbGVyLklSZWNlaXZlciB7XG4gICAgcmV0dXJuIHRoaXMuX3BhcmVudDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUZXN0IHdoZXRoZXIgdGhlIGhhbmRsZXIgaXMgZGlzcG9zZWQuXG4gICAqL1xuICBnZXQgaXNEaXNwb3NlZCgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5faXNEaXNwb3NlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGUgaGFuZGxlci5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICBTaWduYWwuY2xlYXJEYXRhKHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZXIgSU9QdWIgbWVzc2FnZXMuXG4gICAqXG4gICAqIEByZXR1cm5zIGB0cnVlYCBpZiB0aGUgbWVzc2FnZSByZXN1bHRlZCBpbiBhIG5ldyBjZWxsIGluamVjdGlvbiBvciBhXG4gICAqIHByZXZpb3VzbHkgaW5qZWN0ZWQgY2VsbCBiZWluZyB1cGRhdGVkIGFuZCBgZmFsc2VgIGZvciBhbGwgb3RoZXIgbWVzc2FnZXMuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25JT1B1Yk1lc3NhZ2UoXG4gICAgc2VuZGVyOiBJU2Vzc2lvbkNvbnRleHQsXG4gICAgbXNnOiBLZXJuZWxNZXNzYWdlLklJT1B1Yk1lc3NhZ2VcbiAgKTogYm9vbGVhbiB7XG4gICAgLy8gT25seSBwcm9jZXNzIG1lc3NhZ2VzIGlmIGZvcmVpZ24gY2VsbCBpbmplY3Rpb24gaXMgZW5hYmxlZC5cbiAgICBpZiAoIXRoaXMuX2VuYWJsZWQpIHtcbiAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9XG4gICAgY29uc3Qga2VybmVsID0gdGhpcy5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5rZXJuZWw7XG4gICAgaWYgKCFrZXJuZWwpIHtcbiAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9XG5cbiAgICAvLyBDaGVjayB3aGV0aGVyIHRoaXMgbWVzc2FnZSBjYW1lIGZyb20gYW4gZXh0ZXJuYWwgc2Vzc2lvbi5cbiAgICBjb25zdCBwYXJlbnQgPSB0aGlzLl9wYXJlbnQ7XG4gICAgY29uc3Qgc2Vzc2lvbiA9IChtc2cucGFyZW50X2hlYWRlciBhcyBLZXJuZWxNZXNzYWdlLklIZWFkZXIpLnNlc3Npb247XG4gICAgaWYgKHNlc3Npb24gPT09IGtlcm5lbC5jbGllbnRJZCkge1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cbiAgICBjb25zdCBtc2dUeXBlID0gbXNnLmhlYWRlci5tc2dfdHlwZTtcbiAgICBjb25zdCBwYXJlbnRIZWFkZXIgPSBtc2cucGFyZW50X2hlYWRlciBhcyBLZXJuZWxNZXNzYWdlLklIZWFkZXI7XG4gICAgY29uc3QgcGFyZW50TXNnSWQgPSBwYXJlbnRIZWFkZXIubXNnX2lkIGFzIHN0cmluZztcbiAgICBsZXQgY2VsbDogQ29kZUNlbGwgfCB1bmRlZmluZWQ7XG4gICAgc3dpdGNoIChtc2dUeXBlKSB7XG4gICAgICBjYXNlICdleGVjdXRlX2lucHV0Jzoge1xuICAgICAgICBjb25zdCBpbnB1dE1zZyA9IG1zZyBhcyBLZXJuZWxNZXNzYWdlLklFeGVjdXRlSW5wdXRNc2c7XG4gICAgICAgIGNlbGwgPSB0aGlzLl9uZXdDZWxsKHBhcmVudE1zZ0lkKTtcbiAgICAgICAgY29uc3QgbW9kZWwgPSBjZWxsLm1vZGVsO1xuICAgICAgICBtb2RlbC5leGVjdXRpb25Db3VudCA9IGlucHV0TXNnLmNvbnRlbnQuZXhlY3V0aW9uX2NvdW50O1xuICAgICAgICBtb2RlbC52YWx1ZS50ZXh0ID0gaW5wdXRNc2cuY29udGVudC5jb2RlO1xuICAgICAgICBtb2RlbC50cnVzdGVkID0gdHJ1ZTtcbiAgICAgICAgcGFyZW50LnVwZGF0ZSgpO1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cbiAgICAgIGNhc2UgJ2V4ZWN1dGVfcmVzdWx0JzpcbiAgICAgIGNhc2UgJ2Rpc3BsYXlfZGF0YSc6XG4gICAgICBjYXNlICdzdHJlYW0nOlxuICAgICAgY2FzZSAnZXJyb3InOiB7XG4gICAgICAgIGNlbGwgPSB0aGlzLl9wYXJlbnQuZ2V0Q2VsbChwYXJlbnRNc2dJZCk7XG4gICAgICAgIGlmICghY2VsbCkge1xuICAgICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBvdXRwdXQ6IG5iZm9ybWF0LklPdXRwdXQgPSB7XG4gICAgICAgICAgLi4ubXNnLmNvbnRlbnQsXG4gICAgICAgICAgb3V0cHV0X3R5cGU6IG1zZ1R5cGVcbiAgICAgICAgfTtcbiAgICAgICAgY2VsbC5tb2RlbC5vdXRwdXRzLmFkZChvdXRwdXQpO1xuICAgICAgICBwYXJlbnQudXBkYXRlKCk7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfVxuICAgICAgY2FzZSAnY2xlYXJfb3V0cHV0Jzoge1xuICAgICAgICBjb25zdCB3YWl0ID0gKG1zZyBhcyBLZXJuZWxNZXNzYWdlLklDbGVhck91dHB1dE1zZykuY29udGVudC53YWl0O1xuICAgICAgICBjZWxsID0gdGhpcy5fcGFyZW50LmdldENlbGwocGFyZW50TXNnSWQpO1xuICAgICAgICBpZiAoY2VsbCkge1xuICAgICAgICAgIGNlbGwubW9kZWwub3V0cHV0cy5jbGVhcih3YWl0KTtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IGNvZGUgY2VsbCBmb3IgYW4gaW5wdXQgb3JpZ2luYXRlZCBmcm9tIGEgZm9yZWlnbiBzZXNzaW9uLlxuICAgKi9cbiAgcHJpdmF0ZSBfbmV3Q2VsbChwYXJlbnRNc2dJZDogc3RyaW5nKTogQ29kZUNlbGwge1xuICAgIGNvbnN0IGNlbGwgPSB0aGlzLnBhcmVudC5jcmVhdGVDb2RlQ2VsbCgpO1xuICAgIGNlbGwuYWRkQ2xhc3MoRk9SRUlHTl9DRUxMX0NMQVNTKTtcbiAgICB0aGlzLl9wYXJlbnQuYWRkQ2VsbChjZWxsLCBwYXJlbnRNc2dJZCk7XG4gICAgcmV0dXJuIGNlbGw7XG4gIH1cblxuICBwcml2YXRlIF9lbmFibGVkID0gZmFsc2U7XG4gIHByaXZhdGUgX3BhcmVudDogRm9yZWlnbkhhbmRsZXIuSVJlY2VpdmVyO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIGBGb3JlaWduSGFuZGxlcmAgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBGb3JlaWduSGFuZGxlciB7XG4gIC8qKlxuICAgKiBUaGUgaW5zdGFudGlhdGlvbiBvcHRpb25zIGZvciBhIGZvcmVpZ24gaGFuZGxlci5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBjbGllbnQgc2Vzc2lvbiB1c2VkIGJ5IHRoZSBmb3JlaWduIGhhbmRsZXIuXG4gICAgICovXG4gICAgc2Vzc2lvbkNvbnRleHQ6IElTZXNzaW9uQ29udGV4dDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwYXJlbnQgaW50byB3aGljaCB0aGUgaGFuZGxlciB3aWxsIGluamVjdCBjb2RlIGNlbGxzLlxuICAgICAqL1xuICAgIHBhcmVudDogSVJlY2VpdmVyO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcmVjZWl2ZXIgb2YgbmV3bHkgY3JlYXRlZCBmb3JlaWduIGNlbGxzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUmVjZWl2ZXIge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIGNlbGwuXG4gICAgICovXG4gICAgY3JlYXRlQ29kZUNlbGwoKTogQ29kZUNlbGw7XG5cbiAgICAvKipcbiAgICAgKiBBZGQgYSBuZXdseSBjcmVhdGVkIGNlbGwuXG4gICAgICovXG4gICAgYWRkQ2VsbChjZWxsOiBDb2RlQ2VsbCwgbXNnSWQ6IHN0cmluZyk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBUcmlnZ2VyIGEgcmVuZGVyaW5nIHVwZGF0ZSBvbiB0aGUgcmVjZWl2ZXIuXG4gICAgICovXG4gICAgdXBkYXRlKCk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBHZXQgYSBjZWxsIGFzc29jaWF0ZWQgd2l0aCBhIG1lc3NhZ2UgaWQuXG4gICAgICovXG4gICAgZ2V0Q2VsbChtc2dJZDogc3RyaW5nKTogQ29kZUNlbGwgfCB1bmRlZmluZWQ7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVNlc3Npb25Db250ZXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgQ29kZUVkaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0IHsgS2VybmVsTWVzc2FnZSB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IElEaXNwb3NhYmxlIH0gZnJvbSAnQGx1bWluby9kaXNwb3NhYmxlJztcbmltcG9ydCB7IFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcblxuLyoqXG4gKiBUaGUgZGVmaW5pdGlvbiBvZiBhIGNvbnNvbGUgaGlzdG9yeSBtYW5hZ2VyIG9iamVjdC5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJQ29uc29sZUhpc3RvcnkgZXh0ZW5kcyBJRGlzcG9zYWJsZSB7XG4gIC8qKlxuICAgKiBUaGUgc2Vzc2lvbiBjb250ZXh0IHVzZWQgYnkgdGhlIGZvcmVpZ24gaGFuZGxlci5cbiAgICovXG4gIHJlYWRvbmx5IHNlc3Npb25Db250ZXh0OiBJU2Vzc2lvbkNvbnRleHQgfCBudWxsO1xuXG4gIC8qKlxuICAgKiBUaGUgY3VycmVudCBlZGl0b3IgdXNlZCBieSB0aGUgaGlzdG9yeSB3aWRnZXQuXG4gICAqL1xuICBlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvciB8IG51bGw7XG5cbiAgLyoqXG4gICAqIFRoZSBwbGFjZWhvbGRlciB0ZXh0IHRoYXQgYSBoaXN0b3J5IHNlc3Npb24gYmVnYW4gd2l0aC5cbiAgICovXG4gIHJlYWRvbmx5IHBsYWNlaG9sZGVyOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgcHJldmlvdXMgaXRlbSBpbiB0aGUgY29uc29sZSBoaXN0b3J5LlxuICAgKlxuICAgKiBAcGFyYW0gcGxhY2Vob2xkZXIgLSBUaGUgcGxhY2Vob2xkZXIgc3RyaW5nIHRoYXQgZ2V0cyB0ZW1wb3JhcmlseSBhZGRlZFxuICAgKiB0byB0aGUgaGlzdG9yeSBvbmx5IGZvciB0aGUgZHVyYXRpb24gb2Ygb25lIGhpc3Rvcnkgc2Vzc2lvbi4gSWYgbXVsdGlwbGVcbiAgICogcGxhY2Vob2xkZXJzIGFyZSBzZW50IHdpdGhpbiBhIHNlc3Npb24sIG9ubHkgdGhlIGZpcnN0IG9uZSBpcyBhY2NlcHRlZC5cbiAgICpcbiAgICogQHJldHVybnMgQSBQcm9taXNlIGZvciBjb25zb2xlIGNvbW1hbmQgdGV4dCBvciBgdW5kZWZpbmVkYCBpZiB1bmF2YWlsYWJsZS5cbiAgICovXG4gIGJhY2socGxhY2Vob2xkZXI6IHN0cmluZyk6IFByb21pc2U8c3RyaW5nPjtcblxuICAvKipcbiAgICogR2V0IHRoZSBuZXh0IGl0ZW0gaW4gdGhlIGNvbnNvbGUgaGlzdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIHBsYWNlaG9sZGVyIC0gVGhlIHBsYWNlaG9sZGVyIHN0cmluZyB0aGF0IGdldHMgdGVtcG9yYXJpbHkgYWRkZWRcbiAgICogdG8gdGhlIGhpc3Rvcnkgb25seSBmb3IgdGhlIGR1cmF0aW9uIG9mIG9uZSBoaXN0b3J5IHNlc3Npb24uIElmIG11bHRpcGxlXG4gICAqIHBsYWNlaG9sZGVycyBhcmUgc2VudCB3aXRoaW4gYSBzZXNzaW9uLCBvbmx5IHRoZSBmaXJzdCBvbmUgaXMgYWNjZXB0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgUHJvbWlzZSBmb3IgY29uc29sZSBjb21tYW5kIHRleHQgb3IgYHVuZGVmaW5lZGAgaWYgdW5hdmFpbGFibGUuXG4gICAqL1xuICBmb3J3YXJkKHBsYWNlaG9sZGVyOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz47XG5cbiAgLyoqXG4gICAqIEFkZCBhIG5ldyBpdGVtIHRvIHRoZSBib3R0b20gb2YgaGlzdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIGl0ZW0gVGhlIGl0ZW0gYmVpbmcgYWRkZWQgdG8gdGhlIGJvdHRvbSBvZiBoaXN0b3J5LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIElmIHRoZSBpdGVtIGJlaW5nIGFkZGVkIGlzIHVuZGVmaW5lZCBvciBlbXB0eSwgaXQgaXMgaWdub3JlZC4gSWYgdGhlIGl0ZW1cbiAgICogYmVpbmcgYWRkZWQgaXMgdGhlIHNhbWUgYXMgdGhlIGxhc3QgaXRlbSBpbiBoaXN0b3J5LCBpdCBpcyBpZ25vcmVkIGFzIHdlbGxcbiAgICogc28gdGhhdCB0aGUgY29uc29sZSdzIGhpc3Rvcnkgd2lsbCBjb25zaXN0IG9mIG5vIGNvbnRpZ3VvdXMgcmVwZXRpdGlvbnMuXG4gICAqL1xuICBwdXNoKGl0ZW06IHN0cmluZyk6IHZvaWQ7XG5cbiAgLyoqXG4gICAqIFJlc2V0IHRoZSBoaXN0b3J5IG5hdmlnYXRpb24gc3RhdGUsIGkuZS4sIHN0YXJ0IGEgbmV3IGhpc3Rvcnkgc2Vzc2lvbi5cbiAgICovXG4gIHJlc2V0KCk6IHZvaWQ7XG59XG5cbi8qKlxuICogQSBjb25zb2xlIGhpc3RvcnkgbWFuYWdlciBvYmplY3QuXG4gKi9cbmV4cG9ydCBjbGFzcyBDb25zb2xlSGlzdG9yeSBpbXBsZW1lbnRzIElDb25zb2xlSGlzdG9yeSB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgY29uc29sZSBoaXN0b3J5IG9iamVjdC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENvbnNvbGVIaXN0b3J5LklPcHRpb25zKSB7XG4gICAgY29uc3QgeyBzZXNzaW9uQ29udGV4dCB9ID0gb3B0aW9ucztcbiAgICBpZiAoc2Vzc2lvbkNvbnRleHQpIHtcbiAgICAgIHRoaXMuc2Vzc2lvbkNvbnRleHQgPSBzZXNzaW9uQ29udGV4dDtcbiAgICAgIHZvaWQgdGhpcy5faGFuZGxlS2VybmVsKCk7XG4gICAgICB0aGlzLnNlc3Npb25Db250ZXh0Lmtlcm5lbENoYW5nZWQuY29ubmVjdCh0aGlzLl9oYW5kbGVLZXJuZWwsIHRoaXMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY2xpZW50IHNlc3Npb24gdXNlZCBieSB0aGUgZm9yZWlnbiBoYW5kbGVyLlxuICAgKi9cbiAgcmVhZG9ubHkgc2Vzc2lvbkNvbnRleHQ6IElTZXNzaW9uQ29udGV4dCB8IG51bGw7XG5cbiAgLyoqXG4gICAqIFRoZSBjdXJyZW50IGVkaXRvciB1c2VkIGJ5IHRoZSBoaXN0b3J5IG1hbmFnZXIuXG4gICAqL1xuICBnZXQgZWRpdG9yKCk6IENvZGVFZGl0b3IuSUVkaXRvciB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9lZGl0b3I7XG4gIH1cbiAgc2V0IGVkaXRvcih2YWx1ZTogQ29kZUVkaXRvci5JRWRpdG9yIHwgbnVsbCkge1xuICAgIGlmICh0aGlzLl9lZGl0b3IgPT09IHZhbHVlKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgY29uc3QgcHJldiA9IHRoaXMuX2VkaXRvcjtcbiAgICBpZiAocHJldikge1xuICAgICAgcHJldi5lZGdlUmVxdWVzdGVkLmRpc2Nvbm5lY3QodGhpcy5vbkVkZ2VSZXF1ZXN0LCB0aGlzKTtcbiAgICAgIHByZXYubW9kZWwudmFsdWUuY2hhbmdlZC5kaXNjb25uZWN0KHRoaXMub25UZXh0Q2hhbmdlLCB0aGlzKTtcbiAgICB9XG5cbiAgICB0aGlzLl9lZGl0b3IgPSB2YWx1ZTtcblxuICAgIGlmICh2YWx1ZSkge1xuICAgICAgdmFsdWUuZWRnZVJlcXVlc3RlZC5jb25uZWN0KHRoaXMub25FZGdlUmVxdWVzdCwgdGhpcyk7XG4gICAgICB2YWx1ZS5tb2RlbC52YWx1ZS5jaGFuZ2VkLmNvbm5lY3QodGhpcy5vblRleHRDaGFuZ2UsIHRoaXMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgcGxhY2Vob2xkZXIgdGV4dCB0aGF0IGEgaGlzdG9yeSBzZXNzaW9uIGJlZ2FuIHdpdGguXG4gICAqL1xuICBnZXQgcGxhY2Vob2xkZXIoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5fcGxhY2Vob2xkZXI7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHdoZXRoZXIgdGhlIGNvbnNvbGUgaGlzdG9yeSBtYW5hZ2VyIGlzIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIGNvbnNvbGUgaGlzdG9yeSBtYW5hZ2VyLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICB0aGlzLl9oaXN0b3J5Lmxlbmd0aCA9IDA7XG4gICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIHByZXZpb3VzIGl0ZW0gaW4gdGhlIGNvbnNvbGUgaGlzdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIHBsYWNlaG9sZGVyIC0gVGhlIHBsYWNlaG9sZGVyIHN0cmluZyB0aGF0IGdldHMgdGVtcG9yYXJpbHkgYWRkZWRcbiAgICogdG8gdGhlIGhpc3Rvcnkgb25seSBmb3IgdGhlIGR1cmF0aW9uIG9mIG9uZSBoaXN0b3J5IHNlc3Npb24uIElmIG11bHRpcGxlXG4gICAqIHBsYWNlaG9sZGVycyBhcmUgc2VudCB3aXRoaW4gYSBzZXNzaW9uLCBvbmx5IHRoZSBmaXJzdCBvbmUgaXMgYWNjZXB0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgUHJvbWlzZSBmb3IgY29uc29sZSBjb21tYW5kIHRleHQgb3IgYHVuZGVmaW5lZGAgaWYgdW5hdmFpbGFibGUuXG4gICAqL1xuICBiYWNrKHBsYWNlaG9sZGVyOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4ge1xuICAgIGlmICghdGhpcy5faGFzU2Vzc2lvbikge1xuICAgICAgdGhpcy5faGFzU2Vzc2lvbiA9IHRydWU7XG4gICAgICB0aGlzLl9wbGFjZWhvbGRlciA9IHBsYWNlaG9sZGVyO1xuICAgICAgLy8gRmlsdGVyIHRoZSBoaXN0b3J5IHdpdGggdGhlIHBsYWNlaG9sZGVyIHN0cmluZy5cbiAgICAgIHRoaXMuc2V0RmlsdGVyKHBsYWNlaG9sZGVyKTtcbiAgICAgIHRoaXMuX2N1cnNvciA9IHRoaXMuX2ZpbHRlcmVkLmxlbmd0aCAtIDE7XG4gICAgfVxuXG4gICAgLS10aGlzLl9jdXJzb3I7XG4gICAgdGhpcy5fY3Vyc29yID0gTWF0aC5tYXgoMCwgdGhpcy5fY3Vyc29yKTtcbiAgICBjb25zdCBjb250ZW50ID0gdGhpcy5fZmlsdGVyZWRbdGhpcy5fY3Vyc29yXTtcbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKGNvbnRlbnQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgbmV4dCBpdGVtIGluIHRoZSBjb25zb2xlIGhpc3RvcnkuXG4gICAqXG4gICAqIEBwYXJhbSBwbGFjZWhvbGRlciAtIFRoZSBwbGFjZWhvbGRlciBzdHJpbmcgdGhhdCBnZXRzIHRlbXBvcmFyaWx5IGFkZGVkXG4gICAqIHRvIHRoZSBoaXN0b3J5IG9ubHkgZm9yIHRoZSBkdXJhdGlvbiBvZiBvbmUgaGlzdG9yeSBzZXNzaW9uLiBJZiBtdWx0aXBsZVxuICAgKiBwbGFjZWhvbGRlcnMgYXJlIHNlbnQgd2l0aGluIGEgc2Vzc2lvbiwgb25seSB0aGUgZmlyc3Qgb25lIGlzIGFjY2VwdGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIFByb21pc2UgZm9yIGNvbnNvbGUgY29tbWFuZCB0ZXh0IG9yIGB1bmRlZmluZWRgIGlmIHVuYXZhaWxhYmxlLlxuICAgKi9cbiAgZm9yd2FyZChwbGFjZWhvbGRlcjogc3RyaW5nKTogUHJvbWlzZTxzdHJpbmc+IHtcbiAgICBpZiAoIXRoaXMuX2hhc1Nlc3Npb24pIHtcbiAgICAgIHRoaXMuX2hhc1Nlc3Npb24gPSB0cnVlO1xuICAgICAgdGhpcy5fcGxhY2Vob2xkZXIgPSBwbGFjZWhvbGRlcjtcbiAgICAgIC8vIEZpbHRlciB0aGUgaGlzdG9yeSB3aXRoIHRoZSBwbGFjZWhvbGRlciBzdHJpbmcuXG4gICAgICB0aGlzLnNldEZpbHRlcihwbGFjZWhvbGRlcik7XG4gICAgICB0aGlzLl9jdXJzb3IgPSB0aGlzLl9maWx0ZXJlZC5sZW5ndGg7XG4gICAgfVxuXG4gICAgKyt0aGlzLl9jdXJzb3I7XG4gICAgdGhpcy5fY3Vyc29yID0gTWF0aC5taW4odGhpcy5fZmlsdGVyZWQubGVuZ3RoIC0gMSwgdGhpcy5fY3Vyc29yKTtcbiAgICBjb25zdCBjb250ZW50ID0gdGhpcy5fZmlsdGVyZWRbdGhpcy5fY3Vyc29yXTtcbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKGNvbnRlbnQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBhIG5ldyBpdGVtIHRvIHRoZSBib3R0b20gb2YgaGlzdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIGl0ZW0gVGhlIGl0ZW0gYmVpbmcgYWRkZWQgdG8gdGhlIGJvdHRvbSBvZiBoaXN0b3J5LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIElmIHRoZSBpdGVtIGJlaW5nIGFkZGVkIGlzIHVuZGVmaW5lZCBvciBlbXB0eSwgaXQgaXMgaWdub3JlZC4gSWYgdGhlIGl0ZW1cbiAgICogYmVpbmcgYWRkZWQgaXMgdGhlIHNhbWUgYXMgdGhlIGxhc3QgaXRlbSBpbiBoaXN0b3J5LCBpdCBpcyBpZ25vcmVkIGFzIHdlbGxcbiAgICogc28gdGhhdCB0aGUgY29uc29sZSdzIGhpc3Rvcnkgd2lsbCBjb25zaXN0IG9mIG5vIGNvbnRpZ3VvdXMgcmVwZXRpdGlvbnMuXG4gICAqL1xuICBwdXNoKGl0ZW06IHN0cmluZyk6IHZvaWQge1xuICAgIGlmIChpdGVtICYmIGl0ZW0gIT09IHRoaXMuX2hpc3RvcnlbdGhpcy5faGlzdG9yeS5sZW5ndGggLSAxXSkge1xuICAgICAgdGhpcy5faGlzdG9yeS5wdXNoKGl0ZW0pO1xuICAgIH1cbiAgICB0aGlzLnJlc2V0KCk7XG4gIH1cblxuICAvKipcbiAgICogUmVzZXQgdGhlIGhpc3RvcnkgbmF2aWdhdGlvbiBzdGF0ZSwgaS5lLiwgc3RhcnQgYSBuZXcgaGlzdG9yeSBzZXNzaW9uLlxuICAgKi9cbiAgcmVzZXQoKTogdm9pZCB7XG4gICAgdGhpcy5fY3Vyc29yID0gdGhpcy5faGlzdG9yeS5sZW5ndGg7XG4gICAgdGhpcy5faGFzU2Vzc2lvbiA9IGZhbHNlO1xuICAgIHRoaXMuX3BsYWNlaG9sZGVyID0gJyc7XG4gIH1cblxuICAvKipcbiAgICogUG9wdWxhdGUgdGhlIGhpc3RvcnkgY29sbGVjdGlvbiBvbiBoaXN0b3J5IHJlcGx5IGZyb20gYSBrZXJuZWwuXG4gICAqXG4gICAqIEBwYXJhbSB2YWx1ZSBUaGUga2VybmVsIG1lc3NhZ2UgaGlzdG9yeSByZXBseS5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBIaXN0b3J5IGVudHJpZXMgaGF2ZSB0aGUgc2hhcGU6XG4gICAqIFtzZXNzaW9uOiBudW1iZXIsIGxpbmU6IG51bWJlciwgaW5wdXQ6IHN0cmluZ11cbiAgICogQ29udGlndW91cyBkdXBsaWNhdGVzIGFyZSBzdHJpcHBlZCBvdXQgb2YgdGhlIEFQSSByZXNwb25zZS5cbiAgICovXG4gIHByb3RlY3RlZCBvbkhpc3RvcnkodmFsdWU6IEtlcm5lbE1lc3NhZ2UuSUhpc3RvcnlSZXBseU1zZyk6IHZvaWQge1xuICAgIHRoaXMuX2hpc3RvcnkubGVuZ3RoID0gMDtcbiAgICBsZXQgbGFzdCA9ICcnO1xuICAgIGxldCBjdXJyZW50ID0gJyc7XG4gICAgaWYgKHZhbHVlLmNvbnRlbnQuc3RhdHVzID09PSAnb2snKSB7XG4gICAgICBmb3IgKGxldCBpID0gMDsgaSA8IHZhbHVlLmNvbnRlbnQuaGlzdG9yeS5sZW5ndGg7IGkrKykge1xuICAgICAgICBjdXJyZW50ID0gKHZhbHVlLmNvbnRlbnQuaGlzdG9yeVtpXSBhcyBzdHJpbmdbXSlbMl07XG4gICAgICAgIGlmIChjdXJyZW50ICE9PSBsYXN0KSB7XG4gICAgICAgICAgdGhpcy5faGlzdG9yeS5wdXNoKChsYXN0ID0gY3VycmVudCkpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfVxuICAgIC8vIFJlc2V0IHRoZSBoaXN0b3J5IG5hdmlnYXRpb24gY3Vyc29yIGJhY2sgdG8gdGhlIGJvdHRvbS5cbiAgICB0aGlzLl9jdXJzb3IgPSB0aGlzLl9oaXN0b3J5Lmxlbmd0aDtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSB0ZXh0IGNoYW5nZSBzaWduYWwgZnJvbSB0aGUgZWRpdG9yLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uVGV4dENoYW5nZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5fc2V0QnlIaXN0b3J5KSB7XG4gICAgICB0aGlzLl9zZXRCeUhpc3RvcnkgPSBmYWxzZTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5yZXNldCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbiBlZGdlIHJlcXVlc3RlZCBzaWduYWwuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25FZGdlUmVxdWVzdChcbiAgICBlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvcixcbiAgICBsb2NhdGlvbjogQ29kZUVkaXRvci5FZGdlTG9jYXRpb25cbiAgKTogdm9pZCB7XG4gICAgY29uc3QgbW9kZWwgPSBlZGl0b3IubW9kZWw7XG4gICAgY29uc3Qgc291cmNlID0gbW9kZWwudmFsdWUudGV4dDtcblxuICAgIGlmIChsb2NhdGlvbiA9PT0gJ3RvcCcgfHwgbG9jYXRpb24gPT09ICd0b3BMaW5lJykge1xuICAgICAgdm9pZCB0aGlzLmJhY2soc291cmNlKS50aGVuKHZhbHVlID0+IHtcbiAgICAgICAgaWYgKHRoaXMuaXNEaXNwb3NlZCB8fCAhdmFsdWUpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgaWYgKG1vZGVsLnZhbHVlLnRleHQgPT09IHZhbHVlKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIHRoaXMuX3NldEJ5SGlzdG9yeSA9IHRydWU7XG4gICAgICAgIG1vZGVsLnZhbHVlLnRleHQgPSB2YWx1ZTtcbiAgICAgICAgbGV0IGNvbHVtblBvcyA9IDA7XG4gICAgICAgIGNvbHVtblBvcyA9IHZhbHVlLmluZGV4T2YoJ1xcbicpO1xuICAgICAgICBpZiAoY29sdW1uUG9zIDwgMCkge1xuICAgICAgICAgIGNvbHVtblBvcyA9IHZhbHVlLmxlbmd0aDtcbiAgICAgICAgfVxuICAgICAgICBlZGl0b3Iuc2V0Q3Vyc29yUG9zaXRpb24oeyBsaW5lOiAwLCBjb2x1bW46IGNvbHVtblBvcyB9KTtcbiAgICAgIH0pO1xuICAgIH0gZWxzZSB7XG4gICAgICB2b2lkIHRoaXMuZm9yd2FyZChzb3VyY2UpLnRoZW4odmFsdWUgPT4ge1xuICAgICAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHRleHQgPSB2YWx1ZSB8fCB0aGlzLnBsYWNlaG9sZGVyO1xuICAgICAgICBpZiAobW9kZWwudmFsdWUudGV4dCA9PT0gdGV4dCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICB0aGlzLl9zZXRCeUhpc3RvcnkgPSB0cnVlO1xuICAgICAgICBtb2RlbC52YWx1ZS50ZXh0ID0gdGV4dDtcbiAgICAgICAgY29uc3QgcG9zID0gZWRpdG9yLmdldFBvc2l0aW9uQXQodGV4dC5sZW5ndGgpO1xuICAgICAgICBpZiAocG9zKSB7XG4gICAgICAgICAgZWRpdG9yLnNldEN1cnNvclBvc2l0aW9uKHBvcyk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGN1cnJlbnQga2VybmVsIGNoYW5naW5nLlxuICAgKi9cbiAgcHJpdmF0ZSBhc3luYyBfaGFuZGxlS2VybmVsKCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IGtlcm5lbCA9IHRoaXMuc2Vzc2lvbkNvbnRleHQ/LnNlc3Npb24/Lmtlcm5lbDtcbiAgICBpZiAoIWtlcm5lbCkge1xuICAgICAgdGhpcy5faGlzdG9yeS5sZW5ndGggPSAwO1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHJldHVybiBrZXJuZWwucmVxdWVzdEhpc3RvcnkoUHJpdmF0ZS5pbml0aWFsUmVxdWVzdCkudGhlbih2ID0+IHtcbiAgICAgIHRoaXMub25IaXN0b3J5KHYpO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgZmlsdGVyIGRhdGEuXG4gICAqXG4gICAqIEBwYXJhbSBmaWx0ZXJTdHIgLSBUaGUgc3RyaW5nIHRvIHVzZSB3aGVuIGZpbHRlcmluZyB0aGUgZGF0YS5cbiAgICovXG4gIHByb3RlY3RlZCBzZXRGaWx0ZXIoZmlsdGVyU3RyOiBzdHJpbmcgPSAnJyk6IHZvaWQge1xuICAgIC8vIEFwcGx5IHRoZSBuZXcgZmlsdGVyIGFuZCByZW1vdmUgY29udGlndW91cyBkdXBsaWNhdGVzLlxuICAgIHRoaXMuX2ZpbHRlcmVkLmxlbmd0aCA9IDA7XG5cbiAgICBsZXQgbGFzdCA9ICcnO1xuICAgIGxldCBjdXJyZW50ID0gJyc7XG5cbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IHRoaXMuX2hpc3RvcnkubGVuZ3RoOyBpKyspIHtcbiAgICAgIGN1cnJlbnQgPSB0aGlzLl9oaXN0b3J5W2ldO1xuICAgICAgaWYgKFxuICAgICAgICBjdXJyZW50ICE9PSBsYXN0ICYmXG4gICAgICAgIGZpbHRlclN0ciA9PT0gY3VycmVudC5zbGljZSgwLCBmaWx0ZXJTdHIubGVuZ3RoKVxuICAgICAgKSB7XG4gICAgICAgIHRoaXMuX2ZpbHRlcmVkLnB1c2goKGxhc3QgPSBjdXJyZW50KSk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgdGhpcy5fZmlsdGVyZWQucHVzaChmaWx0ZXJTdHIpO1xuICB9XG5cbiAgcHJpdmF0ZSBfY3Vyc29yID0gMDtcbiAgcHJpdmF0ZSBfaGFzU2Vzc2lvbiA9IGZhbHNlO1xuICBwcml2YXRlIF9oaXN0b3J5OiBzdHJpbmdbXSA9IFtdO1xuICBwcml2YXRlIF9wbGFjZWhvbGRlcjogc3RyaW5nID0gJyc7XG4gIHByaXZhdGUgX3NldEJ5SGlzdG9yeSA9IGZhbHNlO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG4gIHByaXZhdGUgX2VkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX2ZpbHRlcmVkOiBzdHJpbmdbXSA9IFtdO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBDb25zb2xlSGlzdG9yeSBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIENvbnNvbGVIaXN0b3J5IHtcbiAgLyoqXG4gICAqIFRoZSBpbml0aWFsaXphdGlvbiBvcHRpb25zIGZvciBhIGNvbnNvbGUgaGlzdG9yeSBvYmplY3QuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBUaGUgY2xpZW50IHNlc3Npb24gdXNlZCBieSB0aGUgZm9yZWlnbiBoYW5kbGVyLlxuICAgICAqL1xuICAgIHNlc3Npb25Db250ZXh0PzogSVNlc3Npb25Db250ZXh0O1xuICB9XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICBleHBvcnQgY29uc3QgaW5pdGlhbFJlcXVlc3Q6IEtlcm5lbE1lc3NhZ2UuSUhpc3RvcnlSZXF1ZXN0TXNnWydjb250ZW50J10gPSB7XG4gICAgb3V0cHV0OiBmYWxzZSxcbiAgICByYXc6IHRydWUsXG4gICAgaGlzdF9hY2Nlc3NfdHlwZTogJ3RhaWwnLFxuICAgIG46IDUwMFxuICB9O1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgY29uc29sZVxuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vZm9yZWlnbic7XG5leHBvcnQgKiBmcm9tICcuL2hpc3RvcnknO1xuZXhwb3J0ICogZnJvbSAnLi9wYW5lbCc7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG5leHBvcnQgKiBmcm9tICcuL3dpZGdldCc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7XG4gIElTZXNzaW9uQ29udGV4dCxcbiAgTWFpbkFyZWFXaWRnZXQsXG4gIFNlc3Npb25Db250ZXh0LFxuICBzZXNzaW9uQ29udGV4dERpYWxvZ3Ncbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgSUVkaXRvck1pbWVUeXBlU2VydmljZSB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0IHsgUGF0aEV4dCwgVGltZSwgVVJMRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIElSZW5kZXJNaW1lUmVnaXN0cnksXG4gIFJlbmRlck1pbWVSZWdpc3RyeVxufSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IFNlcnZpY2VNYW5hZ2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIG51bGxUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgY29uc29sZUljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFRva2VuLCBVVUlEIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFBhbmVsIH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IENvZGVDb25zb2xlIH0gZnJvbSAnLi93aWRnZXQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGNvbnNvbGUgcGFuZWxzLlxuICovXG5jb25zdCBQQU5FTF9DTEFTUyA9ICdqcC1Db25zb2xlUGFuZWwnO1xuXG4vKipcbiAqIEEgcGFuZWwgd2hpY2ggY29udGFpbnMgYSBjb25zb2xlIGFuZCB0aGUgYWJpbGl0eSB0byBhZGQgb3RoZXIgY2hpbGRyZW4uXG4gKi9cbmV4cG9ydCBjbGFzcyBDb25zb2xlUGFuZWwgZXh0ZW5kcyBNYWluQXJlYVdpZGdldDxQYW5lbD4ge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgY29uc29sZSBwYW5lbC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENvbnNvbGVQYW5lbC5JT3B0aW9ucykge1xuICAgIHN1cGVyKHsgY29udGVudDogbmV3IFBhbmVsKCkgfSk7XG4gICAgdGhpcy5hZGRDbGFzcyhQQU5FTF9DTEFTUyk7XG4gICAgbGV0IHtcbiAgICAgIHJlbmRlcm1pbWUsXG4gICAgICBtaW1lVHlwZVNlcnZpY2UsXG4gICAgICBwYXRoLFxuICAgICAgYmFzZVBhdGgsXG4gICAgICBuYW1lLFxuICAgICAgbWFuYWdlcixcbiAgICAgIG1vZGVsRmFjdG9yeSxcbiAgICAgIHNlc3Npb25Db250ZXh0LFxuICAgICAgdHJhbnNsYXRvclxuICAgIH0gPSBvcHRpb25zO1xuICAgIHRoaXMudHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgY29uc3QgdHJhbnMgPSB0aGlzLnRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuXG4gICAgY29uc3QgY29udGVudEZhY3RvcnkgPSAodGhpcy5jb250ZW50RmFjdG9yeSA9XG4gICAgICBvcHRpb25zLmNvbnRlbnRGYWN0b3J5IHx8IENvbnNvbGVQYW5lbC5kZWZhdWx0Q29udGVudEZhY3RvcnkpO1xuICAgIGNvbnN0IGNvdW50ID0gUHJpdmF0ZS5jb3VudCsrO1xuICAgIGlmICghcGF0aCkge1xuICAgICAgcGF0aCA9IFVSTEV4dC5qb2luKGJhc2VQYXRoIHx8ICcnLCBgY29uc29sZS0ke2NvdW50fS0ke1VVSUQudXVpZDQoKX1gKTtcbiAgICB9XG5cbiAgICBzZXNzaW9uQ29udGV4dCA9IHRoaXMuX3Nlc3Npb25Db250ZXh0ID1cbiAgICAgIHNlc3Npb25Db250ZXh0IHx8XG4gICAgICBuZXcgU2Vzc2lvbkNvbnRleHQoe1xuICAgICAgICBzZXNzaW9uTWFuYWdlcjogbWFuYWdlci5zZXNzaW9ucyxcbiAgICAgICAgc3BlY3NNYW5hZ2VyOiBtYW5hZ2VyLmtlcm5lbHNwZWNzLFxuICAgICAgICBwYXRoLFxuICAgICAgICBuYW1lOiBuYW1lIHx8IHRyYW5zLl9fKCdDb25zb2xlICUxJywgY291bnQpLFxuICAgICAgICB0eXBlOiAnY29uc29sZScsXG4gICAgICAgIGtlcm5lbFByZWZlcmVuY2U6IG9wdGlvbnMua2VybmVsUHJlZmVyZW5jZSxcbiAgICAgICAgc2V0QnVzeTogb3B0aW9ucy5zZXRCdXN5XG4gICAgICB9KTtcblxuICAgIGNvbnN0IHJlc29sdmVyID0gbmV3IFJlbmRlck1pbWVSZWdpc3RyeS5VcmxSZXNvbHZlcih7XG4gICAgICBzZXNzaW9uOiBzZXNzaW9uQ29udGV4dCxcbiAgICAgIGNvbnRlbnRzOiBtYW5hZ2VyLmNvbnRlbnRzXG4gICAgfSk7XG4gICAgcmVuZGVybWltZSA9IHJlbmRlcm1pbWUuY2xvbmUoeyByZXNvbHZlciB9KTtcblxuICAgIHRoaXMuY29uc29sZSA9IGNvbnRlbnRGYWN0b3J5LmNyZWF0ZUNvbnNvbGUoe1xuICAgICAgcmVuZGVybWltZSxcbiAgICAgIHNlc3Npb25Db250ZXh0OiBzZXNzaW9uQ29udGV4dCxcbiAgICAgIG1pbWVUeXBlU2VydmljZSxcbiAgICAgIGNvbnRlbnRGYWN0b3J5LFxuICAgICAgbW9kZWxGYWN0b3J5XG4gICAgfSk7XG4gICAgdGhpcy5jb250ZW50LmFkZFdpZGdldCh0aGlzLmNvbnNvbGUpO1xuXG4gICAgdm9pZCBzZXNzaW9uQ29udGV4dC5pbml0aWFsaXplKCkudGhlbihhc3luYyB2YWx1ZSA9PiB7XG4gICAgICBpZiAodmFsdWUpIHtcbiAgICAgICAgYXdhaXQgc2Vzc2lvbkNvbnRleHREaWFsb2dzLnNlbGVjdEtlcm5lbChzZXNzaW9uQ29udGV4dCEpO1xuICAgICAgfVxuICAgICAgdGhpcy5fY29ubmVjdGVkID0gbmV3IERhdGUoKTtcbiAgICAgIHRoaXMuX3VwZGF0ZVRpdGxlUGFuZWwoKTtcbiAgICB9KTtcblxuICAgIHRoaXMuY29uc29sZS5leGVjdXRlZC5jb25uZWN0KHRoaXMuX29uRXhlY3V0ZWQsIHRoaXMpO1xuICAgIHRoaXMuX3VwZGF0ZVRpdGxlUGFuZWwoKTtcbiAgICBzZXNzaW9uQ29udGV4dC5rZXJuZWxDaGFuZ2VkLmNvbm5lY3QodGhpcy5fdXBkYXRlVGl0bGVQYW5lbCwgdGhpcyk7XG4gICAgc2Vzc2lvbkNvbnRleHQucHJvcGVydHlDaGFuZ2VkLmNvbm5lY3QodGhpcy5fdXBkYXRlVGl0bGVQYW5lbCwgdGhpcyk7XG5cbiAgICB0aGlzLnRpdGxlLmljb24gPSBjb25zb2xlSWNvbjtcbiAgICB0aGlzLnRpdGxlLmNsb3NhYmxlID0gdHJ1ZTtcbiAgICB0aGlzLmlkID0gYGNvbnNvbGUtJHtjb3VudH1gO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjb250ZW50IGZhY3RvcnkgdXNlZCBieSB0aGUgY29uc29sZSBwYW5lbC5cbiAgICovXG4gIHJlYWRvbmx5IGNvbnRlbnRGYWN0b3J5OiBDb25zb2xlUGFuZWwuSUNvbnRlbnRGYWN0b3J5O1xuXG4gIC8qKlxuICAgKiBUaGUgY29uc29sZSB3aWRnZXQgdXNlZCBieSB0aGUgcGFuZWwuXG4gICAqL1xuICBjb25zb2xlOiBDb2RlQ29uc29sZTtcblxuICAvKipcbiAgICogVGhlIHNlc3Npb24gdXNlZCBieSB0aGUgcGFuZWwuXG4gICAqL1xuICBnZXQgc2Vzc2lvbkNvbnRleHQoKTogSVNlc3Npb25Db250ZXh0IHtcbiAgICByZXR1cm4gdGhpcy5fc2Vzc2lvbkNvbnRleHQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgdGhpcy5zZXNzaW9uQ29udGV4dC5kaXNwb3NlKCk7XG4gICAgdGhpcy5jb25zb2xlLmRpc3Bvc2UoKTtcbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnYWN0aXZhdGUtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGNvbnN0IHByb21wdCA9IHRoaXMuY29uc29sZS5wcm9tcHRDZWxsO1xuICAgIGlmIChwcm9tcHQpIHtcbiAgICAgIHByb21wdC5lZGl0b3IuZm9jdXMoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnY2xvc2UtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQ2xvc2VSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHN1cGVyLm9uQ2xvc2VSZXF1ZXN0KG1zZyk7XG4gICAgdGhpcy5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY29uc29sZSBleGVjdXRpb24uXG4gICAqL1xuICBwcml2YXRlIF9vbkV4ZWN1dGVkKHNlbmRlcjogQ29kZUNvbnNvbGUsIGFyZ3M6IERhdGUpIHtcbiAgICB0aGlzLl9leGVjdXRlZCA9IGFyZ3M7XG4gICAgdGhpcy5fdXBkYXRlVGl0bGVQYW5lbCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSB0aGUgY29uc29sZSBwYW5lbCB0aXRsZS5cbiAgICovXG4gIHByaXZhdGUgX3VwZGF0ZVRpdGxlUGFuZWwoKTogdm9pZCB7XG4gICAgUHJpdmF0ZS51cGRhdGVUaXRsZSh0aGlzLCB0aGlzLl9jb25uZWN0ZWQsIHRoaXMuX2V4ZWN1dGVkLCB0aGlzLnRyYW5zbGF0b3IpO1xuICB9XG5cbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3I7XG4gIHByaXZhdGUgX2V4ZWN1dGVkOiBEYXRlIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX2Nvbm5lY3RlZDogRGF0ZSB8IG51bGwgPSBudWxsO1xuICBwcml2YXRlIF9zZXNzaW9uQ29udGV4dDogSVNlc3Npb25Db250ZXh0O1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBDb25zb2xlUGFuZWwgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBDb25zb2xlUGFuZWwge1xuICAvKipcbiAgICogVGhlIGluaXRpYWxpemF0aW9uIG9wdGlvbnMgZm9yIGEgY29uc29sZSBwYW5lbC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSByZW5kZXJtaW1lIGluc3RhbmNlIHVzZWQgYnkgdGhlIHBhbmVsLlxuICAgICAqL1xuICAgIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY29udGVudCBmYWN0b3J5IGZvciB0aGUgcGFuZWwuXG4gICAgICovXG4gICAgY29udGVudEZhY3Rvcnk6IElDb250ZW50RmFjdG9yeTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBzZXJ2aWNlIG1hbmFnZXIgdXNlZCBieSB0aGUgcGFuZWwuXG4gICAgICovXG4gICAgbWFuYWdlcjogU2VydmljZU1hbmFnZXIuSU1hbmFnZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcGF0aCBvZiBhbiBleGlzdGluZyBjb25zb2xlLlxuICAgICAqL1xuICAgIHBhdGg/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYmFzZSBwYXRoIGZvciBhIG5ldyBjb25zb2xlLlxuICAgICAqL1xuICAgIGJhc2VQYXRoPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIG5hbWUgb2YgdGhlIGNvbnNvbGUuXG4gICAgICovXG4gICAgbmFtZT86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIEEga2VybmVsIHByZWZlcmVuY2UuXG4gICAgICovXG4gICAga2VybmVsUHJlZmVyZW5jZT86IElTZXNzaW9uQ29udGV4dC5JS2VybmVsUHJlZmVyZW5jZTtcblxuICAgIC8qKlxuICAgICAqIEFuIGV4aXN0aW5nIHNlc3Npb24gY29udGV4dCB0byB1c2UuXG4gICAgICovXG4gICAgc2Vzc2lvbkNvbnRleHQ/OiBJU2Vzc2lvbkNvbnRleHQ7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbW9kZWwgZmFjdG9yeSBmb3IgdGhlIGNvbnNvbGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIG1vZGVsRmFjdG9yeT86IENvZGVDb25zb2xlLklNb2RlbEZhY3Rvcnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgc2VydmljZSB1c2VkIHRvIGxvb2sgdXAgbWltZSB0eXBlcy5cbiAgICAgKi9cbiAgICBtaW1lVHlwZVNlcnZpY2U6IElFZGl0b3JNaW1lVHlwZVNlcnZpY2U7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYXBwbGljYXRpb24gbGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICAgKi9cbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3I7XG5cbiAgICAvKipcbiAgICAgKiBBIGZ1bmN0aW9uIHRvIGNhbGwgd2hlbiB0aGUga2VybmVsIGlzIGJ1c3kuXG4gICAgICovXG4gICAgc2V0QnVzeT86ICgpID0+IElEaXNwb3NhYmxlO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjb25zb2xlIHBhbmVsIHJlbmRlcmVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29udGVudEZhY3RvcnkgZXh0ZW5kcyBDb2RlQ29uc29sZS5JQ29udGVudEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBjb25zb2xlIHBhbmVsLlxuICAgICAqL1xuICAgIGNyZWF0ZUNvbnNvbGUob3B0aW9uczogQ29kZUNvbnNvbGUuSU9wdGlvbnMpOiBDb2RlQ29uc29sZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIGBJQ29udGVudEZhY3RvcnlgLlxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIENvbnRlbnRGYWN0b3J5XG4gICAgZXh0ZW5kcyBDb2RlQ29uc29sZS5Db250ZW50RmFjdG9yeVxuICAgIGltcGxlbWVudHMgSUNvbnRlbnRGYWN0b3J5XG4gIHtcbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSBuZXcgY29uc29sZSBwYW5lbC5cbiAgICAgKi9cbiAgICBjcmVhdGVDb25zb2xlKG9wdGlvbnM6IENvZGVDb25zb2xlLklPcHRpb25zKTogQ29kZUNvbnNvbGUge1xuICAgICAgcmV0dXJuIG5ldyBDb2RlQ29uc29sZShvcHRpb25zKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQSBuYW1lc3BhY2UgZm9yIHRoZSBjb25zb2xlIHBhbmVsIGNvbnRlbnQgZmFjdG9yeS5cbiAgICovXG4gIGV4cG9ydCBuYW1lc3BhY2UgQ29udGVudEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIE9wdGlvbnMgZm9yIHRoZSBjb2RlIGNvbnNvbGUgY29udGVudCBmYWN0b3J5LlxuICAgICAqL1xuICAgIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMgZXh0ZW5kcyBDb2RlQ29uc29sZS5Db250ZW50RmFjdG9yeS5JT3B0aW9ucyB7fVxuICB9XG5cbiAgLyoqXG4gICAqIEEgZGVmYXVsdCBjb2RlIGNvbnNvbGUgY29udGVudCBmYWN0b3J5LlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRlZmF1bHRDb250ZW50RmFjdG9yeTogSUNvbnRlbnRGYWN0b3J5ID0gbmV3IENvbnRlbnRGYWN0b3J5KCk7XG5cbiAgLyoqXG4gICAqIFRoZSBjb25zb2xlIHJlbmRlcmVyIHRva2VuLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IElDb250ZW50RmFjdG9yeSA9IG5ldyBUb2tlbjxJQ29udGVudEZhY3Rvcnk+KFxuICAgICdAanVweXRlcmxhYi9jb25zb2xlOklDb250ZW50RmFjdG9yeSdcbiAgKTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgcHJpdmF0ZSBkYXRhLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBUaGUgY291bnRlciBmb3IgbmV3IGNvbnNvbGVzLlxuICAgKi9cbiAgZXhwb3J0IGxldCBjb3VudCA9IDE7XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSB0aGUgdGl0bGUgb2YgYSBjb25zb2xlIHBhbmVsLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIHVwZGF0ZVRpdGxlKFxuICAgIHBhbmVsOiBDb25zb2xlUGFuZWwsXG4gICAgY29ubmVjdGVkOiBEYXRlIHwgbnVsbCxcbiAgICBleGVjdXRlZDogRGF0ZSB8IG51bGwsXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yXG4gICk6IHZvaWQge1xuICAgIHRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICBjb25zdCBzZXNzaW9uQ29udGV4dCA9IHBhbmVsLmNvbnNvbGUuc2Vzc2lvbkNvbnRleHQuc2Vzc2lvbjtcbiAgICBpZiAoc2Vzc2lvbkNvbnRleHQpIHtcbiAgICAgIC8vIEZJWE1FOlxuICAgICAgbGV0IGNhcHRpb24gPVxuICAgICAgICB0cmFucy5fXygnTmFtZTogJTFcXG4nLCBzZXNzaW9uQ29udGV4dC5uYW1lKSArXG4gICAgICAgIHRyYW5zLl9fKCdEaXJlY3Rvcnk6ICUxXFxuJywgUGF0aEV4dC5kaXJuYW1lKHNlc3Npb25Db250ZXh0LnBhdGgpKSArXG4gICAgICAgIHRyYW5zLl9fKCdLZXJuZWw6ICUxJywgcGFuZWwuY29uc29sZS5zZXNzaW9uQ29udGV4dC5rZXJuZWxEaXNwbGF5TmFtZSk7XG5cbiAgICAgIGlmIChjb25uZWN0ZWQpIHtcbiAgICAgICAgY2FwdGlvbiArPSB0cmFucy5fXyhcbiAgICAgICAgICAnXFxuQ29ubmVjdGVkOiAlMScsXG4gICAgICAgICAgVGltZS5mb3JtYXQoY29ubmVjdGVkLnRvSVNPU3RyaW5nKCkpXG4gICAgICAgICk7XG4gICAgICB9XG5cbiAgICAgIGlmIChleGVjdXRlZCkge1xuICAgICAgICBjYXB0aW9uICs9IHRyYW5zLl9fKCdcXG5MYXN0IEV4ZWN1dGlvbjogJTEnKTtcbiAgICAgIH1cbiAgICAgIHBhbmVsLnRpdGxlLmxhYmVsID0gc2Vzc2lvbkNvbnRleHQubmFtZTtcbiAgICAgIHBhbmVsLnRpdGxlLmNhcHRpb24gPSBjYXB0aW9uO1xuICAgIH0gZWxzZSB7XG4gICAgICBwYW5lbC50aXRsZS5sYWJlbCA9IHRyYW5zLl9fKCdDb25zb2xlJyk7XG4gICAgICBwYW5lbC50aXRsZS5jYXB0aW9uID0gJyc7XG4gICAgfVxuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElXaWRnZXRUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBDb25zb2xlUGFuZWwgfSBmcm9tICcuL3BhbmVsJztcblxuLyoqXG4gKiBUaGUgY29uc29sZSB0cmFja2VyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSUNvbnNvbGVUcmFja2VyID0gbmV3IFRva2VuPElDb25zb2xlVHJhY2tlcj4oXG4gICdAanVweXRlcmxhYi9jb25zb2xlOklDb25zb2xlVHJhY2tlcidcbik7XG5cbi8qKlxuICogQSBjbGFzcyB0aGF0IHRyYWNrcyBjb25zb2xlIHdpZGdldHMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSUNvbnNvbGVUcmFja2VyIGV4dGVuZHMgSVdpZGdldFRyYWNrZXI8Q29uc29sZVBhbmVsPiB7fVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJU2Vzc2lvbkNvbnRleHQgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQge1xuICBDZWxsLFxuICBDZWxsRHJhZ1V0aWxzLFxuICBDZWxsTW9kZWwsXG4gIENvZGVDZWxsLFxuICBDb2RlQ2VsbE1vZGVsLFxuICBJQ29kZUNlbGxNb2RlbCxcbiAgSVJhd0NlbGxNb2RlbCxcbiAgaXNDb2RlQ2VsbE1vZGVsLFxuICBSYXdDZWxsLFxuICBSYXdDZWxsTW9kZWxcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvY2VsbHMnO1xuaW1wb3J0IHsgQ29kZUVkaXRvciwgSUVkaXRvck1pbWVUeXBlU2VydmljZSB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuaW1wb3J0IHsgSU9ic2VydmFibGVMaXN0LCBPYnNlcnZhYmxlTGlzdCB9IGZyb20gJ0BqdXB5dGVybGFiL29ic2VydmFibGVzJztcbmltcG9ydCB7IElSZW5kZXJNaW1lUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IEtlcm5lbE1lc3NhZ2UgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBlYWNoIH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgSlNPTk9iamVjdCwgTWltZURhdGEgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBEcmFnIH0gZnJvbSAnQGx1bWluby9kcmFnZHJvcCc7XG5pbXBvcnQgeyBNZXNzYWdlIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgUGFuZWwsIFBhbmVsTGF5b3V0LCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgQ29uc29sZUhpc3RvcnksIElDb25zb2xlSGlzdG9yeSB9IGZyb20gJy4vaGlzdG9yeSc7XG5cbi8qKlxuICogVGhlIGRhdGEgYXR0cmlidXRlIGFkZGVkIHRvIGEgd2lkZ2V0IHRoYXQgaGFzIGFuIGFjdGl2ZSBrZXJuZWwuXG4gKi9cbmNvbnN0IEtFUk5FTF9VU0VSID0gJ2pwS2VybmVsVXNlcic7XG5cbi8qKlxuICogVGhlIGRhdGEgYXR0cmlidXRlIGFkZGVkIHRvIGEgd2lkZ2V0IGNhbiBydW4gY29kZS5cbiAqL1xuY29uc3QgQ09ERV9SVU5ORVIgPSAnanBDb2RlUnVubmVyJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBjb25zb2xlIHdpZGdldHMuXG4gKi9cbmNvbnN0IENPTlNPTEVfQ0xBU1MgPSAnanAtQ29kZUNvbnNvbGUnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBhZGRlZCB0byBjb25zb2xlIGNlbGxzXG4gKi9cbmNvbnN0IENPTlNPTEVfQ0VMTF9DTEFTUyA9ICdqcC1Db25zb2xlLWNlbGwnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIHRoZSBjb25zb2xlIGJhbm5lci5cbiAqL1xuY29uc3QgQkFOTkVSX0NMQVNTID0gJ2pwLUNvZGVDb25zb2xlLWJhbm5lcic7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgb2YgdGhlIGFjdGl2ZSBwcm9tcHQgY2VsbC5cbiAqL1xuY29uc3QgUFJPTVBUX0NMQVNTID0gJ2pwLUNvZGVDb25zb2xlLXByb21wdENlbGwnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIG9mIHRoZSBwYW5lbCB0aGF0IGhvbGRzIGNlbGwgY29udGVudC5cbiAqL1xuY29uc3QgQ09OVEVOVF9DTEFTUyA9ICdqcC1Db2RlQ29uc29sZS1jb250ZW50JztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBvZiB0aGUgcGFuZWwgdGhhdCBob2xkcyBwcm9tcHRzLlxuICovXG5jb25zdCBJTlBVVF9DTEFTUyA9ICdqcC1Db2RlQ29uc29sZS1pbnB1dCc7XG5cbi8qKlxuICogVGhlIHRpbWVvdXQgaW4gbXMgZm9yIGV4ZWN1dGlvbiByZXF1ZXN0cyB0byB0aGUga2VybmVsLlxuICovXG5jb25zdCBFWEVDVVRJT05fVElNRU9VVCA9IDI1MDtcblxuLyoqXG4gKiBUaGUgbWltZXR5cGUgdXNlZCBmb3IgSnVweXRlciBjZWxsIGRhdGEuXG4gKi9cbmNvbnN0IEpVUFlURVJfQ0VMTF9NSU1FID0gJ2FwcGxpY2F0aW9uL3ZuZC5qdXB5dGVyLmNlbGxzJztcblxuLyoqXG4gKiBBIHdpZGdldCBjb250YWluaW5nIGEgSnVweXRlciBjb25zb2xlLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoZSBDb2RlQ29uc29sZSBjbGFzcyBpcyBpbnRlbmRlZCB0byBiZSB1c2VkIHdpdGhpbiBhIENvbnNvbGVQYW5lbFxuICogaW5zdGFuY2UuIFVuZGVyIG1vc3QgY2lyY3Vtc3RhbmNlcywgaXQgaXMgbm90IGluc3RhbnRpYXRlZCBieSB1c2VyIGNvZGUuXG4gKi9cbmV4cG9ydCBjbGFzcyBDb2RlQ29uc29sZSBleHRlbmRzIFdpZGdldCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBjb25zb2xlIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENvZGVDb25zb2xlLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmFkZENsYXNzKENPTlNPTEVfQ0xBU1MpO1xuICAgIHRoaXMubm9kZS5kYXRhc2V0W0tFUk5FTF9VU0VSXSA9ICd0cnVlJztcbiAgICB0aGlzLm5vZGUuZGF0YXNldFtDT0RFX1JVTk5FUl0gPSAndHJ1ZSc7XG4gICAgdGhpcy5ub2RlLnRhYkluZGV4ID0gLTE7IC8vIEFsbG93IHRoZSB3aWRnZXQgdG8gdGFrZSBmb2N1cy5cblxuICAgIC8vIENyZWF0ZSB0aGUgcGFuZWxzIHRoYXQgaG9sZCB0aGUgY29udGVudCBhbmQgaW5wdXQuXG4gICAgY29uc3QgbGF5b3V0ID0gKHRoaXMubGF5b3V0ID0gbmV3IFBhbmVsTGF5b3V0KCkpO1xuICAgIHRoaXMuX2NlbGxzID0gbmV3IE9ic2VydmFibGVMaXN0PENlbGw+KCk7XG4gICAgdGhpcy5fY29udGVudCA9IG5ldyBQYW5lbCgpO1xuICAgIHRoaXMuX2lucHV0ID0gbmV3IFBhbmVsKCk7XG5cbiAgICB0aGlzLmNvbnRlbnRGYWN0b3J5ID1cbiAgICAgIG9wdGlvbnMuY29udGVudEZhY3RvcnkgfHwgQ29kZUNvbnNvbGUuZGVmYXVsdENvbnRlbnRGYWN0b3J5O1xuICAgIHRoaXMubW9kZWxGYWN0b3J5ID0gb3B0aW9ucy5tb2RlbEZhY3RvcnkgfHwgQ29kZUNvbnNvbGUuZGVmYXVsdE1vZGVsRmFjdG9yeTtcbiAgICB0aGlzLnJlbmRlcm1pbWUgPSBvcHRpb25zLnJlbmRlcm1pbWU7XG4gICAgdGhpcy5zZXNzaW9uQ29udGV4dCA9IG9wdGlvbnMuc2Vzc2lvbkNvbnRleHQ7XG4gICAgdGhpcy5fbWltZVR5cGVTZXJ2aWNlID0gb3B0aW9ucy5taW1lVHlwZVNlcnZpY2U7XG5cbiAgICAvLyBBZGQgdG9wLWxldmVsIENTUyBjbGFzc2VzLlxuICAgIHRoaXMuX2NvbnRlbnQuYWRkQ2xhc3MoQ09OVEVOVF9DTEFTUyk7XG4gICAgdGhpcy5faW5wdXQuYWRkQ2xhc3MoSU5QVVRfQ0xBU1MpO1xuXG4gICAgLy8gSW5zZXJ0IHRoZSBjb250ZW50IGFuZCBpbnB1dCBwYW5lcyBpbnRvIHRoZSB3aWRnZXQuXG4gICAgbGF5b3V0LmFkZFdpZGdldCh0aGlzLl9jb250ZW50KTtcbiAgICBsYXlvdXQuYWRkV2lkZ2V0KHRoaXMuX2lucHV0KTtcblxuICAgIHRoaXMuX2hpc3RvcnkgPSBuZXcgQ29uc29sZUhpc3Rvcnkoe1xuICAgICAgc2Vzc2lvbkNvbnRleHQ6IHRoaXMuc2Vzc2lvbkNvbnRleHRcbiAgICB9KTtcblxuICAgIHZvaWQgdGhpcy5fb25LZXJuZWxDaGFuZ2VkKCk7XG5cbiAgICB0aGlzLnNlc3Npb25Db250ZXh0Lmtlcm5lbENoYW5nZWQuY29ubmVjdCh0aGlzLl9vbktlcm5lbENoYW5nZWQsIHRoaXMpO1xuICAgIHRoaXMuc2Vzc2lvbkNvbnRleHQuc3RhdHVzQ2hhbmdlZC5jb25uZWN0KFxuICAgICAgdGhpcy5fb25LZXJuZWxTdGF0dXNDaGFuZ2VkLFxuICAgICAgdGhpc1xuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBjb25zb2xlIGZpbmlzaGVkIGV4ZWN1dGluZyBpdHMgcHJvbXB0IGNlbGwuXG4gICAqL1xuICBnZXQgZXhlY3V0ZWQoKTogSVNpZ25hbDx0aGlzLCBEYXRlPiB7XG4gICAgcmV0dXJuIHRoaXMuX2V4ZWN1dGVkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBhIG5ldyBwcm9tcHQgY2VsbCBpcyBjcmVhdGVkLlxuICAgKi9cbiAgZ2V0IHByb21wdENlbGxDcmVhdGVkKCk6IElTaWduYWw8dGhpcywgQ29kZUNlbGw+IHtcbiAgICByZXR1cm4gdGhpcy5fcHJvbXB0Q2VsbENyZWF0ZWQ7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNvbnRlbnQgZmFjdG9yeSB1c2VkIGJ5IHRoZSBjb25zb2xlLlxuICAgKi9cbiAgcmVhZG9ubHkgY29udGVudEZhY3Rvcnk6IENvZGVDb25zb2xlLklDb250ZW50RmFjdG9yeTtcblxuICAvKipcbiAgICogVGhlIG1vZGVsIGZhY3RvcnkgZm9yIHRoZSBjb25zb2xlIHdpZGdldC5cbiAgICovXG4gIHJlYWRvbmx5IG1vZGVsRmFjdG9yeTogQ29kZUNvbnNvbGUuSU1vZGVsRmFjdG9yeTtcblxuICAvKipcbiAgICogVGhlIHJlbmRlcm1pbWUgaW5zdGFuY2UgdXNlZCBieSB0aGUgY29uc29sZS5cbiAgICovXG4gIHJlYWRvbmx5IHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG5cbiAgLyoqXG4gICAqIFRoZSBjbGllbnQgc2Vzc2lvbiB1c2VkIGJ5IHRoZSBjb25zb2xlLlxuICAgKi9cbiAgcmVhZG9ubHkgc2Vzc2lvbkNvbnRleHQ6IElTZXNzaW9uQ29udGV4dDtcblxuICAvKipcbiAgICogVGhlIGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBmb3IgdGhlIHRleHQgZWRpdG9yIHdpZGdldC5cbiAgICovXG4gIGVkaXRvckNvbmZpZz86IFBhcnRpYWw8Q29kZUVkaXRvci5JQ29uZmlnPjtcblxuICAvKipcbiAgICogVGhlIGxpc3Qgb2YgY29udGVudCBjZWxscyBpbiB0aGUgY29uc29sZS5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIGxpc3QgZG9lcyBub3QgaW5jbHVkZSB0aGUgY3VycmVudCBiYW5uZXIgb3IgdGhlIHByb21wdCBmb3IgYSBjb25zb2xlLlxuICAgKiBJdCBtYXkgaW5jbHVkZSBwcmV2aW91cyBiYW5uZXJzIGFzIHJhdyBjZWxscy5cbiAgICovXG4gIGdldCBjZWxscygpOiBJT2JzZXJ2YWJsZUxpc3Q8Q2VsbD4ge1xuICAgIHJldHVybiB0aGlzLl9jZWxscztcbiAgfVxuXG4gIC8qXG4gICAqIFRoZSBjb25zb2xlIGlucHV0IHByb21wdCBjZWxsLlxuICAgKi9cbiAgZ2V0IHByb21wdENlbGwoKTogQ29kZUNlbGwgfCBudWxsIHtcbiAgICBjb25zdCBpbnB1dExheW91dCA9IHRoaXMuX2lucHV0LmxheW91dCBhcyBQYW5lbExheW91dDtcbiAgICByZXR1cm4gKGlucHV0TGF5b3V0LndpZGdldHNbMF0gYXMgQ29kZUNlbGwpIHx8IG51bGw7XG4gIH1cblxuICAvKipcbiAgICogQWRkIGEgbmV3IGNlbGwgdG8gdGhlIGNvbnRlbnQgcGFuZWwuXG4gICAqXG4gICAqIEBwYXJhbSBjZWxsIC0gVGhlIGNvZGUgY2VsbCB3aWRnZXQgYmVpbmcgYWRkZWQgdG8gdGhlIGNvbnRlbnQgcGFuZWwuXG4gICAqXG4gICAqIEBwYXJhbSBtc2dJZCAtIFRoZSBvcHRpb25hbCBleGVjdXRpb24gbWVzc2FnZSBpZCBmb3IgdGhlIGNlbGwuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2QgaXMgbWVhbnQgZm9yIHVzZSBieSBvdXRzaWRlIGNsYXNzZXMgdGhhdCB3YW50IHRvIGFkZCBjZWxscyB0byBhXG4gICAqIGNvbnNvbGUuIEl0IGlzIGRpc3RpbmN0IGZyb20gdGhlIGBpbmplY3RgIG1ldGhvZCBpbiB0aGF0IGl0IHJlcXVpcmVzXG4gICAqIHJlbmRlcmVkIGNvZGUgY2VsbCB3aWRnZXRzIGFuZCBkb2VzIG5vdCBleGVjdXRlIHRoZW0gKHRob3VnaCBpdCBjYW4gc3RvcmVcbiAgICogdGhlIGV4ZWN1dGlvbiBtZXNzYWdlIGlkKS5cbiAgICovXG4gIGFkZENlbGwoY2VsbDogQ29kZUNlbGwsIG1zZ0lkPzogc3RyaW5nKTogdm9pZCB7XG4gICAgY2VsbC5hZGRDbGFzcyhDT05TT0xFX0NFTExfQ0xBU1MpO1xuICAgIHRoaXMuX2NvbnRlbnQuYWRkV2lkZ2V0KGNlbGwpO1xuICAgIHRoaXMuX2NlbGxzLnB1c2goY2VsbCk7XG4gICAgaWYgKG1zZ0lkKSB7XG4gICAgICB0aGlzLl9tc2dJZHMuc2V0KG1zZ0lkLCBjZWxsKTtcbiAgICAgIHRoaXMuX21zZ0lkQ2VsbHMuc2V0KGNlbGwsIG1zZ0lkKTtcbiAgICB9XG4gICAgY2VsbC5kaXNwb3NlZC5jb25uZWN0KHRoaXMuX29uQ2VsbERpc3Bvc2VkLCB0aGlzKTtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBhIGJhbm5lciBjZWxsLlxuICAgKi9cbiAgYWRkQmFubmVyKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9iYW5uZXIpIHtcbiAgICAgIC8vIEFuIG9sZCBiYW5uZXIganVzdCBiZWNvbWVzIGEgbm9ybWFsIGNlbGwgbm93LlxuICAgICAgY29uc3QgY2VsbCA9IHRoaXMuX2Jhbm5lcjtcbiAgICAgIHRoaXMuX2NlbGxzLnB1c2godGhpcy5fYmFubmVyKTtcbiAgICAgIGNlbGwuZGlzcG9zZWQuY29ubmVjdCh0aGlzLl9vbkNlbGxEaXNwb3NlZCwgdGhpcyk7XG4gICAgfVxuICAgIC8vIENyZWF0ZSB0aGUgYmFubmVyLlxuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5tb2RlbEZhY3RvcnkuY3JlYXRlUmF3Q2VsbCh7fSk7XG4gICAgbW9kZWwudmFsdWUudGV4dCA9ICcuLi4nO1xuICAgIGNvbnN0IGJhbm5lciA9ICh0aGlzLl9iYW5uZXIgPSBuZXcgUmF3Q2VsbCh7XG4gICAgICBtb2RlbCxcbiAgICAgIGNvbnRlbnRGYWN0b3J5OiB0aGlzLmNvbnRlbnRGYWN0b3J5LFxuICAgICAgcGxhY2Vob2xkZXI6IGZhbHNlXG4gICAgfSkpLmluaXRpYWxpemVTdGF0ZSgpO1xuICAgIGJhbm5lci5hZGRDbGFzcyhCQU5ORVJfQ0xBU1MpO1xuICAgIGJhbm5lci5yZWFkT25seSA9IHRydWU7XG4gICAgdGhpcy5fY29udGVudC5hZGRXaWRnZXQoYmFubmVyKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDbGVhciB0aGUgY29kZSBjZWxscy5cbiAgICovXG4gIGNsZWFyKCk6IHZvaWQge1xuICAgIC8vIERpc3Bvc2UgYWxsIHRoZSBjb250ZW50IGNlbGxzXG4gICAgY29uc3QgY2VsbHMgPSB0aGlzLl9jZWxscztcbiAgICB3aGlsZSAoY2VsbHMubGVuZ3RoID4gMCkge1xuICAgICAgY2VsbHMuZ2V0KDApLmRpc3Bvc2UoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IGNlbGwgd2l0aCB0aGUgYnVpbHQtaW4gZmFjdG9yeS5cbiAgICovXG4gIGNyZWF0ZUNvZGVDZWxsKCk6IENvZGVDZWxsIHtcbiAgICBjb25zdCBmYWN0b3J5ID0gdGhpcy5jb250ZW50RmFjdG9yeTtcbiAgICBjb25zdCBvcHRpb25zID0gdGhpcy5fY3JlYXRlQ29kZUNlbGxPcHRpb25zKCk7XG4gICAgY29uc3QgY2VsbCA9IGZhY3RvcnkuY3JlYXRlQ29kZUNlbGwob3B0aW9ucyk7XG4gICAgY2VsbC5yZWFkT25seSA9IHRydWU7XG4gICAgY2VsbC5tb2RlbC5taW1lVHlwZSA9IHRoaXMuX21pbWV0eXBlO1xuICAgIHJldHVybiBjZWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyBoZWxkIGJ5IHRoZSB3aWRnZXQuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIC8vIERvIG5vdGhpbmcgaWYgYWxyZWFkeSBkaXNwb3NlZC5cbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMuX2NlbGxzLmNsZWFyKCk7XG4gICAgdGhpcy5fbXNnSWRDZWxscyA9IG51bGwhO1xuICAgIHRoaXMuX21zZ0lkcyA9IG51bGwhO1xuICAgIHRoaXMuX2hpc3RvcnkuZGlzcG9zZSgpO1xuXG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEV4ZWN1dGUgdGhlIGN1cnJlbnQgcHJvbXB0LlxuICAgKlxuICAgKiBAcGFyYW0gZm9yY2UgLSBXaGV0aGVyIHRvIGZvcmNlIGV4ZWN1dGlvbiB3aXRob3V0IGNoZWNraW5nIGNvZGVcbiAgICogY29tcGxldGVuZXNzLlxuICAgKlxuICAgKiBAcGFyYW0gdGltZW91dCAtIFRoZSBsZW5ndGggb2YgdGltZSwgaW4gbWlsbGlzZWNvbmRzLCB0aGF0IHRoZSBleGVjdXRpb25cbiAgICogc2hvdWxkIHdhaXQgZm9yIHRoZSBBUEkgdG8gZGV0ZXJtaW5lIHdoZXRoZXIgY29kZSBiZWluZyBzdWJtaXR0ZWQgaXNcbiAgICogaW5jb21wbGV0ZSBiZWZvcmUgYXR0ZW1wdGluZyBzdWJtaXNzaW9uIGFueXdheS4gVGhlIGRlZmF1bHQgdmFsdWUgaXMgYDI1MGAuXG4gICAqL1xuICBhc3luYyBleGVjdXRlKGZvcmNlID0gZmFsc2UsIHRpbWVvdXQgPSBFWEVDVVRJT05fVElNRU9VVCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGlmICh0aGlzLnNlc3Npb25Db250ZXh0LnNlc3Npb24/Lmtlcm5lbD8uc3RhdHVzID09PSAnZGVhZCcpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBwcm9tcHRDZWxsID0gdGhpcy5wcm9tcHRDZWxsO1xuICAgIGlmICghcHJvbXB0Q2VsbCkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKCdDYW5ub3QgZXhlY3V0ZSB3aXRob3V0IGEgcHJvbXB0IGNlbGwnKTtcbiAgICB9XG4gICAgcHJvbXB0Q2VsbC5tb2RlbC50cnVzdGVkID0gdHJ1ZTtcblxuICAgIGlmIChmb3JjZSkge1xuICAgICAgLy8gQ3JlYXRlIGEgbmV3IHByb21wdCBjZWxsIGJlZm9yZSBrZXJuZWwgZXhlY3V0aW9uIHRvIGFsbG93IHR5cGVhaGVhZC5cbiAgICAgIHRoaXMubmV3UHJvbXB0Q2VsbCgpO1xuICAgICAgYXdhaXQgdGhpcy5fZXhlY3V0ZShwcm9tcHRDZWxsKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBDaGVjayB3aGV0aGVyIHdlIHNob3VsZCBleGVjdXRlLlxuICAgIGNvbnN0IHNob3VsZEV4ZWN1dGUgPSBhd2FpdCB0aGlzLl9zaG91bGRFeGVjdXRlKHRpbWVvdXQpO1xuICAgIGlmICh0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgaWYgKHNob3VsZEV4ZWN1dGUpIHtcbiAgICAgIC8vIENyZWF0ZSBhIG5ldyBwcm9tcHQgY2VsbCBiZWZvcmUga2VybmVsIGV4ZWN1dGlvbiB0byBhbGxvdyB0eXBlYWhlYWQuXG4gICAgICB0aGlzLm5ld1Byb21wdENlbGwoKTtcbiAgICAgIHRoaXMucHJvbXB0Q2VsbCEuZWRpdG9yLmZvY3VzKCk7XG4gICAgICBhd2FpdCB0aGlzLl9leGVjdXRlKHByb21wdENlbGwpO1xuICAgIH0gZWxzZSB7XG4gICAgICAvLyBhZGQgYSBuZXdsaW5lIGlmIHdlIHNob3VsZG4ndCBleGVjdXRlXG4gICAgICBwcm9tcHRDZWxsLmVkaXRvci5uZXdJbmRlbnRlZExpbmUoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogR2V0IGEgY2VsbCBnaXZlbiBhIG1lc3NhZ2UgaWQuXG4gICAqXG4gICAqIEBwYXJhbSBtc2dJZCAtIFRoZSBtZXNzYWdlIGlkLlxuICAgKi9cbiAgZ2V0Q2VsbChtc2dJZDogc3RyaW5nKTogQ29kZUNlbGwgfCB1bmRlZmluZWQge1xuICAgIHJldHVybiB0aGlzLl9tc2dJZHMuZ2V0KG1zZ0lkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbmplY3QgYXJiaXRyYXJ5IGNvZGUgZm9yIHRoZSBjb25zb2xlIHRvIGV4ZWN1dGUgaW1tZWRpYXRlbHkuXG4gICAqXG4gICAqIEBwYXJhbSBjb2RlIC0gVGhlIGNvZGUgY29udGVudHMgb2YgdGhlIGNlbGwgYmVpbmcgaW5qZWN0ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IGluZGljYXRlcyB3aGVuIHRoZSBpbmplY3RlZCBjZWxsJ3MgZXhlY3V0aW9uIGVuZHMuXG4gICAqL1xuICBpbmplY3QoY29kZTogc3RyaW5nLCBtZXRhZGF0YTogSlNPTk9iamVjdCA9IHt9KTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgY2VsbCA9IHRoaXMuY3JlYXRlQ29kZUNlbGwoKTtcbiAgICBjZWxsLm1vZGVsLnZhbHVlLnRleHQgPSBjb2RlO1xuICAgIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKG1ldGFkYXRhKSkge1xuICAgICAgY2VsbC5tb2RlbC5tZXRhZGF0YS5zZXQoa2V5LCBtZXRhZGF0YVtrZXldKTtcbiAgICB9XG4gICAgdGhpcy5hZGRDZWxsKGNlbGwpO1xuICAgIHJldHVybiB0aGlzLl9leGVjdXRlKGNlbGwpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluc2VydCBhIGxpbmUgYnJlYWsgaW4gdGhlIHByb21wdCBjZWxsLlxuICAgKi9cbiAgaW5zZXJ0TGluZWJyZWFrKCk6IHZvaWQge1xuICAgIGNvbnN0IHByb21wdENlbGwgPSB0aGlzLnByb21wdENlbGw7XG4gICAgaWYgKCFwcm9tcHRDZWxsKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHByb21wdENlbGwuZWRpdG9yLm5ld0luZGVudGVkTGluZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlcGxhY2VzIHRoZSBzZWxlY3RlZCB0ZXh0IGluIHRoZSBwcm9tcHQgY2VsbC5cbiAgICpcbiAgICogQHBhcmFtIHRleHQgLSBUaGUgdGV4dCB0byByZXBsYWNlIHRoZSBzZWxlY3Rpb24uXG4gICAqL1xuICByZXBsYWNlU2VsZWN0aW9uKHRleHQ6IHN0cmluZyk6IHZvaWQge1xuICAgIGNvbnN0IHByb21wdENlbGwgPSB0aGlzLnByb21wdENlbGw7XG4gICAgaWYgKCFwcm9tcHRDZWxsKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHByb21wdENlbGwuZWRpdG9yLnJlcGxhY2VTZWxlY3Rpb24/Lih0ZXh0KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXJpYWxpemUgdGhlIG91dHB1dC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIG9ubHkgc2VyaWFsaXplcyB0aGUgY29kZSBjZWxscyBhbmQgdGhlIHByb21wdCBjZWxsIGlmIGl0IGV4aXN0cywgYW5kXG4gICAqIHNraXBzIGFueSBvbGQgYmFubmVyIGNlbGxzLlxuICAgKi9cbiAgc2VyaWFsaXplKCk6IG5iZm9ybWF0LklDb2RlQ2VsbFtdIHtcbiAgICBjb25zdCBjZWxsczogbmJmb3JtYXQuSUNvZGVDZWxsW10gPSBbXTtcbiAgICBlYWNoKHRoaXMuX2NlbGxzLCBjZWxsID0+IHtcbiAgICAgIGNvbnN0IG1vZGVsID0gY2VsbC5tb2RlbDtcbiAgICAgIGlmIChpc0NvZGVDZWxsTW9kZWwobW9kZWwpKSB7XG4gICAgICAgIGNlbGxzLnB1c2gobW9kZWwudG9KU09OKCkpO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgaWYgKHRoaXMucHJvbXB0Q2VsbCkge1xuICAgICAgY2VsbHMucHVzaCh0aGlzLnByb21wdENlbGwubW9kZWwudG9KU09OKCkpO1xuICAgIH1cbiAgICByZXR1cm4gY2VsbHM7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBtb3VzZWRvd25gIGV2ZW50cyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByaXZhdGUgX2V2dE1vdXNlRG93bihldmVudDogTW91c2VFdmVudCk6IHZvaWQge1xuICAgIGNvbnN0IHsgYnV0dG9uLCBzaGlmdEtleSB9ID0gZXZlbnQ7XG5cbiAgICAvLyBXZSBvbmx5IGhhbmRsZSBtYWluIG9yIHNlY29uZGFyeSBidXR0b24gYWN0aW9ucy5cbiAgICBpZiAoXG4gICAgICAhKGJ1dHRvbiA9PT0gMCB8fCBidXR0b24gPT09IDIpIHx8XG4gICAgICAvLyBTaGlmdCByaWdodC1jbGljayBnaXZlcyB0aGUgYnJvd3NlciBkZWZhdWx0IGJlaGF2aW9yLlxuICAgICAgKHNoaWZ0S2V5ICYmIGJ1dHRvbiA9PT0gMilcbiAgICApIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBsZXQgdGFyZ2V0ID0gZXZlbnQudGFyZ2V0IGFzIEhUTUxFbGVtZW50O1xuICAgIGNvbnN0IGNlbGxGaWx0ZXIgPSAobm9kZTogSFRNTEVsZW1lbnQpID0+XG4gICAgICBub2RlLmNsYXNzTGlzdC5jb250YWlucyhDT05TT0xFX0NFTExfQ0xBU1MpO1xuICAgIGxldCBjZWxsSW5kZXggPSBDZWxsRHJhZ1V0aWxzLmZpbmRDZWxsKHRhcmdldCwgdGhpcy5fY2VsbHMsIGNlbGxGaWx0ZXIpO1xuXG4gICAgaWYgKGNlbGxJbmRleCA9PT0gLTEpIHtcbiAgICAgIC8vIGBldmVudC50YXJnZXRgIHNvbWV0aW1lcyBnaXZlcyBhbiBvcnBoYW5lZCBub2RlIGluXG4gICAgICAvLyBGaXJlZm94IDU3LCB3aGljaCBjYW4gaGF2ZSBgbnVsbGAgYW55d2hlcmUgaW4gaXRzIHBhcmVudCBsaW5lLiBJZiB3ZSBmYWlsXG4gICAgICAvLyB0byBmaW5kIGEgY2VsbCB1c2luZyBgZXZlbnQudGFyZ2V0YCwgdHJ5IGFnYWluIHVzaW5nIGEgdGFyZ2V0XG4gICAgICAvLyByZWNvbnN0cnVjdGVkIGZyb20gdGhlIHBvc2l0aW9uIG9mIHRoZSBjbGljayBldmVudC5cbiAgICAgIHRhcmdldCA9IGRvY3VtZW50LmVsZW1lbnRGcm9tUG9pbnQoXG4gICAgICAgIGV2ZW50LmNsaWVudFgsXG4gICAgICAgIGV2ZW50LmNsaWVudFlcbiAgICAgICkgYXMgSFRNTEVsZW1lbnQ7XG4gICAgICBjZWxsSW5kZXggPSBDZWxsRHJhZ1V0aWxzLmZpbmRDZWxsKHRhcmdldCwgdGhpcy5fY2VsbHMsIGNlbGxGaWx0ZXIpO1xuICAgIH1cblxuICAgIGlmIChjZWxsSW5kZXggPT09IC0xKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgY29uc3QgY2VsbCA9IHRoaXMuX2NlbGxzLmdldChjZWxsSW5kZXgpO1xuXG4gICAgY29uc3QgdGFyZ2V0QXJlYTogQ2VsbERyYWdVdGlscy5JQ2VsbFRhcmdldEFyZWEgPVxuICAgICAgQ2VsbERyYWdVdGlscy5kZXRlY3RUYXJnZXRBcmVhKGNlbGwsIGV2ZW50LnRhcmdldCBhcyBIVE1MRWxlbWVudCk7XG5cbiAgICBpZiAodGFyZ2V0QXJlYSA9PT0gJ3Byb21wdCcpIHtcbiAgICAgIHRoaXMuX2RyYWdEYXRhID0ge1xuICAgICAgICBwcmVzc1g6IGV2ZW50LmNsaWVudFgsXG4gICAgICAgIHByZXNzWTogZXZlbnQuY2xpZW50WSxcbiAgICAgICAgaW5kZXg6IGNlbGxJbmRleFxuICAgICAgfTtcblxuICAgICAgdGhpcy5fZm9jdXNlZENlbGwgPSBjZWxsO1xuXG4gICAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdtb3VzZXVwJywgdGhpcywgdHJ1ZSk7XG4gICAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdtb3VzZW1vdmUnLCB0aGlzLCB0cnVlKTtcbiAgICAgIGV2ZW50LnByZXZlbnREZWZhdWx0KCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgbW91c2Vtb3ZlYCBldmVudCBvZiB3aWRnZXRcbiAgICovXG4gIHByaXZhdGUgX2V2dE1vdXNlTW92ZShldmVudDogTW91c2VFdmVudCkge1xuICAgIGNvbnN0IGRhdGEgPSB0aGlzLl9kcmFnRGF0YTtcbiAgICBpZiAoXG4gICAgICBkYXRhICYmXG4gICAgICBDZWxsRHJhZ1V0aWxzLnNob3VsZFN0YXJ0RHJhZyhcbiAgICAgICAgZGF0YS5wcmVzc1gsXG4gICAgICAgIGRhdGEucHJlc3NZLFxuICAgICAgICBldmVudC5jbGllbnRYLFxuICAgICAgICBldmVudC5jbGllbnRZXG4gICAgICApXG4gICAgKSB7XG4gICAgICB2b2lkIHRoaXMuX3N0YXJ0RHJhZyhkYXRhLmluZGV4LCBldmVudC5jbGllbnRYLCBldmVudC5jbGllbnRZKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogU3RhcnQgYSBkcmFnIGV2ZW50XG4gICAqL1xuICBwcml2YXRlIF9zdGFydERyYWcoXG4gICAgaW5kZXg6IG51bWJlcixcbiAgICBjbGllbnRYOiBudW1iZXIsXG4gICAgY2xpZW50WTogbnVtYmVyXG4gICk6IFByb21pc2U8dm9pZD4ge1xuICAgIGNvbnN0IGNlbGxNb2RlbCA9IHRoaXMuX2ZvY3VzZWRDZWxsIS5tb2RlbCBhcyBJQ29kZUNlbGxNb2RlbDtcbiAgICBjb25zdCBzZWxlY3RlZDogbmJmb3JtYXQuSUNlbGxbXSA9IFtjZWxsTW9kZWwudG9KU09OKCldO1xuXG4gICAgY29uc3QgZHJhZ0ltYWdlID0gQ2VsbERyYWdVdGlscy5jcmVhdGVDZWxsRHJhZ0ltYWdlKFxuICAgICAgdGhpcy5fZm9jdXNlZENlbGwhLFxuICAgICAgc2VsZWN0ZWRcbiAgICApO1xuXG4gICAgdGhpcy5fZHJhZyA9IG5ldyBEcmFnKHtcbiAgICAgIG1pbWVEYXRhOiBuZXcgTWltZURhdGEoKSxcbiAgICAgIGRyYWdJbWFnZSxcbiAgICAgIHByb3Bvc2VkQWN0aW9uOiAnY29weScsXG4gICAgICBzdXBwb3J0ZWRBY3Rpb25zOiAnY29weScsXG4gICAgICBzb3VyY2U6IHRoaXNcbiAgICB9KTtcblxuICAgIHRoaXMuX2RyYWcubWltZURhdGEuc2V0RGF0YShKVVBZVEVSX0NFTExfTUlNRSwgc2VsZWN0ZWQpO1xuICAgIGNvbnN0IHRleHRDb250ZW50ID0gY2VsbE1vZGVsLnZhbHVlLnRleHQ7XG4gICAgdGhpcy5fZHJhZy5taW1lRGF0YS5zZXREYXRhKCd0ZXh0L3BsYWluJywgdGV4dENvbnRlbnQpO1xuXG4gICAgdGhpcy5fZm9jdXNlZENlbGwgPSBudWxsO1xuXG4gICAgZG9jdW1lbnQucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2Vtb3ZlJywgdGhpcywgdHJ1ZSk7XG4gICAgZG9jdW1lbnQucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2V1cCcsIHRoaXMsIHRydWUpO1xuICAgIHJldHVybiB0aGlzLl9kcmFnLnN0YXJ0KGNsaWVudFgsIGNsaWVudFkpLnRoZW4oKCkgPT4ge1xuICAgICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICB0aGlzLl9kcmFnID0gbnVsbDtcbiAgICAgIHRoaXMuX2RyYWdEYXRhID0gbnVsbDtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2QgaW1wbGVtZW50cyB0aGUgRE9NIGBFdmVudExpc3RlbmVyYCBpbnRlcmZhY2UgYW5kIGlzXG4gICAqIGNhbGxlZCBpbiByZXNwb25zZSB0byBldmVudHMgb24gdGhlIG5vdGVib29rIHBhbmVsJ3Mgbm9kZS4gSXQgc2hvdWxkXG4gICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgKi9cbiAgaGFuZGxlRXZlbnQoZXZlbnQ6IEV2ZW50KTogdm9pZCB7XG4gICAgc3dpdGNoIChldmVudC50eXBlKSB7XG4gICAgICBjYXNlICdrZXlkb3duJzpcbiAgICAgICAgdGhpcy5fZXZ0S2V5RG93bihldmVudCBhcyBLZXlib2FyZEV2ZW50KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdtb3VzZWRvd24nOlxuICAgICAgICB0aGlzLl9ldnRNb3VzZURvd24oZXZlbnQgYXMgTW91c2VFdmVudCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbW91c2Vtb3ZlJzpcbiAgICAgICAgdGhpcy5fZXZ0TW91c2VNb3ZlKGV2ZW50IGFzIE1vdXNlRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ21vdXNldXAnOlxuICAgICAgICB0aGlzLl9ldnRNb3VzZVVwKGV2ZW50IGFzIE1vdXNlRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYGFmdGVyX2F0dGFjaGAgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25BZnRlckF0dGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBjb25zdCBub2RlID0gdGhpcy5ub2RlO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcigna2V5ZG93bicsIHRoaXMsIHRydWUpO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzKTtcbiAgICBub2RlLmFkZEV2ZW50TGlzdGVuZXIoJ21vdXNlZG93bicsIHRoaXMpO1xuICAgIC8vIENyZWF0ZSBhIHByb21wdCBpZiBuZWNlc3NhcnkuXG4gICAgaWYgKCF0aGlzLnByb21wdENlbGwpIHtcbiAgICAgIHRoaXMubmV3UHJvbXB0Q2VsbCgpO1xuICAgIH0gZWxzZSB7XG4gICAgICB0aGlzLnByb21wdENlbGwuZWRpdG9yLmZvY3VzKCk7XG4gICAgICB0aGlzLnVwZGF0ZSgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYGJlZm9yZS1kZXRhY2hgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQmVmb3JlRGV0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGNvbnN0IG5vZGUgPSB0aGlzLm5vZGU7XG4gICAgbm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdrZXlkb3duJywgdGhpcywgdHJ1ZSk7XG4gICAgbm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdjbGljaycsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgJ2FjdGl2YXRlLXJlcXVlc3QnYCBtZXNzYWdlcy5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFjdGl2YXRlUmVxdWVzdChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBjb25zdCBlZGl0b3IgPSB0aGlzLnByb21wdENlbGwgJiYgdGhpcy5wcm9tcHRDZWxsLmVkaXRvcjtcbiAgICBpZiAoZWRpdG9yKSB7XG4gICAgICBlZGl0b3IuZm9jdXMoKTtcbiAgICB9XG4gICAgdGhpcy51cGRhdGUoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBNYWtlIGEgbmV3IHByb21wdCBjZWxsLlxuICAgKi9cbiAgcHJvdGVjdGVkIG5ld1Byb21wdENlbGwoKTogdm9pZCB7XG4gICAgbGV0IHByb21wdENlbGwgPSB0aGlzLnByb21wdENlbGw7XG4gICAgY29uc3QgaW5wdXQgPSB0aGlzLl9pbnB1dDtcblxuICAgIC8vIE1ha2UgdGhlIGxhc3QgcHJvbXB0IHJlYWQtb25seSwgY2xlYXIgaXRzIHNpZ25hbHMsIGFuZCBtb3ZlIHRvIGNvbnRlbnQuXG4gICAgaWYgKHByb21wdENlbGwpIHtcbiAgICAgIHByb21wdENlbGwucmVhZE9ubHkgPSB0cnVlO1xuICAgICAgcHJvbXB0Q2VsbC5yZW1vdmVDbGFzcyhQUk9NUFRfQ0xBU1MpO1xuICAgICAgU2lnbmFsLmNsZWFyRGF0YShwcm9tcHRDZWxsLmVkaXRvcik7XG4gICAgICBjb25zdCBjaGlsZCA9IGlucHV0LndpZGdldHNbMF07XG4gICAgICBjaGlsZC5wYXJlbnQgPSBudWxsO1xuICAgICAgdGhpcy5hZGRDZWxsKHByb21wdENlbGwpO1xuICAgIH1cblxuICAgIC8vIENyZWF0ZSB0aGUgbmV3IHByb21wdCBjZWxsLlxuICAgIGNvbnN0IGZhY3RvcnkgPSB0aGlzLmNvbnRlbnRGYWN0b3J5O1xuICAgIGNvbnN0IG9wdGlvbnMgPSB0aGlzLl9jcmVhdGVDb2RlQ2VsbE9wdGlvbnMoKTtcbiAgICBwcm9tcHRDZWxsID0gZmFjdG9yeS5jcmVhdGVDb2RlQ2VsbChvcHRpb25zKTtcbiAgICBwcm9tcHRDZWxsLm1vZGVsLm1pbWVUeXBlID0gdGhpcy5fbWltZXR5cGU7XG4gICAgcHJvbXB0Q2VsbC5hZGRDbGFzcyhQUk9NUFRfQ0xBU1MpO1xuXG4gICAgLy8gQWRkIHRoZSBwcm9tcHQgY2VsbCB0byB0aGUgRE9NLCBtYWtpbmcgYHRoaXMucHJvbXB0Q2VsbGAgdmFsaWQgYWdhaW4uXG4gICAgdGhpcy5faW5wdXQuYWRkV2lkZ2V0KHByb21wdENlbGwpO1xuXG4gICAgLy8gU3VwcHJlc3MgdGhlIGRlZmF1bHQgXCJFbnRlclwiIGtleSBoYW5kbGluZy5cbiAgICBjb25zdCBlZGl0b3IgPSBwcm9tcHRDZWxsLmVkaXRvcjtcbiAgICBlZGl0b3IuYWRkS2V5ZG93bkhhbmRsZXIodGhpcy5fb25FZGl0b3JLZXlkb3duKTtcblxuICAgIHRoaXMuX2hpc3RvcnkuZWRpdG9yID0gZWRpdG9yO1xuICAgIHRoaXMuX3Byb21wdENlbGxDcmVhdGVkLmVtaXQocHJvbXB0Q2VsbCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGB1cGRhdGUtcmVxdWVzdGAgbWVzc2FnZXMuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIFByaXZhdGUuc2Nyb2xsVG9Cb3R0b20odGhpcy5fY29udGVudC5ub2RlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGAna2V5ZG93bidgIGV2ZW50IGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0S2V5RG93bihldmVudDogS2V5Ym9hcmRFdmVudCk6IHZvaWQge1xuICAgIGNvbnN0IGVkaXRvciA9IHRoaXMucHJvbXB0Q2VsbCAmJiB0aGlzLnByb21wdENlbGwuZWRpdG9yO1xuICAgIGlmICghZWRpdG9yKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGlmIChldmVudC5rZXlDb2RlID09PSAxMyAmJiAhZWRpdG9yLmhhc0ZvY3VzKCkpIHtcbiAgICAgIGV2ZW50LnByZXZlbnREZWZhdWx0KCk7XG4gICAgICBlZGl0b3IuZm9jdXMoKTtcbiAgICB9IGVsc2UgaWYgKGV2ZW50LmtleUNvZGUgPT09IDI3ICYmIGVkaXRvci5oYXNGb2N1cygpKSB7XG4gICAgICAvLyBTZXQgdG8gY29tbWFuZCBtb2RlXG4gICAgICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgZXZlbnQuc3RvcFByb3BhZ2F0aW9uKCk7XG4gICAgICB0aGlzLm5vZGUuZm9jdXMoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBgJ21vdXNldXAnYCBldmVudCBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByaXZhdGUgX2V2dE1vdXNlVXAoZXZlbnQ6IE1vdXNlRXZlbnQpOiB2b2lkIHtcbiAgICBpZiAoXG4gICAgICB0aGlzLnByb21wdENlbGwgJiZcbiAgICAgIHRoaXMucHJvbXB0Q2VsbC5ub2RlLmNvbnRhaW5zKGV2ZW50LnRhcmdldCBhcyBIVE1MRWxlbWVudClcbiAgICApIHtcbiAgICAgIHRoaXMucHJvbXB0Q2VsbC5lZGl0b3IuZm9jdXMoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogRXhlY3V0ZSB0aGUgY29kZSBpbiB0aGUgY3VycmVudCBwcm9tcHQgY2VsbC5cbiAgICovXG4gIHByaXZhdGUgX2V4ZWN1dGUoY2VsbDogQ29kZUNlbGwpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBjb25zdCBzb3VyY2UgPSBjZWxsLm1vZGVsLnZhbHVlLnRleHQ7XG4gICAgdGhpcy5faGlzdG9yeS5wdXNoKHNvdXJjZSk7XG4gICAgLy8gSWYgdGhlIHNvdXJjZSBvZiB0aGUgY29uc29sZSBpcyBqdXN0IFwiY2xlYXJcIiwgY2xlYXIgdGhlIGNvbnNvbGUgYXMgd2VcbiAgICAvLyBkbyBpbiBJUHl0aG9uIG9yIFF0Q29uc29sZS5cbiAgICBpZiAoc291cmNlID09PSAnY2xlYXInIHx8IHNvdXJjZSA9PT0gJyVjbGVhcicpIHtcbiAgICAgIHRoaXMuY2xlYXIoKTtcbiAgICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUodm9pZCAwKTtcbiAgICB9XG4gICAgY2VsbC5tb2RlbC5jb250ZW50Q2hhbmdlZC5jb25uZWN0KHRoaXMudXBkYXRlLCB0aGlzKTtcbiAgICBjb25zdCBvblN1Y2Nlc3MgPSAodmFsdWU6IEtlcm5lbE1lc3NhZ2UuSUV4ZWN1dGVSZXBseU1zZykgPT4ge1xuICAgICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBpZiAodmFsdWUgJiYgdmFsdWUuY29udGVudC5zdGF0dXMgPT09ICdvaycpIHtcbiAgICAgICAgY29uc3QgY29udGVudCA9IHZhbHVlLmNvbnRlbnQ7XG4gICAgICAgIC8vIFVzZSBkZXByZWNhdGVkIHBheWxvYWRzIGZvciBiYWNrd2FyZHMgY29tcGF0aWJpbGl0eS5cbiAgICAgICAgaWYgKGNvbnRlbnQucGF5bG9hZCAmJiBjb250ZW50LnBheWxvYWQubGVuZ3RoKSB7XG4gICAgICAgICAgY29uc3Qgc2V0TmV4dElucHV0ID0gY29udGVudC5wYXlsb2FkLmZpbHRlcihpID0+IHtcbiAgICAgICAgICAgIHJldHVybiAoaSBhcyBhbnkpLnNvdXJjZSA9PT0gJ3NldF9uZXh0X2lucHV0JztcbiAgICAgICAgICB9KVswXTtcbiAgICAgICAgICBpZiAoc2V0TmV4dElucHV0KSB7XG4gICAgICAgICAgICBjb25zdCB0ZXh0ID0gKHNldE5leHRJbnB1dCBhcyBhbnkpLnRleHQ7XG4gICAgICAgICAgICAvLyBJZ25vcmUgdGhlIGByZXBsYWNlYCB2YWx1ZSBhbmQgYWx3YXlzIHNldCB0aGUgbmV4dCBjZWxsLlxuICAgICAgICAgICAgY2VsbC5tb2RlbC52YWx1ZS50ZXh0ID0gdGV4dDtcbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH0gZWxzZSBpZiAodmFsdWUgJiYgdmFsdWUuY29udGVudC5zdGF0dXMgPT09ICdlcnJvcicpIHtcbiAgICAgICAgZWFjaCh0aGlzLl9jZWxscywgKGNlbGw6IENvZGVDZWxsKSA9PiB7XG4gICAgICAgICAgaWYgKGNlbGwubW9kZWwuZXhlY3V0aW9uQ291bnQgPT09IG51bGwpIHtcbiAgICAgICAgICAgIGNlbGwuc2V0UHJvbXB0KCcnKTtcbiAgICAgICAgICB9XG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgICAgY2VsbC5tb2RlbC5jb250ZW50Q2hhbmdlZC5kaXNjb25uZWN0KHRoaXMudXBkYXRlLCB0aGlzKTtcbiAgICAgIHRoaXMudXBkYXRlKCk7XG4gICAgICB0aGlzLl9leGVjdXRlZC5lbWl0KG5ldyBEYXRlKCkpO1xuICAgIH07XG4gICAgY29uc3Qgb25GYWlsdXJlID0gKCkgPT4ge1xuICAgICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjZWxsLm1vZGVsLmNvbnRlbnRDaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy51cGRhdGUsIHRoaXMpO1xuICAgICAgdGhpcy51cGRhdGUoKTtcbiAgICB9O1xuICAgIHJldHVybiBDb2RlQ2VsbC5leGVjdXRlKGNlbGwsIHRoaXMuc2Vzc2lvbkNvbnRleHQpLnRoZW4oXG4gICAgICBvblN1Y2Nlc3MsXG4gICAgICBvbkZhaWx1cmVcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSB0aGUgY29uc29sZSBiYXNlZCBvbiB0aGUga2VybmVsIGluZm8uXG4gICAqL1xuICBwcml2YXRlIF9oYW5kbGVJbmZvKGluZm86IEtlcm5lbE1lc3NhZ2UuSUluZm9SZXBseU1zZ1snY29udGVudCddKTogdm9pZCB7XG4gICAgaWYgKGluZm8uc3RhdHVzICE9PSAnb2snKSB7XG4gICAgICB0aGlzLl9iYW5uZXIhLm1vZGVsLnZhbHVlLnRleHQgPSAnRXJyb3IgaW4gZ2V0dGluZyBrZXJuZWwgYmFubmVyJztcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fYmFubmVyIS5tb2RlbC52YWx1ZS50ZXh0ID0gaW5mby5iYW5uZXI7XG4gICAgY29uc3QgbGFuZyA9IGluZm8ubGFuZ3VhZ2VfaW5mbyBhcyBuYmZvcm1hdC5JTGFuZ3VhZ2VJbmZvTWV0YWRhdGE7XG4gICAgdGhpcy5fbWltZXR5cGUgPSB0aGlzLl9taW1lVHlwZVNlcnZpY2UuZ2V0TWltZVR5cGVCeUxhbmd1YWdlKGxhbmcpO1xuICAgIGlmICh0aGlzLnByb21wdENlbGwpIHtcbiAgICAgIHRoaXMucHJvbXB0Q2VsbC5tb2RlbC5taW1lVHlwZSA9IHRoaXMuX21pbWV0eXBlO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgdGhlIG9wdGlvbnMgdXNlZCB0byBpbml0aWFsaXplIGEgY29kZSBjZWxsIHdpZGdldC5cbiAgICovXG4gIHByaXZhdGUgX2NyZWF0ZUNvZGVDZWxsT3B0aW9ucygpOiBDb2RlQ2VsbC5JT3B0aW9ucyB7XG4gICAgY29uc3QgY29udGVudEZhY3RvcnkgPSB0aGlzLmNvbnRlbnRGYWN0b3J5O1xuICAgIGNvbnN0IG1vZGVsRmFjdG9yeSA9IHRoaXMubW9kZWxGYWN0b3J5O1xuICAgIGNvbnN0IG1vZGVsID0gbW9kZWxGYWN0b3J5LmNyZWF0ZUNvZGVDZWxsKHt9KTtcbiAgICBjb25zdCByZW5kZXJtaW1lID0gdGhpcy5yZW5kZXJtaW1lO1xuICAgIGNvbnN0IGVkaXRvckNvbmZpZyA9IHRoaXMuZWRpdG9yQ29uZmlnO1xuICAgIHJldHVybiB7XG4gICAgICBtb2RlbCxcbiAgICAgIHJlbmRlcm1pbWUsXG4gICAgICBjb250ZW50RmFjdG9yeSxcbiAgICAgIGVkaXRvckNvbmZpZyxcbiAgICAgIHBsYWNlaG9sZGVyOiBmYWxzZVxuICAgIH07XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGNlbGwgZGlzcG9zZWQgc2lnbmFscy5cbiAgICovXG4gIHByaXZhdGUgX29uQ2VsbERpc3Bvc2VkKHNlbmRlcjogQ2VsbCwgYXJnczogdm9pZCk6IHZvaWQge1xuICAgIGlmICghdGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICB0aGlzLl9jZWxscy5yZW1vdmVWYWx1ZShzZW5kZXIpO1xuICAgICAgY29uc3QgbXNnSWQgPSB0aGlzLl9tc2dJZENlbGxzLmdldChzZW5kZXIgYXMgQ29kZUNlbGwpO1xuICAgICAgaWYgKG1zZ0lkKSB7XG4gICAgICAgIHRoaXMuX21zZ0lkQ2VsbHMuZGVsZXRlKHNlbmRlciBhcyBDb2RlQ2VsbCk7XG4gICAgICAgIHRoaXMuX21zZ0lkcy5kZWxldGUobXNnSWQpO1xuICAgICAgfVxuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUZXN0IHdoZXRoZXIgd2Ugc2hvdWxkIGV4ZWN1dGUgdGhlIHByb21wdCBjZWxsLlxuICAgKi9cbiAgcHJpdmF0ZSBfc2hvdWxkRXhlY3V0ZSh0aW1lb3V0OiBudW1iZXIpOiBQcm9taXNlPGJvb2xlYW4+IHtcbiAgICBjb25zdCBwcm9tcHRDZWxsID0gdGhpcy5wcm9tcHRDZWxsO1xuICAgIGlmICghcHJvbXB0Q2VsbCkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShmYWxzZSk7XG4gICAgfVxuICAgIGNvbnN0IG1vZGVsID0gcHJvbXB0Q2VsbC5tb2RlbDtcbiAgICBjb25zdCBjb2RlID0gbW9kZWwudmFsdWUudGV4dDtcbiAgICByZXR1cm4gbmV3IFByb21pc2U8Ym9vbGVhbj4oKHJlc29sdmUsIHJlamVjdCkgPT4ge1xuICAgICAgY29uc3QgdGltZXIgPSBzZXRUaW1lb3V0KCgpID0+IHtcbiAgICAgICAgcmVzb2x2ZSh0cnVlKTtcbiAgICAgIH0sIHRpbWVvdXQpO1xuICAgICAgY29uc3Qga2VybmVsID0gdGhpcy5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5rZXJuZWw7XG4gICAgICBpZiAoIWtlcm5lbCkge1xuICAgICAgICByZXNvbHZlKGZhbHNlKTtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAga2VybmVsXG4gICAgICAgIC5yZXF1ZXN0SXNDb21wbGV0ZSh7IGNvZGUgfSlcbiAgICAgICAgLnRoZW4oaXNDb21wbGV0ZSA9PiB7XG4gICAgICAgICAgY2xlYXJUaW1lb3V0KHRpbWVyKTtcbiAgICAgICAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgICByZXNvbHZlKGZhbHNlKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgaWYgKGlzQ29tcGxldGUuY29udGVudC5zdGF0dXMgIT09ICdpbmNvbXBsZXRlJykge1xuICAgICAgICAgICAgcmVzb2x2ZSh0cnVlKTtcbiAgICAgICAgICAgIHJldHVybjtcbiAgICAgICAgICB9XG4gICAgICAgICAgcmVzb2x2ZShmYWxzZSk7XG4gICAgICAgIH0pXG4gICAgICAgIC5jYXRjaCgoKSA9PiB7XG4gICAgICAgICAgcmVzb2x2ZSh0cnVlKTtcbiAgICAgICAgfSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEga2V5ZG93biBldmVudCBvbiBhbiBlZGl0b3IuXG4gICAqL1xuICBwcml2YXRlIF9vbkVkaXRvcktleWRvd24oZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3IsIGV2ZW50OiBLZXlib2FyZEV2ZW50KSB7XG4gICAgLy8gU3VwcHJlc3MgXCJFbnRlclwiIGV2ZW50cy5cbiAgICByZXR1cm4gZXZlbnQua2V5Q29kZSA9PT0gMTM7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSBrZXJuZWwuXG4gICAqL1xuICBwcml2YXRlIGFzeW5jIF9vbktlcm5lbENoYW5nZWQoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgdGhpcy5jbGVhcigpO1xuICAgIGlmICh0aGlzLl9iYW5uZXIpIHtcbiAgICAgIHRoaXMuX2Jhbm5lci5kaXNwb3NlKCk7XG4gICAgICB0aGlzLl9iYW5uZXIgPSBudWxsO1xuICAgIH1cbiAgICB0aGlzLmFkZEJhbm5lcigpO1xuICAgIGlmICh0aGlzLnNlc3Npb25Db250ZXh0LnNlc3Npb24/Lmtlcm5lbCkge1xuICAgICAgdGhpcy5faGFuZGxlSW5mbyhhd2FpdCB0aGlzLnNlc3Npb25Db250ZXh0LnNlc3Npb24ua2VybmVsLmluZm8pO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIGtlcm5lbCBzdGF0dXMuXG4gICAqL1xuICBwcml2YXRlIGFzeW5jIF9vbktlcm5lbFN0YXR1c0NoYW5nZWQoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3Qga2VybmVsID0gdGhpcy5zZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5rZXJuZWw7XG4gICAgaWYgKGtlcm5lbD8uc3RhdHVzID09PSAncmVzdGFydGluZycpIHtcbiAgICAgIHRoaXMuYWRkQmFubmVyKCk7XG4gICAgICB0aGlzLl9oYW5kbGVJbmZvKGF3YWl0IGtlcm5lbD8uaW5mbyk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfYmFubmVyOiBSYXdDZWxsIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX2NlbGxzOiBJT2JzZXJ2YWJsZUxpc3Q8Q2VsbD47XG4gIHByaXZhdGUgX2NvbnRlbnQ6IFBhbmVsO1xuICBwcml2YXRlIF9leGVjdXRlZCA9IG5ldyBTaWduYWw8dGhpcywgRGF0ZT4odGhpcyk7XG4gIHByaXZhdGUgX2hpc3Rvcnk6IElDb25zb2xlSGlzdG9yeTtcbiAgcHJpdmF0ZSBfaW5wdXQ6IFBhbmVsO1xuICBwcml2YXRlIF9taW1ldHlwZSA9ICd0ZXh0L3gtaXB5dGhvbic7XG4gIHByaXZhdGUgX21pbWVUeXBlU2VydmljZTogSUVkaXRvck1pbWVUeXBlU2VydmljZTtcbiAgcHJpdmF0ZSBfbXNnSWRzID0gbmV3IE1hcDxzdHJpbmcsIENvZGVDZWxsPigpO1xuICBwcml2YXRlIF9tc2dJZENlbGxzID0gbmV3IE1hcDxDb2RlQ2VsbCwgc3RyaW5nPigpO1xuICBwcml2YXRlIF9wcm9tcHRDZWxsQ3JlYXRlZCA9IG5ldyBTaWduYWw8dGhpcywgQ29kZUNlbGw+KHRoaXMpO1xuICBwcml2YXRlIF9kcmFnRGF0YToge1xuICAgIHByZXNzWDogbnVtYmVyO1xuICAgIHByZXNzWTogbnVtYmVyO1xuICAgIGluZGV4OiBudW1iZXI7XG4gIH0gfCBudWxsID0gbnVsbDtcbiAgcHJpdmF0ZSBfZHJhZzogRHJhZyB8IG51bGwgPSBudWxsO1xuICBwcml2YXRlIF9mb2N1c2VkQ2VsbDogQ2VsbCB8IG51bGwgPSBudWxsO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBDb2RlQ29uc29sZSBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIENvZGVDb25zb2xlIHtcbiAgLyoqXG4gICAqIFRoZSBpbml0aWFsaXphdGlvbiBvcHRpb25zIGZvciBhIGNvbnNvbGUgd2lkZ2V0LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGNvbnRlbnQgZmFjdG9yeSBmb3IgdGhlIGNvbnNvbGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIGNvbnRlbnRGYWN0b3J5OiBJQ29udGVudEZhY3Rvcnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbW9kZWwgZmFjdG9yeSBmb3IgdGhlIGNvbnNvbGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIG1vZGVsRmFjdG9yeT86IElNb2RlbEZhY3Rvcnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbWltZSByZW5kZXJlciBmb3IgdGhlIGNvbnNvbGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY2xpZW50IHNlc3Npb24gZm9yIHRoZSBjb25zb2xlIHdpZGdldC5cbiAgICAgKi9cbiAgICBzZXNzaW9uQ29udGV4dDogSVNlc3Npb25Db250ZXh0O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHNlcnZpY2UgdXNlZCB0byBsb29rIHVwIG1pbWUgdHlwZXMuXG4gICAgICovXG4gICAgbWltZVR5cGVTZXJ2aWNlOiBJRWRpdG9yTWltZVR5cGVTZXJ2aWNlO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgY29udGVudCBmYWN0b3J5IGZvciBjb25zb2xlIGNoaWxkcmVuLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29udGVudEZhY3RvcnkgZXh0ZW5kcyBDZWxsLklDb250ZW50RmFjdG9yeSB7XG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGEgbmV3IGNvZGUgY2VsbCB3aWRnZXQuXG4gICAgICovXG4gICAgY3JlYXRlQ29kZUNlbGwob3B0aW9uczogQ29kZUNlbGwuSU9wdGlvbnMpOiBDb2RlQ2VsbDtcblxuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyByYXcgY2VsbCB3aWRnZXQuXG4gICAgICovXG4gICAgY3JlYXRlUmF3Q2VsbChvcHRpb25zOiBSYXdDZWxsLklPcHRpb25zKTogUmF3Q2VsbDtcbiAgfVxuXG4gIC8qKlxuICAgKiBEZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIGBJQ29udGVudEZhY3RvcnlgLlxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIENvbnRlbnRGYWN0b3J5XG4gICAgZXh0ZW5kcyBDZWxsLkNvbnRlbnRGYWN0b3J5XG4gICAgaW1wbGVtZW50cyBJQ29udGVudEZhY3RvcnlcbiAge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBjb2RlIGNlbGwgd2lkZ2V0LlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIElmIG5vIGNlbGwgY29udGVudCBmYWN0b3J5IGlzIHBhc3NlZCBpbiB3aXRoIHRoZSBvcHRpb25zLCB0aGUgb25lIG9uIHRoZVxuICAgICAqIG5vdGVib29rIGNvbnRlbnQgZmFjdG9yeSBpcyB1c2VkLlxuICAgICAqL1xuICAgIGNyZWF0ZUNvZGVDZWxsKG9wdGlvbnM6IENvZGVDZWxsLklPcHRpb25zKTogQ29kZUNlbGwge1xuICAgICAgaWYgKCFvcHRpb25zLmNvbnRlbnRGYWN0b3J5KSB7XG4gICAgICAgIG9wdGlvbnMuY29udGVudEZhY3RvcnkgPSB0aGlzO1xuICAgICAgfVxuICAgICAgcmV0dXJuIG5ldyBDb2RlQ2VsbChvcHRpb25zKS5pbml0aWFsaXplU3RhdGUoKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSBuZXcgcmF3IGNlbGwgd2lkZ2V0LlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIElmIG5vIGNlbGwgY29udGVudCBmYWN0b3J5IGlzIHBhc3NlZCBpbiB3aXRoIHRoZSBvcHRpb25zLCB0aGUgb25lIG9uIHRoZVxuICAgICAqIG5vdGVib29rIGNvbnRlbnQgZmFjdG9yeSBpcyB1c2VkLlxuICAgICAqL1xuICAgIGNyZWF0ZVJhd0NlbGwob3B0aW9uczogUmF3Q2VsbC5JT3B0aW9ucyk6IFJhd0NlbGwge1xuICAgICAgaWYgKCFvcHRpb25zLmNvbnRlbnRGYWN0b3J5KSB7XG4gICAgICAgIG9wdGlvbnMuY29udGVudEZhY3RvcnkgPSB0aGlzO1xuICAgICAgfVxuICAgICAgcmV0dXJuIG5ldyBSYXdDZWxsKG9wdGlvbnMpLmluaXRpYWxpemVTdGF0ZSgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBBIG5hbWVzcGFjZSBmb3IgdGhlIGNvZGUgY29uc29sZSBjb250ZW50IGZhY3RvcnkuXG4gICAqL1xuICBleHBvcnQgbmFtZXNwYWNlIENvbnRlbnRGYWN0b3J5IHtcbiAgICAvKipcbiAgICAgKiBBbiBpbml0aWFsaXplIG9wdGlvbnMgZm9yIGBDb250ZW50RmFjdG9yeWAuXG4gICAgICovXG4gICAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyBleHRlbmRzIENlbGwuSUNvbnRlbnRGYWN0b3J5IHt9XG4gIH1cblxuICAvKipcbiAgICogQSBkZWZhdWx0IGNvbnRlbnQgZmFjdG9yeSBmb3IgdGhlIGNvZGUgY29uc29sZS5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBkZWZhdWx0Q29udGVudEZhY3Rvcnk6IElDb250ZW50RmFjdG9yeSA9IG5ldyBDb250ZW50RmFjdG9yeSgpO1xuXG4gIC8qKlxuICAgKiBBIG1vZGVsIGZhY3RvcnkgZm9yIGEgY29uc29sZSB3aWRnZXQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElNb2RlbEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIFRoZSBmYWN0b3J5IGZvciBjb2RlIGNlbGwgY29udGVudC5cbiAgICAgKi9cbiAgICByZWFkb25seSBjb2RlQ2VsbENvbnRlbnRGYWN0b3J5OiBDb2RlQ2VsbE1vZGVsLklDb250ZW50RmFjdG9yeTtcblxuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBjb2RlIGNlbGwuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gb3B0aW9ucyAtIFRoZSBvcHRpb25zIHVzZWQgdG8gY3JlYXRlIHRoZSBjZWxsLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBuZXcgY29kZSBjZWxsLiBJZiBhIHNvdXJjZSBjZWxsIGlzIHByb3ZpZGVkLCB0aGVcbiAgICAgKiAgIG5ldyBjZWxsIHdpbGwgYmUgaW5pdGlhbGl6ZWQgd2l0aCB0aGUgZGF0YSBmcm9tIHRoZSBzb3VyY2UuXG4gICAgICovXG4gICAgY3JlYXRlQ29kZUNlbGwob3B0aW9uczogQ29kZUNlbGxNb2RlbC5JT3B0aW9ucyk6IElDb2RlQ2VsbE1vZGVsO1xuXG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGEgbmV3IHJhdyBjZWxsLlxuICAgICAqXG4gICAgICogQHBhcmFtIG9wdGlvbnMgLSBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSB0aGUgY2VsbC5cbiAgICAgKlxuICAgICAqIEByZXR1cm5zIEEgbmV3IHJhdyBjZWxsLiBJZiBhIHNvdXJjZSBjZWxsIGlzIHByb3ZpZGVkLCB0aGVcbiAgICAgKiAgIG5ldyBjZWxsIHdpbGwgYmUgaW5pdGlhbGl6ZWQgd2l0aCB0aGUgZGF0YSBmcm9tIHRoZSBzb3VyY2UuXG4gICAgICovXG4gICAgY3JlYXRlUmF3Q2VsbChvcHRpb25zOiBDZWxsTW9kZWwuSU9wdGlvbnMpOiBJUmF3Q2VsbE1vZGVsO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIGFuIGBJTW9kZWxGYWN0b3J5YC5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBNb2RlbEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyBjZWxsIG1vZGVsIGZhY3RvcnkuXG4gICAgICovXG4gICAgY29uc3RydWN0b3Iob3B0aW9uczogSU1vZGVsRmFjdG9yeU9wdGlvbnMgPSB7fSkge1xuICAgICAgdGhpcy5jb2RlQ2VsbENvbnRlbnRGYWN0b3J5ID1cbiAgICAgICAgb3B0aW9ucy5jb2RlQ2VsbENvbnRlbnRGYWN0b3J5IHx8IENvZGVDZWxsTW9kZWwuZGVmYXVsdENvbnRlbnRGYWN0b3J5O1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBmYWN0b3J5IGZvciBvdXRwdXQgYXJlYSBtb2RlbHMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY29kZUNlbGxDb250ZW50RmFjdG9yeTogQ29kZUNlbGxNb2RlbC5JQ29udGVudEZhY3Rvcnk7XG5cbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSBuZXcgY29kZSBjZWxsLlxuICAgICAqXG4gICAgICogQHBhcmFtIHNvdXJjZSAtIFRoZSBkYXRhIHRvIHVzZSBmb3IgdGhlIG9yaWdpbmFsIHNvdXJjZSBkYXRhLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBuZXcgY29kZSBjZWxsLiBJZiBhIHNvdXJjZSBjZWxsIGlzIHByb3ZpZGVkLCB0aGVcbiAgICAgKiAgIG5ldyBjZWxsIHdpbGwgYmUgaW5pdGlhbGl6ZWQgd2l0aCB0aGUgZGF0YSBmcm9tIHRoZSBzb3VyY2UuXG4gICAgICogICBJZiB0aGUgY29udGVudEZhY3RvcnkgaXMgbm90IHByb3ZpZGVkLCB0aGUgaW5zdGFuY2VcbiAgICAgKiAgIGBjb2RlQ2VsbENvbnRlbnRGYWN0b3J5YCB3aWxsIGJlIHVzZWQuXG4gICAgICovXG4gICAgY3JlYXRlQ29kZUNlbGwob3B0aW9uczogQ29kZUNlbGxNb2RlbC5JT3B0aW9ucyk6IElDb2RlQ2VsbE1vZGVsIHtcbiAgICAgIGlmICghb3B0aW9ucy5jb250ZW50RmFjdG9yeSkge1xuICAgICAgICBvcHRpb25zLmNvbnRlbnRGYWN0b3J5ID0gdGhpcy5jb2RlQ2VsbENvbnRlbnRGYWN0b3J5O1xuICAgICAgfVxuICAgICAgcmV0dXJuIG5ldyBDb2RlQ2VsbE1vZGVsKG9wdGlvbnMpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhIG5ldyByYXcgY2VsbC5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBzb3VyY2UgLSBUaGUgZGF0YSB0byB1c2UgZm9yIHRoZSBvcmlnaW5hbCBzb3VyY2UgZGF0YS5cbiAgICAgKlxuICAgICAqIEByZXR1cm5zIEEgbmV3IHJhdyBjZWxsLiBJZiBhIHNvdXJjZSBjZWxsIGlzIHByb3ZpZGVkLCB0aGVcbiAgICAgKiAgIG5ldyBjZWxsIHdpbGwgYmUgaW5pdGlhbGl6ZWQgd2l0aCB0aGUgZGF0YSBmcm9tIHRoZSBzb3VyY2UuXG4gICAgICovXG4gICAgY3JlYXRlUmF3Q2VsbChvcHRpb25zOiBDZWxsTW9kZWwuSU9wdGlvbnMpOiBJUmF3Q2VsbE1vZGVsIHtcbiAgICAgIHJldHVybiBuZXcgUmF3Q2VsbE1vZGVsKG9wdGlvbnMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGluaXRpYWxpemUgYSBgTW9kZWxGYWN0b3J5YC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU1vZGVsRmFjdG9yeU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBmYWN0b3J5IGZvciBvdXRwdXQgYXJlYSBtb2RlbHMuXG4gICAgICovXG4gICAgY29kZUNlbGxDb250ZW50RmFjdG9yeT86IENvZGVDZWxsTW9kZWwuSUNvbnRlbnRGYWN0b3J5O1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IGBNb2RlbEZhY3RvcnlgIGluc3RhbmNlLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRlZmF1bHRNb2RlbEZhY3RvcnkgPSBuZXcgTW9kZWxGYWN0b3J5KHt9KTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgY29uc29sZSB3aWRnZXQgcHJpdmF0ZSBkYXRhLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBKdW1wIHRvIHRoZSBib3R0b20gb2YgYSBub2RlLlxuICAgKlxuICAgKiBAcGFyYW0gbm9kZSAtIFRoZSBzY3JvbGxhYmxlIGVsZW1lbnQuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gc2Nyb2xsVG9Cb3R0b20obm9kZTogSFRNTEVsZW1lbnQpOiB2b2lkIHtcbiAgICBub2RlLnNjcm9sbFRvcCA9IG5vZGUuc2Nyb2xsSGVpZ2h0IC0gbm9kZS5jbGllbnRIZWlnaHQ7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==