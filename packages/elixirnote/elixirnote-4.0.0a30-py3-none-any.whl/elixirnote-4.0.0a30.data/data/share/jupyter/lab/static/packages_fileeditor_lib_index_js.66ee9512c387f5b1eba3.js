"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_fileeditor_lib_index_js"],{

/***/ "../../packages/fileeditor/lib/fileeditorlspadapter.js":
/*!*************************************************************!*\
  !*** ../../packages/fileeditor/lib/fileeditorlspadapter.js ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FileEditorAdapter": () => (/* binding */ FileEditorAdapter)
/* harmony export */ });
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/lsp */ "webpack/sharing/consume/default/@jupyterlab/lsp/@jupyterlab/lsp");
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
var __rest = (undefined && undefined.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};

class FileEditorAdapter extends _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.WidgetLSPAdapter {
    constructor(editorWidget, options) {
        const { docRegistry } = options, others = __rest(options, ["docRegistry"]);
        super(editorWidget, others);
        this.editor = editorWidget.content;
        this._docRegistry = docRegistry;
        this.ready = new Promise((resolve, reject) => {
            this.initOnceReady().then(resolve).catch(reject);
        });
        // Dispose the adapter when the editor is disposed.
        editorWidget.disposed.connect(() => this.dispose());
    }
    /**
     * Get current path of the document.
     */
    get documentPath() {
        return this.widget.context.path;
    }
    /**
     * Get the mime type of the document.
     */
    get mimeType() {
        const codeMirrorMimeType = this.editor.model.mimeType;
        const contentsModel = this.editor.context.contentsModel;
        // when MIME type is not known it defaults to 'text/plain',
        // so if it is different we can accept it as it is
        if (codeMirrorMimeType != 'text/plain') {
            return codeMirrorMimeType;
        }
        else if (contentsModel) {
            // a script that does not have a MIME type known by the editor
            // (no syntax highlight mode), can still be known by the document
            // registry (and this is arguably easier to extend).
            let fileType = this._docRegistry.getFileTypeForModel(contentsModel);
            return fileType.mimeTypes[0];
        }
        else {
            // "text/plain" this is
            return codeMirrorMimeType;
        }
    }
    /**
     * Get the file extension of the document.
     */
    get languageFileExtension() {
        let parts = this.documentPath.split('.');
        return parts[parts.length - 1];
    }
    /**
     * Get the CM editor
     */
    get ceEditor() {
        return this.editor.editor;
    }
    /**
     * Get the activated CM editor.
     */
    get activeEditor() {
        return this.editor.editor;
    }
    /**
     * Get the inner HTMLElement of the document widget.
     */
    get wrapperElement() {
        return this.widget.node;
    }
    /**
     * Get current path of the document.
     */
    get path() {
        return this.widget.context.path;
    }
    /**
     *  Get the list of CM editors in the document, there is only one editor
     * in the case of file editor.
     */
    get editors() {
        return [{ ceEditor: this.editor.editor, type: 'code' }];
    }
    /**
     * Generate the virtual document associated with the document.
     */
    createVirtualDocument() {
        return new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.VirtualDocument({
            language: this.language,
            foreignCodeExtractors: this.options.foreignCodeExtractorsManager,
            path: this.documentPath,
            fileExtension: this.languageFileExtension,
            // notebooks are continuous, each cell is dependent on the previous one
            standalone: true,
            // notebooks are not supported by LSP servers
            hasLspSupportedFile: true
        });
    }
    /**
     * Get the index of editor from the cursor position in the virtual
     * document. Since there is only one editor, this method always return
     * 0
     *
     * @param position - the position of cursor in the virtual document.
     * @return  {number} - index of the virtual editor
     */
    getEditorIndexAt(position) {
        return 0;
    }
    /**
     * Get the index of input editor
     *
     * @param ceEditor - instance of the code editor
     */
    getEditorIndex(ceEditor) {
        return 0;
    }
    /**
     * Get the wrapper of input editor.
     *
     * @param ceEditor
     * @return  {HTMLElement}
     */
    getEditorWrapper(ceEditor) {
        return this.wrapperElement;
    }
    /**
     * Initialization function called once the editor and the LSP connection
     * manager is ready. This function will create the virtual document and
     * connect various signals.
     */
    async initOnceReady() {
        if (!this.editor.context.isReady) {
            await this.editor.context.ready;
        }
        await this.connectionManager.ready;
        this.initVirtual();
        // connect the document, but do not open it as the adapter will handle this
        // after registering all features
        this.connectDocument(this.virtualDocument, false).catch(console.warn);
        this.editor.model.mimeTypeChanged.connect(this.reloadConnection, this);
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/index.js":
/*!**********************************************!*\
  !*** ../../packages/fileeditor/lib/index.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EditorTableOfContentsFactory": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.EditorTableOfContentsFactory),
/* harmony export */   "FileEditor": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_5__.FileEditor),
/* harmony export */   "FileEditorAdapter": () => (/* reexport safe */ _fileeditorlspadapter__WEBPACK_IMPORTED_MODULE_0__.FileEditorAdapter),
/* harmony export */   "FileEditorFactory": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_5__.FileEditorFactory),
/* harmony export */   "FileEditorSearchProvider": () => (/* reexport safe */ _searchprovider__WEBPACK_IMPORTED_MODULE_1__.FileEditorSearchProvider),
/* harmony export */   "IEditorTracker": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.IEditorTracker),
/* harmony export */   "LaTeXTableOfContentsFactory": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.LaTeXTableOfContentsFactory),
/* harmony export */   "LaTeXTableOfContentsModel": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.LaTeXTableOfContentsModel),
/* harmony export */   "MarkdownTableOfContentsFactory": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.MarkdownTableOfContentsFactory),
/* harmony export */   "MarkdownTableOfContentsModel": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.MarkdownTableOfContentsModel),
/* harmony export */   "PythonTableOfContentsFactory": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.PythonTableOfContentsFactory),
/* harmony export */   "PythonTableOfContentsModel": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_3__.PythonTableOfContentsModel),
/* harmony export */   "TabSpaceStatus": () => (/* reexport safe */ _tabspacestatus__WEBPACK_IMPORTED_MODULE_2__.TabSpaceStatus)
/* harmony export */ });
/* harmony import */ var _fileeditorlspadapter__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./fileeditorlspadapter */ "../../packages/fileeditor/lib/fileeditorlspadapter.js");
/* harmony import */ var _searchprovider__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./searchprovider */ "../../packages/fileeditor/lib/searchprovider.js");
/* harmony import */ var _tabspacestatus__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./tabspacestatus */ "../../packages/fileeditor/lib/tabspacestatus.js");
/* harmony import */ var _toc__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./toc */ "../../packages/fileeditor/lib/toc/index.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./tokens */ "../../packages/fileeditor/lib/tokens.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./widget */ "../../packages/fileeditor/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module fileeditor
 */








/***/ }),

/***/ "../../packages/fileeditor/lib/searchprovider.js":
/*!*******************************************************!*\
  !*** ../../packages/fileeditor/lib/searchprovider.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FileEditorSearchProvider": () => (/* binding */ FileEditorSearchProvider)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widget */ "../../packages/fileeditor/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * File editor search provider
 */
class FileEditorSearchProvider extends _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__.CodeMirrorSearchProvider {
    /**
     * Constructor
     * @param widget File editor panel
     */
    constructor(widget) {
        super(widget.content.editor);
    }
    /**
     * Instantiate a search provider for the widget.
     *
     * #### Notes
     * The widget provided is always checked using `isApplicable` before calling
     * this factory.
     *
     * @param widget The widget to search on
     * @param translator [optional] The translator object
     *
     * @returns The search provider on the widget
     */
    static createNew(widget, translator) {
        return new FileEditorSearchProvider(widget);
    }
    /**
     * Report whether or not this provider has the ability to search on the given object
     */
    static isApplicable(domain) {
        return (domain instanceof _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.MainAreaWidget &&
            domain.content instanceof _widget__WEBPACK_IMPORTED_MODULE_2__.FileEditor &&
            domain.content.editor instanceof _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__.CodeMirrorEditor);
    }
    /**
     * Get an initial query value if applicable so that it can be entered
     * into the search box as an initial query
     *
     * @returns Initial value used to populate the search box.
     */
    getInitialQuery() {
        const cm = this.editor;
        const selection = cm.state.sliceDoc(cm.state.selection.main.from, cm.state.selection.main.to);
        // if there are newlines, just return empty string
        return selection.search(/\r?\n|\r/g) === -1 ? selection : '';
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/tabspacestatus.js":
/*!*******************************************************!*\
  !*** ../../packages/fileeditor/lib/tabspacestatus.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TabSpaceStatus": () => (/* binding */ TabSpaceStatus)
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
 * A pure functional component for rendering the TabSpace status.
 */
function TabSpaceComponent(props) {
    const translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
    const trans = translator.load('jupyterlab');
    const description = props.isSpaces
        ? trans.__('Spaces')
        : trans.__('Tab Size');
    return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.TextItem, { onClick: props.handleClick, source: `${description}: ${props.tabSpace}`, title: trans.__('Change Tab indentation…') }));
}
/**
 * A VDomRenderer for a tabs vs. spaces status item.
 */
class TabSpaceStatus extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomRenderer {
    /**
     * Create a new tab/space status item.
     */
    constructor(options) {
        super(new TabSpaceStatus.Model());
        this._popup = null;
        this._menu = options.menu;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this.addClass(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.interactiveItem);
    }
    /**
     * Render the TabSpace status item.
     */
    render() {
        if (!this.model || !this.model.config) {
            return null;
        }
        else {
            return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(TabSpaceComponent, { isSpaces: this.model.config.insertSpaces, tabSpace: this.model.config.tabSize, handleClick: () => this._handleClick(), translator: this.translator }));
        }
    }
    /**
     * Handle a click on the status item.
     */
    _handleClick() {
        const menu = this._menu;
        if (this._popup) {
            this._popup.dispose();
        }
        menu.aboutToClose.connect(this._menuClosed, this);
        this._popup = (0,_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.showPopup)({
            body: menu,
            anchor: this,
            align: 'right'
        });
    }
    _menuClosed() {
        this.removeClass(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_0__.clickedItem);
    }
}
/**
 * A namespace for TabSpace statics.
 */
(function (TabSpaceStatus) {
    /**
     * A VDomModel for the TabSpace status item.
     */
    class Model extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.VDomModel {
        constructor() {
            super(...arguments);
            this._config = null;
        }
        /**
         * The editor config from the settings system.
         */
        get config() {
            return this._config;
        }
        set config(val) {
            const oldConfig = this._config;
            this._config = val;
            this._triggerChange(oldConfig, this._config);
        }
        _triggerChange(oldValue, newValue) {
            const oldSpaces = oldValue && oldValue.insertSpaces;
            const oldSize = oldValue && oldValue.tabSize;
            const newSpaces = newValue && newValue.insertSpaces;
            const newSize = newValue && newValue.tabSize;
            if (oldSpaces !== newSpaces || oldSize !== newSize) {
                this.stateChanged.emit(void 0);
            }
        }
    }
    TabSpaceStatus.Model = Model;
})(TabSpaceStatus || (TabSpaceStatus = {}));


/***/ }),

/***/ "../../packages/fileeditor/lib/toc/factory.js":
/*!****************************************************!*\
  !*** ../../packages/fileeditor/lib/toc/factory.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EditorTableOfContentsFactory": () => (/* binding */ EditorTableOfContentsFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Base table of contents model factory for file editor
 */
class EditorTableOfContentsFactory extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsFactory {
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    createNew(widget, configuration) {
        const model = super.createNew(widget, configuration);
        const onActiveHeadingChanged = (model, heading) => {
            if (heading) {
                widget.content.editor.setCursorPosition({
                    line: heading.line,
                    column: 0
                });
            }
        };
        model.activeHeadingChanged.connect(onActiveHeadingChanged);
        widget.disposed.connect(() => {
            model.activeHeadingChanged.disconnect(onActiveHeadingChanged);
        });
        return model;
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/toc/index.js":
/*!**************************************************!*\
  !*** ../../packages/fileeditor/lib/toc/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EditorTableOfContentsFactory": () => (/* reexport safe */ _factory__WEBPACK_IMPORTED_MODULE_0__.EditorTableOfContentsFactory),
/* harmony export */   "LaTeXTableOfContentsFactory": () => (/* reexport safe */ _latex__WEBPACK_IMPORTED_MODULE_1__.LaTeXTableOfContentsFactory),
/* harmony export */   "LaTeXTableOfContentsModel": () => (/* reexport safe */ _latex__WEBPACK_IMPORTED_MODULE_1__.LaTeXTableOfContentsModel),
/* harmony export */   "MarkdownTableOfContentsFactory": () => (/* reexport safe */ _markdown__WEBPACK_IMPORTED_MODULE_2__.MarkdownTableOfContentsFactory),
/* harmony export */   "MarkdownTableOfContentsModel": () => (/* reexport safe */ _markdown__WEBPACK_IMPORTED_MODULE_2__.MarkdownTableOfContentsModel),
/* harmony export */   "PythonTableOfContentsFactory": () => (/* reexport safe */ _python__WEBPACK_IMPORTED_MODULE_3__.PythonTableOfContentsFactory),
/* harmony export */   "PythonTableOfContentsModel": () => (/* reexport safe */ _python__WEBPACK_IMPORTED_MODULE_3__.PythonTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./factory */ "../../packages/fileeditor/lib/toc/factory.js");
/* harmony import */ var _latex__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./latex */ "../../packages/fileeditor/lib/toc/latex.js");
/* harmony import */ var _markdown__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./markdown */ "../../packages/fileeditor/lib/toc/markdown.js");
/* harmony import */ var _python__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./python */ "../../packages/fileeditor/lib/toc/python.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.






/***/ }),

/***/ "../../packages/fileeditor/lib/toc/latex.js":
/*!**************************************************!*\
  !*** ../../packages/fileeditor/lib/toc/latex.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LaTeXTableOfContentsFactory": () => (/* binding */ LaTeXTableOfContentsFactory),
/* harmony export */   "LaTeXTableOfContentsModel": () => (/* binding */ LaTeXTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./factory */ "../../packages/fileeditor/lib/toc/factory.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * Maps LaTeX section headings to HTML header levels.
 *
 * ## Notes
 *
 * -   As `part` and `chapter` section headings appear to be less common, assign them to heading level 1.
 *
 * @private
 */
const LATEX_LEVELS = {
    part: 1,
    chapter: 1,
    section: 1,
    subsection: 2,
    subsubsection: 3,
    paragraph: 4,
    subparagraph: 5
};
/**
 * Regular expression to create the outline
 */
const SECTIONS = /^\s*\\(section|subsection|subsubsection){(.+)}/;
/**
 * Table of content model for LaTeX files.
 */
class LaTeXTableOfContentsModel extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsModel {
    /**
     * Type of document supported by the model.
     *
     * #### Notes
     * A `data-document-type` attribute with this value will be set
     * on the tree view `.jp-TableOfContents-content[data-document-type="..."]`
     */
    get documentType() {
        return 'latex';
    }
    /**
     * List of configuration options supported by the model.
     */
    get supportedOptions() {
        return ['maximalDepth', 'numberHeaders'];
    }
    /**
     * Produce the headings for a document.
     *
     * @returns The list of new headings or `null` if nothing needs to be updated.
     */
    getHeadings() {
        if (!this.isActive) {
            return Promise.resolve(null);
        }
        // Split the text into lines:
        const lines = this.widget.content.model.value.text.split('\n');
        const levels = new Array();
        let previousLevel = levels.length;
        const headings = new Array();
        for (let i = 0; i < lines.length; i++) {
            const match = lines[i].match(SECTIONS);
            if (match) {
                const level = LATEX_LEVELS[match[1]];
                if (level <= this.configuration.maximalDepth) {
                    const prefix = _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.getPrefix(level, previousLevel, levels, Object.assign(Object.assign({}, this.configuration), { 
                        // Force base numbering and numbering first level
                        baseNumbering: 1, numberingH1: true }));
                    previousLevel = level;
                    headings.push({
                        text: match[2],
                        prefix: prefix,
                        level,
                        line: i
                    });
                }
            }
        }
        return Promise.resolve(headings);
    }
}
/**
 * Table of content model factory for LaTeX files.
 */
class LaTeXTableOfContentsFactory extends _factory__WEBPACK_IMPORTED_MODULE_1__.EditorTableOfContentsFactory {
    /**
     * Whether the factory can handle the widget or not.
     *
     * @param widget - widget
     * @returns boolean indicating a ToC can be generated
     */
    isApplicable(widget) {
        var _a, _b;
        const isApplicable = super.isApplicable(widget);
        if (isApplicable) {
            let mime = (_b = (_a = widget.content) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.mimeType;
            return mime && (mime === 'text/x-latex' || mime === 'text/x-stex');
        }
        return false;
    }
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    _createNew(widget, configuration) {
        return new LaTeXTableOfContentsModel(widget, configuration);
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/toc/markdown.js":
/*!*****************************************************!*\
  !*** ../../packages/fileeditor/lib/toc/markdown.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MarkdownTableOfContentsFactory": () => (/* binding */ MarkdownTableOfContentsFactory),
/* harmony export */   "MarkdownTableOfContentsModel": () => (/* binding */ MarkdownTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./factory */ "../../packages/fileeditor/lib/toc/factory.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * Table of content model for Markdown files.
 */
class MarkdownTableOfContentsModel extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsModel {
    /**
     * Type of document supported by the model.
     *
     * #### Notes
     * A `data-document-type` attribute with this value will be set
     * on the tree view `.jp-TableOfContents-content[data-document-type="..."]`
     */
    get documentType() {
        return 'markdown';
    }
    /**
     * Produce the headings for a document.
     *
     * @returns The list of new headings or `null` if nothing needs to be updated.
     */
    getHeadings() {
        if (!this.isActive) {
            return Promise.resolve(null);
        }
        const content = this.widget.content.model.value.text;
        const headings = _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.Markdown.getHeadings(content, Object.assign(Object.assign({}, this.configuration), { 
            // Force removing numbering as they cannot be displayed
            // in the document
            numberHeaders: false }));
        return Promise.resolve(headings);
    }
}
/**
 * Table of content model factory for Markdown files.
 */
class MarkdownTableOfContentsFactory extends _factory__WEBPACK_IMPORTED_MODULE_1__.EditorTableOfContentsFactory {
    /**
     * Whether the factory can handle the widget or not.
     *
     * @param widget - widget
     * @returns boolean indicating a ToC can be generated
     */
    isApplicable(widget) {
        var _a, _b;
        const isApplicable = super.isApplicable(widget);
        if (isApplicable) {
            let mime = (_b = (_a = widget.content) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.mimeType;
            return mime && _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.Markdown.isMarkdown(mime);
        }
        return false;
    }
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    _createNew(widget, configuration) {
        return new MarkdownTableOfContentsModel(widget, configuration);
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/toc/python.js":
/*!***************************************************!*\
  !*** ../../packages/fileeditor/lib/toc/python.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "PythonTableOfContentsFactory": () => (/* binding */ PythonTableOfContentsFactory),
/* harmony export */   "PythonTableOfContentsModel": () => (/* binding */ PythonTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./factory */ "../../packages/fileeditor/lib/toc/factory.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * Regular expression to create the outline
 */
let KEYWORDS;
try {
    // https://github.com/tc39/proposal-regexp-match-indices was accepted
    // in May 2021 (https://github.com/tc39/proposals/blob/main/finished-proposals.md)
    // So we will fallback to the polyfill regexp-match-indices if not available
    KEYWORDS = new RegExp('^\\s*(class |def |from |import )', 'd');
}
catch (_a) {
    KEYWORDS = new RegExp('^\\s*(class |def |from |import )');
}
/**
 * Table of content model for Python files.
 */
class PythonTableOfContentsModel extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsModel {
    /**
     * Type of document supported by the model.
     *
     * #### Notes
     * A `data-document-type` attribute with this value will be set
     * on the tree view `.jp-TableOfContents-content[data-document-type="..."]`
     */
    get documentType() {
        return 'python';
    }
    /**
     * Produce the headings for a document.
     *
     * @returns The list of new headings or `null` if nothing needs to be updated.
     */
    async getHeadings() {
        if (!this.isActive) {
            return Promise.resolve(null);
        }
        // Split the text into lines:
        const lines = this.widget.content.model.value.text.split('\n');
        // Iterate over the lines to get the heading level and text for each line:
        let headings = new Array();
        let processingImports = false;
        let indent = 1;
        let lineIdx = -1;
        for (const line of lines) {
            lineIdx++;
            let hasKeyword;
            if (KEYWORDS.flags.includes('d')) {
                hasKeyword = KEYWORDS.exec(line);
            }
            else {
                const { default: execWithIndices } = await __webpack_require__.e(/*! import() */ "vendors-node_modules_regexp-match-indices_index_js").then(__webpack_require__.t.bind(__webpack_require__, /*! regexp-match-indices */ "../../node_modules/regexp-match-indices/index.js", 23));
                hasKeyword = execWithIndices(KEYWORDS, line);
            }
            if (hasKeyword) {
                // Index 0 contains the spaces, index 1 is the keyword group
                const [start] = hasKeyword.indices[1];
                if (indent === 1 && start > 0) {
                    indent = start;
                }
                const isImport = ['from ', 'import '].includes(hasKeyword[1]);
                if (isImport && processingImports) {
                    continue;
                }
                processingImports = isImport;
                const level = 1 + start / indent;
                if (level > this.configuration.maximalDepth) {
                    continue;
                }
                headings.push({
                    text: line.slice(start),
                    level,
                    line: lineIdx
                });
            }
        }
        return Promise.resolve(headings);
    }
}
/**
 * Table of content model factory for Python files.
 */
class PythonTableOfContentsFactory extends _factory__WEBPACK_IMPORTED_MODULE_1__.EditorTableOfContentsFactory {
    /**
     * Whether the factory can handle the widget or not.
     *
     * @param widget - widget
     * @returns boolean indicating a ToC can be generated
     */
    isApplicable(widget) {
        var _a, _b;
        const isApplicable = super.isApplicable(widget);
        if (isApplicable) {
            let mime = (_b = (_a = widget.content) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.mimeType;
            return (mime &&
                (mime === 'application/x-python-code' || mime === 'text/x-python'));
        }
        return false;
    }
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    _createNew(widget, configuration) {
        return new PythonTableOfContentsModel(widget, configuration);
    }
}


/***/ }),

/***/ "../../packages/fileeditor/lib/tokens.js":
/*!***********************************************!*\
  !*** ../../packages/fileeditor/lib/tokens.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IEditorTracker": () => (/* binding */ IEditorTracker)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The editor tracker token.
 */
const IEditorTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/fileeditor:IEditorTracker');


/***/ }),

/***/ "../../packages/fileeditor/lib/widget.js":
/*!***********************************************!*\
  !*** ../../packages/fileeditor/lib/widget.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FileEditor": () => (/* binding */ FileEditor),
/* harmony export */   "FileEditorFactory": () => (/* binding */ FileEditorFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





/**
 * The data attribute added to a widget that can run code.
 */
const CODE_RUNNER = 'jpCodeRunner';
/**
 * The data attribute added to a widget that can undo.
 */
const UNDOER = 'jpUndoer';
/**
 * A widget for editors.
 */
class FileEditor extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__.Widget {
    /**
     * Construct a new editor widget.
     */
    constructor(options) {
        super();
        this._ready = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_3__.PromiseDelegate();
        this.addClass('jp-FileEditor');
        const context = (this._context = options.context);
        this._mimeTypeService = options.mimeTypeService;
        const editorWidget = (this._editorWidget = new _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_0__.CodeEditorWrapper({
            factory: options.factory,
            model: context.model
        }));
        this._editorWidget.addClass('jp-FileEditorCodeWrapper');
        this._editorWidget.node.dataset[CODE_RUNNER] = 'true';
        this._editorWidget.node.dataset[UNDOER] = 'true';
        this.editor = editorWidget.editor;
        this.model = editorWidget.model;
        void context.ready.then(() => {
            this._onContextReady();
        });
        // Listen for changes to the path.
        context.pathChanged.connect(this._onPathChanged, this);
        this._onPathChanged();
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__.StackedLayout());
        layout.addWidget(editorWidget);
    }
    /**
     * Get the context for the editor widget.
     */
    get context() {
        return this._context;
    }
    /**
     * A promise that resolves when the file editor is ready.
     */
    get ready() {
        return this.ready;
    }
    /**
     * Handle the DOM events for the widget.
     *
     * @param event - The DOM event sent to the widget.
     *
     * #### Notes
     * This method implements the DOM `EventListener` interface and is
     * called in response to events on the widget's node. It should
     * not be called directly by user code.
     */
    handleEvent(event) {
        if (!this.model) {
            return;
        }
        switch (event.type) {
            case 'mousedown':
                this._ensureFocus();
                break;
            default:
                break;
        }
    }
    /**
     * Handle `after-attach` messages for the widget.
     */
    onAfterAttach(msg) {
        super.onAfterAttach(msg);
        const node = this.node;
        node.addEventListener('mousedown', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        const node = this.node;
        node.removeEventListener('mousedown', this);
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this._ensureFocus();
    }
    /**
     * Ensure that the widget has focus.
     */
    _ensureFocus() {
        if (!this.editor.hasFocus()) {
            this.editor.focus();
        }
    }
    /**
     * Handle actions that should be taken when the context is ready.
     */
    _onContextReady() {
        if (this.isDisposed) {
            return;
        }
        // Prevent the initial loading from disk from being in the editor history.
        this.editor.clearHistory();
        // Resolve the ready promise.
        this._ready.resolve(undefined);
    }
    /**
     * Handle a change to the path.
     */
    _onPathChanged() {
        const editor = this.editor;
        const localPath = this._context.localPath;
        editor.model.mimeType =
            this._mimeTypeService.getMimeTypeByFilePath(localPath);
    }
}
/**
 * A widget factory for editors.
 */
class FileEditorFactory extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.ABCWidgetFactory {
    /**
     * Construct a new editor widget factory.
     */
    constructor(options) {
        super(options.factoryOptions);
        this._services = options.editorServices;
    }
    /**
     * Create a new widget given a context.
     */
    createNewWidget(context) {
        const func = this._services.factoryService.newDocumentEditor;
        const factory = options => {
            return func(options);
        };
        const content = new FileEditor({
            factory,
            context,
            mimeTypeService: this._services.mimeTypeService
        });
        content.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.textEditorIcon;
        const widget = new _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.DocumentWidget({ content, context });
        return widget;
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZmlsZWVkaXRvcl9saWJfaW5kZXhfanMuNjZlZTk1MTJjMzg3ZjViMWViYTMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDs7Ozs7Ozs7Ozs7O0FBVWxDO0FBV2xCLE1BQU0saUJBQWtCLFNBQVEsNkRBRXRDO0lBQ0MsWUFDRSxZQUF5QyxFQUN6QyxPQUFrQztRQUVsQyxNQUFNLEVBQUUsV0FBVyxLQUFnQixPQUFPLEVBQWxCLE1BQU0sVUFBSyxPQUFPLEVBQXBDLGVBQTBCLENBQVUsQ0FBQztRQUMzQyxLQUFLLENBQUMsWUFBWSxFQUFFLE1BQU0sQ0FBQyxDQUFDO1FBQzVCLElBQUksQ0FBQyxNQUFNLEdBQUcsWUFBWSxDQUFDLE9BQU8sQ0FBQztRQUNuQyxJQUFJLENBQUMsWUFBWSxHQUFHLFdBQVcsQ0FBQztRQUNoQyxJQUFJLENBQUMsS0FBSyxHQUFHLElBQUksT0FBTyxDQUFPLENBQUMsT0FBTyxFQUFFLE1BQU0sRUFBRSxFQUFFO1lBQ2pELElBQUksQ0FBQyxhQUFhLEVBQUUsQ0FBQyxJQUFJLENBQUMsT0FBTyxDQUFDLENBQUMsS0FBSyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQ25ELENBQUMsQ0FBQyxDQUFDO1FBRUgsbURBQW1EO1FBQ25ELFlBQVksQ0FBQyxRQUFRLENBQUMsT0FBTyxDQUFDLEdBQUcsRUFBRSxDQUFDLElBQUksQ0FBQyxPQUFPLEVBQUUsQ0FBQyxDQUFDO0lBQ3RELENBQUM7SUFPRDs7T0FFRztJQUNILElBQUksWUFBWTtRQUNkLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDO0lBQ2xDLENBQUM7SUFFRDs7T0FFRztJQUNILElBQUksUUFBUTtRQUNWLE1BQU0sa0JBQWtCLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUFDO1FBQ3RELE1BQU0sYUFBYSxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLGFBQWEsQ0FBQztRQUV4RCwyREFBMkQ7UUFDM0Qsa0RBQWtEO1FBQ2xELElBQUksa0JBQWtCLElBQUksWUFBWSxFQUFFO1lBQ3RDLE9BQU8sa0JBQWtCLENBQUM7U0FDM0I7YUFBTSxJQUFJLGFBQWEsRUFBRTtZQUN4Qiw4REFBOEQ7WUFDOUQsaUVBQWlFO1lBQ2pFLG9EQUFvRDtZQUNwRCxJQUFJLFFBQVEsR0FBRyxJQUFJLENBQUMsWUFBWSxDQUFDLG1CQUFtQixDQUFDLGFBQWEsQ0FBQyxDQUFDO1lBQ3BFLE9BQU8sUUFBUSxDQUFDLFNBQVMsQ0FBQyxDQUFDLENBQUMsQ0FBQztTQUM5QjthQUFNO1lBQ0wsdUJBQXVCO1lBQ3ZCLE9BQU8sa0JBQWtCLENBQUM7U0FDM0I7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxJQUFJLHFCQUFxQjtRQUN2QixJQUFJLEtBQUssR0FBRyxJQUFJLENBQUMsWUFBWSxDQUFDLEtBQUssQ0FBQyxHQUFHLENBQUMsQ0FBQztRQUN6QyxPQUFPLEtBQUssQ0FBQyxLQUFLLENBQUMsTUFBTSxHQUFHLENBQUMsQ0FBQyxDQUFDO0lBQ2pDLENBQUM7SUFFRDs7T0FFRztJQUNILElBQUksUUFBUTtRQUNWLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxNQUEwQixDQUFDO0lBQ2hELENBQUM7SUFFRDs7T0FFRztJQUNILElBQUksWUFBWTtRQUNkLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxNQUFNLENBQUM7SUFDNUIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxjQUFjO1FBQ2hCLE9BQU8sSUFBSSxDQUFDLE1BQU0sQ0FBQyxJQUFJLENBQUM7SUFDMUIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxJQUFJO1FBQ04sT0FBTyxJQUFJLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUM7SUFDbEMsQ0FBQztJQUVEOzs7T0FHRztJQUNILElBQUksT0FBTztRQUNULE9BQU8sQ0FBQyxFQUFFLFFBQVEsRUFBRSxJQUFJLENBQUMsTUFBTSxDQUFDLE1BQU0sRUFBRSxJQUFJLEVBQUUsTUFBTSxFQUFFLENBQUMsQ0FBQztJQUMxRCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxxQkFBcUI7UUFDbkIsT0FBTyxJQUFJLDREQUFlLENBQUM7WUFDekIsUUFBUSxFQUFFLElBQUksQ0FBQyxRQUFRO1lBQ3ZCLHFCQUFxQixFQUFFLElBQUksQ0FBQyxPQUFPLENBQUMsNEJBQTRCO1lBQ2hFLElBQUksRUFBRSxJQUFJLENBQUMsWUFBWTtZQUN2QixhQUFhLEVBQUUsSUFBSSxDQUFDLHFCQUFxQjtZQUN6Qyx1RUFBdUU7WUFDdkUsVUFBVSxFQUFFLElBQUk7WUFDaEIsNkNBQTZDO1lBQzdDLG1CQUFtQixFQUFFLElBQUk7U0FDMUIsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQUVEOzs7Ozs7O09BT0c7SUFDSCxnQkFBZ0IsQ0FBQyxRQUEwQjtRQUN6QyxPQUFPLENBQUMsQ0FBQztJQUNYLENBQUM7SUFFRDs7OztPQUlHO0lBQ0gsY0FBYyxDQUFDLFFBQTRCO1FBQ3pDLE9BQU8sQ0FBQyxDQUFDO0lBQ1gsQ0FBQztJQUVEOzs7OztPQUtHO0lBQ0gsZ0JBQWdCLENBQUMsUUFBNEI7UUFDM0MsT0FBTyxJQUFJLENBQUMsY0FBYyxDQUFDO0lBQzdCLENBQUM7SUFFRDs7OztPQUlHO0lBQ08sS0FBSyxDQUFDLGFBQWE7UUFDM0IsSUFBSSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLE9BQU8sRUFBRTtZQUNoQyxNQUFNLElBQUksQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQztTQUNqQztRQUNELE1BQU0sSUFBSSxDQUFDLGlCQUFpQixDQUFDLEtBQUssQ0FBQztRQUNuQyxJQUFJLENBQUMsV0FBVyxFQUFFLENBQUM7UUFFbkIsMkVBQTJFO1FBQzNFLGlDQUFpQztRQUNqQyxJQUFJLENBQUMsZUFBZSxDQUFDLElBQUksQ0FBQyxlQUFlLEVBQUUsS0FBSyxDQUFDLENBQUMsS0FBSyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUV0RSxJQUFJLENBQUMsTUFBTSxDQUFDLEtBQUssQ0FBQyxlQUFlLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxnQkFBZ0IsRUFBRSxJQUFJLENBQUMsQ0FBQztJQUN6RSxDQUFDO0NBTUY7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQzlMRCwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQUVvQztBQUNOO0FBQ0E7QUFDWDtBQUNHO0FBQ0E7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDWnpCLDBDQUEwQztBQUMxQywyREFBMkQ7QUFFTDtBQUl0QjtBQUlNO0FBT3RDOztHQUVHO0FBQ0ksTUFBTSx3QkFDWCxTQUFRLDRFQUF3QjtJQUdoQzs7O09BR0c7SUFDSCxZQUFZLE1BQXVCO1FBQ2pDLEtBQUssQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLE1BQTBCLENBQUMsQ0FBQztJQUNuRCxDQUFDO0lBRUQ7Ozs7Ozs7Ozs7O09BV0c7SUFDSCxNQUFNLENBQUMsU0FBUyxDQUNkLE1BQXVCLEVBQ3ZCLFVBQXdCO1FBRXhCLE9BQU8sSUFBSSx3QkFBd0IsQ0FBQyxNQUFNLENBQUMsQ0FBQztJQUM5QyxDQUFDO0lBRUQ7O09BRUc7SUFDSCxNQUFNLENBQUMsWUFBWSxDQUFDLE1BQWM7UUFDaEMsT0FBTyxDQUNMLE1BQU0sWUFBWSxnRUFBYztZQUNoQyxNQUFNLENBQUMsT0FBTyxZQUFZLCtDQUFVO1lBQ3BDLE1BQU0sQ0FBQyxPQUFPLENBQUMsTUFBTSxZQUFZLG9FQUFnQixDQUNsRCxDQUFDO0lBQ0osQ0FBQztJQUVEOzs7OztPQUtHO0lBQ0gsZUFBZTtRQUNiLE1BQU0sRUFBRSxHQUFHLElBQUksQ0FBQyxNQUEwQixDQUFDO1FBQzNDLE1BQU0sU0FBUyxHQUFHLEVBQUUsQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUNqQyxFQUFFLENBQUMsS0FBSyxDQUFDLFNBQVMsQ0FBQyxJQUFJLENBQUMsSUFBSSxFQUM1QixFQUFFLENBQUMsS0FBSyxDQUFDLFNBQVMsQ0FBQyxJQUFJLENBQUMsRUFBRSxDQUMzQixDQUFDO1FBQ0Ysa0RBQWtEO1FBQ2xELE9BQU8sU0FBUyxDQUFDLE1BQU0sQ0FBQyxXQUFXLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUMsU0FBUyxDQUFDLENBQUMsQ0FBQyxFQUFFLENBQUM7SUFDL0QsQ0FBQztDQUNGOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQzlFRCwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBUzVCO0FBQ3VDO0FBQ0Y7QUFFMUM7QUFpQzFCOztHQUVHO0FBQ0gsU0FBUyxpQkFBaUIsQ0FDeEIsS0FBK0I7SUFFL0IsTUFBTSxVQUFVLEdBQUcsS0FBSyxDQUFDLFVBQVUsSUFBSSxtRUFBYyxDQUFDO0lBQ3RELE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFDNUMsTUFBTSxXQUFXLEdBQUcsS0FBSyxDQUFDLFFBQVE7UUFDaEMsQ0FBQyxDQUFDLEtBQUssQ0FBQyxFQUFFLENBQUMsUUFBUSxDQUFDO1FBQ3BCLENBQUMsQ0FBQyxLQUFLLENBQUMsRUFBRSxDQUFDLFVBQVUsQ0FBQyxDQUFDO0lBQ3pCLE9BQU8sQ0FDTCwyREFBQywyREFBUSxJQUNQLE9BQU8sRUFBRSxLQUFLLENBQUMsV0FBVyxFQUMxQixNQUFNLEVBQUUsR0FBRyxXQUFXLEtBQUssS0FBSyxDQUFDLFFBQVEsRUFBRSxFQUMzQyxLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyx5QkFBeUIsQ0FBQyxHQUMxQyxDQUNILENBQUM7QUFDSixDQUFDO0FBRUQ7O0dBRUc7QUFDSSxNQUFNLGNBQWUsU0FBUSxtRUFBa0M7SUFDcEU7O09BRUc7SUFDSCxZQUFZLE9BQWdDO1FBQzFDLEtBQUssQ0FBQyxJQUFJLGNBQWMsQ0FBQyxLQUFLLEVBQUUsQ0FBQyxDQUFDO1FBZ0Q1QixXQUFNLEdBQWlCLElBQUksQ0FBQztRQS9DbEMsSUFBSSxDQUFDLEtBQUssR0FBRyxPQUFPLENBQUMsSUFBSSxDQUFDO1FBQzFCLElBQUksQ0FBQyxVQUFVLEdBQUcsT0FBTyxDQUFDLFVBQVUsSUFBSSxtRUFBYyxDQUFDO1FBQ3ZELElBQUksQ0FBQyxRQUFRLENBQUMsa0VBQWUsQ0FBQyxDQUFDO0lBQ2pDLENBQUM7SUFFRDs7T0FFRztJQUNILE1BQU07UUFDSixJQUFJLENBQUMsSUFBSSxDQUFDLEtBQUssSUFBSSxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsTUFBTSxFQUFFO1lBQ3JDLE9BQU8sSUFBSSxDQUFDO1NBQ2I7YUFBTTtZQUNMLE9BQU8sQ0FDTCwyREFBQyxpQkFBaUIsSUFDaEIsUUFBUSxFQUFFLElBQUksQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLFlBQVksRUFDeEMsUUFBUSxFQUFFLElBQUksQ0FBQyxLQUFLLENBQUMsTUFBTSxDQUFDLE9BQU8sRUFDbkMsV0FBVyxFQUFFLEdBQUcsRUFBRSxDQUFDLElBQUksQ0FBQyxZQUFZLEVBQUUsRUFDdEMsVUFBVSxFQUFFLElBQUksQ0FBQyxVQUFVLEdBQzNCLENBQ0gsQ0FBQztTQUNIO0lBQ0gsQ0FBQztJQUVEOztPQUVHO0lBQ0ssWUFBWTtRQUNsQixNQUFNLElBQUksR0FBRyxJQUFJLENBQUMsS0FBSyxDQUFDO1FBQ3hCLElBQUksSUFBSSxDQUFDLE1BQU0sRUFBRTtZQUNmLElBQUksQ0FBQyxNQUFNLENBQUMsT0FBTyxFQUFFLENBQUM7U0FDdkI7UUFFRCxJQUFJLENBQUMsWUFBWSxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsV0FBVyxFQUFFLElBQUksQ0FBQyxDQUFDO1FBRWxELElBQUksQ0FBQyxNQUFNLEdBQUcsZ0VBQVMsQ0FBQztZQUN0QixJQUFJLEVBQUUsSUFBSTtZQUNWLE1BQU0sRUFBRSxJQUFJO1lBQ1osS0FBSyxFQUFFLE9BQU87U0FDZixDQUFDLENBQUM7SUFDTCxDQUFDO0lBRU8sV0FBVztRQUNqQixJQUFJLENBQUMsV0FBVyxDQUFDLDhEQUFXLENBQUMsQ0FBQztJQUNoQyxDQUFDO0NBS0Y7QUFFRDs7R0FFRztBQUNILFdBQWlCLGNBQWM7SUFDN0I7O09BRUc7SUFDSCxNQUFhLEtBQU0sU0FBUSxnRUFBUztRQUFwQzs7WUEwQlUsWUFBTyxHQUE4QixJQUFJLENBQUM7UUFDcEQsQ0FBQztRQTFCQzs7V0FFRztRQUNILElBQUksTUFBTTtZQUNSLE9BQU8sSUFBSSxDQUFDLE9BQU8sQ0FBQztRQUN0QixDQUFDO1FBQ0QsSUFBSSxNQUFNLENBQUMsR0FBOEI7WUFDdkMsTUFBTSxTQUFTLEdBQUcsSUFBSSxDQUFDLE9BQU8sQ0FBQztZQUMvQixJQUFJLENBQUMsT0FBTyxHQUFHLEdBQUcsQ0FBQztZQUNuQixJQUFJLENBQUMsY0FBYyxDQUFDLFNBQVMsRUFBRSxJQUFJLENBQUMsT0FBTyxDQUFDLENBQUM7UUFDL0MsQ0FBQztRQUVPLGNBQWMsQ0FDcEIsUUFBbUMsRUFDbkMsUUFBbUM7WUFFbkMsTUFBTSxTQUFTLEdBQUcsUUFBUSxJQUFJLFFBQVEsQ0FBQyxZQUFZLENBQUM7WUFDcEQsTUFBTSxPQUFPLEdBQUcsUUFBUSxJQUFJLFFBQVEsQ0FBQyxPQUFPLENBQUM7WUFDN0MsTUFBTSxTQUFTLEdBQUcsUUFBUSxJQUFJLFFBQVEsQ0FBQyxZQUFZLENBQUM7WUFDcEQsTUFBTSxPQUFPLEdBQUcsUUFBUSxJQUFJLFFBQVEsQ0FBQyxPQUFPLENBQUM7WUFDN0MsSUFBSSxTQUFTLEtBQUssU0FBUyxJQUFJLE9BQU8sS0FBSyxPQUFPLEVBQUU7Z0JBQ2xELElBQUksQ0FBQyxZQUFZLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7YUFDaEM7UUFDSCxDQUFDO0tBR0Y7SUEzQlksb0JBQUssUUEyQmpCO0FBaUJILENBQUMsRUFoRGdCLGNBQWMsS0FBZCxjQUFjLFFBZ0Q5Qjs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNqTEQsMENBQTBDO0FBQzFDLDJEQUEyRDtBQU9sQztBQWF6Qjs7R0FFRztBQUNJLE1BQWUsNEJBQTZCLFNBQVEsbUVBRTFEO0lBQ0M7Ozs7OztPQU1HO0lBQ0gsU0FBUyxDQUNQLE1BQTRELEVBQzVELGFBQXVDO1FBS3ZDLE1BQU0sS0FBSyxHQUFHLEtBQUssQ0FBQyxTQUFTLENBQzNCLE1BQU0sRUFDTixhQUFhLENBSWQsQ0FBQztRQUVGLE1BQU0sc0JBQXNCLEdBQUcsQ0FDN0IsS0FHQyxFQUNELE9BQThCLEVBQzlCLEVBQUU7WUFDRixJQUFJLE9BQU8sRUFBRTtnQkFDWCxNQUFNLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxpQkFBaUIsQ0FBQztvQkFDdEMsSUFBSSxFQUFFLE9BQU8sQ0FBQyxJQUFJO29CQUNsQixNQUFNLEVBQUUsQ0FBQztpQkFDVixDQUFDLENBQUM7YUFDSjtRQUNILENBQUMsQ0FBQztRQUVGLEtBQUssQ0FBQyxvQkFBb0IsQ0FBQyxPQUFPLENBQUMsc0JBQXNCLENBQUMsQ0FBQztRQUMzRCxNQUFNLENBQUMsUUFBUSxDQUFDLE9BQU8sQ0FBQyxHQUFHLEVBQUU7WUFDM0IsS0FBSyxDQUFDLG9CQUFvQixDQUFDLFVBQVUsQ0FBQyxzQkFBc0IsQ0FBQyxDQUFDO1FBQ2hFLENBQUMsQ0FBQyxDQUFDO1FBRUgsT0FBTyxLQUFLLENBQUM7SUFDZixDQUFDO0NBQ0Y7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUN2RUQsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVqQztBQUNGO0FBQ0c7QUFDRjs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ056QiwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBT2xDO0FBR2dEO0FBRXpFOzs7Ozs7OztHQVFHO0FBQ0gsTUFBTSxZQUFZLEdBQWdDO0lBQ2hELElBQUksRUFBRSxDQUFDO0lBQ1AsT0FBTyxFQUFFLENBQUM7SUFDVixPQUFPLEVBQUUsQ0FBQztJQUNWLFVBQVUsRUFBRSxDQUFDO0lBQ2IsYUFBYSxFQUFFLENBQUM7SUFDaEIsU0FBUyxFQUFFLENBQUM7SUFDWixZQUFZLEVBQUUsQ0FBQztDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLFFBQVEsR0FBRyxnREFBZ0QsQ0FBQztBQUVsRTs7R0FFRztBQUNJLE1BQU0seUJBQTBCLFNBQVEsaUVBRzlDO0lBQ0M7Ozs7OztPQU1HO0lBQ0gsSUFBSSxZQUFZO1FBQ2QsT0FBTyxPQUFPLENBQUM7SUFDakIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxnQkFBZ0I7UUFDbEIsT0FBTyxDQUFDLGNBQWMsRUFBRSxlQUFlLENBQUMsQ0FBQztJQUMzQyxDQUFDO0lBRUQ7Ozs7T0FJRztJQUNPLFdBQVc7UUFDbkIsSUFBSSxDQUFDLElBQUksQ0FBQyxRQUFRLEVBQUU7WUFDbEIsT0FBTyxPQUFPLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO1NBQzlCO1FBRUQsNkJBQTZCO1FBQzdCLE1BQU0sS0FBSyxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FDdEQsSUFBSSxDQUNZLENBQUM7UUFFbkIsTUFBTSxNQUFNLEdBQUcsSUFBSSxLQUFLLEVBQVUsQ0FBQztRQUNuQyxJQUFJLGFBQWEsR0FBRyxNQUFNLENBQUMsTUFBTSxDQUFDO1FBQ2xDLE1BQU0sUUFBUSxHQUFHLElBQUksS0FBSyxFQUFrQixDQUFDO1FBQzdDLEtBQUssSUFBSSxDQUFDLEdBQUcsQ0FBQyxFQUFFLENBQUMsR0FBRyxLQUFLLENBQUMsTUFBTSxFQUFFLENBQUMsRUFBRSxFQUFFO1lBQ3JDLE1BQU0sS0FBSyxHQUFHLEtBQUssQ0FBQyxDQUFDLENBQUMsQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUFDLENBQUM7WUFDdkMsSUFBSSxLQUFLLEVBQUU7Z0JBQ1QsTUFBTSxLQUFLLEdBQUcsWUFBWSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDO2dCQUNyQyxJQUFJLEtBQUssSUFBSSxJQUFJLENBQUMsYUFBYSxDQUFDLFlBQVksRUFBRTtvQkFDNUMsTUFBTSxNQUFNLEdBQUcsMkVBQThCLENBQzNDLEtBQUssRUFDTCxhQUFhLEVBQ2IsTUFBTSxrQ0FFRCxJQUFJLENBQUMsYUFBYTt3QkFDckIsaURBQWlEO3dCQUNqRCxhQUFhLEVBQUUsQ0FBQyxFQUNoQixXQUFXLEVBQUUsSUFBSSxJQUVwQixDQUFDO29CQUNGLGFBQWEsR0FBRyxLQUFLLENBQUM7b0JBRXRCLFFBQVEsQ0FBQyxJQUFJLENBQUM7d0JBQ1osSUFBSSxFQUFFLEtBQUssQ0FBQyxDQUFDLENBQUM7d0JBQ2QsTUFBTSxFQUFFLE1BQU07d0JBQ2QsS0FBSzt3QkFDTCxJQUFJLEVBQUUsQ0FBQztxQkFDUixDQUFDLENBQUM7aUJBQ0o7YUFDRjtTQUNGO1FBQ0QsT0FBTyxPQUFPLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBQyxDQUFDO0lBQ25DLENBQUM7Q0FDRjtBQUVEOztHQUVHO0FBQ0ksTUFBTSwyQkFBNEIsU0FBUSxrRUFBNEI7SUFDM0U7Ozs7O09BS0c7SUFDSCxZQUFZLENBQUMsTUFBYzs7UUFDekIsTUFBTSxZQUFZLEdBQUcsS0FBSyxDQUFDLFlBQVksQ0FBQyxNQUFNLENBQUMsQ0FBQztRQUVoRCxJQUFJLFlBQVksRUFBRTtZQUNoQixJQUFJLElBQUksR0FBRyxZQUFDLE1BQWMsQ0FBQyxPQUFPLDBDQUFFLEtBQUssMENBQUUsUUFBUSxDQUFDO1lBQ3BELE9BQU8sSUFBSSxJQUFJLENBQUMsSUFBSSxLQUFLLGNBQWMsSUFBSSxJQUFJLEtBQUssYUFBYSxDQUFDLENBQUM7U0FDcEU7UUFDRCxPQUFPLEtBQUssQ0FBQztJQUNmLENBQUM7SUFFRDs7Ozs7O09BTUc7SUFDTyxVQUFVLENBQ2xCLE1BQTRELEVBQzVELGFBQXVDO1FBRXZDLE9BQU8sSUFBSSx5QkFBeUIsQ0FBQyxNQUFNLEVBQUUsYUFBYSxDQUFDLENBQUM7SUFDOUQsQ0FBQztDQUNGOzs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDaEpELDBDQUEwQztBQUMxQywyREFBMkQ7QUFPbEM7QUFHZ0Q7QUFFekU7O0dBRUc7QUFDSSxNQUFNLDRCQUE2QixTQUFRLGlFQUdqRDtJQUNDOzs7Ozs7T0FNRztJQUNILElBQUksWUFBWTtRQUNkLE9BQU8sVUFBVSxDQUFDO0lBQ3BCLENBQUM7SUFFRDs7OztPQUlHO0lBQ08sV0FBVztRQUNuQixJQUFJLENBQUMsSUFBSSxDQUFDLFFBQVEsRUFBRTtZQUNsQixPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLENBQUM7U0FDOUI7UUFFRCxNQUFNLE9BQU8sR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDLElBQUksQ0FBQztRQUVyRCxNQUFNLFFBQVEsR0FBRyxzRkFBeUMsQ0FBQyxPQUFPLGtDQUM3RCxJQUFJLENBQUMsYUFBYTtZQUNyQix1REFBdUQ7WUFDdkQsa0JBQWtCO1lBQ2xCLGFBQWEsRUFBRSxLQUFLLElBQ3BCLENBQUM7UUFDSCxPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsUUFBUSxDQUFDLENBQUM7SUFDbkMsQ0FBQztDQUNGO0FBRUQ7O0dBRUc7QUFDSSxNQUFNLDhCQUErQixTQUFRLGtFQUE0QjtJQUM5RTs7Ozs7T0FLRztJQUNILFlBQVksQ0FBQyxNQUFjOztRQUN6QixNQUFNLFlBQVksR0FBRyxLQUFLLENBQUMsWUFBWSxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBRWhELElBQUksWUFBWSxFQUFFO1lBQ2hCLElBQUksSUFBSSxHQUFHLFlBQUMsTUFBYyxDQUFDLE9BQU8sMENBQUUsS0FBSywwQ0FBRSxRQUFRLENBQUM7WUFDcEQsT0FBTyxJQUFJLElBQUkscUZBQXdDLENBQUMsSUFBSSxDQUFDLENBQUM7U0FDL0Q7UUFDRCxPQUFPLEtBQUssQ0FBQztJQUNmLENBQUM7SUFFRDs7Ozs7O09BTUc7SUFDTyxVQUFVLENBQ2xCLE1BQTRELEVBQzVELGFBQXVDO1FBRXZDLE9BQU8sSUFBSSw0QkFBNEIsQ0FBQyxNQUFNLEVBQUUsYUFBYSxDQUFDLENBQUM7SUFDakUsQ0FBQztDQUNGOzs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDdEZELDBDQUEwQztBQUMxQywyREFBMkQ7QUFLYTtBQUdDO0FBRXpFOztHQUVHO0FBQ0gsSUFBSSxRQUFnQixDQUFDO0FBQ3JCLElBQUk7SUFDRixxRUFBcUU7SUFDckUsa0ZBQWtGO0lBQ2xGLDRFQUE0RTtJQUM1RSxRQUFRLEdBQUcsSUFBSSxNQUFNLENBQUMsa0NBQWtDLEVBQUUsR0FBRyxDQUFDLENBQUM7Q0FDaEU7QUFBQyxXQUFNO0lBQ04sUUFBUSxHQUFHLElBQUksTUFBTSxDQUFDLGtDQUFrQyxDQUFDLENBQUM7Q0FDM0Q7QUFFRDs7R0FFRztBQUNJLE1BQU0sMEJBQTJCLFNBQVEsaUVBRy9DO0lBQ0M7Ozs7OztPQU1HO0lBQ0gsSUFBSSxZQUFZO1FBQ2QsT0FBTyxRQUFRLENBQUM7SUFDbEIsQ0FBQztJQUVEOzs7O09BSUc7SUFDTyxLQUFLLENBQUMsV0FBVztRQUN6QixJQUFJLENBQUMsSUFBSSxDQUFDLFFBQVEsRUFBRTtZQUNsQixPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLENBQUM7U0FDOUI7UUFFRCw2QkFBNkI7UUFDN0IsTUFBTSxLQUFLLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUMsS0FBSyxDQUN0RCxJQUFJLENBQ1ksQ0FBQztRQUVuQiwwRUFBMEU7UUFDMUUsSUFBSSxRQUFRLEdBQUcsSUFBSSxLQUFLLEVBQWtCLENBQUM7UUFDM0MsSUFBSSxpQkFBaUIsR0FBRyxLQUFLLENBQUM7UUFFOUIsSUFBSSxNQUFNLEdBQUcsQ0FBQyxDQUFDO1FBRWYsSUFBSSxPQUFPLEdBQUcsQ0FBQyxDQUFDLENBQUM7UUFDakIsS0FBSyxNQUFNLElBQUksSUFBSSxLQUFLLEVBQUU7WUFDeEIsT0FBTyxFQUFFLENBQUM7WUFDVixJQUFJLFVBQWtDLENBQUM7WUFDdkMsSUFBSSxRQUFRLENBQUMsS0FBSyxDQUFDLFFBQVEsQ0FBQyxHQUFHLENBQUMsRUFBRTtnQkFDaEMsVUFBVSxHQUFHLFFBQVEsQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7YUFDbEM7aUJBQU07Z0JBQ0wsTUFBTSxFQUFFLE9BQU8sRUFBRSxlQUFlLEVBQUUsR0FBRyxNQUFNLHFPQUUxQyxDQUFDO2dCQUNGLFVBQVUsR0FBRyxlQUFlLENBQUMsUUFBUSxFQUFFLElBQUksQ0FBQyxDQUFDO2FBQzlDO1lBQ0QsSUFBSSxVQUFVLEVBQUU7Z0JBQ2QsNERBQTREO2dCQUM1RCxNQUFNLENBQUMsS0FBSyxDQUFDLEdBQUksVUFBa0IsQ0FBQyxPQUFPLENBQUMsQ0FBQyxDQUFDLENBQUM7Z0JBQy9DLElBQUksTUFBTSxLQUFLLENBQUMsSUFBSSxLQUFLLEdBQUcsQ0FBQyxFQUFFO29CQUM3QixNQUFNLEdBQUcsS0FBSyxDQUFDO2lCQUNoQjtnQkFFRCxNQUFNLFFBQVEsR0FBRyxDQUFDLE9BQU8sRUFBRSxTQUFTLENBQUMsQ0FBQyxRQUFRLENBQUMsVUFBVSxDQUFDLENBQUMsQ0FBQyxDQUFDLENBQUM7Z0JBQzlELElBQUksUUFBUSxJQUFJLGlCQUFpQixFQUFFO29CQUNqQyxTQUFTO2lCQUNWO2dCQUNELGlCQUFpQixHQUFHLFFBQVEsQ0FBQztnQkFFN0IsTUFBTSxLQUFLLEdBQUcsQ0FBQyxHQUFHLEtBQUssR0FBRyxNQUFNLENBQUM7Z0JBRWpDLElBQUksS0FBSyxHQUFHLElBQUksQ0FBQyxhQUFhLENBQUMsWUFBWSxFQUFFO29CQUMzQyxTQUFTO2lCQUNWO2dCQUVELFFBQVEsQ0FBQyxJQUFJLENBQUM7b0JBQ1osSUFBSSxFQUFFLElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDO29CQUN2QixLQUFLO29CQUNMLElBQUksRUFBRSxPQUFPO2lCQUNkLENBQUMsQ0FBQzthQUNKO1NBQ0Y7UUFFRCxPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsUUFBUSxDQUFDLENBQUM7SUFDbkMsQ0FBQztDQUNGO0FBRUQ7O0dBRUc7QUFDSSxNQUFNLDRCQUE2QixTQUFRLGtFQUE0QjtJQUM1RTs7Ozs7T0FLRztJQUNILFlBQVksQ0FBQyxNQUFjOztRQUN6QixNQUFNLFlBQVksR0FBRyxLQUFLLENBQUMsWUFBWSxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBRWhELElBQUksWUFBWSxFQUFFO1lBQ2hCLElBQUksSUFBSSxHQUFHLFlBQUMsTUFBYyxDQUFDLE9BQU8sMENBQUUsS0FBSywwQ0FBRSxRQUFRLENBQUM7WUFDcEQsT0FBTyxDQUNMLElBQUk7Z0JBQ0osQ0FBQyxJQUFJLEtBQUssMkJBQTJCLElBQUksSUFBSSxLQUFLLGVBQWUsQ0FBQyxDQUNuRSxDQUFDO1NBQ0g7UUFDRCxPQUFPLEtBQUssQ0FBQztJQUNmLENBQUM7SUFFRDs7Ozs7O09BTUc7SUFDTyxVQUFVLENBQ2xCLE1BQW1DLEVBQ25DLGFBQXVDO1FBRXZDLE9BQU8sSUFBSSwwQkFBMEIsQ0FBQyxNQUFNLEVBQUUsYUFBYSxDQUFDLENBQUM7SUFDL0QsQ0FBQztDQUNGOzs7Ozs7Ozs7Ozs7Ozs7OztBQzlJRCwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBSWpCO0FBUzFDOztHQUVHO0FBQ0ksTUFBTSxjQUFjLEdBQUcsSUFBSSxvREFBSyxDQUNyQyx1Q0FBdUMsQ0FDeEMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNuQkYsMENBQTBDO0FBQzFDLDJEQUEyRDtBQU8zQjtBQU1DO0FBQzBCO0FBQ1A7QUFFSTtBQUV4RDs7R0FFRztBQUNILE1BQU0sV0FBVyxHQUFHLGNBQWMsQ0FBQztBQUVuQzs7R0FFRztBQUNILE1BQU0sTUFBTSxHQUFHLFVBQVUsQ0FBQztBQUUxQjs7R0FFRztBQUNJLE1BQU0sVUFBVyxTQUFRLG1EQUFNO0lBQ3BDOztPQUVHO0lBQ0gsWUFBWSxPQUE0QjtRQUN0QyxLQUFLLEVBQUUsQ0FBQztRQWlJRixXQUFNLEdBQUcsSUFBSSw4REFBZSxFQUFRLENBQUM7UUFoSTNDLElBQUksQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLENBQUM7UUFFL0IsTUFBTSxPQUFPLEdBQUcsQ0FBQyxJQUFJLENBQUMsUUFBUSxHQUFHLE9BQU8sQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUNsRCxJQUFJLENBQUMsZ0JBQWdCLEdBQUcsT0FBTyxDQUFDLGVBQWUsQ0FBQztRQUVoRCxNQUFNLFlBQVksR0FBRyxDQUFDLElBQUksQ0FBQyxhQUFhLEdBQUcsSUFBSSxxRUFBaUIsQ0FBQztZQUMvRCxPQUFPLEVBQUUsT0FBTyxDQUFDLE9BQU87WUFDeEIsS0FBSyxFQUFFLE9BQU8sQ0FBQyxLQUFLO1NBQ3JCLENBQUMsQ0FBQyxDQUFDO1FBQ0osSUFBSSxDQUFDLGFBQWEsQ0FBQyxRQUFRLENBQUMsMEJBQTBCLENBQUMsQ0FBQztRQUN4RCxJQUFJLENBQUMsYUFBYSxDQUFDLElBQUksQ0FBQyxPQUFPLENBQUMsV0FBVyxDQUFDLEdBQUcsTUFBTSxDQUFDO1FBQ3RELElBQUksQ0FBQyxhQUFhLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxNQUFNLENBQUMsR0FBRyxNQUFNLENBQUM7UUFFakQsSUFBSSxDQUFDLE1BQU0sR0FBRyxZQUFZLENBQUMsTUFBTSxDQUFDO1FBQ2xDLElBQUksQ0FBQyxLQUFLLEdBQUcsWUFBWSxDQUFDLEtBQUssQ0FBQztRQUVoQyxLQUFLLE9BQU8sQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLEdBQUcsRUFBRTtZQUMzQixJQUFJLENBQUMsZUFBZSxFQUFFLENBQUM7UUFDekIsQ0FBQyxDQUFDLENBQUM7UUFFSCxrQ0FBa0M7UUFDbEMsT0FBTyxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGNBQWMsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUN2RCxJQUFJLENBQUMsY0FBYyxFQUFFLENBQUM7UUFFdEIsTUFBTSxNQUFNLEdBQUcsQ0FBQyxJQUFJLENBQUMsTUFBTSxHQUFHLElBQUksMERBQWEsRUFBRSxDQUFDLENBQUM7UUFDbkQsTUFBTSxDQUFDLFNBQVMsQ0FBQyxZQUFZLENBQUMsQ0FBQztJQUNqQyxDQUFDO0lBRUQ7O09BRUc7SUFDSCxJQUFJLE9BQU87UUFDVCxPQUFPLElBQUksQ0FBQyxRQUFRLENBQUM7SUFDdkIsQ0FBQztJQUVEOztPQUVHO0lBQ0gsSUFBSSxLQUFLO1FBQ1AsT0FBTyxJQUFJLENBQUMsS0FBSyxDQUFDO0lBQ3BCLENBQUM7SUFFRDs7Ozs7Ozs7O09BU0c7SUFDSCxXQUFXLENBQUMsS0FBWTtRQUN0QixJQUFJLENBQUMsSUFBSSxDQUFDLEtBQUssRUFBRTtZQUNmLE9BQU87U0FDUjtRQUNELFFBQVEsS0FBSyxDQUFDLElBQUksRUFBRTtZQUNsQixLQUFLLFdBQVc7Z0JBQ2QsSUFBSSxDQUFDLFlBQVksRUFBRSxDQUFDO2dCQUNwQixNQUFNO1lBQ1I7Z0JBQ0UsTUFBTTtTQUNUO0lBQ0gsQ0FBQztJQUVEOztPQUVHO0lBQ08sYUFBYSxDQUFDLEdBQVk7UUFDbEMsS0FBSyxDQUFDLGFBQWEsQ0FBQyxHQUFHLENBQUMsQ0FBQztRQUN6QixNQUFNLElBQUksR0FBRyxJQUFJLENBQUMsSUFBSSxDQUFDO1FBQ3ZCLElBQUksQ0FBQyxnQkFBZ0IsQ0FBQyxXQUFXLEVBQUUsSUFBSSxDQUFDLENBQUM7SUFDM0MsQ0FBQztJQUVEOztPQUVHO0lBQ08sY0FBYyxDQUFDLEdBQVk7UUFDbkMsTUFBTSxJQUFJLEdBQUcsSUFBSSxDQUFDLElBQUksQ0FBQztRQUN2QixJQUFJLENBQUMsbUJBQW1CLENBQUMsV0FBVyxFQUFFLElBQUksQ0FBQyxDQUFDO0lBQzlDLENBQUM7SUFFRDs7T0FFRztJQUNPLGlCQUFpQixDQUFDLEdBQVk7UUFDdEMsSUFBSSxDQUFDLFlBQVksRUFBRSxDQUFDO0lBQ3RCLENBQUM7SUFFRDs7T0FFRztJQUNLLFlBQVk7UUFDbEIsSUFBSSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsUUFBUSxFQUFFLEVBQUU7WUFDM0IsSUFBSSxDQUFDLE1BQU0sQ0FBQyxLQUFLLEVBQUUsQ0FBQztTQUNyQjtJQUNILENBQUM7SUFFRDs7T0FFRztJQUNLLGVBQWU7UUFDckIsSUFBSSxJQUFJLENBQUMsVUFBVSxFQUFFO1lBQ25CLE9BQU87U0FDUjtRQUVELDBFQUEwRTtRQUMxRSxJQUFJLENBQUMsTUFBTSxDQUFDLFlBQVksRUFBRSxDQUFDO1FBQzNCLDZCQUE2QjtRQUM3QixJQUFJLENBQUMsTUFBTSxDQUFDLE9BQU8sQ0FBQyxTQUFTLENBQUMsQ0FBQztJQUNqQyxDQUFDO0lBRUQ7O09BRUc7SUFDSyxjQUFjO1FBQ3BCLE1BQU0sTUFBTSxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUM7UUFDM0IsTUFBTSxTQUFTLEdBQUcsSUFBSSxDQUFDLFFBQVEsQ0FBQyxTQUFTLENBQUM7UUFFMUMsTUFBTSxDQUFDLEtBQUssQ0FBQyxRQUFRO1lBQ25CLElBQUksQ0FBQyxnQkFBZ0IsQ0FBQyxxQkFBcUIsQ0FBQyxTQUFTLENBQUMsQ0FBQztJQUMzRCxDQUFDO0NBUUY7QUEyQkQ7O0dBRUc7QUFDSSxNQUFNLGlCQUFrQixTQUFRLHFFQUd0QztJQUNDOztPQUVHO0lBQ0gsWUFBWSxPQUFtQztRQUM3QyxLQUFLLENBQUMsT0FBTyxDQUFDLGNBQWMsQ0FBQyxDQUFDO1FBQzlCLElBQUksQ0FBQyxTQUFTLEdBQUcsT0FBTyxDQUFDLGNBQWMsQ0FBQztJQUMxQyxDQUFDO0lBRUQ7O09BRUc7SUFDTyxlQUFlLENBQ3ZCLE9BQXFDO1FBRXJDLE1BQU0sSUFBSSxHQUFHLElBQUksQ0FBQyxTQUFTLENBQUMsY0FBYyxDQUFDLGlCQUFpQixDQUFDO1FBQzdELE1BQU0sT0FBTyxHQUF1QixPQUFPLENBQUMsRUFBRTtZQUM1QyxPQUFPLElBQUksQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUN2QixDQUFDLENBQUM7UUFDRixNQUFNLE9BQU8sR0FBRyxJQUFJLFVBQVUsQ0FBQztZQUM3QixPQUFPO1lBQ1AsT0FBTztZQUNQLGVBQWUsRUFBRSxJQUFJLENBQUMsU0FBUyxDQUFDLGVBQWU7U0FDaEQsQ0FBQyxDQUFDO1FBRUgsT0FBTyxDQUFDLEtBQUssQ0FBQyxJQUFJLEdBQUcscUVBQWMsQ0FBQztRQUNwQyxNQUFNLE1BQU0sR0FBRyxJQUFJLG1FQUFjLENBQUMsRUFBRSxPQUFPLEVBQUUsT0FBTyxFQUFFLENBQUMsQ0FBQztRQUN4RCxPQUFPLE1BQU0sQ0FBQztJQUNoQixDQUFDO0NBR0YiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci9zcmMvZmlsZWVkaXRvcmxzcGFkYXB0ZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2ZpbGVlZGl0b3Ivc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9maWxlZWRpdG9yL3NyYy9zZWFyY2hwcm92aWRlci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci9zcmMvdGFic3BhY2VzdGF0dXMudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9maWxlZWRpdG9yL3NyYy90b2MvZmFjdG9yeS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci9zcmMvdG9jL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9maWxlZWRpdG9yL3NyYy90b2MvbGF0ZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2ZpbGVlZGl0b3Ivc3JjL3RvYy9tYXJrZG93bi50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci9zcmMvdG9jL3B5dGhvbi50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZmlsZWVkaXRvci9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9maWxlZWRpdG9yL3NyYy93aWRnZXQudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBDb2RlRWRpdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZWVkaXRvcic7XG5pbXBvcnQgeyBDb2RlTWlycm9yRWRpdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29kZW1pcnJvcic7XG5pbXBvcnQgeyBEb2N1bWVudFJlZ2lzdHJ5LCBJRG9jdW1lbnRXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQge1xuICBJQWRhcHRlck9wdGlvbnMsXG4gIElWaXJ0dWFsUG9zaXRpb24sXG4gIFZpcnR1YWxEb2N1bWVudCxcbiAgV2lkZ2V0TFNQQWRhcHRlclxufSBmcm9tICdAanVweXRlcmxhYi9sc3AnO1xuXG5pbXBvcnQgeyBGaWxlRWRpdG9yIH0gZnJvbSAnLi93aWRnZXQnO1xuXG5leHBvcnQgaW50ZXJmYWNlIElGaWxlRWRpdG9yQWRhcHRlck9wdGlvbnMgZXh0ZW5kcyBJQWRhcHRlck9wdGlvbnMge1xuICAvKipcbiAgICogVGhlIGRvY3VtZW50IHJlZ2lzdHJ5IGluc3RhbmNlLlxuICAgKi9cbiAgZG9jUmVnaXN0cnk6IERvY3VtZW50UmVnaXN0cnk7XG59XG5cbmV4cG9ydCBjbGFzcyBGaWxlRWRpdG9yQWRhcHRlciBleHRlbmRzIFdpZGdldExTUEFkYXB0ZXI8XG4gIElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yPlxuPiB7XG4gIGNvbnN0cnVjdG9yKFxuICAgIGVkaXRvcldpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+LFxuICAgIG9wdGlvbnM6IElGaWxlRWRpdG9yQWRhcHRlck9wdGlvbnNcbiAgKSB7XG4gICAgY29uc3QgeyBkb2NSZWdpc3RyeSwgLi4ub3RoZXJzIH0gPSBvcHRpb25zO1xuICAgIHN1cGVyKGVkaXRvcldpZGdldCwgb3RoZXJzKTtcbiAgICB0aGlzLmVkaXRvciA9IGVkaXRvcldpZGdldC5jb250ZW50O1xuICAgIHRoaXMuX2RvY1JlZ2lzdHJ5ID0gZG9jUmVnaXN0cnk7XG4gICAgdGhpcy5yZWFkeSA9IG5ldyBQcm9taXNlPHZvaWQ+KChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICAgIHRoaXMuaW5pdE9uY2VSZWFkeSgpLnRoZW4ocmVzb2x2ZSkuY2F0Y2gocmVqZWN0KTtcbiAgICB9KTtcblxuICAgIC8vIERpc3Bvc2UgdGhlIGFkYXB0ZXIgd2hlbiB0aGUgZWRpdG9yIGlzIGRpc3Bvc2VkLlxuICAgIGVkaXRvcldpZGdldC5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHRoaXMuZGlzcG9zZSgpKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgd3JhcHBlZCBgRmlsZUVkaXRvcmAgd2lkZ2V0LlxuICAgKi9cbiAgcmVhZG9ubHkgZWRpdG9yOiBGaWxlRWRpdG9yO1xuXG4gIC8qKlxuICAgKiBHZXQgY3VycmVudCBwYXRoIG9mIHRoZSBkb2N1bWVudC5cbiAgICovXG4gIGdldCBkb2N1bWVudFBhdGgoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy53aWRnZXQuY29udGV4dC5wYXRoO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgbWltZSB0eXBlIG9mIHRoZSBkb2N1bWVudC5cbiAgICovXG4gIGdldCBtaW1lVHlwZSgpOiBzdHJpbmcge1xuICAgIGNvbnN0IGNvZGVNaXJyb3JNaW1lVHlwZSA9IHRoaXMuZWRpdG9yLm1vZGVsLm1pbWVUeXBlO1xuICAgIGNvbnN0IGNvbnRlbnRzTW9kZWwgPSB0aGlzLmVkaXRvci5jb250ZXh0LmNvbnRlbnRzTW9kZWw7XG5cbiAgICAvLyB3aGVuIE1JTUUgdHlwZSBpcyBub3Qga25vd24gaXQgZGVmYXVsdHMgdG8gJ3RleHQvcGxhaW4nLFxuICAgIC8vIHNvIGlmIGl0IGlzIGRpZmZlcmVudCB3ZSBjYW4gYWNjZXB0IGl0IGFzIGl0IGlzXG4gICAgaWYgKGNvZGVNaXJyb3JNaW1lVHlwZSAhPSAndGV4dC9wbGFpbicpIHtcbiAgICAgIHJldHVybiBjb2RlTWlycm9yTWltZVR5cGU7XG4gICAgfSBlbHNlIGlmIChjb250ZW50c01vZGVsKSB7XG4gICAgICAvLyBhIHNjcmlwdCB0aGF0IGRvZXMgbm90IGhhdmUgYSBNSU1FIHR5cGUga25vd24gYnkgdGhlIGVkaXRvclxuICAgICAgLy8gKG5vIHN5bnRheCBoaWdobGlnaHQgbW9kZSksIGNhbiBzdGlsbCBiZSBrbm93biBieSB0aGUgZG9jdW1lbnRcbiAgICAgIC8vIHJlZ2lzdHJ5IChhbmQgdGhpcyBpcyBhcmd1YWJseSBlYXNpZXIgdG8gZXh0ZW5kKS5cbiAgICAgIGxldCBmaWxlVHlwZSA9IHRoaXMuX2RvY1JlZ2lzdHJ5LmdldEZpbGVUeXBlRm9yTW9kZWwoY29udGVudHNNb2RlbCk7XG4gICAgICByZXR1cm4gZmlsZVR5cGUubWltZVR5cGVzWzBdO1xuICAgIH0gZWxzZSB7XG4gICAgICAvLyBcInRleHQvcGxhaW5cIiB0aGlzIGlzXG4gICAgICByZXR1cm4gY29kZU1pcnJvck1pbWVUeXBlO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGZpbGUgZXh0ZW5zaW9uIG9mIHRoZSBkb2N1bWVudC5cbiAgICovXG4gIGdldCBsYW5ndWFnZUZpbGVFeHRlbnNpb24oKTogc3RyaW5nIHtcbiAgICBsZXQgcGFydHMgPSB0aGlzLmRvY3VtZW50UGF0aC5zcGxpdCgnLicpO1xuICAgIHJldHVybiBwYXJ0c1twYXJ0cy5sZW5ndGggLSAxXTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIENNIGVkaXRvclxuICAgKi9cbiAgZ2V0IGNlRWRpdG9yKCk6IENvZGVNaXJyb3JFZGl0b3Ige1xuICAgIHJldHVybiB0aGlzLmVkaXRvci5lZGl0b3IgYXMgQ29kZU1pcnJvckVkaXRvcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGFjdGl2YXRlZCBDTSBlZGl0b3IuXG4gICAqL1xuICBnZXQgYWN0aXZlRWRpdG9yKCk6IENvZGVFZGl0b3IuSUVkaXRvciB7XG4gICAgcmV0dXJuIHRoaXMuZWRpdG9yLmVkaXRvcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGlubmVyIEhUTUxFbGVtZW50IG9mIHRoZSBkb2N1bWVudCB3aWRnZXQuXG4gICAqL1xuICBnZXQgd3JhcHBlckVsZW1lbnQoKTogSFRNTEVsZW1lbnQge1xuICAgIHJldHVybiB0aGlzLndpZGdldC5ub2RlO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCBjdXJyZW50IHBhdGggb2YgdGhlIGRvY3VtZW50LlxuICAgKi9cbiAgZ2V0IHBhdGgoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy53aWRnZXQuY29udGV4dC5wYXRoO1xuICB9XG5cbiAgLyoqXG4gICAqICBHZXQgdGhlIGxpc3Qgb2YgQ00gZWRpdG9ycyBpbiB0aGUgZG9jdW1lbnQsIHRoZXJlIGlzIG9ubHkgb25lIGVkaXRvclxuICAgKiBpbiB0aGUgY2FzZSBvZiBmaWxlIGVkaXRvci5cbiAgICovXG4gIGdldCBlZGl0b3JzKCk6IHsgY2VFZGl0b3I6IENvZGVFZGl0b3IuSUVkaXRvcjsgdHlwZTogc3RyaW5nIH1bXSB7XG4gICAgcmV0dXJuIFt7IGNlRWRpdG9yOiB0aGlzLmVkaXRvci5lZGl0b3IsIHR5cGU6ICdjb2RlJyB9XTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZW5lcmF0ZSB0aGUgdmlydHVhbCBkb2N1bWVudCBhc3NvY2lhdGVkIHdpdGggdGhlIGRvY3VtZW50LlxuICAgKi9cbiAgY3JlYXRlVmlydHVhbERvY3VtZW50KCk6IFZpcnR1YWxEb2N1bWVudCB7XG4gICAgcmV0dXJuIG5ldyBWaXJ0dWFsRG9jdW1lbnQoe1xuICAgICAgbGFuZ3VhZ2U6IHRoaXMubGFuZ3VhZ2UsXG4gICAgICBmb3JlaWduQ29kZUV4dHJhY3RvcnM6IHRoaXMub3B0aW9ucy5mb3JlaWduQ29kZUV4dHJhY3RvcnNNYW5hZ2VyLFxuICAgICAgcGF0aDogdGhpcy5kb2N1bWVudFBhdGgsXG4gICAgICBmaWxlRXh0ZW5zaW9uOiB0aGlzLmxhbmd1YWdlRmlsZUV4dGVuc2lvbixcbiAgICAgIC8vIG5vdGVib29rcyBhcmUgY29udGludW91cywgZWFjaCBjZWxsIGlzIGRlcGVuZGVudCBvbiB0aGUgcHJldmlvdXMgb25lXG4gICAgICBzdGFuZGFsb25lOiB0cnVlLFxuICAgICAgLy8gbm90ZWJvb2tzIGFyZSBub3Qgc3VwcG9ydGVkIGJ5IExTUCBzZXJ2ZXJzXG4gICAgICBoYXNMc3BTdXBwb3J0ZWRGaWxlOiB0cnVlXG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHRoZSBpbmRleCBvZiBlZGl0b3IgZnJvbSB0aGUgY3Vyc29yIHBvc2l0aW9uIGluIHRoZSB2aXJ0dWFsXG4gICAqIGRvY3VtZW50LiBTaW5jZSB0aGVyZSBpcyBvbmx5IG9uZSBlZGl0b3IsIHRoaXMgbWV0aG9kIGFsd2F5cyByZXR1cm5cbiAgICogMFxuICAgKlxuICAgKiBAcGFyYW0gcG9zaXRpb24gLSB0aGUgcG9zaXRpb24gb2YgY3Vyc29yIGluIHRoZSB2aXJ0dWFsIGRvY3VtZW50LlxuICAgKiBAcmV0dXJuICB7bnVtYmVyfSAtIGluZGV4IG9mIHRoZSB2aXJ0dWFsIGVkaXRvclxuICAgKi9cbiAgZ2V0RWRpdG9ySW5kZXhBdChwb3NpdGlvbjogSVZpcnR1YWxQb3NpdGlvbik6IG51bWJlciB7XG4gICAgcmV0dXJuIDA7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHRoZSBpbmRleCBvZiBpbnB1dCBlZGl0b3JcbiAgICpcbiAgICogQHBhcmFtIGNlRWRpdG9yIC0gaW5zdGFuY2Ugb2YgdGhlIGNvZGUgZWRpdG9yXG4gICAqL1xuICBnZXRFZGl0b3JJbmRleChjZUVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yKTogbnVtYmVyIHtcbiAgICByZXR1cm4gMDtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgdGhlIHdyYXBwZXIgb2YgaW5wdXQgZWRpdG9yLlxuICAgKlxuICAgKiBAcGFyYW0gY2VFZGl0b3JcbiAgICogQHJldHVybiAge0hUTUxFbGVtZW50fVxuICAgKi9cbiAgZ2V0RWRpdG9yV3JhcHBlcihjZUVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yKTogSFRNTEVsZW1lbnQge1xuICAgIHJldHVybiB0aGlzLndyYXBwZXJFbGVtZW50O1xuICB9XG5cbiAgLyoqXG4gICAqIEluaXRpYWxpemF0aW9uIGZ1bmN0aW9uIGNhbGxlZCBvbmNlIHRoZSBlZGl0b3IgYW5kIHRoZSBMU1AgY29ubmVjdGlvblxuICAgKiBtYW5hZ2VyIGlzIHJlYWR5LiBUaGlzIGZ1bmN0aW9uIHdpbGwgY3JlYXRlIHRoZSB2aXJ0dWFsIGRvY3VtZW50IGFuZFxuICAgKiBjb25uZWN0IHZhcmlvdXMgc2lnbmFscy5cbiAgICovXG4gIHByb3RlY3RlZCBhc3luYyBpbml0T25jZVJlYWR5KCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGlmICghdGhpcy5lZGl0b3IuY29udGV4dC5pc1JlYWR5KSB7XG4gICAgICBhd2FpdCB0aGlzLmVkaXRvci5jb250ZXh0LnJlYWR5O1xuICAgIH1cbiAgICBhd2FpdCB0aGlzLmNvbm5lY3Rpb25NYW5hZ2VyLnJlYWR5O1xuICAgIHRoaXMuaW5pdFZpcnR1YWwoKTtcblxuICAgIC8vIGNvbm5lY3QgdGhlIGRvY3VtZW50LCBidXQgZG8gbm90IG9wZW4gaXQgYXMgdGhlIGFkYXB0ZXIgd2lsbCBoYW5kbGUgdGhpc1xuICAgIC8vIGFmdGVyIHJlZ2lzdGVyaW5nIGFsbCBmZWF0dXJlc1xuICAgIHRoaXMuY29ubmVjdERvY3VtZW50KHRoaXMudmlydHVhbERvY3VtZW50LCBmYWxzZSkuY2F0Y2goY29uc29sZS53YXJuKTtcblxuICAgIHRoaXMuZWRpdG9yLm1vZGVsLm1pbWVUeXBlQ2hhbmdlZC5jb25uZWN0KHRoaXMucmVsb2FkQ29ubmVjdGlvbiwgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGRvY3VtZW50IHJlZ2lzdHJ5IGluc3RhbmNlLlxuICAgKi9cbiAgcHJpdmF0ZSByZWFkb25seSBfZG9jUmVnaXN0cnk6IERvY3VtZW50UmVnaXN0cnk7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBmaWxlZWRpdG9yXG4gKi9cblxuZXhwb3J0ICogZnJvbSAnLi9maWxlZWRpdG9ybHNwYWRhcHRlcic7XG5leHBvcnQgKiBmcm9tICcuL3NlYXJjaHByb3ZpZGVyJztcbmV4cG9ydCAqIGZyb20gJy4vdGFic3BhY2VzdGF0dXMnO1xuZXhwb3J0ICogZnJvbSAnLi90b2MnO1xuZXhwb3J0ICogZnJvbSAnLi90b2tlbnMnO1xuZXhwb3J0ICogZnJvbSAnLi93aWRnZXQnO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBNYWluQXJlYVdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7XG4gIENvZGVNaXJyb3JFZGl0b3IsXG4gIENvZGVNaXJyb3JTZWFyY2hQcm92aWRlclxufSBmcm9tICdAanVweXRlcmxhYi9jb2RlbWlycm9yJztcbmltcG9ydCB7IElTZWFyY2hQcm92aWRlciB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3VtZW50c2VhcmNoJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IEZpbGVFZGl0b3IgfSBmcm9tICcuL3dpZGdldCc7XG5cbi8qKlxuICogSGVscGVyIHR5cGVcbiAqL1xuZXhwb3J0IHR5cGUgRmlsZUVkaXRvclBhbmVsID0gTWFpbkFyZWFXaWRnZXQ8RmlsZUVkaXRvcj47XG5cbi8qKlxuICogRmlsZSBlZGl0b3Igc2VhcmNoIHByb3ZpZGVyXG4gKi9cbmV4cG9ydCBjbGFzcyBGaWxlRWRpdG9yU2VhcmNoUHJvdmlkZXJcbiAgZXh0ZW5kcyBDb2RlTWlycm9yU2VhcmNoUHJvdmlkZXJcbiAgaW1wbGVtZW50cyBJU2VhcmNoUHJvdmlkZXJcbntcbiAgLyoqXG4gICAqIENvbnN0cnVjdG9yXG4gICAqIEBwYXJhbSB3aWRnZXQgRmlsZSBlZGl0b3IgcGFuZWxcbiAgICovXG4gIGNvbnN0cnVjdG9yKHdpZGdldDogRmlsZUVkaXRvclBhbmVsKSB7XG4gICAgc3VwZXIod2lkZ2V0LmNvbnRlbnQuZWRpdG9yIGFzIENvZGVNaXJyb3JFZGl0b3IpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluc3RhbnRpYXRlIGEgc2VhcmNoIHByb3ZpZGVyIGZvciB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoZSB3aWRnZXQgcHJvdmlkZWQgaXMgYWx3YXlzIGNoZWNrZWQgdXNpbmcgYGlzQXBwbGljYWJsZWAgYmVmb3JlIGNhbGxpbmdcbiAgICogdGhpcyBmYWN0b3J5LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFRoZSB3aWRnZXQgdG8gc2VhcmNoIG9uXG4gICAqIEBwYXJhbSB0cmFuc2xhdG9yIFtvcHRpb25hbF0gVGhlIHRyYW5zbGF0b3Igb2JqZWN0XG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBzZWFyY2ggcHJvdmlkZXIgb24gdGhlIHdpZGdldFxuICAgKi9cbiAgc3RhdGljIGNyZWF0ZU5ldyhcbiAgICB3aWRnZXQ6IEZpbGVFZGl0b3JQYW5lbCxcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKTogSVNlYXJjaFByb3ZpZGVyIHtcbiAgICByZXR1cm4gbmV3IEZpbGVFZGl0b3JTZWFyY2hQcm92aWRlcih3aWRnZXQpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlcG9ydCB3aGV0aGVyIG9yIG5vdCB0aGlzIHByb3ZpZGVyIGhhcyB0aGUgYWJpbGl0eSB0byBzZWFyY2ggb24gdGhlIGdpdmVuIG9iamVjdFxuICAgKi9cbiAgc3RhdGljIGlzQXBwbGljYWJsZShkb21haW46IFdpZGdldCk6IGRvbWFpbiBpcyBGaWxlRWRpdG9yUGFuZWwge1xuICAgIHJldHVybiAoXG4gICAgICBkb21haW4gaW5zdGFuY2VvZiBNYWluQXJlYVdpZGdldCAmJlxuICAgICAgZG9tYWluLmNvbnRlbnQgaW5zdGFuY2VvZiBGaWxlRWRpdG9yICYmXG4gICAgICBkb21haW4uY29udGVudC5lZGl0b3IgaW5zdGFuY2VvZiBDb2RlTWlycm9yRWRpdG9yXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgYW4gaW5pdGlhbCBxdWVyeSB2YWx1ZSBpZiBhcHBsaWNhYmxlIHNvIHRoYXQgaXQgY2FuIGJlIGVudGVyZWRcbiAgICogaW50byB0aGUgc2VhcmNoIGJveCBhcyBhbiBpbml0aWFsIHF1ZXJ5XG4gICAqXG4gICAqIEByZXR1cm5zIEluaXRpYWwgdmFsdWUgdXNlZCB0byBwb3B1bGF0ZSB0aGUgc2VhcmNoIGJveC5cbiAgICovXG4gIGdldEluaXRpYWxRdWVyeSgpOiBzdHJpbmcge1xuICAgIGNvbnN0IGNtID0gdGhpcy5lZGl0b3IgYXMgQ29kZU1pcnJvckVkaXRvcjtcbiAgICBjb25zdCBzZWxlY3Rpb24gPSBjbS5zdGF0ZS5zbGljZURvYyhcbiAgICAgIGNtLnN0YXRlLnNlbGVjdGlvbi5tYWluLmZyb20sXG4gICAgICBjbS5zdGF0ZS5zZWxlY3Rpb24ubWFpbi50b1xuICAgICk7XG4gICAgLy8gaWYgdGhlcmUgYXJlIG5ld2xpbmVzLCBqdXN0IHJldHVybiBlbXB0eSBzdHJpbmdcbiAgICByZXR1cm4gc2VsZWN0aW9uLnNlYXJjaCgvXFxyP1xcbnxcXHIvZykgPT09IC0xID8gc2VsZWN0aW9uIDogJyc7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgQ29kZUVkaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVlZGl0b3InO1xuaW1wb3J0IHtcbiAgY2xpY2tlZEl0ZW0sXG4gIGludGVyYWN0aXZlSXRlbSxcbiAgUG9wdXAsXG4gIHNob3dQb3B1cCxcbiAgVGV4dEl0ZW1cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdHVzYmFyJztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IFZEb21Nb2RlbCwgVkRvbVJlbmRlcmVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBNZW51IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCBSZWFjdCBmcm9tICdyZWFjdCc7XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIFRhYlNwYWNlQ29tcG9uZW50IHN0YXRpY3MuXG4gKi9cbm5hbWVzcGFjZSBUYWJTcGFjZUNvbXBvbmVudCB7XG4gIC8qKlxuICAgKiBUaGUgcHJvcHMgZm9yIFRhYlNwYWNlQ29tcG9uZW50LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBudW1iZXIgb2Ygc3BhY2VzIHRvIGluc2VydCBvbiB0YWIuXG4gICAgICovXG4gICAgdGFiU3BhY2U6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gdXNlIHNwYWNlcyBvciB0YWJzLlxuICAgICAqL1xuICAgIGlzU3BhY2VzOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFwcGxpY2F0aW9uIGxhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAgICovXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuXG4gICAgLyoqXG4gICAgICogQSBjbGljayBoYW5kbGVyIGZvciB0aGUgVGFiU3BhY2UgY29tcG9uZW50LiBCeSBkZWZhdWx0XG4gICAgICogb3BlbnMgYSBtZW51IGFsbG93aW5nIHRoZSB1c2VyIHRvIHNlbGVjdCB0YWJzIHZzIHNwYWNlcy5cbiAgICAgKi9cbiAgICBoYW5kbGVDbGljazogKCkgPT4gdm9pZDtcbiAgfVxufVxuXG4vKipcbiAqIEEgcHVyZSBmdW5jdGlvbmFsIGNvbXBvbmVudCBmb3IgcmVuZGVyaW5nIHRoZSBUYWJTcGFjZSBzdGF0dXMuXG4gKi9cbmZ1bmN0aW9uIFRhYlNwYWNlQ29tcG9uZW50KFxuICBwcm9wczogVGFiU3BhY2VDb21wb25lbnQuSVByb3BzXG4pOiBSZWFjdC5SZWFjdEVsZW1lbnQ8VGFiU3BhY2VDb21wb25lbnQuSVByb3BzPiB7XG4gIGNvbnN0IHRyYW5zbGF0b3IgPSBwcm9wcy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICBjb25zdCB0cmFucyA9IHRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICBjb25zdCBkZXNjcmlwdGlvbiA9IHByb3BzLmlzU3BhY2VzXG4gICAgPyB0cmFucy5fXygnU3BhY2VzJylcbiAgICA6IHRyYW5zLl9fKCdUYWIgU2l6ZScpO1xuICByZXR1cm4gKFxuICAgIDxUZXh0SXRlbVxuICAgICAgb25DbGljaz17cHJvcHMuaGFuZGxlQ2xpY2t9XG4gICAgICBzb3VyY2U9e2Ake2Rlc2NyaXB0aW9ufTogJHtwcm9wcy50YWJTcGFjZX1gfVxuICAgICAgdGl0bGU9e3RyYW5zLl9fKCdDaGFuZ2UgVGFiIGluZGVudGF0aW9u4oCmJyl9XG4gICAgLz5cbiAgKTtcbn1cblxuLyoqXG4gKiBBIFZEb21SZW5kZXJlciBmb3IgYSB0YWJzIHZzLiBzcGFjZXMgc3RhdHVzIGl0ZW0uXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWJTcGFjZVN0YXR1cyBleHRlbmRzIFZEb21SZW5kZXJlcjxUYWJTcGFjZVN0YXR1cy5Nb2RlbD4ge1xuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IHRhYi9zcGFjZSBzdGF0dXMgaXRlbS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IFRhYlNwYWNlU3RhdHVzLklPcHRpb25zKSB7XG4gICAgc3VwZXIobmV3IFRhYlNwYWNlU3RhdHVzLk1vZGVsKCkpO1xuICAgIHRoaXMuX21lbnUgPSBvcHRpb25zLm1lbnU7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuYWRkQ2xhc3MoaW50ZXJhY3RpdmVJdGVtKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgdGhlIFRhYlNwYWNlIHN0YXR1cyBpdGVtLlxuICAgKi9cbiAgcmVuZGVyKCk6IFJlYWN0LlJlYWN0RWxlbWVudDxUYWJTcGFjZUNvbXBvbmVudC5JUHJvcHM+IHwgbnVsbCB7XG4gICAgaWYgKCF0aGlzLm1vZGVsIHx8ICF0aGlzLm1vZGVsLmNvbmZpZykge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIDxUYWJTcGFjZUNvbXBvbmVudFxuICAgICAgICAgIGlzU3BhY2VzPXt0aGlzLm1vZGVsLmNvbmZpZy5pbnNlcnRTcGFjZXN9XG4gICAgICAgICAgdGFiU3BhY2U9e3RoaXMubW9kZWwuY29uZmlnLnRhYlNpemV9XG4gICAgICAgICAgaGFuZGxlQ2xpY2s9eygpID0+IHRoaXMuX2hhbmRsZUNsaWNrKCl9XG4gICAgICAgICAgdHJhbnNsYXRvcj17dGhpcy50cmFuc2xhdG9yfVxuICAgICAgICAvPlxuICAgICAgKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2xpY2sgb24gdGhlIHN0YXR1cyBpdGVtLlxuICAgKi9cbiAgcHJpdmF0ZSBfaGFuZGxlQ2xpY2soKTogdm9pZCB7XG4gICAgY29uc3QgbWVudSA9IHRoaXMuX21lbnU7XG4gICAgaWYgKHRoaXMuX3BvcHVwKSB7XG4gICAgICB0aGlzLl9wb3B1cC5kaXNwb3NlKCk7XG4gICAgfVxuXG4gICAgbWVudS5hYm91dFRvQ2xvc2UuY29ubmVjdCh0aGlzLl9tZW51Q2xvc2VkLCB0aGlzKTtcblxuICAgIHRoaXMuX3BvcHVwID0gc2hvd1BvcHVwKHtcbiAgICAgIGJvZHk6IG1lbnUsXG4gICAgICBhbmNob3I6IHRoaXMsXG4gICAgICBhbGlnbjogJ3JpZ2h0J1xuICAgIH0pO1xuICB9XG5cbiAgcHJpdmF0ZSBfbWVudUNsb3NlZCgpOiB2b2lkIHtcbiAgICB0aGlzLnJlbW92ZUNsYXNzKGNsaWNrZWRJdGVtKTtcbiAgfVxuXG4gIHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbiAgcHJpdmF0ZSBfbWVudTogTWVudTtcbiAgcHJpdmF0ZSBfcG9wdXA6IFBvcHVwIHwgbnVsbCA9IG51bGw7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIFRhYlNwYWNlIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgVGFiU3BhY2VTdGF0dXMge1xuICAvKipcbiAgICogQSBWRG9tTW9kZWwgZm9yIHRoZSBUYWJTcGFjZSBzdGF0dXMgaXRlbS5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBNb2RlbCBleHRlbmRzIFZEb21Nb2RlbCB7XG4gICAgLyoqXG4gICAgICogVGhlIGVkaXRvciBjb25maWcgZnJvbSB0aGUgc2V0dGluZ3Mgc3lzdGVtLlxuICAgICAqL1xuICAgIGdldCBjb25maWcoKTogQ29kZUVkaXRvci5JQ29uZmlnIHwgbnVsbCB7XG4gICAgICByZXR1cm4gdGhpcy5fY29uZmlnO1xuICAgIH1cbiAgICBzZXQgY29uZmlnKHZhbDogQ29kZUVkaXRvci5JQ29uZmlnIHwgbnVsbCkge1xuICAgICAgY29uc3Qgb2xkQ29uZmlnID0gdGhpcy5fY29uZmlnO1xuICAgICAgdGhpcy5fY29uZmlnID0gdmFsO1xuICAgICAgdGhpcy5fdHJpZ2dlckNoYW5nZShvbGRDb25maWcsIHRoaXMuX2NvbmZpZyk7XG4gICAgfVxuXG4gICAgcHJpdmF0ZSBfdHJpZ2dlckNoYW5nZShcbiAgICAgIG9sZFZhbHVlOiBDb2RlRWRpdG9yLklDb25maWcgfCBudWxsLFxuICAgICAgbmV3VmFsdWU6IENvZGVFZGl0b3IuSUNvbmZpZyB8IG51bGxcbiAgICApOiB2b2lkIHtcbiAgICAgIGNvbnN0IG9sZFNwYWNlcyA9IG9sZFZhbHVlICYmIG9sZFZhbHVlLmluc2VydFNwYWNlcztcbiAgICAgIGNvbnN0IG9sZFNpemUgPSBvbGRWYWx1ZSAmJiBvbGRWYWx1ZS50YWJTaXplO1xuICAgICAgY29uc3QgbmV3U3BhY2VzID0gbmV3VmFsdWUgJiYgbmV3VmFsdWUuaW5zZXJ0U3BhY2VzO1xuICAgICAgY29uc3QgbmV3U2l6ZSA9IG5ld1ZhbHVlICYmIG5ld1ZhbHVlLnRhYlNpemU7XG4gICAgICBpZiAob2xkU3BhY2VzICE9PSBuZXdTcGFjZXMgfHwgb2xkU2l6ZSAhPT0gbmV3U2l6ZSkge1xuICAgICAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KHZvaWQgMCk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgcHJpdmF0ZSBfY29uZmlnOiBDb2RlRWRpdG9yLklDb25maWcgfCBudWxsID0gbnVsbDtcbiAgfVxuXG4gIC8qKlxuICAgKiBPcHRpb25zIGZvciBjcmVhdGluZyBhIFRhYlNwYWNlIHN0YXR1cyBpdGVtLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogQSBtZW51IHRvIG9wZW4gd2hlbiBjbGlja2luZyBvbiB0aGUgc3RhdHVzIGl0ZW0uIFRoaXMgc2hvdWxkIGFsbG93XG4gICAgICogdGhlIHVzZXIgdG8gbWFrZSBhIGRpZmZlcmVudCBzZWxlY3Rpb24gYWJvdXQgdGFicy9zcGFjZXMuXG4gICAgICovXG4gICAgbWVudTogTWVudTtcblxuICAgIC8qKlxuICAgICAqIExhbmd1YWdlIHRyYW5zbGF0b3IuXG4gICAgICovXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnksIElEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7XG4gIFRhYmxlT2ZDb250ZW50cyxcbiAgVGFibGVPZkNvbnRlbnRzRmFjdG9yeSxcbiAgVGFibGVPZkNvbnRlbnRzTW9kZWxcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdG9jJztcbmltcG9ydCB7IEZpbGVFZGl0b3IgfSBmcm9tICcuLi93aWRnZXQnO1xuXG4vKipcbiAqIEludGVyZmFjZSBkZXNjcmliaW5nIGEgZmlsZSBlZGl0b3IgaGVhZGluZy5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRWRpdG9ySGVhZGluZyBleHRlbmRzIFRhYmxlT2ZDb250ZW50cy5JSGVhZGluZyB7XG4gIC8qKlxuICAgKiBIZWFkaW5nIGxpbmUgbnVtYmVyLlxuICAgKi9cbiAgbGluZTogbnVtYmVyO1xufVxuXG4vKipcbiAqIEJhc2UgdGFibGUgb2YgY29udGVudHMgbW9kZWwgZmFjdG9yeSBmb3IgZmlsZSBlZGl0b3JcbiAqL1xuZXhwb3J0IGFic3RyYWN0IGNsYXNzIEVkaXRvclRhYmxlT2ZDb250ZW50c0ZhY3RvcnkgZXh0ZW5kcyBUYWJsZU9mQ29udGVudHNGYWN0b3J5PFxuICBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj5cbj4ge1xuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsIGZvciB0aGUgd2lkZ2V0XG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSB3aWRnZXRcbiAgICogQHBhcmFtIGNvbmZpZ3VyYXRpb24gLSBUYWJsZSBvZiBjb250ZW50cyBjb25maWd1cmF0aW9uXG4gICAqIEByZXR1cm5zIFRoZSB0YWJsZSBvZiBjb250ZW50cyBtb2RlbFxuICAgKi9cbiAgY3JlYXRlTmV3KFxuICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3IsIERvY3VtZW50UmVnaXN0cnkuSU1vZGVsPixcbiAgICBjb25maWd1cmF0aW9uPzogVGFibGVPZkNvbnRlbnRzLklDb25maWdcbiAgKTogVGFibGVPZkNvbnRlbnRzTW9kZWw8XG4gICAgSUVkaXRvckhlYWRpbmcsXG4gICAgSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3IsIERvY3VtZW50UmVnaXN0cnkuSU1vZGVsPlxuICA+IHtcbiAgICBjb25zdCBtb2RlbCA9IHN1cGVyLmNyZWF0ZU5ldyhcbiAgICAgIHdpZGdldCxcbiAgICAgIGNvbmZpZ3VyYXRpb25cbiAgICApIGFzIFRhYmxlT2ZDb250ZW50c01vZGVsPFxuICAgICAgSUVkaXRvckhlYWRpbmcsXG4gICAgICBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvciwgRG9jdW1lbnRSZWdpc3RyeS5JTW9kZWw+XG4gICAgPjtcblxuICAgIGNvbnN0IG9uQWN0aXZlSGVhZGluZ0NoYW5nZWQgPSAoXG4gICAgICBtb2RlbDogVGFibGVPZkNvbnRlbnRzTW9kZWw8XG4gICAgICAgIElFZGl0b3JIZWFkaW5nLFxuICAgICAgICBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvciwgRG9jdW1lbnRSZWdpc3RyeS5JTW9kZWw+XG4gICAgICA+LFxuICAgICAgaGVhZGluZzogSUVkaXRvckhlYWRpbmcgfCBudWxsXG4gICAgKSA9PiB7XG4gICAgICBpZiAoaGVhZGluZykge1xuICAgICAgICB3aWRnZXQuY29udGVudC5lZGl0b3Iuc2V0Q3Vyc29yUG9zaXRpb24oe1xuICAgICAgICAgIGxpbmU6IGhlYWRpbmcubGluZSxcbiAgICAgICAgICBjb2x1bW46IDBcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfTtcblxuICAgIG1vZGVsLmFjdGl2ZUhlYWRpbmdDaGFuZ2VkLmNvbm5lY3Qob25BY3RpdmVIZWFkaW5nQ2hhbmdlZCk7XG4gICAgd2lkZ2V0LmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgbW9kZWwuYWN0aXZlSGVhZGluZ0NoYW5nZWQuZGlzY29ubmVjdChvbkFjdGl2ZUhlYWRpbmdDaGFuZ2VkKTtcbiAgICB9KTtcblxuICAgIHJldHVybiBtb2RlbDtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5leHBvcnQgKiBmcm9tICcuL2ZhY3RvcnknO1xuZXhwb3J0ICogZnJvbSAnLi9sYXRleCc7XG5leHBvcnQgKiBmcm9tICcuL21hcmtkb3duJztcbmV4cG9ydCAqIGZyb20gJy4vcHl0aG9uJztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSwgSURvY3VtZW50V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHtcbiAgVGFibGVPZkNvbnRlbnRzLFxuICBUYWJsZU9mQ29udGVudHNNb2RlbCxcbiAgVGFibGVPZkNvbnRlbnRzVXRpbHNcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdG9jJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBGaWxlRWRpdG9yIH0gZnJvbSAnLi4vd2lkZ2V0JztcbmltcG9ydCB7IEVkaXRvclRhYmxlT2ZDb250ZW50c0ZhY3RvcnksIElFZGl0b3JIZWFkaW5nIH0gZnJvbSAnLi9mYWN0b3J5JztcblxuLyoqXG4gKiBNYXBzIExhVGVYIHNlY3Rpb24gaGVhZGluZ3MgdG8gSFRNTCBoZWFkZXIgbGV2ZWxzLlxuICpcbiAqICMjIE5vdGVzXG4gKlxuICogLSAgIEFzIGBwYXJ0YCBhbmQgYGNoYXB0ZXJgIHNlY3Rpb24gaGVhZGluZ3MgYXBwZWFyIHRvIGJlIGxlc3MgY29tbW9uLCBhc3NpZ24gdGhlbSB0byBoZWFkaW5nIGxldmVsIDEuXG4gKlxuICogQHByaXZhdGVcbiAqL1xuY29uc3QgTEFURVhfTEVWRUxTOiB7IFtsYWJlbDogc3RyaW5nXTogbnVtYmVyIH0gPSB7XG4gIHBhcnQ6IDEsIC8vIE9ubHkgYXZhaWxhYmxlIGZvciByZXBvcnQgYW5kIGJvb2sgY2xhc3Nlc1xuICBjaGFwdGVyOiAxLCAvLyBPbmx5IGF2YWlsYWJsZSBmb3IgcmVwb3J0IGFuZCBib29rIGNsYXNzZXNcbiAgc2VjdGlvbjogMSxcbiAgc3Vic2VjdGlvbjogMixcbiAgc3Vic3Vic2VjdGlvbjogMyxcbiAgcGFyYWdyYXBoOiA0LFxuICBzdWJwYXJhZ3JhcGg6IDVcbn07XG5cbi8qKlxuICogUmVndWxhciBleHByZXNzaW9uIHRvIGNyZWF0ZSB0aGUgb3V0bGluZVxuICovXG5jb25zdCBTRUNUSU9OUyA9IC9eXFxzKlxcXFwoc2VjdGlvbnxzdWJzZWN0aW9ufHN1YnN1YnNlY3Rpb24peyguKyl9LztcblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50IG1vZGVsIGZvciBMYVRlWCBmaWxlcy5cbiAqL1xuZXhwb3J0IGNsYXNzIExhVGVYVGFibGVPZkNvbnRlbnRzTW9kZWwgZXh0ZW5kcyBUYWJsZU9mQ29udGVudHNNb2RlbDxcbiAgSUVkaXRvckhlYWRpbmcsXG4gIElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yLCBEb2N1bWVudFJlZ2lzdHJ5LklNb2RlbD5cbj4ge1xuICAvKipcbiAgICogVHlwZSBvZiBkb2N1bWVudCBzdXBwb3J0ZWQgYnkgdGhlIG1vZGVsLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIEEgYGRhdGEtZG9jdW1lbnQtdHlwZWAgYXR0cmlidXRlIHdpdGggdGhpcyB2YWx1ZSB3aWxsIGJlIHNldFxuICAgKiBvbiB0aGUgdHJlZSB2aWV3IGAuanAtVGFibGVPZkNvbnRlbnRzLWNvbnRlbnRbZGF0YS1kb2N1bWVudC10eXBlPVwiLi4uXCJdYFxuICAgKi9cbiAgZ2V0IGRvY3VtZW50VHlwZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiAnbGF0ZXgnO1xuICB9XG5cbiAgLyoqXG4gICAqIExpc3Qgb2YgY29uZmlndXJhdGlvbiBvcHRpb25zIHN1cHBvcnRlZCBieSB0aGUgbW9kZWwuXG4gICAqL1xuICBnZXQgc3VwcG9ydGVkT3B0aW9ucygpOiAoa2V5b2YgVGFibGVPZkNvbnRlbnRzLklDb25maWcpW10ge1xuICAgIHJldHVybiBbJ21heGltYWxEZXB0aCcsICdudW1iZXJIZWFkZXJzJ107XG4gIH1cblxuICAvKipcbiAgICogUHJvZHVjZSB0aGUgaGVhZGluZ3MgZm9yIGEgZG9jdW1lbnQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBsaXN0IG9mIG5ldyBoZWFkaW5ncyBvciBgbnVsbGAgaWYgbm90aGluZyBuZWVkcyB0byBiZSB1cGRhdGVkLlxuICAgKi9cbiAgcHJvdGVjdGVkIGdldEhlYWRpbmdzKCk6IFByb21pc2U8SUVkaXRvckhlYWRpbmdbXSB8IG51bGw+IHtcbiAgICBpZiAoIXRoaXMuaXNBY3RpdmUpIHtcbiAgICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUobnVsbCk7XG4gICAgfVxuXG4gICAgLy8gU3BsaXQgdGhlIHRleHQgaW50byBsaW5lczpcbiAgICBjb25zdCBsaW5lcyA9IHRoaXMud2lkZ2V0LmNvbnRlbnQubW9kZWwudmFsdWUudGV4dC5zcGxpdChcbiAgICAgICdcXG4nXG4gICAgKSBhcyBBcnJheTxzdHJpbmc+O1xuXG4gICAgY29uc3QgbGV2ZWxzID0gbmV3IEFycmF5PG51bWJlcj4oKTtcbiAgICBsZXQgcHJldmlvdXNMZXZlbCA9IGxldmVscy5sZW5ndGg7XG4gICAgY29uc3QgaGVhZGluZ3MgPSBuZXcgQXJyYXk8SUVkaXRvckhlYWRpbmc+KCk7XG4gICAgZm9yIChsZXQgaSA9IDA7IGkgPCBsaW5lcy5sZW5ndGg7IGkrKykge1xuICAgICAgY29uc3QgbWF0Y2ggPSBsaW5lc1tpXS5tYXRjaChTRUNUSU9OUyk7XG4gICAgICBpZiAobWF0Y2gpIHtcbiAgICAgICAgY29uc3QgbGV2ZWwgPSBMQVRFWF9MRVZFTFNbbWF0Y2hbMV1dO1xuICAgICAgICBpZiAobGV2ZWwgPD0gdGhpcy5jb25maWd1cmF0aW9uLm1heGltYWxEZXB0aCkge1xuICAgICAgICAgIGNvbnN0IHByZWZpeCA9IFRhYmxlT2ZDb250ZW50c1V0aWxzLmdldFByZWZpeChcbiAgICAgICAgICAgIGxldmVsLFxuICAgICAgICAgICAgcHJldmlvdXNMZXZlbCxcbiAgICAgICAgICAgIGxldmVscyxcbiAgICAgICAgICAgIHtcbiAgICAgICAgICAgICAgLi4udGhpcy5jb25maWd1cmF0aW9uLFxuICAgICAgICAgICAgICAvLyBGb3JjZSBiYXNlIG51bWJlcmluZyBhbmQgbnVtYmVyaW5nIGZpcnN0IGxldmVsXG4gICAgICAgICAgICAgIGJhc2VOdW1iZXJpbmc6IDEsXG4gICAgICAgICAgICAgIG51bWJlcmluZ0gxOiB0cnVlXG4gICAgICAgICAgICB9XG4gICAgICAgICAgKTtcbiAgICAgICAgICBwcmV2aW91c0xldmVsID0gbGV2ZWw7XG5cbiAgICAgICAgICBoZWFkaW5ncy5wdXNoKHtcbiAgICAgICAgICAgIHRleHQ6IG1hdGNoWzJdLFxuICAgICAgICAgICAgcHJlZml4OiBwcmVmaXgsXG4gICAgICAgICAgICBsZXZlbCxcbiAgICAgICAgICAgIGxpbmU6IGlcbiAgICAgICAgICB9KTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKGhlYWRpbmdzKTtcbiAgfVxufVxuXG4vKipcbiAqIFRhYmxlIG9mIGNvbnRlbnQgbW9kZWwgZmFjdG9yeSBmb3IgTGFUZVggZmlsZXMuXG4gKi9cbmV4cG9ydCBjbGFzcyBMYVRlWFRhYmxlT2ZDb250ZW50c0ZhY3RvcnkgZXh0ZW5kcyBFZGl0b3JUYWJsZU9mQ29udGVudHNGYWN0b3J5IHtcbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIGZhY3RvcnkgY2FuIGhhbmRsZSB0aGUgd2lkZ2V0IG9yIG5vdC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIHdpZGdldFxuICAgKiBAcmV0dXJucyBib29sZWFuIGluZGljYXRpbmcgYSBUb0MgY2FuIGJlIGdlbmVyYXRlZFxuICAgKi9cbiAgaXNBcHBsaWNhYmxlKHdpZGdldDogV2lkZ2V0KTogYm9vbGVhbiB7XG4gICAgY29uc3QgaXNBcHBsaWNhYmxlID0gc3VwZXIuaXNBcHBsaWNhYmxlKHdpZGdldCk7XG5cbiAgICBpZiAoaXNBcHBsaWNhYmxlKSB7XG4gICAgICBsZXQgbWltZSA9ICh3aWRnZXQgYXMgYW55KS5jb250ZW50Py5tb2RlbD8ubWltZVR5cGU7XG4gICAgICByZXR1cm4gbWltZSAmJiAobWltZSA9PT0gJ3RleHQveC1sYXRleCcgfHwgbWltZSA9PT0gJ3RleHQveC1zdGV4Jyk7XG4gICAgfVxuICAgIHJldHVybiBmYWxzZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgdGFibGUgb2YgY29udGVudHMgbW9kZWwgZm9yIHRoZSB3aWRnZXRcbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIHdpZGdldFxuICAgKiBAcGFyYW0gY29uZmlndXJhdGlvbiAtIFRhYmxlIG9mIGNvbnRlbnRzIGNvbmZpZ3VyYXRpb25cbiAgICogQHJldHVybnMgVGhlIHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsXG4gICAqL1xuICBwcm90ZWN0ZWQgX2NyZWF0ZU5ldyhcbiAgICB3aWRnZXQ6IElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yLCBEb2N1bWVudFJlZ2lzdHJ5LklNb2RlbD4sXG4gICAgY29uZmlndXJhdGlvbj86IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnXG4gICk6IExhVGVYVGFibGVPZkNvbnRlbnRzTW9kZWwge1xuICAgIHJldHVybiBuZXcgTGFUZVhUYWJsZU9mQ29udGVudHNNb2RlbCh3aWRnZXQsIGNvbmZpZ3VyYXRpb24pO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnksIElEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7XG4gIFRhYmxlT2ZDb250ZW50cyxcbiAgVGFibGVPZkNvbnRlbnRzTW9kZWwsXG4gIFRhYmxlT2ZDb250ZW50c1V0aWxzXG59IGZyb20gJ0BqdXB5dGVybGFiL3RvYyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgRmlsZUVkaXRvciB9IGZyb20gJy4uL3dpZGdldCc7XG5pbXBvcnQgeyBFZGl0b3JUYWJsZU9mQ29udGVudHNGYWN0b3J5LCBJRWRpdG9ySGVhZGluZyB9IGZyb20gJy4vZmFjdG9yeSc7XG5cbi8qKlxuICogVGFibGUgb2YgY29udGVudCBtb2RlbCBmb3IgTWFya2Rvd24gZmlsZXMuXG4gKi9cbmV4cG9ydCBjbGFzcyBNYXJrZG93blRhYmxlT2ZDb250ZW50c01vZGVsIGV4dGVuZHMgVGFibGVPZkNvbnRlbnRzTW9kZWw8XG4gIElFZGl0b3JIZWFkaW5nLFxuICBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvciwgRG9jdW1lbnRSZWdpc3RyeS5JTW9kZWw+XG4+IHtcbiAgLyoqXG4gICAqIFR5cGUgb2YgZG9jdW1lbnQgc3VwcG9ydGVkIGJ5IHRoZSBtb2RlbC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBBIGBkYXRhLWRvY3VtZW50LXR5cGVgIGF0dHJpYnV0ZSB3aXRoIHRoaXMgdmFsdWUgd2lsbCBiZSBzZXRcbiAgICogb24gdGhlIHRyZWUgdmlldyBgLmpwLVRhYmxlT2ZDb250ZW50cy1jb250ZW50W2RhdGEtZG9jdW1lbnQtdHlwZT1cIi4uLlwiXWBcbiAgICovXG4gIGdldCBkb2N1bWVudFR5cGUoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gJ21hcmtkb3duJztcbiAgfVxuXG4gIC8qKlxuICAgKiBQcm9kdWNlIHRoZSBoZWFkaW5ncyBmb3IgYSBkb2N1bWVudC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGxpc3Qgb2YgbmV3IGhlYWRpbmdzIG9yIGBudWxsYCBpZiBub3RoaW5nIG5lZWRzIHRvIGJlIHVwZGF0ZWQuXG4gICAqL1xuICBwcm90ZWN0ZWQgZ2V0SGVhZGluZ3MoKTogUHJvbWlzZTxJRWRpdG9ySGVhZGluZ1tdIHwgbnVsbD4ge1xuICAgIGlmICghdGhpcy5pc0FjdGl2ZSkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShudWxsKTtcbiAgICB9XG5cbiAgICBjb25zdCBjb250ZW50ID0gdGhpcy53aWRnZXQuY29udGVudC5tb2RlbC52YWx1ZS50ZXh0O1xuXG4gICAgY29uc3QgaGVhZGluZ3MgPSBUYWJsZU9mQ29udGVudHNVdGlscy5NYXJrZG93bi5nZXRIZWFkaW5ncyhjb250ZW50LCB7XG4gICAgICAuLi50aGlzLmNvbmZpZ3VyYXRpb24sXG4gICAgICAvLyBGb3JjZSByZW1vdmluZyBudW1iZXJpbmcgYXMgdGhleSBjYW5ub3QgYmUgZGlzcGxheWVkXG4gICAgICAvLyBpbiB0aGUgZG9jdW1lbnRcbiAgICAgIG51bWJlckhlYWRlcnM6IGZhbHNlXG4gICAgfSk7XG4gICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShoZWFkaW5ncyk7XG4gIH1cbn1cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50IG1vZGVsIGZhY3RvcnkgZm9yIE1hcmtkb3duIGZpbGVzLlxuICovXG5leHBvcnQgY2xhc3MgTWFya2Rvd25UYWJsZU9mQ29udGVudHNGYWN0b3J5IGV4dGVuZHMgRWRpdG9yVGFibGVPZkNvbnRlbnRzRmFjdG9yeSB7XG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBmYWN0b3J5IGNhbiBoYW5kbGUgdGhlIHdpZGdldCBvciBub3QuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSB3aWRnZXRcbiAgICogQHJldHVybnMgYm9vbGVhbiBpbmRpY2F0aW5nIGEgVG9DIGNhbiBiZSBnZW5lcmF0ZWRcbiAgICovXG4gIGlzQXBwbGljYWJsZSh3aWRnZXQ6IFdpZGdldCk6IGJvb2xlYW4ge1xuICAgIGNvbnN0IGlzQXBwbGljYWJsZSA9IHN1cGVyLmlzQXBwbGljYWJsZSh3aWRnZXQpO1xuXG4gICAgaWYgKGlzQXBwbGljYWJsZSkge1xuICAgICAgbGV0IG1pbWUgPSAod2lkZ2V0IGFzIGFueSkuY29udGVudD8ubW9kZWw/Lm1pbWVUeXBlO1xuICAgICAgcmV0dXJuIG1pbWUgJiYgVGFibGVPZkNvbnRlbnRzVXRpbHMuTWFya2Rvd24uaXNNYXJrZG93bihtaW1lKTtcbiAgICB9XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB0YWJsZSBvZiBjb250ZW50cyBtb2RlbCBmb3IgdGhlIHdpZGdldFxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAqIEBwYXJhbSBjb25maWd1cmF0aW9uIC0gVGFibGUgb2YgY29udGVudHMgY29uZmlndXJhdGlvblxuICAgKiBAcmV0dXJucyBUaGUgdGFibGUgb2YgY29udGVudHMgbW9kZWxcbiAgICovXG4gIHByb3RlY3RlZCBfY3JlYXRlTmV3KFxuICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3IsIERvY3VtZW50UmVnaXN0cnkuSU1vZGVsPixcbiAgICBjb25maWd1cmF0aW9uPzogVGFibGVPZkNvbnRlbnRzLklDb25maWdcbiAgKTogTWFya2Rvd25UYWJsZU9mQ29udGVudHNNb2RlbCB7XG4gICAgcmV0dXJuIG5ldyBNYXJrZG93blRhYmxlT2ZDb250ZW50c01vZGVsKHdpZGdldCwgY29uZmlndXJhdGlvbik7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuLyplc2xpbnQgbm8taW52YWxpZC1yZWdleHA6IFtcImVycm9yXCIsIHsgXCJhbGxvd0NvbnN0cnVjdG9yRmxhZ3NcIjogW1wiZFwiXSB9XSovXG5cbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnksIElEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IFRhYmxlT2ZDb250ZW50cywgVGFibGVPZkNvbnRlbnRzTW9kZWwgfSBmcm9tICdAanVweXRlcmxhYi90b2MnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IEZpbGVFZGl0b3IgfSBmcm9tICcuLi93aWRnZXQnO1xuaW1wb3J0IHsgRWRpdG9yVGFibGVPZkNvbnRlbnRzRmFjdG9yeSwgSUVkaXRvckhlYWRpbmcgfSBmcm9tICcuL2ZhY3RvcnknO1xuXG4vKipcbiAqIFJlZ3VsYXIgZXhwcmVzc2lvbiB0byBjcmVhdGUgdGhlIG91dGxpbmVcbiAqL1xubGV0IEtFWVdPUkRTOiBSZWdFeHA7XG50cnkge1xuICAvLyBodHRwczovL2dpdGh1Yi5jb20vdGMzOS9wcm9wb3NhbC1yZWdleHAtbWF0Y2gtaW5kaWNlcyB3YXMgYWNjZXB0ZWRcbiAgLy8gaW4gTWF5IDIwMjEgKGh0dHBzOi8vZ2l0aHViLmNvbS90YzM5L3Byb3Bvc2Fscy9ibG9iL21haW4vZmluaXNoZWQtcHJvcG9zYWxzLm1kKVxuICAvLyBTbyB3ZSB3aWxsIGZhbGxiYWNrIHRvIHRoZSBwb2x5ZmlsbCByZWdleHAtbWF0Y2gtaW5kaWNlcyBpZiBub3QgYXZhaWxhYmxlXG4gIEtFWVdPUkRTID0gbmV3IFJlZ0V4cCgnXlxcXFxzKihjbGFzcyB8ZGVmIHxmcm9tIHxpbXBvcnQgKScsICdkJyk7XG59IGNhdGNoIHtcbiAgS0VZV09SRFMgPSBuZXcgUmVnRXhwKCdeXFxcXHMqKGNsYXNzIHxkZWYgfGZyb20gfGltcG9ydCApJyk7XG59XG5cbi8qKlxuICogVGFibGUgb2YgY29udGVudCBtb2RlbCBmb3IgUHl0aG9uIGZpbGVzLlxuICovXG5leHBvcnQgY2xhc3MgUHl0aG9uVGFibGVPZkNvbnRlbnRzTW9kZWwgZXh0ZW5kcyBUYWJsZU9mQ29udGVudHNNb2RlbDxcbiAgSUVkaXRvckhlYWRpbmcsXG4gIElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yLCBEb2N1bWVudFJlZ2lzdHJ5LklNb2RlbD5cbj4ge1xuICAvKipcbiAgICogVHlwZSBvZiBkb2N1bWVudCBzdXBwb3J0ZWQgYnkgdGhlIG1vZGVsLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIEEgYGRhdGEtZG9jdW1lbnQtdHlwZWAgYXR0cmlidXRlIHdpdGggdGhpcyB2YWx1ZSB3aWxsIGJlIHNldFxuICAgKiBvbiB0aGUgdHJlZSB2aWV3IGAuanAtVGFibGVPZkNvbnRlbnRzLWNvbnRlbnRbZGF0YS1kb2N1bWVudC10eXBlPVwiLi4uXCJdYFxuICAgKi9cbiAgZ2V0IGRvY3VtZW50VHlwZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiAncHl0aG9uJztcbiAgfVxuXG4gIC8qKlxuICAgKiBQcm9kdWNlIHRoZSBoZWFkaW5ncyBmb3IgYSBkb2N1bWVudC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGxpc3Qgb2YgbmV3IGhlYWRpbmdzIG9yIGBudWxsYCBpZiBub3RoaW5nIG5lZWRzIHRvIGJlIHVwZGF0ZWQuXG4gICAqL1xuICBwcm90ZWN0ZWQgYXN5bmMgZ2V0SGVhZGluZ3MoKTogUHJvbWlzZTxJRWRpdG9ySGVhZGluZ1tdIHwgbnVsbD4ge1xuICAgIGlmICghdGhpcy5pc0FjdGl2ZSkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShudWxsKTtcbiAgICB9XG5cbiAgICAvLyBTcGxpdCB0aGUgdGV4dCBpbnRvIGxpbmVzOlxuICAgIGNvbnN0IGxpbmVzID0gdGhpcy53aWRnZXQuY29udGVudC5tb2RlbC52YWx1ZS50ZXh0LnNwbGl0KFxuICAgICAgJ1xcbidcbiAgICApIGFzIEFycmF5PHN0cmluZz47XG5cbiAgICAvLyBJdGVyYXRlIG92ZXIgdGhlIGxpbmVzIHRvIGdldCB0aGUgaGVhZGluZyBsZXZlbCBhbmQgdGV4dCBmb3IgZWFjaCBsaW5lOlxuICAgIGxldCBoZWFkaW5ncyA9IG5ldyBBcnJheTxJRWRpdG9ySGVhZGluZz4oKTtcbiAgICBsZXQgcHJvY2Vzc2luZ0ltcG9ydHMgPSBmYWxzZTtcblxuICAgIGxldCBpbmRlbnQgPSAxO1xuXG4gICAgbGV0IGxpbmVJZHggPSAtMTtcbiAgICBmb3IgKGNvbnN0IGxpbmUgb2YgbGluZXMpIHtcbiAgICAgIGxpbmVJZHgrKztcbiAgICAgIGxldCBoYXNLZXl3b3JkOiBSZWdFeHBFeGVjQXJyYXkgfCBudWxsO1xuICAgICAgaWYgKEtFWVdPUkRTLmZsYWdzLmluY2x1ZGVzKCdkJykpIHtcbiAgICAgICAgaGFzS2V5d29yZCA9IEtFWVdPUkRTLmV4ZWMobGluZSk7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBjb25zdCB7IGRlZmF1bHQ6IGV4ZWNXaXRoSW5kaWNlcyB9ID0gYXdhaXQgaW1wb3J0KFxuICAgICAgICAgICdyZWdleHAtbWF0Y2gtaW5kaWNlcydcbiAgICAgICAgKTtcbiAgICAgICAgaGFzS2V5d29yZCA9IGV4ZWNXaXRoSW5kaWNlcyhLRVlXT1JEUywgbGluZSk7XG4gICAgICB9XG4gICAgICBpZiAoaGFzS2V5d29yZCkge1xuICAgICAgICAvLyBJbmRleCAwIGNvbnRhaW5zIHRoZSBzcGFjZXMsIGluZGV4IDEgaXMgdGhlIGtleXdvcmQgZ3JvdXBcbiAgICAgICAgY29uc3QgW3N0YXJ0XSA9IChoYXNLZXl3b3JkIGFzIGFueSkuaW5kaWNlc1sxXTtcbiAgICAgICAgaWYgKGluZGVudCA9PT0gMSAmJiBzdGFydCA+IDApIHtcbiAgICAgICAgICBpbmRlbnQgPSBzdGFydDtcbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGlzSW1wb3J0ID0gWydmcm9tICcsICdpbXBvcnQgJ10uaW5jbHVkZXMoaGFzS2V5d29yZFsxXSk7XG4gICAgICAgIGlmIChpc0ltcG9ydCAmJiBwcm9jZXNzaW5nSW1wb3J0cykge1xuICAgICAgICAgIGNvbnRpbnVlO1xuICAgICAgICB9XG4gICAgICAgIHByb2Nlc3NpbmdJbXBvcnRzID0gaXNJbXBvcnQ7XG5cbiAgICAgICAgY29uc3QgbGV2ZWwgPSAxICsgc3RhcnQgLyBpbmRlbnQ7XG5cbiAgICAgICAgaWYgKGxldmVsID4gdGhpcy5jb25maWd1cmF0aW9uLm1heGltYWxEZXB0aCkge1xuICAgICAgICAgIGNvbnRpbnVlO1xuICAgICAgICB9XG5cbiAgICAgICAgaGVhZGluZ3MucHVzaCh7XG4gICAgICAgICAgdGV4dDogbGluZS5zbGljZShzdGFydCksXG4gICAgICAgICAgbGV2ZWwsXG4gICAgICAgICAgbGluZTogbGluZUlkeFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKGhlYWRpbmdzKTtcbiAgfVxufVxuXG4vKipcbiAqIFRhYmxlIG9mIGNvbnRlbnQgbW9kZWwgZmFjdG9yeSBmb3IgUHl0aG9uIGZpbGVzLlxuICovXG5leHBvcnQgY2xhc3MgUHl0aG9uVGFibGVPZkNvbnRlbnRzRmFjdG9yeSBleHRlbmRzIEVkaXRvclRhYmxlT2ZDb250ZW50c0ZhY3Rvcnkge1xuICAvKipcbiAgICogV2hldGhlciB0aGUgZmFjdG9yeSBjYW4gaGFuZGxlIHRoZSB3aWRnZXQgb3Igbm90LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAqIEByZXR1cm5zIGJvb2xlYW4gaW5kaWNhdGluZyBhIFRvQyBjYW4gYmUgZ2VuZXJhdGVkXG4gICAqL1xuICBpc0FwcGxpY2FibGUod2lkZ2V0OiBXaWRnZXQpOiBib29sZWFuIHtcbiAgICBjb25zdCBpc0FwcGxpY2FibGUgPSBzdXBlci5pc0FwcGxpY2FibGUod2lkZ2V0KTtcblxuICAgIGlmIChpc0FwcGxpY2FibGUpIHtcbiAgICAgIGxldCBtaW1lID0gKHdpZGdldCBhcyBhbnkpLmNvbnRlbnQ/Lm1vZGVsPy5taW1lVHlwZTtcbiAgICAgIHJldHVybiAoXG4gICAgICAgIG1pbWUgJiZcbiAgICAgICAgKG1pbWUgPT09ICdhcHBsaWNhdGlvbi94LXB5dGhvbi1jb2RlJyB8fCBtaW1lID09PSAndGV4dC94LXB5dGhvbicpXG4gICAgICApO1xuICAgIH1cbiAgICByZXR1cm4gZmFsc2U7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsIGZvciB0aGUgd2lkZ2V0XG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSB3aWRnZXRcbiAgICogQHBhcmFtIGNvbmZpZ3VyYXRpb24gLSBUYWJsZSBvZiBjb250ZW50cyBjb25maWd1cmF0aW9uXG4gICAqIEByZXR1cm5zIFRoZSB0YWJsZSBvZiBjb250ZW50cyBtb2RlbFxuICAgKi9cbiAgcHJvdGVjdGVkIF9jcmVhdGVOZXcoXG4gICAgd2lkZ2V0OiBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj4sXG4gICAgY29uZmlndXJhdGlvbj86IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnXG4gICk6IFB5dGhvblRhYmxlT2ZDb250ZW50c01vZGVsIHtcbiAgICByZXR1cm4gbmV3IFB5dGhvblRhYmxlT2ZDb250ZW50c01vZGVsKHdpZGdldCwgY29uZmlndXJhdGlvbik7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVdpZGdldFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJRG9jdW1lbnRXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IEZpbGVFZGl0b3IgfSBmcm9tICcuL3dpZGdldCc7XG5cbi8qKlxuICogQSBjbGFzcyB0aGF0IHRyYWNrcyBlZGl0b3Igd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRWRpdG9yVHJhY2tlclxuICBleHRlbmRzIElXaWRnZXRUcmFja2VyPElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yPj4ge31cblxuLyoqXG4gKiBUaGUgZWRpdG9yIHRyYWNrZXIgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJRWRpdG9yVHJhY2tlciA9IG5ldyBUb2tlbjxJRWRpdG9yVHJhY2tlcj4oXG4gICdAanVweXRlcmxhYi9maWxlZWRpdG9yOklFZGl0b3JUcmFja2VyJ1xuKTtcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHtcbiAgQ29kZUVkaXRvcixcbiAgQ29kZUVkaXRvcldyYXBwZXIsXG4gIElFZGl0b3JNaW1lVHlwZVNlcnZpY2UsXG4gIElFZGl0b3JTZXJ2aWNlc1xufSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7XG4gIEFCQ1dpZGdldEZhY3RvcnksXG4gIERvY3VtZW50UmVnaXN0cnksXG4gIERvY3VtZW50V2lkZ2V0LFxuICBJRG9jdW1lbnRXaWRnZXRcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcmVnaXN0cnknO1xuaW1wb3J0IHsgdGV4dEVkaXRvckljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFByb21pc2VEZWxlZ2F0ZSB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBTdGFja2VkTGF5b3V0LCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBkYXRhIGF0dHJpYnV0ZSBhZGRlZCB0byBhIHdpZGdldCB0aGF0IGNhbiBydW4gY29kZS5cbiAqL1xuY29uc3QgQ09ERV9SVU5ORVIgPSAnanBDb2RlUnVubmVyJztcblxuLyoqXG4gKiBUaGUgZGF0YSBhdHRyaWJ1dGUgYWRkZWQgdG8gYSB3aWRnZXQgdGhhdCBjYW4gdW5kby5cbiAqL1xuY29uc3QgVU5ET0VSID0gJ2pwVW5kb2VyJztcblxuLyoqXG4gKiBBIHdpZGdldCBmb3IgZWRpdG9ycy5cbiAqL1xuZXhwb3J0IGNsYXNzIEZpbGVFZGl0b3IgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGVkaXRvciB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBGaWxlRWRpdG9yLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmFkZENsYXNzKCdqcC1GaWxlRWRpdG9yJyk7XG5cbiAgICBjb25zdCBjb250ZXh0ID0gKHRoaXMuX2NvbnRleHQgPSBvcHRpb25zLmNvbnRleHQpO1xuICAgIHRoaXMuX21pbWVUeXBlU2VydmljZSA9IG9wdGlvbnMubWltZVR5cGVTZXJ2aWNlO1xuXG4gICAgY29uc3QgZWRpdG9yV2lkZ2V0ID0gKHRoaXMuX2VkaXRvcldpZGdldCA9IG5ldyBDb2RlRWRpdG9yV3JhcHBlcih7XG4gICAgICBmYWN0b3J5OiBvcHRpb25zLmZhY3RvcnksXG4gICAgICBtb2RlbDogY29udGV4dC5tb2RlbFxuICAgIH0pKTtcbiAgICB0aGlzLl9lZGl0b3JXaWRnZXQuYWRkQ2xhc3MoJ2pwLUZpbGVFZGl0b3JDb2RlV3JhcHBlcicpO1xuICAgIHRoaXMuX2VkaXRvcldpZGdldC5ub2RlLmRhdGFzZXRbQ09ERV9SVU5ORVJdID0gJ3RydWUnO1xuICAgIHRoaXMuX2VkaXRvcldpZGdldC5ub2RlLmRhdGFzZXRbVU5ET0VSXSA9ICd0cnVlJztcblxuICAgIHRoaXMuZWRpdG9yID0gZWRpdG9yV2lkZ2V0LmVkaXRvcjtcbiAgICB0aGlzLm1vZGVsID0gZWRpdG9yV2lkZ2V0Lm1vZGVsO1xuXG4gICAgdm9pZCBjb250ZXh0LnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgdGhpcy5fb25Db250ZXh0UmVhZHkoKTtcbiAgICB9KTtcblxuICAgIC8vIExpc3RlbiBmb3IgY2hhbmdlcyB0byB0aGUgcGF0aC5cbiAgICBjb250ZXh0LnBhdGhDaGFuZ2VkLmNvbm5lY3QodGhpcy5fb25QYXRoQ2hhbmdlZCwgdGhpcyk7XG4gICAgdGhpcy5fb25QYXRoQ2hhbmdlZCgpO1xuXG4gICAgY29uc3QgbGF5b3V0ID0gKHRoaXMubGF5b3V0ID0gbmV3IFN0YWNrZWRMYXlvdXQoKSk7XG4gICAgbGF5b3V0LmFkZFdpZGdldChlZGl0b3JXaWRnZXQpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgY29udGV4dCBmb3IgdGhlIGVkaXRvciB3aWRnZXQuXG4gICAqL1xuICBnZXQgY29udGV4dCgpOiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHQge1xuICAgIHJldHVybiB0aGlzLl9jb250ZXh0O1xuICB9XG5cbiAgLyoqXG4gICAqIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIGZpbGUgZWRpdG9yIGlzIHJlYWR5LlxuICAgKi9cbiAgZ2V0IHJlYWR5KCk6IFByb21pc2U8dm9pZD4ge1xuICAgIHJldHVybiB0aGlzLnJlYWR5O1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgRE9NIGV2ZW50cyBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIGV2ZW50IC0gVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2QgaW1wbGVtZW50cyB0aGUgRE9NIGBFdmVudExpc3RlbmVyYCBpbnRlcmZhY2UgYW5kIGlzXG4gICAqIGNhbGxlZCBpbiByZXNwb25zZSB0byBldmVudHMgb24gdGhlIHdpZGdldCdzIG5vZGUuIEl0IHNob3VsZFxuICAgKiBub3QgYmUgY2FsbGVkIGRpcmVjdGx5IGJ5IHVzZXIgY29kZS5cbiAgICovXG4gIGhhbmRsZUV2ZW50KGV2ZW50OiBFdmVudCk6IHZvaWQge1xuICAgIGlmICghdGhpcy5tb2RlbCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBzd2l0Y2ggKGV2ZW50LnR5cGUpIHtcbiAgICAgIGNhc2UgJ21vdXNlZG93bic6XG4gICAgICAgIHRoaXMuX2Vuc3VyZUZvY3VzKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYWZ0ZXItYXR0YWNoYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHN1cGVyLm9uQWZ0ZXJBdHRhY2gobXNnKTtcbiAgICBjb25zdCBub2RlID0gdGhpcy5ub2RlO1xuICAgIG5vZGUuYWRkRXZlbnRMaXN0ZW5lcignbW91c2Vkb3duJywgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBiZWZvcmUtZGV0YWNoYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBvbkJlZm9yZURldGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBjb25zdCBub2RlID0gdGhpcy5ub2RlO1xuICAgIG5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2Vkb3duJywgdGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnYWN0aXZhdGUtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX2Vuc3VyZUZvY3VzKCk7XG4gIH1cblxuICAvKipcbiAgICogRW5zdXJlIHRoYXQgdGhlIHdpZGdldCBoYXMgZm9jdXMuXG4gICAqL1xuICBwcml2YXRlIF9lbnN1cmVGb2N1cygpOiB2b2lkIHtcbiAgICBpZiAoIXRoaXMuZWRpdG9yLmhhc0ZvY3VzKCkpIHtcbiAgICAgIHRoaXMuZWRpdG9yLmZvY3VzKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhY3Rpb25zIHRoYXQgc2hvdWxkIGJlIHRha2VuIHdoZW4gdGhlIGNvbnRleHQgaXMgcmVhZHkuXG4gICAqL1xuICBwcml2YXRlIF9vbkNvbnRleHRSZWFkeSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgLy8gUHJldmVudCB0aGUgaW5pdGlhbCBsb2FkaW5nIGZyb20gZGlzayBmcm9tIGJlaW5nIGluIHRoZSBlZGl0b3IgaGlzdG9yeS5cbiAgICB0aGlzLmVkaXRvci5jbGVhckhpc3RvcnkoKTtcbiAgICAvLyBSZXNvbHZlIHRoZSByZWFkeSBwcm9taXNlLlxuICAgIHRoaXMuX3JlYWR5LnJlc29sdmUodW5kZWZpbmVkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIHBhdGguXG4gICAqL1xuICBwcml2YXRlIF9vblBhdGhDaGFuZ2VkKCk6IHZvaWQge1xuICAgIGNvbnN0IGVkaXRvciA9IHRoaXMuZWRpdG9yO1xuICAgIGNvbnN0IGxvY2FsUGF0aCA9IHRoaXMuX2NvbnRleHQubG9jYWxQYXRoO1xuXG4gICAgZWRpdG9yLm1vZGVsLm1pbWVUeXBlID1cbiAgICAgIHRoaXMuX21pbWVUeXBlU2VydmljZS5nZXRNaW1lVHlwZUJ5RmlsZVBhdGgobG9jYWxQYXRoKTtcbiAgfVxuXG4gIG1vZGVsOiBDb2RlRWRpdG9yLklNb2RlbDtcbiAgZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3I7XG4gIHByaXZhdGUgX2NvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dDtcbiAgcHJpdmF0ZSBfZWRpdG9yV2lkZ2V0OiBDb2RlRWRpdG9yV3JhcHBlcjtcbiAgcHJpdmF0ZSBfbWltZVR5cGVTZXJ2aWNlOiBJRWRpdG9yTWltZVR5cGVTZXJ2aWNlO1xuICBwcml2YXRlIF9yZWFkeSA9IG5ldyBQcm9taXNlRGVsZWdhdGU8dm9pZD4oKTtcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBlZGl0b3Igd2lkZ2V0IHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgRmlsZUVkaXRvciB7XG4gIC8qKlxuICAgKiBUaGUgb3B0aW9ucyB1c2VkIHRvIGNyZWF0ZSBhbiBlZGl0b3Igd2lkZ2V0LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogQSBjb2RlIGVkaXRvciBmYWN0b3J5LlxuICAgICAqL1xuICAgIGZhY3Rvcnk6IENvZGVFZGl0b3IuRmFjdG9yeTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBtaW1lIHR5cGUgc2VydmljZSBmb3IgdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBtaW1lVHlwZVNlcnZpY2U6IElFZGl0b3JNaW1lVHlwZVNlcnZpY2U7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZG9jdW1lbnQgY29udGV4dCBhc3NvY2lhdGVkIHdpdGggdGhlIGVkaXRvci5cbiAgICAgKi9cbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvZGVDb250ZXh0O1xuICB9XG59XG5cbi8qKlxuICogQSB3aWRnZXQgZmFjdG9yeSBmb3IgZWRpdG9ycy5cbiAqL1xuZXhwb3J0IGNsYXNzIEZpbGVFZGl0b3JGYWN0b3J5IGV4dGVuZHMgQUJDV2lkZ2V0RmFjdG9yeTxcbiAgSURvY3VtZW50V2lkZ2V0PEZpbGVFZGl0b3I+LFxuICBEb2N1bWVudFJlZ2lzdHJ5LklDb2RlTW9kZWxcbj4ge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IGVkaXRvciB3aWRnZXQgZmFjdG9yeS5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IEZpbGVFZGl0b3JGYWN0b3J5LklPcHRpb25zKSB7XG4gICAgc3VwZXIob3B0aW9ucy5mYWN0b3J5T3B0aW9ucyk7XG4gICAgdGhpcy5fc2VydmljZXMgPSBvcHRpb25zLmVkaXRvclNlcnZpY2VzO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB3aWRnZXQgZ2l2ZW4gYSBjb250ZXh0LlxuICAgKi9cbiAgcHJvdGVjdGVkIGNyZWF0ZU5ld1dpZGdldChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvZGVDb250ZXh0XG4gICk6IElEb2N1bWVudFdpZGdldDxGaWxlRWRpdG9yPiB7XG4gICAgY29uc3QgZnVuYyA9IHRoaXMuX3NlcnZpY2VzLmZhY3RvcnlTZXJ2aWNlLm5ld0RvY3VtZW50RWRpdG9yO1xuICAgIGNvbnN0IGZhY3Rvcnk6IENvZGVFZGl0b3IuRmFjdG9yeSA9IG9wdGlvbnMgPT4ge1xuICAgICAgcmV0dXJuIGZ1bmMob3B0aW9ucyk7XG4gICAgfTtcbiAgICBjb25zdCBjb250ZW50ID0gbmV3IEZpbGVFZGl0b3Ioe1xuICAgICAgZmFjdG9yeSxcbiAgICAgIGNvbnRleHQsXG4gICAgICBtaW1lVHlwZVNlcnZpY2U6IHRoaXMuX3NlcnZpY2VzLm1pbWVUeXBlU2VydmljZVxuICAgIH0pO1xuXG4gICAgY29udGVudC50aXRsZS5pY29uID0gdGV4dEVkaXRvckljb247XG4gICAgY29uc3Qgd2lkZ2V0ID0gbmV3IERvY3VtZW50V2lkZ2V0KHsgY29udGVudCwgY29udGV4dCB9KTtcbiAgICByZXR1cm4gd2lkZ2V0O1xuICB9XG5cbiAgcHJpdmF0ZSBfc2VydmljZXM6IElFZGl0b3JTZXJ2aWNlcztcbn1cblxuLyoqXG4gKiBUaGUgbmFtZXNwYWNlIGZvciBgRmlsZUVkaXRvckZhY3RvcnlgIGNsYXNzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgRmlsZUVkaXRvckZhY3Rvcnkge1xuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdXNlZCB0byBjcmVhdGUgYW4gZWRpdG9yIHdpZGdldCBmYWN0b3J5LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGVkaXRvciBzZXJ2aWNlcyB1c2VkIGJ5IHRoZSBmYWN0b3J5LlxuICAgICAqL1xuICAgIGVkaXRvclNlcnZpY2VzOiBJRWRpdG9yU2VydmljZXM7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZmFjdG9yeSBvcHRpb25zIGFzc29jaWF0ZWQgd2l0aCB0aGUgZmFjdG9yeS5cbiAgICAgKi9cbiAgICBmYWN0b3J5T3B0aW9uczogRG9jdW1lbnRSZWdpc3RyeS5JV2lkZ2V0RmFjdG9yeU9wdGlvbnM8XG4gICAgICBJRG9jdW1lbnRXaWRnZXQ8RmlsZUVkaXRvcj5cbiAgICA+O1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=