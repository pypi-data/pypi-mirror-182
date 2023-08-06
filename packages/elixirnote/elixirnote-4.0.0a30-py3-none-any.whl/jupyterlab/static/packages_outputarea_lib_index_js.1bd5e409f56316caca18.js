"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_outputarea_lib_index_js"],{

/***/ "../../packages/outputarea/lib/index.js":
/*!**********************************************!*\
  !*** ../../packages/outputarea/lib/index.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OutputArea": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.OutputArea),
/* harmony export */   "OutputAreaModel": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_0__.OutputAreaModel),
/* harmony export */   "OutputPrompt": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.OutputPrompt),
/* harmony export */   "SimplifiedOutputArea": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.SimplifiedOutputArea),
/* harmony export */   "Stdin": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.Stdin)
/* harmony export */ });
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./model */ "../../packages/outputarea/lib/model.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "../../packages/outputarea/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module outputarea
 */




/***/ }),

/***/ "../../packages/outputarea/lib/model.js":
/*!**********************************************!*\
  !*** ../../packages/outputarea/lib/model.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OutputAreaModel": () => (/* binding */ OutputAreaModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/nbformat */ "webpack/sharing/consume/default/@jupyterlab/nbformat/@jupyterlab/nbformat");
/* harmony import */ var _jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.






/**
 * The default implementation of the IOutputAreaModel.
 */
class OutputAreaModel {
    /**
     * Construct a new observable outputs instance.
     */
    constructor(options = {}) {
        /**
         * A flag that is set when we want to clear the output area
         * *after* the next addition to it.
         */
        this.clearNext = false;
        this._lastStream = '';
        this._trusted = false;
        this._isDisposed = false;
        this._stateChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        this._trusted = !!options.trusted;
        this.contentFactory =
            options.contentFactory || OutputAreaModel.defaultContentFactory;
        this.list = new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_1__.ObservableList();
        if (options.values) {
            (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(options.values, value => {
                const index = this._add(value) - 1;
                const item = this.list.get(index);
                item.changed.connect(this._onGenericChange, this);
            });
        }
        this.list.changed.connect(this._onListChanged, this);
    }
    /**
     * A signal emitted when an item changes.
     */
    get stateChanged() {
        return this._stateChanged;
    }
    /**
     * A signal emitted when the list of items changes.
     */
    get changed() {
        return this._changed;
    }
    /**
     * Get the length of the items in the model.
     */
    get length() {
        return this.list ? this.list.length : 0;
    }
    /**
     * Get whether the model is trusted.
     */
    get trusted() {
        return this._trusted;
    }
    /**
     * Set whether the model is trusted.
     *
     * #### Notes
     * Changing the value will cause all of the models to re-set.
     */
    set trusted(value) {
        if (value === this._trusted) {
            return;
        }
        const trusted = (this._trusted = value);
        for (let i = 0; i < this.list.length; i++) {
            const oldItem = this.list.get(i);
            const value = oldItem.toJSON();
            const item = this._createItem({ value, trusted });
            this.list.set(i, item);
            oldItem.dispose();
        }
    }
    /**
     * Test whether the model is disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * Dispose of the resources used by the model.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        this.list.dispose();
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal.clearData(this);
    }
    /**
     * Get an item at the specified index.
     */
    get(index) {
        return this.list.get(index);
    }
    /**
     * Set the value at the specified index.
     */
    set(index, value) {
        value = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__.JSONExt.deepCopy(value);
        // Normalize stream data.
        Private.normalize(value);
        const item = this._createItem({ value, trusted: this._trusted });
        this.list.set(index, item);
    }
    /**
     * Add an output, which may be combined with previous output.
     *
     * @returns The total number of outputs.
     *
     * #### Notes
     * The output bundle is copied.
     * Contiguous stream outputs of the same `name` are combined.
     */
    add(output) {
        // If we received a delayed clear message, then clear now.
        if (this.clearNext) {
            this.clear();
            this.clearNext = false;
        }
        return this._add(output);
    }
    /**
     * Clear all of the output.
     *
     * @param wait Delay clearing the output until the next message is added.
     */
    clear(wait = false) {
        this._lastStream = '';
        if (wait) {
            this.clearNext = true;
            return;
        }
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(this.list, (item) => {
            item.dispose();
        });
        this.list.clear();
    }
    /**
     * Deserialize the model from JSON.
     *
     * #### Notes
     * This will clear any existing data.
     */
    fromJSON(values) {
        this.clear();
        (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.each)(values, value => {
            this._add(value);
        });
    }
    /**
     * Serialize the model to JSON.
     */
    toJSON() {
        return (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.toArray)((0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_3__.map)(this.list, (output) => output.toJSON()));
    }
    /**
     * Add a copy of the item to the list.
     *
     * @returns The list length
     */
    _add(value) {
        const trusted = this._trusted;
        value = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__.JSONExt.deepCopy(value);
        // Normalize the value.
        Private.normalize(value);
        // Consolidate outputs if they are stream outputs of the same kind.
        if (_jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__.isStream(value) &&
            this._lastStream &&
            value.name === this._lastName &&
            this.shouldCombine({
                value,
                lastModel: this.list.get(this.length - 1)
            })) {
            // In order to get a list change event, we add the previous
            // text to the current item and replace the previous item.
            // This also replaces the metadata of the last item.
            this._lastStream += value.text;
            this._lastStream = Private.removeOverwrittenChars(this._lastStream);
            value.text = this._lastStream;
            const item = this._createItem({ value, trusted });
            const index = this.length - 1;
            const prev = this.list.get(index);
            this.list.set(index, item);
            prev.dispose();
            return this.length;
        }
        if (_jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__.isStream(value)) {
            value.text = Private.removeOverwrittenChars(value.text);
        }
        // Create the new item.
        const item = this._createItem({ value, trusted });
        // Update the stream information.
        if (_jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__.isStream(value)) {
            this._lastStream = value.text;
            this._lastName = value.name;
        }
        else {
            this._lastStream = '';
        }
        // Add the item to our list and return the new length.
        return this.list.push(item);
    }
    /**
     * Whether a new value should be consolidated with the previous output.
     *
     * This will only be called if the minimal criteria of both being stream
     * messages of the same type.
     */
    shouldCombine(options) {
        return true;
    }
    /**
     * Create an output item and hook up its signals.
     */
    _createItem(options) {
        const factory = this.contentFactory;
        const item = factory.createOutputModel(options);
        return item;
    }
    /**
     * Handle a change to the list.
     */
    _onListChanged(sender, args) {
        switch (args.type) {
            case 'add':
                args.newValues.forEach(item => {
                    item.changed.connect(this._onGenericChange, this);
                });
                break;
            case 'remove':
                args.oldValues.forEach(item => {
                    item.changed.disconnect(this._onGenericChange, this);
                });
                break;
            case 'set':
                args.newValues.forEach(item => {
                    item.changed.connect(this._onGenericChange, this);
                });
                args.oldValues.forEach(item => {
                    item.changed.disconnect(this._onGenericChange, this);
                });
                break;
        }
        this._changed.emit(args);
    }
    /**
     * Handle a change to an item.
     */
    _onGenericChange(itemModel) {
        let idx;
        for (idx = 0; idx < this.list.length; idx++) {
            const item = this.list.get(idx);
            if (item === itemModel) {
                break;
            }
        }
        this._stateChanged.emit(idx);
    }
}
/**
 * The namespace for OutputAreaModel class statics.
 */
(function (OutputAreaModel) {
    /**
     * The default implementation of a `IModelOutputFactory`.
     */
    class ContentFactory {
        /**
         * Create an output model.
         */
        createOutputModel(options) {
            return new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.OutputModel(options);
        }
    }
    OutputAreaModel.ContentFactory = ContentFactory;
    /**
     * The default output model factory.
     */
    OutputAreaModel.defaultContentFactory = new ContentFactory();
})(OutputAreaModel || (OutputAreaModel = {}));
/**
 * A namespace for module-private functionality.
 */
var Private;
(function (Private) {
    /**
     * Normalize an output.
     */
    function normalize(value) {
        if (_jupyterlab_nbformat__WEBPACK_IMPORTED_MODULE_0__.isStream(value)) {
            if (Array.isArray(value.text)) {
                value.text = value.text.join('\n');
            }
        }
    }
    Private.normalize = normalize;
    /**
     * Remove characters that are overridden by backspace characters.
     */
    function fixBackspace(txt) {
        let tmp = txt;
        do {
            txt = tmp;
            // Cancel out anything-but-newline followed by backspace
            tmp = txt.replace(/[^\n]\x08/gm, ''); // eslint-disable-line no-control-regex
        } while (tmp.length < txt.length);
        return txt;
    }
    /**
     * Remove chunks that should be overridden by the effect of
     * carriage return characters.
     */
    function fixCarriageReturn(txt) {
        txt = txt.replace(/\r+\n/gm, '\n'); // \r followed by \n --> newline
        while (txt.search(/\r[^$]/g) > -1) {
            const base = txt.match(/^(.*)\r+/m)[1];
            let insert = txt.match(/\r+(.*)$/m)[1];
            insert = insert + base.slice(insert.length, base.length);
            txt = txt.replace(/\r+.*$/m, '\r').replace(/^.*\r/m, insert);
        }
        return txt;
    }
    /*
     * Remove characters overridden by backspaces and carriage returns
     */
    function removeOverwrittenChars(text) {
        return fixCarriageReturn(fixBackspace(text));
    }
    Private.removeOverwrittenChars = removeOverwrittenChars;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/outputarea/lib/widget.js":
/*!***********************************************!*\
  !*** ../../packages/outputarea/lib/widget.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OutputArea": () => (/* binding */ OutputArea),
/* harmony export */   "OutputPrompt": () => (/* binding */ OutputPrompt),
/* harmony export */   "SimplifiedOutputArea": () => (/* binding */ SimplifiedOutputArea),
/* harmony export */   "Stdin": () => (/* binding */ Stdin)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/properties */ "webpack/sharing/consume/default/@lumino/properties/@lumino/properties");
/* harmony import */ var _lumino_properties__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_properties__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_6__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.







/**
 * The class name added to an output area widget.
 */
const OUTPUT_AREA_CLASS = 'jp-OutputArea';
/**
 * The class name added to the direction children of OutputArea
 */
const OUTPUT_AREA_ITEM_CLASS = 'jp-OutputArea-child';
/**
 * The class name added to actual outputs
 */
const OUTPUT_AREA_OUTPUT_CLASS = 'jp-OutputArea-output';
/**
 * The class name added to prompt children of OutputArea.
 */
const OUTPUT_AREA_PROMPT_CLASS = 'jp-OutputArea-prompt';
/**
 * The class name added to OutputPrompt.
 */
const OUTPUT_PROMPT_CLASS = 'jp-OutputPrompt';
/**
 * The class name added to an execution result.
 */
const EXECUTE_CLASS = 'jp-OutputArea-executeResult';
/**
 * The class name added stdin items of OutputArea
 */
const OUTPUT_AREA_STDIN_ITEM_CLASS = 'jp-OutputArea-stdin-item';
/**
 * The class name added to stdin widgets.
 */
const STDIN_CLASS = 'jp-Stdin';
/**
 * The class name added to stdin data prompt nodes.
 */
const STDIN_PROMPT_CLASS = 'jp-Stdin-prompt';
/**
 * The class name added to stdin data input nodes.
 */
const STDIN_INPUT_CLASS = 'jp-Stdin-input';
/** ****************************************************************************
 * OutputArea
 ******************************************************************************/
/**
 * An output area widget.
 *
 * #### Notes
 * The widget model must be set separately and can be changed
 * at any time.  Consumers of the widget must account for a
 * `null` model, and may want to listen to the `modelChanged`
 * signal.
 */
class OutputArea extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
    /**
     * Construct an output area widget.
     */
    constructor(options) {
        var _a, _b;
        super();
        /**
         * A public signal used to indicate the number of displayed outputs has changed.
         *
         * #### Notes
         * This is useful for parents who want to apply styling based on the number
         * of outputs. Emits the current number of outputs.
         */
        this.outputLengthChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        /**
         * Handle an iopub message.
         */
        this._onIOPub = (msg) => {
            const model = this.model;
            const msgType = msg.header.msg_type;
            let output;
            const transient = (msg.content.transient || {});
            const displayId = transient['display_id'];
            let targets;
            switch (msgType) {
                case 'execute_result':
                case 'display_data':
                case 'stream':
                case 'error':
                    output = Object.assign(Object.assign({}, msg.content), { output_type: msgType });
                    model.add(output);
                    break;
                case 'clear_output': {
                    const wait = msg.content.wait;
                    model.clear(wait);
                    break;
                }
                case 'update_display_data':
                    output = Object.assign(Object.assign({}, msg.content), { output_type: 'display_data' });
                    targets = this._displayIdMap.get(displayId);
                    if (targets) {
                        for (const index of targets) {
                            model.set(index, output);
                        }
                    }
                    break;
                default:
                    break;
            }
            if (displayId && msgType === 'display_data') {
                targets = this._displayIdMap.get(displayId) || [];
                targets.push(model.length - 1);
                this._displayIdMap.set(displayId, targets);
            }
        };
        /**
         * Handle an execute reply message.
         */
        this._onExecuteReply = (msg) => {
            // API responses that contain a pager are special cased and their type
            // is overridden from 'execute_reply' to 'display_data' in order to
            // render output.
            const model = this.model;
            const content = msg.content;
            if (content.status !== 'ok') {
                return;
            }
            const payload = content && content.payload;
            if (!payload || !payload.length) {
                return;
            }
            const pages = payload.filter((i) => i.source === 'page');
            if (!pages.length) {
                return;
            }
            const page = JSON.parse(JSON.stringify(pages[0]));
            const output = {
                output_type: 'display_data',
                data: page.data,
                metadata: {}
            };
            model.add(output);
        };
        this._minHeightTimeout = null;
        this._displayIdMap = new Map();
        this._outputTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.WidgetTracker({
            namespace: _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__.UUID.uuid4()
        });
        this.addClass(OUTPUT_AREA_CLASS);
        this.contentFactory =
            options.contentFactory || OutputArea.defaultContentFactory;
        this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.PanelLayout();
        this.rendermime = options.rendermime;
        this._maxNumberOutputs = (_a = options.maxNumberOutputs) !== null && _a !== void 0 ? _a : Infinity;
        this._translator = (_b = options.translator) !== null && _b !== void 0 ? _b : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
        const model = (this.model = options.model);
        for (let i = 0; i < Math.min(model.length, this._maxNumberOutputs + 1); i++) {
            const output = model.get(i);
            this._insertOutput(i, output);
        }
        model.changed.connect(this.onModelChanged, this);
        model.stateChanged.connect(this.onStateChanged, this);
    }
    /**
     * A read-only sequence of the children widgets in the output area.
     */
    get widgets() {
        return this.layout.widgets;
    }
    /**
     * The kernel future associated with the output area.
     */
    get future() {
        return this._future;
    }
    set future(value) {
        // Bail if the model is disposed.
        if (this.model.isDisposed) {
            throw Error('Model is disposed');
        }
        if (this._future === value) {
            return;
        }
        if (this._future) {
            this._future.dispose();
        }
        this._future = value;
        this.model.clear();
        // Make sure there were no input widgets.
        if (this.widgets.length) {
            this._clear();
            this.outputLengthChanged.emit(Math.min(this.model.length, this._maxNumberOutputs));
        }
        // Handle published messages.
        value.onIOPub = this._onIOPub;
        // Handle the execute reply.
        value.onReply = this._onExecuteReply;
        // Handle stdin.
        value.onStdin = msg => {
            if (_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.KernelMessage.isInputRequestMsg(msg)) {
                this.onInputRequest(msg, value);
            }
        };
    }
    /**
     * The maximum number of output items to display on top and bottom of cell output.
     *
     * ### Notes
     * It is set to Infinity if no trim is applied.
     */
    get maxNumberOutputs() {
        return this._maxNumberOutputs;
    }
    set maxNumberOutputs(limit) {
        if (limit <= 0) {
            console.warn(`OutputArea.maxNumberOutputs must be strictly positive.`);
            return;
        }
        const lastShown = this._maxNumberOutputs;
        this._maxNumberOutputs = limit;
        if (lastShown < limit) {
            this._showTrimmedOutputs(lastShown);
        }
    }
    /**
     * Dispose of the resources used by the output area.
     */
    dispose() {
        if (this._future) {
            this._future.dispose();
            this._future = null;
        }
        this._displayIdMap.clear();
        this._outputTracker.dispose();
        super.dispose();
    }
    /**
     * Follow changes on the model state.
     */
    onModelChanged(sender, args) {
        switch (args.type) {
            case 'add':
                this._insertOutput(args.newIndex, args.newValues[0]);
                break;
            case 'remove':
                if (this.widgets.length) {
                    // all items removed from model
                    if (this.model.length === 0) {
                        this._clear();
                    }
                    else {
                        // range of items removed from model
                        // remove widgets corresponding to removed model items
                        const startIndex = args.oldIndex;
                        for (let i = 0; i < args.oldValues.length && startIndex < this.widgets.length; ++i) {
                            const widget = this.widgets[startIndex];
                            widget.parent = null;
                            widget.dispose();
                        }
                        // apply item offset to target model item indices in _displayIdMap
                        this._moveDisplayIdIndices(startIndex, args.oldValues.length);
                        // prevent jitter caused by immediate height change
                        this._preventHeightChangeJitter();
                    }
                }
                break;
            case 'set':
                this._setOutput(args.newIndex, args.newValues[0]);
                break;
            default:
                break;
        }
        this.outputLengthChanged.emit(Math.min(this.model.length, this._maxNumberOutputs));
    }
    /**
     * Update indices in _displayIdMap in response to element remove from model items
     *
     * @param startIndex - The index of first element removed
     *
     * @param count - The number of elements removed from model items
     *
     */
    _moveDisplayIdIndices(startIndex, count) {
        this._displayIdMap.forEach((indices) => {
            const rangeEnd = startIndex + count;
            const numIndices = indices.length;
            // reverse loop in order to prevent removing element affecting the index
            for (let i = numIndices - 1; i >= 0; --i) {
                const index = indices[i];
                // remove model item indices in removed range
                if (index >= startIndex && index < rangeEnd) {
                    indices.splice(i, 1);
                }
                else if (index >= rangeEnd) {
                    // move model item indices that were larger than range end
                    indices[i] -= count;
                }
            }
        });
    }
    /**
     * Follow changes on the output model state.
     */
    onStateChanged(sender, change) {
        const outputLength = Math.min(this.model.length, this._maxNumberOutputs);
        if (change) {
            if (change >= this._maxNumberOutputs) {
                // Bail early
                return;
            }
            this._setOutput(change, this.model.get(change));
        }
        else {
            for (let i = 0; i < outputLength; i++) {
                this._setOutput(i, this.model.get(i));
            }
        }
        this.outputLengthChanged.emit(outputLength);
    }
    /**
     * Clear the widget outputs.
     */
    _clear() {
        // Bail if there is no work to do.
        if (!this.widgets.length) {
            return;
        }
        // Remove all of our widgets.
        const length = this.widgets.length;
        for (let i = 0; i < length; i++) {
            const widget = this.widgets[0];
            widget.parent = null;
            widget.dispose();
        }
        // Clear the display id map.
        this._displayIdMap.clear();
        // prevent jitter caused by immediate height change
        this._preventHeightChangeJitter();
    }
    _preventHeightChangeJitter() {
        // When an output area is cleared and then quickly replaced with new
        // content (as happens with @interact in widgets, for example), the
        // quickly changing height can make the page jitter.
        // We introduce a small delay in the minimum height
        // to prevent this jitter.
        const rect = this.node.getBoundingClientRect();
        this.node.style.minHeight = `${rect.height}px`;
        if (this._minHeightTimeout) {
            window.clearTimeout(this._minHeightTimeout);
        }
        this._minHeightTimeout = window.setTimeout(() => {
            if (this.isDisposed) {
                return;
            }
            this.node.style.minHeight = '';
        }, 50);
    }
    /**
     * Handle an input request from a kernel.
     */
    onInputRequest(msg, future) {
        // Add an output widget to the end.
        const factory = this.contentFactory;
        const stdinPrompt = msg.content.prompt;
        const password = msg.content.password;
        const panel = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Panel();
        panel.addClass(OUTPUT_AREA_ITEM_CLASS);
        panel.addClass(OUTPUT_AREA_STDIN_ITEM_CLASS);
        const prompt = factory.createOutputPrompt();
        prompt.addClass(OUTPUT_AREA_PROMPT_CLASS);
        panel.addWidget(prompt);
        const input = factory.createStdin({
            parent_header: msg.header,
            prompt: stdinPrompt,
            password,
            future,
            translator: this._translator
        });
        input.addClass(OUTPUT_AREA_OUTPUT_CLASS);
        panel.addWidget(input);
        // Increase number of outputs to display the result up to the input request.
        if (this.model.length >= this.maxNumberOutputs) {
            this.maxNumberOutputs = this.model.length;
        }
        this.layout.addWidget(panel);
        /**
         * Wait for the stdin to complete, add it to the model (so it persists)
         * and remove the stdin widget.
         */
        void input.value.then(value => {
            // Increase number of outputs to display the result of stdin if needed.
            if (this.model.length >= this.maxNumberOutputs) {
                this.maxNumberOutputs = this.model.length + 1;
            }
            // Use stdin as the stream so it does not get combined with stdout.
            this.model.add({
                output_type: 'stream',
                name: 'stdin',
                text: value + '\n'
            });
            panel.dispose();
        });
    }
    /**
     * Update an output in the layout in place.
     */
    _setOutput(index, model) {
        if (index >= this._maxNumberOutputs) {
            return;
        }
        const panel = this.layout.widgets[index];
        const renderer = (panel.widgets ? panel.widgets[1] : panel);
        // Check whether it is safe to reuse renderer:
        // - Preferred mime type has not changed
        // - Isolation has not changed
        const mimeType = this.rendermime.preferredMimeType(model.data, model.trusted ? 'any' : 'ensure');
        if (Private.currentPreferredMimetype.get(renderer) === mimeType &&
            OutputArea.isIsolated(mimeType, model.metadata) ===
                renderer instanceof Private.IsolatedRenderer) {
            void renderer.renderModel(model);
        }
        else {
            this.layout.widgets[index].dispose();
            this._insertOutput(index, model);
        }
    }
    /**
     * Render and insert a single output into the layout.
     *
     * @param index - The index of the output to be inserted.
     * @param model - The model of the output to be inserted.
     */
    _insertOutput(index, model) {
        if (index > this._maxNumberOutputs) {
            return;
        }
        const layout = this.layout;
        if (index === this._maxNumberOutputs) {
            const warning = new Private.TrimmedOutputs(this._maxNumberOutputs, () => {
                const lastShown = this._maxNumberOutputs;
                this._maxNumberOutputs = Infinity;
                this._showTrimmedOutputs(lastShown);
            });
            layout.insertWidget(index, this._wrappedOutput(warning));
        }
        else {
            let output = this.createOutputItem(model);
            if (output) {
                output.toggleClass(EXECUTE_CLASS, model.executionCount !== null);
            }
            else {
                output = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget();
            }
            if (!this._outputTracker.has(output)) {
                void this._outputTracker.add(output);
            }
            layout.insertWidget(index, output);
        }
    }
    /**
     * A widget tracker for individual output widgets in the output area.
     */
    get outputTracker() {
        return this._outputTracker;
    }
    /**
     * Dispose information message and show output models from the given
     * index to maxNumberOutputs
     *
     * @param lastShown Starting model index to insert.
     */
    _showTrimmedOutputs(lastShown) {
        // Dispose information widget
        this.widgets[lastShown].dispose();
        for (let idx = lastShown; idx < this.model.length; idx++) {
            this._insertOutput(idx, this.model.get(idx));
        }
        this.outputLengthChanged.emit(Math.min(this.model.length, this._maxNumberOutputs));
    }
    /**
     * Create an output item with a prompt and actual output
     *
     * @returns a rendered widget, or null if we cannot render
     * #### Notes
     */
    createOutputItem(model) {
        const output = this.createRenderedMimetype(model);
        if (!output) {
            return null;
        }
        return this._wrappedOutput(output, model.executionCount);
    }
    /**
     * Render a mimetype
     */
    createRenderedMimetype(model) {
        const mimeType = this.rendermime.preferredMimeType(model.data, model.trusted ? 'any' : 'ensure');
        if (!mimeType) {
            return null;
        }
        let output = this.rendermime.createRenderer(mimeType);
        const isolated = OutputArea.isIsolated(mimeType, model.metadata);
        if (isolated === true) {
            output = new Private.IsolatedRenderer(output);
        }
        Private.currentPreferredMimetype.set(output, mimeType);
        output.renderModel(model).catch(error => {
            // Manually append error message to output
            const pre = document.createElement('pre');
            const trans = this._translator.load('jupyterlab');
            pre.textContent = trans.__('Javascript Error: %1', error.message);
            output.node.appendChild(pre);
            // Remove mime-type-specific CSS classes
            output.node.className = 'lm-Widget jp-RenderedText';
            output.node.setAttribute('data-mime-type', 'application/vnd.jupyter.stderr');
        });
        return output;
    }
    /**
     * Wrap a output widget within a output panel
     *
     * @param output Output widget to wrap
     * @param executionCount Execution count
     * @returns The output panel
     */
    _wrappedOutput(output, executionCount = null) {
        const panel = new Private.OutputPanel();
        panel.addClass(OUTPUT_AREA_ITEM_CLASS);
        const prompt = this.contentFactory.createOutputPrompt();
        prompt.executionCount = executionCount;
        prompt.addClass(OUTPUT_AREA_PROMPT_CLASS);
        panel.addWidget(prompt);
        output.addClass(OUTPUT_AREA_OUTPUT_CLASS);
        panel.addWidget(output);
        return panel;
    }
}
class SimplifiedOutputArea extends OutputArea {
    /**
     * Handle an input request from a kernel by doing nothing.
     */
    onInputRequest(msg, future) {
        return;
    }
    /**
     * Create an output item without a prompt, just the output widgets
     */
    createOutputItem(model) {
        const output = this.createRenderedMimetype(model);
        if (output) {
            output.addClass(OUTPUT_AREA_OUTPUT_CLASS);
        }
        return output;
    }
}
/**
 * A namespace for OutputArea statics.
 */
(function (OutputArea) {
    /**
     * Execute code on an output area.
     */
    async function execute(code, output, sessionContext, metadata) {
        var _a;
        // Override the default for `stop_on_error`.
        let stopOnError = true;
        if (metadata &&
            Array.isArray(metadata.tags) &&
            metadata.tags.indexOf('raises-exception') !== -1) {
            stopOnError = false;
        }
        const content = {
            code,
            stop_on_error: stopOnError
        };
        const kernel = (_a = sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if (!kernel) {
            throw new Error('Session has no kernel.');
        }
        const future = kernel.requestExecute(content, false, metadata);
        output.future = future;
        return future.done;
    }
    OutputArea.execute = execute;
    function isIsolated(mimeType, metadata) {
        const mimeMd = metadata[mimeType];
        // mime-specific higher priority
        if (mimeMd && mimeMd['isolated'] !== undefined) {
            return !!mimeMd['isolated'];
        }
        else {
            // fallback on global
            return !!metadata['isolated'];
        }
    }
    OutputArea.isIsolated = isIsolated;
    /**
     * The default implementation of `IContentFactory`.
     */
    class ContentFactory {
        /**
         * Create the output prompt for the widget.
         */
        createOutputPrompt() {
            return new OutputPrompt();
        }
        /**
         * Create an stdin widget.
         */
        createStdin(options) {
            return new Stdin(options);
        }
    }
    OutputArea.ContentFactory = ContentFactory;
    /**
     * The default `ContentFactory` instance.
     */
    OutputArea.defaultContentFactory = new ContentFactory();
})(OutputArea || (OutputArea = {}));
/**
 * The default output prompt implementation
 */
class OutputPrompt extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
    /*
     * Create an output prompt widget.
     */
    constructor() {
        super();
        this._executionCount = null;
        this.addClass(OUTPUT_PROMPT_CLASS);
    }
    /**
     * The execution count for the prompt.
     */
    get executionCount() {
        return this._executionCount;
    }
    set executionCount(value) {
        this._executionCount = value;
        if (value === null) {
            this.node.textContent = '↪ Output';
        }
        else {
            // this.node.textContent = `[${value}]:`;
            this.node.textContent = '↪ Output';
        }
    }
}
/**
 * The default stdin widget.
 */
class Stdin extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
    /**
     * Construct a new input widget.
     */
    constructor(options) {
        var _a;
        super({
            node: Private.createInputWidgetNode(options.prompt, options.password)
        });
        this._promise = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__.PromiseDelegate();
        this.addClass(STDIN_CLASS);
        this._historyIndex = 0;
        this._input = this.node.getElementsByTagName('input')[0];
        this._input.focus();
        this._trans = ((_a = options.translator) !== null && _a !== void 0 ? _a : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator).load('jupyterlab');
        // make users aware of the line history feature
        this._input.placeholder = this._trans.__('↑↓ for history');
        this._future = options.future;
        this._parentHeader = options.parent_header;
        this._value = options.prompt + ' ';
        this._password = options.password;
    }
    static _historyAt(ix) {
        const len = Stdin._history.length;
        // interpret negative ix exactly like Array.at
        ix = ix < 0 ? len + ix : ix;
        if (ix < len) {
            return Stdin._history[ix];
        }
        // return undefined if ix is out of bounds
    }
    static _historyPush(line) {
        Stdin._history.push(line);
        if (Stdin._history.length > 1000) {
            // truncate line history if it's too long
            Stdin._history.shift();
        }
    }
    /**
     * The value of the widget.
     */
    get value() {
        return this._promise.promise.then(() => this._value);
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event - The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the dock panel's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        const input = this._input;
        if (event.type === 'keydown') {
            if (event.key === 'ArrowUp') {
                const historyLine = Stdin._historyAt(this._historyIndex - 1);
                if (historyLine) {
                    if (this._historyIndex === 0) {
                        this._valueCache = input.value;
                    }
                    input.value = historyLine;
                    --this._historyIndex;
                }
            }
            else if (event.key === 'ArrowDown') {
                if (this._historyIndex === 0) {
                    // do nothing
                }
                else if (this._historyIndex === -1) {
                    input.value = this._valueCache;
                    ++this._historyIndex;
                }
                else {
                    const historyLine = Stdin._historyAt(this._historyIndex + 1);
                    if (historyLine) {
                        input.value = historyLine;
                        ++this._historyIndex;
                    }
                }
            }
            else if (event.key === 'Enter') {
                this._future.sendInputReply({
                    status: 'ok',
                    value: input.value
                }, this._parentHeader);
                if (this._password) {
                    this._value += '········';
                }
                else {
                    this._value += input.value;
                    Stdin._historyPush(input.value);
                }
                this._promise.resolve(void 0);
            }
        }
    }
    /**
     * Handle `after-attach` messages sent to the widget.
     */
    onAfterAttach(msg) {
        this._input.addEventListener('keydown', this);
        this.update();
    }
    /**
     * Handle `update-request` messages sent to the widget.
     */
    onUpdateRequest(msg) {
        this._input.focus();
    }
    /**
     * Handle `before-detach` messages sent to the widget.
     */
    onBeforeDetach(msg) {
        this._input.removeEventListener('keydown', this);
    }
}
Stdin._history = [];
/** ****************************************************************************
 * Private namespace
 ******************************************************************************/
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * Create the node for an InputWidget.
     */
    function createInputWidgetNode(prompt, password) {
        const node = document.createElement('div');
        const promptNode = document.createElement('pre');
        promptNode.className = STDIN_PROMPT_CLASS;
        promptNode.textContent = prompt;
        const input = document.createElement('input');
        input.className = STDIN_INPUT_CLASS;
        if (password) {
            input.type = 'password';
        }
        node.appendChild(promptNode);
        promptNode.appendChild(input);
        return node;
    }
    Private.createInputWidgetNode = createInputWidgetNode;
    /**
     * A renderer for IFrame data.
     */
    class IsolatedRenderer extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
        /**
         * Create an isolated renderer.
         */
        constructor(wrapped) {
            super({ node: document.createElement('iframe') });
            this.addClass('jp-mod-isolated');
            this._wrapped = wrapped;
            // Once the iframe is loaded, the subarea is dynamically inserted
            const iframe = this.node;
            iframe.frameBorder = '0';
            iframe.scrolling = 'auto';
            iframe.addEventListener('load', () => {
                // Workaround needed by Firefox, to properly render svg inside
                // iframes, see https://stackoverflow.com/questions/10177190/
                // svg-dynamically-added-to-iframe-does-not-render-correctly
                iframe.contentDocument.open();
                // Insert the subarea into the iframe
                // We must directly write the html. At this point, subarea doesn't
                // contain any user content.
                iframe.contentDocument.write(this._wrapped.node.innerHTML);
                iframe.contentDocument.close();
                const body = iframe.contentDocument.body;
                // Adjust the iframe height automatically
                iframe.style.height = `${body.scrollHeight}px`;
                iframe.heightChangeObserver = new ResizeObserver(() => {
                    iframe.style.height = `${body.scrollHeight}px`;
                });
                iframe.heightChangeObserver.observe(body);
            });
        }
        /**
         * Render a mime model.
         *
         * @param model - The mime model to render.
         *
         * @returns A promise which resolves when rendering is complete.
         *
         * #### Notes
         * This method may be called multiple times during the lifetime
         * of the widget to update it if and when new data is available.
         */
        renderModel(model) {
            return this._wrapped.renderModel(model);
        }
    }
    Private.IsolatedRenderer = IsolatedRenderer;
    Private.currentPreferredMimetype = new _lumino_properties__WEBPACK_IMPORTED_MODULE_4__.AttachedProperty({
        name: 'preferredMimetype',
        create: owner => ''
    });
    /**
     * A `Panel` that's focused by a `contextmenu` event.
     */
    class OutputPanel extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Panel {
        /**
         * Construct a new `OutputPanel` widget.
         */
        constructor(options) {
            super(options);
        }
        /**
         * A callback that focuses on the widget.
         */
        _onContext(_) {
            this.node.focus();
        }
        /**
         * Handle `after-attach` messages sent to the widget.
         */
        onAfterAttach(msg) {
            super.onAfterAttach(msg);
            this.node.addEventListener('contextmenu', this._onContext.bind(this));
        }
        /**
         * Handle `before-detach` messages sent to the widget.
         */
        onBeforeDetach(msg) {
            super.onAfterDetach(msg);
            this.node.removeEventListener('contextmenu', this._onContext.bind(this));
        }
    }
    Private.OutputPanel = OutputPanel;
    /**
     * Trimmed outputs information widget.
     */
    class TrimmedOutputs extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_6__.Widget {
        /**
         * Widget constructor
         *
         * ### Notes
         * The widget will be disposed on click after calling the callback.
         *
         * @param maxNumberOutputs Maximal number of outputs to display
         * @param _onClick Callback on click event on the widget
         */
        constructor(maxNumberOutputs, onClick) {
            const node = document.createElement('div');
            const title = `The first ${maxNumberOutputs} are displayed`;
            const msg = 'Show more outputs';
            node.insertAdjacentHTML('afterbegin', `<a title=${title}>
          <pre>${msg}</pre>
        </a>`);
            super({
                node
            });
            this._onClick = onClick;
            this.addClass('jp-TrimmedOutputs');
            this.addClass('jp-RenderedHTMLCommon');
        }
        /**
         * Handle the DOM events for widget.
         *
         * @param event - The DOM event sent to the widget.
         *
         * #### Notes
         * This method implements the DOM `EventListener` interface and is
         * called in response to events on the widget's DOM node. It should
         * not be called directly by user code.
         */
        handleEvent(event) {
            if (event.type === 'click') {
                this._onClick(event);
            }
        }
        /**
         * Handle `after-attach` messages for the widget.
         */
        onAfterAttach(msg) {
            super.onAfterAttach(msg);
            this.node.addEventListener('click', this);
        }
        /**
         * A message handler invoked on a `'before-detach'`
         * message
         */
        onBeforeDetach(msg) {
            super.onBeforeDetach(msg);
            this.node.removeEventListener('click', this);
        }
    }
    Private.TrimmedOutputs = TrimmedOutputs;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfb3V0cHV0YXJlYV9saWJfaW5kZXhfanMuMWJkNWU0MDlmNTYzMTZjYWNhMTguanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBRXFCO0FBQ0M7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ1J6QiwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBRVY7QUFDeUI7QUFDUDtBQUNaO0FBQ1g7QUFFUTtBQXFIcEQ7O0dBRUc7QUFDSSxNQUFNLGVBQWU7SUFDMUI7O09BRUc7SUFDSCxZQUFZLFVBQXFDLEVBQUU7UUFxT25EOzs7V0FHRztRQUNPLGNBQVMsR0FBRyxLQUFLLENBQUM7UUE2RHBCLGdCQUFXLEdBQUcsRUFBRSxDQUFDO1FBRWpCLGFBQVEsR0FBRyxLQUFLLENBQUM7UUFDakIsZ0JBQVcsR0FBRyxLQUFLLENBQUM7UUFDcEIsa0JBQWEsR0FBRyxJQUFJLHFEQUFNLENBQTBCLElBQUksQ0FBQyxDQUFDO1FBQzFELGFBQVEsR0FBRyxJQUFJLHFEQUFNLENBQzNCLElBQUksQ0FDTCxDQUFDO1FBNVNBLElBQUksQ0FBQyxRQUFRLEdBQUcsQ0FBQyxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUM7UUFDbEMsSUFBSSxDQUFDLGNBQWM7WUFDakIsT0FBTyxDQUFDLGNBQWMsSUFBSSxlQUFlLENBQUMscUJBQXFCLENBQUM7UUFDbEUsSUFBSSxDQUFDLElBQUksR0FBRyxJQUFJLG1FQUFjLEVBQWdCLENBQUM7UUFDL0MsSUFBSSxPQUFPLENBQUMsTUFBTSxFQUFFO1lBQ2xCLHVEQUFJLENBQUMsT0FBTyxDQUFDLE1BQU0sRUFBRSxLQUFLLENBQUMsRUFBRTtnQkFDM0IsTUFBTSxLQUFLLEdBQUcsSUFBSSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLENBQUM7Z0JBQ25DLE1BQU0sSUFBSSxHQUFHLElBQUksQ0FBQyxJQUFJLENBQUMsR0FBRyxDQUFDLEtBQUss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Y0FBYyxDQUFDLEdBQVk7WUFDbkMsS0FBSyxDQUFDLGNBQWMsQ0FBQyxHQUFHLENBQUMsQ0FBQztZQUMxQixJQUFJLENBQUMsSUFBSSxDQUFDLG1CQUFtQixDQUFDLE9BQU8sRUFBRSxJQUFJLENBQUMsQ0FBQztRQUMvQyxDQUFDO0tBR0Y7SUFqRVksc0JBQWMsaUJBaUUxQjtBQUNILENBQUMsRUF4TVMsT0FBTyxLQUFQLE9BQU8sUUF3TWhCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL291dHB1dGFyZWEvc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9vdXRwdXRhcmVhL3NyYy9tb2RlbC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvb3V0cHV0YXJlYS9zcmMvd2lkZ2V0LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIG91dHB1dGFyZWFcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL21vZGVsJztcbmV4cG9ydCAqIGZyb20gJy4vd2lkZ2V0JztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuaW1wb3J0IHsgSU9ic2VydmFibGVMaXN0LCBPYnNlcnZhYmxlTGlzdCB9IGZyb20gJ0BqdXB5dGVybGFiL29ic2VydmFibGVzJztcbmltcG9ydCB7IElPdXRwdXRNb2RlbCwgT3V0cHV0TW9kZWwgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IGVhY2gsIG1hcCwgdG9BcnJheSB9IGZyb20gJ0BsdW1pbm8vYWxnb3JpdGhtJztcbmltcG9ydCB7IEpTT05FeHQgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5cbi8qKlxuICogVGhlIG1vZGVsIGZvciBhbiBvdXRwdXQgYXJlYS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJT3V0cHV0QXJlYU1vZGVsIGV4dGVuZHMgSURpc3Bvc2FibGUge1xuICAvKipcbiAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBvdXRwdXQgaXRlbSBjaGFuZ2VzLlxuICAgKlxuICAgKiBUaGUgbnVtYmVyIGlzIHRoZSBpbmRleCBvZiB0aGUgb3V0cHV0IHRoYXQgY2hhbmdlZC5cbiAgICovXG4gIHJlYWRvbmx5IHN0YXRlQ2hhbmdlZDogSVNpZ25hbDxJT3V0cHV0QXJlYU1vZGVsLCBudW1iZXI+O1xuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIGxpc3Qgb2YgaXRlbXMgY2hhbmdlcy5cbiAgICovXG4gIHJlYWRvbmx5IGNoYW5nZWQ6IElTaWduYWw8SU91dHB1dEFyZWFNb2RlbCwgSU91dHB1dEFyZWFNb2RlbC5DaGFuZ2VkQXJncz47XG5cbiAgLyoqXG4gICAqIFRoZSBsZW5ndGggb2YgdGhlIGl0ZW1zIGluIHRoZSBtb2RlbC5cbiAgICovXG4gIHJlYWRvbmx5IGxlbmd0aDogbnVtYmVyO1xuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBvdXRwdXQgYXJlYSBpcyB0cnVzdGVkLlxuICAgKi9cbiAgdHJ1c3RlZDogYm9vbGVhbjtcblxuICAvKipcbiAgICogVGhlIG91dHB1dCBjb250ZW50IGZhY3RvcnkgdXNlZCBieSB0aGUgbW9kZWwuXG4gICAqL1xuICByZWFkb25seSBjb250ZW50RmFjdG9yeTogSU91dHB1dEFyZWFNb2RlbC5JQ29udGVudEZhY3Rvcnk7XG5cbiAgLyoqXG4gICAqIEdldCBhbiBpdGVtIGF0IHRoZSBzcGVjaWZpZWQgaW5kZXguXG4gICAqL1xuICBnZXQoaW5kZXg6IG51bWJlcik6IElPdXRwdXRNb2RlbDtcblxuICAvKipcbiAgICogQWRkIGFuIG91dHB1dCwgd2hpY2ggbWF5IGJlIGNvbWJpbmVkIHdpdGggcHJldmlvdXMgb3V0cHV0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgdG90YWwgbnVtYmVyIG9mIG91dHB1dHMuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhlIG91dHB1dCBidW5kbGUgaXMgY29waWVkLlxuICAgKiBDb250aWd1b3VzIHN0cmVhbSBvdXRwdXRzIG9mIHRoZSBzYW1lIGBuYW1lYCBhcmUgY29tYmluZWQuXG4gICAqL1xuICBhZGQob3V0cHV0OiBuYmZvcm1hdC5JT3V0cHV0KTogbnVtYmVyO1xuXG4gIC8qKlxuICAgKiBTZXQgdGhlIHZhbHVlIGF0IHRoZSBzcGVjaWZpZWQgaW5kZXguXG4gICAqL1xuICBzZXQoaW5kZXg6IG51bWJlciwgb3V0cHV0OiBuYmZvcm1hdC5JT3V0cHV0KTogdm9pZDtcblxuICAvKipcbiAgICogQ2xlYXIgYWxsIG9mIHRoZSBvdXRwdXQuXG4gICAqXG4gICAqIEBwYXJhbSB3YWl0IC0gRGVsYXkgY2xlYXJpbmcgdGhlIG91dHB1dCB1bnRpbCB0aGUgbmV4dCBtZXNzYWdlIGlzIGFkZGVkLlxuICAgKi9cbiAgY2xlYXIod2FpdD86IGJvb2xlYW4pOiB2b2lkO1xuXG4gIC8qKlxuICAgKiBEZXNlcmlhbGl6ZSB0aGUgbW9kZWwgZnJvbSBKU09OLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgd2lsbCBjbGVhciBhbnkgZXhpc3RpbmcgZGF0YS5cbiAgICovXG4gIGZyb21KU09OKHZhbHVlczogbmJmb3JtYXQuSU91dHB1dFtdKTogdm9pZDtcblxuICAvKipcbiAgICogU2VyaWFsaXplIHRoZSBtb2RlbCB0byBKU09OLlxuICAgKi9cbiAgdG9KU09OKCk6IG5iZm9ybWF0LklPdXRwdXRbXTtcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBJT3V0cHV0QXJlYU1vZGVsIGludGVyZmFjZXMuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSU91dHB1dEFyZWFNb2RlbCB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhIG91dHB1dCBhcmVhIG1vZGVsLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGluaXRpYWwgdmFsdWVzIGZvciB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgdmFsdWVzPzogbmJmb3JtYXQuSU91dHB1dFtdO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgb3V0cHV0IGlzIHRydXN0ZWQuICBUaGUgZGVmYXVsdCBpcyBmYWxzZS5cbiAgICAgKi9cbiAgICB0cnVzdGVkPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBvdXRwdXQgY29udGVudCBmYWN0b3J5IHVzZWQgYnkgdGhlIG1vZGVsLlxuICAgICAqXG4gICAgICogSWYgbm90IGdpdmVuLCBhIGRlZmF1bHQgZmFjdG9yeSB3aWxsIGJlIHVzZWQuXG4gICAgICovXG4gICAgY29udGVudEZhY3Rvcnk/OiBJQ29udGVudEZhY3Rvcnk7XG4gIH1cblxuICAvKipcbiAgICogQSB0eXBlIGFsaWFzIGZvciBjaGFuZ2VkIGFyZ3MuXG4gICAqL1xuICBleHBvcnQgdHlwZSBDaGFuZ2VkQXJncyA9IElPYnNlcnZhYmxlTGlzdC5JQ2hhbmdlZEFyZ3M8SU91dHB1dE1vZGVsPjtcblxuICAvKipcbiAgICogVGhlIGludGVyZmFjZSBmb3IgYW4gb3V0cHV0IGNvbnRlbnQgZmFjdG9yeS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvbnRlbnRGYWN0b3J5IHtcbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYW4gb3V0cHV0IG1vZGVsLlxuICAgICAqL1xuICAgIGNyZWF0ZU91dHB1dE1vZGVsKG9wdGlvbnM6IElPdXRwdXRNb2RlbC5JT3B0aW9ucyk6IElPdXRwdXRNb2RlbDtcbiAgfVxufVxuXG4vKipcbiAqIFRoZSBkZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIHRoZSBJT3V0cHV0QXJlYU1vZGVsLlxuICovXG5leHBvcnQgY2xhc3MgT3V0cHV0QXJlYU1vZGVsIGltcGxlbWVudHMgSU91dHB1dEFyZWFNb2RlbCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgb2JzZXJ2YWJsZSBvdXRwdXRzIGluc3RhbmNlLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogSU91dHB1dEFyZWFNb2RlbC5JT3B0aW9ucyA9IHt9KSB7XG4gICAgdGhpcy5fdHJ1c3RlZCA9ICEhb3B0aW9ucy50cnVzdGVkO1xuICAgIHRoaXMuY29udGVudEZhY3RvcnkgPVxuICAgICAgb3B0aW9ucy5jb250ZW50RmFjdG9yeSB8fCBPdXRwdXRBcmVhTW9kZWwuZGVmYXVsdENvbnRlbnRGYWN0b3J5O1xuICAgIHRoaXMubGlzdCA9IG5ldyBPYnNlcnZhYmxlTGlzdDxJT3V0cHV0TW9kZWw+KCk7XG4gICAgaWYgKG9wdGlvbnMudmFsdWVzKSB7XG4gICAgICBlYWNoKG9wdGlvbnMudmFsdWVzLCB2YWx1ZSA9PiB7XG4gICAgICAgIGNvbnN0IGluZGV4ID0gdGhpcy5fYWRkKHZhbHVlKSAtIDE7XG4gICAgICAgIGNvbnN0IGl0ZW0gPSB0aGlzLmxpc3QuZ2V0KGluZGV4KTtcbiAgICAgICAgaXRlbS5jaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25HZW5lcmljQ2hhbmdlLCB0aGlzKTtcbiAgICAgIH0pO1xuICAgIH1cbiAgICB0aGlzLmxpc3QuY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uTGlzdENoYW5nZWQsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBhbiBpdGVtIGNoYW5nZXMuXG4gICAqL1xuICBnZXQgc3RhdGVDaGFuZ2VkKCk6IElTaWduYWw8SU91dHB1dEFyZWFNb2RlbCwgbnVtYmVyPiB7XG4gICAgcmV0dXJuIHRoaXMuX3N0YXRlQ2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIGxpc3Qgb2YgaXRlbXMgY2hhbmdlcy5cbiAgICovXG4gIGdldCBjaGFuZ2VkKCk6IElTaWduYWw8SU91dHB1dEFyZWFNb2RlbCwgSU91dHB1dEFyZWFNb2RlbC5DaGFuZ2VkQXJncz4ge1xuICAgIHJldHVybiB0aGlzLl9jaGFuZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgbGVuZ3RoIG9mIHRoZSBpdGVtcyBpbiB0aGUgbW9kZWwuXG4gICAqL1xuICBnZXQgbGVuZ3RoKCk6IG51bWJlciB7XG4gICAgcmV0dXJuIHRoaXMubGlzdCA/IHRoaXMubGlzdC5sZW5ndGggOiAwO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB3aGV0aGVyIHRoZSBtb2RlbCBpcyB0cnVzdGVkLlxuICAgKi9cbiAgZ2V0IHRydXN0ZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX3RydXN0ZWQ7XG4gIH1cblxuICAvKipcbiAgICogU2V0IHdoZXRoZXIgdGhlIG1vZGVsIGlzIHRydXN0ZWQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogQ2hhbmdpbmcgdGhlIHZhbHVlIHdpbGwgY2F1c2UgYWxsIG9mIHRoZSBtb2RlbHMgdG8gcmUtc2V0LlxuICAgKi9cbiAgc2V0IHRydXN0ZWQodmFsdWU6IGJvb2xlYW4pIHtcbiAgICBpZiAodmFsdWUgPT09IHRoaXMuX3RydXN0ZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgY29uc3QgdHJ1c3RlZCA9ICh0aGlzLl90cnVzdGVkID0gdmFsdWUpO1xuICAgIGZvciAobGV0IGkgPSAwOyBpIDwgdGhpcy5saXN0Lmxlbmd0aDsgaSsrKSB7XG4gICAgICBjb25zdCBvbGRJdGVtID0gdGhpcy5saXN0LmdldChpKTtcbiAgICAgIGNvbnN0IHZhbHVlID0gb2xkSXRlbS50b0pTT04oKTtcbiAgICAgIGNvbnN0IGl0ZW0gPSB0aGlzLl9jcmVhdGVJdGVtKHsgdmFsdWUsIHRydXN0ZWQgfSk7XG4gICAgICB0aGlzLmxpc3Quc2V0KGksIGl0ZW0pO1xuICAgICAgb2xkSXRlbS5kaXNwb3NlKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBvdXRwdXQgY29udGVudCBmYWN0b3J5IHVzZWQgYnkgdGhlIG1vZGVsLlxuICAgKi9cbiAgcmVhZG9ubHkgY29udGVudEZhY3Rvcnk6IElPdXRwdXRBcmVhTW9kZWwuSUNvbnRlbnRGYWN0b3J5O1xuXG4gIC8qKlxuICAgKiBUZXN0IHdoZXRoZXIgdGhlIG1vZGVsIGlzIGRpc3Bvc2VkLlxuICAgKi9cbiAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2lzRGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIHVzZWQgYnkgdGhlIG1vZGVsLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMuX2lzRGlzcG9zZWQgPSB0cnVlO1xuICAgIHRoaXMubGlzdC5kaXNwb3NlKCk7XG4gICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgYW4gaXRlbSBhdCB0aGUgc3BlY2lmaWVkIGluZGV4LlxuICAgKi9cbiAgZ2V0KGluZGV4OiBudW1iZXIpOiBJT3V0cHV0TW9kZWwge1xuICAgIHJldHVybiB0aGlzLmxpc3QuZ2V0KGluZGV4KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgdGhlIHZhbHVlIGF0IHRoZSBzcGVjaWZpZWQgaW5kZXguXG4gICAqL1xuICBzZXQoaW5kZXg6IG51bWJlciwgdmFsdWU6IG5iZm9ybWF0LklPdXRwdXQpOiB2b2lkIHtcbiAgICB2YWx1ZSA9IEpTT05FeHQuZGVlcENvcHkodmFsdWUpO1xuICAgIC8vIE5vcm1hbGl6ZSBzdHJlYW0gZGF0YS5cbiAgICBQcml2YXRlLm5vcm1hbGl6ZSh2YWx1ZSk7XG4gICAgY29uc3QgaXRlbSA9IHRoaXMuX2NyZWF0ZUl0ZW0oeyB2YWx1ZSwgdHJ1c3RlZDogdGhpcy5fdHJ1c3RlZCB9KTtcbiAgICB0aGlzLmxpc3Quc2V0KGluZGV4LCBpdGVtKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgYW4gb3V0cHV0LCB3aGljaCBtYXkgYmUgY29tYmluZWQgd2l0aCBwcmV2aW91cyBvdXRwdXQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSB0b3RhbCBudW1iZXIgb2Ygb3V0cHV0cy5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGUgb3V0cHV0IGJ1bmRsZSBpcyBjb3BpZWQuXG4gICAqIENvbnRpZ3VvdXMgc3RyZWFtIG91dHB1dHMgb2YgdGhlIHNhbWUgYG5hbWVgIGFyZSBjb21iaW5lZC5cbiAgICovXG4gIGFkZChvdXRwdXQ6IG5iZm9ybWF0LklPdXRwdXQpOiBudW1iZXIge1xuICAgIC8vIElmIHdlIHJlY2VpdmVkIGEgZGVsYXllZCBjbGVhciBtZXNzYWdlLCB0aGVuIGNsZWFyIG5vdy5cbiAgICBpZiAodGhpcy5jbGVhck5leHQpIHtcbiAgICAgIHRoaXMuY2xlYXIoKTtcbiAgICAgIHRoaXMuY2xlYXJOZXh0ID0gZmFsc2U7XG4gICAgfVxuXG4gICAgcmV0dXJuIHRoaXMuX2FkZChvdXRwdXQpO1xuICB9XG5cbiAgLyoqXG4gICAqIENsZWFyIGFsbCBvZiB0aGUgb3V0cHV0LlxuICAgKlxuICAgKiBAcGFyYW0gd2FpdCBEZWxheSBjbGVhcmluZyB0aGUgb3V0cHV0IHVudGlsIHRoZSBuZXh0IG1lc3NhZ2UgaXMgYWRkZWQuXG4gICAqL1xuICBjbGVhcih3YWl0OiBib29sZWFuID0gZmFsc2UpOiB2b2lkIHtcbiAgICB0aGlzLl9sYXN0U3RyZWFtID0gJyc7XG4gICAgaWYgKHdhaXQpIHtcbiAgICAgIHRoaXMuY2xlYXJOZXh0ID0gdHJ1ZTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZWFjaCh0aGlzLmxpc3QsIChpdGVtOiBJT3V0cHV0TW9kZWwpID0+IHtcbiAgICAgIGl0ZW0uZGlzcG9zZSgpO1xuICAgIH0pO1xuICAgIHRoaXMubGlzdC5jbGVhcigpO1xuICB9XG5cbiAgLyoqXG4gICAqIERlc2VyaWFsaXplIHRoZSBtb2RlbCBmcm9tIEpTT04uXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyB3aWxsIGNsZWFyIGFueSBleGlzdGluZyBkYXRhLlxuICAgKi9cbiAgZnJvbUpTT04odmFsdWVzOiBuYmZvcm1hdC5JT3V0cHV0W10pOiB2b2lkIHtcbiAgICB0aGlzLmNsZWFyKCk7XG4gICAgZWFjaCh2YWx1ZXMsIHZhbHVlID0+IHtcbiAgICAgIHRoaXMuX2FkZCh2YWx1ZSk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogU2VyaWFsaXplIHRoZSBtb2RlbCB0byBKU09OLlxuICAgKi9cbiAgdG9KU09OKCk6IG5iZm9ybWF0LklPdXRwdXRbXSB7XG4gICAgcmV0dXJuIHRvQXJyYXkobWFwKHRoaXMubGlzdCwgKG91dHB1dDogSU91dHB1dE1vZGVsKSA9PiBvdXRwdXQudG9KU09OKCkpKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgYSBjb3B5IG9mIHRoZSBpdGVtIHRvIHRoZSBsaXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgbGlzdCBsZW5ndGhcbiAgICovXG4gIHByaXZhdGUgX2FkZCh2YWx1ZTogbmJmb3JtYXQuSU91dHB1dCk6IG51bWJlciB7XG4gICAgY29uc3QgdHJ1c3RlZCA9IHRoaXMuX3RydXN0ZWQ7XG4gICAgdmFsdWUgPSBKU09ORXh0LmRlZXBDb3B5KHZhbHVlKTtcblxuICAgIC8vIE5vcm1hbGl6ZSB0aGUgdmFsdWUuXG4gICAgUHJpdmF0ZS5ub3JtYWxpemUodmFsdWUpO1xuXG4gICAgLy8gQ29uc29saWRhdGUgb3V0cHV0cyBpZiB0aGV5IGFyZSBzdHJlYW0gb3V0cHV0cyBvZiB0aGUgc2FtZSBraW5kLlxuICAgIGlmIChcbiAgICAgIG5iZm9ybWF0LmlzU3RyZWFtKHZhbHVlKSAmJlxuICAgICAgdGhpcy5fbGFzdFN0cmVhbSAmJlxuICAgICAgdmFsdWUubmFtZSA9PT0gdGhpcy5fbGFzdE5hbWUgJiZcbiAgICAgIHRoaXMuc2hvdWxkQ29tYmluZSh7XG4gICAgICAgIHZhbHVlLFxuICAgICAgICBsYXN0TW9kZWw6IHRoaXMubGlzdC5nZXQodGhpcy5sZW5ndGggLSAxKVxuICAgICAgfSlcbiAgICApIHtcbiAgICAgIC8vIEluIG9yZGVyIHRvIGdldCBhIGxpc3QgY2hhbmdlIGV2ZW50LCB3ZSBhZGQgdGhlIHByZXZpb3VzXG4gICAgICAvLyB0ZXh0IHRvIHRoZSBjdXJyZW50IGl0ZW0gYW5kIHJlcGxhY2UgdGhlIHByZXZpb3VzIGl0ZW0uXG4gICAgICAvLyBUaGlzIGFsc28gcmVwbGFjZXMgdGhlIG1ldGFkYXRhIG9mIHRoZSBsYXN0IGl0ZW0uXG4gICAgICB0aGlzLl9sYXN0U3RyZWFtICs9IHZhbHVlLnRleHQgYXMgc3RyaW5nO1xuICAgICAgdGhpcy5fbGFzdFN0cmVhbSA9IFByaXZhdGUucmVtb3ZlT3ZlcndyaXR0ZW5DaGFycyh0aGlzLl9sYXN0U3RyZWFtKTtcbiAgICAgIHZhbHVlLnRleHQgPSB0aGlzLl9sYXN0U3RyZWFtO1xuICAgICAgY29uc3QgaXRlbSA9IHRoaXMuX2NyZWF0ZUl0ZW0oeyB2YWx1ZSwgdHJ1c3RlZCB9KTtcbiAgICAgIGNvbnN0IGluZGV4ID0gdGhpcy5sZW5ndGggLSAxO1xuICAgICAgY29uc3QgcHJldiA9IHRoaXMubGlzdC5nZXQoaW5kZXgpO1xuICAgICAgdGhpcy5saXN0LnNldChpbmRleCwgaXRlbSk7XG4gICAgICBwcmV2LmRpc3Bvc2UoKTtcbiAgICAgIHJldHVybiB0aGlzLmxlbmd0aDtcbiAgICB9XG5cbiAgICBpZiAobmJmb3JtYXQuaXNTdHJlYW0odmFsdWUpKSB7XG4gICAgICB2YWx1ZS50ZXh0ID0gUHJpdmF0ZS5yZW1vdmVPdmVyd3JpdHRlbkNoYXJzKHZhbHVlLnRleHQgYXMgc3RyaW5nKTtcbiAgICB9XG5cbiAgICAvLyBDcmVhdGUgdGhlIG5ldyBpdGVtLlxuICAgIGNvbnN0IGl0ZW0gPSB0aGlzLl9jcmVhdGVJdGVtKHsgdmFsdWUsIHRydXN0ZWQgfSk7XG5cbiAgICAvLyBVcGRhdGUgdGhlIHN0cmVhbSBpbmZvcm1hdGlvbi5cbiAgICBpZiAobmJmb3JtYXQuaXNTdHJlYW0odmFsdWUpKSB7XG4gICAgICB0aGlzLl9sYXN0U3RyZWFtID0gdmFsdWUudGV4dCBhcyBzdHJpbmc7XG4gICAgICB0aGlzLl9sYXN0TmFtZSA9IHZhbHVlLm5hbWU7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMuX2xhc3RTdHJlYW0gPSAnJztcbiAgICB9XG5cbiAgICAvLyBBZGQgdGhlIGl0ZW0gdG8gb3VyIGxpc3QgYW5kIHJldHVybiB0aGUgbmV3IGxlbmd0aC5cbiAgICByZXR1cm4gdGhpcy5saXN0LnB1c2goaXRlbSk7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciBhIG5ldyB2YWx1ZSBzaG91bGQgYmUgY29uc29saWRhdGVkIHdpdGggdGhlIHByZXZpb3VzIG91dHB1dC5cbiAgICpcbiAgICogVGhpcyB3aWxsIG9ubHkgYmUgY2FsbGVkIGlmIHRoZSBtaW5pbWFsIGNyaXRlcmlhIG9mIGJvdGggYmVpbmcgc3RyZWFtXG4gICAqIG1lc3NhZ2VzIG9mIHRoZSBzYW1lIHR5cGUuXG4gICAqL1xuICBwcm90ZWN0ZWQgc2hvdWxkQ29tYmluZShvcHRpb25zOiB7XG4gICAgdmFsdWU6IG5iZm9ybWF0LklPdXRwdXQ7XG4gICAgbGFzdE1vZGVsOiBJT3V0cHV0TW9kZWw7XG4gIH0pOiBib29sZWFuIHtcbiAgICByZXR1cm4gdHJ1ZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIGZsYWcgdGhhdCBpcyBzZXQgd2hlbiB3ZSB3YW50IHRvIGNsZWFyIHRoZSBvdXRwdXQgYXJlYVxuICAgKiAqYWZ0ZXIqIHRoZSBuZXh0IGFkZGl0aW9uIHRvIGl0LlxuICAgKi9cbiAgcHJvdGVjdGVkIGNsZWFyTmV4dCA9IGZhbHNlO1xuXG4gIC8qKlxuICAgKiBBbiBvYnNlcnZhYmxlIGxpc3QgY29udGFpbmluZyB0aGUgb3V0cHV0IG1vZGVsc1xuICAgKiBmb3IgdGhpcyBvdXRwdXQgYXJlYS5cbiAgICovXG4gIHByb3RlY3RlZCBsaXN0OiBJT2JzZXJ2YWJsZUxpc3Q8SU91dHB1dE1vZGVsPjtcblxuICAvKipcbiAgICogQ3JlYXRlIGFuIG91dHB1dCBpdGVtIGFuZCBob29rIHVwIGl0cyBzaWduYWxzLlxuICAgKi9cbiAgcHJpdmF0ZSBfY3JlYXRlSXRlbShvcHRpb25zOiBJT3V0cHV0TW9kZWwuSU9wdGlvbnMpOiBJT3V0cHV0TW9kZWwge1xuICAgIGNvbnN0IGZhY3RvcnkgPSB0aGlzLmNvbnRlbnRGYWN0b3J5O1xuICAgIGNvbnN0IGl0ZW0gPSBmYWN0b3J5LmNyZWF0ZU91dHB1dE1vZGVsKG9wdGlvbnMpO1xuICAgIHJldHVybiBpdGVtO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhIGNoYW5nZSB0byB0aGUgbGlzdC5cbiAgICovXG4gIHByaXZhdGUgX29uTGlzdENoYW5nZWQoXG4gICAgc2VuZGVyOiBJT2JzZXJ2YWJsZUxpc3Q8SU91dHB1dE1vZGVsPixcbiAgICBhcmdzOiBJT2JzZXJ2YWJsZUxpc3QuSUNoYW5nZWRBcmdzPElPdXRwdXRNb2RlbD5cbiAgKSB7XG4gICAgc3dpdGNoIChhcmdzLnR5cGUpIHtcbiAgICAgIGNhc2UgJ2FkZCc6XG4gICAgICAgIGFyZ3MubmV3VmFsdWVzLmZvckVhY2goaXRlbSA9PiB7XG4gICAgICAgICAgaXRlbS5jaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25HZW5lcmljQ2hhbmdlLCB0aGlzKTtcbiAgICAgICAgfSk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAncmVtb3ZlJzpcbiAgICAgICAgYXJncy5vbGRWYWx1ZXMuZm9yRWFjaChpdGVtID0+IHtcbiAgICAgICAgICBpdGVtLmNoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl9vbkdlbmVyaWNDaGFuZ2UsIHRoaXMpO1xuICAgICAgICB9KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdzZXQnOlxuICAgICAgICBhcmdzLm5ld1ZhbHVlcy5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgICAgICAgIGl0ZW0uY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uR2VuZXJpY0NoYW5nZSwgdGhpcyk7XG4gICAgICAgIH0pO1xuICAgICAgICBhcmdzLm9sZFZhbHVlcy5mb3JFYWNoKGl0ZW0gPT4ge1xuICAgICAgICAgIGl0ZW0uY2hhbmdlZC5kaXNjb25uZWN0KHRoaXMuX29uR2VuZXJpY0NoYW5nZSwgdGhpcyk7XG4gICAgICAgIH0pO1xuICAgICAgICBicmVhaztcbiAgICB9XG4gICAgdGhpcy5fY2hhbmdlZC5lbWl0KGFyZ3MpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhIGNoYW5nZSB0byBhbiBpdGVtLlxuICAgKi9cbiAgcHJpdmF0ZSBfb25HZW5lcmljQ2hhbmdlKGl0ZW1Nb2RlbDogSU91dHB1dE1vZGVsKTogdm9pZCB7XG4gICAgbGV0IGlkeDogbnVtYmVyO1xuICAgIGZvciAoaWR4ID0gMDsgaWR4IDwgdGhpcy5saXN0Lmxlbmd0aDsgaWR4KyspIHtcbiAgICAgIGNvbnN0IGl0ZW0gPSB0aGlzLmxpc3QuZ2V0KGlkeCk7XG4gICAgICBpZiAoaXRlbSA9PT0gaXRlbU1vZGVsKSB7XG4gICAgICAgIGJyZWFrO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLl9zdGF0ZUNoYW5nZWQuZW1pdChpZHgpO1xuICB9XG5cbiAgcHJpdmF0ZSBfbGFzdFN0cmVhbSA9ICcnO1xuICBwcml2YXRlIF9sYXN0TmFtZTogJ3N0ZG91dCcgfCAnc3RkZXJyJztcbiAgcHJpdmF0ZSBfdHJ1c3RlZCA9IGZhbHNlO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG4gIHByaXZhdGUgX3N0YXRlQ2hhbmdlZCA9IG5ldyBTaWduYWw8T3V0cHV0QXJlYU1vZGVsLCBudW1iZXI+KHRoaXMpO1xuICBwcml2YXRlIF9jaGFuZ2VkID0gbmV3IFNpZ25hbDxPdXRwdXRBcmVhTW9kZWwsIElPdXRwdXRBcmVhTW9kZWwuQ2hhbmdlZEFyZ3M+KFxuICAgIHRoaXNcbiAgKTtcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBPdXRwdXRBcmVhTW9kZWwgY2xhc3Mgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBPdXRwdXRBcmVhTW9kZWwge1xuICAvKipcbiAgICogVGhlIGRlZmF1bHQgaW1wbGVtZW50YXRpb24gb2YgYSBgSU1vZGVsT3V0cHV0RmFjdG9yeWAuXG4gICAqL1xuICBleHBvcnQgY2xhc3MgQ29udGVudEZhY3RvcnkgaW1wbGVtZW50cyBJT3V0cHV0QXJlYU1vZGVsLklDb250ZW50RmFjdG9yeSB7XG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGFuIG91dHB1dCBtb2RlbC5cbiAgICAgKi9cbiAgICBjcmVhdGVPdXRwdXRNb2RlbChvcHRpb25zOiBJT3V0cHV0TW9kZWwuSU9wdGlvbnMpOiBJT3V0cHV0TW9kZWwge1xuICAgICAgcmV0dXJuIG5ldyBPdXRwdXRNb2RlbChvcHRpb25zKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogVGhlIGRlZmF1bHQgb3V0cHV0IG1vZGVsIGZhY3RvcnkuXG4gICAqL1xuICBleHBvcnQgY29uc3QgZGVmYXVsdENvbnRlbnRGYWN0b3J5ID0gbmV3IENvbnRlbnRGYWN0b3J5KCk7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIG1vZHVsZS1wcml2YXRlIGZ1bmN0aW9uYWxpdHkuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIE5vcm1hbGl6ZSBhbiBvdXRwdXQuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gbm9ybWFsaXplKHZhbHVlOiBuYmZvcm1hdC5JT3V0cHV0KTogdm9pZCB7XG4gICAgaWYgKG5iZm9ybWF0LmlzU3RyZWFtKHZhbHVlKSkge1xuICAgICAgaWYgKEFycmF5LmlzQXJyYXkodmFsdWUudGV4dCkpIHtcbiAgICAgICAgdmFsdWUudGV4dCA9ICh2YWx1ZS50ZXh0IGFzIHN0cmluZ1tdKS5qb2luKCdcXG4nKTtcbiAgICAgIH1cbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogUmVtb3ZlIGNoYXJhY3RlcnMgdGhhdCBhcmUgb3ZlcnJpZGRlbiBieSBiYWNrc3BhY2UgY2hhcmFjdGVycy5cbiAgICovXG4gIGZ1bmN0aW9uIGZpeEJhY2tzcGFjZSh0eHQ6IHN0cmluZyk6IHN0cmluZyB7XG4gICAgbGV0IHRtcCA9IHR4dDtcbiAgICBkbyB7XG4gICAgICB0eHQgPSB0bXA7XG4gICAgICAvLyBDYW5jZWwgb3V0IGFueXRoaW5nLWJ1dC1uZXdsaW5lIGZvbGxvd2VkIGJ5IGJhY2tzcGFjZVxuICAgICAgdG1wID0gdHh0LnJlcGxhY2UoL1teXFxuXVxceDA4L2dtLCAnJyk7IC8vIGVzbGludC1kaXNhYmxlLWxpbmUgbm8tY29udHJvbC1yZWdleFxuICAgIH0gd2hpbGUgKHRtcC5sZW5ndGggPCB0eHQubGVuZ3RoKTtcbiAgICByZXR1cm4gdHh0O1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbW92ZSBjaHVua3MgdGhhdCBzaG91bGQgYmUgb3ZlcnJpZGRlbiBieSB0aGUgZWZmZWN0IG9mXG4gICAqIGNhcnJpYWdlIHJldHVybiBjaGFyYWN0ZXJzLlxuICAgKi9cbiAgZnVuY3Rpb24gZml4Q2FycmlhZ2VSZXR1cm4odHh0OiBzdHJpbmcpOiBzdHJpbmcge1xuICAgIHR4dCA9IHR4dC5yZXBsYWNlKC9cXHIrXFxuL2dtLCAnXFxuJyk7IC8vIFxcciBmb2xsb3dlZCBieSBcXG4gLS0+IG5ld2xpbmVcbiAgICB3aGlsZSAodHh0LnNlYXJjaCgvXFxyW14kXS9nKSA+IC0xKSB7XG4gICAgICBjb25zdCBiYXNlID0gdHh0Lm1hdGNoKC9eKC4qKVxccisvbSkhWzFdO1xuICAgICAgbGV0IGluc2VydCA9IHR4dC5tYXRjaCgvXFxyKyguKikkL20pIVsxXTtcbiAgICAgIGluc2VydCA9IGluc2VydCArIGJhc2Uuc2xpY2UoaW5zZXJ0Lmxlbmd0aCwgYmFzZS5sZW5ndGgpO1xuICAgICAgdHh0ID0gdHh0LnJlcGxhY2UoL1xccisuKiQvbSwgJ1xccicpLnJlcGxhY2UoL14uKlxcci9tLCBpbnNlcnQpO1xuICAgIH1cbiAgICByZXR1cm4gdHh0O1xuICB9XG5cbiAgLypcbiAgICogUmVtb3ZlIGNoYXJhY3RlcnMgb3ZlcnJpZGRlbiBieSBiYWNrc3BhY2VzIGFuZCBjYXJyaWFnZSByZXR1cm5zXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gcmVtb3ZlT3ZlcndyaXR0ZW5DaGFycyh0ZXh0OiBzdHJpbmcpOiBzdHJpbmcge1xuICAgIHJldHVybiBmaXhDYXJyaWFnZVJldHVybihmaXhCYWNrc3BhY2UodGV4dCkpO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZXNzaW9uQ29udGV4dCwgV2lkZ2V0VHJhY2tlciB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCAqIGFzIG5iZm9ybWF0IGZyb20gJ0BqdXB5dGVybGFiL25iZm9ybWF0JztcbmltcG9ydCB7IElPdXRwdXRNb2RlbCwgSVJlbmRlck1pbWVSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUnO1xuaW1wb3J0IHsgSVJlbmRlck1pbWUgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lLWludGVyZmFjZXMnO1xuaW1wb3J0IHsgS2VybmVsLCBLZXJuZWxNZXNzYWdlIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuaW1wb3J0IHtcbiAgSVRyYW5zbGF0b3IsXG4gIG51bGxUcmFuc2xhdG9yLFxuICBUcmFuc2xhdGlvbkJ1bmRsZVxufSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBKU09OT2JqZWN0LFxuICBQcm9taXNlRGVsZWdhdGUsXG4gIFJlYWRvbmx5SlNPTk9iamVjdCxcbiAgUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdCxcbiAgVVVJRFxufSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBNZXNzYWdlIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuaW1wb3J0IHsgQXR0YWNoZWRQcm9wZXJ0eSB9IGZyb20gJ0BsdW1pbm8vcHJvcGVydGllcyc7XG5pbXBvcnQgeyBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBQYW5lbCwgUGFuZWxMYXlvdXQsIFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBJT3V0cHV0QXJlYU1vZGVsIH0gZnJvbSAnLi9tb2RlbCc7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gYW4gb3V0cHV0IGFyZWEgd2lkZ2V0LlxuICovXG5jb25zdCBPVVRQVVRfQVJFQV9DTEFTUyA9ICdqcC1PdXRwdXRBcmVhJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byB0aGUgZGlyZWN0aW9uIGNoaWxkcmVuIG9mIE91dHB1dEFyZWFcbiAqL1xuY29uc3QgT1VUUFVUX0FSRUFfSVRFTV9DTEFTUyA9ICdqcC1PdXRwdXRBcmVhLWNoaWxkJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBhY3R1YWwgb3V0cHV0c1xuICovXG5jb25zdCBPVVRQVVRfQVJFQV9PVVRQVVRfQ0xBU1MgPSAnanAtT3V0cHV0QXJlYS1vdXRwdXQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIHByb21wdCBjaGlsZHJlbiBvZiBPdXRwdXRBcmVhLlxuICovXG5jb25zdCBPVVRQVVRfQVJFQV9QUk9NUFRfQ0xBU1MgPSAnanAtT3V0cHV0QXJlYS1wcm9tcHQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIE91dHB1dFByb21wdC5cbiAqL1xuY29uc3QgT1VUUFVUX1BST01QVF9DTEFTUyA9ICdqcC1PdXRwdXRQcm9tcHQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGFuIGV4ZWN1dGlvbiByZXN1bHQuXG4gKi9cbmNvbnN0IEVYRUNVVEVfQ0xBU1MgPSAnanAtT3V0cHV0QXJlYS1leGVjdXRlUmVzdWx0JztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCBzdGRpbiBpdGVtcyBvZiBPdXRwdXRBcmVhXG4gKi9cbmNvbnN0IE9VVFBVVF9BUkVBX1NURElOX0lURU1fQ0xBU1MgPSAnanAtT3V0cHV0QXJlYS1zdGRpbi1pdGVtJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBzdGRpbiB3aWRnZXRzLlxuICovXG5jb25zdCBTVERJTl9DTEFTUyA9ICdqcC1TdGRpbic7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gc3RkaW4gZGF0YSBwcm9tcHQgbm9kZXMuXG4gKi9cbmNvbnN0IFNURElOX1BST01QVF9DTEFTUyA9ICdqcC1TdGRpbi1wcm9tcHQnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIHN0ZGluIGRhdGEgaW5wdXQgbm9kZXMuXG4gKi9cbmNvbnN0IFNURElOX0lOUFVUX0NMQVNTID0gJ2pwLVN0ZGluLWlucHV0JztcblxuLyoqICoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKipcbiAqIE91dHB1dEFyZWFcbiAqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiovXG5cbi8qKlxuICogQW4gb3V0cHV0IGFyZWEgd2lkZ2V0LlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoZSB3aWRnZXQgbW9kZWwgbXVzdCBiZSBzZXQgc2VwYXJhdGVseSBhbmQgY2FuIGJlIGNoYW5nZWRcbiAqIGF0IGFueSB0aW1lLiAgQ29uc3VtZXJzIG9mIHRoZSB3aWRnZXQgbXVzdCBhY2NvdW50IGZvciBhXG4gKiBgbnVsbGAgbW9kZWwsIGFuZCBtYXkgd2FudCB0byBsaXN0ZW4gdG8gdGhlIGBtb2RlbENoYW5nZWRgXG4gKiBzaWduYWwuXG4gKi9cbmV4cG9ydCBjbGFzcyBPdXRwdXRBcmVhIGV4dGVuZHMgV2lkZ2V0IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhbiBvdXRwdXQgYXJlYSB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBPdXRwdXRBcmVhLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmFkZENsYXNzKE9VVFBVVF9BUkVBX0NMQVNTKTtcblxuICAgIHRoaXMuY29udGVudEZhY3RvcnkgPVxuICAgICAgb3B0aW9ucy5jb250ZW50RmFjdG9yeSB8fCBPdXRwdXRBcmVhLmRlZmF1bHRDb250ZW50RmFjdG9yeTtcbiAgICB0aGlzLmxheW91dCA9IG5ldyBQYW5lbExheW91dCgpO1xuICAgIHRoaXMucmVuZGVybWltZSA9IG9wdGlvbnMucmVuZGVybWltZTtcbiAgICB0aGlzLl9tYXhOdW1iZXJPdXRwdXRzID0gb3B0aW9ucy5tYXhOdW1iZXJPdXRwdXRzID8/IEluZmluaXR5O1xuICAgIHRoaXMuX3RyYW5zbGF0b3IgPSBvcHRpb25zLnRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3I7XG5cbiAgICBjb25zdCBtb2RlbCA9ICh0aGlzLm1vZGVsID0gb3B0aW9ucy5tb2RlbCk7XG4gICAgZm9yIChcbiAgICAgIGxldCBpID0gMDtcbiAgICAgIGkgPCBNYXRoLm1pbihtb2RlbC5sZW5ndGgsIHRoaXMuX21heE51bWJlck91dHB1dHMgKyAxKTtcbiAgICAgIGkrK1xuICAgICkge1xuICAgICAgY29uc3Qgb3V0cHV0ID0gbW9kZWwuZ2V0KGkpO1xuICAgICAgdGhpcy5faW5zZXJ0T3V0cHV0KGksIG91dHB1dCk7XG4gICAgfVxuICAgIG1vZGVsLmNoYW5nZWQuY29ubmVjdCh0aGlzLm9uTW9kZWxDaGFuZ2VkLCB0aGlzKTtcbiAgICBtb2RlbC5zdGF0ZUNoYW5nZWQuY29ubmVjdCh0aGlzLm9uU3RhdGVDaGFuZ2VkLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY29udGVudCBmYWN0b3J5IHVzZWQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIHJlYWRvbmx5IGNvbnRlbnRGYWN0b3J5OiBPdXRwdXRBcmVhLklDb250ZW50RmFjdG9yeTtcblxuICAvKipcbiAgICogTmFycm93IHRoZSB0eXBlIG9mIE91dHB1dEFyZWEncyBsYXlvdXQgcHJvcFxuICAgKi9cbiAgcmVhZG9ubHkgbGF5b3V0OiBQYW5lbExheW91dDtcblxuICAvKipcbiAgICogVGhlIG1vZGVsIHVzZWQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIHJlYWRvbmx5IG1vZGVsOiBJT3V0cHV0QXJlYU1vZGVsO1xuXG4gIC8qKlxuICAgKiBUaGUgcmVuZGVybWltZSBpbnN0YW5jZSB1c2VkIGJ5IHRoZSB3aWRnZXQuXG4gICAqL1xuICByZWFkb25seSByZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5O1xuXG4gIC8qKlxuICAgKiBBIHJlYWQtb25seSBzZXF1ZW5jZSBvZiB0aGUgY2hpbGRyZW4gd2lkZ2V0cyBpbiB0aGUgb3V0cHV0IGFyZWEuXG4gICAqL1xuICBnZXQgd2lkZ2V0cygpOiBSZWFkb25seUFycmF5PFdpZGdldD4ge1xuICAgIHJldHVybiB0aGlzLmxheW91dC53aWRnZXRzO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcHVibGljIHNpZ25hbCB1c2VkIHRvIGluZGljYXRlIHRoZSBudW1iZXIgb2YgZGlzcGxheWVkIG91dHB1dHMgaGFzIGNoYW5nZWQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBpcyB1c2VmdWwgZm9yIHBhcmVudHMgd2hvIHdhbnQgdG8gYXBwbHkgc3R5bGluZyBiYXNlZCBvbiB0aGUgbnVtYmVyXG4gICAqIG9mIG91dHB1dHMuIEVtaXRzIHRoZSBjdXJyZW50IG51bWJlciBvZiBvdXRwdXRzLlxuICAgKi9cbiAgcmVhZG9ubHkgb3V0cHV0TGVuZ3RoQ2hhbmdlZCA9IG5ldyBTaWduYWw8dGhpcywgbnVtYmVyPih0aGlzKTtcblxuICAvKipcbiAgICogVGhlIGtlcm5lbCBmdXR1cmUgYXNzb2NpYXRlZCB3aXRoIHRoZSBvdXRwdXQgYXJlYS5cbiAgICovXG4gIGdldCBmdXR1cmUoKTogS2VybmVsLklTaGVsbEZ1dHVyZTxcbiAgICBLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVxdWVzdE1zZyxcbiAgICBLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVwbHlNc2dcbiAgPiB7XG4gICAgcmV0dXJuIHRoaXMuX2Z1dHVyZTtcbiAgfVxuXG4gIHNldCBmdXR1cmUoXG4gICAgdmFsdWU6IEtlcm5lbC5JU2hlbGxGdXR1cmU8XG4gICAgICBLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVxdWVzdE1zZyxcbiAgICAgIEtlcm5lbE1lc3NhZ2UuSUV4ZWN1dGVSZXBseU1zZ1xuICAgID5cbiAgKSB7XG4gICAgLy8gQmFpbCBpZiB0aGUgbW9kZWwgaXMgZGlzcG9zZWQuXG4gICAgaWYgKHRoaXMubW9kZWwuaXNEaXNwb3NlZCkge1xuICAgICAgdGhyb3cgRXJyb3IoJ01vZGVsIGlzIGRpc3Bvc2VkJyk7XG4gICAgfVxuICAgIGlmICh0aGlzLl9mdXR1cmUgPT09IHZhbHVlKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGlmICh0aGlzLl9mdXR1cmUpIHtcbiAgICAgIHRoaXMuX2Z1dHVyZS5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHRoaXMuX2Z1dHVyZSA9IHZhbHVlO1xuXG4gICAgdGhpcy5tb2RlbC5jbGVhcigpO1xuXG4gICAgLy8gTWFrZSBzdXJlIHRoZXJlIHdlcmUgbm8gaW5wdXQgd2lkZ2V0cy5cbiAgICBpZiAodGhpcy53aWRnZXRzLmxlbmd0aCkge1xuICAgICAgdGhpcy5fY2xlYXIoKTtcbiAgICAgIHRoaXMub3V0cHV0TGVuZ3RoQ2hhbmdlZC5lbWl0KFxuICAgICAgICBNYXRoLm1pbih0aGlzLm1vZGVsLmxlbmd0aCwgdGhpcy5fbWF4TnVtYmVyT3V0cHV0cylcbiAgICAgICk7XG4gICAgfVxuXG4gICAgLy8gSGFuZGxlIHB1Ymxpc2hlZCBtZXNzYWdlcy5cbiAgICB2YWx1ZS5vbklPUHViID0gdGhpcy5fb25JT1B1YjtcblxuICAgIC8vIEhhbmRsZSB0aGUgZXhlY3V0ZSByZXBseS5cbiAgICB2YWx1ZS5vblJlcGx5ID0gdGhpcy5fb25FeGVjdXRlUmVwbHk7XG5cbiAgICAvLyBIYW5kbGUgc3RkaW4uXG4gICAgdmFsdWUub25TdGRpbiA9IG1zZyA9PiB7XG4gICAgICBpZiAoS2VybmVsTWVzc2FnZS5pc0lucHV0UmVxdWVzdE1zZyhtc2cpKSB7XG4gICAgICAgIHRoaXMub25JbnB1dFJlcXVlc3QobXNnLCB2YWx1ZSk7XG4gICAgICB9XG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgbWF4aW11bSBudW1iZXIgb2Ygb3V0cHV0IGl0ZW1zIHRvIGRpc3BsYXkgb24gdG9wIGFuZCBib3R0b20gb2YgY2VsbCBvdXRwdXQuXG4gICAqXG4gICAqICMjIyBOb3Rlc1xuICAgKiBJdCBpcyBzZXQgdG8gSW5maW5pdHkgaWYgbm8gdHJpbSBpcyBhcHBsaWVkLlxuICAgKi9cbiAgZ2V0IG1heE51bWJlck91dHB1dHMoKTogbnVtYmVyIHtcbiAgICByZXR1cm4gdGhpcy5fbWF4TnVtYmVyT3V0cHV0cztcbiAgfVxuICBzZXQgbWF4TnVtYmVyT3V0cHV0cyhsaW1pdDogbnVtYmVyKSB7XG4gICAgaWYgKGxpbWl0IDw9IDApIHtcbiAgICAgIGNvbnNvbGUud2FybihgT3V0cHV0QXJlYS5tYXhOdW1iZXJPdXRwdXRzIG11c3QgYmUgc3RyaWN0bHkgcG9zaXRpdmUuYCk7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IGxhc3RTaG93biA9IHRoaXMuX21heE51bWJlck91dHB1dHM7XG4gICAgdGhpcy5fbWF4TnVtYmVyT3V0cHV0cyA9IGxpbWl0O1xuICAgIGlmIChsYXN0U2hvd24gPCBsaW1pdCkge1xuICAgICAgdGhpcy5fc2hvd1RyaW1tZWRPdXRwdXRzKGxhc3RTaG93bik7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyB1c2VkIGJ5IHRoZSBvdXRwdXQgYXJlYS5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuX2Z1dHVyZSkge1xuICAgICAgdGhpcy5fZnV0dXJlLmRpc3Bvc2UoKTtcbiAgICAgIHRoaXMuX2Z1dHVyZSA9IG51bGwhO1xuICAgIH1cbiAgICB0aGlzLl9kaXNwbGF5SWRNYXAuY2xlYXIoKTtcbiAgICB0aGlzLl9vdXRwdXRUcmFja2VyLmRpc3Bvc2UoKTtcbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogRm9sbG93IGNoYW5nZXMgb24gdGhlIG1vZGVsIHN0YXRlLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uTW9kZWxDaGFuZ2VkKFxuICAgIHNlbmRlcjogSU91dHB1dEFyZWFNb2RlbCxcbiAgICBhcmdzOiBJT3V0cHV0QXJlYU1vZGVsLkNoYW5nZWRBcmdzXG4gICk6IHZvaWQge1xuICAgIHN3aXRjaCAoYXJncy50eXBlKSB7XG4gICAgICBjYXNlICdhZGQnOlxuICAgICAgICB0aGlzLl9pbnNlcnRPdXRwdXQoYXJncy5uZXdJbmRleCwgYXJncy5uZXdWYWx1ZXNbMF0pO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ3JlbW92ZSc6XG4gICAgICAgIGlmICh0aGlzLndpZGdldHMubGVuZ3RoKSB7XG4gICAgICAgICAgLy8gYWxsIGl0ZW1zIHJlbW92ZWQgZnJvbSBtb2RlbFxuICAgICAgICAgIGlmICh0aGlzLm1vZGVsLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICAgICAgdGhpcy5fY2xlYXIoKTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgLy8gcmFuZ2Ugb2YgaXRlbXMgcmVtb3ZlZCBmcm9tIG1vZGVsXG4gICAgICAgICAgICAvLyByZW1vdmUgd2lkZ2V0cyBjb3JyZXNwb25kaW5nIHRvIHJlbW92ZWQgbW9kZWwgaXRlbXNcbiAgICAgICAgICAgIGNvbnN0IHN0YXJ0SW5kZXggPSBhcmdzLm9sZEluZGV4O1xuICAgICAgICAgICAgZm9yIChcbiAgICAgICAgICAgICAgbGV0IGkgPSAwO1xuICAgICAgICAgICAgICBpIDwgYXJncy5vbGRWYWx1ZXMubGVuZ3RoICYmIHN0YXJ0SW5kZXggPCB0aGlzLndpZGdldHMubGVuZ3RoO1xuICAgICAgICAgICAgICArK2lcbiAgICAgICAgICAgICkge1xuICAgICAgICAgICAgICBjb25zdCB3aWRnZXQgPSB0aGlzLndpZGdldHNbc3RhcnRJbmRleF07XG4gICAgICAgICAgICAgIHdpZGdldC5wYXJlbnQgPSBudWxsO1xuICAgICAgICAgICAgICB3aWRnZXQuZGlzcG9zZSgpO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICAvLyBhcHBseSBpdGVtIG9mZnNldCB0byB0YXJnZXQgbW9kZWwgaXRlbSBpbmRpY2VzIGluIF9kaXNwbGF5SWRNYXBcbiAgICAgICAgICAgIHRoaXMuX21vdmVEaXNwbGF5SWRJbmRpY2VzKHN0YXJ0SW5kZXgsIGFyZ3Mub2xkVmFsdWVzLmxlbmd0aCk7XG5cbiAgICAgICAgICAgIC8vIHByZXZlbnQgaml0dGVyIGNhdXNlZCBieSBpbW1lZGlhdGUgaGVpZ2h0IGNoYW5nZVxuICAgICAgICAgICAgdGhpcy5fcHJldmVudEhlaWdodENoYW5nZUppdHRlcigpO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ3NldCc6XG4gICAgICAgIHRoaXMuX3NldE91dHB1dChhcmdzLm5ld0luZGV4LCBhcmdzLm5ld1ZhbHVlc1swXSk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICAgIHRoaXMub3V0cHV0TGVuZ3RoQ2hhbmdlZC5lbWl0KFxuICAgICAgTWF0aC5taW4odGhpcy5tb2RlbC5sZW5ndGgsIHRoaXMuX21heE51bWJlck91dHB1dHMpXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGRhdGUgaW5kaWNlcyBpbiBfZGlzcGxheUlkTWFwIGluIHJlc3BvbnNlIHRvIGVsZW1lbnQgcmVtb3ZlIGZyb20gbW9kZWwgaXRlbXNcbiAgICpcbiAgICogQHBhcmFtIHN0YXJ0SW5kZXggLSBUaGUgaW5kZXggb2YgZmlyc3QgZWxlbWVudCByZW1vdmVkXG4gICAqXG4gICAqIEBwYXJhbSBjb3VudCAtIFRoZSBudW1iZXIgb2YgZWxlbWVudHMgcmVtb3ZlZCBmcm9tIG1vZGVsIGl0ZW1zXG4gICAqXG4gICAqL1xuICBwcml2YXRlIF9tb3ZlRGlzcGxheUlkSW5kaWNlcyhzdGFydEluZGV4OiBudW1iZXIsIGNvdW50OiBudW1iZXIpIHtcbiAgICB0aGlzLl9kaXNwbGF5SWRNYXAuZm9yRWFjaCgoaW5kaWNlczogbnVtYmVyW10pID0+IHtcbiAgICAgIGNvbnN0IHJhbmdlRW5kID0gc3RhcnRJbmRleCArIGNvdW50O1xuICAgICAgY29uc3QgbnVtSW5kaWNlcyA9IGluZGljZXMubGVuZ3RoO1xuICAgICAgLy8gcmV2ZXJzZSBsb29wIGluIG9yZGVyIHRvIHByZXZlbnQgcmVtb3ZpbmcgZWxlbWVudCBhZmZlY3RpbmcgdGhlIGluZGV4XG4gICAgICBmb3IgKGxldCBpID0gbnVtSW5kaWNlcyAtIDE7IGkgPj0gMDsgLS1pKSB7XG4gICAgICAgIGNvbnN0IGluZGV4ID0gaW5kaWNlc1tpXTtcbiAgICAgICAgLy8gcmVtb3ZlIG1vZGVsIGl0ZW0gaW5kaWNlcyBpbiByZW1vdmVkIHJhbmdlXG4gICAgICAgIGlmIChpbmRleCA+PSBzdGFydEluZGV4ICYmIGluZGV4IDwgcmFuZ2VFbmQpIHtcbiAgICAgICAgICBpbmRpY2VzLnNwbGljZShpLCAxKTtcbiAgICAgICAgfSBlbHNlIGlmIChpbmRleCA+PSByYW5nZUVuZCkge1xuICAgICAgICAgIC8vIG1vdmUgbW9kZWwgaXRlbSBpbmRpY2VzIHRoYXQgd2VyZSBsYXJnZXIgdGhhbiByYW5nZSBlbmRcbiAgICAgICAgICBpbmRpY2VzW2ldIC09IGNvdW50O1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogRm9sbG93IGNoYW5nZXMgb24gdGhlIG91dHB1dCBtb2RlbCBzdGF0ZS5cbiAgICovXG4gIHByb3RlY3RlZCBvblN0YXRlQ2hhbmdlZChcbiAgICBzZW5kZXI6IElPdXRwdXRBcmVhTW9kZWwsXG4gICAgY2hhbmdlOiBudW1iZXIgfCB2b2lkXG4gICk6IHZvaWQge1xuICAgIGNvbnN0IG91dHB1dExlbmd0aCA9IE1hdGgubWluKHRoaXMubW9kZWwubGVuZ3RoLCB0aGlzLl9tYXhOdW1iZXJPdXRwdXRzKTtcbiAgICBpZiAoY2hhbmdlKSB7XG4gICAgICBpZiAoY2hhbmdlID49IHRoaXMuX21heE51bWJlck91dHB1dHMpIHtcbiAgICAgICAgLy8gQmFpbCBlYXJseVxuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICB0aGlzLl9zZXRPdXRwdXQoY2hhbmdlLCB0aGlzLm1vZGVsLmdldChjaGFuZ2UpKTtcbiAgICB9IGVsc2Uge1xuICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBvdXRwdXRMZW5ndGg7IGkrKykge1xuICAgICAgICB0aGlzLl9zZXRPdXRwdXQoaSwgdGhpcy5tb2RlbC5nZXQoaSkpO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLm91dHB1dExlbmd0aENoYW5nZWQuZW1pdChvdXRwdXRMZW5ndGgpO1xuICB9XG5cbiAgLyoqXG4gICAqIENsZWFyIHRoZSB3aWRnZXQgb3V0cHV0cy5cbiAgICovXG4gIHByaXZhdGUgX2NsZWFyKCk6IHZvaWQge1xuICAgIC8vIEJhaWwgaWYgdGhlcmUgaXMgbm8gd29yayB0byBkby5cbiAgICBpZiAoIXRoaXMud2lkZ2V0cy5sZW5ndGgpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBSZW1vdmUgYWxsIG9mIG91ciB3aWRnZXRzLlxuICAgIGNvbnN0IGxlbmd0aCA9IHRoaXMud2lkZ2V0cy5sZW5ndGg7XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBsZW5ndGg7IGkrKykge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdGhpcy53aWRnZXRzWzBdO1xuICAgICAgd2lkZ2V0LnBhcmVudCA9IG51bGw7XG4gICAgICB3aWRnZXQuZGlzcG9zZSgpO1xuICAgIH1cblxuICAgIC8vIENsZWFyIHRoZSBkaXNwbGF5IGlkIG1hcC5cbiAgICB0aGlzLl9kaXNwbGF5SWRNYXAuY2xlYXIoKTtcblxuICAgIC8vIHByZXZlbnQgaml0dGVyIGNhdXNlZCBieSBpbW1lZGlhdGUgaGVpZ2h0IGNoYW5nZVxuICAgIHRoaXMuX3ByZXZlbnRIZWlnaHRDaGFuZ2VKaXR0ZXIoKTtcbiAgfVxuXG4gIHByaXZhdGUgX3ByZXZlbnRIZWlnaHRDaGFuZ2VKaXR0ZXIoKSB7XG4gICAgLy8gV2hlbiBhbiBvdXRwdXQgYXJlYSBpcyBjbGVhcmVkIGFuZCB0aGVuIHF1aWNrbHkgcmVwbGFjZWQgd2l0aCBuZXdcbiAgICAvLyBjb250ZW50IChhcyBoYXBwZW5zIHdpdGggQGludGVyYWN0IGluIHdpZGdldHMsIGZvciBleGFtcGxlKSwgdGhlXG4gICAgLy8gcXVpY2tseSBjaGFuZ2luZyBoZWlnaHQgY2FuIG1ha2UgdGhlIHBhZ2Ugaml0dGVyLlxuICAgIC8vIFdlIGludHJvZHVjZSBhIHNtYWxsIGRlbGF5IGluIHRoZSBtaW5pbXVtIGhlaWdodFxuICAgIC8vIHRvIHByZXZlbnQgdGhpcyBqaXR0ZXIuXG4gICAgY29uc3QgcmVjdCA9IHRoaXMubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICB0aGlzLm5vZGUuc3R5bGUubWluSGVpZ2h0ID0gYCR7cmVjdC5oZWlnaHR9cHhgO1xuICAgIGlmICh0aGlzLl9taW5IZWlnaHRUaW1lb3V0KSB7XG4gICAgICB3aW5kb3cuY2xlYXJUaW1lb3V0KHRoaXMuX21pbkhlaWdodFRpbWVvdXQpO1xuICAgIH1cbiAgICB0aGlzLl9taW5IZWlnaHRUaW1lb3V0ID0gd2luZG93LnNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICB0aGlzLm5vZGUuc3R5bGUubWluSGVpZ2h0ID0gJyc7XG4gICAgfSwgNTApO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbiBpbnB1dCByZXF1ZXN0IGZyb20gYSBrZXJuZWwuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25JbnB1dFJlcXVlc3QoXG4gICAgbXNnOiBLZXJuZWxNZXNzYWdlLklJbnB1dFJlcXVlc3RNc2csXG4gICAgZnV0dXJlOiBLZXJuZWwuSVNoZWxsRnV0dXJlXG4gICk6IHZvaWQge1xuICAgIC8vIEFkZCBhbiBvdXRwdXQgd2lkZ2V0IHRvIHRoZSBlbmQuXG4gICAgY29uc3QgZmFjdG9yeSA9IHRoaXMuY29udGVudEZhY3Rvcnk7XG4gICAgY29uc3Qgc3RkaW5Qcm9tcHQgPSBtc2cuY29udGVudC5wcm9tcHQ7XG4gICAgY29uc3QgcGFzc3dvcmQgPSBtc2cuY29udGVudC5wYXNzd29yZDtcblxuICAgIGNvbnN0IHBhbmVsID0gbmV3IFBhbmVsKCk7XG4gICAgcGFuZWwuYWRkQ2xhc3MoT1VUUFVUX0FSRUFfSVRFTV9DTEFTUyk7XG4gICAgcGFuZWwuYWRkQ2xhc3MoT1VUUFVUX0FSRUFfU1RESU5fSVRFTV9DTEFTUyk7XG5cbiAgICBjb25zdCBwcm9tcHQgPSBmYWN0b3J5LmNyZWF0ZU91dHB1dFByb21wdCgpO1xuICAgIHByb21wdC5hZGRDbGFzcyhPVVRQVVRfQVJFQV9QUk9NUFRfQ0xBU1MpO1xuICAgIHBhbmVsLmFkZFdpZGdldChwcm9tcHQpO1xuXG4gICAgY29uc3QgaW5wdXQgPSBmYWN0b3J5LmNyZWF0ZVN0ZGluKHtcbiAgICAgIHBhcmVudF9oZWFkZXI6IG1zZy5oZWFkZXIsXG4gICAgICBwcm9tcHQ6IHN0ZGluUHJvbXB0LFxuICAgICAgcGFzc3dvcmQsXG4gICAgICBmdXR1cmUsXG4gICAgICB0cmFuc2xhdG9yOiB0aGlzLl90cmFuc2xhdG9yXG4gICAgfSk7XG4gICAgaW5wdXQuYWRkQ2xhc3MoT1VUUFVUX0FSRUFfT1VUUFVUX0NMQVNTKTtcbiAgICBwYW5lbC5hZGRXaWRnZXQoaW5wdXQpO1xuXG4gICAgLy8gSW5jcmVhc2UgbnVtYmVyIG9mIG91dHB1dHMgdG8gZGlzcGxheSB0aGUgcmVzdWx0IHVwIHRvIHRoZSBpbnB1dCByZXF1ZXN0LlxuICAgIGlmICh0aGlzLm1vZGVsLmxlbmd0aCA+PSB0aGlzLm1heE51bWJlck91dHB1dHMpIHtcbiAgICAgIHRoaXMubWF4TnVtYmVyT3V0cHV0cyA9IHRoaXMubW9kZWwubGVuZ3RoO1xuICAgIH1cbiAgICB0aGlzLmxheW91dC5hZGRXaWRnZXQocGFuZWwpO1xuXG4gICAgLyoqXG4gICAgICogV2FpdCBmb3IgdGhlIHN0ZGluIHRvIGNvbXBsZXRlLCBhZGQgaXQgdG8gdGhlIG1vZGVsIChzbyBpdCBwZXJzaXN0cylcbiAgICAgKiBhbmQgcmVtb3ZlIHRoZSBzdGRpbiB3aWRnZXQuXG4gICAgICovXG4gICAgdm9pZCBpbnB1dC52YWx1ZS50aGVuKHZhbHVlID0+IHtcbiAgICAgIC8vIEluY3JlYXNlIG51bWJlciBvZiBvdXRwdXRzIHRvIGRpc3BsYXkgdGhlIHJlc3VsdCBvZiBzdGRpbiBpZiBuZWVkZWQuXG4gICAgICBpZiAodGhpcy5tb2RlbC5sZW5ndGggPj0gdGhpcy5tYXhOdW1iZXJPdXRwdXRzKSB7XG4gICAgICAgIHRoaXMubWF4TnVtYmVyT3V0cHV0cyA9IHRoaXMubW9kZWwubGVuZ3RoICsgMTtcbiAgICAgIH1cbiAgICAgIC8vIFVzZSBzdGRpbiBhcyB0aGUgc3RyZWFtIHNvIGl0IGRvZXMgbm90IGdldCBjb21iaW5lZCB3aXRoIHN0ZG91dC5cbiAgICAgIHRoaXMubW9kZWwuYWRkKHtcbiAgICAgICAgb3V0cHV0X3R5cGU6ICdzdHJlYW0nLFxuICAgICAgICBuYW1lOiAnc3RkaW4nLFxuICAgICAgICB0ZXh0OiB2YWx1ZSArICdcXG4nXG4gICAgICB9KTtcbiAgICAgIHBhbmVsLmRpc3Bvc2UoKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGRhdGUgYW4gb3V0cHV0IGluIHRoZSBsYXlvdXQgaW4gcGxhY2UuXG4gICAqL1xuICBwcml2YXRlIF9zZXRPdXRwdXQoaW5kZXg6IG51bWJlciwgbW9kZWw6IElPdXRwdXRNb2RlbCk6IHZvaWQge1xuICAgIGlmIChpbmRleCA+PSB0aGlzLl9tYXhOdW1iZXJPdXRwdXRzKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHBhbmVsID0gdGhpcy5sYXlvdXQud2lkZ2V0c1tpbmRleF0gYXMgUGFuZWw7XG4gICAgY29uc3QgcmVuZGVyZXIgPSAoXG4gICAgICBwYW5lbC53aWRnZXRzID8gcGFuZWwud2lkZ2V0c1sxXSA6IHBhbmVsXG4gICAgKSBhcyBJUmVuZGVyTWltZS5JUmVuZGVyZXI7XG4gICAgLy8gQ2hlY2sgd2hldGhlciBpdCBpcyBzYWZlIHRvIHJldXNlIHJlbmRlcmVyOlxuICAgIC8vIC0gUHJlZmVycmVkIG1pbWUgdHlwZSBoYXMgbm90IGNoYW5nZWRcbiAgICAvLyAtIElzb2xhdGlvbiBoYXMgbm90IGNoYW5nZWRcbiAgICBjb25zdCBtaW1lVHlwZSA9IHRoaXMucmVuZGVybWltZS5wcmVmZXJyZWRNaW1lVHlwZShcbiAgICAgIG1vZGVsLmRhdGEsXG4gICAgICBtb2RlbC50cnVzdGVkID8gJ2FueScgOiAnZW5zdXJlJ1xuICAgICk7XG4gICAgaWYgKFxuICAgICAgUHJpdmF0ZS5jdXJyZW50UHJlZmVycmVkTWltZXR5cGUuZ2V0KHJlbmRlcmVyKSA9PT0gbWltZVR5cGUgJiZcbiAgICAgIE91dHB1dEFyZWEuaXNJc29sYXRlZChtaW1lVHlwZSwgbW9kZWwubWV0YWRhdGEpID09PVxuICAgICAgICByZW5kZXJlciBpbnN0YW5jZW9mIFByaXZhdGUuSXNvbGF0ZWRSZW5kZXJlclxuICAgICkge1xuICAgICAgdm9pZCByZW5kZXJlci5yZW5kZXJNb2RlbChtb2RlbCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMubGF5b3V0LndpZGdldHNbaW5kZXhdLmRpc3Bvc2UoKTtcbiAgICAgIHRoaXMuX2luc2VydE91dHB1dChpbmRleCwgbW9kZWwpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgYW5kIGluc2VydCBhIHNpbmdsZSBvdXRwdXQgaW50byB0aGUgbGF5b3V0LlxuICAgKlxuICAgKiBAcGFyYW0gaW5kZXggLSBUaGUgaW5kZXggb2YgdGhlIG91dHB1dCB0byBiZSBpbnNlcnRlZC5cbiAgICogQHBhcmFtIG1vZGVsIC0gVGhlIG1vZGVsIG9mIHRoZSBvdXRwdXQgdG8gYmUgaW5zZXJ0ZWQuXG4gICAqL1xuICBwcml2YXRlIF9pbnNlcnRPdXRwdXQoaW5kZXg6IG51bWJlciwgbW9kZWw6IElPdXRwdXRNb2RlbCk6IHZvaWQge1xuICAgIGlmIChpbmRleCA+IHRoaXMuX21heE51bWJlck91dHB1dHMpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBsYXlvdXQgPSB0aGlzLmxheW91dCBhcyBQYW5lbExheW91dDtcblxuICAgIGlmIChpbmRleCA9PT0gdGhpcy5fbWF4TnVtYmVyT3V0cHV0cykge1xuICAgICAgY29uc3Qgd2FybmluZyA9IG5ldyBQcml2YXRlLlRyaW1tZWRPdXRwdXRzKHRoaXMuX21heE51bWJlck91dHB1dHMsICgpID0+IHtcbiAgICAgICAgY29uc3QgbGFzdFNob3duID0gdGhpcy5fbWF4TnVtYmVyT3V0cHV0cztcbiAgICAgICAgdGhpcy5fbWF4TnVtYmVyT3V0cHV0cyA9IEluZmluaXR5O1xuICAgICAgICB0aGlzLl9zaG93VHJpbW1lZE91dHB1dHMobGFzdFNob3duKTtcbiAgICAgIH0pO1xuICAgICAgbGF5b3V0Lmluc2VydFdpZGdldChpbmRleCwgdGhpcy5fd3JhcHBlZE91dHB1dCh3YXJuaW5nKSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIGxldCBvdXRwdXQgPSB0aGlzLmNyZWF0ZU91dHB1dEl0ZW0obW9kZWwpO1xuICAgICAgaWYgKG91dHB1dCkge1xuICAgICAgICBvdXRwdXQudG9nZ2xlQ2xhc3MoRVhFQ1VURV9DTEFTUywgbW9kZWwuZXhlY3V0aW9uQ291bnQgIT09IG51bGwpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgb3V0cHV0ID0gbmV3IFdpZGdldCgpO1xuICAgICAgfVxuXG4gICAgICBpZiAoIXRoaXMuX291dHB1dFRyYWNrZXIuaGFzKG91dHB1dCkpIHtcbiAgICAgICAgdm9pZCB0aGlzLl9vdXRwdXRUcmFja2VyLmFkZChvdXRwdXQpO1xuICAgICAgfVxuICAgICAgbGF5b3V0Lmluc2VydFdpZGdldChpbmRleCwgb3V0cHV0KTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQSB3aWRnZXQgdHJhY2tlciBmb3IgaW5kaXZpZHVhbCBvdXRwdXQgd2lkZ2V0cyBpbiB0aGUgb3V0cHV0IGFyZWEuXG4gICAqL1xuICBnZXQgb3V0cHV0VHJhY2tlcigpOiBXaWRnZXRUcmFja2VyPFdpZGdldD4ge1xuICAgIHJldHVybiB0aGlzLl9vdXRwdXRUcmFja2VyO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2UgaW5mb3JtYXRpb24gbWVzc2FnZSBhbmQgc2hvdyBvdXRwdXQgbW9kZWxzIGZyb20gdGhlIGdpdmVuXG4gICAqIGluZGV4IHRvIG1heE51bWJlck91dHB1dHNcbiAgICpcbiAgICogQHBhcmFtIGxhc3RTaG93biBTdGFydGluZyBtb2RlbCBpbmRleCB0byBpbnNlcnQuXG4gICAqL1xuICBwcml2YXRlIF9zaG93VHJpbW1lZE91dHB1dHMobGFzdFNob3duOiBudW1iZXIpIHtcbiAgICAvLyBEaXNwb3NlIGluZm9ybWF0aW9uIHdpZGdldFxuICAgIHRoaXMud2lkZ2V0c1tsYXN0U2hvd25dLmRpc3Bvc2UoKTtcblxuICAgIGZvciAobGV0IGlkeCA9IGxhc3RTaG93bjsgaWR4IDwgdGhpcy5tb2RlbC5sZW5ndGg7IGlkeCsrKSB7XG4gICAgICB0aGlzLl9pbnNlcnRPdXRwdXQoaWR4LCB0aGlzLm1vZGVsLmdldChpZHgpKTtcbiAgICB9XG5cbiAgICB0aGlzLm91dHB1dExlbmd0aENoYW5nZWQuZW1pdChcbiAgICAgIE1hdGgubWluKHRoaXMubW9kZWwubGVuZ3RoLCB0aGlzLl9tYXhOdW1iZXJPdXRwdXRzKVxuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGFuIG91dHB1dCBpdGVtIHdpdGggYSBwcm9tcHQgYW5kIGFjdHVhbCBvdXRwdXRcbiAgICpcbiAgICogQHJldHVybnMgYSByZW5kZXJlZCB3aWRnZXQsIG9yIG51bGwgaWYgd2UgY2Fubm90IHJlbmRlclxuICAgKiAjIyMjIE5vdGVzXG4gICAqL1xuICBwcm90ZWN0ZWQgY3JlYXRlT3V0cHV0SXRlbShtb2RlbDogSU91dHB1dE1vZGVsKTogV2lkZ2V0IHwgbnVsbCB7XG4gICAgY29uc3Qgb3V0cHV0ID0gdGhpcy5jcmVhdGVSZW5kZXJlZE1pbWV0eXBlKG1vZGVsKTtcblxuICAgIGlmICghb3V0cHV0KSB7XG4gICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG5cbiAgICByZXR1cm4gdGhpcy5fd3JhcHBlZE91dHB1dChvdXRwdXQsIG1vZGVsLmV4ZWN1dGlvbkNvdW50KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgYSBtaW1ldHlwZVxuICAgKi9cbiAgcHJvdGVjdGVkIGNyZWF0ZVJlbmRlcmVkTWltZXR5cGUobW9kZWw6IElPdXRwdXRNb2RlbCk6IFdpZGdldCB8IG51bGwge1xuICAgIGNvbnN0IG1pbWVUeXBlID0gdGhpcy5yZW5kZXJtaW1lLnByZWZlcnJlZE1pbWVUeXBlKFxuICAgICAgbW9kZWwuZGF0YSxcbiAgICAgIG1vZGVsLnRydXN0ZWQgPyAnYW55JyA6ICdlbnN1cmUnXG4gICAgKTtcblxuICAgIGlmICghbWltZVR5cGUpIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbiAgICBsZXQgb3V0cHV0ID0gdGhpcy5yZW5kZXJtaW1lLmNyZWF0ZVJlbmRlcmVyKG1pbWVUeXBlKTtcbiAgICBjb25zdCBpc29sYXRlZCA9IE91dHB1dEFyZWEuaXNJc29sYXRlZChtaW1lVHlwZSwgbW9kZWwubWV0YWRhdGEpO1xuICAgIGlmIChpc29sYXRlZCA9PT0gdHJ1ZSkge1xuICAgICAgb3V0cHV0ID0gbmV3IFByaXZhdGUuSXNvbGF0ZWRSZW5kZXJlcihvdXRwdXQpO1xuICAgIH1cbiAgICBQcml2YXRlLmN1cnJlbnRQcmVmZXJyZWRNaW1ldHlwZS5zZXQob3V0cHV0LCBtaW1lVHlwZSk7XG4gICAgb3V0cHV0LnJlbmRlck1vZGVsKG1vZGVsKS5jYXRjaChlcnJvciA9PiB7XG4gICAgICAvLyBNYW51YWxseSBhcHBlbmQgZXJyb3IgbWVzc2FnZSB0byBvdXRwdXRcbiAgICAgIGNvbnN0IHByZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3ByZScpO1xuICAgICAgY29uc3QgdHJhbnMgPSB0aGlzLl90cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICAgIHByZS50ZXh0Q29udGVudCA9IHRyYW5zLl9fKCdKYXZhc2NyaXB0IEVycm9yOiAlMScsIGVycm9yLm1lc3NhZ2UpO1xuICAgICAgb3V0cHV0Lm5vZGUuYXBwZW5kQ2hpbGQocHJlKTtcblxuICAgICAgLy8gUmVtb3ZlIG1pbWUtdHlwZS1zcGVjaWZpYyBDU1MgY2xhc3Nlc1xuICAgICAgb3V0cHV0Lm5vZGUuY2xhc3NOYW1lID0gJ2xtLVdpZGdldCBqcC1SZW5kZXJlZFRleHQnO1xuICAgICAgb3V0cHV0Lm5vZGUuc2V0QXR0cmlidXRlKFxuICAgICAgICAnZGF0YS1taW1lLXR5cGUnLFxuICAgICAgICAnYXBwbGljYXRpb24vdm5kLmp1cHl0ZXIuc3RkZXJyJ1xuICAgICAgKTtcbiAgICB9KTtcbiAgICByZXR1cm4gb3V0cHV0O1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbiBpb3B1YiBtZXNzYWdlLlxuICAgKi9cbiAgcHJpdmF0ZSBfb25JT1B1YiA9IChtc2c6IEtlcm5lbE1lc3NhZ2UuSUlPUHViTWVzc2FnZSkgPT4ge1xuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5tb2RlbDtcbiAgICBjb25zdCBtc2dUeXBlID0gbXNnLmhlYWRlci5tc2dfdHlwZTtcbiAgICBsZXQgb3V0cHV0OiBuYmZvcm1hdC5JT3V0cHV0O1xuICAgIGNvbnN0IHRyYW5zaWVudCA9ICgobXNnLmNvbnRlbnQgYXMgYW55KS50cmFuc2llbnQgfHwge30pIGFzIEpTT05PYmplY3Q7XG4gICAgY29uc3QgZGlzcGxheUlkID0gdHJhbnNpZW50WydkaXNwbGF5X2lkJ10gYXMgc3RyaW5nO1xuICAgIGxldCB0YXJnZXRzOiBudW1iZXJbXSB8IHVuZGVmaW5lZDtcblxuICAgIHN3aXRjaCAobXNnVHlwZSkge1xuICAgICAgY2FzZSAnZXhlY3V0ZV9yZXN1bHQnOlxuICAgICAgY2FzZSAnZGlzcGxheV9kYXRhJzpcbiAgICAgIGNhc2UgJ3N0cmVhbSc6XG4gICAgICBjYXNlICdlcnJvcic6XG4gICAgICAgIG91dHB1dCA9IHsgLi4ubXNnLmNvbnRlbnQsIG91dHB1dF90eXBlOiBtc2dUeXBlIH07XG4gICAgICAgIG1vZGVsLmFkZChvdXRwdXQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2NsZWFyX291dHB1dCc6IHtcbiAgICAgICAgY29uc3Qgd2FpdCA9IChtc2cgYXMgS2VybmVsTWVzc2FnZS5JQ2xlYXJPdXRwdXRNc2cpLmNvbnRlbnQud2FpdDtcbiAgICAgICAgbW9kZWwuY2xlYXIod2FpdCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgfVxuICAgICAgY2FzZSAndXBkYXRlX2Rpc3BsYXlfZGF0YSc6XG4gICAgICAgIG91dHB1dCA9IHsgLi4ubXNnLmNvbnRlbnQsIG91dHB1dF90eXBlOiAnZGlzcGxheV9kYXRhJyB9O1xuICAgICAgICB0YXJnZXRzID0gdGhpcy5fZGlzcGxheUlkTWFwLmdldChkaXNwbGF5SWQpO1xuICAgICAgICBpZiAodGFyZ2V0cykge1xuICAgICAgICAgIGZvciAoY29uc3QgaW5kZXggb2YgdGFyZ2V0cykge1xuICAgICAgICAgICAgbW9kZWwuc2V0KGluZGV4LCBvdXRwdXQpO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgICBpZiAoZGlzcGxheUlkICYmIG1zZ1R5cGUgPT09ICdkaXNwbGF5X2RhdGEnKSB7XG4gICAgICB0YXJnZXRzID0gdGhpcy5fZGlzcGxheUlkTWFwLmdldChkaXNwbGF5SWQpIHx8IFtdO1xuICAgICAgdGFyZ2V0cy5wdXNoKG1vZGVsLmxlbmd0aCAtIDEpO1xuICAgICAgdGhpcy5fZGlzcGxheUlkTWFwLnNldChkaXNwbGF5SWQsIHRhcmdldHMpO1xuICAgIH1cbiAgfTtcblxuICAvKipcbiAgICogSGFuZGxlIGFuIGV4ZWN1dGUgcmVwbHkgbWVzc2FnZS5cbiAgICovXG4gIHByaXZhdGUgX29uRXhlY3V0ZVJlcGx5ID0gKG1zZzogS2VybmVsTWVzc2FnZS5JRXhlY3V0ZVJlcGx5TXNnKSA9PiB7XG4gICAgLy8gQVBJIHJlc3BvbnNlcyB0aGF0IGNvbnRhaW4gYSBwYWdlciBhcmUgc3BlY2lhbCBjYXNlZCBhbmQgdGhlaXIgdHlwZVxuICAgIC8vIGlzIG92ZXJyaWRkZW4gZnJvbSAnZXhlY3V0ZV9yZXBseScgdG8gJ2Rpc3BsYXlfZGF0YScgaW4gb3JkZXIgdG9cbiAgICAvLyByZW5kZXIgb3V0cHV0LlxuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5tb2RlbDtcbiAgICBjb25zdCBjb250ZW50ID0gbXNnLmNvbnRlbnQ7XG4gICAgaWYgKGNvbnRlbnQuc3RhdHVzICE9PSAnb2snKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHBheWxvYWQgPSBjb250ZW50ICYmIGNvbnRlbnQucGF5bG9hZDtcbiAgICBpZiAoIXBheWxvYWQgfHwgIXBheWxvYWQubGVuZ3RoKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IHBhZ2VzID0gcGF5bG9hZC5maWx0ZXIoKGk6IGFueSkgPT4gKGkgYXMgYW55KS5zb3VyY2UgPT09ICdwYWdlJyk7XG4gICAgaWYgKCFwYWdlcy5sZW5ndGgpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgY29uc3QgcGFnZSA9IEpTT04ucGFyc2UoSlNPTi5zdHJpbmdpZnkocGFnZXNbMF0pKTtcbiAgICBjb25zdCBvdXRwdXQ6IG5iZm9ybWF0LklPdXRwdXQgPSB7XG4gICAgICBvdXRwdXRfdHlwZTogJ2Rpc3BsYXlfZGF0YScsXG4gICAgICBkYXRhOiAocGFnZSBhcyBhbnkpLmRhdGEgYXMgbmJmb3JtYXQuSU1pbWVCdW5kbGUsXG4gICAgICBtZXRhZGF0YToge31cbiAgICB9O1xuICAgIG1vZGVsLmFkZChvdXRwdXQpO1xuICB9O1xuXG4gIC8qKlxuICAgKiBXcmFwIGEgb3V0cHV0IHdpZGdldCB3aXRoaW4gYSBvdXRwdXQgcGFuZWxcbiAgICpcbiAgICogQHBhcmFtIG91dHB1dCBPdXRwdXQgd2lkZ2V0IHRvIHdyYXBcbiAgICogQHBhcmFtIGV4ZWN1dGlvbkNvdW50IEV4ZWN1dGlvbiBjb3VudFxuICAgKiBAcmV0dXJucyBUaGUgb3V0cHV0IHBhbmVsXG4gICAqL1xuICBwcml2YXRlIF93cmFwcGVkT3V0cHV0KFxuICAgIG91dHB1dDogV2lkZ2V0LFxuICAgIGV4ZWN1dGlvbkNvdW50OiBudW1iZXIgfCBudWxsID0gbnVsbFxuICApOiBQYW5lbCB7XG4gICAgY29uc3QgcGFuZWwgPSBuZXcgUHJpdmF0ZS5PdXRwdXRQYW5lbCgpO1xuXG4gICAgcGFuZWwuYWRkQ2xhc3MoT1VUUFVUX0FSRUFfSVRFTV9DTEFTUyk7XG5cbiAgICBjb25zdCBwcm9tcHQgPSB0aGlzLmNvbnRlbnRGYWN0b3J5LmNyZWF0ZU91dHB1dFByb21wdCgpO1xuICAgIHByb21wdC5leGVjdXRpb25Db3VudCA9IGV4ZWN1dGlvbkNvdW50O1xuICAgIHByb21wdC5hZGRDbGFzcyhPVVRQVVRfQVJFQV9QUk9NUFRfQ0xBU1MpO1xuICAgIHBhbmVsLmFkZFdpZGdldChwcm9tcHQpO1xuXG4gICAgb3V0cHV0LmFkZENsYXNzKE9VVFBVVF9BUkVBX09VVFBVVF9DTEFTUyk7XG4gICAgcGFuZWwuYWRkV2lkZ2V0KG91dHB1dCk7XG4gICAgcmV0dXJuIHBhbmVsO1xuICB9XG5cbiAgcHJpdmF0ZSBfbWluSGVpZ2h0VGltZW91dDogbnVtYmVyIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX2Z1dHVyZTogS2VybmVsLklTaGVsbEZ1dHVyZTxcbiAgICBLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVxdWVzdE1zZyxcbiAgICBLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVwbHlNc2dcbiAgPjtcbiAgcHJpdmF0ZSBfZGlzcGxheUlkTWFwID0gbmV3IE1hcDxzdHJpbmcsIG51bWJlcltdPigpO1xuICBwcml2YXRlIF9vdXRwdXRUcmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8V2lkZ2V0Pih7XG4gICAgbmFtZXNwYWNlOiBVVUlELnV1aWQ0KClcbiAgfSk7XG5cbiAgLyoqXG4gICAqIFRoZSBtYXhpbXVtIG91dHB1dHMgdG8gc2hvdyBpbiB0aGUgdHJpbW1lZFxuICAgKiBvdXRwdXQgYXJlYS5cbiAgICovXG4gIHByaXZhdGUgX21heE51bWJlck91dHB1dHM6IG51bWJlcjtcbiAgcHJpdmF0ZSBfdHJhbnNsYXRvcjogSVRyYW5zbGF0b3I7XG59XG5cbmV4cG9ydCBjbGFzcyBTaW1wbGlmaWVkT3V0cHV0QXJlYSBleHRlbmRzIE91dHB1dEFyZWEge1xuICAvKipcbiAgICogSGFuZGxlIGFuIGlucHV0IHJlcXVlc3QgZnJvbSBhIGtlcm5lbCBieSBkb2luZyBub3RoaW5nLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uSW5wdXRSZXF1ZXN0KFxuICAgIG1zZzogS2VybmVsTWVzc2FnZS5JSW5wdXRSZXF1ZXN0TXNnLFxuICAgIGZ1dHVyZTogS2VybmVsLklTaGVsbEZ1dHVyZVxuICApOiB2b2lkIHtcbiAgICByZXR1cm47XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGFuIG91dHB1dCBpdGVtIHdpdGhvdXQgYSBwcm9tcHQsIGp1c3QgdGhlIG91dHB1dCB3aWRnZXRzXG4gICAqL1xuICBwcm90ZWN0ZWQgY3JlYXRlT3V0cHV0SXRlbShtb2RlbDogSU91dHB1dE1vZGVsKTogV2lkZ2V0IHwgbnVsbCB7XG4gICAgY29uc3Qgb3V0cHV0ID0gdGhpcy5jcmVhdGVSZW5kZXJlZE1pbWV0eXBlKG1vZGVsKTtcbiAgICBpZiAob3V0cHV0KSB7XG4gICAgICBvdXRwdXQuYWRkQ2xhc3MoT1VUUFVUX0FSRUFfT1VUUFVUX0NMQVNTKTtcbiAgICB9XG4gICAgcmV0dXJuIG91dHB1dDtcbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBPdXRwdXRBcmVhIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgT3V0cHV0QXJlYSB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB0byBjcmVhdGUgYW4gYE91dHB1dEFyZWFgLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIG1vZGVsIHVzZWQgYnkgdGhlIHdpZGdldC5cbiAgICAgKi9cbiAgICBtb2RlbDogSU91dHB1dEFyZWFNb2RlbDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBjb250ZW50IGZhY3RvcnkgdXNlZCBieSB0aGUgd2lkZ2V0IHRvIGNyZWF0ZSBjaGlsZHJlbi5cbiAgICAgKi9cbiAgICBjb250ZW50RmFjdG9yeT86IElDb250ZW50RmFjdG9yeTtcblxuICAgIC8qKlxuICAgICAqIFRoZSByZW5kZXJtaW1lIGluc3RhbmNlIHVzZWQgYnkgdGhlIHdpZGdldC5cbiAgICAgKi9cbiAgICByZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5O1xuXG4gICAgLyoqXG4gICAgICogVGhlIG1heGltdW0gbnVtYmVyIG9mIG91dHB1dCBpdGVtcyB0byBkaXNwbGF5IG9uIHRvcCBhbmQgYm90dG9tIG9mIGNlbGwgb3V0cHV0LlxuICAgICAqL1xuICAgIG1heE51bWJlck91dHB1dHM/OiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBUcmFuc2xhdG9yXG4gICAgICovXG4gICAgcmVhZG9ubHkgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuICB9XG5cbiAgLyoqXG4gICAqIEV4ZWN1dGUgY29kZSBvbiBhbiBvdXRwdXQgYXJlYS5cbiAgICovXG4gIGV4cG9ydCBhc3luYyBmdW5jdGlvbiBleGVjdXRlKFxuICAgIGNvZGU6IHN0cmluZyxcbiAgICBvdXRwdXQ6IE91dHB1dEFyZWEsXG4gICAgc2Vzc2lvbkNvbnRleHQ6IElTZXNzaW9uQ29udGV4dCxcbiAgICBtZXRhZGF0YT86IEpTT05PYmplY3RcbiAgKTogUHJvbWlzZTxLZXJuZWxNZXNzYWdlLklFeGVjdXRlUmVwbHlNc2cgfCB1bmRlZmluZWQ+IHtcbiAgICAvLyBPdmVycmlkZSB0aGUgZGVmYXVsdCBmb3IgYHN0b3Bfb25fZXJyb3JgLlxuICAgIGxldCBzdG9wT25FcnJvciA9IHRydWU7XG4gICAgaWYgKFxuICAgICAgbWV0YWRhdGEgJiZcbiAgICAgIEFycmF5LmlzQXJyYXkobWV0YWRhdGEudGFncykgJiZcbiAgICAgIG1ldGFkYXRhLnRhZ3MuaW5kZXhPZigncmFpc2VzLWV4Y2VwdGlvbicpICE9PSAtMVxuICAgICkge1xuICAgICAgc3RvcE9uRXJyb3IgPSBmYWxzZTtcbiAgICB9XG4gICAgY29uc3QgY29udGVudDogS2VybmVsTWVzc2FnZS5JRXhlY3V0ZVJlcXVlc3RNc2dbJ2NvbnRlbnQnXSA9IHtcbiAgICAgIGNvZGUsXG4gICAgICBzdG9wX29uX2Vycm9yOiBzdG9wT25FcnJvclxuICAgIH07XG5cbiAgICBjb25zdCBrZXJuZWwgPSBzZXNzaW9uQ29udGV4dC5zZXNzaW9uPy5rZXJuZWw7XG4gICAgaWYgKCFrZXJuZWwpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcignU2Vzc2lvbiBoYXMgbm8ga2VybmVsLicpO1xuICAgIH1cbiAgICBjb25zdCBmdXR1cmUgPSBrZXJuZWwucmVxdWVzdEV4ZWN1dGUoY29udGVudCwgZmFsc2UsIG1ldGFkYXRhKTtcbiAgICBvdXRwdXQuZnV0dXJlID0gZnV0dXJlO1xuICAgIHJldHVybiBmdXR1cmUuZG9uZTtcbiAgfVxuXG4gIGV4cG9ydCBmdW5jdGlvbiBpc0lzb2xhdGVkKFxuICAgIG1pbWVUeXBlOiBzdHJpbmcsXG4gICAgbWV0YWRhdGE6IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3RcbiAgKTogYm9vbGVhbiB7XG4gICAgY29uc3QgbWltZU1kID0gbWV0YWRhdGFbbWltZVR5cGVdIGFzIFJlYWRvbmx5SlNPTk9iamVjdCB8IHVuZGVmaW5lZDtcbiAgICAvLyBtaW1lLXNwZWNpZmljIGhpZ2hlciBwcmlvcml0eVxuICAgIGlmIChtaW1lTWQgJiYgbWltZU1kWydpc29sYXRlZCddICE9PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybiAhIW1pbWVNZFsnaXNvbGF0ZWQnXTtcbiAgICB9IGVsc2Uge1xuICAgICAgLy8gZmFsbGJhY2sgb24gZ2xvYmFsXG4gICAgICByZXR1cm4gISFtZXRhZGF0YVsnaXNvbGF0ZWQnXTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQW4gb3V0cHV0IGFyZWEgd2lkZ2V0IGNvbnRlbnQgZmFjdG9yeS5cbiAgICpcbiAgICogVGhlIGNvbnRlbnQgZmFjdG9yeSBpcyB1c2VkIHRvIGNyZWF0ZSBjaGlsZHJlbiBpbiBhIHdheVxuICAgKiB0aGF0IGNhbiBiZSBjdXN0b21pemVkLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29udGVudEZhY3Rvcnkge1xuICAgIC8qKlxuICAgICAqIENyZWF0ZSBhbiBvdXRwdXQgcHJvbXB0LlxuICAgICAqL1xuICAgIGNyZWF0ZU91dHB1dFByb21wdCgpOiBJT3V0cHV0UHJvbXB0O1xuXG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGFuIHN0ZGluIHdpZGdldC5cbiAgICAgKi9cbiAgICBjcmVhdGVTdGRpbihvcHRpb25zOiBTdGRpbi5JT3B0aW9ucyk6IElTdGRpbjtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBpbXBsZW1lbnRhdGlvbiBvZiBgSUNvbnRlbnRGYWN0b3J5YC5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBDb250ZW50RmFjdG9yeSBpbXBsZW1lbnRzIElDb250ZW50RmFjdG9yeSB7XG4gICAgLyoqXG4gICAgICogQ3JlYXRlIHRoZSBvdXRwdXQgcHJvbXB0IGZvciB0aGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIGNyZWF0ZU91dHB1dFByb21wdCgpOiBJT3V0cHV0UHJvbXB0IHtcbiAgICAgIHJldHVybiBuZXcgT3V0cHV0UHJvbXB0KCk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGFuIHN0ZGluIHdpZGdldC5cbiAgICAgKi9cbiAgICBjcmVhdGVTdGRpbihvcHRpb25zOiBTdGRpbi5JT3B0aW9ucyk6IElTdGRpbiB7XG4gICAgICByZXR1cm4gbmV3IFN0ZGluKG9wdGlvbnMpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBgQ29udGVudEZhY3RvcnlgIGluc3RhbmNlLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRlZmF1bHRDb250ZW50RmFjdG9yeSA9IG5ldyBDb250ZW50RmFjdG9yeSgpO1xufVxuXG4vKiogKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKlxuICogT3V0cHV0UHJvbXB0XG4gKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqL1xuXG4vKipcbiAqIFRoZSBpbnRlcmZhY2UgZm9yIGFuIG91dHB1dCBwcm9tcHQuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSU91dHB1dFByb21wdCBleHRlbmRzIFdpZGdldCB7XG4gIC8qKlxuICAgKiBUaGUgZXhlY3V0aW9uIGNvdW50IGZvciB0aGUgcHJvbXB0LlxuICAgKi9cbiAgZXhlY3V0aW9uQ291bnQ6IG5iZm9ybWF0LkV4ZWN1dGlvbkNvdW50O1xufVxuXG4vKipcbiAqIFRoZSBkZWZhdWx0IG91dHB1dCBwcm9tcHQgaW1wbGVtZW50YXRpb25cbiAqL1xuZXhwb3J0IGNsYXNzIE91dHB1dFByb21wdCBleHRlbmRzIFdpZGdldCBpbXBsZW1lbnRzIElPdXRwdXRQcm9tcHQge1xuICAvKlxuICAgKiBDcmVhdGUgYW4gb3V0cHV0IHByb21wdCB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3RvcigpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuYWRkQ2xhc3MoT1VUUFVUX1BST01QVF9DTEFTUyk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGV4ZWN1dGlvbiBjb3VudCBmb3IgdGhlIHByb21wdC5cbiAgICovXG4gIGdldCBleGVjdXRpb25Db3VudCgpOiBuYmZvcm1hdC5FeGVjdXRpb25Db3VudCB7XG4gICAgcmV0dXJuIHRoaXMuX2V4ZWN1dGlvbkNvdW50O1xuICB9XG4gIHNldCBleGVjdXRpb25Db3VudCh2YWx1ZTogbmJmb3JtYXQuRXhlY3V0aW9uQ291bnQpIHtcbiAgICB0aGlzLl9leGVjdXRpb25Db3VudCA9IHZhbHVlO1xuICAgIGlmICh2YWx1ZSA9PT0gbnVsbCkge1xuICAgICAgdGhpcy5ub2RlLnRleHRDb250ZW50ID0gJ+KGqiBPdXRwdXQnO1xuICAgIH0gZWxzZSB7XG4gICAgICAvLyB0aGlzLm5vZGUudGV4dENvbnRlbnQgPSBgWyR7dmFsdWV9XTpgO1xuICAgICAgdGhpcy5ub2RlLnRleHRDb250ZW50ID0gJ+KGqiBPdXRwdXQnO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX2V4ZWN1dGlvbkNvdW50OiBuYmZvcm1hdC5FeGVjdXRpb25Db3VudCA9IG51bGw7XG59XG5cbi8qKiAqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqXG4gKiBTdGRpblxuICoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi9cblxuLyoqXG4gKiBUaGUgc3RkaW4gaW50ZXJmYWNlXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVN0ZGluIGV4dGVuZHMgV2lkZ2V0IHtcbiAgLyoqXG4gICAqIFRoZSBzdGRpbiB2YWx1ZS5cbiAgICovXG4gIHJlYWRvbmx5IHZhbHVlOiBQcm9taXNlPHN0cmluZz47XG59XG5cbi8qKlxuICogVGhlIGRlZmF1bHQgc3RkaW4gd2lkZ2V0LlxuICovXG5leHBvcnQgY2xhc3MgU3RkaW4gZXh0ZW5kcyBXaWRnZXQgaW1wbGVtZW50cyBJU3RkaW4ge1xuICBwcml2YXRlIHN0YXRpYyBfaGlzdG9yeTogc3RyaW5nW10gPSBbXTtcblxuICBwcml2YXRlIHN0YXRpYyBfaGlzdG9yeUF0KGl4OiBudW1iZXIpOiBzdHJpbmcgfCB1bmRlZmluZWQge1xuICAgIGNvbnN0IGxlbiA9IFN0ZGluLl9oaXN0b3J5Lmxlbmd0aDtcbiAgICAvLyBpbnRlcnByZXQgbmVnYXRpdmUgaXggZXhhY3RseSBsaWtlIEFycmF5LmF0XG4gICAgaXggPSBpeCA8IDAgPyBsZW4gKyBpeCA6IGl4O1xuXG4gICAgaWYgKGl4IDwgbGVuKSB7XG4gICAgICByZXR1cm4gU3RkaW4uX2hpc3RvcnlbaXhdO1xuICAgIH1cbiAgICAvLyByZXR1cm4gdW5kZWZpbmVkIGlmIGl4IGlzIG91dCBvZiBib3VuZHNcbiAgfVxuXG4gIHByaXZhdGUgc3RhdGljIF9oaXN0b3J5UHVzaChsaW5lOiBzdHJpbmcpOiB2b2lkIHtcbiAgICBTdGRpbi5faGlzdG9yeS5wdXNoKGxpbmUpO1xuICAgIGlmIChTdGRpbi5faGlzdG9yeS5sZW5ndGggPiAxMDAwKSB7XG4gICAgICAvLyB0cnVuY2F0ZSBsaW5lIGhpc3RvcnkgaWYgaXQncyB0b28gbG9uZ1xuICAgICAgU3RkaW4uX2hpc3Rvcnkuc2hpZnQoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGlucHV0IHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IFN0ZGluLklPcHRpb25zKSB7XG4gICAgc3VwZXIoe1xuICAgICAgbm9kZTogUHJpdmF0ZS5jcmVhdGVJbnB1dFdpZGdldE5vZGUob3B0aW9ucy5wcm9tcHQsIG9wdGlvbnMucGFzc3dvcmQpXG4gICAgfSk7XG4gICAgdGhpcy5hZGRDbGFzcyhTVERJTl9DTEFTUyk7XG4gICAgdGhpcy5faGlzdG9yeUluZGV4ID0gMDtcbiAgICB0aGlzLl9pbnB1dCA9IHRoaXMubm9kZS5nZXRFbGVtZW50c0J5VGFnTmFtZSgnaW5wdXQnKVswXTtcbiAgICB0aGlzLl9pbnB1dC5mb2N1cygpO1xuICAgIHRoaXMuX3RyYW5zID0gKG9wdGlvbnMudHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvcikubG9hZCgnanVweXRlcmxhYicpO1xuICAgIC8vIG1ha2UgdXNlcnMgYXdhcmUgb2YgdGhlIGxpbmUgaGlzdG9yeSBmZWF0dXJlXG4gICAgdGhpcy5faW5wdXQucGxhY2Vob2xkZXIgPSB0aGlzLl90cmFucy5fXygn4oaR4oaTIGZvciBoaXN0b3J5Jyk7XG4gICAgdGhpcy5fZnV0dXJlID0gb3B0aW9ucy5mdXR1cmU7XG4gICAgdGhpcy5fcGFyZW50SGVhZGVyID0gb3B0aW9ucy5wYXJlbnRfaGVhZGVyO1xuICAgIHRoaXMuX3ZhbHVlID0gb3B0aW9ucy5wcm9tcHQgKyAnICc7XG4gICAgdGhpcy5fcGFzc3dvcmQgPSBvcHRpb25zLnBhc3N3b3JkO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSB2YWx1ZSBvZiB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgZ2V0IHZhbHVlKCk6IFByb21pc2U8c3RyaW5nPiB7XG4gICAgcmV0dXJuIHRoaXMuX3Byb21pc2UucHJvbWlzZS50aGVuKCgpID0+IHRoaXMuX3ZhbHVlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtIFRoZSBET00gZXZlbnQgc2VudCB0byB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgbWV0aG9kIGltcGxlbWVudHMgdGhlIERPTSBgRXZlbnRMaXN0ZW5lcmAgaW50ZXJmYWNlIGFuZCBpc1xuICAgKiBjYWxsZWQgaW4gcmVzcG9uc2UgdG8gZXZlbnRzIG9uIHRoZSBkb2NrIHBhbmVsJ3Mgbm9kZS4gSXQgc2hvdWxkXG4gICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgKi9cbiAgaGFuZGxlRXZlbnQoZXZlbnQ6IEtleWJvYXJkRXZlbnQpOiB2b2lkIHtcbiAgICBjb25zdCBpbnB1dCA9IHRoaXMuX2lucHV0O1xuICAgIGlmIChldmVudC50eXBlID09PSAna2V5ZG93bicpIHtcbiAgICAgIGlmIChldmVudC5rZXkgPT09ICdBcnJvd1VwJykge1xuICAgICAgICBjb25zdCBoaXN0b3J5TGluZSA9IFN0ZGluLl9oaXN0b3J5QXQodGhpcy5faGlzdG9yeUluZGV4IC0gMSk7XG4gICAgICAgIGlmIChoaXN0b3J5TGluZSkge1xuICAgICAgICAgIGlmICh0aGlzLl9oaXN0b3J5SW5kZXggPT09IDApIHtcbiAgICAgICAgICAgIHRoaXMuX3ZhbHVlQ2FjaGUgPSBpbnB1dC52YWx1ZTtcbiAgICAgICAgICB9XG4gICAgICAgICAgaW5wdXQudmFsdWUgPSBoaXN0b3J5TGluZTtcbiAgICAgICAgICAtLXRoaXMuX2hpc3RvcnlJbmRleDtcbiAgICAgICAgfVxuICAgICAgfSBlbHNlIGlmIChldmVudC5rZXkgPT09ICdBcnJvd0Rvd24nKSB7XG4gICAgICAgIGlmICh0aGlzLl9oaXN0b3J5SW5kZXggPT09IDApIHtcbiAgICAgICAgICAvLyBkbyBub3RoaW5nXG4gICAgICAgIH0gZWxzZSBpZiAodGhpcy5faGlzdG9yeUluZGV4ID09PSAtMSkge1xuICAgICAgICAgIGlucHV0LnZhbHVlID0gdGhpcy5fdmFsdWVDYWNoZTtcbiAgICAgICAgICArK3RoaXMuX2hpc3RvcnlJbmRleDtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBjb25zdCBoaXN0b3J5TGluZSA9IFN0ZGluLl9oaXN0b3J5QXQodGhpcy5faGlzdG9yeUluZGV4ICsgMSk7XG4gICAgICAgICAgaWYgKGhpc3RvcnlMaW5lKSB7XG4gICAgICAgICAgICBpbnB1dC52YWx1ZSA9IGhpc3RvcnlMaW5lO1xuICAgICAgICAgICAgKyt0aGlzLl9oaXN0b3J5SW5kZXg7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9IGVsc2UgaWYgKGV2ZW50LmtleSA9PT0gJ0VudGVyJykge1xuICAgICAgICB0aGlzLl9mdXR1cmUuc2VuZElucHV0UmVwbHkoXG4gICAgICAgICAge1xuICAgICAgICAgICAgc3RhdHVzOiAnb2snLFxuICAgICAgICAgICAgdmFsdWU6IGlucHV0LnZhbHVlXG4gICAgICAgICAgfSxcbiAgICAgICAgICB0aGlzLl9wYXJlbnRIZWFkZXJcbiAgICAgICAgKTtcbiAgICAgICAgaWYgKHRoaXMuX3Bhc3N3b3JkKSB7XG4gICAgICAgICAgdGhpcy5fdmFsdWUgKz0gJ8K3wrfCt8K3wrfCt8K3wrcnO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgIHRoaXMuX3ZhbHVlICs9IGlucHV0LnZhbHVlO1xuICAgICAgICAgIFN0ZGluLl9oaXN0b3J5UHVzaChpbnB1dC52YWx1ZSk7XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy5fcHJvbWlzZS5yZXNvbHZlKHZvaWQgMCk7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYWZ0ZXItYXR0YWNoYCBtZXNzYWdlcyBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25BZnRlckF0dGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICB0aGlzLl9pbnB1dC5hZGRFdmVudExpc3RlbmVyKCdrZXlkb3duJywgdGhpcyk7XG4gICAgdGhpcy51cGRhdGUoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYHVwZGF0ZS1yZXF1ZXN0YCBtZXNzYWdlcyBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX2lucHV0LmZvY3VzKCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBiZWZvcmUtZGV0YWNoYCBtZXNzYWdlcyBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25CZWZvcmVEZXRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgdGhpcy5faW5wdXQucmVtb3ZlRXZlbnRMaXN0ZW5lcigna2V5ZG93bicsIHRoaXMpO1xuICB9XG5cbiAgcHJpdmF0ZSBfaGlzdG9yeUluZGV4OiBudW1iZXI7XG4gIHByaXZhdGUgX3BhcmVudEhlYWRlcjogS2VybmVsTWVzc2FnZS5JSW5wdXRSZXBseU1zZ1sncGFyZW50X2hlYWRlciddO1xuICBwcml2YXRlIF9mdXR1cmU6IEtlcm5lbC5JU2hlbGxGdXR1cmU7XG4gIHByaXZhdGUgX2lucHV0OiBIVE1MSW5wdXRFbGVtZW50O1xuICBwcml2YXRlIF92YWx1ZTogc3RyaW5nO1xuICBwcml2YXRlIF92YWx1ZUNhY2hlOiBzdHJpbmc7XG4gIHByaXZhdGUgX3Byb21pc2UgPSBuZXcgUHJvbWlzZURlbGVnYXRlPHZvaWQ+KCk7XG4gIHByaXZhdGUgX3Bhc3N3b3JkOiBib29sZWFuO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG59XG5cbmV4cG9ydCBuYW1lc3BhY2UgU3RkaW4ge1xuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdG8gY3JlYXRlIGEgc3RkaW4gd2lkZ2V0LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHByb21wdCB0ZXh0LlxuICAgICAqL1xuICAgIHByb21wdDogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgaW5wdXQgaXMgYSBwYXNzd29yZC5cbiAgICAgKi9cbiAgICBwYXNzd29yZDogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBrZXJuZWwgZnV0dXJlIGFzc29jaWF0ZWQgd2l0aCB0aGUgcmVxdWVzdC5cbiAgICAgKi9cbiAgICBmdXR1cmU6IEtlcm5lbC5JU2hlbGxGdXR1cmU7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgaGVhZGVyIG9mIHRoZSBpbnB1dF9yZXF1ZXN0IG1lc3NhZ2UuXG4gICAgICovXG4gICAgcGFyZW50X2hlYWRlcjogS2VybmVsTWVzc2FnZS5JSW5wdXRSZXBseU1zZ1sncGFyZW50X2hlYWRlciddO1xuXG4gICAgLyoqXG4gICAgICogVHJhbnNsYXRvclxuICAgICAqL1xuICAgIHJlYWRvbmx5IHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxufVxuXG4vKiogKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKlxuICogUHJpdmF0ZSBuYW1lc3BhY2VcbiAqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiovXG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQ3JlYXRlIHRoZSBub2RlIGZvciBhbiBJbnB1dFdpZGdldC5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVJbnB1dFdpZGdldE5vZGUoXG4gICAgcHJvbXB0OiBzdHJpbmcsXG4gICAgcGFzc3dvcmQ6IGJvb2xlYW5cbiAgKTogSFRNTEVsZW1lbnQge1xuICAgIGNvbnN0IG5vZGUgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgICBjb25zdCBwcm9tcHROb2RlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgncHJlJyk7XG4gICAgcHJvbXB0Tm9kZS5jbGFzc05hbWUgPSBTVERJTl9QUk9NUFRfQ0xBU1M7XG4gICAgcHJvbXB0Tm9kZS50ZXh0Q29udGVudCA9IHByb21wdDtcbiAgICBjb25zdCBpbnB1dCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2lucHV0Jyk7XG4gICAgaW5wdXQuY2xhc3NOYW1lID0gU1RESU5fSU5QVVRfQ0xBU1M7XG4gICAgaWYgKHBhc3N3b3JkKSB7XG4gICAgICBpbnB1dC50eXBlID0gJ3Bhc3N3b3JkJztcbiAgICB9XG4gICAgbm9kZS5hcHBlbmRDaGlsZChwcm9tcHROb2RlKTtcbiAgICBwcm9tcHROb2RlLmFwcGVuZENoaWxkKGlucHV0KTtcbiAgICByZXR1cm4gbm9kZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHJlbmRlcmVyIGZvciBJRnJhbWUgZGF0YS5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBJc29sYXRlZFJlbmRlcmVyXG4gICAgZXh0ZW5kcyBXaWRnZXRcbiAgICBpbXBsZW1lbnRzIElSZW5kZXJNaW1lLklSZW5kZXJlclxuICB7XG4gICAgLyoqXG4gICAgICogQ3JlYXRlIGFuIGlzb2xhdGVkIHJlbmRlcmVyLlxuICAgICAqL1xuICAgIGNvbnN0cnVjdG9yKHdyYXBwZWQ6IElSZW5kZXJNaW1lLklSZW5kZXJlcikge1xuICAgICAgc3VwZXIoeyBub2RlOiBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdpZnJhbWUnKSB9KTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLW1vZC1pc29sYXRlZCcpO1xuXG4gICAgICB0aGlzLl93cmFwcGVkID0gd3JhcHBlZDtcblxuICAgICAgLy8gT25jZSB0aGUgaWZyYW1lIGlzIGxvYWRlZCwgdGhlIHN1YmFyZWEgaXMgZHluYW1pY2FsbHkgaW5zZXJ0ZWRcbiAgICAgIGNvbnN0IGlmcmFtZSA9IHRoaXMubm9kZSBhcyBIVE1MSUZyYW1lRWxlbWVudCAmIHtcbiAgICAgICAgaGVpZ2h0Q2hhbmdlT2JzZXJ2ZXI6IFJlc2l6ZU9ic2VydmVyO1xuICAgICAgfTtcblxuICAgICAgaWZyYW1lLmZyYW1lQm9yZGVyID0gJzAnO1xuICAgICAgaWZyYW1lLnNjcm9sbGluZyA9ICdhdXRvJztcblxuICAgICAgaWZyYW1lLmFkZEV2ZW50TGlzdGVuZXIoJ2xvYWQnLCAoKSA9PiB7XG4gICAgICAgIC8vIFdvcmthcm91bmQgbmVlZGVkIGJ5IEZpcmVmb3gsIHRvIHByb3Blcmx5IHJlbmRlciBzdmcgaW5zaWRlXG4gICAgICAgIC8vIGlmcmFtZXMsIHNlZSBodHRwczovL3N0YWNrb3ZlcmZsb3cuY29tL3F1ZXN0aW9ucy8xMDE3NzE5MC9cbiAgICAgICAgLy8gc3ZnLWR5bmFtaWNhbGx5LWFkZGVkLXRvLWlmcmFtZS1kb2VzLW5vdC1yZW5kZXItY29ycmVjdGx5XG4gICAgICAgIGlmcmFtZS5jb250ZW50RG9jdW1lbnQhLm9wZW4oKTtcblxuICAgICAgICAvLyBJbnNlcnQgdGhlIHN1YmFyZWEgaW50byB0aGUgaWZyYW1lXG4gICAgICAgIC8vIFdlIG11c3QgZGlyZWN0bHkgd3JpdGUgdGhlIGh0bWwuIEF0IHRoaXMgcG9pbnQsIHN1YmFyZWEgZG9lc24ndFxuICAgICAgICAvLyBjb250YWluIGFueSB1c2VyIGNvbnRlbnQuXG4gICAgICAgIGlmcmFtZS5jb250ZW50RG9jdW1lbnQhLndyaXRlKHRoaXMuX3dyYXBwZWQubm9kZS5pbm5lckhUTUwpO1xuXG4gICAgICAgIGlmcmFtZS5jb250ZW50RG9jdW1lbnQhLmNsb3NlKCk7XG5cbiAgICAgICAgY29uc3QgYm9keSA9IGlmcmFtZS5jb250ZW50RG9jdW1lbnQhLmJvZHk7XG5cbiAgICAgICAgLy8gQWRqdXN0IHRoZSBpZnJhbWUgaGVpZ2h0IGF1dG9tYXRpY2FsbHlcbiAgICAgICAgaWZyYW1lLnN0eWxlLmhlaWdodCA9IGAke2JvZHkuc2Nyb2xsSGVpZ2h0fXB4YDtcbiAgICAgICAgaWZyYW1lLmhlaWdodENoYW5nZU9ic2VydmVyID0gbmV3IFJlc2l6ZU9ic2VydmVyKCgpID0+IHtcbiAgICAgICAgICBpZnJhbWUuc3R5bGUuaGVpZ2h0ID0gYCR7Ym9keS5zY3JvbGxIZWlnaHR9cHhgO1xuICAgICAgICB9KTtcbiAgICAgICAgaWZyYW1lLmhlaWdodENoYW5nZU9ic2VydmVyLm9ic2VydmUoYm9keSk7XG4gICAgICB9KTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW5kZXIgYSBtaW1lIG1vZGVsLlxuICAgICAqXG4gICAgICogQHBhcmFtIG1vZGVsIC0gVGhlIG1pbWUgbW9kZWwgdG8gcmVuZGVyLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBwcm9taXNlIHdoaWNoIHJlc29sdmVzIHdoZW4gcmVuZGVyaW5nIGlzIGNvbXBsZXRlLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoaXMgbWV0aG9kIG1heSBiZSBjYWxsZWQgbXVsdGlwbGUgdGltZXMgZHVyaW5nIHRoZSBsaWZldGltZVxuICAgICAqIG9mIHRoZSB3aWRnZXQgdG8gdXBkYXRlIGl0IGlmIGFuZCB3aGVuIG5ldyBkYXRhIGlzIGF2YWlsYWJsZS5cbiAgICAgKi9cbiAgICByZW5kZXJNb2RlbChtb2RlbDogSVJlbmRlck1pbWUuSU1pbWVNb2RlbCk6IFByb21pc2U8dm9pZD4ge1xuICAgICAgcmV0dXJuIHRoaXMuX3dyYXBwZWQucmVuZGVyTW9kZWwobW9kZWwpO1xuICAgIH1cblxuICAgIHByaXZhdGUgX3dyYXBwZWQ6IElSZW5kZXJNaW1lLklSZW5kZXJlcjtcbiAgfVxuXG4gIGV4cG9ydCBjb25zdCBjdXJyZW50UHJlZmVycmVkTWltZXR5cGUgPSBuZXcgQXR0YWNoZWRQcm9wZXJ0eTxcbiAgICBJUmVuZGVyTWltZS5JUmVuZGVyZXIsXG4gICAgc3RyaW5nXG4gID4oe1xuICAgIG5hbWU6ICdwcmVmZXJyZWRNaW1ldHlwZScsXG4gICAgY3JlYXRlOiBvd25lciA9PiAnJ1xuICB9KTtcblxuICAvKipcbiAgICogQSBgUGFuZWxgIHRoYXQncyBmb2N1c2VkIGJ5IGEgYGNvbnRleHRtZW51YCBldmVudC5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBPdXRwdXRQYW5lbCBleHRlbmRzIFBhbmVsIHtcbiAgICAvKipcbiAgICAgKiBDb25zdHJ1Y3QgYSBuZXcgYE91dHB1dFBhbmVsYCB3aWRnZXQuXG4gICAgICovXG4gICAgY29uc3RydWN0b3Iob3B0aW9ucz86IFBhbmVsLklPcHRpb25zKSB7XG4gICAgICBzdXBlcihvcHRpb25zKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIGNhbGxiYWNrIHRoYXQgZm9jdXNlcyBvbiB0aGUgd2lkZ2V0LlxuICAgICAqL1xuICAgIHByaXZhdGUgX29uQ29udGV4dChfOiBFdmVudCk6IHZvaWQge1xuICAgICAgdGhpcy5ub2RlLmZvY3VzKCk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogSGFuZGxlIGBhZnRlci1hdHRhY2hgIG1lc3NhZ2VzIHNlbnQgdG8gdGhlIHdpZGdldC5cbiAgICAgKi9cbiAgICBwcm90ZWN0ZWQgb25BZnRlckF0dGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICAgIHN1cGVyLm9uQWZ0ZXJBdHRhY2gobXNnKTtcbiAgICAgIHRoaXMubm9kZS5hZGRFdmVudExpc3RlbmVyKCdjb250ZXh0bWVudScsIHRoaXMuX29uQ29udGV4dC5iaW5kKHRoaXMpKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBIYW5kbGUgYGJlZm9yZS1kZXRhY2hgIG1lc3NhZ2VzIHNlbnQgdG8gdGhlIHdpZGdldC5cbiAgICAgKi9cbiAgICBwcm90ZWN0ZWQgb25CZWZvcmVEZXRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgICBzdXBlci5vbkFmdGVyRGV0YWNoKG1zZyk7XG4gICAgICB0aGlzLm5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignY29udGV4dG1lbnUnLCB0aGlzLl9vbkNvbnRleHQuYmluZCh0aGlzKSk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFRyaW1tZWQgb3V0cHV0cyBpbmZvcm1hdGlvbiB3aWRnZXQuXG4gICAqL1xuICBleHBvcnQgY2xhc3MgVHJpbW1lZE91dHB1dHMgZXh0ZW5kcyBXaWRnZXQge1xuICAgIC8qKlxuICAgICAqIFdpZGdldCBjb25zdHJ1Y3RvclxuICAgICAqXG4gICAgICogIyMjIE5vdGVzXG4gICAgICogVGhlIHdpZGdldCB3aWxsIGJlIGRpc3Bvc2VkIG9uIGNsaWNrIGFmdGVyIGNhbGxpbmcgdGhlIGNhbGxiYWNrLlxuICAgICAqXG4gICAgICogQHBhcmFtIG1heE51bWJlck91dHB1dHMgTWF4aW1hbCBudW1iZXIgb2Ygb3V0cHV0cyB0byBkaXNwbGF5XG4gICAgICogQHBhcmFtIF9vbkNsaWNrIENhbGxiYWNrIG9uIGNsaWNrIGV2ZW50IG9uIHRoZSB3aWRnZXRcbiAgICAgKi9cbiAgICBjb25zdHJ1Y3RvcihcbiAgICAgIG1heE51bWJlck91dHB1dHM6IG51bWJlcixcbiAgICAgIG9uQ2xpY2s6IChldmVudDogTW91c2VFdmVudCkgPT4gdm9pZFxuICAgICkge1xuICAgICAgY29uc3Qgbm9kZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2RpdicpO1xuICAgICAgY29uc3QgdGl0bGUgPSBgVGhlIGZpcnN0ICR7bWF4TnVtYmVyT3V0cHV0c30gYXJlIGRpc3BsYXllZGA7XG4gICAgICBjb25zdCBtc2cgPSAnU2hvdyBtb3JlIG91dHB1dHMnO1xuICAgICAgbm9kZS5pbnNlcnRBZGphY2VudEhUTUwoXG4gICAgICAgICdhZnRlcmJlZ2luJyxcbiAgICAgICAgYDxhIHRpdGxlPSR7dGl0bGV9PlxuICAgICAgICAgIDxwcmU+JHttc2d9PC9wcmU+XG4gICAgICAgIDwvYT5gXG4gICAgICApO1xuICAgICAgc3VwZXIoe1xuICAgICAgICBub2RlXG4gICAgICB9KTtcbiAgICAgIHRoaXMuX29uQ2xpY2sgPSBvbkNsaWNrO1xuICAgICAgdGhpcy5hZGRDbGFzcygnanAtVHJpbW1lZE91dHB1dHMnKTtcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLVJlbmRlcmVkSFRNTENvbW1vbicpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIEhhbmRsZSB0aGUgRE9NIGV2ZW50cyBmb3Igd2lkZ2V0LlxuICAgICAqXG4gICAgICogQHBhcmFtIGV2ZW50IC0gVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhpcyBtZXRob2QgaW1wbGVtZW50cyB0aGUgRE9NIGBFdmVudExpc3RlbmVyYCBpbnRlcmZhY2UgYW5kIGlzXG4gICAgICogY2FsbGVkIGluIHJlc3BvbnNlIHRvIGV2ZW50cyBvbiB0aGUgd2lkZ2V0J3MgRE9NIG5vZGUuIEl0IHNob3VsZFxuICAgICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgICAqL1xuICAgIGhhbmRsZUV2ZW50KGV2ZW50OiBFdmVudCk6IHZvaWQge1xuICAgICAgaWYgKGV2ZW50LnR5cGUgPT09ICdjbGljaycpIHtcbiAgICAgICAgdGhpcy5fb25DbGljayhldmVudCBhcyBNb3VzZUV2ZW50KTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBIYW5kbGUgYGFmdGVyLWF0dGFjaGAgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAgICovXG4gICAgcHJvdGVjdGVkIG9uQWZ0ZXJBdHRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgICBzdXBlci5vbkFmdGVyQXR0YWNoKG1zZyk7XG4gICAgICB0aGlzLm5vZGUuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIG1lc3NhZ2UgaGFuZGxlciBpbnZva2VkIG9uIGEgYCdiZWZvcmUtZGV0YWNoJ2BcbiAgICAgKiBtZXNzYWdlXG4gICAgICovXG4gICAgcHJvdGVjdGVkIG9uQmVmb3JlRGV0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgICAgc3VwZXIub25CZWZvcmVEZXRhY2gobXNnKTtcbiAgICAgIHRoaXMubm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdjbGljaycsIHRoaXMpO1xuICAgIH1cblxuICAgIHByaXZhdGUgX29uQ2xpY2s6IChldmVudDogTW91c2VFdmVudCkgPT4gdm9pZDtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9