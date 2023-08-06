"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_inspector_lib_index_js"],{

/***/ "../../packages/inspector/lib/handler.js":
/*!***********************************************!*\
  !*** ../../packages/inspector/lib/handler.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "InspectionHandler": () => (/* binding */ InspectionHandler)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/polling */ "webpack/sharing/consume/default/@lumino/polling/@lumino/polling");
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_polling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * An object that handles code inspection.
 */
class InspectionHandler {
    /**
     * Construct a new inspection handler for a widget.
     */
    constructor(options) {
        this._cleared = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        this._disposed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        this._editor = null;
        this._inspected = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal(this);
        this._isDisposed = false;
        this._pending = 0;
        this._standby = true;
        this._lastInspectedReply = null;
        this._connector = options.connector;
        this._rendermime = options.rendermime;
        this._debouncer = new _lumino_polling__WEBPACK_IMPORTED_MODULE_3__.Debouncer(this.onEditorChange.bind(this), 250);
    }
    /**
     * A signal emitted when the inspector should clear all items.
     */
    get cleared() {
        return this._cleared;
    }
    /**
     * A signal emitted when the handler is disposed.
     */
    get disposed() {
        return this._disposed;
    }
    /**
     * A signal emitted when an inspector value is generated.
     */
    get inspected() {
        return this._inspected;
    }
    /**
     * The editor widget used by the inspection handler.
     */
    get editor() {
        return this._editor;
    }
    set editor(newValue) {
        if (newValue === this._editor) {
            return;
        }
        // Remove all of our listeners.
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal.disconnectReceiver(this);
        const editor = (this._editor = newValue);
        if (editor) {
            // Clear the inspector in preparation for a new editor.
            this._cleared.emit(void 0);
            // Call onEditorChange to cover the case where the user changes
            // the active cell
            this.onEditorChange();
            editor.model.selections.changed.connect(this._onChange, this);
            editor.model.value.changed.connect(this._onChange, this);
        }
    }
    /**
     * Indicates whether the handler makes API inspection requests or stands by.
     *
     * #### Notes
     * The use case for this attribute is to limit the API traffic when no
     * inspector is visible.
     */
    get standby() {
        return this._standby;
    }
    set standby(value) {
        this._standby = value;
    }
    /**
     * Get whether the inspection handler is disposed.
     *
     * #### Notes
     * This is a read-only property.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources used by the handler.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        this._debouncer.dispose();
        this._disposed.emit(void 0);
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_4__.Signal.clearData(this);
    }
    /**
     * Handle a text changed signal from an editor.
     *
     * #### Notes
     * Update the hints inspector based on a text change.
     */
    onEditorChange(customText) {
        // If the handler is in standby mode, bail.
        if (this._standby) {
            return;
        }
        const editor = this.editor;
        if (!editor) {
            return;
        }
        const text = customText ? customText : editor.model.value.text;
        const position = editor.getCursorPosition();
        const offset = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.Text.jsIndexToCharIndex(editor.getOffsetAt(position), text);
        const update = { content: null };
        const pending = ++this._pending;
        void this._connector
            .fetch({ offset, text })
            .then(reply => {
            // If handler has been disposed or a newer request is pending, bail.
            if (!reply || this.isDisposed || pending !== this._pending) {
                this._lastInspectedReply = null;
                this._inspected.emit(update);
                return;
            }
            const { data } = reply;
            // Do not update if there would be no change.
            if (this._lastInspectedReply &&
                _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.deepEqual(this._lastInspectedReply, data)) {
                return;
            }
            const mimeType = this._rendermime.preferredMimeType(data);
            if (mimeType) {
                const widget = this._rendermime.createRenderer(mimeType);
                const model = new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__.MimeModel({ data });
                void widget.renderModel(model);
                update.content = widget;
            }
            this._lastInspectedReply = reply.data;
            this._inspected.emit(update);
        })
            .catch(reason => {
            // Since almost all failures are benign, fail silently.
            this._lastInspectedReply = null;
            this._inspected.emit(update);
        });
    }
    /**
     * Handle changes to the editor state, debouncing.
     */
    _onChange() {
        void this._debouncer.invoke();
    }
}


/***/ }),

/***/ "../../packages/inspector/lib/index.js":
/*!*********************************************!*\
  !*** ../../packages/inspector/lib/index.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IInspector": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_3__.IInspector),
/* harmony export */   "InspectionHandler": () => (/* reexport safe */ _handler__WEBPACK_IMPORTED_MODULE_0__.InspectionHandler),
/* harmony export */   "InspectorPanel": () => (/* reexport safe */ _inspector__WEBPACK_IMPORTED_MODULE_1__.InspectorPanel),
/* harmony export */   "KernelConnector": () => (/* reexport safe */ _kernelconnector__WEBPACK_IMPORTED_MODULE_2__.KernelConnector)
/* harmony export */ });
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./handler */ "../../packages/inspector/lib/handler.js");
/* harmony import */ var _inspector__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./inspector */ "../../packages/inspector/lib/inspector.js");
/* harmony import */ var _kernelconnector__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./kernelconnector */ "../../packages/inspector/lib/kernelconnector.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./tokens */ "../../packages/inspector/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module inspector
 */






/***/ }),

/***/ "../../packages/inspector/lib/inspector.js":
/*!*************************************************!*\
  !*** ../../packages/inspector/lib/inspector.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "InspectorPanel": () => (/* binding */ InspectorPanel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * The class name added to inspector panels.
 */
const PANEL_CLASS = 'jp-Inspector';
/**
 * The class name added to inspector content.
 */
const CONTENT_CLASS = 'jp-Inspector-content';
/**
 * The class name added to default inspector content.
 */
const DEFAULT_CONTENT_CLASS = 'jp-Inspector-default-content';
/**
 * A panel which contains a set of inspectors.
 */
class InspectorPanel extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Panel {
    /**
     * Construct an inspector.
     */
    constructor(options = {}) {
        super();
        this._source = null;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        if (options.initialContent instanceof _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget) {
            this._content = options.initialContent;
        }
        else if (typeof options.initialContent === 'string') {
            this._content = InspectorPanel._generateContentWidget(`<p>${options.initialContent}</p>`);
        }
        else {
            this._content = InspectorPanel._generateContentWidget('<p>' +
                this._trans.__('Click on a function to see documentation.') +
                '</p>');
        }
        this.addClass(PANEL_CLASS);
        this.layout.addWidget(this._content);
    }
    /**
     * Print in iframe
     */
    [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Printing.symbol]() {
        return () => _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.Printing.printWidget(this);
    }
    /**
     * The source of events the inspector panel listens for.
     */
    get source() {
        return this._source;
    }
    set source(source) {
        if (this._source === source) {
            return;
        }
        // Disconnect old signal handler.
        if (this._source) {
            this._source.standby = true;
            this._source.inspected.disconnect(this.onInspectorUpdate, this);
            this._source.disposed.disconnect(this.onSourceDisposed, this);
        }
        // Reject a source that is already disposed.
        if (source && source.isDisposed) {
            source = null;
        }
        // Update source.
        this._source = source;
        // Connect new signal handler.
        if (this._source) {
            this._source.standby = false;
            this._source.inspected.connect(this.onInspectorUpdate, this);
            this._source.disposed.connect(this.onSourceDisposed, this);
        }
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this.source = null;
        super.dispose();
    }
    /**
     * Handle inspector update signals.
     */
    onInspectorUpdate(sender, args) {
        const { content } = args;
        // Update the content of the inspector widget.
        if (!content || content === this._content) {
            return;
        }
        this._content.dispose();
        this._content = content;
        content.addClass(CONTENT_CLASS);
        this.layout.addWidget(content);
    }
    /**
     * Handle source disposed signals.
     */
    onSourceDisposed(sender, args) {
        this.source = null;
    }
    /**
     * Generate content widget from string
     */
    static _generateContentWidget(message) {
        const widget = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget();
        widget.node.innerHTML = message;
        widget.addClass(CONTENT_CLASS);
        widget.addClass(DEFAULT_CONTENT_CLASS);
        return widget;
    }
}


/***/ }),

/***/ "../../packages/inspector/lib/kernelconnector.js":
/*!*******************************************************!*\
  !*** ../../packages/inspector/lib/kernelconnector.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "KernelConnector": () => (/* binding */ KernelConnector)
/* harmony export */ });
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The default connector for making inspection requests from the Jupyter API.
 */
class KernelConnector extends _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__.DataConnector {
    /**
     * Create a new kernel connector for inspection requests.
     *
     * @param options - The instantiation options for the kernel connector.
     */
    constructor(options) {
        super();
        this._sessionContext = options.sessionContext;
    }
    /**
     * Fetch inspection requests.
     *
     * @param request - The inspection request text and details.
     */
    fetch(request) {
        var _a;
        const kernel = (_a = this._sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if (!kernel) {
            return Promise.reject(new Error('Inspection fetch requires a kernel.'));
        }
        const contents = {
            code: request.text,
            cursor_pos: request.offset,
            detail_level: 1
        };
        return kernel.requestInspect(contents).then(msg => {
            const response = msg.content;
            if (response.status !== 'ok' || !response.found) {
                throw new Error('Inspection fetch failed to return successfully.');
            }
            return { data: response.data, metadata: response.metadata };
        });
    }
}


/***/ }),

/***/ "../../packages/inspector/lib/tokens.js":
/*!**********************************************!*\
  !*** ../../packages/inspector/lib/tokens.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IInspector": () => (/* binding */ IInspector)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The inspector panel token.
 */
const IInspector = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/inspector:IInspector');


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfaW5zcGVjdG9yX2xpYl9pbmRleF9qcy44MTZkZDdlMWY2YmRkMTQwYmU0NC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFHZDtBQUMyQjtBQUVSO0FBRXBCO0FBQ1E7QUFHcEQ7O0dBRUc7QUFDSSxNQUFNLGlCQUFpQjtJQUM1Qjs7T0FFRztJQUNILFlBQVksT0FBbUM7UUErSnZDLGFBQVEsR0FBRyxJQUFJLHFEQUFNLENBQTBCLElBQUksQ0FBQyxDQUFDO1FBTXJELGNBQVMsR0FBRyxJQUFJLHFEQUFNLENBQWEsSUFBSSxDQUFDLENBQUM7UUFDekMsWUFBTyxHQUE4QixJQUFJLENBQUM7UUFDMUMsZUFBVSxHQUFHLElBQUkscURBQU0sQ0FBb0MsSUFBSSxDQUFDLENBQUM7UUFDakUsZ0JBQVcsR0FBRyxLQUFLLENBQUM7UUFDcEIsYUFBUSxHQUFHLENBQUMsQ0FBQztRQUViLGFBQVEsR0FBRyxJQUFJLENBQUM7UUFFaEIsd0JBQW1CLEdBQTRDLElBQUksQ0FBQztRQTVLMUUsSUFBSSxDQUFDLFVBQVUsR0FBRyxPQUFPLENBQUMsU0FBUyxDQUFDO1FBQ3BDLElBQUksQ0FBQyxXQUFXLEdBQUcsT0FBTyxDQUFDLFVBQVUsQ0FBQztRQUN0QyxJQUFJLENBQUMsVUFBVSxHQUFHLElBQUksc0RBQVMsQ0FBQyxJQUFJLENBQUMsY0FBYyxDQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsRUFBRSxHQUFHLENBQUMsQ0FBQztJQUN2RSxDQUFDO0lBRUQ7O09BRUc7SUFDSCxJQUFJLE9BQU87UUFDVCxPQUFPLElBQUksQ0FBQyxRQUFRLENBQUM7SUFDdkIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxRQUFRO1FBQ1YsT0FBTyxJQUFJLENBQUMsU0FBUyxDQUFDO0lBQ3hCLENBQUM7SUFFRDs7T0FFRztJQUNILElBQUksU0FBUztRQUNYLE9BQU8sSUFBSSxDQUFDLFVBQVUsQ0FBQztJQUN6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LDBDQUEwQztBQUMxQywyREFBMkQ7QUFFakI7QUFJMUM7O0dBRUc7QUFDSSxNQUFNLFVBQVUsR0FBRyxJQUFJLG9EQUFLLENBQ2pDLGtDQUFrQyxDQUNuQyxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2luc3BlY3Rvci9zcmMvaGFuZGxlci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvaW5zcGVjdG9yL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvaW5zcGVjdG9yL3NyYy9pbnNwZWN0b3IudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2luc3BlY3Rvci9zcmMva2VybmVsY29ubmVjdG9yLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9pbnNwZWN0b3Ivc3JjL3Rva2Vucy50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IENvZGVFZGl0b3IgfSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7IFRleHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSVJlbmRlck1pbWVSZWdpc3RyeSwgTWltZU1vZGVsIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyBJRGF0YUNvbm5lY3RvciB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXRlZGInO1xuaW1wb3J0IHsgSlNPTkV4dCwgUmVhZG9ubHlKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgRGVib3VuY2VyIH0gZnJvbSAnQGx1bWluby9wb2xsaW5nJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IElJbnNwZWN0b3IgfSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogQW4gb2JqZWN0IHRoYXQgaGFuZGxlcyBjb2RlIGluc3BlY3Rpb24uXG4gKi9cbmV4cG9ydCBjbGFzcyBJbnNwZWN0aW9uSGFuZGxlciBpbXBsZW1lbnRzIElEaXNwb3NhYmxlLCBJSW5zcGVjdG9yLklJbnNwZWN0YWJsZSB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgaW5zcGVjdGlvbiBoYW5kbGVyIGZvciBhIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IEluc3BlY3Rpb25IYW5kbGVyLklPcHRpb25zKSB7XG4gICAgdGhpcy5fY29ubmVjdG9yID0gb3B0aW9ucy5jb25uZWN0b3I7XG4gICAgdGhpcy5fcmVuZGVybWltZSA9IG9wdGlvbnMucmVuZGVybWltZTtcbiAgICB0aGlzLl9kZWJvdW5jZXIgPSBuZXcgRGVib3VuY2VyKHRoaXMub25FZGl0b3JDaGFuZ2UuYmluZCh0aGlzKSwgMjUwKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIGluc3BlY3RvciBzaG91bGQgY2xlYXIgYWxsIGl0ZW1zLlxuICAgKi9cbiAgZ2V0IGNsZWFyZWQoKTogSVNpZ25hbDxJbnNwZWN0aW9uSGFuZGxlciwgdm9pZD4ge1xuICAgIHJldHVybiB0aGlzLl9jbGVhcmVkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgaGFuZGxlciBpcyBkaXNwb3NlZC5cbiAgICovXG4gIGdldCBkaXNwb3NlZCgpOiBJU2lnbmFsPEluc3BlY3Rpb25IYW5kbGVyLCB2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX2Rpc3Bvc2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBhbiBpbnNwZWN0b3IgdmFsdWUgaXMgZ2VuZXJhdGVkLlxuICAgKi9cbiAgZ2V0IGluc3BlY3RlZCgpOiBJU2lnbmFsPEluc3BlY3Rpb25IYW5kbGVyLCBJSW5zcGVjdG9yLklJbnNwZWN0b3JVcGRhdGU+IHtcbiAgICByZXR1cm4gdGhpcy5faW5zcGVjdGVkO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBlZGl0b3Igd2lkZ2V0IHVzZWQgYnkgdGhlIGluc3BlY3Rpb24gaGFuZGxlci5cbiAgICovXG4gIGdldCBlZGl0b3IoKTogQ29kZUVkaXRvci5JRWRpdG9yIHwgbnVsbCB7XG4gICAgcmV0dXJuIHRoaXMuX2VkaXRvcjtcbiAgfVxuICBzZXQgZWRpdG9yKG5ld1ZhbHVlOiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsKSB7XG4gICAgaWYgKG5ld1ZhbHVlID09PSB0aGlzLl9lZGl0b3IpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgLy8gUmVtb3ZlIGFsbCBvZiBvdXIgbGlzdGVuZXJzLlxuICAgIFNpZ25hbC5kaXNjb25uZWN0UmVjZWl2ZXIodGhpcyk7XG5cbiAgICBjb25zdCBlZGl0b3IgPSAodGhpcy5fZWRpdG9yID0gbmV3VmFsdWUpO1xuICAgIGlmIChlZGl0b3IpIHtcbiAgICAgIC8vIENsZWFyIHRoZSBpbnNwZWN0b3IgaW4gcHJlcGFyYXRpb24gZm9yIGEgbmV3IGVkaXRvci5cbiAgICAgIHRoaXMuX2NsZWFyZWQuZW1pdCh2b2lkIDApO1xuICAgICAgLy8gQ2FsbCBvbkVkaXRvckNoYW5nZSB0byBjb3ZlciB0aGUgY2FzZSB3aGVyZSB0aGUgdXNlciBjaGFuZ2VzXG4gICAgICAvLyB0aGUgYWN0aXZlIGNlbGxcbiAgICAgIHRoaXMub25FZGl0b3JDaGFuZ2UoKTtcbiAgICAgIGVkaXRvci5tb2RlbC5zZWxlY3Rpb25zLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vbkNoYW5nZSwgdGhpcyk7XG4gICAgICBlZGl0b3IubW9kZWwudmFsdWUuY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uQ2hhbmdlLCB0aGlzKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSW5kaWNhdGVzIHdoZXRoZXIgdGhlIGhhbmRsZXIgbWFrZXMgQVBJIGluc3BlY3Rpb24gcmVxdWVzdHMgb3Igc3RhbmRzIGJ5LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoZSB1c2UgY2FzZSBmb3IgdGhpcyBhdHRyaWJ1dGUgaXMgdG8gbGltaXQgdGhlIEFQSSB0cmFmZmljIHdoZW4gbm9cbiAgICogaW5zcGVjdG9yIGlzIHZpc2libGUuXG4gICAqL1xuICBnZXQgc3RhbmRieSgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5fc3RhbmRieTtcbiAgfVxuICBzZXQgc3RhbmRieSh2YWx1ZTogYm9vbGVhbikge1xuICAgIHRoaXMuX3N0YW5kYnkgPSB2YWx1ZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgd2hldGhlciB0aGUgaW5zcGVjdGlvbiBoYW5kbGVyIGlzIGRpc3Bvc2VkLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgaXMgYSByZWFkLW9ubHkgcHJvcGVydHkuXG4gICAqL1xuICBnZXQgaXNEaXNwb3NlZCgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5faXNEaXNwb3NlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgdXNlZCBieSB0aGUgaGFuZGxlci5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICB0aGlzLl9kZWJvdW5jZXIuZGlzcG9zZSgpO1xuICAgIHRoaXMuX2Rpc3Bvc2VkLmVtaXQodm9pZCAwKTtcbiAgICBTaWduYWwuY2xlYXJEYXRhKHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhIHRleHQgY2hhbmdlZCBzaWduYWwgZnJvbSBhbiBlZGl0b3IuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVXBkYXRlIHRoZSBoaW50cyBpbnNwZWN0b3IgYmFzZWQgb24gYSB0ZXh0IGNoYW5nZS5cbiAgICovXG4gIG9uRWRpdG9yQ2hhbmdlKGN1c3RvbVRleHQ/OiBzdHJpbmcpOiB2b2lkIHtcbiAgICAvLyBJZiB0aGUgaGFuZGxlciBpcyBpbiBzdGFuZGJ5IG1vZGUsIGJhaWwuXG4gICAgaWYgKHRoaXMuX3N0YW5kYnkpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBlZGl0b3IgPSB0aGlzLmVkaXRvcjtcblxuICAgIGlmICghZWRpdG9yKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHRleHQgPSBjdXN0b21UZXh0ID8gY3VzdG9tVGV4dCA6IGVkaXRvci5tb2RlbC52YWx1ZS50ZXh0O1xuICAgIGNvbnN0IHBvc2l0aW9uID0gZWRpdG9yLmdldEN1cnNvclBvc2l0aW9uKCk7XG4gICAgY29uc3Qgb2Zmc2V0ID0gVGV4dC5qc0luZGV4VG9DaGFySW5kZXgoZWRpdG9yLmdldE9mZnNldEF0KHBvc2l0aW9uKSwgdGV4dCk7XG4gICAgY29uc3QgdXBkYXRlOiBJSW5zcGVjdG9yLklJbnNwZWN0b3JVcGRhdGUgPSB7IGNvbnRlbnQ6IG51bGwgfTtcblxuICAgIGNvbnN0IHBlbmRpbmcgPSArK3RoaXMuX3BlbmRpbmc7XG5cbiAgICB2b2lkIHRoaXMuX2Nvbm5lY3RvclxuICAgICAgLmZldGNoKHsgb2Zmc2V0LCB0ZXh0IH0pXG4gICAgICAudGhlbihyZXBseSA9PiB7XG4gICAgICAgIC8vIElmIGhhbmRsZXIgaGFzIGJlZW4gZGlzcG9zZWQgb3IgYSBuZXdlciByZXF1ZXN0IGlzIHBlbmRpbmcsIGJhaWwuXG4gICAgICAgIGlmICghcmVwbHkgfHwgdGhpcy5pc0Rpc3Bvc2VkIHx8IHBlbmRpbmcgIT09IHRoaXMuX3BlbmRpbmcpIHtcbiAgICAgICAgICB0aGlzLl9sYXN0SW5zcGVjdGVkUmVwbHkgPSBudWxsO1xuICAgICAgICAgIHRoaXMuX2luc3BlY3RlZC5lbWl0KHVwZGF0ZSk7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgeyBkYXRhIH0gPSByZXBseTtcblxuICAgICAgICAvLyBEbyBub3QgdXBkYXRlIGlmIHRoZXJlIHdvdWxkIGJlIG5vIGNoYW5nZS5cbiAgICAgICAgaWYgKFxuICAgICAgICAgIHRoaXMuX2xhc3RJbnNwZWN0ZWRSZXBseSAmJlxuICAgICAgICAgIEpTT05FeHQuZGVlcEVxdWFsKHRoaXMuX2xhc3RJbnNwZWN0ZWRSZXBseSwgZGF0YSlcbiAgICAgICAgKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgY29uc3QgbWltZVR5cGUgPSB0aGlzLl9yZW5kZXJtaW1lLnByZWZlcnJlZE1pbWVUeXBlKGRhdGEpO1xuICAgICAgICBpZiAobWltZVR5cGUpIHtcbiAgICAgICAgICBjb25zdCB3aWRnZXQgPSB0aGlzLl9yZW5kZXJtaW1lLmNyZWF0ZVJlbmRlcmVyKG1pbWVUeXBlKTtcbiAgICAgICAgICBjb25zdCBtb2RlbCA9IG5ldyBNaW1lTW9kZWwoeyBkYXRhIH0pO1xuXG4gICAgICAgICAgdm9pZCB3aWRnZXQucmVuZGVyTW9kZWwobW9kZWwpO1xuICAgICAgICAgIHVwZGF0ZS5jb250ZW50ID0gd2lkZ2V0O1xuICAgICAgICB9XG5cbiAgICAgICAgdGhpcy5fbGFzdEluc3BlY3RlZFJlcGx5ID0gcmVwbHkuZGF0YTtcbiAgICAgICAgdGhpcy5faW5zcGVjdGVkLmVtaXQodXBkYXRlKTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgLy8gU2luY2UgYWxtb3N0IGFsbCBmYWlsdXJlcyBhcmUgYmVuaWduLCBmYWlsIHNpbGVudGx5LlxuICAgICAgICB0aGlzLl9sYXN0SW5zcGVjdGVkUmVwbHkgPSBudWxsO1xuICAgICAgICB0aGlzLl9pbnNwZWN0ZWQuZW1pdCh1cGRhdGUpO1xuICAgICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGNoYW5nZXMgdG8gdGhlIGVkaXRvciBzdGF0ZSwgZGVib3VuY2luZy5cbiAgICovXG4gIHByaXZhdGUgX29uQ2hhbmdlKCk6IHZvaWQge1xuICAgIHZvaWQgdGhpcy5fZGVib3VuY2VyLmludm9rZSgpO1xuICB9XG5cbiAgcHJpdmF0ZSBfY2xlYXJlZCA9IG5ldyBTaWduYWw8SW5zcGVjdGlvbkhhbmRsZXIsIHZvaWQ+KHRoaXMpO1xuICBwcml2YXRlIF9jb25uZWN0b3I6IElEYXRhQ29ubmVjdG9yPFxuICAgIEluc3BlY3Rpb25IYW5kbGVyLklSZXBseSxcbiAgICB2b2lkLFxuICAgIEluc3BlY3Rpb25IYW5kbGVyLklSZXF1ZXN0XG4gID47XG4gIHByaXZhdGUgX2Rpc3Bvc2VkID0gbmV3IFNpZ25hbDx0aGlzLCB2b2lkPih0aGlzKTtcbiAgcHJpdmF0ZSBfZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsID0gbnVsbDtcbiAgcHJpdmF0ZSBfaW5zcGVjdGVkID0gbmV3IFNpZ25hbDx0aGlzLCBJSW5zcGVjdG9yLklJbnNwZWN0b3JVcGRhdGU+KHRoaXMpO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG4gIHByaXZhdGUgX3BlbmRpbmcgPSAwO1xuICBwcml2YXRlIF9yZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5O1xuICBwcml2YXRlIF9zdGFuZGJ5ID0gdHJ1ZTtcbiAgcHJpdmF0ZSBfZGVib3VuY2VyOiBEZWJvdW5jZXI7XG4gIHByaXZhdGUgX2xhc3RJbnNwZWN0ZWRSZXBseTogSW5zcGVjdGlvbkhhbmRsZXIuSVJlcGx5WydkYXRhJ10gfCBudWxsID0gbnVsbDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgaW5zcGVjdGlvbiBoYW5kbGVyIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSW5zcGVjdGlvbkhhbmRsZXIge1xuICAvKipcbiAgICogVGhlIGluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgYW4gaW5zcGVjdGlvbiBoYW5kbGVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGNvbm5lY3RvciB1c2VkIHRvIG1ha2UgaW5zcGVjdGlvbiByZXF1ZXN0cy5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGUgb25seSBtZXRob2Qgb2YgdGhpcyBjb25uZWN0b3IgdGhhdCB3aWxsIGV2ZXIgYmUgY2FsbGVkIGlzIGBmZXRjaGAsIHNvXG4gICAgICogaXQgaXMgYWNjZXB0YWJsZSBmb3IgdGhlIG90aGVyIG1ldGhvZHMgdG8gYmUgc2ltcGxlIGZ1bmN0aW9ucyB0aGF0IHJldHVyblxuICAgICAqIHJlamVjdGVkIHByb21pc2VzLlxuICAgICAqL1xuICAgIGNvbm5lY3RvcjogSURhdGFDb25uZWN0b3I8SVJlcGx5LCB2b2lkLCBJUmVxdWVzdD47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbWltZSByZW5kZXJlciBmb3IgdGhlIGluc3BlY3Rpb24gaGFuZGxlci5cbiAgICAgKi9cbiAgICByZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5O1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcmVwbHkgdG8gYW4gaW5zcGVjdGlvbiByZXF1ZXN0LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUmVwbHkge1xuICAgIC8qKlxuICAgICAqIFRoZSBNSU1FIGJ1bmRsZSBkYXRhIHJldHVybmVkIGZyb20gYW4gaW5zcGVjdGlvbiByZXF1ZXN0LlxuICAgICAqL1xuICAgIGRhdGE6IFJlYWRvbmx5SlNPTk9iamVjdDtcblxuICAgIC8qKlxuICAgICAqIEFueSBtZXRhZGF0YSB0aGF0IGFjY29tcGFuaWVzIHRoZSBNSU1FIGJ1bmRsZSByZXR1cm5pbmcgZnJvbSBhIHJlcXVlc3QuXG4gICAgICovXG4gICAgbWV0YWRhdGE6IFJlYWRvbmx5SlNPTk9iamVjdDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGV0YWlscyBvZiBhbiBpbnNwZWN0aW9uIHJlcXVlc3QuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElSZXF1ZXN0IHtcbiAgICAvKipcbiAgICAgKiBUaGUgY3Vyc29yIG9mZnNldCBwb3NpdGlvbiB3aXRoaW4gdGhlIHRleHQgYmVpbmcgaW5zcGVjdGVkLlxuICAgICAqL1xuICAgIG9mZnNldDogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHRleHQgYmVpbmcgaW5zcGVjdGVkLlxuICAgICAqL1xuICAgIHRleHQ6IHN0cmluZztcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgaW5zcGVjdG9yXG4gKi9cblxuZXhwb3J0ICogZnJvbSAnLi9oYW5kbGVyJztcbmV4cG9ydCAqIGZyb20gJy4vaW5zcGVjdG9yJztcbmV4cG9ydCAqIGZyb20gJy4va2VybmVsY29ubmVjdG9yJztcbmV4cG9ydCAqIGZyb20gJy4vdG9rZW5zJztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgUHJpbnRpbmcgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IFBhbmVsLCBQYW5lbExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IElJbnNwZWN0b3IgfSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gaW5zcGVjdG9yIHBhbmVscy5cbiAqL1xuY29uc3QgUEFORUxfQ0xBU1MgPSAnanAtSW5zcGVjdG9yJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBpbnNwZWN0b3IgY29udGVudC5cbiAqL1xuY29uc3QgQ09OVEVOVF9DTEFTUyA9ICdqcC1JbnNwZWN0b3ItY29udGVudCc7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gZGVmYXVsdCBpbnNwZWN0b3IgY29udGVudC5cbiAqL1xuY29uc3QgREVGQVVMVF9DT05URU5UX0NMQVNTID0gJ2pwLUluc3BlY3Rvci1kZWZhdWx0LWNvbnRlbnQnO1xuXG4vKipcbiAqIEEgcGFuZWwgd2hpY2ggY29udGFpbnMgYSBzZXQgb2YgaW5zcGVjdG9ycy5cbiAqL1xuZXhwb3J0IGNsYXNzIEluc3BlY3RvclBhbmVsXG4gIGV4dGVuZHMgUGFuZWxcbiAgaW1wbGVtZW50cyBJSW5zcGVjdG9yLCBQcmludGluZy5JUHJpbnRhYmxlXG57XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYW4gaW5zcGVjdG9yLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogSW5zcGVjdG9yUGFuZWwuSU9wdGlvbnMgPSB7fSkge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGlmIChvcHRpb25zLmluaXRpYWxDb250ZW50IGluc3RhbmNlb2YgV2lkZ2V0KSB7XG4gICAgICB0aGlzLl9jb250ZW50ID0gb3B0aW9ucy5pbml0aWFsQ29udGVudDtcbiAgICB9IGVsc2UgaWYgKHR5cGVvZiBvcHRpb25zLmluaXRpYWxDb250ZW50ID09PSAnc3RyaW5nJykge1xuICAgICAgdGhpcy5fY29udGVudCA9IEluc3BlY3RvclBhbmVsLl9nZW5lcmF0ZUNvbnRlbnRXaWRnZXQoXG4gICAgICAgIGA8cD4ke29wdGlvbnMuaW5pdGlhbENvbnRlbnR9PC9wPmBcbiAgICAgICk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMuX2NvbnRlbnQgPSBJbnNwZWN0b3JQYW5lbC5fZ2VuZXJhdGVDb250ZW50V2lkZ2V0KFxuICAgICAgICAnPHA+JyArXG4gICAgICAgICAgdGhpcy5fdHJhbnMuX18oJ0NsaWNrIG9uIGEgZnVuY3Rpb24gdG8gc2VlIGRvY3VtZW50YXRpb24uJykgK1xuICAgICAgICAgICc8L3A+J1xuICAgICAgKTtcbiAgICB9XG5cbiAgICB0aGlzLmFkZENsYXNzKFBBTkVMX0NMQVNTKTtcbiAgICAodGhpcy5sYXlvdXQgYXMgUGFuZWxMYXlvdXQpLmFkZFdpZGdldCh0aGlzLl9jb250ZW50KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBQcmludCBpbiBpZnJhbWVcbiAgICovXG4gIFtQcmludGluZy5zeW1ib2xdKCkge1xuICAgIHJldHVybiAoKTogUHJvbWlzZTx2b2lkPiA9PiBQcmludGluZy5wcmludFdpZGdldCh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgc291cmNlIG9mIGV2ZW50cyB0aGUgaW5zcGVjdG9yIHBhbmVsIGxpc3RlbnMgZm9yLlxuICAgKi9cbiAgZ2V0IHNvdXJjZSgpOiBJSW5zcGVjdG9yLklJbnNwZWN0YWJsZSB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9zb3VyY2U7XG4gIH1cbiAgc2V0IHNvdXJjZShzb3VyY2U6IElJbnNwZWN0b3IuSUluc3BlY3RhYmxlIHwgbnVsbCkge1xuICAgIGlmICh0aGlzLl9zb3VyY2UgPT09IHNvdXJjZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIC8vIERpc2Nvbm5lY3Qgb2xkIHNpZ25hbCBoYW5kbGVyLlxuICAgIGlmICh0aGlzLl9zb3VyY2UpIHtcbiAgICAgIHRoaXMuX3NvdXJjZS5zdGFuZGJ5ID0gdHJ1ZTtcbiAgICAgIHRoaXMuX3NvdXJjZS5pbnNwZWN0ZWQuZGlzY29ubmVjdCh0aGlzLm9uSW5zcGVjdG9yVXBkYXRlLCB0aGlzKTtcbiAgICAgIHRoaXMuX3NvdXJjZS5kaXNwb3NlZC5kaXNjb25uZWN0KHRoaXMub25Tb3VyY2VEaXNwb3NlZCwgdGhpcyk7XG4gICAgfVxuXG4gICAgLy8gUmVqZWN0IGEgc291cmNlIHRoYXQgaXMgYWxyZWFkeSBkaXNwb3NlZC5cbiAgICBpZiAoc291cmNlICYmIHNvdXJjZS5pc0Rpc3Bvc2VkKSB7XG4gICAgICBzb3VyY2UgPSBudWxsO1xuICAgIH1cblxuICAgIC8vIFVwZGF0ZSBzb3VyY2UuXG4gICAgdGhpcy5fc291cmNlID0gc291cmNlO1xuXG4gICAgLy8gQ29ubmVjdCBuZXcgc2lnbmFsIGhhbmRsZXIuXG4gICAgaWYgKHRoaXMuX3NvdXJjZSkge1xuICAgICAgdGhpcy5fc291cmNlLnN0YW5kYnkgPSBmYWxzZTtcbiAgICAgIHRoaXMuX3NvdXJjZS5pbnNwZWN0ZWQuY29ubmVjdCh0aGlzLm9uSW5zcGVjdG9yVXBkYXRlLCB0aGlzKTtcbiAgICAgIHRoaXMuX3NvdXJjZS5kaXNwb3NlZC5jb25uZWN0KHRoaXMub25Tb3VyY2VEaXNwb3NlZCwgdGhpcyk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyBoZWxkIGJ5IHRoZSB3aWRnZXQuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5zb3VyY2UgPSBudWxsO1xuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgaW5zcGVjdG9yIHVwZGF0ZSBzaWduYWxzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uSW5zcGVjdG9yVXBkYXRlKFxuICAgIHNlbmRlcjogYW55LFxuICAgIGFyZ3M6IElJbnNwZWN0b3IuSUluc3BlY3RvclVwZGF0ZVxuICApOiB2b2lkIHtcbiAgICBjb25zdCB7IGNvbnRlbnQgfSA9IGFyZ3M7XG5cbiAgICAvLyBVcGRhdGUgdGhlIGNvbnRlbnQgb2YgdGhlIGluc3BlY3RvciB3aWRnZXQuXG4gICAgaWYgKCFjb250ZW50IHx8IGNvbnRlbnQgPT09IHRoaXMuX2NvbnRlbnQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fY29udGVudC5kaXNwb3NlKCk7XG5cbiAgICB0aGlzLl9jb250ZW50ID0gY29udGVudDtcbiAgICBjb250ZW50LmFkZENsYXNzKENPTlRFTlRfQ0xBU1MpO1xuICAgICh0aGlzLmxheW91dCBhcyBQYW5lbExheW91dCkuYWRkV2lkZ2V0KGNvbnRlbnQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBzb3VyY2UgZGlzcG9zZWQgc2lnbmFscy5cbiAgICovXG4gIHByb3RlY3RlZCBvblNvdXJjZURpc3Bvc2VkKHNlbmRlcjogYW55LCBhcmdzOiB2b2lkKTogdm9pZCB7XG4gICAgdGhpcy5zb3VyY2UgPSBudWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIEdlbmVyYXRlIGNvbnRlbnQgd2lkZ2V0IGZyb20gc3RyaW5nXG4gICAqL1xuICBwcml2YXRlIHN0YXRpYyBfZ2VuZXJhdGVDb250ZW50V2lkZ2V0KG1lc3NhZ2U6IHN0cmluZyk6IFdpZGdldCB7XG4gICAgY29uc3Qgd2lkZ2V0ID0gbmV3IFdpZGdldCgpO1xuICAgIHdpZGdldC5ub2RlLmlubmVySFRNTCA9IG1lc3NhZ2U7XG4gICAgd2lkZ2V0LmFkZENsYXNzKENPTlRFTlRfQ0xBU1MpO1xuICAgIHdpZGdldC5hZGRDbGFzcyhERUZBVUxUX0NPTlRFTlRfQ0xBU1MpO1xuXG4gICAgcmV0dXJuIHdpZGdldDtcbiAgfVxuXG4gIHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbiAgcHJpdmF0ZSBfdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlO1xuICBwcml2YXRlIF9jb250ZW50OiBXaWRnZXQ7XG4gIHByaXZhdGUgX3NvdXJjZTogSUluc3BlY3Rvci5JSW5zcGVjdGFibGUgfCBudWxsID0gbnVsbDtcbn1cblxuZXhwb3J0IG5hbWVzcGFjZSBJbnNwZWN0b3JQYW5lbCB7XG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIGluaXRpYWxDb250ZW50PzogV2lkZ2V0IHwgc3RyaW5nIHwgdW5kZWZpbmVkO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAgICovXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZXNzaW9uQ29udGV4dCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IEtlcm5lbE1lc3NhZ2UgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBEYXRhQ29ubmVjdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdGVkYic7XG5pbXBvcnQgeyBJbnNwZWN0aW9uSGFuZGxlciB9IGZyb20gJy4vaGFuZGxlcic7XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgY29ubmVjdG9yIGZvciBtYWtpbmcgaW5zcGVjdGlvbiByZXF1ZXN0cyBmcm9tIHRoZSBKdXB5dGVyIEFQSS5cbiAqL1xuZXhwb3J0IGNsYXNzIEtlcm5lbENvbm5lY3RvciBleHRlbmRzIERhdGFDb25uZWN0b3I8XG4gIEluc3BlY3Rpb25IYW5kbGVyLklSZXBseSxcbiAgdm9pZCxcbiAgSW5zcGVjdGlvbkhhbmRsZXIuSVJlcXVlc3Rcbj4ge1xuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IGtlcm5lbCBjb25uZWN0b3IgZm9yIGluc3BlY3Rpb24gcmVxdWVzdHMuXG4gICAqXG4gICAqIEBwYXJhbSBvcHRpb25zIC0gVGhlIGluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgdGhlIGtlcm5lbCBjb25uZWN0b3IuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBLZXJuZWxDb25uZWN0b3IuSU9wdGlvbnMpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX3Nlc3Npb25Db250ZXh0ID0gb3B0aW9ucy5zZXNzaW9uQ29udGV4dDtcbiAgfVxuXG4gIC8qKlxuICAgKiBGZXRjaCBpbnNwZWN0aW9uIHJlcXVlc3RzLlxuICAgKlxuICAgKiBAcGFyYW0gcmVxdWVzdCAtIFRoZSBpbnNwZWN0aW9uIHJlcXVlc3QgdGV4dCBhbmQgZGV0YWlscy5cbiAgICovXG4gIGZldGNoKFxuICAgIHJlcXVlc3Q6IEluc3BlY3Rpb25IYW5kbGVyLklSZXF1ZXN0XG4gICk6IFByb21pc2U8SW5zcGVjdGlvbkhhbmRsZXIuSVJlcGx5PiB7XG4gICAgY29uc3Qga2VybmVsID0gdGhpcy5fc2Vzc2lvbkNvbnRleHQuc2Vzc2lvbj8ua2VybmVsO1xuXG4gICAgaWYgKCFrZXJuZWwpIHtcbiAgICAgIHJldHVybiBQcm9taXNlLnJlamVjdChuZXcgRXJyb3IoJ0luc3BlY3Rpb24gZmV0Y2ggcmVxdWlyZXMgYSBrZXJuZWwuJykpO1xuICAgIH1cblxuICAgIGNvbnN0IGNvbnRlbnRzOiBLZXJuZWxNZXNzYWdlLklJbnNwZWN0UmVxdWVzdE1zZ1snY29udGVudCddID0ge1xuICAgICAgY29kZTogcmVxdWVzdC50ZXh0LFxuICAgICAgY3Vyc29yX3BvczogcmVxdWVzdC5vZmZzZXQsXG4gICAgICBkZXRhaWxfbGV2ZWw6IDFcbiAgICB9O1xuXG4gICAgcmV0dXJuIGtlcm5lbC5yZXF1ZXN0SW5zcGVjdChjb250ZW50cykudGhlbihtc2cgPT4ge1xuICAgICAgY29uc3QgcmVzcG9uc2UgPSBtc2cuY29udGVudDtcblxuICAgICAgaWYgKHJlc3BvbnNlLnN0YXR1cyAhPT0gJ29rJyB8fCAhcmVzcG9uc2UuZm91bmQpIHtcbiAgICAgICAgdGhyb3cgbmV3IEVycm9yKCdJbnNwZWN0aW9uIGZldGNoIGZhaWxlZCB0byByZXR1cm4gc3VjY2Vzc2Z1bGx5LicpO1xuICAgICAgfVxuXG4gICAgICByZXR1cm4geyBkYXRhOiByZXNwb25zZS5kYXRhLCBtZXRhZGF0YTogcmVzcG9uc2UubWV0YWRhdGEgfTtcbiAgICB9KTtcbiAgfVxuXG4gIHByaXZhdGUgX3Nlc3Npb25Db250ZXh0OiBJU2Vzc2lvbkNvbnRleHQ7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIGtlcm5lbCBjb25uZWN0b3Igc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBLZXJuZWxDb25uZWN0b3Ige1xuICAvKipcbiAgICogVGhlIGluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgYW4gaW5zcGVjdGlvbiBoYW5kbGVyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHNlc3Npb24gY29udGV4dCB1c2VkIHRvIG1ha2UgQVBJIHJlcXVlc3RzIHRvIHRoZSBrZXJuZWwuXG4gICAgICovXG4gICAgc2Vzc2lvbkNvbnRleHQ6IElTZXNzaW9uQ29udGV4dDtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBpbnNwZWN0b3IgcGFuZWwgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJSW5zcGVjdG9yID0gbmV3IFRva2VuPElJbnNwZWN0b3I+KFxuICAnQGp1cHl0ZXJsYWIvaW5zcGVjdG9yOklJbnNwZWN0b3InXG4pO1xuXG4vKipcbiAqIEFuIGludGVyZmFjZSBmb3IgYW4gaW5zcGVjdG9yLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElJbnNwZWN0b3Ige1xuICAvKipcbiAgICogVGhlIHNvdXJjZSBvZiBldmVudHMgdGhlIGluc3BlY3RvciBsaXN0ZW5zIGZvci5cbiAgICovXG4gIHNvdXJjZTogSUluc3BlY3Rvci5JSW5zcGVjdGFibGUgfCBudWxsO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBpbnNwZWN0b3IgaW50ZXJmYWNlcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJSW5zcGVjdG9yIHtcbiAgLyoqXG4gICAqIFRoZSBkZWZpbml0aW9uIG9mIGFuIGluc3BlY3RhYmxlIHNvdXJjZS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUluc3BlY3RhYmxlIHtcbiAgICAvKipcbiAgICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIGluc3BlY3RvciBzaG91bGQgY2xlYXIgYWxsIGl0ZW1zLlxuICAgICAqL1xuICAgIGNsZWFyZWQ6IElTaWduYWw8YW55LCB2b2lkPjtcblxuICAgIC8qKlxuICAgICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgaW5zcGVjdGFibGUgaXMgZGlzcG9zZWQuXG4gICAgICovXG4gICAgZGlzcG9zZWQ6IElTaWduYWw8YW55LCB2b2lkPjtcblxuICAgIC8qKlxuICAgICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBhbiBpbnNwZWN0b3IgdmFsdWUgaXMgZ2VuZXJhdGVkLlxuICAgICAqL1xuICAgIGluc3BlY3RlZDogSVNpZ25hbDxhbnksIElJbnNwZWN0b3JVcGRhdGU+O1xuXG4gICAgLyoqXG4gICAgICogVGVzdCB3aGV0aGVyIHRoZSBpbnNwZWN0YWJsZSBoYXMgYmVlbiBkaXNwb3NlZC5cbiAgICAgKi9cbiAgICBpc0Rpc3Bvc2VkOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogSW5kaWNhdGVzIHdoZXRoZXIgdGhlIGluc3BlY3RhYmxlIHNvdXJjZSBlbWl0cyBzaWduYWxzLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoZSB1c2UgY2FzZSBmb3IgdGhpcyBhdHRyaWJ1dGUgaXMgdG8gbGltaXQgdGhlIEFQSSB0cmFmZmljIHdoZW4gbm9cbiAgICAgKiBpbnNwZWN0b3IgaXMgdmlzaWJsZS4gSXQgY2FuIGJlIG1vZGlmaWVkIGJ5IHRoZSBjb25zdW1lciBvZiB0aGUgc291cmNlLlxuICAgICAqL1xuICAgIHN0YW5kYnk6IGJvb2xlYW47XG4gICAgLyoqXG4gICAgICogSGFuZGxlIGEgdGV4dCBjaGFuZ2VkIHNpZ25hbCBmcm9tIGFuIGVkaXRvci5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBVcGRhdGUgdGhlIGhpbnRzIGluc3BlY3RvciBiYXNlZCBvbiBhIHRleHQgY2hhbmdlLlxuICAgICAqL1xuICAgIG9uRWRpdG9yQ2hhbmdlKGN1c3RvbVRleHQ/OiBzdHJpbmcpOiB2b2lkO1xuICB9XG5cbiAgLyoqXG4gICAqIEFuIHVwZGF0ZSB2YWx1ZSBmb3IgY29kZSBpbnNwZWN0b3JzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJSW5zcGVjdG9yVXBkYXRlIHtcbiAgICAvKipcbiAgICAgKiBUaGUgY29udGVudCBiZWluZyBzZW50IHRvIHRoZSBpbnNwZWN0b3IgZm9yIGRpc3BsYXkuXG4gICAgICovXG4gICAgY29udGVudDogV2lkZ2V0IHwgbnVsbDtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9