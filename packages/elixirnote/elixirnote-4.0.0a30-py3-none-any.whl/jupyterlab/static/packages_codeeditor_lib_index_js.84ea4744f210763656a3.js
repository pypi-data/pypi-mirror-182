"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_codeeditor_lib_index_js"],{

/***/ "../../packages/codeeditor/lib/editor.js":
/*!***********************************************!*\
  !*** ../../packages/codeeditor/lib/editor.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeEditor": () => (/* binding */ CodeEditor)
/* harmony export */ });
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/observables */ "webpack/sharing/consume/default/@jupyterlab/observables/@jupyterlab/observables");
/* harmony import */ var _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/shared-models */ "webpack/sharing/consume/default/@jupyterlab/shared-models/@jupyterlab/shared-models");
/* harmony import */ var _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



const globalModelDBMutex = _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_1__.createMutex();
/**
 * A namespace for code editors.
 *
 * #### Notes
 * - A code editor is a set of common assumptions which hold for all concrete editors.
 * - Changes in implementations of the code editor should only be caused by changes in concrete editors.
 * - Common JLab services which are based on the code editor should belong to `IEditorServices`.
 */
var CodeEditor;
(function (CodeEditor) {
    /**
     * The default selection style.
     */
    CodeEditor.defaultSelectionStyle = {
        className: '',
        displayName: '',
        color: 'black'
    };
    /**
     * The default implementation of the editor model.
     */
    class Model {
        /**
         * Construct a new Model.
         */
        constructor(options) {
            this._isDisposed = false;
            this._mimeTypeChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
            this._sharedModelSwitched = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
            options = options || {};
            if (options.modelDB) {
                this.modelDB = options.modelDB;
            }
            else {
                this.modelDB = new _jupyterlab_observables__WEBPACK_IMPORTED_MODULE_0__.ModelDB();
            }
            this.sharedModel = _jupyterlab_shared_models__WEBPACK_IMPORTED_MODULE_1__.createStandaloneCell(this.type, options.id);
            this.sharedModel.changed.connect(this._onSharedModelChanged, this);
            const value = this.modelDB.createString('value');
            value.changed.connect(this._onModelDBValueChanged, this);
            value.text = value.text || options.value || '';
            const mimeType = this.modelDB.createValue('mimeType');
            mimeType.changed.connect(this._onModelDBMimeTypeChanged, this);
            mimeType.set(options.mimeType || 'text/plain');
            this.modelDB.createMap('selections');
        }
        /**
         * When we initialize a cell model, we create a standalone model that cannot be shared in a YNotebook.
         * Call this function to re-initialize the local representation based on a fresh shared model (e.g. models.YFile or models.YCodeCell).
         *
         * @param sharedModel
         * @param reinitialize Whether to reinitialize the shared model.
         */
        switchSharedModel(sharedModel, reinitialize) {
            if (reinitialize) {
                // update local modeldb
                // @todo also change metadata
                this.value.text = sharedModel.getSource();
            }
            this.sharedModel.changed.disconnect(this._onSharedModelChanged, this);
            this.sharedModel.dispose();
            // clone model retrieve a shared (not standalone) model
            this.sharedModel = sharedModel;
            this.sharedModel.changed.connect(this._onSharedModelChanged, this);
            this._sharedModelSwitched.emit(true);
        }
        /**
         * We update the modeldb store when the shared model changes.
         * To ensure that we don't run into infinite loops, we wrap this call in a "mutex".
         * The "mutex" ensures that the wrapped code can only be executed by either the sharedModelChanged handler
         * or the modelDB change handler.
         */
        _onSharedModelChanged(sender, change) {
            globalModelDBMutex(() => {
                if (change.sourceChange) {
                    const value = this.modelDB.get('value');
                    let currpos = 0;
                    change.sourceChange.forEach(delta => {
                        if (delta.insert != null) {
                            value.insert(currpos, delta.insert);
                            currpos += delta.insert.length;
                        }
                        else if (delta.delete != null) {
                            value.remove(currpos, currpos + delta.delete);
                        }
                        else if (delta.retain != null) {
                            currpos += delta.retain;
                        }
                    });
                }
            });
        }
        /**
         * Handle a change to the modelDB value.
         */
        _onModelDBValueChanged(value, event) {
            globalModelDBMutex(() => {
                this.sharedModel.transact(() => {
                    switch (event.type) {
                        case 'insert':
                            this.sharedModel.updateSource(event.start, event.start, event.value);
                            break;
                        case 'remove':
                            this.sharedModel.updateSource(event.start, event.end);
                            break;
                        default:
                            this.sharedModel.setSource(value.text);
                            break;
                    }
                });
            });
        }
        get type() {
            return 'code';
        }
        /**
         * A signal emitted when a mimetype changes.
         */
        get mimeTypeChanged() {
            return this._mimeTypeChanged;
        }
        /**
         * A signal emitted when the shared model was switched.
         */
        get sharedModelSwitched() {
            return this._sharedModelSwitched;
        }
        /**
         * Get the value of the model.
         */
        get value() {
            return this.modelDB.get('value');
        }
        /**
         * Get the selections for the model.
         */
        get selections() {
            return this.modelDB.get('selections');
        }
        /**
         * A mime type of the model.
         */
        get mimeType() {
            return this.modelDB.getValue('mimeType');
        }
        set mimeType(newValue) {
            const oldValue = this.mimeType;
            if (oldValue === newValue) {
                return;
            }
            this.modelDB.setValue('mimeType', newValue);
        }
        /**
         * Whether the model is disposed.
         */
        get isDisposed() {
            return this._isDisposed;
        }
        /**
         * Dispose of the resources used by the model.
         */
        dispose() {
            if (this._isDisposed) {
                return;
            }
            this._isDisposed = true;
            this.modelDB.dispose();
            _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal.clearData(this);
        }
        _onModelDBMimeTypeChanged(mimeType, args) {
            this._mimeTypeChanged.emit({
                name: 'mimeType',
                oldValue: args.oldValue,
                newValue: args.newValue
            });
        }
    }
    CodeEditor.Model = Model;
    /**
     * The default configuration options for an editor.
     */
    CodeEditor.defaultConfig = {
        // Order matters as gutters will be sorted by the configuration order
        autoClosingBrackets: false,
        cursorBlinkRate: 530,
        fontFamily: null,
        fontSize: null,
        handlePaste: true,
        insertSpaces: true,
        lineHeight: null,
        lineNumbers: false,
        lineWrap: 'on',
        matchBrackets: true,
        readOnly: false,
        tabSize: 4,
        rulers: [],
        showTrailingSpace: false,
        wordWrapColumn: 80,
        codeFolding: false
    };
})(CodeEditor || (CodeEditor = {}));


/***/ }),

/***/ "../../packages/codeeditor/lib/index.js":
/*!**********************************************!*\
  !*** ../../packages/codeeditor/lib/index.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeEditor": () => (/* reexport safe */ _editor__WEBPACK_IMPORTED_MODULE_0__.CodeEditor),
/* harmony export */   "CodeEditorWrapper": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_6__.CodeEditorWrapper),
/* harmony export */   "CodeViewerWidget": () => (/* reexport safe */ _viewer__WEBPACK_IMPORTED_MODULE_5__.CodeViewerWidget),
/* harmony export */   "IEditorMimeTypeService": () => (/* reexport safe */ _mimetype__WEBPACK_IMPORTED_MODULE_3__.IEditorMimeTypeService),
/* harmony export */   "IEditorServices": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.IEditorServices),
/* harmony export */   "IPositionModel": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.IPositionModel),
/* harmony export */   "JSONEditor": () => (/* reexport safe */ _jsoneditor__WEBPACK_IMPORTED_MODULE_1__.JSONEditor),
/* harmony export */   "LineCol": () => (/* reexport safe */ _lineCol__WEBPACK_IMPORTED_MODULE_2__.LineCol)
/* harmony export */ });
/* harmony import */ var _editor__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./editor */ "../../packages/codeeditor/lib/editor.js");
/* harmony import */ var _jsoneditor__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./jsoneditor */ "../../packages/codeeditor/lib/jsoneditor.js");
/* harmony import */ var _lineCol__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./lineCol */ "../../packages/codeeditor/lib/lineCol.js");
/* harmony import */ var _mimetype__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./mimetype */ "../../packages/codeeditor/lib/mimetype.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./tokens */ "../../packages/codeeditor/lib/tokens.js");
/* harmony import */ var _viewer__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./viewer */ "../../packages/codeeditor/lib/viewer.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./widget */ "../../packages/codeeditor/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module codeeditor
 */










/***/ }),

/***/ "../../packages/codeeditor/lib/jsoneditor.js":
/*!***************************************************!*\
  !*** ../../packages/codeeditor/lib/jsoneditor.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JSONEditor": () => (/* binding */ JSONEditor)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _editor__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./editor */ "../../packages/codeeditor/lib/editor.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * The class name added to a JSONEditor instance.
 */
const JSONEDITOR_CLASS = 'jp-JSONEditor';
/**
 * The class name added when the Metadata editor contains invalid JSON.
 */
const ERROR_CLASS = 'jp-mod-error';
/**
 * The class name added to the editor host node.
 */
const HOST_CLASS = 'jp-JSONEditor-host';
/**
 * The class name added to the header area.
 */
const HEADER_CLASS = 'jp-JSONEditor-header';
/**
 * A widget for editing observable JSON.
 */
class JSONEditor extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget {
    /**
     * Construct a new JSON editor.
     */
    constructor(options) {
        super();
        this._dataDirty = false;
        this._inputDirty = false;
        this._source = null;
        this._originalValue = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.emptyObject;
        this._changeGuard = false;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.addClass(JSONEDITOR_CLASS);
        this.headerNode = document.createElement('div');
        this.headerNode.className = HEADER_CLASS;
        this.revertButtonNode = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.undoIcon.element({
            tag: 'span',
            title: this._trans.__('Revert changes to data')
        });
        this.commitButtonNode = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.checkIcon.element({
            tag: 'span',
            title: this._trans.__('Commit changes to data'),
            marginLeft: '8px'
        });
        this.editorHostNode = document.createElement('div');
        this.editorHostNode.className = HOST_CLASS;
        this.headerNode.appendChild(this.revertButtonNode);
        this.headerNode.appendChild(this.commitButtonNode);
        this.node.appendChild(this.headerNode);
        this.node.appendChild(this.editorHostNode);
        const model = new _editor__WEBPACK_IMPORTED_MODULE_4__.CodeEditor.Model();
        model.value.text = this._trans.__('No data!');
        model.mimeType = 'application/json';
        model.value.changed.connect(this._onValueChanged, this);
        this.model = model;
        this.editor = options.editorFactory({ host: this.editorHostNode, model });
        this.editor.setOption('readOnly', true);
    }
    /**
     * The observable source.
     */
    get source() {
        return this._source;
    }
    set source(value) {
        if (this._source === value) {
            return;
        }
        if (this._source) {
            this._source.changed.disconnect(this._onSourceChanged, this);
        }
        this._source = value;
        this.editor.setOption('readOnly', value === null);
        if (value) {
            value.changed.connect(this._onSourceChanged, this);
        }
        this._setValue();
    }
    /**
     * Get whether the editor is dirty.
     */
    get isDirty() {
        return this._dataDirty || this._inputDirty;
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event - The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the notebook panel's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        switch (event.type) {
            case 'blur':
                this._evtBlur(event);
                break;
            case 'click':
                this._evtClick(event);
                break;
            default:
                break;
        }
    }
    /**
     * Handle `after-attach` messages for the widget.
     */
    onAfterAttach(msg) {
        const node = this.editorHostNode;
        node.addEventListener('blur', this, true);
        node.addEventListener('click', this, true);
        this.revertButtonNode.hidden = true;
        this.commitButtonNode.hidden = true;
        this.headerNode.addEventListener('click', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        const node = this.editorHostNode;
        node.removeEventListener('blur', this, true);
        node.removeEventListener('click', this, true);
        this.headerNode.removeEventListener('click', this);
    }
    /**
     * Handle a change to the metadata of the source.
     */
    _onSourceChanged(sender, args) {
        if (this._changeGuard) {
            return;
        }
        if (this._inputDirty || this.editor.hasFocus()) {
            this._dataDirty = true;
            return;
        }
        this._setValue();
    }
    /**
     * Handle change events.
     */
    _onValueChanged() {
        let valid = true;
        try {
            const value = JSON.parse(this.editor.model.value.text);
            this.removeClass(ERROR_CLASS);
            this._inputDirty =
                !this._changeGuard && !_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.deepEqual(value, this._originalValue);
        }
        catch (err) {
            this.addClass(ERROR_CLASS);
            this._inputDirty = true;
            valid = false;
        }
        this.revertButtonNode.hidden = !this._inputDirty;
        this.commitButtonNode.hidden = !valid || !this._inputDirty;
    }
    /**
     * Handle blur events for the text area.
     */
    _evtBlur(event) {
        // Update the metadata if necessary.
        if (!this._inputDirty && this._dataDirty) {
            this._setValue();
        }
    }
    /**
     * Handle click events for the buttons.
     */
    _evtClick(event) {
        const target = event.target;
        if (this.revertButtonNode.contains(target)) {
            this._setValue();
        }
        else if (this.commitButtonNode.contains(target)) {
            if (!this.commitButtonNode.hidden && !this.hasClass(ERROR_CLASS)) {
                this._changeGuard = true;
                this._mergeContent();
                this._changeGuard = false;
                this._setValue();
            }
        }
        else if (this.editorHostNode.contains(target)) {
            this.editor.focus();
        }
    }
    /**
     * Merge the user content.
     */
    _mergeContent() {
        const model = this.editor.model;
        const old = this._originalValue;
        const user = JSON.parse(model.value.text);
        const source = this.source;
        if (!source) {
            return;
        }
        // If it is in user and has changed from old, set in new.
        for (const key in user) {
            if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.deepEqual(user[key], old[key] || null)) {
                source.set(key, user[key]);
            }
        }
        // If it was in old and is not in user, remove from source.
        for (const key in old) {
            if (!(key in user)) {
                source.delete(key);
            }
        }
    }
    /**
     * Set the value given the owner contents.
     */
    _setValue() {
        this._dataDirty = false;
        this._inputDirty = false;
        this.revertButtonNode.hidden = true;
        this.commitButtonNode.hidden = true;
        this.removeClass(ERROR_CLASS);
        const model = this.editor.model;
        const content = this._source ? this._source.toJSON() : {};
        this._changeGuard = true;
        if (content === void 0) {
            model.value.text = this._trans.__('No data!');
            this._originalValue = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.JSONExt.emptyObject;
        }
        else {
            const value = JSON.stringify(content, null, 4);
            model.value.text = value;
            this._originalValue = content;
            // Move the cursor to within the brace.
            if (value.length > 1 && value[0] === '{') {
                this.editor.setCursorPosition({ line: 0, column: 1 });
            }
        }
        this._changeGuard = false;
        this.commitButtonNode.hidden = true;
        this.revertButtonNode.hidden = true;
    }
}


/***/ }),

/***/ "../../packages/codeeditor/lib/lineCol.js":
/*!************************************************!*\
  !*** ../../packages/codeeditor/lib/lineCol.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LineCol": () => (/* binding */ LineCol)
/* harmony export */ });
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * A component for rendering a "go-to-line" form.
 */
class LineFormComponent extends (react__WEBPACK_IMPORTED_MODULE_3___default().Component) {
    /**
     * Construct a new LineFormComponent.
     */
    constructor(props) {
        super(props);
        /**
         * Handle a change to the value in the input field.
         */
        this._handleChange = (event) => {
            this.setState({ value: event.currentTarget.value });
        };
        /**
         * Handle submission of the input field.
         */
        this._handleSubmit = (event) => {
            event.preventDefault();
            const value = parseInt(this._textInput.value, 10);
            if (!isNaN(value) &&
                isFinite(value) &&
                1 <= value &&
                value <= this.props.maxLine) {
                this.props.handleSubmit(value);
            }
            return false;
        };
        /**
         * Handle focusing of the input field.
         */
        this._handleFocus = () => {
            this.setState({ hasFocus: true });
        };
        /**
         * Handle blurring of the input field.
         */
        this._handleBlur = () => {
            this.setState({ hasFocus: false });
        };
        this._textInput = null;
        this.translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.state = {
            value: '',
            hasFocus: false
        };
    }
    /**
     * Focus the element on mount.
     */
    componentDidMount() {
        this._textInput.focus();
    }
    /**
     * Render the LineFormComponent.
     */
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-lineFormSearch" },
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("form", { name: "lineColumnForm", onSubmit: this._handleSubmit, noValidate: true },
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: (0,_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.classes)('jp-lineFormWrapper', 'lm-lineForm-wrapper', this.state.hasFocus ? 'jp-lineFormWrapperFocusWithin' : undefined) },
                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { type: "text", className: "jp-lineFormInput", onChange: this._handleChange, onFocus: this._handleFocus, onBlur: this._handleBlur, value: this.state.value, ref: input => {
                            this._textInput = input;
                        } }),
                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-baseLineForm jp-lineFormButtonContainer" },
                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.lineFormIcon.react, { className: "jp-baseLineForm jp-lineFormButtonIcon", elementPosition: "center" }),
                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { type: "submit", className: "jp-baseLineForm jp-lineFormButton", value: "" }))),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("label", { className: "jp-lineFormCaption" }, this._trans.__('Go to line number between 1 and %1', this.props.maxLine)))));
    }
}
/**
 * A pure functional component for rendering a line/column
 * status item.
 */
function LineColComponent(props) {
    const translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
    const trans = translator.load('jupyterlab');
    return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.TextItem, { onClick: props.handleClick, source: trans.__('Ln %1, Col %2', props.line, props.column), title: trans.__('Go to line number…') }));
}
/**
 * A widget implementing a line/column status item.
 */
class LineCol extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Construct a new LineCol status item.
     */
    constructor(translator) {
        super(new LineCol.Model());
        this._popup = null;
        this.addClass(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.interactiveItem);
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
    }
    /**
     * Render the status item.
     */
    render() {
        if (this.model === null) {
            return null;
        }
        else {
            return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(LineColComponent, { line: this.model.line, column: this.model.column, translator: this.translator, handleClick: () => this._handleClick() }));
        }
    }
    /**
     * A click handler for the widget.
     */
    _handleClick() {
        if (this._popup) {
            this._popup.dispose();
        }
        const body = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_3___default().createElement(LineFormComponent, { handleSubmit: val => this._handleSubmit(val), currentLine: this.model.line, maxLine: this.model.editor.lineCount, translator: this.translator }));
        this._popup = (0,_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.showPopup)({
            body: body,
            anchor: this,
            align: 'right'
        });
    }
    /**
     * Handle submission for the widget.
     */
    _handleSubmit(value) {
        this.model.editor.setCursorPosition({ line: value - 1, column: 0 });
        this._popup.dispose();
        this.model.editor.focus();
    }
}
/**
 * A namespace for LineCol statics.
 */
(function (LineCol) {
    /**
     * A VDom model for a status item tracking the line/column of an editor.
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
        constructor() {
            super(...arguments);
            /**
             * React to a change in the cursors of the current editor.
             */
            this._onSelectionChanged = () => {
                const oldState = this._getAllState();
                const pos = this.editor.getCursorPosition();
                this._line = pos.line + 1;
                this._column = pos.column + 1;
                this._triggerChange(oldState, this._getAllState());
            };
            this._line = 1;
            this._column = 1;
            this._editor = null;
        }
        /**
         * The current editor of the model.
         */
        get editor() {
            return this._editor;
        }
        set editor(editor) {
            var _a;
            const oldEditor = this._editor;
            if ((_a = oldEditor === null || oldEditor === void 0 ? void 0 : oldEditor.model) === null || _a === void 0 ? void 0 : _a.selections) {
                oldEditor.model.selections.changed.disconnect(this._onSelectionChanged);
            }
            const oldState = this._getAllState();
            this._editor = editor;
            if (!this._editor) {
                this._column = 1;
                this._line = 1;
            }
            else {
                this._editor.model.selections.changed.connect(this._onSelectionChanged);
                const pos = this._editor.getCursorPosition();
                this._column = pos.column + 1;
                this._line = pos.line + 1;
            }
            this._triggerChange(oldState, this._getAllState());
        }
        /**
         * The current line of the model.
         */
        get line() {
            return this._line;
        }
        /**
         * The current column of the model.
         */
        get column() {
            return this._column;
        }
        _getAllState() {
            return [this._line, this._column];
        }
        _triggerChange(oldState, newState) {
            if (oldState[0] !== newState[0] || oldState[1] !== newState[1]) {
                this.stateChanged.emit(void 0);
            }
        }
    }
    LineCol.Model = Model;
})(LineCol || (LineCol = {}));


/***/ }),

/***/ "../../packages/codeeditor/lib/mimetype.js":
/*!*************************************************!*\
  !*** ../../packages/codeeditor/lib/mimetype.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IEditorMimeTypeService": () => (/* binding */ IEditorMimeTypeService)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * A namespace for `IEditorMimeTypeService`.
 */
var IEditorMimeTypeService;
(function (IEditorMimeTypeService) {
    /**
     * The default mime type.
     */
    IEditorMimeTypeService.defaultMimeType = 'text/plain';
})(IEditorMimeTypeService || (IEditorMimeTypeService = {}));


/***/ }),

/***/ "../../packages/codeeditor/lib/tokens.js":
/*!***********************************************!*\
  !*** ../../packages/codeeditor/lib/tokens.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IEditorServices": () => (/* binding */ IEditorServices),
/* harmony export */   "IPositionModel": () => (/* binding */ IPositionModel)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Code editor services token.
 */
const IEditorServices = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/codeeditor:IEditorServices');
/**
 * Code editor cursor position token.
 */
const IPositionModel = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/codeeditor:IPositionModel');


/***/ }),

/***/ "../../packages/codeeditor/lib/viewer.js":
/*!***********************************************!*\
  !*** ../../packages/codeeditor/lib/viewer.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeViewerWidget": () => (/* binding */ CodeViewerWidget)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _editor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./editor */ "../../packages/codeeditor/lib/editor.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "../../packages/codeeditor/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



class CodeViewerWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    /**
     * Construct a new code viewer widget.
     */
    constructor(options) {
        super();
        this.model = options.model;
        const editorWidget = new _widget__WEBPACK_IMPORTED_MODULE_1__.CodeEditorWrapper({
            factory: options.factory,
            model: options.model
        });
        this.editor = editorWidget.editor;
        this.editor.setOption('readOnly', true);
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.StackedLayout());
        layout.addWidget(editorWidget);
    }
    static createCodeViewer(options) {
        const model = new _editor__WEBPACK_IMPORTED_MODULE_2__.CodeEditor.Model({
            value: options.content,
            mimeType: options.mimeType
        });
        return new CodeViewerWidget({ factory: options.factory, model });
    }
    get content() {
        return this.model.value.text;
    }
    get mimeType() {
        return this.model.mimeType;
    }
}


/***/ }),

/***/ "../../packages/codeeditor/lib/widget.js":
/*!***********************************************!*\
  !*** ../../packages/codeeditor/lib/widget.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodeEditorWrapper": () => (/* binding */ CodeEditorWrapper)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The class name added to an editor widget that has a primary selection.
 */
const HAS_SELECTION_CLASS = 'jp-mod-has-primary-selection';
/**
 * The class name added to an editor widget that has a cursor/selection
 * within the whitespace at the beginning of a line
 */
const HAS_IN_LEADING_WHITESPACE_CLASS = 'jp-mod-in-leading-whitespace';
/**
 * A class used to indicate a drop target.
 */
const DROP_TARGET_CLASS = 'jp-mod-dropTarget';
/**
 * RegExp to test for leading whitespace
 */
const leadingWhitespaceRe = /^\s+$/;
/**
 * A widget which hosts a code editor.
 */
class CodeEditorWrapper extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    /**
     * Construct a new code editor widget.
     */
    constructor(options) {
        super();
        const editor = (this.editor = options.factory({
            host: this.node,
            model: options.model,
            uuid: options.uuid,
            config: options.config,
            selectionStyle: options.selectionStyle
        }));
        editor.model.selections.changed.connect(this._onSelectionsChanged, this);
    }
    /**
     * Get the model used by the widget.
     */
    get model() {
        return this.editor.model;
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        super.dispose();
        this.editor.dispose();
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event - The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the notebook panel's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        switch (event.type) {
            case 'lm-dragenter':
                this._evtDragEnter(event);
                break;
            case 'lm-dragleave':
                this._evtDragLeave(event);
                break;
            case 'lm-dragover':
                this._evtDragOver(event);
                break;
            case 'lm-drop':
                this._evtDrop(event);
                break;
            default:
                break;
        }
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this.editor.focus();
    }
    /**
     * A message handler invoked on an `'after-attach'` message.
     */
    onAfterAttach(msg) {
        super.onAfterAttach(msg);
        const node = this.node;
        node.addEventListener('lm-dragenter', this);
        node.addEventListener('lm-dragleave', this);
        node.addEventListener('lm-dragover', this);
        node.addEventListener('lm-drop', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        const node = this.node;
        node.removeEventListener('lm-dragenter', this);
        node.removeEventListener('lm-dragleave', this);
        node.removeEventListener('lm-dragover', this);
        node.removeEventListener('lm-drop', this);
    }
    /**
     * A message handler invoked on a `'resize'` message.
     */
    onResize(msg) {
        if (this.isVisible) {
            this.editor.resizeToFit();
        }
    }
    /**
     * Handle a change in model selections.
     */
    _onSelectionsChanged() {
        const { start, end } = this.editor.getSelection();
        if (start.column !== end.column || start.line !== end.line) {
            // a selection was made
            this.addClass(HAS_SELECTION_CLASS);
            this.removeClass(HAS_IN_LEADING_WHITESPACE_CLASS);
        }
        else {
            // the cursor was placed
            this.removeClass(HAS_SELECTION_CLASS);
            if (this.editor
                .getLine(end.line)
                .slice(0, end.column)
                .match(leadingWhitespaceRe)) {
                this.addClass(HAS_IN_LEADING_WHITESPACE_CLASS);
            }
            else {
                this.removeClass(HAS_IN_LEADING_WHITESPACE_CLASS);
            }
        }
    }
    /**
     * Handle the `'lm-dragenter'` event for the widget.
     */
    _evtDragEnter(event) {
        if (this.editor.getOption('readOnly') === true) {
            return;
        }
        const data = Private.findTextData(event.mimeData);
        if (data === undefined) {
            return;
        }
        event.preventDefault();
        event.stopPropagation();
        this.addClass('jp-mod-dropTarget');
    }
    /**
     * Handle the `'lm-dragleave'` event for the widget.
     */
    _evtDragLeave(event) {
        this.removeClass(DROP_TARGET_CLASS);
        if (this.editor.getOption('readOnly') === true) {
            return;
        }
        const data = Private.findTextData(event.mimeData);
        if (data === undefined) {
            return;
        }
        event.preventDefault();
        event.stopPropagation();
    }
    /**
     * Handle the `'lm-dragover'` event for the widget.
     */
    _evtDragOver(event) {
        this.removeClass(DROP_TARGET_CLASS);
        if (this.editor.getOption('readOnly') === true) {
            return;
        }
        const data = Private.findTextData(event.mimeData);
        if (data === undefined) {
            return;
        }
        event.preventDefault();
        event.stopPropagation();
        event.dropAction = 'copy';
        this.addClass(DROP_TARGET_CLASS);
    }
    /**
     * Handle the `'lm-drop'` event for the widget.
     */
    _evtDrop(event) {
        if (this.editor.getOption('readOnly') === true) {
            return;
        }
        const data = Private.findTextData(event.mimeData);
        if (data === undefined) {
            return;
        }
        const coordinate = {
            top: event.y,
            bottom: event.y,
            left: event.x,
            right: event.x,
            x: event.x,
            y: event.y,
            width: 0,
            height: 0
        };
        const position = this.editor.getPositionForCoordinate(coordinate);
        if (position === null) {
            return;
        }
        this.removeClass(DROP_TARGET_CLASS);
        event.preventDefault();
        event.stopPropagation();
        if (event.proposedAction === 'none') {
            event.dropAction = 'none';
            return;
        }
        const offset = this.editor.getOffsetAt(position);
        this.model.value.insert(offset, data);
    }
}
/**
 * A namespace for private functionality.
 */
var Private;
(function (Private) {
    /**
     * Given a MimeData instance, extract the first text data, if any.
     */
    function findTextData(mime) {
        const types = mime.types();
        const textType = types.find(t => t.indexOf('text') === 0);
        if (textType === undefined) {
            return undefined;
        }
        return mime.getData(textType);
    }
    Private.findTextData = findTextData;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29kZWVkaXRvcl9saWJfaW5kZXhfanMuODRlYTQ3NDRmMjEwNzYzNjU2YTMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFXMUI7QUFDbUI7QUFJQTtBQUVwRCxNQUFNLGtCQUFrQixHQUFHLGtFQUFrQixFQUFFLENBQUM7QUFFaEQ7Ozs7Ozs7R0FPRztBQUNJLElBQVUsVUFBVSxDQXEwQjFCO0FBcjBCRCxXQUFpQixVQUFVO0lBK0V6Qjs7T0FFRztJQUNVLGdDQUFxQixHQUFvQjtRQUNwRCxTQUFTLEVBQUUsRUFBRTtRQUNiLFdBQVcsRUFBRSxFQUFFO1FBQ2YsS0FBSyxFQUFFLE9BQU87S0FDZixDQUFDO0lBMkdGOztPQUVHO0lBQ0gsTUFBYSxLQUFLO1FBQ2hCOztXQUVHO1FBQ0gsWUFBWSxPQUF3QjtZQStMNUIsZ0JBQVcsR0FBRyxLQUFLLENBQUM7WUFDcEIscUJBQWdCLEdBQUcsSUFBSSxxREFBTSxDQUE2QixJQUFJLENBQUMsQ0FBQztZQUNoRSx5QkFBb0IsR0FBRyxJQUFJLHFEQUFNLENBQWdCLElBQUksQ0FBQyxDQUFDO1lBaE03RCxPQUFPLEdBQUcsT0FBTyxJQUFJLEVBQUUsQ0FBQztZQUN4QixJQUFJLE9BQU8sQ0FBQyxPQUFPLEVBQUU7Z0JBQ25CLElBQUksQ0FBQyxPQUFPLEdBQUcsT0FBTyxDQUFDLE9BQU8sQ0FBQzthQUNoQztpQkFBTTtnQkFDTCxJQUFJLENBQUMsT0FBTyxHQUFHLElBQUksNERBQU8sRUFBRSxDQUFDO2FBQzlCO1lBQ0QsSUFBSSxDQUFDLFdBQVcsR0FBRywyRUFBMkIsQ0FDNUMsSUFBSSxDQUFDLElBQUksRUFDVCxPQUFPLENBQUMsRUFBRSxDQUNXLENBQUM7WUFDeEIsSUFBSSxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxxQkFBcUIsRUFBRSxJQUFJLENBQUMsQ0FBQztZQUVuRSxNQUFNLEtBQUssR0FB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Oi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvZGVlZGl0b3Ivc3JjL2VkaXRvci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29kZWVkaXRvci9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvZGVlZGl0b3Ivc3JjL2pzb25lZGl0b3IudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvZGVlZGl0b3Ivc3JjL2xpbmVDb2wudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb2RlZWRpdG9yL3NyYy9taW1ldHlwZS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29kZWVkaXRvci9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb2RlZWRpdG9yL3NyYy92aWV3ZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvZGVlZGl0b3Ivc3JjL3dpZGdldC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElDaGFuZ2VkQXJncyB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQgKiBhcyBuYmZvcm1hdCBmcm9tICdAanVweXRlcmxhYi9uYmZvcm1hdCc7XG5pbXBvcnQge1xuICBJTW9kZWxEQixcbiAgSU9ic2VydmFibGVNYXAsXG4gIElPYnNlcnZhYmxlU3RyaW5nLFxuICBJT2JzZXJ2YWJsZVZhbHVlLFxuICBNb2RlbERCLFxuICBPYnNlcnZhYmxlVmFsdWVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvb2JzZXJ2YWJsZXMnO1xuaW1wb3J0ICogYXMgbW9kZWxzIGZyb20gJ0BqdXB5dGVybGFiL3NoYXJlZC1tb2RlbHMnO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuXG5jb25zdCBnbG9iYWxNb2RlbERCTXV0ZXggPSBtb2RlbHMuY3JlYXRlTXV0ZXgoKTtcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgY29kZSBlZGl0b3JzLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIC0gQSBjb2RlIGVkaXRvciBpcyBhIHNldCBvZiBjb21tb24gYXNzdW1wdGlvbnMgd2hpY2ggaG9sZCBmb3IgYWxsIGNvbmNyZXRlIGVkaXRvcnMuXG4gKiAtIENoYW5nZXMgaW4gaW1wbGVtZW50YXRpb25zIG9mIHRoZSBjb2RlIGVkaXRvciBzaG91bGQgb25seSBiZSBjYXVzZWQgYnkgY2hhbmdlcyBpbiBjb25jcmV0ZSBlZGl0b3JzLlxuICogLSBDb21tb24gSkxhYiBzZXJ2aWNlcyB3aGljaCBhcmUgYmFzZWQgb24gdGhlIGNvZGUgZWRpdG9yIHNob3VsZCBiZWxvbmcgdG8gYElFZGl0b3JTZXJ2aWNlc2AuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgQ29kZUVkaXRvciB7XG4gIC8qKlxuICAgKiBBIHplcm8tYmFzZWQgcG9zaXRpb24gaW4gdGhlIGVkaXRvci5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVBvc2l0aW9uIGV4dGVuZHMgSlNPTk9iamVjdCB7XG4gICAgLyoqXG4gICAgICogVGhlIGN1cnNvciBsaW5lIG51bWJlci5cbiAgICAgKi9cbiAgICByZWFkb25seSBsaW5lOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY3Vyc29yIGNvbHVtbiBudW1iZXIuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY29sdW1uOiBudW1iZXI7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGRpbWVuc2lvbiBvZiBhbiBlbGVtZW50LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJRGltZW5zaW9uIHtcbiAgICAvKipcbiAgICAgKiBUaGUgd2lkdGggb2YgYW4gZWxlbWVudCBpbiBwaXhlbHMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgd2lkdGg6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBoZWlnaHQgb2YgYW4gZWxlbWVudCBpbiBwaXhlbHMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgaGVpZ2h0OiBudW1iZXI7XG4gIH1cblxuICAvKipcbiAgICogQW4gaW50ZXJmYWNlIGRlc2NyaWJpbmcgZWRpdG9yIHN0YXRlIGNvb3JkaW5hdGVzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29vcmRpbmF0ZSBleHRlbmRzIERPTVJlY3RSZWFkT25seSB7fVxuXG4gIC8qKlxuICAgKiBBIHJhbmdlLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUmFuZ2UgZXh0ZW5kcyBKU09OT2JqZWN0IHtcbiAgICAvKipcbiAgICAgKiBUaGUgcG9zaXRpb24gb2YgdGhlIGZpcnN0IGNoYXJhY3RlciBpbiB0aGUgY3VycmVudCByYW5nZS5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBJZiB0aGlzIHBvc2l0aW9uIGlzIGdyZWF0ZXIgdGhhbiBbZW5kXSB0aGVuIHRoZSByYW5nZSBpcyBjb25zaWRlcmVkXG4gICAgICogdG8gYmUgYmFja3dhcmQuXG4gICAgICovXG4gICAgcmVhZG9ubHkgc3RhcnQ6IElQb3NpdGlvbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwb3NpdGlvbiBvZiB0aGUgbGFzdCBjaGFyYWN0ZXIgaW4gdGhlIGN1cnJlbnQgcmFuZ2UuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogSWYgdGhpcyBwb3NpdGlvbiBpcyBsZXNzIHRoYW4gW3N0YXJ0XSB0aGVuIHRoZSByYW5nZSBpcyBjb25zaWRlcmVkXG4gICAgICogdG8gYmUgYmFja3dhcmQuXG4gICAgICovXG4gICAgcmVhZG9ubHkgZW5kOiBJUG9zaXRpb247XG4gIH1cblxuICAvKipcbiAgICogQSBzZWxlY3Rpb24gc3R5bGUuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElTZWxlY3Rpb25TdHlsZSBleHRlbmRzIEpTT05PYmplY3Qge1xuICAgIC8qKlxuICAgICAqIEEgY2xhc3MgbmFtZSBhZGRlZCB0byBhIHNlbGVjdGlvbi5cbiAgICAgKi9cbiAgICBjbGFzc05hbWU6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIEEgZGlzcGxheSBuYW1lIGFkZGVkIHRvIGEgc2VsZWN0aW9uLlxuICAgICAqL1xuICAgIGRpc3BsYXlOYW1lOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBBIGNvbG9yIGZvciBVSSBlbGVtZW50cy5cbiAgICAgKi9cbiAgICBjb2xvcjogc3RyaW5nO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IHNlbGVjdGlvbiBzdHlsZS5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBkZWZhdWx0U2VsZWN0aW9uU3R5bGU6IElTZWxlY3Rpb25TdHlsZSA9IHtcbiAgICBjbGFzc05hbWU6ICcnLFxuICAgIGRpc3BsYXlOYW1lOiAnJyxcbiAgICBjb2xvcjogJ2JsYWNrJ1xuICB9O1xuXG4gIC8qKlxuICAgKiBBIHRleHQgc2VsZWN0aW9uLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJVGV4dFNlbGVjdGlvbiBleHRlbmRzIElSYW5nZSB7XG4gICAgLyoqXG4gICAgICogVGhlIHV1aWQgb2YgdGhlIHRleHQgc2VsZWN0aW9uIG93bmVyLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHV1aWQ6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBzdHlsZSBvZiB0aGlzIHNlbGVjdGlvbi5cbiAgICAgKi9cbiAgICByZWFkb25seSBzdHlsZTogSVNlbGVjdGlvblN0eWxlO1xuICB9XG5cbiAgLyoqXG4gICAqIEFuIGludGVyZmFjZSBmb3IgYSB0ZXh0IHRva2VuLCBzdWNoIGFzIGEgd29yZCwga2V5d29yZCwgb3IgdmFyaWFibGUuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElUb2tlbiB7XG4gICAgLyoqXG4gICAgICogVGhlIHZhbHVlIG9mIHRoZSB0b2tlbi5cbiAgICAgKi9cbiAgICB2YWx1ZTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIG9mZnNldCBvZiB0aGUgdG9rZW4gaW4gdGhlIGNvZGUgZWRpdG9yLlxuICAgICAqL1xuICAgIG9mZnNldDogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogQW4gb3B0aW9uYWwgdHlwZSBmb3IgdGhlIHRva2VuLlxuICAgICAqL1xuICAgIHR5cGU/OiBzdHJpbmc7XG4gIH1cblxuICAvKipcbiAgICogQW4gaW50ZXJmYWNlIHRvIG1hbmFnZSBzZWxlY3Rpb25zIGJ5IHNlbGVjdGlvbiBvd25lcnMuXG4gICAqXG4gICAqICMjIyMgRGVmaW5pdGlvbnNcbiAgICogLSBhIHVzZXIgY29kZSB0aGF0IGhhcyBhbiBhc3NvY2lhdGVkIHV1aWQgaXMgY2FsbGVkIGEgc2VsZWN0aW9uIG93bmVyLCBzZWUgYENvZGVFZGl0b3IuSVNlbGVjdGlvbk93bmVyYFxuICAgKiAtIGEgc2VsZWN0aW9uIGJlbG9uZ3MgdG8gYSBzZWxlY3Rpb24gb3duZXIgb25seSBpZiBpdCBpcyBhc3NvY2lhdGVkIHdpdGggdGhlIG93bmVyIGJ5IGFuIHV1aWQsIHNlZSBgQ29kZUVkaXRvci5JVGV4dFNlbGVjdGlvbmBcbiAgICpcbiAgICogIyMjIyBSZWFkIGFjY2Vzc1xuICAgKiAtIGFueSB1c2VyIGNvZGUgY2FuIG9ic2VydmUgYW55IHNlbGVjdGlvblxuICAgKlxuICAgKiAjIyMjIFdyaXRlIGFjY2Vzc1xuICAgKiAtIGlmIGEgdXNlciBjb2RlIGlzIGEgc2VsZWN0aW9uIG93bmVyIHRoZW46XG4gICAqICAgLSBpdCBjYW4gY2hhbmdlIHNlbGVjdGlvbnMgYmVsb25naW5nIHRvIGl0XG4gICAqICAgLSBidXQgaXQgbXVzdCBub3QgY2hhbmdlIHNlbGVjdGlvbnMgYmVsb25naW5nIHRvIG90aGVyIHNlbGVjdGlvbiBvd25lcnNcbiAgICogLSBvdGhlcndpc2UgaXQgbXVzdCBub3QgY2hhbmdlIGFueSBzZWxlY3Rpb25cbiAgICovXG5cbiAgLyoqXG4gICAqIEFuIGVkaXRvciBtb2RlbC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU1vZGVsIGV4dGVuZHMgSURpc3Bvc2FibGUge1xuICAgIC8qKlxuICAgICAqIEEgc2lnbmFsIGVtaXR0ZWQgd2hlbiBhIHByb3BlcnR5IGNoYW5nZXMuXG4gICAgICovXG4gICAgbWltZVR5cGVDaGFuZ2VkOiBJU2lnbmFsPElNb2RlbCwgSUNoYW5nZWRBcmdzPHN0cmluZz4+O1xuXG4gICAgLyoqXG4gICAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBzaGFyZWQgbW9kZWwgd2FzIHN3aXRjaGVkLlxuICAgICAqL1xuICAgIHNoYXJlZE1vZGVsU3dpdGNoZWQ6IElTaWduYWw8SU1vZGVsLCBib29sZWFuPjtcblxuICAgIC8qKlxuICAgICAqIFRoZSB0ZXh0IHN0b3JlZCBpbiB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgcmVhZG9ubHkgdmFsdWU6IElPYnNlcnZhYmxlU3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogQSBtaW1lIHR5cGUgb2YgdGhlIG1vZGVsLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIEl0IGlzIG5ldmVyIGBudWxsYCwgdGhlIGRlZmF1bHQgbWltZSB0eXBlIGlzIGB0ZXh0L3BsYWluYC5cbiAgICAgKi9cbiAgICBtaW1lVHlwZTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnRseSBzZWxlY3RlZCBjb2RlLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHNlbGVjdGlvbnM6IElPYnNlcnZhYmxlTWFwPElUZXh0U2VsZWN0aW9uW10+O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHVuZGVybHlpbmcgYElNb2RlbERCYCBpbnN0YW5jZSBpbiB3aGljaCBtb2RlbFxuICAgICAqIGRhdGEgaXMgc3RvcmVkLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IG1vZGVsREI6IElNb2RlbERCO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHNoYXJlZCBtb2RlbCBmb3IgdGhlIGNlbGwgZWRpdG9yLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHNoYXJlZE1vZGVsOiBtb2RlbHMuSVNoYXJlZFRleHQ7XG5cbiAgICAvKipcbiAgICAgKiBXaGVuIHdlIGluaXRpYWxpemUgYSBjZWxsIG1vZGVsLCB3ZSBjcmVhdGUgYSBzdGFuZGFsb25lIGNlbGwgbW9kZWwgdGhhdCBjYW5ub3QgYmUgc2hhcmVkIGluIGEgWU5vdGVib29rLlxuICAgICAqIENhbGwgdGhpcyBmdW5jdGlvbiB0byByZS1pbml0aWFsaXplIHRoZSBsb2NhbCByZXByZXNlbnRhdGlvbiBiYXNlZCBvbiBhIGZyZXNoIHNoYXJlZCBtb2RlbCAoZS5nLiBtb2RlbHMuWUZpbGUgb3IgbW9kZWxzLllDb2RlQ2VsbCkuXG4gICAgICovXG4gICAgc3dpdGNoU2hhcmVkTW9kZWwoXG4gICAgICBzaGFyZWRNb2RlbDogbW9kZWxzLklTaGFyZWRUZXh0LFxuICAgICAgcmVpbml0aWFsaXplOiBib29sZWFuXG4gICAgKTogdm9pZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBpbXBsZW1lbnRhdGlvbiBvZiB0aGUgZWRpdG9yIG1vZGVsLlxuICAgKi9cbiAgZXhwb3J0IGNsYXNzIE1vZGVsIGltcGxlbWVudHMgSU1vZGVsIHtcbiAgICAvKipcbiAgICAgKiBDb25zdHJ1Y3QgYSBuZXcgTW9kZWwuXG4gICAgICovXG4gICAgY29uc3RydWN0b3Iob3B0aW9ucz86IE1vZGVsLklPcHRpb25zKSB7XG4gICAgICBvcHRpb25zID0gb3B0aW9ucyB8fCB7fTtcbiAgICAgIGlmIChvcHRpb25zLm1vZGVsREIpIHtcbiAgICAgICAgdGhpcy5tb2RlbERCID0gb3B0aW9ucy5tb2RlbERCO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgdGhpcy5tb2RlbERCID0gbmV3IE1vZGVsREIoKTtcbiAgICAgIH1cbiAgICAgIHRoaXMuc2hhcmVkTW9kZWwgPSBtb2RlbHMuY3JlYXRlU3RhbmRhbG9uZUNlbGwoXG4gICAgICAgIHRoaXMudHlwZSxcbiAgICAgICAgb3B0aW9ucy5pZFxuICAgICAgKSBhcyBtb2RlbHMuSVNoYXJlZFRleHQ7XG4gICAgICB0aGlzLnNoYXJlZE1vZGVsLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblNoYXJlZE1vZGVsQ2hhbmdlZCwgdGhpcyk7XG5cbiAgICAgIGNvbnN0IHZhbHVlID0gdGhpcy5tb2RlbERCLmNyZWF0ZVN0cmluZygndmFsdWUnKTtcbiAgICAgIHZhbHVlLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vbk1vZGVsREJWYWx1ZUNoYW5nZWQsIHRoaXMpO1xuICAgICAgdmFsdWUudGV4dCA9IHZhbHVlLnRleHQgfHwgb3B0aW9ucy52YWx1ZSB8fCAnJztcblxuICAgICAgY29uc3QgbWltZVR5cGUgPSB0aGlzLm1vZGVsREIuY3JlYXRlVmFsdWUoJ21pbWVUeXBlJyk7XG4gICAgICBtaW1lVHlwZS5jaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25Nb2RlbERCTWltZVR5cGVDaGFuZ2VkLCB0aGlzKTtcbiAgICAgIG1pbWVUeXBlLnNldChvcHRpb25zLm1pbWVUeXBlIHx8ICd0ZXh0L3BsYWluJyk7XG5cbiAgICAgIHRoaXMubW9kZWxEQi5jcmVhdGVNYXAoJ3NlbGVjdGlvbnMnKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBXaGVuIHdlIGluaXRpYWxpemUgYSBjZWxsIG1vZGVsLCB3ZSBjcmVhdGUgYSBzdGFuZGFsb25lIG1vZGVsIHRoYXQgY2Fubm90IGJlIHNoYXJlZCBpbiBhIFlOb3RlYm9vay5cbiAgICAgKiBDYWxsIHRoaXMgZnVuY3Rpb24gdG8gcmUtaW5pdGlhbGl6ZSB0aGUgbG9jYWwgcmVwcmVzZW50YXRpb24gYmFzZWQgb24gYSBmcmVzaCBzaGFyZWQgbW9kZWwgKGUuZy4gbW9kZWxzLllGaWxlIG9yIG1vZGVscy5ZQ29kZUNlbGwpLlxuICAgICAqXG4gICAgICogQHBhcmFtIHNoYXJlZE1vZGVsXG4gICAgICogQHBhcmFtIHJlaW5pdGlhbGl6ZSBXaGV0aGVyIHRvIHJlaW5pdGlhbGl6ZSB0aGUgc2hhcmVkIG1vZGVsLlxuICAgICAqL1xuICAgIHB1YmxpYyBzd2l0Y2hTaGFyZWRNb2RlbChcbiAgICAgIHNoYXJlZE1vZGVsOiBtb2RlbHMuSVNoYXJlZFRleHQsXG4gICAgICByZWluaXRpYWxpemU/OiBib29sZWFuXG4gICAgKTogdm9pZCB7XG4gICAgICBpZiAocmVpbml0aWFsaXplKSB7XG4gICAgICAgIC8vIHVwZGF0ZSBsb2NhbCBtb2RlbGRiXG4gICAgICAgIC8vIEB0b2RvIGFsc28gY2hhbmdlIG1ldGFkYXRhXG4gICAgICAgIHRoaXMudmFsdWUudGV4dCA9IHNoYXJlZE1vZGVsLmdldFNvdXJjZSgpO1xuICAgICAgfVxuICAgICAgdGhpcy5zaGFyZWRNb2RlbC5jaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy5fb25TaGFyZWRNb2RlbENoYW5nZWQsIHRoaXMpO1xuICAgICAgdGhpcy5zaGFyZWRNb2RlbC5kaXNwb3NlKCk7XG4gICAgICAvLyBjbG9uZSBtb2RlbCByZXRyaWV2ZSBhIHNoYXJlZCAobm90IHN0YW5kYWxvbmUpIG1vZGVsXG4gICAgICB0aGlzLnNoYXJlZE1vZGVsID0gc2hhcmVkTW9kZWw7XG4gICAgICB0aGlzLnNoYXJlZE1vZGVsLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblNoYXJlZE1vZGVsQ2hhbmdlZCwgdGhpcyk7XG4gICAgICB0aGlzLl9zaGFyZWRNb2RlbFN3aXRjaGVkLmVtaXQodHJ1ZSk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogV2UgdXBkYXRlIHRoZSBtb2RlbGRiIHN0b3JlIHdoZW4gdGhlIHNoYXJlZCBtb2RlbCBjaGFuZ2VzLlxuICAgICAqIFRvIGVuc3VyZSB0aGF0IHdlIGRvbid0IHJ1biBpbnRvIGluZmluaXRlIGxvb3BzLCB3ZSB3cmFwIHRoaXMgY2FsbCBpbiBhIFwibXV0ZXhcIi5cbiAgICAgKiBUaGUgXCJtdXRleFwiIGVuc3VyZXMgdGhhdCB0aGUgd3JhcHBlZCBjb2RlIGNhbiBvbmx5IGJlIGV4ZWN1dGVkIGJ5IGVpdGhlciB0aGUgc2hhcmVkTW9kZWxDaGFuZ2VkIGhhbmRsZXJcbiAgICAgKiBvciB0aGUgbW9kZWxEQiBjaGFuZ2UgaGFuZGxlci5cbiAgICAgKi9cbiAgICBwcm90ZWN0ZWQgX29uU2hhcmVkTW9kZWxDaGFuZ2VkKFxuICAgICAgc2VuZGVyOiBtb2RlbHMuSVNoYXJlZEJhc2VDZWxsPGFueT4sXG4gICAgICBjaGFuZ2U6IG1vZGVscy5DZWxsQ2hhbmdlPG5iZm9ybWF0LklCYXNlQ2VsbE1ldGFkYXRhPlxuICAgICk6IHZvaWQge1xuICAgICAgZ2xvYmFsTW9kZWxEQk11dGV4KCgpID0+IHtcbiAgICAgICAgaWYgKGNoYW5nZS5zb3VyY2VDaGFuZ2UpIHtcbiAgICAgICAgICBjb25zdCB2YWx1ZSA9IHRoaXMubW9kZWxEQi5nZXQoJ3ZhbHVlJykgYXMgSU9ic2VydmFibGVTdHJpbmc7XG4gICAgICAgICAgbGV0IGN1cnJwb3MgPSAwO1xuICAgICAgICAgIGNoYW5nZS5zb3VyY2VDaGFuZ2UuZm9yRWFjaChkZWx0YSA9PiB7XG4gICAgICAgICAgICBpZiAoZGVsdGEuaW5zZXJ0ICE9IG51bGwpIHtcbiAgICAgICAgICAgICAgdmFsdWUuaW5zZXJ0KGN1cnJwb3MsIGRlbHRhLmluc2VydCk7XG4gICAgICAgICAgICAgIGN1cnJwb3MgKz0gZGVsdGEuaW5zZXJ0Lmxlbmd0aDtcbiAgICAgICAgICAgIH0gZWxzZSBpZiAoZGVsdGEuZGVsZXRlICE9IG51bGwpIHtcbiAgICAgICAgICAgICAgdmFsdWUucmVtb3ZlKGN1cnJwb3MsIGN1cnJwb3MgKyBkZWx0YS5kZWxldGUpO1xuICAgICAgICAgICAgfSBlbHNlIGlmIChkZWx0YS5yZXRhaW4gIT0gbnVsbCkge1xuICAgICAgICAgICAgICBjdXJycG9zICs9IGRlbHRhLnJldGFpbjtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9KTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSBtb2RlbERCIHZhbHVlLlxuICAgICAqL1xuICAgIHByaXZhdGUgX29uTW9kZWxEQlZhbHVlQ2hhbmdlZChcbiAgICAgIHZhbHVlOiBJT2JzZXJ2YWJsZVN0cmluZyxcbiAgICAgIGV2ZW50OiBJT2JzZXJ2YWJsZVN0cmluZy5JQ2hhbmdlZEFyZ3NcbiAgICApOiB2b2lkIHtcbiAgICAgIGdsb2JhbE1vZGVsREJNdXRleCgoKSA9PiB7XG4gICAgICAgIHRoaXMuc2hhcmVkTW9kZWwudHJhbnNhY3QoKCkgPT4ge1xuICAgICAgICAgIHN3aXRjaCAoZXZlbnQudHlwZSkge1xuICAgICAgICAgICAgY2FzZSAnaW5zZXJ0JzpcbiAgICAgICAgICAgICAgdGhpcy5zaGFyZWRNb2RlbC51cGRhdGVTb3VyY2UoXG4gICAgICAgICAgICAgICAgZXZlbnQuc3RhcnQsXG4gICAgICAgICAgICAgICAgZXZlbnQuc3RhcnQsXG4gICAgICAgICAgICAgICAgZXZlbnQudmFsdWVcbiAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICBjYXNlICdyZW1vdmUnOlxuICAgICAgICAgICAgICB0aGlzLnNoYXJlZE1vZGVsLnVwZGF0ZVNvdXJjZShldmVudC5zdGFydCwgZXZlbnQuZW5kKTtcbiAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgICBkZWZhdWx0OlxuICAgICAgICAgICAgICB0aGlzLnNoYXJlZE1vZGVsLnNldFNvdXJjZSh2YWx1ZS50ZXh0KTtcbiAgICAgICAgICAgICAgYnJlYWs7XG4gICAgICAgICAgfVxuICAgICAgICB9KTtcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIGdldCB0eXBlKCk6IG5iZm9ybWF0LkNlbGxUeXBlIHtcbiAgICAgIHJldHVybiAnY29kZSc7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIHNoYXJlZCBtb2RlbCBmb3IgdGhlIGNlbGwgZWRpdG9yLlxuICAgICAqL1xuICAgIHNoYXJlZE1vZGVsOiBtb2RlbHMuSVNoYXJlZFRleHQ7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdW5kZXJseWluZyBgSU1vZGVsREJgIGluc3RhbmNlIGluIHdoaWNoIG1vZGVsXG4gICAgICogZGF0YSBpcyBzdG9yZWQuXG4gICAgICovXG4gICAgcmVhZG9ubHkgbW9kZWxEQjogSU1vZGVsREI7XG5cbiAgICAvKipcbiAgICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gYSBtaW1ldHlwZSBjaGFuZ2VzLlxuICAgICAqL1xuICAgIGdldCBtaW1lVHlwZUNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCBJQ2hhbmdlZEFyZ3M8c3RyaW5nPj4ge1xuICAgICAgcmV0dXJuIHRoaXMuX21pbWVUeXBlQ2hhbmdlZDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIHNoYXJlZCBtb2RlbCB3YXMgc3dpdGNoZWQuXG4gICAgICovXG4gICAgZ2V0IHNoYXJlZE1vZGVsU3dpdGNoZWQoKTogSVNpZ25hbDx0aGlzLCBib29sZWFuPiB7XG4gICAgICByZXR1cm4gdGhpcy5fc2hhcmVkTW9kZWxTd2l0Y2hlZDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBHZXQgdGhlIHZhbHVlIG9mIHRoZSBtb2RlbC5cbiAgICAgKi9cbiAgICBnZXQgdmFsdWUoKTogSU9ic2VydmFibGVTdHJpbmcge1xuICAgICAgcmV0dXJuIHRoaXMubW9kZWxEQi5nZXQoJ3ZhbHVlJykgYXMgSU9ic2VydmFibGVTdHJpbmc7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogR2V0IHRoZSBzZWxlY3Rpb25zIGZvciB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgZ2V0IHNlbGVjdGlvbnMoKTogSU9ic2VydmFibGVNYXA8SVRleHRTZWxlY3Rpb25bXT4ge1xuICAgICAgcmV0dXJuIHRoaXMubW9kZWxEQi5nZXQoJ3NlbGVjdGlvbnMnKSBhcyBJT2JzZXJ2YWJsZU1hcDxJVGV4dFNlbGVjdGlvbltdPjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIG1pbWUgdHlwZSBvZiB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgZ2V0IG1pbWVUeXBlKCk6IHN0cmluZyB7XG4gICAgICByZXR1cm4gdGhpcy5tb2RlbERCLmdldFZhbHVlKCdtaW1lVHlwZScpIGFzIHN0cmluZztcbiAgICB9XG4gICAgc2V0IG1pbWVUeXBlKG5ld1ZhbHVlOiBzdHJpbmcpIHtcbiAgICAgIGNvbnN0IG9sZFZhbHVlID0gdGhpcy5taW1lVHlwZTtcbiAgICAgIGlmIChvbGRWYWx1ZSA9PT0gbmV3VmFsdWUpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgdGhpcy5tb2RlbERCLnNldFZhbHVlKCdtaW1lVHlwZScsIG5ld1ZhbHVlKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBtb2RlbCBpcyBkaXNwb3NlZC5cbiAgICAgKi9cbiAgICBnZXQgaXNEaXNwb3NlZCgpOiBib29sZWFuIHtcbiAgICAgIHJldHVybiB0aGlzLl9pc0Rpc3Bvc2VkO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyB1c2VkIGJ5IHRoZSBtb2RlbC5cbiAgICAgKi9cbiAgICBkaXNwb3NlKCk6IHZvaWQge1xuICAgICAgaWYgKHRoaXMuX2lzRGlzcG9zZWQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgdGhpcy5faXNEaXNwb3NlZCA9IHRydWU7XG4gICAgICB0aGlzLm1vZGVsREIuZGlzcG9zZSgpO1xuICAgICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF9vbk1vZGVsREJNaW1lVHlwZUNoYW5nZWQoXG4gICAgICBtaW1lVHlwZTogSU9ic2VydmFibGVWYWx1ZSxcbiAgICAgIGFyZ3M6IE9ic2VydmFibGVWYWx1ZS5JQ2hhbmdlZEFyZ3NcbiAgICApOiB2b2lkIHtcbiAgICAgIHRoaXMuX21pbWVUeXBlQ2hhbmdlZC5lbWl0KHtcbiAgICAgICAgbmFtZTogJ21pbWVUeXBlJyxcbiAgICAgICAgb2xkVmFsdWU6IGFyZ3Mub2xkVmFsdWUgYXMgc3RyaW5nLFxuICAgICAgICBuZXdWYWx1ZTogYXJncy5uZXdWYWx1ZSBhcyBzdHJpbmdcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIHByaXZhdGUgX2lzRGlzcG9zZWQgPSBmYWxzZTtcbiAgICBwcml2YXRlIF9taW1lVHlwZUNoYW5nZWQgPSBuZXcgU2lnbmFsPHRoaXMsIElDaGFuZ2VkQXJnczxzdHJpbmc+Pih0aGlzKTtcbiAgICBwcml2YXRlIF9zaGFyZWRNb2RlbFN3aXRjaGVkID0gbmV3IFNpZ25hbDx0aGlzLCBib29sZWFuPih0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNlbGVjdGlvbiBvd25lci5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVNlbGVjdGlvbk93bmVyIHtcbiAgICAvKipcbiAgICAgKiBUaGUgdXVpZCBvZiB0aGlzIHNlbGVjdGlvbiBvd25lci5cbiAgICAgKi9cbiAgICB1dWlkOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBSZXR1cm5zIHRoZSBwcmltYXJ5IHBvc2l0aW9uIG9mIHRoZSBjdXJzb3IsIG5ldmVyIGBudWxsYC5cbiAgICAgKi9cbiAgICBnZXRDdXJzb3JQb3NpdGlvbigpOiBJUG9zaXRpb247XG5cbiAgICAvKipcbiAgICAgKiBTZXQgdGhlIHByaW1hcnkgcG9zaXRpb24gb2YgdGhlIGN1cnNvci5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBwb3NpdGlvbiAtIFRoZSBuZXcgcHJpbWFyeSBwb3NpdGlvbi5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGlzIHdpbGwgcmVtb3ZlIGFueSBzZWNvbmRhcnkgY3Vyc29ycy5cbiAgICAgKi9cbiAgICBzZXRDdXJzb3JQb3NpdGlvbihwb3NpdGlvbjogSVBvc2l0aW9uKTogdm9pZDtcblxuICAgIC8qKlxuICAgICAqIFJldHVybnMgdGhlIHByaW1hcnkgc2VsZWN0aW9uLCBuZXZlciBgbnVsbGAuXG4gICAgICovXG4gICAgZ2V0U2VsZWN0aW9uKCk6IElSYW5nZTtcblxuICAgIC8qKlxuICAgICAqIFNldCB0aGUgcHJpbWFyeSBzZWxlY3Rpb24uXG4gICAgICpcbiAgICAgKiBAcGFyYW0gc2VsZWN0aW9uIC0gVGhlIGRlc2lyZWQgc2VsZWN0aW9uIHJhbmdlLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoaXMgd2lsbCByZW1vdmUgYW55IHNlY29uZGFyeSBjdXJzb3JzLlxuICAgICAqL1xuICAgIHNldFNlbGVjdGlvbihzZWxlY3Rpb246IElSYW5nZSk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBHZXRzIHRoZSBzZWxlY3Rpb25zIGZvciBhbGwgdGhlIGN1cnNvcnMsIG5ldmVyIGBudWxsYCBvciBlbXB0eS5cbiAgICAgKi9cbiAgICBnZXRTZWxlY3Rpb25zKCk6IElSYW5nZVtdO1xuXG4gICAgLyoqXG4gICAgICogU2V0cyB0aGUgc2VsZWN0aW9ucyBmb3IgYWxsIHRoZSBjdXJzb3JzLlxuICAgICAqXG4gICAgICogQHBhcmFtIHNlbGVjdGlvbnMgLSBUaGUgbmV3IHNlbGVjdGlvbnMuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogQ3Vyc29ycyB3aWxsIGJlIHJlbW92ZWQgb3IgYWRkZWQsIGFzIG5lY2Vzc2FyeS5cbiAgICAgKiBQYXNzaW5nIGFuIGVtcHR5IGFycmF5IHJlc2V0cyBhIGN1cnNvciBwb3NpdGlvbiB0byB0aGUgc3RhcnQgb2YgYVxuICAgICAqIGRvY3VtZW50LlxuICAgICAqL1xuICAgIHNldFNlbGVjdGlvbnMoc2VsZWN0aW9uczogSVJhbmdlW10pOiB2b2lkO1xuICB9XG5cbiAgLyoqXG4gICAqIEEga2V5ZG93biBoYW5kbGVyIHR5cGUuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogUmV0dXJuIGB0cnVlYCB0byBwcmV2ZW50IHRoZSBkZWZhdWx0IGhhbmRsaW5nIG9mIHRoZSBldmVudCBieSB0aGVcbiAgICogZWRpdG9yLlxuICAgKi9cbiAgZXhwb3J0IHR5cGUgS2V5ZG93bkhhbmRsZXIgPSAoXG4gICAgaW5zdGFuY2U6IElFZGl0b3IsXG4gICAgZXZlbnQ6IEtleWJvYXJkRXZlbnRcbiAgKSA9PiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBUaGUgbG9jYXRpb24gb2YgcmVxdWVzdGVkIGVkZ2VzLlxuICAgKi9cbiAgZXhwb3J0IHR5cGUgRWRnZUxvY2F0aW9uID0gJ3RvcCcgfCAndG9wTGluZScgfCAnYm90dG9tJztcblxuICAvKipcbiAgICogQSB3aWRnZXQgdGhhdCBwcm92aWRlcyBhIGNvZGUgZWRpdG9yLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJRWRpdG9yIGV4dGVuZHMgSVNlbGVjdGlvbk93bmVyLCBJRGlzcG9zYWJsZSB7XG4gICAgLyoqXG4gICAgICogQSBzaWduYWwgZW1pdHRlZCB3aGVuIGVpdGhlciB0aGUgdG9wIG9yIGJvdHRvbSBlZGdlIGlzIHJlcXVlc3RlZC5cbiAgICAgKi9cbiAgICByZWFkb25seSBlZGdlUmVxdWVzdGVkOiBJU2lnbmFsPElFZGl0b3IsIEVkZ2VMb2NhdGlvbj47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZGVmYXVsdCBzZWxlY3Rpb24gc3R5bGUgZm9yIHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgc2VsZWN0aW9uU3R5bGU6IENvZGVFZGl0b3IuSVNlbGVjdGlvblN0eWxlO1xuXG4gICAgLyoqXG4gICAgICogVGhlIERPTSBub2RlIHRoYXQgaG9zdHMgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICByZWFkb25seSBob3N0OiBIVE1MRWxlbWVudDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBtb2RlbCB1c2VkIGJ5IHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgcmVhZG9ubHkgbW9kZWw6IElNb2RlbDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBoZWlnaHQgb2YgYSBsaW5lIGluIHRoZSBlZGl0b3IgaW4gcGl4ZWxzLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGxpbmVIZWlnaHQ6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSB3aWRnZXQgb2YgYSBjaGFyYWN0ZXIgaW4gdGhlIGVkaXRvciBpbiBwaXhlbHMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY2hhcldpZHRoOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBHZXQgdGhlIG51bWJlciBvZiBsaW5lcyBpbiB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGxpbmVDb3VudDogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogR2V0IGEgY29uZmlnIG9wdGlvbiBmb3IgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBnZXRPcHRpb248SyBleHRlbmRzIGtleW9mIElDb25maWc+KG9wdGlvbjogSyk6IElDb25maWdbS107XG5cbiAgICAvKipcbiAgICAgKiBTZXQgYSBjb25maWcgb3B0aW9uIGZvciB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIHNldE9wdGlvbjxLIGV4dGVuZHMga2V5b2YgSUNvbmZpZz4ob3B0aW9uOiBLLCB2YWx1ZTogSUNvbmZpZ1tLXSk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBTZXQgY29uZmlnIG9wdGlvbnMgZm9yIHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgc2V0T3B0aW9ucyhvcHRpb25zOiBQYXJ0aWFsPElDb25maWc+KTogdm9pZDtcblxuICAgIC8qKlxuICAgICAqIFJldHVybnMgdGhlIGNvbnRlbnQgZm9yIHRoZSBnaXZlbiBsaW5lIG51bWJlci5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBsaW5lIC0gVGhlIGxpbmUgb2YgaW50ZXJlc3QuXG4gICAgICpcbiAgICAgKiBAcmV0dXJucyBUaGUgdmFsdWUgb2YgdGhlIGxpbmUuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogTGluZXMgYXJlIDAtYmFzZWQsIGFuZCBhY2Nlc3NpbmcgYSBsaW5lIG91dCBvZiByYW5nZSByZXR1cm5zXG4gICAgICogYHVuZGVmaW5lZGAuXG4gICAgICovXG4gICAgZ2V0TGluZShsaW5lOiBudW1iZXIpOiBzdHJpbmcgfCB1bmRlZmluZWQ7XG5cbiAgICAvKipcbiAgICAgKiBGaW5kIGFuIG9mZnNldCBmb3IgdGhlIGdpdmVuIHBvc2l0aW9uLlxuICAgICAqXG4gICAgICogQHBhcmFtIHBvc2l0aW9uIC0gVGhlIHBvc2l0aW9uIG9mIGludGVyZXN0LlxuICAgICAqXG4gICAgICogQHJldHVybnMgVGhlIG9mZnNldCBhdCB0aGUgcG9zaXRpb24sIGNsYW1wZWQgdG8gdGhlIGV4dGVudCBvZiB0aGVcbiAgICAgKiBlZGl0b3IgY29udGVudHMuXG4gICAgICovXG4gICAgZ2V0T2Zmc2V0QXQocG9zaXRpb246IElQb3NpdGlvbik6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIEZpbmQgYSBwb3NpdGlvbiBmb3IgdGhlIGdpdmVuIG9mZnNldC5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBvZmZzZXQgLSBUaGUgb2Zmc2V0IG9mIGludGVyZXN0LlxuICAgICAqXG4gICAgICogQHJldHVybnMgVGhlIHBvc2l0aW9uIGF0IHRoZSBvZmZzZXQsIGNsYW1wZWQgdG8gdGhlIGV4dGVudCBvZiB0aGVcbiAgICAgKiBlZGl0b3IgY29udGVudHMuXG4gICAgICovXG4gICAgZ2V0UG9zaXRpb25BdChvZmZzZXQ6IG51bWJlcik6IElQb3NpdGlvbiB8IHVuZGVmaW5lZDtcblxuICAgIC8qKlxuICAgICAqIFVuZG8gb25lIGVkaXQgKGlmIGFueSB1bmRvIGV2ZW50cyBhcmUgc3RvcmVkKS5cbiAgICAgKi9cbiAgICB1bmRvKCk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBSZWRvIG9uZSB1bmRvbmUgZWRpdC5cbiAgICAgKi9cbiAgICByZWRvKCk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBDbGVhciB0aGUgdW5kbyBoaXN0b3J5LlxuICAgICAqL1xuICAgIGNsZWFySGlzdG9yeSgpOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogQnJpbmdzIGJyb3dzZXIgZm9jdXMgdG8gdGhpcyBlZGl0b3IgdGV4dC5cbiAgICAgKi9cbiAgICBmb2N1cygpOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogVGVzdCB3aGV0aGVyIHRoZSBlZGl0b3IgaGFzIGtleWJvYXJkIGZvY3VzLlxuICAgICAqL1xuICAgIGhhc0ZvY3VzKCk6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBFeHBsaWNpdGx5IGJsdXIgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBibHVyKCk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBSZXNpemUgdGhlIGVkaXRvciB0byBmaXQgaXRzIGhvc3Qgbm9kZS5cbiAgICAgKi9cbiAgICByZXNpemVUb0ZpdCgpOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogQWRkIGEga2V5ZG93biBoYW5kbGVyIHRvIHRoZSBlZGl0b3IuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gaGFuZGxlciAtIEEga2V5ZG93biBoYW5kbGVyLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBkaXNwb3NhYmxlIHRoYXQgY2FuIGJlIHVzZWQgdG8gcmVtb3ZlIHRoZSBoYW5kbGVyLlxuICAgICAqL1xuICAgIGFkZEtleWRvd25IYW5kbGVyKGhhbmRsZXI6IEtleWRvd25IYW5kbGVyKTogSURpc3Bvc2FibGU7XG5cbiAgICAvKipcbiAgICAgKiBSZXZlYWxzIHRoZSBnaXZlbiBwb3NpdGlvbiBpbiB0aGUgZWRpdG9yLlxuICAgICAqXG4gICAgICogQHBhcmFtIHBvc2l0aW9uIC0gVGhlIGRlc2lyZWQgcG9zaXRpb24gdG8gcmV2ZWFsLlxuICAgICAqL1xuICAgIHJldmVhbFBvc2l0aW9uKHBvc2l0aW9uOiBJUG9zaXRpb24pOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogUmV2ZWFscyB0aGUgZ2l2ZW4gc2VsZWN0aW9uIGluIHRoZSBlZGl0b3IuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gcG9zaXRpb24gLSBUaGUgZGVzaXJlZCBzZWxlY3Rpb24gdG8gcmV2ZWFsLlxuICAgICAqL1xuICAgIHJldmVhbFNlbGVjdGlvbihzZWxlY3Rpb246IElSYW5nZSk6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBHZXQgdGhlIHdpbmRvdyBjb29yZGluYXRlcyBnaXZlbiBhIGN1cnNvciBwb3NpdGlvbi5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBwb3NpdGlvbiAtIFRoZSBkZXNpcmVkIHBvc2l0aW9uLlxuICAgICAqXG4gICAgICogQHJldHVybnMgVGhlIGNvb3JkaW5hdGVzIG9mIHRoZSBwb3NpdGlvbi5cbiAgICAgKi9cbiAgICBnZXRDb29yZGluYXRlRm9yUG9zaXRpb24ocG9zaXRpb246IElQb3NpdGlvbik6IElDb29yZGluYXRlO1xuXG4gICAgLyoqXG4gICAgICogR2V0IHRoZSBjdXJzb3IgcG9zaXRpb24gZ2l2ZW4gd2luZG93IGNvb3JkaW5hdGVzLlxuICAgICAqXG4gICAgICogQHBhcmFtIGNvb3JkaW5hdGUgLSBUaGUgZGVzaXJlZCBjb29yZGluYXRlLlxuICAgICAqXG4gICAgICogQHJldHVybnMgVGhlIHBvc2l0aW9uIG9mIHRoZSBjb29yZGluYXRlcywgb3IgbnVsbCBpZiBub3RcbiAgICAgKiAgIGNvbnRhaW5lZCBpbiB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIGdldFBvc2l0aW9uRm9yQ29vcmRpbmF0ZShjb29yZGluYXRlOiBJQ29vcmRpbmF0ZSk6IElQb3NpdGlvbiB8IG51bGw7XG5cbiAgICAvKipcbiAgICAgKiBHZXQgYSBsaXN0IG9mIHRva2VucyBmb3IgdGhlIGN1cnJlbnQgZWRpdG9yIHRleHQgY29udGVudC5cbiAgICAgKi9cbiAgICBnZXRUb2tlbnMoKTogQ29kZUVkaXRvci5JVG9rZW5bXTtcblxuICAgIC8qKlxuICAgICAqIEdldCB0aGUgdG9rZW4gYXQgYSBnaXZlbiBlZGl0b3IgcG9zaXRpb24uXG4gICAgICovXG4gICAgZ2V0VG9rZW5BdChvZmZzZXQ6IG51bWJlcik6IENvZGVFZGl0b3IuSVRva2VuO1xuXG4gICAgLyoqXG4gICAgICogR2V0IHRoZSB0b2tlbiBhIHRoZSBjdXJzb3IgcG9zaXRpb24uXG4gICAgICovXG4gICAgZ2V0VG9rZW5BdEN1cnNvcigpOiBDb2RlRWRpdG9yLklUb2tlbjtcblxuICAgIC8qKlxuICAgICAqIEluc2VydHMgYSBuZXcgbGluZSBhdCB0aGUgY3Vyc29yIHBvc2l0aW9uIGFuZCBpbmRlbnRzIGl0LlxuICAgICAqL1xuICAgIG5ld0luZGVudGVkTGluZSgpOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogUmVwbGFjZXMgc2VsZWN0aW9uIHdpdGggdGhlIGdpdmVuIHRleHQuXG4gICAgICovXG4gICAgcmVwbGFjZVNlbGVjdGlvbj8odGV4dDogc3RyaW5nKTogdm9pZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIGZhY3RvcnkgdXNlZCB0byBjcmVhdGUgYSBjb2RlIGVkaXRvci5cbiAgICovXG4gIGV4cG9ydCB0eXBlIEZhY3RvcnkgPSAob3B0aW9uczogSU9wdGlvbnMpID0+IENvZGVFZGl0b3IuSUVkaXRvcjtcblxuICAvKipcbiAgICogVGhlIGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBmb3IgYW4gZWRpdG9yLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29uZmlnIHtcbiAgICAvKipcbiAgICAgKiBIYWxmLXBlcmlvZCBpbiBtaWxsaXNlY29uZHMgdXNlZCBmb3IgY3Vyc29yIGJsaW5raW5nLlxuICAgICAqIEJ5IHNldHRpbmcgdGhpcyB0byB6ZXJvLCBibGlua2luZyBjYW4gYmUgZGlzYWJsZWQuXG4gICAgICogQSBuZWdhdGl2ZSB2YWx1ZSBoaWRlcyB0aGUgY3Vyc29yIGVudGlyZWx5LlxuICAgICAqL1xuICAgIGN1cnNvckJsaW5rUmF0ZTogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogVXNlciBwcmVmZXJyZWQgZm9udCBmYW1pbHkgZm9yIHRleHQgZWRpdG9ycy5cbiAgICAgKi9cbiAgICBmb250RmFtaWx5OiBzdHJpbmcgfCBudWxsO1xuXG4gICAgLyoqXG4gICAgICogVXNlciBwcmVmZXJyZWQgc2l6ZSBpbiBwaXhlbCBvZiB0aGUgZm9udCB1c2VkIGluIHRleHQgZWRpdG9ycy5cbiAgICAgKi9cbiAgICBmb250U2l6ZTogbnVtYmVyIHwgbnVsbDtcblxuICAgIC8qKlxuICAgICAqIFVzZXIgcHJlZmVycmVkIHRleHQgbGluZSBoZWlnaHQsIGFzIGEgbXVsdGlwbGllciBvZiBmb250IHNpemUuXG4gICAgICovXG4gICAgbGluZUhlaWdodDogbnVtYmVyIHwgbnVsbDtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgbGluZSBudW1iZXJzIHNob3VsZCBiZSBkaXNwbGF5ZWQuXG4gICAgICovXG4gICAgbGluZU51bWJlcnM6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBDb250cm9sIHRoZSBsaW5lIHdyYXBwaW5nIG9mIHRoZSBlZGl0b3IuIFBvc3NpYmxlIHZhbHVlcyBhcmU6XG4gICAgICogLSBcIm9mZlwiLCBsaW5lcyB3aWxsIG5ldmVyIHdyYXAuXG4gICAgICogLSBcIm9uXCIsIGxpbmVzIHdpbGwgd3JhcCBhdCB0aGUgdmlld3BvcnQgYm9yZGVyLlxuICAgICAqIC0gXCJ3b3JkV3JhcENvbHVtblwiLCBsaW5lcyB3aWxsIHdyYXAgYXQgYHdvcmRXcmFwQ29sdW1uYC5cbiAgICAgKiAtIFwiYm91bmRlZFwiLCBsaW5lcyB3aWxsIHdyYXAgYXQgbWluaW11bSBiZXR3ZWVuIHZpZXdwb3J0IHdpZHRoIGFuZCB3b3JkV3JhcENvbHVtbi5cbiAgICAgKi9cbiAgICBsaW5lV3JhcDogJ29mZicgfCAnb24nIHwgJ3dvcmRXcmFwQ29sdW1uJyB8ICdib3VuZGVkJztcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdGhlIGVkaXRvciBpcyByZWFkLW9ubHkuXG4gICAgICovXG4gICAgcmVhZE9ubHk6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbnVtYmVyIG9mIHNwYWNlcyBhIHRhYiBpcyBlcXVhbCB0by5cbiAgICAgKi9cbiAgICB0YWJTaXplOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIGluc2VydCBzcGFjZXMgd2hlbiBwcmVzc2luZyBUYWIuXG4gICAgICovXG4gICAgaW5zZXJ0U3BhY2VzOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBoaWdobGlnaHQgbWF0Y2hpbmcgYnJhY2tldHMgd2hlbiBvbmUgb2YgdGhlbSBpcyBzZWxlY3RlZC5cbiAgICAgKi9cbiAgICBtYXRjaEJyYWNrZXRzOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBhdXRvbWF0aWNhbGx5IGNsb3NlIGJyYWNrZXRzIGFmdGVyIG9wZW5pbmcgdGhlbS5cbiAgICAgKi9cbiAgICBhdXRvQ2xvc2luZ0JyYWNrZXRzOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgZWRpdG9yIHNob3VsZCBoYW5kbGUgcGFzdGUgZXZlbnRzLlxuICAgICAqL1xuICAgIGhhbmRsZVBhc3RlPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBjb2x1bW4gd2hlcmUgdG8gYnJlYWsgdGV4dCBsaW5lLlxuICAgICAqL1xuICAgIHdvcmRXcmFwQ29sdW1uOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBDb2x1bW4gaW5kZXggYXQgd2hpY2ggcnVsZXJzIHNob3VsZCBiZSBhZGRlZC5cbiAgICAgKi9cbiAgICBydWxlcnM6IEFycmF5PG51bWJlcj47XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIGFsbG93IGNvZGUgZm9sZGluZ1xuICAgICAqL1xuICAgIGNvZGVGb2xkaW5nOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBoaWdobGlnaHQgdHJhaWxpbmcgd2hpdGVzcGFjZVxuICAgICAqL1xuICAgIHNob3dUcmFpbGluZ1NwYWNlOiBib29sZWFuO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkZWZhdWx0IGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBmb3IgYW4gZWRpdG9yLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IGRlZmF1bHRDb25maWc6IElDb25maWcgPSB7XG4gICAgLy8gT3JkZXIgbWF0dGVycyBhcyBndXR0ZXJzIHdpbGwgYmUgc29ydGVkIGJ5IHRoZSBjb25maWd1cmF0aW9uIG9yZGVyXG4gICAgYXV0b0Nsb3NpbmdCcmFja2V0czogZmFsc2UsXG4gICAgY3Vyc29yQmxpbmtSYXRlOiA1MzAsXG4gICAgZm9udEZhbWlseTogbnVsbCxcbiAgICBmb250U2l6ZTogbnVsbCxcbiAgICBoYW5kbGVQYXN0ZTogdHJ1ZSxcbiAgICBpbnNlcnRTcGFjZXM6IHRydWUsXG4gICAgbGluZUhlaWdodDogbnVsbCxcbiAgICBsaW5lTnVtYmVyczogZmFsc2UsXG4gICAgbGluZVdyYXA6ICdvbicsXG4gICAgbWF0Y2hCcmFja2V0czogdHJ1ZSxcbiAgICByZWFkT25seTogZmFsc2UsXG4gICAgdGFiU2l6ZTogNCxcbiAgICBydWxlcnM6IFtdLFxuICAgIHNob3dUcmFpbGluZ1NwYWNlOiBmYWxzZSxcbiAgICB3b3JkV3JhcENvbHVtbjogODAsXG4gICAgY29kZUZvbGRpbmc6IGZhbHNlXG4gIH07XG5cbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gaW5pdGlhbGl6ZSBhbiBlZGl0b3IuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBUaGUgaG9zdCB3aWRnZXQgdXNlZCBieSB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIGhvc3Q6IEhUTUxFbGVtZW50O1xuXG4gICAgLyoqXG4gICAgICogVGhlIG1vZGVsIHVzZWQgYnkgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBtb2RlbDogSU1vZGVsO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGRlc2lyZWQgdXVpZCBmb3IgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICB1dWlkPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGRlZmF1bHQgc2VsZWN0aW9uIHN0eWxlIGZvciB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIHNlbGVjdGlvblN0eWxlPzogUGFydGlhbDxDb2RlRWRpdG9yLklTZWxlY3Rpb25TdHlsZT47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY29uZmlndXJhdGlvbiBvcHRpb25zIGZvciB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIGNvbmZpZz86IFBhcnRpYWw8SUNvbmZpZz47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY29uZmlndXJhdGlvbiBvcHRpb25zIGZvciB0aGUgZWRpdG9yLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxuXG4gIGV4cG9ydCBuYW1lc3BhY2UgTW9kZWwge1xuICAgIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgICAgLyoqXG4gICAgICAgKiBBIHVuaXF1ZSBpZGVudGlmaWVyIGZvciB0aGUgbW9kZWwuXG4gICAgICAgKi9cbiAgICAgIGlkPzogc3RyaW5nO1xuXG4gICAgICAvKipcbiAgICAgICAqIFRoZSBpbml0aWFsIHZhbHVlIG9mIHRoZSBtb2RlbC5cbiAgICAgICAqL1xuICAgICAgdmFsdWU/OiBzdHJpbmc7XG5cbiAgICAgIC8qKlxuICAgICAgICogVGhlIG1pbWV0eXBlIG9mIHRoZSBtb2RlbC5cbiAgICAgICAqL1xuICAgICAgbWltZVR5cGU/OiBzdHJpbmc7XG5cbiAgICAgIC8qKlxuICAgICAgICogQW4gb3B0aW9uYWwgbW9kZWxEQiBmb3Igc3RvcmluZyBtb2RlbCBzdGF0ZS5cbiAgICAgICAqL1xuICAgICAgbW9kZWxEQj86IElNb2RlbERCO1xuICAgIH1cbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgY29kZWVkaXRvclxuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vZWRpdG9yJztcbmV4cG9ydCAqIGZyb20gJy4vZmFjdG9yeSc7XG5leHBvcnQgKiBmcm9tICcuL2pzb25lZGl0b3InO1xuZXhwb3J0ICogZnJvbSAnLi9saW5lQ29sJztcbmV4cG9ydCAqIGZyb20gJy4vbWltZXR5cGUnO1xuZXhwb3J0ICogZnJvbSAnLi90b2tlbnMnO1xuZXhwb3J0ICogZnJvbSAnLi92aWV3ZXInO1xuZXhwb3J0ICogZnJvbSAnLi93aWRnZXQnO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJT2JzZXJ2YWJsZUpTT04gfSBmcm9tICdAanVweXRlcmxhYi9vYnNlcnZhYmxlcyc7XG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGNoZWNrSWNvbiwgdW5kb0ljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7XG4gIEpTT05FeHQsXG4gIEpTT05PYmplY3QsXG4gIFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3Rcbn0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBDb2RlRWRpdG9yIH0gZnJvbSAnLi9lZGl0b3InO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGEgSlNPTkVkaXRvciBpbnN0YW5jZS5cbiAqL1xuY29uc3QgSlNPTkVESVRPUl9DTEFTUyA9ICdqcC1KU09ORWRpdG9yJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB3aGVuIHRoZSBNZXRhZGF0YSBlZGl0b3IgY29udGFpbnMgaW52YWxpZCBKU09OLlxuICovXG5jb25zdCBFUlJPUl9DTEFTUyA9ICdqcC1tb2QtZXJyb3InO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIHRoZSBlZGl0b3IgaG9zdCBub2RlLlxuICovXG5jb25zdCBIT1NUX0NMQVNTID0gJ2pwLUpTT05FZGl0b3ItaG9zdCc7XG5cbi8qKlxuICogVGhlIGNsYXNzIG5hbWUgYWRkZWQgdG8gdGhlIGhlYWRlciBhcmVhLlxuICovXG5jb25zdCBIRUFERVJfQ0xBU1MgPSAnanAtSlNPTkVkaXRvci1oZWFkZXInO1xuXG4vKipcbiAqIEEgd2lkZ2V0IGZvciBlZGl0aW5nIG9ic2VydmFibGUgSlNPTi5cbiAqL1xuZXhwb3J0IGNsYXNzIEpTT05FZGl0b3IgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IEpTT04gZWRpdG9yLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogSlNPTkVkaXRvci5JT3B0aW9ucykge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLmFkZENsYXNzKEpTT05FRElUT1JfQ0xBU1MpO1xuXG4gICAgdGhpcy5oZWFkZXJOb2RlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgdGhpcy5oZWFkZXJOb2RlLmNsYXNzTmFtZSA9IEhFQURFUl9DTEFTUztcblxuICAgIHRoaXMucmV2ZXJ0QnV0dG9uTm9kZSA9IHVuZG9JY29uLmVsZW1lbnQoe1xuICAgICAgdGFnOiAnc3BhbicsXG4gICAgICB0aXRsZTogdGhpcy5fdHJhbnMuX18oJ1JldmVydCBjaGFuZ2VzIHRvIGRhdGEnKVxuICAgIH0pO1xuXG4gICAgdGhpcy5jb21taXRCdXR0b25Ob2RlID0gY2hlY2tJY29uLmVsZW1lbnQoe1xuICAgICAgdGFnOiAnc3BhbicsXG4gICAgICB0aXRsZTogdGhpcy5fdHJhbnMuX18oJ0NvbW1pdCBjaGFuZ2VzIHRvIGRhdGEnKSxcbiAgICAgIG1hcmdpbkxlZnQ6ICc4cHgnXG4gICAgfSk7XG5cbiAgICB0aGlzLmVkaXRvckhvc3ROb2RlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgdGhpcy5lZGl0b3JIb3N0Tm9kZS5jbGFzc05hbWUgPSBIT1NUX0NMQVNTO1xuXG4gICAgdGhpcy5oZWFkZXJOb2RlLmFwcGVuZENoaWxkKHRoaXMucmV2ZXJ0QnV0dG9uTm9kZSk7XG4gICAgdGhpcy5oZWFkZXJOb2RlLmFwcGVuZENoaWxkKHRoaXMuY29tbWl0QnV0dG9uTm9kZSk7XG5cbiAgICB0aGlzLm5vZGUuYXBwZW5kQ2hpbGQodGhpcy5oZWFkZXJOb2RlKTtcbiAgICB0aGlzLm5vZGUuYXBwZW5kQ2hpbGQodGhpcy5lZGl0b3JIb3N0Tm9kZSk7XG5cbiAgICBjb25zdCBtb2RlbCA9IG5ldyBDb2RlRWRpdG9yLk1vZGVsKCk7XG5cbiAgICBtb2RlbC52YWx1ZS50ZXh0ID0gdGhpcy5fdHJhbnMuX18oJ05vIGRhdGEhJyk7XG4gICAgbW9kZWwubWltZVR5cGUgPSAnYXBwbGljYXRpb24vanNvbic7XG4gICAgbW9kZWwudmFsdWUuY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uVmFsdWVDaGFuZ2VkLCB0aGlzKTtcbiAgICB0aGlzLm1vZGVsID0gbW9kZWw7XG4gICAgdGhpcy5lZGl0b3IgPSBvcHRpb25zLmVkaXRvckZhY3RvcnkoeyBob3N0OiB0aGlzLmVkaXRvckhvc3ROb2RlLCBtb2RlbCB9KTtcbiAgICB0aGlzLmVkaXRvci5zZXRPcHRpb24oJ3JlYWRPbmx5JywgdHJ1ZSk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGNvZGUgZWRpdG9yIHVzZWQgYnkgdGhlIGVkaXRvci5cbiAgICovXG4gIHJlYWRvbmx5IGVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yO1xuXG4gIC8qKlxuICAgKiBUaGUgY29kZSBlZGl0b3IgbW9kZWwgdXNlZCBieSB0aGUgZWRpdG9yLlxuICAgKi9cbiAgcmVhZG9ubHkgbW9kZWw6IENvZGVFZGl0b3IuSU1vZGVsO1xuXG4gIC8qKlxuICAgKiBUaGUgZWRpdG9yIGhvc3Qgbm9kZSB1c2VkIGJ5IHRoZSBKU09OIGVkaXRvci5cbiAgICovXG4gIHJlYWRvbmx5IGhlYWRlck5vZGU6IEhUTUxEaXZFbGVtZW50O1xuXG4gIC8qKlxuICAgKiBUaGUgZWRpdG9yIGhvc3Qgbm9kZSB1c2VkIGJ5IHRoZSBKU09OIGVkaXRvci5cbiAgICovXG4gIHJlYWRvbmx5IGVkaXRvckhvc3ROb2RlOiBIVE1MRGl2RWxlbWVudDtcblxuICAvKipcbiAgICogVGhlIHJldmVydCBidXR0b24gdXNlZCBieSB0aGUgSlNPTiBlZGl0b3IuXG4gICAqL1xuICByZWFkb25seSByZXZlcnRCdXR0b25Ob2RlOiBIVE1MU3BhbkVsZW1lbnQ7XG5cbiAgLyoqXG4gICAqIFRoZSBjb21taXQgYnV0dG9uIHVzZWQgYnkgdGhlIEpTT04gZWRpdG9yLlxuICAgKi9cbiAgcmVhZG9ubHkgY29tbWl0QnV0dG9uTm9kZTogSFRNTFNwYW5FbGVtZW50O1xuXG4gIC8qKlxuICAgKiBUaGUgb2JzZXJ2YWJsZSBzb3VyY2UuXG4gICAqL1xuICBnZXQgc291cmNlKCk6IElPYnNlcnZhYmxlSlNPTiB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9zb3VyY2U7XG4gIH1cbiAgc2V0IHNvdXJjZSh2YWx1ZTogSU9ic2VydmFibGVKU09OIHwgbnVsbCkge1xuICAgIGlmICh0aGlzLl9zb3VyY2UgPT09IHZhbHVlKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGlmICh0aGlzLl9zb3VyY2UpIHtcbiAgICAgIHRoaXMuX3NvdXJjZS5jaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy5fb25Tb3VyY2VDaGFuZ2VkLCB0aGlzKTtcbiAgICB9XG4gICAgdGhpcy5fc291cmNlID0gdmFsdWU7XG4gICAgdGhpcy5lZGl0b3Iuc2V0T3B0aW9uKCdyZWFkT25seScsIHZhbHVlID09PSBudWxsKTtcbiAgICBpZiAodmFsdWUpIHtcbiAgICAgIHZhbHVlLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblNvdXJjZUNoYW5nZWQsIHRoaXMpO1xuICAgIH1cbiAgICB0aGlzLl9zZXRWYWx1ZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB3aGV0aGVyIHRoZSBlZGl0b3IgaXMgZGlydHkuXG4gICAqL1xuICBnZXQgaXNEaXJ0eSgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5fZGF0YURpcnR5IHx8IHRoaXMuX2lucHV0RGlydHk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBET00gZXZlbnRzIGZvciB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0gZXZlbnQgLSBUaGUgRE9NIGV2ZW50IHNlbnQgdG8gdGhlIHdpZGdldC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGlzIG1ldGhvZCBpbXBsZW1lbnRzIHRoZSBET00gYEV2ZW50TGlzdGVuZXJgIGludGVyZmFjZSBhbmQgaXNcbiAgICogY2FsbGVkIGluIHJlc3BvbnNlIHRvIGV2ZW50cyBvbiB0aGUgbm90ZWJvb2sgcGFuZWwncyBub2RlLiBJdCBzaG91bGRcbiAgICogbm90IGJlIGNhbGxlZCBkaXJlY3RseSBieSB1c2VyIGNvZGUuXG4gICAqL1xuICBoYW5kbGVFdmVudChldmVudDogRXZlbnQpOiB2b2lkIHtcbiAgICBzd2l0Y2ggKGV2ZW50LnR5cGUpIHtcbiAgICAgIGNhc2UgJ2JsdXInOlxuICAgICAgICB0aGlzLl9ldnRCbHVyKGV2ZW50IGFzIEZvY3VzRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2NsaWNrJzpcbiAgICAgICAgdGhpcy5fZXZ0Q2xpY2soZXZlbnQgYXMgTW91c2VFdmVudCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYWZ0ZXItYXR0YWNoYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGNvbnN0IG5vZGUgPSB0aGlzLmVkaXRvckhvc3ROb2RlO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcignYmx1cicsIHRoaXMsIHRydWUpO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzLCB0cnVlKTtcbiAgICB0aGlzLnJldmVydEJ1dHRvbk5vZGUuaGlkZGVuID0gdHJ1ZTtcbiAgICB0aGlzLmNvbW1pdEJ1dHRvbk5vZGUuaGlkZGVuID0gdHJ1ZTtcbiAgICB0aGlzLmhlYWRlck5vZGUuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYGJlZm9yZS1kZXRhY2hgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQmVmb3JlRGV0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGNvbnN0IG5vZGUgPSB0aGlzLmVkaXRvckhvc3ROb2RlO1xuICAgIG5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignYmx1cicsIHRoaXMsIHRydWUpO1xuICAgIG5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzLCB0cnVlKTtcbiAgICB0aGlzLmhlYWRlck5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIG1ldGFkYXRhIG9mIHRoZSBzb3VyY2UuXG4gICAqL1xuICBwcml2YXRlIF9vblNvdXJjZUNoYW5nZWQoXG4gICAgc2VuZGVyOiBJT2JzZXJ2YWJsZUpTT04sXG4gICAgYXJnczogSU9ic2VydmFibGVKU09OLklDaGFuZ2VkQXJnc1xuICApIHtcbiAgICBpZiAodGhpcy5fY2hhbmdlR3VhcmQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgaWYgKHRoaXMuX2lucHV0RGlydHkgfHwgdGhpcy5lZGl0b3IuaGFzRm9jdXMoKSkge1xuICAgICAgdGhpcy5fZGF0YURpcnR5ID0gdHJ1ZTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fc2V0VmFsdWUoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgY2hhbmdlIGV2ZW50cy5cbiAgICovXG4gIHByaXZhdGUgX29uVmFsdWVDaGFuZ2VkKCk6IHZvaWQge1xuICAgIGxldCB2YWxpZCA9IHRydWU7XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IHZhbHVlID0gSlNPTi5wYXJzZSh0aGlzLmVkaXRvci5tb2RlbC52YWx1ZS50ZXh0KTtcbiAgICAgIHRoaXMucmVtb3ZlQ2xhc3MoRVJST1JfQ0xBU1MpO1xuICAgICAgdGhpcy5faW5wdXREaXJ0eSA9XG4gICAgICAgICF0aGlzLl9jaGFuZ2VHdWFyZCAmJiAhSlNPTkV4dC5kZWVwRXF1YWwodmFsdWUsIHRoaXMuX29yaWdpbmFsVmFsdWUpO1xuICAgIH0gY2F0Y2ggKGVycikge1xuICAgICAgdGhpcy5hZGRDbGFzcyhFUlJPUl9DTEFTUyk7XG4gICAgICB0aGlzLl9pbnB1dERpcnR5ID0gdHJ1ZTtcbiAgICAgIHZhbGlkID0gZmFsc2U7XG4gICAgfVxuICAgIHRoaXMucmV2ZXJ0QnV0dG9uTm9kZS5oaWRkZW4gPSAhdGhpcy5faW5wdXREaXJ0eTtcbiAgICB0aGlzLmNvbW1pdEJ1dHRvbk5vZGUuaGlkZGVuID0gIXZhbGlkIHx8ICF0aGlzLl9pbnB1dERpcnR5O1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBibHVyIGV2ZW50cyBmb3IgdGhlIHRleHQgYXJlYS5cbiAgICovXG4gIHByaXZhdGUgX2V2dEJsdXIoZXZlbnQ6IEZvY3VzRXZlbnQpOiB2b2lkIHtcbiAgICAvLyBVcGRhdGUgdGhlIG1ldGFkYXRhIGlmIG5lY2Vzc2FyeS5cbiAgICBpZiAoIXRoaXMuX2lucHV0RGlydHkgJiYgdGhpcy5fZGF0YURpcnR5KSB7XG4gICAgICB0aGlzLl9zZXRWYWx1ZSgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgY2xpY2sgZXZlbnRzIGZvciB0aGUgYnV0dG9ucy5cbiAgICovXG4gIHByaXZhdGUgX2V2dENsaWNrKGV2ZW50OiBNb3VzZUV2ZW50KTogdm9pZCB7XG4gICAgY29uc3QgdGFyZ2V0ID0gZXZlbnQudGFyZ2V0IGFzIEhUTUxFbGVtZW50O1xuICAgIGlmICh0aGlzLnJldmVydEJ1dHRvbk5vZGUuY29udGFpbnModGFyZ2V0KSkge1xuICAgICAgdGhpcy5fc2V0VmFsdWUoKTtcbiAgICB9IGVsc2UgaWYgKHRoaXMuY29tbWl0QnV0dG9uTm9kZS5jb250YWlucyh0YXJnZXQpKSB7XG4gICAgICBpZiAoIXRoaXMuY29tbWl0QnV0dG9uTm9kZS5oaWRkZW4gJiYgIXRoaXMuaGFzQ2xhc3MoRVJST1JfQ0xBU1MpKSB7XG4gICAgICAgIHRoaXMuX2NoYW5nZUd1YXJkID0gdHJ1ZTtcbiAgICAgICAgdGhpcy5fbWVyZ2VDb250ZW50KCk7XG4gICAgICAgIHRoaXMuX2NoYW5nZUd1YXJkID0gZmFsc2U7XG4gICAgICAgIHRoaXMuX3NldFZhbHVlKCk7XG4gICAgICB9XG4gICAgfSBlbHNlIGlmICh0aGlzLmVkaXRvckhvc3ROb2RlLmNvbnRhaW5zKHRhcmdldCkpIHtcbiAgICAgIHRoaXMuZWRpdG9yLmZvY3VzKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIE1lcmdlIHRoZSB1c2VyIGNvbnRlbnQuXG4gICAqL1xuICBwcml2YXRlIF9tZXJnZUNvbnRlbnQoKTogdm9pZCB7XG4gICAgY29uc3QgbW9kZWwgPSB0aGlzLmVkaXRvci5tb2RlbDtcbiAgICBjb25zdCBvbGQgPSB0aGlzLl9vcmlnaW5hbFZhbHVlO1xuICAgIGNvbnN0IHVzZXIgPSBKU09OLnBhcnNlKG1vZGVsLnZhbHVlLnRleHQpIGFzIEpTT05PYmplY3Q7XG4gICAgY29uc3Qgc291cmNlID0gdGhpcy5zb3VyY2U7XG4gICAgaWYgKCFzb3VyY2UpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBJZiBpdCBpcyBpbiB1c2VyIGFuZCBoYXMgY2hhbmdlZCBmcm9tIG9sZCwgc2V0IGluIG5ldy5cbiAgICBmb3IgKGNvbnN0IGtleSBpbiB1c2VyKSB7XG4gICAgICBpZiAoIUpTT05FeHQuZGVlcEVxdWFsKHVzZXJba2V5XSwgb2xkW2tleV0gfHwgbnVsbCkpIHtcbiAgICAgICAgc291cmNlLnNldChrZXksIHVzZXJba2V5XSk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgLy8gSWYgaXQgd2FzIGluIG9sZCBhbmQgaXMgbm90IGluIHVzZXIsIHJlbW92ZSBmcm9tIHNvdXJjZS5cbiAgICBmb3IgKGNvbnN0IGtleSBpbiBvbGQpIHtcbiAgICAgIGlmICghKGtleSBpbiB1c2VyKSkge1xuICAgICAgICBzb3VyY2UuZGVsZXRlKGtleSk7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgdmFsdWUgZ2l2ZW4gdGhlIG93bmVyIGNvbnRlbnRzLlxuICAgKi9cbiAgcHJpdmF0ZSBfc2V0VmFsdWUoKTogdm9pZCB7XG4gICAgdGhpcy5fZGF0YURpcnR5ID0gZmFsc2U7XG4gICAgdGhpcy5faW5wdXREaXJ0eSA9IGZhbHNlO1xuICAgIHRoaXMucmV2ZXJ0QnV0dG9uTm9kZS5oaWRkZW4gPSB0cnVlO1xuICAgIHRoaXMuY29tbWl0QnV0dG9uTm9kZS5oaWRkZW4gPSB0cnVlO1xuICAgIHRoaXMucmVtb3ZlQ2xhc3MoRVJST1JfQ0xBU1MpO1xuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5lZGl0b3IubW9kZWw7XG4gICAgY29uc3QgY29udGVudCA9IHRoaXMuX3NvdXJjZSA/IHRoaXMuX3NvdXJjZS50b0pTT04oKSA6IHt9O1xuICAgIHRoaXMuX2NoYW5nZUd1YXJkID0gdHJ1ZTtcbiAgICBpZiAoY29udGVudCA9PT0gdm9pZCAwKSB7XG4gICAgICBtb2RlbC52YWx1ZS50ZXh0ID0gdGhpcy5fdHJhbnMuX18oJ05vIGRhdGEhJyk7XG4gICAgICB0aGlzLl9vcmlnaW5hbFZhbHVlID0gSlNPTkV4dC5lbXB0eU9iamVjdDtcbiAgICB9IGVsc2Uge1xuICAgICAgY29uc3QgdmFsdWUgPSBKU09OLnN0cmluZ2lmeShjb250ZW50LCBudWxsLCA0KTtcbiAgICAgIG1vZGVsLnZhbHVlLnRleHQgPSB2YWx1ZTtcbiAgICAgIHRoaXMuX29yaWdpbmFsVmFsdWUgPSBjb250ZW50O1xuICAgICAgLy8gTW92ZSB0aGUgY3Vyc29yIHRvIHdpdGhpbiB0aGUgYnJhY2UuXG4gICAgICBpZiAodmFsdWUubGVuZ3RoID4gMSAmJiB2YWx1ZVswXSA9PT0gJ3snKSB7XG4gICAgICAgIHRoaXMuZWRpdG9yLnNldEN1cnNvclBvc2l0aW9uKHsgbGluZTogMCwgY29sdW1uOiAxIH0pO1xuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLl9jaGFuZ2VHdWFyZCA9IGZhbHNlO1xuICAgIHRoaXMuY29tbWl0QnV0dG9uTm9kZS5oaWRkZW4gPSB0cnVlO1xuICAgIHRoaXMucmV2ZXJ0QnV0dG9uTm9kZS5oaWRkZW4gPSB0cnVlO1xuICB9XG5cbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIHByaXZhdGUgX2RhdGFEaXJ0eSA9IGZhbHNlO1xuICBwcml2YXRlIF9pbnB1dERpcnR5ID0gZmFsc2U7XG4gIHByaXZhdGUgX3NvdXJjZTogSU9ic2VydmFibGVKU09OIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgX29yaWdpbmFsVmFsdWU6IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3QgPSBKU09ORXh0LmVtcHR5T2JqZWN0O1xuICBwcml2YXRlIF9jaGFuZ2VHdWFyZCA9IGZhbHNlO1xufVxuXG4vKipcbiAqIFRoZSBzdGF0aWMgbmFtZXNwYWNlIEpTT05FZGl0b3IgY2xhc3Mgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBKU09ORWRpdG9yIHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gaW5pdGlhbGl6ZSBhIGpzb24gZWRpdG9yLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGVkaXRvciBmYWN0b3J5IHVzZWQgYnkgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBlZGl0b3JGYWN0b3J5OiBDb2RlRWRpdG9yLkZhY3Rvcnk7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgbGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICAgKi9cbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3I7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHtcbiAgaW50ZXJhY3RpdmVJdGVtLFxuICBQb3B1cCxcbiAgc2hvd1BvcHVwLFxuICBUZXh0SXRlbVxufSBmcm9tICdAanVweXRlcmxhYi9zdGF0dXNiYXInO1xuaW1wb3J0IHtcbiAgSVRyYW5zbGF0b3IsXG4gIG51bGxUcmFuc2xhdG9yLFxuICBUcmFuc2xhdGlvbkJ1bmRsZVxufSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQge1xuICBjbGFzc2VzLFxuICBsaW5lRm9ybUljb24sXG4gIFJlYWN0V2lkZ2V0LFxuICBWRG9tTW9kZWwsXG4gIFZEb21SZW5kZXJlclxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgeyBDb2RlRWRpdG9yIH0gZnJvbSAnLi9lZGl0b3InO1xuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBMaW5lRm9ybUNvbXBvbmVudCBzdGF0aWNzLlxuICovXG5uYW1lc3BhY2UgTGluZUZvcm1Db21wb25lbnQge1xuICAvKipcbiAgICogVGhlIHByb3BzIGZvciBMaW5lRm9ybUNvbXBvbmVudC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVByb3BzIHtcbiAgICAvKipcbiAgICAgKiBBIGNhbGxiYWNrIGZvciB3aGVuIHRoZSBmb3JtIGlzIHN1Ym1pdHRlZC5cbiAgICAgKi9cbiAgICBoYW5kbGVTdWJtaXQ6ICh2YWx1ZTogbnVtYmVyKSA9PiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgbGluZSBvZiB0aGUgZm9ybS5cbiAgICAgKi9cbiAgICBjdXJyZW50TGluZTogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogVGhlIG1heGltdW0gbGluZSB0aGUgZm9ybSBjYW4gdGFrZSAodHlwaWNhbGx5IHRoZVxuICAgICAqIG1heGltdW0gbGluZSBvZiB0aGUgcmVsZXZhbnQgZWRpdG9yKS5cbiAgICAgKi9cbiAgICBtYXhMaW5lOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgYXBwbGljYXRpb24gbGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICAgKi9cbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3I7XG4gIH1cblxuICAvKipcbiAgICogVGhlIHByb3BzIGZvciBMaW5lRm9ybUNvbXBvbmVudC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVN0YXRlIHtcbiAgICAvKipcbiAgICAgKiBUaGUgY3VycmVudCB2YWx1ZSBvZiB0aGUgZm9ybS5cbiAgICAgKi9cbiAgICB2YWx1ZTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgZm9ybSBoYXMgZm9jdXMuXG4gICAgICovXG4gICAgaGFzRm9jdXM6IGJvb2xlYW47XG4gIH1cbn1cblxuLyoqXG4gKiBBIGNvbXBvbmVudCBmb3IgcmVuZGVyaW5nIGEgXCJnby10by1saW5lXCIgZm9ybS5cbiAqL1xuY2xhc3MgTGluZUZvcm1Db21wb25lbnQgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQ8XG4gIExpbmVGb3JtQ29tcG9uZW50LklQcm9wcyxcbiAgTGluZUZvcm1Db21wb25lbnQuSVN0YXRlXG4+IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBMaW5lRm9ybUNvbXBvbmVudC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKHByb3BzOiBMaW5lRm9ybUNvbXBvbmVudC5JUHJvcHMpIHtcbiAgICBzdXBlcihwcm9wcyk7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gcHJvcHMudHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgICB0aGlzLl90cmFucyA9IHRoaXMudHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgdGhpcy5zdGF0ZSA9IHtcbiAgICAgIHZhbHVlOiAnJyxcbiAgICAgIGhhc0ZvY3VzOiBmYWxzZVxuICAgIH07XG4gIH1cblxuICAvKipcbiAgICogRm9jdXMgdGhlIGVsZW1lbnQgb24gbW91bnQuXG4gICAqL1xuICBjb21wb25lbnREaWRNb3VudCgpIHtcbiAgICB0aGlzLl90ZXh0SW5wdXQhLmZvY3VzKCk7XG4gIH1cblxuICAvKipcbiAgICogUmVuZGVyIHRoZSBMaW5lRm9ybUNvbXBvbmVudC5cbiAgICovXG4gIHJlbmRlcigpIHtcbiAgICByZXR1cm4gKFxuICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1saW5lRm9ybVNlYXJjaFwiPlxuICAgICAgICA8Zm9ybSBuYW1lPVwibGluZUNvbHVtbkZvcm1cIiBvblN1Ym1pdD17dGhpcy5faGFuZGxlU3VibWl0fSBub1ZhbGlkYXRlPlxuICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgIGNsYXNzTmFtZT17Y2xhc3NlcyhcbiAgICAgICAgICAgICAgJ2pwLWxpbmVGb3JtV3JhcHBlcicsXG4gICAgICAgICAgICAgICdsbS1saW5lRm9ybS13cmFwcGVyJyxcbiAgICAgICAgICAgICAgdGhpcy5zdGF0ZS5oYXNGb2N1cyA/ICdqcC1saW5lRm9ybVdyYXBwZXJGb2N1c1dpdGhpbicgOiB1bmRlZmluZWRcbiAgICAgICAgICAgICl9XG4gICAgICAgICAgPlxuICAgICAgICAgICAgPGlucHV0XG4gICAgICAgICAgICAgIHR5cGU9XCJ0ZXh0XCJcbiAgICAgICAgICAgICAgY2xhc3NOYW1lPVwianAtbGluZUZvcm1JbnB1dFwiXG4gICAgICAgICAgICAgIG9uQ2hhbmdlPXt0aGlzLl9oYW5kbGVDaGFuZ2V9XG4gICAgICAgICAgICAgIG9uRm9jdXM9e3RoaXMuX2hhbmRsZUZvY3VzfVxuICAgICAgICAgICAgICBvbkJsdXI9e3RoaXMuX2hhbmRsZUJsdXJ9XG4gICAgICAgICAgICAgIHZhbHVlPXt0aGlzLnN0YXRlLnZhbHVlfVxuICAgICAgICAgICAgICByZWY9e2lucHV0ID0+IHtcbiAgICAgICAgICAgICAgICB0aGlzLl90ZXh0SW5wdXQgPSBpbnB1dDtcbiAgICAgICAgICAgICAgfX1cbiAgICAgICAgICAgIC8+XG4gICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLWJhc2VMaW5lRm9ybSBqcC1saW5lRm9ybUJ1dHRvbkNvbnRhaW5lclwiPlxuICAgICAgICAgICAgICA8bGluZUZvcm1JY29uLnJlYWN0XG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwianAtYmFzZUxpbmVGb3JtIGpwLWxpbmVGb3JtQnV0dG9uSWNvblwiXG4gICAgICAgICAgICAgICAgZWxlbWVudFBvc2l0aW9uPVwiY2VudGVyXCJcbiAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgPGlucHV0XG4gICAgICAgICAgICAgICAgdHlwZT1cInN1Ym1pdFwiXG4gICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwianAtYmFzZUxpbmVGb3JtIGpwLWxpbmVGb3JtQnV0dG9uXCJcbiAgICAgICAgICAgICAgICB2YWx1ZT1cIlwiXG4gICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICA8bGFiZWwgY2xhc3NOYW1lPVwianAtbGluZUZvcm1DYXB0aW9uXCI+XG4gICAgICAgICAgICB7dGhpcy5fdHJhbnMuX18oXG4gICAgICAgICAgICAgICdHbyB0byBsaW5lIG51bWJlciBiZXR3ZWVuIDEgYW5kICUxJyxcbiAgICAgICAgICAgICAgdGhpcy5wcm9wcy5tYXhMaW5lXG4gICAgICAgICAgICApfVxuICAgICAgICAgIDwvbGFiZWw+XG4gICAgICAgIDwvZm9ybT5cbiAgICAgIDwvZGl2PlxuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIHRoZSB2YWx1ZSBpbiB0aGUgaW5wdXQgZmllbGQuXG4gICAqL1xuICBwcml2YXRlIF9oYW5kbGVDaGFuZ2UgPSAoZXZlbnQ6IFJlYWN0LkNoYW5nZUV2ZW50PEhUTUxJbnB1dEVsZW1lbnQ+KSA9PiB7XG4gICAgdGhpcy5zZXRTdGF0ZSh7IHZhbHVlOiBldmVudC5jdXJyZW50VGFyZ2V0LnZhbHVlIH0pO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgc3VibWlzc2lvbiBvZiB0aGUgaW5wdXQgZmllbGQuXG4gICAqL1xuICBwcml2YXRlIF9oYW5kbGVTdWJtaXQgPSAoZXZlbnQ6IFJlYWN0LkZvcm1FdmVudDxIVE1MRm9ybUVsZW1lbnQ+KSA9PiB7XG4gICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcblxuICAgIGNvbnN0IHZhbHVlID0gcGFyc2VJbnQodGhpcy5fdGV4dElucHV0IS52YWx1ZSwgMTApO1xuICAgIGlmIChcbiAgICAgICFpc05hTih2YWx1ZSkgJiZcbiAgICAgIGlzRmluaXRlKHZhbHVlKSAmJlxuICAgICAgMSA8PSB2YWx1ZSAmJlxuICAgICAgdmFsdWUgPD0gdGhpcy5wcm9wcy5tYXhMaW5lXG4gICAgKSB7XG4gICAgICB0aGlzLnByb3BzLmhhbmRsZVN1Ym1pdCh2YWx1ZSk7XG4gICAgfVxuXG4gICAgcmV0dXJuIGZhbHNlO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgZm9jdXNpbmcgb2YgdGhlIGlucHV0IGZpZWxkLlxuICAgKi9cbiAgcHJpdmF0ZSBfaGFuZGxlRm9jdXMgPSAoKSA9PiB7XG4gICAgdGhpcy5zZXRTdGF0ZSh7IGhhc0ZvY3VzOiB0cnVlIH0pO1xuICB9O1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgYmx1cnJpbmcgb2YgdGhlIGlucHV0IGZpZWxkLlxuICAgKi9cbiAgcHJpdmF0ZSBfaGFuZGxlQmx1ciA9ICgpID0+IHtcbiAgICB0aGlzLnNldFN0YXRlKHsgaGFzRm9jdXM6IGZhbHNlIH0pO1xuICB9O1xuXG4gIHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbiAgcHJpdmF0ZSBfdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlO1xuICBwcml2YXRlIF90ZXh0SW5wdXQ6IEhUTUxJbnB1dEVsZW1lbnQgfCBudWxsID0gbnVsbDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgTGluZUNvbENvbXBvbmVudC5cbiAqL1xubmFtZXNwYWNlIExpbmVDb2xDb21wb25lbnQge1xuICAvKipcbiAgICogUHJvcHMgZm9yIExpbmVDb2xDb21wb25lbnQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgbGluZSBudW1iZXIuXG4gICAgICovXG4gICAgbGluZTogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgY29sdW1uIG51bWJlci5cbiAgICAgKi9cbiAgICBjb2x1bW46IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBhcHBsaWNhdGlvbiBsYW5ndWFnZSB0cmFuc2xhdG9yLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcblxuICAgIC8qKlxuICAgICAqIEEgY2xpY2sgaGFuZGxlciBmb3IgdGhlIExpbmVDb2xDb21wb25lbnQsIHdoaWNoXG4gICAgICogd2UgdXNlIHRvIGxhdW5jaCB0aGUgTGluZUZvcm1Db21wb25lbnQuXG4gICAgICovXG4gICAgaGFuZGxlQ2xpY2s6ICgpID0+IHZvaWQ7XG4gIH1cbn1cblxuLyoqXG4gKiBBIHB1cmUgZnVuY3Rpb25hbCBjb21wb25lbnQgZm9yIHJlbmRlcmluZyBhIGxpbmUvY29sdW1uXG4gKiBzdGF0dXMgaXRlbS5cbiAqL1xuZnVuY3Rpb24gTGluZUNvbENvbXBvbmVudChcbiAgcHJvcHM6IExpbmVDb2xDb21wb25lbnQuSVByb3BzXG4pOiBSZWFjdC5SZWFjdEVsZW1lbnQ8TGluZUNvbENvbXBvbmVudC5JUHJvcHM+IHtcbiAgY29uc3QgdHJhbnNsYXRvciA9IHByb3BzLnRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIHJldHVybiAoXG4gICAgPFRleHRJdGVtXG4gICAgICBvbkNsaWNrPXtwcm9wcy5oYW5kbGVDbGlja31cbiAgICAgIHNvdXJjZT17dHJhbnMuX18oJ0xuICUxLCBDb2wgJTInLCBwcm9wcy5saW5lLCBwcm9wcy5jb2x1bW4pfVxuICAgICAgdGl0bGU9e3RyYW5zLl9fKCdHbyB0byBsaW5lIG51bWJlcuKApicpfVxuICAgIC8+XG4gICk7XG59XG5cbi8qKlxuICogQSB3aWRnZXQgaW1wbGVtZW50aW5nIGEgbGluZS9jb2x1bW4gc3RhdHVzIGl0ZW0uXG4gKi9cbmV4cG9ydCBjbGFzcyBMaW5lQ29sIGV4dGVuZHMgVkRvbVJlbmRlcmVyPExpbmVDb2wuTW9kZWw+IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBMaW5lQ29sIHN0YXR1cyBpdGVtLlxuICAgKi9cbiAgY29uc3RydWN0b3IodHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSB7XG4gICAgc3VwZXIobmV3IExpbmVDb2wuTW9kZWwoKSk7XG4gICAgdGhpcy5hZGRDbGFzcyhpbnRlcmFjdGl2ZUl0ZW0pO1xuICAgIHRoaXMudHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gIH1cblxuICAvKipcbiAgICogUmVuZGVyIHRoZSBzdGF0dXMgaXRlbS5cbiAgICovXG4gIHJlbmRlcigpOiBSZWFjdC5SZWFjdEVsZW1lbnQ8TGluZUNvbENvbXBvbmVudC5JUHJvcHM+IHwgbnVsbCB7XG4gICAgaWYgKHRoaXMubW9kZWwgPT09IG51bGwpIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH0gZWxzZSB7XG4gICAgICByZXR1cm4gKFxuICAgICAgICA8TGluZUNvbENvbXBvbmVudFxuICAgICAgICAgIGxpbmU9e3RoaXMubW9kZWwubGluZX1cbiAgICAgICAgICBjb2x1bW49e3RoaXMubW9kZWwuY29sdW1ufVxuICAgICAgICAgIHRyYW5zbGF0b3I9e3RoaXMudHJhbnNsYXRvcn1cbiAgICAgICAgICBoYW5kbGVDbGljaz17KCkgPT4gdGhpcy5faGFuZGxlQ2xpY2soKX1cbiAgICAgICAgLz5cbiAgICAgICk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEEgY2xpY2sgaGFuZGxlciBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByaXZhdGUgX2hhbmRsZUNsaWNrKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9wb3B1cCkge1xuICAgICAgdGhpcy5fcG9wdXAuZGlzcG9zZSgpO1xuICAgIH1cbiAgICBjb25zdCBib2R5ID0gUmVhY3RXaWRnZXQuY3JlYXRlKFxuICAgICAgPExpbmVGb3JtQ29tcG9uZW50XG4gICAgICAgIGhhbmRsZVN1Ym1pdD17dmFsID0+IHRoaXMuX2hhbmRsZVN1Ym1pdCh2YWwpfVxuICAgICAgICBjdXJyZW50TGluZT17dGhpcy5tb2RlbCEubGluZX1cbiAgICAgICAgbWF4TGluZT17dGhpcy5tb2RlbCEuZWRpdG9yIS5saW5lQ291bnR9XG4gICAgICAgIHRyYW5zbGF0b3I9e3RoaXMudHJhbnNsYXRvcn1cbiAgICAgIC8+XG4gICAgKTtcblxuICAgIHRoaXMuX3BvcHVwID0gc2hvd1BvcHVwKHtcbiAgICAgIGJvZHk6IGJvZHksXG4gICAgICBhbmNob3I6IHRoaXMsXG4gICAgICBhbGlnbjogJ3JpZ2h0J1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBzdWJtaXNzaW9uIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfaGFuZGxlU3VibWl0KHZhbHVlOiBudW1iZXIpOiB2b2lkIHtcbiAgICB0aGlzLm1vZGVsIS5lZGl0b3IhLnNldEN1cnNvclBvc2l0aW9uKHsgbGluZTogdmFsdWUgLSAxLCBjb2x1bW46IDAgfSk7XG4gICAgdGhpcy5fcG9wdXAhLmRpc3Bvc2UoKTtcbiAgICB0aGlzLm1vZGVsIS5lZGl0b3IhLmZvY3VzKCk7XG4gIH1cblxuICBwcm90ZWN0ZWQgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3I7XG4gIHByaXZhdGUgX3BvcHVwOiBQb3B1cCB8IG51bGwgPSBudWxsO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBMaW5lQ29sIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgTGluZUNvbCB7XG4gIC8qKlxuICAgKiBBIFZEb20gbW9kZWwgZm9yIGEgc3RhdHVzIGl0ZW0gdHJhY2tpbmcgdGhlIGxpbmUvY29sdW1uIG9mIGFuIGVkaXRvci5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBNb2RlbCBleHRlbmRzIFZEb21Nb2RlbCB7XG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgZWRpdG9yIG9mIHRoZSBtb2RlbC5cbiAgICAgKi9cbiAgICBnZXQgZWRpdG9yKCk6IENvZGVFZGl0b3IuSUVkaXRvciB8IG51bGwge1xuICAgICAgcmV0dXJuIHRoaXMuX2VkaXRvcjtcbiAgICB9XG4gICAgc2V0IGVkaXRvcihlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvciB8IG51bGwpIHtcbiAgICAgIGNvbnN0IG9sZEVkaXRvciA9IHRoaXMuX2VkaXRvcjtcbiAgICAgIGlmIChvbGRFZGl0b3I/Lm1vZGVsPy5zZWxlY3Rpb25zKSB7XG4gICAgICAgIG9sZEVkaXRvci5tb2RlbC5zZWxlY3Rpb25zLmNoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl9vblNlbGVjdGlvbkNoYW5nZWQpO1xuICAgICAgfVxuXG4gICAgICBjb25zdCBvbGRTdGF0ZSA9IHRoaXMuX2dldEFsbFN0YXRlKCk7XG4gICAgICB0aGlzLl9lZGl0b3IgPSBlZGl0b3I7XG4gICAgICBpZiAoIXRoaXMuX2VkaXRvcikge1xuICAgICAgICB0aGlzLl9jb2x1bW4gPSAxO1xuICAgICAgICB0aGlzLl9saW5lID0gMTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHRoaXMuX2VkaXRvci5tb2RlbC5zZWxlY3Rpb25zLmNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblNlbGVjdGlvbkNoYW5nZWQpO1xuXG4gICAgICAgIGNvbnN0IHBvcyA9IHRoaXMuX2VkaXRvci5nZXRDdXJzb3JQb3NpdGlvbigpO1xuICAgICAgICB0aGlzLl9jb2x1bW4gPSBwb3MuY29sdW1uICsgMTtcbiAgICAgICAgdGhpcy5fbGluZSA9IHBvcy5saW5lICsgMTtcbiAgICAgIH1cblxuICAgICAgdGhpcy5fdHJpZ2dlckNoYW5nZShvbGRTdGF0ZSwgdGhpcy5fZ2V0QWxsU3RhdGUoKSk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgbGluZSBvZiB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgZ2V0IGxpbmUoKTogbnVtYmVyIHtcbiAgICAgIHJldHVybiB0aGlzLl9saW5lO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IGNvbHVtbiBvZiB0aGUgbW9kZWwuXG4gICAgICovXG4gICAgZ2V0IGNvbHVtbigpOiBudW1iZXIge1xuICAgICAgcmV0dXJuIHRoaXMuX2NvbHVtbjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZWFjdCB0byBhIGNoYW5nZSBpbiB0aGUgY3Vyc29ycyBvZiB0aGUgY3VycmVudCBlZGl0b3IuXG4gICAgICovXG4gICAgcHJpdmF0ZSBfb25TZWxlY3Rpb25DaGFuZ2VkID0gKCkgPT4ge1xuICAgICAgY29uc3Qgb2xkU3RhdGUgPSB0aGlzLl9nZXRBbGxTdGF0ZSgpO1xuICAgICAgY29uc3QgcG9zID0gdGhpcy5lZGl0b3IhLmdldEN1cnNvclBvc2l0aW9uKCk7XG4gICAgICB0aGlzLl9saW5lID0gcG9zLmxpbmUgKyAxO1xuICAgICAgdGhpcy5fY29sdW1uID0gcG9zLmNvbHVtbiArIDE7XG5cbiAgICAgIHRoaXMuX3RyaWdnZXJDaGFuZ2Uob2xkU3RhdGUsIHRoaXMuX2dldEFsbFN0YXRlKCkpO1xuICAgIH07XG5cbiAgICBwcml2YXRlIF9nZXRBbGxTdGF0ZSgpOiBbbnVtYmVyLCBudW1iZXJdIHtcbiAgICAgIHJldHVybiBbdGhpcy5fbGluZSwgdGhpcy5fY29sdW1uXTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF90cmlnZ2VyQ2hhbmdlKFxuICAgICAgb2xkU3RhdGU6IFtudW1iZXIsIG51bWJlcl0sXG4gICAgICBuZXdTdGF0ZTogW251bWJlciwgbnVtYmVyXVxuICAgICkge1xuICAgICAgaWYgKG9sZFN0YXRlWzBdICE9PSBuZXdTdGF0ZVswXSB8fCBvbGRTdGF0ZVsxXSAhPT0gbmV3U3RhdGVbMV0pIHtcbiAgICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCh2b2lkIDApO1xuICAgICAgfVxuICAgIH1cblxuICAgIHByaXZhdGUgX2xpbmU6IG51bWJlciA9IDE7XG4gICAgcHJpdmF0ZSBfY29sdW1uOiBudW1iZXIgPSAxO1xuICAgIHByaXZhdGUgX2VkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yIHwgbnVsbCA9IG51bGw7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgbmJmb3JtYXQgZnJvbSAnQGp1cHl0ZXJsYWIvbmJmb3JtYXQnO1xuXG4vKipcbiAqIFRoZSBtaW1lIHR5cGUgc2VydmljZSBvZiBhIGNvZGUgZWRpdG9yLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElFZGl0b3JNaW1lVHlwZVNlcnZpY2Uge1xuICAvKipcbiAgICogR2V0IGEgbWltZSB0eXBlIGZvciB0aGUgZ2l2ZW4gbGFuZ3VhZ2UgaW5mby5cbiAgICpcbiAgICogQHBhcmFtIGluZm8gLSBUaGUgbGFuZ3VhZ2UgaW5mb3JtYXRpb24uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgdmFsaWQgbWltZXR5cGUuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogSWYgYSBtaW1lIHR5cGUgY2Fubm90IGJlIGZvdW5kIHJldHVybnMgdGhlIGRlZmF1bHQgbWltZSB0eXBlIGB0ZXh0L3BsYWluYCwgbmV2ZXIgYG51bGxgLlxuICAgKi9cbiAgZ2V0TWltZVR5cGVCeUxhbmd1YWdlKGluZm86IG5iZm9ybWF0LklMYW5ndWFnZUluZm9NZXRhZGF0YSk6IHN0cmluZztcblxuICAvKipcbiAgICogR2V0IGEgbWltZSB0eXBlIGZvciB0aGUgZ2l2ZW4gZmlsZSBwYXRoLlxuICAgKlxuICAgKiBAcGFyYW0gZmlsZVBhdGggLSBUaGUgZnVsbCBwYXRoIHRvIHRoZSBmaWxlLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHZhbGlkIG1pbWV0eXBlLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIElmIGEgbWltZSB0eXBlIGNhbm5vdCBiZSBmb3VuZCByZXR1cm5zIHRoZSBkZWZhdWx0IG1pbWUgdHlwZSBgdGV4dC9wbGFpbmAsIG5ldmVyIGBudWxsYC5cbiAgICovXG4gIGdldE1pbWVUeXBlQnlGaWxlUGF0aChmaWxlUGF0aDogc3RyaW5nKTogc3RyaW5nO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBgSUVkaXRvck1pbWVUeXBlU2VydmljZWAuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSUVkaXRvck1pbWVUeXBlU2VydmljZSB7XG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBtaW1lIHR5cGUuXG4gICAqL1xuICBleHBvcnQgY29uc3QgZGVmYXVsdE1pbWVUeXBlOiBzdHJpbmcgPSAndGV4dC9wbGFpbic7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFRva2VuIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IENvZGVFZGl0b3IgfSBmcm9tICcuL2VkaXRvcic7XG5pbXBvcnQgeyBJRWRpdG9yRmFjdG9yeVNlcnZpY2UgfSBmcm9tICcuL2ZhY3RvcnknO1xuaW1wb3J0IHsgSUVkaXRvck1pbWVUeXBlU2VydmljZSB9IGZyb20gJy4vbWltZXR5cGUnO1xuXG4vKipcbiAqIENvZGUgZWRpdG9yIHNlcnZpY2VzIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSUVkaXRvclNlcnZpY2VzID0gbmV3IFRva2VuPElFZGl0b3JTZXJ2aWNlcz4oXG4gICdAanVweXRlcmxhYi9jb2RlZWRpdG9yOklFZGl0b3JTZXJ2aWNlcydcbik7XG5cbi8qKlxuICogQ29kZSBlZGl0b3Igc2VydmljZXMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSUVkaXRvclNlcnZpY2VzIHtcbiAgLyoqXG4gICAqIFRoZSBjb2RlIGVkaXRvciBmYWN0b3J5LlxuICAgKi9cbiAgcmVhZG9ubHkgZmFjdG9yeVNlcnZpY2U6IElFZGl0b3JGYWN0b3J5U2VydmljZTtcblxuICAvKipcbiAgICogVGhlIGVkaXRvciBtaW1lIHR5cGUgc2VydmljZS5cbiAgICovXG4gIHJlYWRvbmx5IG1pbWVUeXBlU2VydmljZTogSUVkaXRvck1pbWVUeXBlU2VydmljZTtcbn1cblxuLyoqXG4gKiBDb2RlIGVkaXRvciBjdXJzb3IgcG9zaXRpb24gdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJUG9zaXRpb25Nb2RlbCA9IG5ldyBUb2tlbjxJUG9zaXRpb25Nb2RlbD4oXG4gICdAanVweXRlcmxhYi9jb2RlZWRpdG9yOklQb3NpdGlvbk1vZGVsJ1xuKTtcblxuLyoqXG4gKiBDb2RlIGVkaXRvciBjdXJzb3IgcG9zaXRpb24gbW9kZWwuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVBvc2l0aW9uTW9kZWwge1xuICAvKipcbiAgICogQWRkIGEgZWRpdG9yIHByb3ZpZGVyLlxuICAgKlxuICAgKiBBIHByb3ZpZGVyIHdpbGwgcmVjZWl2ZSB0aGUgY3VycmVudGx5IGFjdGl2ZSB3aWRnZXQgYW5kIG11c3QgcmV0dXJuIHRoZVxuICAgKiBhc3NvY2lhdGVkIGVkaXRvciBpZiBpdCBjYW4gb3IgbnVsbCBvdGhlcndpc2UuXG4gICAqL1xuICBhZGRFZGl0b3JQcm92aWRlcjogKFxuICAgIHByb3ZpZGVyOiAod2lkZ2V0OiBXaWRnZXQgfCBudWxsKSA9PiBDb2RlRWRpdG9yLklFZGl0b3IgfCBudWxsXG4gICkgPT4gdm9pZDtcblxuICAvKipcbiAgICogQ2FsbGJhY2sgdG8gZm9yY2UgdXBkYXRpbmcgdGhlIHByb3ZpZGVyXG4gICAqL1xuICB1cGRhdGUoKTogdm9pZDtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgU3RhY2tlZExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IENvZGVFZGl0b3IgfSBmcm9tICcuL2VkaXRvcic7XG5pbXBvcnQgeyBDb2RlRWRpdG9yV3JhcHBlciB9IGZyb20gJy4vd2lkZ2V0JztcblxuZXhwb3J0IGNsYXNzIENvZGVWaWV3ZXJXaWRnZXQgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGNvZGUgdmlld2VyIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENvZGVWaWV3ZXJXaWRnZXQuSU9wdGlvbnMpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMubW9kZWwgPSBvcHRpb25zLm1vZGVsO1xuXG4gICAgY29uc3QgZWRpdG9yV2lkZ2V0ID0gbmV3IENvZGVFZGl0b3JXcmFwcGVyKHtcbiAgICAgIGZhY3Rvcnk6IG9wdGlvbnMuZmFjdG9yeSxcbiAgICAgIG1vZGVsOiBvcHRpb25zLm1vZGVsXG4gICAgfSk7XG4gICAgdGhpcy5lZGl0b3IgPSBlZGl0b3JXaWRnZXQuZWRpdG9yO1xuICAgIHRoaXMuZWRpdG9yLnNldE9wdGlvbigncmVhZE9ubHknLCB0cnVlKTtcblxuICAgIGNvbnN0IGxheW91dCA9ICh0aGlzLmxheW91dCA9IG5ldyBTdGFja2VkTGF5b3V0KCkpO1xuICAgIGxheW91dC5hZGRXaWRnZXQoZWRpdG9yV2lkZ2V0KTtcbiAgfVxuXG4gIHN0YXRpYyBjcmVhdGVDb2RlVmlld2VyKFxuICAgIG9wdGlvbnM6IENvZGVWaWV3ZXJXaWRnZXQuSU5vTW9kZWxPcHRpb25zXG4gICk6IENvZGVWaWV3ZXJXaWRnZXQge1xuICAgIGNvbnN0IG1vZGVsID0gbmV3IENvZGVFZGl0b3IuTW9kZWwoe1xuICAgICAgdmFsdWU6IG9wdGlvbnMuY29udGVudCxcbiAgICAgIG1pbWVUeXBlOiBvcHRpb25zLm1pbWVUeXBlXG4gICAgfSk7XG4gICAgcmV0dXJuIG5ldyBDb2RlVmlld2VyV2lkZ2V0KHsgZmFjdG9yeTogb3B0aW9ucy5mYWN0b3J5LCBtb2RlbCB9KTtcbiAgfVxuXG4gIGdldCBjb250ZW50KCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMubW9kZWwudmFsdWUudGV4dDtcbiAgfVxuXG4gIGdldCBtaW1lVHlwZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLm1vZGVsLm1pbWVUeXBlO1xuICB9XG5cbiAgbW9kZWw6IENvZGVFZGl0b3IuSU1vZGVsO1xuICBlZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvcjtcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBjb2RlIHZpZXdlciB3aWRnZXQuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgQ29kZVZpZXdlcldpZGdldCB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhbiBjb2RlIHZpZXdlciB3aWRnZXQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBBIGNvZGUgZWRpdG9yIGZhY3RvcnkuXG4gICAgICovXG4gICAgZmFjdG9yeTogQ29kZUVkaXRvci5GYWN0b3J5O1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbnRlbnQgbW9kZWwgZm9yIHRoZSB2aWV3ZXIuXG4gICAgICovXG4gICAgbW9kZWw6IENvZGVFZGl0b3IuTW9kZWw7XG4gIH1cblxuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdXNlZCB0byBjcmVhdGUgYW4gY29kZSB2aWV3ZXIgd2lkZ2V0IHdpdGhvdXQgYSBtb2RlbC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU5vTW9kZWxPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBBIGNvZGUgZWRpdG9yIGZhY3RvcnkuXG4gICAgICovXG4gICAgZmFjdG9yeTogQ29kZUVkaXRvci5GYWN0b3J5O1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbnRlbnQgdG8gZGlzcGxheSBpbiB0aGUgdmlld2VyLlxuICAgICAqL1xuICAgIGNvbnRlbnQ6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBtaW1lIHR5cGUgZm9yIHRoZSBjb250ZW50LlxuICAgICAqL1xuICAgIG1pbWVUeXBlPzogc3RyaW5nO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IE1pbWVEYXRhIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSURyYWdFdmVudCB9IGZyb20gJ0BsdW1pbm8vZHJhZ2Ryb3AnO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBDb2RlRWRpdG9yIH0gZnJvbSAnLi8nO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGFuIGVkaXRvciB3aWRnZXQgdGhhdCBoYXMgYSBwcmltYXJ5IHNlbGVjdGlvbi5cbiAqL1xuY29uc3QgSEFTX1NFTEVDVElPTl9DTEFTUyA9ICdqcC1tb2QtaGFzLXByaW1hcnktc2VsZWN0aW9uJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBhbiBlZGl0b3Igd2lkZ2V0IHRoYXQgaGFzIGEgY3Vyc29yL3NlbGVjdGlvblxuICogd2l0aGluIHRoZSB3aGl0ZXNwYWNlIGF0IHRoZSBiZWdpbm5pbmcgb2YgYSBsaW5lXG4gKi9cbmNvbnN0IEhBU19JTl9MRUFESU5HX1dISVRFU1BBQ0VfQ0xBU1MgPSAnanAtbW9kLWluLWxlYWRpbmctd2hpdGVzcGFjZSc7XG5cbi8qKlxuICogQSBjbGFzcyB1c2VkIHRvIGluZGljYXRlIGEgZHJvcCB0YXJnZXQuXG4gKi9cbmNvbnN0IERST1BfVEFSR0VUX0NMQVNTID0gJ2pwLW1vZC1kcm9wVGFyZ2V0JztcblxuLyoqXG4gKiBSZWdFeHAgdG8gdGVzdCBmb3IgbGVhZGluZyB3aGl0ZXNwYWNlXG4gKi9cbmNvbnN0IGxlYWRpbmdXaGl0ZXNwYWNlUmUgPSAvXlxccyskLztcblxuLyoqXG4gKiBBIHdpZGdldCB3aGljaCBob3N0cyBhIGNvZGUgZWRpdG9yLlxuICovXG5leHBvcnQgY2xhc3MgQ29kZUVkaXRvcldyYXBwZXIgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGNvZGUgZWRpdG9yIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IENvZGVFZGl0b3JXcmFwcGVyLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICBjb25zdCBlZGl0b3IgPSAodGhpcy5lZGl0b3IgPSBvcHRpb25zLmZhY3Rvcnkoe1xuICAgICAgaG9zdDogdGhpcy5ub2RlLFxuICAgICAgbW9kZWw6IG9wdGlvbnMubW9kZWwsXG4gICAgICB1dWlkOiBvcHRpb25zLnV1aWQsXG4gICAgICBjb25maWc6IG9wdGlvbnMuY29uZmlnLFxuICAgICAgc2VsZWN0aW9uU3R5bGU6IG9wdGlvbnMuc2VsZWN0aW9uU3R5bGVcbiAgICB9KSk7XG4gICAgZWRpdG9yLm1vZGVsLnNlbGVjdGlvbnMuY2hhbmdlZC5jb25uZWN0KHRoaXMuX29uU2VsZWN0aW9uc0NoYW5nZWQsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgZWRpdG9yIHdyYXBwZWQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIHJlYWRvbmx5IGVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yO1xuXG4gIC8qKlxuICAgKiBHZXQgdGhlIG1vZGVsIHVzZWQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIGdldCBtb2RlbCgpOiBDb2RlRWRpdG9yLklNb2RlbCB7XG4gICAgcmV0dXJuIHRoaXMuZWRpdG9yLm1vZGVsO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyBoZWxkIGJ5IHRoZSB3aWRnZXQuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICAgIHRoaXMuZWRpdG9yLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtIFRoZSBET00gZXZlbnQgc2VudCB0byB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgbWV0aG9kIGltcGxlbWVudHMgdGhlIERPTSBgRXZlbnRMaXN0ZW5lcmAgaW50ZXJmYWNlIGFuZCBpc1xuICAgKiBjYWxsZWQgaW4gcmVzcG9uc2UgdG8gZXZlbnRzIG9uIHRoZSBub3RlYm9vayBwYW5lbCdzIG5vZGUuIEl0IHNob3VsZFxuICAgKiBub3QgYmUgY2FsbGVkIGRpcmVjdGx5IGJ5IHVzZXIgY29kZS5cbiAgICovXG4gIGhhbmRsZUV2ZW50KGV2ZW50OiBFdmVudCk6IHZvaWQge1xuICAgIHN3aXRjaCAoZXZlbnQudHlwZSkge1xuICAgICAgY2FzZSAnbG0tZHJhZ2VudGVyJzpcbiAgICAgICAgdGhpcy5fZXZ0RHJhZ0VudGVyKGV2ZW50IGFzIElEcmFnRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2xtLWRyYWdsZWF2ZSc6XG4gICAgICAgIHRoaXMuX2V2dERyYWdMZWF2ZShldmVudCBhcyBJRHJhZ0V2ZW50KTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdsbS1kcmFnb3Zlcic6XG4gICAgICAgIHRoaXMuX2V2dERyYWdPdmVyKGV2ZW50IGFzIElEcmFnRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2xtLWRyb3AnOlxuICAgICAgICB0aGlzLl9ldnREcm9wKGV2ZW50IGFzIElEcmFnRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYCdhY3RpdmF0ZS1yZXF1ZXN0J2AgbWVzc2FnZXMuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25BY3RpdmF0ZVJlcXVlc3QobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgdGhpcy5lZGl0b3IuZm9jdXMoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIG1lc3NhZ2UgaGFuZGxlciBpbnZva2VkIG9uIGFuIGAnYWZ0ZXItYXR0YWNoJ2AgbWVzc2FnZS5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHN1cGVyLm9uQWZ0ZXJBdHRhY2gobXNnKTtcbiAgICBjb25zdCBub2RlID0gdGhpcy5ub2RlO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcignbG0tZHJhZ2VudGVyJywgdGhpcyk7XG4gICAgbm9kZS5hZGRFdmVudExpc3RlbmVyKCdsbS1kcmFnbGVhdmUnLCB0aGlzKTtcbiAgICBub2RlLmFkZEV2ZW50TGlzdGVuZXIoJ2xtLWRyYWdvdmVyJywgdGhpcyk7XG4gICAgbm9kZS5hZGRFdmVudExpc3RlbmVyKCdsbS1kcm9wJywgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBiZWZvcmUtZGV0YWNoYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBvbkJlZm9yZURldGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBjb25zdCBub2RlID0gdGhpcy5ub2RlO1xuICAgIG5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignbG0tZHJhZ2VudGVyJywgdGhpcyk7XG4gICAgbm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdsbS1kcmFnbGVhdmUnLCB0aGlzKTtcbiAgICBub2RlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2xtLWRyYWdvdmVyJywgdGhpcyk7XG4gICAgbm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdsbS1kcm9wJywgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogQSBtZXNzYWdlIGhhbmRsZXIgaW52b2tlZCBvbiBhIGAncmVzaXplJ2AgbWVzc2FnZS5cbiAgICovXG4gIHByb3RlY3RlZCBvblJlc2l6ZShtc2c6IFdpZGdldC5SZXNpemVNZXNzYWdlKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNWaXNpYmxlKSB7XG4gICAgICB0aGlzLmVkaXRvci5yZXNpemVUb0ZpdCgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgaW4gbW9kZWwgc2VsZWN0aW9ucy5cbiAgICovXG4gIHByaXZhdGUgX29uU2VsZWN0aW9uc0NoYW5nZWQoKTogdm9pZCB7XG4gICAgY29uc3QgeyBzdGFydCwgZW5kIH0gPSB0aGlzLmVkaXRvci5nZXRTZWxlY3Rpb24oKTtcblxuICAgIGlmIChzdGFydC5jb2x1bW4gIT09IGVuZC5jb2x1bW4gfHwgc3RhcnQubGluZSAhPT0gZW5kLmxpbmUpIHtcbiAgICAgIC8vIGEgc2VsZWN0aW9uIHdhcyBtYWRlXG4gICAgICB0aGlzLmFkZENsYXNzKEhBU19TRUxFQ1RJT05fQ0xBU1MpO1xuICAgICAgdGhpcy5yZW1vdmVDbGFzcyhIQVNfSU5fTEVBRElOR19XSElURVNQQUNFX0NMQVNTKTtcbiAgICB9IGVsc2Uge1xuICAgICAgLy8gdGhlIGN1cnNvciB3YXMgcGxhY2VkXG4gICAgICB0aGlzLnJlbW92ZUNsYXNzKEhBU19TRUxFQ1RJT05fQ0xBU1MpO1xuXG4gICAgICBpZiAoXG4gICAgICAgIHRoaXMuZWRpdG9yXG4gICAgICAgICAgLmdldExpbmUoZW5kLmxpbmUpIVxuICAgICAgICAgIC5zbGljZSgwLCBlbmQuY29sdW1uKVxuICAgICAgICAgIC5tYXRjaChsZWFkaW5nV2hpdGVzcGFjZVJlKVxuICAgICAgKSB7XG4gICAgICAgIHRoaXMuYWRkQ2xhc3MoSEFTX0lOX0xFQURJTkdfV0hJVEVTUEFDRV9DTEFTUyk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICB0aGlzLnJlbW92ZUNsYXNzKEhBU19JTl9MRUFESU5HX1dISVRFU1BBQ0VfQ0xBU1MpO1xuICAgICAgfVxuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGAnbG0tZHJhZ2VudGVyJ2AgZXZlbnQgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcml2YXRlIF9ldnREcmFnRW50ZXIoZXZlbnQ6IElEcmFnRXZlbnQpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5lZGl0b3IuZ2V0T3B0aW9uKCdyZWFkT25seScpID09PSB0cnVlKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IGRhdGEgPSBQcml2YXRlLmZpbmRUZXh0RGF0YShldmVudC5taW1lRGF0YSk7XG4gICAgaWYgKGRhdGEgPT09IHVuZGVmaW5lZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICAgIGV2ZW50LnN0b3BQcm9wYWdhdGlvbigpO1xuICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLW1vZC1kcm9wVGFyZ2V0Jyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBgJ2xtLWRyYWdsZWF2ZSdgIGV2ZW50IGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0RHJhZ0xlYXZlKGV2ZW50OiBJRHJhZ0V2ZW50KTogdm9pZCB7XG4gICAgdGhpcy5yZW1vdmVDbGFzcyhEUk9QX1RBUkdFVF9DTEFTUyk7XG4gICAgaWYgKHRoaXMuZWRpdG9yLmdldE9wdGlvbigncmVhZE9ubHknKSA9PT0gdHJ1ZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBkYXRhID0gUHJpdmF0ZS5maW5kVGV4dERhdGEoZXZlbnQubWltZURhdGEpO1xuICAgIGlmIChkYXRhID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICBldmVudC5zdG9wUHJvcGFnYXRpb24oKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGAnbG0tZHJhZ292ZXInYCBldmVudCBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByaXZhdGUgX2V2dERyYWdPdmVyKGV2ZW50OiBJRHJhZ0V2ZW50KTogdm9pZCB7XG4gICAgdGhpcy5yZW1vdmVDbGFzcyhEUk9QX1RBUkdFVF9DTEFTUyk7XG4gICAgaWYgKHRoaXMuZWRpdG9yLmdldE9wdGlvbigncmVhZE9ubHknKSA9PT0gdHJ1ZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBkYXRhID0gUHJpdmF0ZS5maW5kVGV4dERhdGEoZXZlbnQubWltZURhdGEpO1xuICAgIGlmIChkYXRhID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICBldmVudC5zdG9wUHJvcGFnYXRpb24oKTtcbiAgICBldmVudC5kcm9wQWN0aW9uID0gJ2NvcHknO1xuICAgIHRoaXMuYWRkQ2xhc3MoRFJPUF9UQVJHRVRfQ0xBU1MpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgYCdsbS1kcm9wJ2AgZXZlbnQgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcml2YXRlIF9ldnREcm9wKGV2ZW50OiBJRHJhZ0V2ZW50KTogdm9pZCB7XG4gICAgaWYgKHRoaXMuZWRpdG9yLmdldE9wdGlvbigncmVhZE9ubHknKSA9PT0gdHJ1ZSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBkYXRhID0gUHJpdmF0ZS5maW5kVGV4dERhdGEoZXZlbnQubWltZURhdGEpO1xuICAgIGlmIChkYXRhID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgY29uc3QgY29vcmRpbmF0ZSA9IHtcbiAgICAgIHRvcDogZXZlbnQueSxcbiAgICAgIGJvdHRvbTogZXZlbnQueSxcbiAgICAgIGxlZnQ6IGV2ZW50LngsXG4gICAgICByaWdodDogZXZlbnQueCxcbiAgICAgIHg6IGV2ZW50LngsXG4gICAgICB5OiBldmVudC55LFxuICAgICAgd2lkdGg6IDAsXG4gICAgICBoZWlnaHQ6IDBcbiAgICB9IGFzIENvZGVFZGl0b3IuSUNvb3JkaW5hdGU7XG4gICAgY29uc3QgcG9zaXRpb24gPSB0aGlzLmVkaXRvci5nZXRQb3NpdGlvbkZvckNvb3JkaW5hdGUoY29vcmRpbmF0ZSk7XG4gICAgaWYgKHBvc2l0aW9uID09PSBudWxsKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMucmVtb3ZlQ2xhc3MoRFJPUF9UQVJHRVRfQ0xBU1MpO1xuICAgIGV2ZW50LnByZXZlbnREZWZhdWx0KCk7XG4gICAgZXZlbnQuc3RvcFByb3BhZ2F0aW9uKCk7XG4gICAgaWYgKGV2ZW50LnByb3Bvc2VkQWN0aW9uID09PSAnbm9uZScpIHtcbiAgICAgIGV2ZW50LmRyb3BBY3Rpb24gPSAnbm9uZSc7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIGNvbnN0IG9mZnNldCA9IHRoaXMuZWRpdG9yLmdldE9mZnNldEF0KHBvc2l0aW9uKTtcbiAgICB0aGlzLm1vZGVsLnZhbHVlLmluc2VydChvZmZzZXQsIGRhdGEpO1xuICB9XG59XG5cbi8qKlxuICogVGhlIG5hbWVzcGFjZSBmb3IgdGhlIGBDb2RlRWRpdG9yV3JhcHBlcmAgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBDb2RlRWRpdG9yV3JhcHBlciB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGluaXRpYWxpemUgYSBjb2RlIGVkaXRvciB3aWRnZXQuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBBIGNvZGUgZWRpdG9yIGZhY3RvcnkuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhlIHdpZGdldCBuZWVkcyBhIGZhY3RvcnkgYW5kIGEgbW9kZWwgaW5zdGVhZCBvZiBhIGBDb2RlRWRpdG9yLklFZGl0b3JgXG4gICAgICogb2JqZWN0IGJlY2F1c2UgaXQgbmVlZHMgdG8gcHJvdmlkZSBpdHMgb3duIG5vZGUgYXMgdGhlIGhvc3QuXG4gICAgICovXG4gICAgZmFjdG9yeTogQ29kZUVkaXRvci5GYWN0b3J5O1xuXG4gICAgLyoqXG4gICAgICogVGhlIG1vZGVsIHVzZWQgdG8gaW5pdGlhbGl6ZSB0aGUgY29kZSBlZGl0b3IuXG4gICAgICovXG4gICAgbW9kZWw6IENvZGVFZGl0b3IuSU1vZGVsO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGRlc2lyZWQgdXVpZCBmb3IgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICB1dWlkPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBmb3IgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBjb25maWc/OiBQYXJ0aWFsPENvZGVFZGl0b3IuSUNvbmZpZz47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZGVmYXVsdCBzZWxlY3Rpb24gc3R5bGUgZm9yIHRoZSBlZGl0b3IuXG4gICAgICovXG4gICAgc2VsZWN0aW9uU3R5bGU/OiBDb2RlRWRpdG9yLklTZWxlY3Rpb25TdHlsZTtcbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGZ1bmN0aW9uYWxpdHkuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEdpdmVuIGEgTWltZURhdGEgaW5zdGFuY2UsIGV4dHJhY3QgdGhlIGZpcnN0IHRleHQgZGF0YSwgaWYgYW55LlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGZpbmRUZXh0RGF0YShtaW1lOiBNaW1lRGF0YSk6IHN0cmluZyB8IHVuZGVmaW5lZCB7XG4gICAgY29uc3QgdHlwZXMgPSBtaW1lLnR5cGVzKCk7XG4gICAgY29uc3QgdGV4dFR5cGUgPSB0eXBlcy5maW5kKHQgPT4gdC5pbmRleE9mKCd0ZXh0JykgPT09IDApO1xuICAgIGlmICh0ZXh0VHlwZSA9PT0gdW5kZWZpbmVkKSB7XG4gICAgICByZXR1cm4gdW5kZWZpbmVkO1xuICAgIH1cbiAgICByZXR1cm4gbWltZS5nZXREYXRhKHRleHRUeXBlKSBhcyBzdHJpbmc7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==