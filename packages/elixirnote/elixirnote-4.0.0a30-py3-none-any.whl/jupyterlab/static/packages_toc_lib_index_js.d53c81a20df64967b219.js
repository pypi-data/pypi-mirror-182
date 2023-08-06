"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_toc_lib_index_js"],{

/***/ "../../packages/toc/lib/factory.js":
/*!*****************************************!*\
  !*** ../../packages/toc/lib/factory.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsFactory": () => (/* binding */ TableOfContentsFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Timeout for throttling ToC rendering following model changes.
 *
 * @private
 */
const RENDER_TIMEOUT = 1000;
/**
 * Abstract table of contents model factory for IDocumentWidget.
 */
class TableOfContentsFactory {
    /**
     * Constructor
     *
     * @param tracker Widget tracker
     */
    constructor(tracker) {
        this.tracker = tracker;
    }
    /**
     * Whether the factory can handle the widget or not.
     *
     * @param widget - widget
     * @returns boolean indicating a ToC can be generated
     */
    isApplicable(widget) {
        if (!this.tracker.has(widget)) {
            return false;
        }
        return true;
    }
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    createNew(widget, configuration) {
        const model = this._createNew(widget, configuration);
        const context = widget.context;
        const updateHeadings = () => {
            model.refresh().catch(reason => {
                console.error('Failed to update the table of contents.', reason);
            });
        };
        const monitor = new _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.ActivityMonitor({
            signal: context.model.contentChanged,
            timeout: RENDER_TIMEOUT
        });
        monitor.activityStopped.connect(updateHeadings);
        const updateTitle = () => {
            model.title = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PathExt.basename(context.localPath);
        };
        context.pathChanged.connect(updateTitle);
        context.ready
            .then(() => {
            updateTitle();
            updateHeadings();
        })
            .catch(reason => {
            console.error(`Failed to initiate headings for ${context.localPath}.`);
        });
        widget.disposed.connect(() => {
            monitor.activityStopped.disconnect(updateHeadings);
            context.pathChanged.disconnect(updateTitle);
        });
        return model;
    }
}


/***/ }),

/***/ "../../packages/toc/lib/index.js":
/*!***************************************!*\
  !*** ../../packages/toc/lib/index.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITableOfContentsRegistry": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_7__.ITableOfContentsRegistry),
/* harmony export */   "ITableOfContentsTracker": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_7__.ITableOfContentsTracker),
/* harmony export */   "TableOfContents": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_7__.TableOfContents),
/* harmony export */   "TableOfContentsFactory": () => (/* reexport safe */ _factory__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsFactory),
/* harmony export */   "TableOfContentsItem": () => (/* reexport safe */ _tocitem__WEBPACK_IMPORTED_MODULE_5__.TableOfContentsItem),
/* harmony export */   "TableOfContentsModel": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_1__.TableOfContentsModel),
/* harmony export */   "TableOfContentsPanel": () => (/* reexport safe */ _panel__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsPanel),
/* harmony export */   "TableOfContentsRegistry": () => (/* reexport safe */ _registry__WEBPACK_IMPORTED_MODULE_3__.TableOfContentsRegistry),
/* harmony export */   "TableOfContentsTracker": () => (/* reexport safe */ _tracker__WEBPACK_IMPORTED_MODULE_8__.TableOfContentsTracker),
/* harmony export */   "TableOfContentsTree": () => (/* reexport safe */ _toctree__WEBPACK_IMPORTED_MODULE_6__.TableOfContentsTree),
/* harmony export */   "TableOfContentsUtils": () => (/* reexport module object */ _utils__WEBPACK_IMPORTED_MODULE_9__),
/* harmony export */   "TableOfContentsWidget": () => (/* reexport safe */ _treeview__WEBPACK_IMPORTED_MODULE_4__.TableOfContentsWidget)
/* harmony export */ });
/* harmony import */ var _factory__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./factory */ "../../packages/toc/lib/factory.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./model */ "../../packages/toc/lib/model.js");
/* harmony import */ var _panel__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./panel */ "../../packages/toc/lib/panel.js");
/* harmony import */ var _registry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./registry */ "../../packages/toc/lib/registry.js");
/* harmony import */ var _treeview__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./treeview */ "../../packages/toc/lib/treeview.js");
/* harmony import */ var _tocitem__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./tocitem */ "../../packages/toc/lib/tocitem.js");
/* harmony import */ var _toctree__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./toctree */ "../../packages/toc/lib/toctree.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./tokens */ "../../packages/toc/lib/tokens.js");
/* harmony import */ var _tracker__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./tracker */ "../../packages/toc/lib/tracker.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./utils */ "../../packages/toc/lib/utils/index.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module toc
 */









// Namespace the utils



/***/ }),

/***/ "../../packages/toc/lib/model.js":
/*!***************************************!*\
  !*** ../../packages/toc/lib/model.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsModel": () => (/* binding */ TableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./tokens */ "../../packages/toc/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * Abstract table of contents model.
 */
class TableOfContentsModel extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.VDomModel {
    /**
     * Constructor
     *
     * @param widget The widget to search in
     * @param configuration Default model configuration
     */
    constructor(widget, configuration) {
        super();
        this.widget = widget;
        this._activeHeading = null;
        this._activeHeadingChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._collapseChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._configuration = configuration !== null && configuration !== void 0 ? configuration : Object.assign({}, _tokens__WEBPACK_IMPORTED_MODULE_3__.TableOfContents.defaultConfig);
        this._headings = new Array();
        this._headingsChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._isActive = false;
        this._isRefreshing = false;
        this._needsRefreshing = false;
    }
    /**
     * Current active entry.
     *
     * @returns table of contents active entry
     */
    get activeHeading() {
        return this._activeHeading;
    }
    /**
     * Signal emitted when the active heading changes.
     */
    get activeHeadingChanged() {
        return this._activeHeadingChanged;
    }
    /**
     * Signal emitted when a table of content section collapse state changes.
     */
    get collapseChanged() {
        return this._collapseChanged;
    }
    /**
     * Model configuration
     */
    get configuration() {
        return this._configuration;
    }
    /**
     * List of headings.
     *
     * @returns table of contents list of headings
     */
    get headings() {
        return this._headings;
    }
    /**
     * Signal emitted when the headings changes.
     */
    get headingsChanged() {
        return this._headingsChanged;
    }
    /**
     * Whether the model is active or not.
     *
     * #### Notes
     * An active model means it is displayed in the table of contents.
     * This can be used by subclass to limit updating the headings.
     */
    get isActive() {
        return this._isActive;
    }
    set isActive(v) {
        this._isActive = v;
        // Refresh on activation expect if it is always active
        //  => a ToC model is always active e.g. when displaying numbering in the document
        if (this._isActive && !this.isAlwaysActive) {
            this.refresh().catch(reason => {
                console.error('Failed to refresh ToC model.', reason);
            });
        }
    }
    /**
     * Whether the model gets updated even if the table of contents panel
     * is hidden or not.
     *
     * #### Notes
     * For example, ToC models use to add title numbering will
     * set this to true.
     */
    get isAlwaysActive() {
        return false;
    }
    /**
     * List of configuration options supported by the model.
     */
    get supportedOptions() {
        return ['maximalDepth'];
    }
    /**
     * Document title
     */
    get title() {
        return this._title;
    }
    set title(v) {
        if (v !== this._title) {
            this._title = v;
            this.stateChanged.emit();
        }
    }
    /**
     * Refresh the headings list.
     */
    async refresh() {
        if (this._isRefreshing) {
            // Schedule a refresh if one is in progress
            this._needsRefreshing = true;
            return Promise.resolve();
        }
        this._isRefreshing = true;
        try {
            const newHeadings = await this.getHeadings();
            if (this._needsRefreshing) {
                this._needsRefreshing = false;
                this._isRefreshing = false;
                return this.refresh();
            }
            if (newHeadings &&
                !Private.areHeadingsEqual(newHeadings, this._headings)) {
                this._headings = newHeadings;
                this.stateChanged.emit();
                this._headingsChanged.emit();
            }
        }
        finally {
            this._isRefreshing = false;
        }
    }
    /**
     * Set a new active heading.
     *
     * @param heading The new active heading
     * @param emitSignal Whether to emit the activeHeadingChanged signal or not.
     */
    setActiveHeading(heading, emitSignal = true) {
        if (this._activeHeading !== heading) {
            this._activeHeading = heading;
            this.stateChanged.emit();
            if (emitSignal) {
                this._activeHeadingChanged.emit(heading);
            }
        }
    }
    /**
     * Model configuration setter.
     *
     * @param c New configuration
     */
    setConfiguration(c) {
        const newConfiguration = Object.assign(Object.assign({}, this._configuration), c);
        if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(this._configuration, newConfiguration)) {
            this._configuration = newConfiguration;
            this.refresh().catch(reason => {
                console.error('Failed to update the table of contents.', reason);
            });
        }
    }
    /**
     * Callback on heading collapse.
     *
     * @param options.heading The heading to change state (all headings if not provided)
     * @param options.collapsed The new collapsed status (toggle existing status if not provided)
     */
    toggleCollapse(options) {
        var _a, _b;
        if (options.heading) {
            options.heading.collapsed =
                (_a = options.collapsed) !== null && _a !== void 0 ? _a : !options.heading.collapsed;
            this.stateChanged.emit();
            this._collapseChanged.emit(options.heading);
        }
        else {
            // Use the provided state or collapsed all except if all are collapsed
            const newState = (_b = options.collapsed) !== null && _b !== void 0 ? _b : !this.headings.some(h => { var _a; return !((_a = h.collapsed) !== null && _a !== void 0 ? _a : false); });
            this.headings.forEach(h => (h.collapsed = newState));
            this.stateChanged.emit();
            this._collapseChanged.emit(null);
        }
    }
}
/**
 * Private functions namespace
 */
var Private;
(function (Private) {
    /**
     * Test if two list of headings are equal or not.
     *
     * @param headings1 First list of headings
     * @param headings2 Second list of headings
     * @returns Whether the array are identical or not.
     */
    function areHeadingsEqual(headings1, headings2) {
        if (headings1.length === headings2.length) {
            for (let i = 0; i < headings1.length; i++) {
                if (headings1[i].level !== headings2[i].level ||
                    headings1[i].text !== headings2[i].text ||
                    headings1[i].prefix !== headings2[i].prefix) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }
    Private.areHeadingsEqual = areHeadingsEqual;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/toc/lib/panel.js":
/*!***************************************!*\
  !*** ../../packages/toc/lib/panel.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsPanel": () => (/* binding */ TableOfContentsPanel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _treeview__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./treeview */ "../../packages/toc/lib/treeview.js");
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */



/**
 * Table of contents sidebar panel.
 */
class TableOfContentsPanel extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.SidePanel {
    /**
     * Constructor
     *
     * @param translator - Translator tool
     */
    constructor(translator) {
        super({ content: new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Panel(), translator });
        this._model = null;
        this.addClass('jp-TableOfContents');
        this._title = new Private.Header(this._trans.__('Table of Contents'));
        this.header.addWidget(this._title);
        this._treeview = new _treeview__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsWidget();
        this._treeview.addClass('jp-TableOfContents-tree');
        this.content.addWidget(this._treeview);
    }
    /**
     * Get the current model.
     */
    get model() {
        return this._model;
    }
    set model(newValue) {
        var _a, _b;
        if (this._model !== newValue) {
            (_a = this._model) === null || _a === void 0 ? void 0 : _a.stateChanged.disconnect(this._onTitleChanged, this);
            this._model = newValue;
            if (this._model) {
                this._model.isActive = this.isVisible;
            }
            (_b = this._model) === null || _b === void 0 ? void 0 : _b.stateChanged.connect(this._onTitleChanged, this);
            this._onTitleChanged();
            this._treeview.model = this._model;
        }
    }
    onAfterHide(msg) {
        super.onAfterHide(msg);
        if (this._model) {
            this._model.isActive = false;
        }
    }
    onBeforeShow(msg) {
        super.onBeforeShow(msg);
        if (this._model) {
            this._model.isActive = true;
        }
    }
    _onTitleChanged() {
        var _a, _b;
        this._title.setTitle((_b = (_a = this._model) === null || _a === void 0 ? void 0 : _a.title) !== null && _b !== void 0 ? _b : this._trans.__('Table of Contents'));
    }
}
/**
 * Private helpers namespace
 */
var Private;
(function (Private) {
    /**
     * Panel header
     */
    class Header extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget {
        /**
         * Constructor
         *
         * @param title - Title text
         */
        constructor(title) {
            const node = document.createElement('h2');
            node.textContent = title;
            node.classList.add('jp-text-truncated');
            super({ node });
            this._title = node;
        }
        /**
         * Set the header title.
         */
        setTitle(title) {
            this._title.textContent = title;
        }
    }
    Private.Header = Header;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/toc/lib/registry.js":
/*!******************************************!*\
  !*** ../../packages/toc/lib/registry.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsRegistry": () => (/* binding */ TableOfContentsRegistry)
/* harmony export */ });
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Class for registering table of contents generators.
 */
class TableOfContentsRegistry {
    constructor() {
        this._generators = new Map();
        this._idCounter = 0;
    }
    /**
     * Finds a table of contents model for a widget.
     *
     * ## Notes
     *
     * -   If unable to find a table of contents model, the method return `undefined`.
     *
     * @param widget - widget
     * @param configuration - Default model configuration
     * @returns Table of contents model
     */
    getModel(widget, configuration) {
        for (const generator of this._generators.values()) {
            if (generator.isApplicable(widget)) {
                return generator.createNew(widget, configuration);
            }
        }
    }
    /**
     * Adds a table of contents generator to the registry.
     *
     * @param generator - table of contents generator
     */
    add(generator) {
        const id = this._idCounter++;
        this._generators.set(id, generator);
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__.DisposableDelegate(() => {
            this._generators.delete(id);
        });
    }
}


/***/ }),

/***/ "../../packages/toc/lib/tocitem.js":
/*!*****************************************!*\
  !*** ../../packages/toc/lib/tocitem.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsItem": () => (/* binding */ TableOfContentsItem)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * React component for a table of contents entry.
 */
class TableOfContentsItem extends react__WEBPACK_IMPORTED_MODULE_1__.PureComponent {
    /**
     * Renders a table of contents entry.
     *
     * @returns rendered entry
     */
    render() {
        const { children, isActive, heading, onCollapse, onMouseDown } = this.props;
        return (react__WEBPACK_IMPORTED_MODULE_1__.createElement("li", { className: "jp-tocItem", key: `${heading.level}-${heading.text}` },
            react__WEBPACK_IMPORTED_MODULE_1__.createElement("div", { className: `jp-tocItem-heading ${isActive ? 'jp-tocItem-active' : ''}`, onMouseDown: (event) => {
                    // React only on deepest item
                    if (!event.defaultPrevented) {
                        event.preventDefault();
                        onMouseDown(heading);
                    }
                } },
                react__WEBPACK_IMPORTED_MODULE_1__.createElement("button", { className: "jp-tocItem-collapser", onClick: (event) => {
                        event.preventDefault();
                        onCollapse(heading);
                    }, style: { visibility: children ? 'visible' : 'hidden' } }, heading.collapsed ? (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.caretRightIcon.react, { tag: "span", width: "20px" })) : (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.caretDownIcon.react, { tag: "span", width: "20px" }))),
                react__WEBPACK_IMPORTED_MODULE_1__.createElement("span", Object.assign({ className: "jp-tocItem-content", title: heading.text }, heading.dataset),
                    heading.prefix,
                    heading.text)),
            children && !heading.collapsed && react__WEBPACK_IMPORTED_MODULE_1__.createElement("ol", null, children)));
    }
}


/***/ }),

/***/ "../../packages/toc/lib/toctree.js":
/*!*****************************************!*\
  !*** ../../packages/toc/lib/toctree.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsTree": () => (/* binding */ TableOfContentsTree)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _tocitem__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tocitem */ "../../packages/toc/lib/tocitem.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * React component for a table of contents tree.
 */
class TableOfContentsTree extends react__WEBPACK_IMPORTED_MODULE_0__.PureComponent {
    /**
     * Renders a table of contents tree.
     */
    render() {
        const { documentType } = this.props;
        return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("ol", Object.assign({ className: "jp-TableOfContents-content" }, { 'data-document-type': documentType }), this.buildTree()));
    }
    /**
     * Convert the flat headings list to a nested tree list
     */
    buildTree() {
        if (this.props.headings.length === 0) {
            return [];
        }
        let globalIndex = 0;
        const getChildren = (items, level) => {
            const nested = new Array();
            while (globalIndex < items.length) {
                const current = items[globalIndex];
                if (current.level >= level) {
                    globalIndex += 1;
                    const next = items[globalIndex];
                    nested.push(react__WEBPACK_IMPORTED_MODULE_0__.createElement(_tocitem__WEBPACK_IMPORTED_MODULE_1__.TableOfContentsItem, { key: `${current.level}-${current.text}`, isActive: !!this.props.activeHeading &&
                            current === this.props.activeHeading, heading: current, onMouseDown: this.props.setActiveHeading, onCollapse: this.props.onCollapseChange }, next && next.level > level && getChildren(items, level + 1)));
                }
                else {
                    break;
                }
            }
            return nested;
        };
        return getChildren(this.props.headings, this.props.headings[0].level);
    }
}


/***/ }),

/***/ "../../packages/toc/lib/tokens.js":
/*!****************************************!*\
  !*** ../../packages/toc/lib/tokens.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITableOfContentsRegistry": () => (/* binding */ ITableOfContentsRegistry),
/* harmony export */   "ITableOfContentsTracker": () => (/* binding */ ITableOfContentsTracker),
/* harmony export */   "TableOfContents": () => (/* binding */ TableOfContents)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Table of contents registry token.
 */
const ITableOfContentsRegistry = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/toc:ITableOfContentsRegistry');
/**
 * Table of contents tracker token.
 */
const ITableOfContentsTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/toc:ITableOfContentsTracker');
/**
 * Namespace for table of contents interface
 */
var TableOfContents;
(function (TableOfContents) {
    /**
     * Default table of content configuration
     */
    TableOfContents.defaultConfig = {
        baseNumbering: 1,
        maximalDepth: 4,
        numberingH1: true,
        numberHeaders: false,
        includeOutput: true,
        syncCollapseState: false
    };
})(TableOfContents || (TableOfContents = {}));


/***/ }),

/***/ "../../packages/toc/lib/tracker.js":
/*!*****************************************!*\
  !*** ../../packages/toc/lib/tracker.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsTracker": () => (/* binding */ TableOfContentsTracker)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * Table of contents tracker
 */
class TableOfContentsTracker {
    /**
     * Constructor
     */
    constructor() {
        this.modelMapping = new WeakMap();
    }
    /**
     * Track a given model.
     *
     * @param widget Widget
     * @param model Table of contents model
     */
    add(widget, model) {
        this.modelMapping.set(widget, model);
    }
    /**
     * Get the table of contents model associated with a given widget.
     *
     * @param widget Widget
     * @returns The table of contents model
     */
    get(widget) {
        const model = this.modelMapping.get(widget);
        return !model || model.isDisposed ? null : model;
    }
}


/***/ }),

/***/ "../../packages/toc/lib/treeview.js":
/*!******************************************!*\
  !*** ../../packages/toc/lib/treeview.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TableOfContentsWidget": () => (/* binding */ TableOfContentsWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _toctree__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./toctree */ "../../packages/toc/lib/toctree.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Table of contents widget.
 */
class TableOfContentsWidget extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.VDomRenderer {
    /**
     * Constructor
     *
     * @param options Widget options
     */
    constructor(options = {}) {
        super(options.model);
    }
    /**
     * Render the content of this widget using the virtual DOM.
     *
     * This method will be called anytime the widget needs to be rendered, which
     * includes layout triggered rendering.
     */
    render() {
        if (!this.model) {
            return null;
        }
        return (react__WEBPACK_IMPORTED_MODULE_1__.createElement(_toctree__WEBPACK_IMPORTED_MODULE_2__.TableOfContentsTree, { activeHeading: this.model.activeHeading, documentType: this.model.documentType, headings: this.model.headings, onCollapseChange: (heading) => {
                this.model.toggleCollapse({ heading });
            }, setActiveHeading: (heading) => {
                this.model.setActiveHeading(heading);
            } }));
    }
}


/***/ }),

/***/ "../../packages/toc/lib/utils/common.js":
/*!**********************************************!*\
  !*** ../../packages/toc/lib/utils/common.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NUMBERING_CLASS": () => (/* binding */ NUMBERING_CLASS),
/* harmony export */   "addPrefix": () => (/* binding */ addPrefix),
/* harmony export */   "clearNumbering": () => (/* binding */ clearNumbering),
/* harmony export */   "getHTMLHeadings": () => (/* binding */ getHTMLHeadings),
/* harmony export */   "getPrefix": () => (/* binding */ getPrefix),
/* harmony export */   "isHTML": () => (/* binding */ isHTML)
/* harmony export */ });
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../tokens */ "../../packages/toc/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Class used to mark numbering prefix for headings in a document.
 */
const NUMBERING_CLASS = 'numbering-entry';
/**
 * Returns whether a MIME type corresponds to either HTML.
 *
 * @param mime - MIME type string
 * @returns boolean indicating whether a provided MIME type corresponds to either HTML
 *
 * @example
 * const bool = isHTML('text/html');
 * // returns true
 *
 * @example
 * const bool = isHTML('text/plain');
 * // returns false
 */
function isHTML(mime) {
    return mime === 'text/html';
}
/**
 * Parse a HTML string for headings.
 *
 * ### Notes
 * The html string is not sanitized - use with caution
 *
 * @param html HTML string to parse
 * @param options Options
 * @param initialLevels Initial levels for prefix computation
 * @returns Extracted headings
 */
function getHTMLHeadings(html, options, initialLevels = []) {
    var _a;
    const config = Object.assign(Object.assign({}, _tokens__WEBPACK_IMPORTED_MODULE_0__.TableOfContents.defaultConfig), options);
    const container = document.createElement('div');
    container.innerHTML = html;
    const levels = initialLevels;
    let previousLevel = levels.length;
    const headings = new Array();
    const headers = container.querySelectorAll('h1, h2, h3, h4, h5, h6');
    for (const h of headers) {
        if (h.classList.contains('jp-toc-ignore') ||
            h.classList.contains('tocSkip')) {
            // skip this element if a special class name is included
            continue;
        }
        let level = parseInt(h.tagName[1], 10);
        if (level > 0 && level <= config.maximalDepth) {
            const prefix = getPrefix(level, previousLevel, levels, config);
            previousLevel = level;
            headings.push({
                text: (_a = h.textContent) !== null && _a !== void 0 ? _a : '',
                prefix,
                level,
                id: h === null || h === void 0 ? void 0 : h.getAttribute('id')
            });
        }
    }
    return headings;
}
/**
 * Add an heading prefix to a HTML node.
 *
 * @param container HTML node containing the heading
 * @param selector Heading selector
 * @param prefix Title prefix to add
 * @returns The modified HTML element
 */
function addPrefix(container, selector, prefix) {
    let element = container.querySelector(selector);
    if (!element) {
        return null;
    }
    if (!element.querySelector(`span.${NUMBERING_CLASS}`)) {
        addNumbering(element, prefix);
    }
    else {
        // There are likely multiple elements with the same selector
        //  => use the first one without prefix
        const allElements = container.querySelectorAll(selector);
        for (const el of allElements) {
            if (!el.querySelector(`span.${NUMBERING_CLASS}`)) {
                element = el;
                addNumbering(el, prefix);
                break;
            }
        }
    }
    return element;
}
/**
 * Update the levels and create the numbering prefix
 *
 * @param level Current level
 * @param previousLevel Previous level
 * @param levels Levels list
 * @param options Options
 * @returns The numbering prefix
 */
function getPrefix(level, previousLevel, levels, options) {
    const { baseNumbering, numberingH1, numberHeaders } = options;
    let prefix = '';
    if (numberHeaders) {
        const highestLevel = numberingH1 ? 1 : 2;
        if (level > previousLevel) {
            // Initialize the new levels
            for (let l = previousLevel; l < level - 1; l++) {
                levels[l] = 0;
            }
            levels[level - 1] = level === highestLevel ? baseNumbering : 1;
        }
        else {
            // Increment the current level
            levels[level - 1] += 1;
            // Drop higher levels
            if (level < previousLevel) {
                levels.splice(level);
            }
        }
        // If the header list skips some level, replace missing elements by 0
        if (numberingH1) {
            prefix = levels.map(level => level !== null && level !== void 0 ? level : 0).join('.') + '. ';
        }
        else {
            if (levels.length > 1) {
                prefix =
                    levels
                        .slice(1)
                        .map(level => level !== null && level !== void 0 ? level : 0)
                        .join('.') + '. ';
            }
        }
    }
    return prefix;
}
/**
 * Add a numbering prefix to a HTML element.
 *
 * @param el HTML element
 * @param numbering Numbering prefix to add
 */
function addNumbering(el, numbering) {
    el.insertAdjacentHTML('afterbegin', `<span class="${NUMBERING_CLASS}">${numbering}</span>`);
}
/**
 * Remove all numbering nodes from element
 * @param element Node to clear
 */
function clearNumbering(element) {
    element.querySelectorAll(`span.${NUMBERING_CLASS}`).forEach(el => {
        el.remove();
    });
}


/***/ }),

/***/ "../../packages/toc/lib/utils/index.js":
/*!*********************************************!*\
  !*** ../../packages/toc/lib/utils/index.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Markdown": () => (/* reexport module object */ _markdown__WEBPACK_IMPORTED_MODULE_1__),
/* harmony export */   "NUMBERING_CLASS": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.NUMBERING_CLASS),
/* harmony export */   "addPrefix": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.addPrefix),
/* harmony export */   "clearNumbering": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.clearNumbering),
/* harmony export */   "getHTMLHeadings": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.getHTMLHeadings),
/* harmony export */   "getPrefix": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.getPrefix),
/* harmony export */   "isHTML": () => (/* reexport safe */ _common__WEBPACK_IMPORTED_MODULE_0__.isHTML)
/* harmony export */ });
/* harmony import */ var _common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./common */ "../../packages/toc/lib/utils/common.js");
/* harmony import */ var _markdown__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./markdown */ "../../packages/toc/lib/utils/markdown.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/***/ }),

/***/ "../../packages/toc/lib/utils/markdown.js":
/*!************************************************!*\
  !*** ../../packages/toc/lib/utils/markdown.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getHeadingId": () => (/* binding */ getHeadingId),
/* harmony export */   "getHeadings": () => (/* binding */ getHeadings),
/* harmony export */   "isMarkdown": () => (/* binding */ isMarkdown)
/* harmony export */ });
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../tokens */ "../../packages/toc/lib/tokens.js");
/* harmony import */ var _common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./common */ "../../packages/toc/lib/utils/common.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Build the heading html id.
 *
 * @param raw Raw markdown heading
 * @param level Heading level
 */
async function getHeadingId(parser, raw, level) {
    try {
        const innerHTML = await parser.render(raw);
        if (!innerHTML) {
            return null;
        }
        const container = document.createElement('div');
        container.innerHTML = innerHTML;
        const header = container.querySelector(`h${level}`);
        if (!header) {
            return null;
        }
        return _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.renderMarkdown.createHeaderId(header);
    }
    catch (reason) {
        console.error('Failed to parse a heading.', reason);
    }
    return null;
}
/**
 * Parses the provided string and returns a list of headings.
 *
 * @param text - Input text
 * @param options - Parser configuration
 * @param initialLevels - Initial levels to use for computing the prefix
 * @returns List of headings
 */
function getHeadings(text, options, initialLevels = []) {
    const config = Object.assign(Object.assign({}, _tokens__WEBPACK_IMPORTED_MODULE_1__.TableOfContents.defaultConfig), options);
    // Split the text into lines:
    const lines = text.split('\n');
    // Iterate over the lines to get the header level and text for each line:
    const levels = initialLevels;
    let previousLevel = levels.length;
    let headings = new Array();
    let isCodeBlock;
    for (let lineIdx = 0; lineIdx < lines.length; lineIdx++) {
        let line = lines[lineIdx];
        if (line === '') {
            // Bail early
            continue;
        }
        // Don't check for Markdown headings if in a code block:
        if (line.startsWith('```')) {
            isCodeBlock = !isCodeBlock;
        }
        if (isCodeBlock) {
            continue;
        }
        const heading = parseHeading(line, lines[lineIdx + 1]); // append the next line to capture alternative style Markdown headings
        if (heading) {
            let level = heading.level;
            if (level > 0 && level <= config.maximalDepth) {
                const prefix = (0,_common__WEBPACK_IMPORTED_MODULE_2__.getPrefix)(level, previousLevel, levels, config);
                previousLevel = level;
                headings.push({
                    text: heading.text,
                    prefix,
                    level,
                    line: lineIdx,
                    raw: heading.raw
                });
            }
        }
    }
    return headings;
}
const MARKDOWN_MIME_TYPE = [
    'text/x-ipythongfm',
    'text/x-markdown',
    'text/x-gfm',
    'text/markdown'
];
/**
 * Returns whether a MIME type corresponds to a Markdown flavor.
 *
 * @param mime - MIME type string
 * @returns boolean indicating whether a provided MIME type corresponds to a Markdown flavor
 *
 * @example
 * const bool = isMarkdown('text/markdown');
 * // returns true
 *
 * @example
 * const bool = isMarkdown('text/plain');
 * // returns false
 */
function isMarkdown(mime) {
    return MARKDOWN_MIME_TYPE.includes(mime);
}
/**
 * Parses a heading, if one exists, from a provided string.
 *
 * ## Notes
 *
 * -   Heading examples:
 *
 *     -   Markdown heading:
 *
 *         ```
 *         # Foo
 *         ```
 *
 *     -   Markdown heading (alternative style):
 *
 *         ```
 *         Foo
 *         ===
 *         ```
 *
 *         ```
 *         Foo
 *         ---
 *         ```
 *
 *     -   HTML heading:
 *
 *         ```
 *         <h3>Foo</h3>
 *         ```
 *
 * @private
 * @param line - Line to parse
 * @param nextLine - The line after the one to parse
 * @returns heading info
 *
 * @example
 * const out = parseHeading('### Foo\n');
 * // returns {'text': 'Foo', 'level': 3}
 *
 * @example
 * const out = parseHeading('Foo\n===\n');
 * // returns {'text': 'Foo', 'level': 1}
 *
 * @example
 * const out = parseHeading('<h4>Foo</h4>\n');
 * // returns {'text': 'Foo', 'level': 4}
 *
 * @example
 * const out = parseHeading('Foo');
 * // returns null
 */
function parseHeading(line, nextLine) {
    // Case: Markdown heading
    let match = line.match(/^([#]{1,6}) (.*)/);
    if (match) {
        if (!skipHeading.test(match[0])) {
            return {
                text: cleanTitle(match[2]),
                level: match[1].length,
                raw: line
            };
        }
    }
    // Case: Markdown heading (alternative style)
    if (nextLine) {
        match = nextLine.match(/^ {0,3}([=]{2,}|[-]{2,})\s*$/);
        if (match) {
            if (!skipHeading.test(line)) {
                return {
                    text: cleanTitle(line),
                    level: match[1][0] === '=' ? 1 : 2,
                    raw: [line, nextLine].join('\n')
                };
            }
        }
    }
    // Case: HTML heading (WARNING: this is not particularly robust, as HTML headings can span multiple lines)
    match = line.match(/<h([1-6]).*>(.*)<\/h\1>/i);
    if (match) {
        if (!skipHeading.test(match[0])) {
            return {
                text: match[2],
                level: parseInt(match[1], 10),
                raw: line
            };
        }
    }
    return null;
}
function cleanTitle(heading) {
    // take special care to parse Markdown links into raw text
    return heading.replace(/\[(.+)\]\(.+\)/g, '$1');
}
/**
 * Ignore title with html tag with a class name equal to `jp-toc-ignore` or `tocSkip`
 */
const skipHeading = /<\w+\s(.*?\s)?class="(.*?\s)?(jp-toc-ignore|tocSkip)(\s.*?)?"(\s.*?)?>/;


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdG9jX2xpYl9pbmRleF9qcy5kNTNjODFhMjBkZjY0OTY3YjIxOS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBR007QUFNakU7Ozs7R0FJRztBQUNILE1BQU0sY0FBYyxHQUFHLElBQUksQ0FBQztBQUU1Qjs7R0FFRztBQUNJLE1BQWUsc0JBQXNCO0lBRzFDOzs7O09BSUc7SUFDSCxZQUFzQixPQUEwQjtRQUExQixZQUFPLEdBQVAsT0FBTyxDQUFtQjtJQUFHLENBQUM7SUFFcEQ7Ozs7O09BS0c7SUFDSCxZQUFZLENBQUMsTUFBYztRQUN6QixJQUFJLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDLEVBQUU7WUFDN0IsT0FBTyxLQUFLLENBQUM7U0FDZDtRQUVELE9BQU8sSUFBSSxDQUFDO0lBQ2QsQ0FBQztJQUVEOzs7Ozs7T0FNRztJQUNILFNBQVMsQ0FDUCxNQUFTLEVBQ1QsYUFBdUM7UUFFdkMsTUFBTSxLQUFLLEdBQUcsSUFBSSxDQUFDLFVBQVUsQ0FBQyxNQUFNLEVBQUUsYUFBYSxDQUFDLENBQUM7UUFFckQsTUFBTSxPQUFPLEdBQUcsTUFBTSxDQUFDLE9BQU8sQ0FBQztRQUUvQixNQUFNLGNBQWMsR0FBRyxHQUFHLEVBQUU7WUFDMUIsS0FBSyxDQUFDLE9BQU8sRUFBRSxDQUFDLEtBQUssQ0FBQyxNQUFNLENBQUMsRUFBRTtnQkFDN0IsT0FBTyxDQUFDLEtBQUssQ0FBQyx5Q0FBeUMsRUFBRSxNQUFNLENBQUMsQ0FBQztZQUNuRSxDQUFDLENBQUMsQ0FBQztRQUNMLENBQUMsQ0FBQztRQUNGLE1BQU0sT0FBTyxHQUFHLElBQUksa0VBQWUsQ0FBQztZQUNsQyxNQUFNLEVBQUUsT0FBTyxDQUFDLEtBQUssQ0FBQyxjQUFjO1lBQ3BDLE9BQU8sRUFBRSxjQUFjO1NBQ3hCLENBQUMsQ0FBQztRQUNILE9BQU8sQ0FBQyxlQUFlLENBQUMsT0FBTyxDQUFD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U0FDRjtLQUNGO0lBQ0QsMEdBQTBHO0lBQzFHLEtBQUssR0FBRyxJQUFJLENBQUMsS0FBSyxDQUFDLDBCQUEwQixDQUFDLENBQUM7SUFDL0MsSUFBSSxLQUFLLEVBQUU7UUFDVCxJQUFJLENBQUMsV0FBVyxDQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDLENBQUMsRUFBRTtZQUMvQixPQUFPO2dCQUNMLElBQUksRUFBRSxLQUFLLENBQUMsQ0FBQyxDQUFDO2dCQUNkLEtBQUssRUFBRSxRQUFRLENBQUMsS0FBSyxDQUFDLENBQUMsQ0FBQyxFQUFFLEVBQUUsQ0FBQztnQkFDN0IsR0FBRyxFQUFFLElBQUk7YUFDVixDQUFDO1NBQ0g7S0FDRjtJQUVELE9BQU8sSUFBSSxDQUFDO0FBQ2QsQ0FBQztBQUVELFNBQVMsVUFBVSxDQUFDLE9BQWU7SUFDakMsMERBQTBEO0lBQzFELE9BQU8sT0FBTyxDQUFDLE9BQU8sQ0FBQyxpQkFBaUIsRUFBRSxJQUFJLENBQUMsQ0FBQztBQUNsRCxDQUFDO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLFdBQVcsR0FDZix3RUFBd0UsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90b2Mvc3JjL2ZhY3RvcnkudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvbW9kZWwudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvcGFuZWwudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvcmVnaXN0cnkudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvdG9jaXRlbS50c3giLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvdG9jdHJlZS50c3giLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90b2Mvc3JjL3RyYWNrZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RvYy9zcmMvdHJlZXZpZXcudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90b2Mvc3JjL3V0aWxzL2NvbW1vbi50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdG9jL3NyYy91dGlscy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdG9jL3NyYy91dGlscy9tYXJrZG93bi50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElXaWRnZXRUcmFja2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgQWN0aXZpdHlNb25pdG9yLCBQYXRoRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7IElEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBUYWJsZU9mQ29udGVudHNNb2RlbCB9IGZyb20gJy4vbW9kZWwnO1xuaW1wb3J0IHsgVGFibGVPZkNvbnRlbnRzIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIFRpbWVvdXQgZm9yIHRocm90dGxpbmcgVG9DIHJlbmRlcmluZyBmb2xsb3dpbmcgbW9kZWwgY2hhbmdlcy5cbiAqXG4gKiBAcHJpdmF0ZVxuICovXG5jb25zdCBSRU5ERVJfVElNRU9VVCA9IDEwMDA7XG5cbi8qKlxuICogQWJzdHJhY3QgdGFibGUgb2YgY29udGVudHMgbW9kZWwgZmFjdG9yeSBmb3IgSURvY3VtZW50V2lkZ2V0LlxuICovXG5leHBvcnQgYWJzdHJhY3QgY2xhc3MgVGFibGVPZkNvbnRlbnRzRmFjdG9yeTxXIGV4dGVuZHMgSURvY3VtZW50V2lkZ2V0PlxuICBpbXBsZW1lbnRzIFRhYmxlT2ZDb250ZW50cy5JRmFjdG9yeTxXPlxue1xuICAvKipcbiAgICogQ29uc3RydWN0b3JcbiAgICpcbiAgICogQHBhcmFtIHRyYWNrZXIgV2lkZ2V0IHRyYWNrZXJcbiAgICovXG4gIGNvbnN0cnVjdG9yKHByb3RlY3RlZCB0cmFja2VyOiBJV2lkZ2V0VHJhY2tlcjxXPikge31cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgZmFjdG9yeSBjYW4gaGFuZGxlIHRoZSB3aWRnZXQgb3Igbm90LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAqIEByZXR1cm5zIGJvb2xlYW4gaW5kaWNhdGluZyBhIFRvQyBjYW4gYmUgZ2VuZXJhdGVkXG4gICAqL1xuICBpc0FwcGxpY2FibGUod2lkZ2V0OiBXaWRnZXQpOiBib29sZWFuIHtcbiAgICBpZiAoIXRoaXMudHJhY2tlci5oYXMod2lkZ2V0KSkge1xuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cblxuICAgIHJldHVybiB0cnVlO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB0YWJsZSBvZiBjb250ZW50cyBtb2RlbCBmb3IgdGhlIHdpZGdldFxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAqIEBwYXJhbSBjb25maWd1cmF0aW9uIC0gVGFibGUgb2YgY29udGVudHMgY29uZmlndXJhdGlvblxuICAgKiBAcmV0dXJucyBUaGUgdGFibGUgb2YgY29udGVudHMgbW9kZWxcbiAgICovXG4gIGNyZWF0ZU5ldyhcbiAgICB3aWRnZXQ6IFcsXG4gICAgY29uZmlndXJhdGlvbj86IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnXG4gICk6IFRhYmxlT2ZDb250ZW50c01vZGVsPFRhYmxlT2ZDb250ZW50cy5JSGVhZGluZywgVz4ge1xuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5fY3JlYXRlTmV3KHdpZGdldCwgY29uZmlndXJhdGlvbik7XG5cbiAgICBjb25zdCBjb250ZXh0ID0gd2lkZ2V0LmNvbnRleHQ7XG5cbiAgICBjb25zdCB1cGRhdGVIZWFkaW5ncyA9ICgpID0+IHtcbiAgICAgIG1vZGVsLnJlZnJlc2goKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gdXBkYXRlIHRoZSB0YWJsZSBvZiBjb250ZW50cy4nLCByZWFzb24pO1xuICAgICAgfSk7XG4gICAgfTtcbiAgICBjb25zdCBtb25pdG9yID0gbmV3IEFjdGl2aXR5TW9uaXRvcih7XG4gICAgICBzaWduYWw6IGNvbnRleHQubW9kZWwuY29udGVudENoYW5nZWQsXG4gICAgICB0aW1lb3V0OiBSRU5ERVJfVElNRU9VVFxuICAgIH0pO1xuICAgIG1vbml0b3IuYWN0aXZpdHlTdG9wcGVkLmNvbm5lY3QodXBkYXRlSGVhZGluZ3MpO1xuXG4gICAgY29uc3QgdXBkYXRlVGl0bGUgPSAoKSA9PiB7XG4gICAgICBtb2RlbC50aXRsZSA9IFBhdGhFeHQuYmFzZW5hbWUoY29udGV4dC5sb2NhbFBhdGgpO1xuICAgIH07XG4gICAgY29udGV4dC5wYXRoQ2hhbmdlZC5jb25uZWN0KHVwZGF0ZVRpdGxlKTtcblxuICAgIGNvbnRleHQucmVhZHlcbiAgICAgIC50aGVuKCgpID0+IHtcbiAgICAgICAgdXBkYXRlVGl0bGUoKTtcbiAgICAgICAgdXBkYXRlSGVhZGluZ3MoKTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIGluaXRpYXRlIGhlYWRpbmdzIGZvciAke2NvbnRleHQubG9jYWxQYXRofS5gKTtcbiAgICAgIH0pO1xuXG4gICAgd2lkZ2V0LmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgbW9uaXRvci5hY3Rpdml0eVN0b3BwZWQuZGlzY29ubmVjdCh1cGRhdGVIZWFkaW5ncyk7XG4gICAgICBjb250ZXh0LnBhdGhDaGFuZ2VkLmRpc2Nvbm5lY3QodXBkYXRlVGl0bGUpO1xuICAgIH0pO1xuXG4gICAgcmV0dXJuIG1vZGVsO1xuICB9XG5cbiAgLyoqXG4gICAqIEFic3RyYWN0IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsIGluc3RhbnRpYXRpb24gdG8gYWxsb3dcbiAgICogb3ZlcnJpZGUgYnkgcmVhbCBpbXBsZW1lbnRhdGlvbiB0byBjdXN0b21pemUgaXQuIFRoZSBwdWJsaWNcbiAgICogYGNyZWF0ZU5ld2AgY29udGFpbnMgdGhlIHNpZ25hbCBjb25uZWN0aW9ucyBzdGFuZGFyZHMgZm9yIElEb2N1bWVudFdpZGdldFxuICAgKiB3aGVuIHRoZSBtb2RlbCBoYXMgYmVlbiBpbnN0YW50aWF0ZWQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXRcbiAgICogQHBhcmFtIGNvbmZpZ3VyYXRpb25cbiAgICovXG4gIHByb3RlY3RlZCBhYnN0cmFjdCBfY3JlYXRlTmV3KFxuICAgIHdpZGdldDogVyxcbiAgICBjb25maWd1cmF0aW9uPzogVGFibGVPZkNvbnRlbnRzLklDb25maWdcbiAgKTogVGFibGVPZkNvbnRlbnRzTW9kZWw8VGFibGVPZkNvbnRlbnRzLklIZWFkaW5nLCBXPjtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHRvY1xuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vZmFjdG9yeSc7XG5leHBvcnQgKiBmcm9tICcuL21vZGVsJztcbmV4cG9ydCAqIGZyb20gJy4vcGFuZWwnO1xuZXhwb3J0ICogZnJvbSAnLi9yZWdpc3RyeSc7XG5leHBvcnQgKiBmcm9tICcuL3RyZWV2aWV3JztcbmV4cG9ydCAqIGZyb20gJy4vdG9jaXRlbSc7XG5leHBvcnQgKiBmcm9tICcuL3RvY3RyZWUnO1xuZXhwb3J0ICogZnJvbSAnLi90b2tlbnMnO1xuZXhwb3J0ICogZnJvbSAnLi90cmFja2VyJztcbi8vIE5hbWVzcGFjZSB0aGUgdXRpbHNcbmV4cG9ydCAqIGFzIFRhYmxlT2ZDb250ZW50c1V0aWxzIGZyb20gJy4vdXRpbHMnO1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBWRG9tTW9kZWwgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IEpTT05FeHQgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgVGFibGVPZkNvbnRlbnRzIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIEFic3RyYWN0IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsLlxuICovXG5leHBvcnQgYWJzdHJhY3QgY2xhc3MgVGFibGVPZkNvbnRlbnRzTW9kZWw8XG4gICAgSCBleHRlbmRzIFRhYmxlT2ZDb250ZW50cy5JSGVhZGluZyxcbiAgICBUIGV4dGVuZHMgV2lkZ2V0ID0gV2lkZ2V0XG4gID5cbiAgZXh0ZW5kcyBWRG9tTW9kZWxcbiAgaW1wbGVtZW50cyBUYWJsZU9mQ29udGVudHMuSU1vZGVsPEg+XG57XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3RvclxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFRoZSB3aWRnZXQgdG8gc2VhcmNoIGluXG4gICAqIEBwYXJhbSBjb25maWd1cmF0aW9uIERlZmF1bHQgbW9kZWwgY29uZmlndXJhdGlvblxuICAgKi9cbiAgY29uc3RydWN0b3IocHJvdGVjdGVkIHdpZGdldDogVCwgY29uZmlndXJhdGlvbj86IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl9hY3RpdmVIZWFkaW5nID0gbnVsbDtcbiAgICB0aGlzLl9hY3RpdmVIZWFkaW5nQ2hhbmdlZCA9IG5ldyBTaWduYWw8XG4gICAgICBUYWJsZU9mQ29udGVudHNNb2RlbDxILCBUPixcbiAgICAgIEggfCBudWxsXG4gICAgPih0aGlzKTtcbiAgICB0aGlzLl9jb2xsYXBzZUNoYW5nZWQgPSBuZXcgU2lnbmFsPFRhYmxlT2ZDb250ZW50c01vZGVsPEgsIFQ+LCBIPih0aGlzKTtcbiAgICB0aGlzLl9jb25maWd1cmF0aW9uID0gY29uZmlndXJhdGlvbiA/PyB7IC4uLlRhYmxlT2ZDb250ZW50cy5kZWZhdWx0Q29uZmlnIH07XG4gICAgdGhpcy5faGVhZGluZ3MgPSBuZXcgQXJyYXk8SD4oKTtcbiAgICB0aGlzLl9oZWFkaW5nc0NoYW5nZWQgPSBuZXcgU2lnbmFsPFRhYmxlT2ZDb250ZW50c01vZGVsPEgsIFQ+LCB2b2lkPih0aGlzKTtcbiAgICB0aGlzLl9pc0FjdGl2ZSA9IGZhbHNlO1xuICAgIHRoaXMuX2lzUmVmcmVzaGluZyA9IGZhbHNlO1xuICAgIHRoaXMuX25lZWRzUmVmcmVzaGluZyA9IGZhbHNlO1xuICB9XG5cbiAgLyoqXG4gICAqIEN1cnJlbnQgYWN0aXZlIGVudHJ5LlxuICAgKlxuICAgKiBAcmV0dXJucyB0YWJsZSBvZiBjb250ZW50cyBhY3RpdmUgZW50cnlcbiAgICovXG4gIGdldCBhY3RpdmVIZWFkaW5nKCk6IEggfCBudWxsIHtcbiAgICByZXR1cm4gdGhpcy5fYWN0aXZlSGVhZGluZztcbiAgfVxuXG4gIC8qKlxuICAgKiBTaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBhY3RpdmUgaGVhZGluZyBjaGFuZ2VzLlxuICAgKi9cbiAgZ2V0IGFjdGl2ZUhlYWRpbmdDaGFuZ2VkKCk6IElTaWduYWw8VGFibGVPZkNvbnRlbnRzLklNb2RlbDxIPiwgSCB8IG51bGw+IHtcbiAgICByZXR1cm4gdGhpcy5fYWN0aXZlSGVhZGluZ0NoYW5nZWQ7XG4gIH1cblxuICAvKipcbiAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiBhIHRhYmxlIG9mIGNvbnRlbnQgc2VjdGlvbiBjb2xsYXBzZSBzdGF0ZSBjaGFuZ2VzLlxuICAgKi9cbiAgZ2V0IGNvbGxhcHNlQ2hhbmdlZCgpOiBJU2lnbmFsPFRhYmxlT2ZDb250ZW50cy5JTW9kZWw8SD4sIEggfCBudWxsPiB7XG4gICAgcmV0dXJuIHRoaXMuX2NvbGxhcHNlQ2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBNb2RlbCBjb25maWd1cmF0aW9uXG4gICAqL1xuICBnZXQgY29uZmlndXJhdGlvbigpOiBUYWJsZU9mQ29udGVudHMuSUNvbmZpZyB7XG4gICAgcmV0dXJuIHRoaXMuX2NvbmZpZ3VyYXRpb247XG4gIH1cblxuICAvKipcbiAgICogVHlwZSBvZiBkb2N1bWVudCBzdXBwb3J0ZWQgYnkgdGhlIG1vZGVsLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIEEgYGRhdGEtZG9jdW1lbnQtdHlwZWAgYXR0cmlidXRlIHdpdGggdGhpcyB2YWx1ZSB3aWxsIGJlIHNldFxuICAgKiBvbiB0aGUgdHJlZSB2aWV3IGAuanAtVGFibGVPZkNvbnRlbnRzLWNvbnRlbnRbZGF0YS1kb2N1bWVudC10eXBlPVwiLi4uXCJdYFxuICAgKi9cbiAgYWJzdHJhY3QgcmVhZG9ubHkgZG9jdW1lbnRUeXBlOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIExpc3Qgb2YgaGVhZGluZ3MuXG4gICAqXG4gICAqIEByZXR1cm5zIHRhYmxlIG9mIGNvbnRlbnRzIGxpc3Qgb2YgaGVhZGluZ3NcbiAgICovXG4gIGdldCBoZWFkaW5ncygpOiBIW10ge1xuICAgIHJldHVybiB0aGlzLl9oZWFkaW5ncztcbiAgfVxuXG4gIC8qKlxuICAgKiBTaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBoZWFkaW5ncyBjaGFuZ2VzLlxuICAgKi9cbiAgZ2V0IGhlYWRpbmdzQ2hhbmdlZCgpOiBJU2lnbmFsPFRhYmxlT2ZDb250ZW50cy5JTW9kZWw8SD4sIHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5faGVhZGluZ3NDaGFuZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIG1vZGVsIGlzIGFjdGl2ZSBvciBub3QuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogQW4gYWN0aXZlIG1vZGVsIG1lYW5zIGl0IGlzIGRpc3BsYXllZCBpbiB0aGUgdGFibGUgb2YgY29udGVudHMuXG4gICAqIFRoaXMgY2FuIGJlIHVzZWQgYnkgc3ViY2xhc3MgdG8gbGltaXQgdXBkYXRpbmcgdGhlIGhlYWRpbmdzLlxuICAgKi9cbiAgZ2V0IGlzQWN0aXZlKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9pc0FjdGl2ZTtcbiAgfVxuICBzZXQgaXNBY3RpdmUodjogYm9vbGVhbikge1xuICAgIHRoaXMuX2lzQWN0aXZlID0gdjtcbiAgICAvLyBSZWZyZXNoIG9uIGFjdGl2YXRpb24gZXhwZWN0IGlmIGl0IGlzIGFsd2F5cyBhY3RpdmVcbiAgICAvLyAgPT4gYSBUb0MgbW9kZWwgaXMgYWx3YXlzIGFjdGl2ZSBlLmcuIHdoZW4gZGlzcGxheWluZyBudW1iZXJpbmcgaW4gdGhlIGRvY3VtZW50XG4gICAgaWYgKHRoaXMuX2lzQWN0aXZlICYmICF0aGlzLmlzQWx3YXlzQWN0aXZlKSB7XG4gICAgICB0aGlzLnJlZnJlc2goKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gcmVmcmVzaCBUb0MgbW9kZWwuJywgcmVhc29uKTtcbiAgICAgIH0pO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBtb2RlbCBnZXRzIHVwZGF0ZWQgZXZlbiBpZiB0aGUgdGFibGUgb2YgY29udGVudHMgcGFuZWxcbiAgICogaXMgaGlkZGVuIG9yIG5vdC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBGb3IgZXhhbXBsZSwgVG9DIG1vZGVscyB1c2UgdG8gYWRkIHRpdGxlIG51bWJlcmluZyB3aWxsXG4gICAqIHNldCB0aGlzIHRvIHRydWUuXG4gICAqL1xuICBwcm90ZWN0ZWQgZ2V0IGlzQWx3YXlzQWN0aXZlKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiBmYWxzZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBMaXN0IG9mIGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBzdXBwb3J0ZWQgYnkgdGhlIG1vZGVsLlxuICAgKi9cbiAgZ2V0IHN1cHBvcnRlZE9wdGlvbnMoKTogKGtleW9mIFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnKVtdIHtcbiAgICByZXR1cm4gWydtYXhpbWFsRGVwdGgnXTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEb2N1bWVudCB0aXRsZVxuICAgKi9cbiAgZ2V0IHRpdGxlKCk6IHN0cmluZyB8IHVuZGVmaW5lZCB7XG4gICAgcmV0dXJuIHRoaXMuX3RpdGxlO1xuICB9XG4gIHNldCB0aXRsZSh2OiBzdHJpbmcgfCB1bmRlZmluZWQpIHtcbiAgICBpZiAodiAhPT0gdGhpcy5fdGl0bGUpIHtcbiAgICAgIHRoaXMuX3RpdGxlID0gdjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQWJzdHJhY3QgZnVuY3Rpb24gdGhhdCB3aWxsIHByb2R1Y2UgdGhlIGhlYWRpbmdzIGZvciBhIGRvY3VtZW50LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgbGlzdCBvZiBuZXcgaGVhZGluZ3Mgb3IgYG51bGxgIGlmIG5vdGhpbmcgbmVlZHMgdG8gYmUgdXBkYXRlZC5cbiAgICovXG4gIHByb3RlY3RlZCBhYnN0cmFjdCBnZXRIZWFkaW5ncygpOiBQcm9taXNlPEhbXSB8IG51bGw+O1xuXG4gIC8qKlxuICAgKiBSZWZyZXNoIHRoZSBoZWFkaW5ncyBsaXN0LlxuICAgKi9cbiAgYXN5bmMgcmVmcmVzaCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBpZiAodGhpcy5faXNSZWZyZXNoaW5nKSB7XG4gICAgICAvLyBTY2hlZHVsZSBhIHJlZnJlc2ggaWYgb25lIGlzIGluIHByb2dyZXNzXG4gICAgICB0aGlzLl9uZWVkc1JlZnJlc2hpbmcgPSB0cnVlO1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSgpO1xuICAgIH1cblxuICAgIHRoaXMuX2lzUmVmcmVzaGluZyA9IHRydWU7XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IG5ld0hlYWRpbmdzID0gYXdhaXQgdGhpcy5nZXRIZWFkaW5ncygpO1xuXG4gICAgICBpZiAodGhpcy5fbmVlZHNSZWZyZXNoaW5nKSB7XG4gICAgICAgIHRoaXMuX25lZWRzUmVmcmVzaGluZyA9IGZhbHNlO1xuICAgICAgICB0aGlzLl9pc1JlZnJlc2hpbmcgPSBmYWxzZTtcbiAgICAgICAgcmV0dXJuIHRoaXMucmVmcmVzaCgpO1xuICAgICAgfVxuXG4gICAgICBpZiAoXG4gICAgICAgIG5ld0hlYWRpbmdzICYmXG4gICAgICAgICFQcml2YXRlLmFyZUhlYWRpbmdzRXF1YWwobmV3SGVhZGluZ3MsIHRoaXMuX2hlYWRpbmdzKVxuICAgICAgKSB7XG4gICAgICAgIHRoaXMuX2hlYWRpbmdzID0gbmV3SGVhZGluZ3M7XG4gICAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgICAgdGhpcy5faGVhZGluZ3NDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIH1cbiAgICB9IGZpbmFsbHkge1xuICAgICAgdGhpcy5faXNSZWZyZXNoaW5nID0gZmFsc2U7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFNldCBhIG5ldyBhY3RpdmUgaGVhZGluZy5cbiAgICpcbiAgICogQHBhcmFtIGhlYWRpbmcgVGhlIG5ldyBhY3RpdmUgaGVhZGluZ1xuICAgKiBAcGFyYW0gZW1pdFNpZ25hbCBXaGV0aGVyIHRvIGVtaXQgdGhlIGFjdGl2ZUhlYWRpbmdDaGFuZ2VkIHNpZ25hbCBvciBub3QuXG4gICAqL1xuICBzZXRBY3RpdmVIZWFkaW5nKGhlYWRpbmc6IEggfCBudWxsLCBlbWl0U2lnbmFsID0gdHJ1ZSk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9hY3RpdmVIZWFkaW5nICE9PSBoZWFkaW5nKSB7XG4gICAgICB0aGlzLl9hY3RpdmVIZWFkaW5nID0gaGVhZGluZztcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIGlmIChlbWl0U2lnbmFsKSB7XG4gICAgICAgIHRoaXMuX2FjdGl2ZUhlYWRpbmdDaGFuZ2VkLmVtaXQoaGVhZGluZyk7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIE1vZGVsIGNvbmZpZ3VyYXRpb24gc2V0dGVyLlxuICAgKlxuICAgKiBAcGFyYW0gYyBOZXcgY29uZmlndXJhdGlvblxuICAgKi9cbiAgc2V0Q29uZmlndXJhdGlvbihjOiBQYXJ0aWFsPFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnPik6IHZvaWQge1xuICAgIGNvbnN0IG5ld0NvbmZpZ3VyYXRpb24gPSB7IC4uLnRoaXMuX2NvbmZpZ3VyYXRpb24sIC4uLmMgfTtcbiAgICBpZiAoIUpTT05FeHQuZGVlcEVxdWFsKHRoaXMuX2NvbmZpZ3VyYXRpb24sIG5ld0NvbmZpZ3VyYXRpb24pKSB7XG4gICAgICB0aGlzLl9jb25maWd1cmF0aW9uID0gbmV3Q29uZmlndXJhdGlvbiBhcyBUYWJsZU9mQ29udGVudHMuSUNvbmZpZztcbiAgICAgIHRoaXMucmVmcmVzaCgpLmNhdGNoKHJlYXNvbiA9PiB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoJ0ZhaWxlZCB0byB1cGRhdGUgdGhlIHRhYmxlIG9mIGNvbnRlbnRzLicsIHJlYXNvbik7XG4gICAgICB9KTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQ2FsbGJhY2sgb24gaGVhZGluZyBjb2xsYXBzZS5cbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMuaGVhZGluZyBUaGUgaGVhZGluZyB0byBjaGFuZ2Ugc3RhdGUgKGFsbCBoZWFkaW5ncyBpZiBub3QgcHJvdmlkZWQpXG4gICAqIEBwYXJhbSBvcHRpb25zLmNvbGxhcHNlZCBUaGUgbmV3IGNvbGxhcHNlZCBzdGF0dXMgKHRvZ2dsZSBleGlzdGluZyBzdGF0dXMgaWYgbm90IHByb3ZpZGVkKVxuICAgKi9cbiAgdG9nZ2xlQ29sbGFwc2Uob3B0aW9uczogeyBoZWFkaW5nPzogSDsgY29sbGFwc2VkPzogYm9vbGVhbiB9KTogdm9pZCB7XG4gICAgaWYgKG9wdGlvbnMuaGVhZGluZykge1xuICAgICAgb3B0aW9ucy5oZWFkaW5nLmNvbGxhcHNlZCA9XG4gICAgICAgIG9wdGlvbnMuY29sbGFwc2VkID8/ICFvcHRpb25zLmhlYWRpbmcuY29sbGFwc2VkO1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgICAgdGhpcy5fY29sbGFwc2VDaGFuZ2VkLmVtaXQob3B0aW9ucy5oZWFkaW5nKTtcbiAgICB9IGVsc2Uge1xuICAgICAgLy8gVXNlIHRoZSBwcm92aWRlZCBzdGF0ZSBvciBjb2xsYXBzZWQgYWxsIGV4Y2VwdCBpZiBhbGwgYXJlIGNvbGxhcHNlZFxuICAgICAgY29uc3QgbmV3U3RhdGUgPVxuICAgICAgICBvcHRpb25zLmNvbGxhcHNlZCA/PyAhdGhpcy5oZWFkaW5ncy5zb21lKGggPT4gIShoLmNvbGxhcHNlZCA/PyBmYWxzZSkpO1xuICAgICAgdGhpcy5oZWFkaW5ncy5mb3JFYWNoKGggPT4gKGguY29sbGFwc2VkID0gbmV3U3RhdGUpKTtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIHRoaXMuX2NvbGxhcHNlQ2hhbmdlZC5lbWl0KG51bGwpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX2FjdGl2ZUhlYWRpbmc6IEggfCBudWxsO1xuICBwcml2YXRlIF9hY3RpdmVIZWFkaW5nQ2hhbmdlZDogU2lnbmFsPFRhYmxlT2ZDb250ZW50c01vZGVsPEgsIFQ+LCBIIHwgbnVsbD47XG4gIHByaXZhdGUgX2NvbGxhcHNlQ2hhbmdlZDogU2lnbmFsPFRhYmxlT2ZDb250ZW50c01vZGVsPEgsIFQ+LCBIIHwgbnVsbD47XG4gIHByaXZhdGUgX2NvbmZpZ3VyYXRpb246IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnO1xuICBwcml2YXRlIF9oZWFkaW5nczogSFtdO1xuICBwcml2YXRlIF9oZWFkaW5nc0NoYW5nZWQ6IFNpZ25hbDxUYWJsZU9mQ29udGVudHNNb2RlbDxILCBUPiwgdm9pZD47XG4gIHByaXZhdGUgX2lzQWN0aXZlOiBib29sZWFuO1xuICBwcml2YXRlIF9pc1JlZnJlc2hpbmc6IGJvb2xlYW47XG4gIHByaXZhdGUgX25lZWRzUmVmcmVzaGluZzogYm9vbGVhbjtcbiAgcHJpdmF0ZSBfdGl0bGU/OiBzdHJpbmc7XG59XG5cbi8qKlxuICogUHJpdmF0ZSBmdW5jdGlvbnMgbmFtZXNwYWNlXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIFRlc3QgaWYgdHdvIGxpc3Qgb2YgaGVhZGluZ3MgYXJlIGVxdWFsIG9yIG5vdC5cbiAgICpcbiAgICogQHBhcmFtIGhlYWRpbmdzMSBGaXJzdCBsaXN0IG9mIGhlYWRpbmdzXG4gICAqIEBwYXJhbSBoZWFkaW5nczIgU2Vjb25kIGxpc3Qgb2YgaGVhZGluZ3NcbiAgICogQHJldHVybnMgV2hldGhlciB0aGUgYXJyYXkgYXJlIGlkZW50aWNhbCBvciBub3QuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gYXJlSGVhZGluZ3NFcXVhbChcbiAgICBoZWFkaW5nczE6IFRhYmxlT2ZDb250ZW50cy5JSGVhZGluZ1tdLFxuICAgIGhlYWRpbmdzMjogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nW11cbiAgKTogYm9vbGVhbiB7XG4gICAgaWYgKGhlYWRpbmdzMS5sZW5ndGggPT09IGhlYWRpbmdzMi5sZW5ndGgpIHtcbiAgICAgIGZvciAobGV0IGkgPSAwOyBpIDwgaGVhZGluZ3MxLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgIGlmIChcbiAgICAgICAgICBoZWFkaW5nczFbaV0ubGV2ZWwgIT09IGhlYWRpbmdzMltpXS5sZXZlbCB8fFxuICAgICAgICAgIGhlYWRpbmdzMVtpXS50ZXh0ICE9PSBoZWFkaW5nczJbaV0udGV4dCB8fFxuICAgICAgICAgIGhlYWRpbmdzMVtpXS5wcmVmaXggIT09IGhlYWRpbmdzMltpXS5wcmVmaXhcbiAgICAgICAgKSB7XG4gICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG5cbiAgICByZXR1cm4gZmFsc2U7XG4gIH1cbn1cbiIsIi8qXG4gKiBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbiAqIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4gKi9cblxuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBTaWRlUGFuZWwgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFBhbmVsLCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgVGFibGVPZkNvbnRlbnRzV2lkZ2V0IH0gZnJvbSAnLi90cmVldmlldyc7XG5pbXBvcnQgeyBUYWJsZU9mQ29udGVudHMgfSBmcm9tICcuL3Rva2Vucyc7XG5pbXBvcnQgeyBNZXNzYWdlIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuXG4vKipcbiAqIFRhYmxlIG9mIGNvbnRlbnRzIHNpZGViYXIgcGFuZWwuXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWJsZU9mQ29udGVudHNQYW5lbCBleHRlbmRzIFNpZGVQYW5lbCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3RvclxuICAgKlxuICAgKiBAcGFyYW0gdHJhbnNsYXRvciAtIFRyYW5zbGF0b3IgdG9vbFxuICAgKi9cbiAgY29uc3RydWN0b3IodHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSB7XG4gICAgc3VwZXIoeyBjb250ZW50OiBuZXcgUGFuZWwoKSwgdHJhbnNsYXRvciB9KTtcbiAgICB0aGlzLl9tb2RlbCA9IG51bGw7XG5cbiAgICB0aGlzLmFkZENsYXNzKCdqcC1UYWJsZU9mQ29udGVudHMnKTtcblxuICAgIHRoaXMuX3RpdGxlID0gbmV3IFByaXZhdGUuSGVhZGVyKHRoaXMuX3RyYW5zLl9fKCdUYWJsZSBvZiBDb250ZW50cycpKTtcbiAgICB0aGlzLmhlYWRlci5hZGRXaWRnZXQodGhpcy5fdGl0bGUpO1xuXG4gICAgdGhpcy5fdHJlZXZpZXcgPSBuZXcgVGFibGVPZkNvbnRlbnRzV2lkZ2V0KCk7XG4gICAgdGhpcy5fdHJlZXZpZXcuYWRkQ2xhc3MoJ2pwLVRhYmxlT2ZDb250ZW50cy10cmVlJyk7XG4gICAgdGhpcy5jb250ZW50LmFkZFdpZGdldCh0aGlzLl90cmVldmlldyk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHRoZSBjdXJyZW50IG1vZGVsLlxuICAgKi9cbiAgZ2V0IG1vZGVsKCk6IFRhYmxlT2ZDb250ZW50cy5Nb2RlbCB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9tb2RlbDtcbiAgfVxuICBzZXQgbW9kZWwobmV3VmFsdWU6IFRhYmxlT2ZDb250ZW50cy5Nb2RlbCB8IG51bGwpIHtcbiAgICBpZiAodGhpcy5fbW9kZWwgIT09IG5ld1ZhbHVlKSB7XG4gICAgICB0aGlzLl9tb2RlbD8uc3RhdGVDaGFuZ2VkLmRpc2Nvbm5lY3QodGhpcy5fb25UaXRsZUNoYW5nZWQsIHRoaXMpO1xuXG4gICAgICB0aGlzLl9tb2RlbCA9IG5ld1ZhbHVlO1xuICAgICAgaWYgKHRoaXMuX21vZGVsKSB7XG4gICAgICAgIHRoaXMuX21vZGVsLmlzQWN0aXZlID0gdGhpcy5pc1Zpc2libGU7XG4gICAgICB9XG5cbiAgICAgIHRoaXMuX21vZGVsPy5zdGF0ZUNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblRpdGxlQ2hhbmdlZCwgdGhpcyk7XG4gICAgICB0aGlzLl9vblRpdGxlQ2hhbmdlZCgpO1xuXG4gICAgICB0aGlzLl90cmVldmlldy5tb2RlbCA9IHRoaXMuX21vZGVsO1xuICAgIH1cbiAgfVxuXG4gIHByb3RlY3RlZCBvbkFmdGVySGlkZShtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBzdXBlci5vbkFmdGVySGlkZShtc2cpO1xuICAgIGlmICh0aGlzLl9tb2RlbCkge1xuICAgICAgdGhpcy5fbW9kZWwuaXNBY3RpdmUgPSBmYWxzZTtcbiAgICB9XG4gIH1cblxuICBwcm90ZWN0ZWQgb25CZWZvcmVTaG93KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHN1cGVyLm9uQmVmb3JlU2hvdyhtc2cpO1xuICAgIGlmICh0aGlzLl9tb2RlbCkge1xuICAgICAgdGhpcy5fbW9kZWwuaXNBY3RpdmUgPSB0cnVlO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX29uVGl0bGVDaGFuZ2VkKCk6IHZvaWQge1xuICAgIHRoaXMuX3RpdGxlLnNldFRpdGxlKFxuICAgICAgdGhpcy5fbW9kZWw/LnRpdGxlID8/IHRoaXMuX3RyYW5zLl9fKCdUYWJsZSBvZiBDb250ZW50cycpXG4gICAgKTtcbiAgfVxuXG4gIHByaXZhdGUgX21vZGVsOiBUYWJsZU9mQ29udGVudHMuTW9kZWwgfCBudWxsO1xuICBwcml2YXRlIF90aXRsZTogUHJpdmF0ZS5IZWFkZXI7XG4gIHByaXZhdGUgX3RyZWV2aWV3OiBUYWJsZU9mQ29udGVudHNXaWRnZXQ7XG59XG5cbi8qKlxuICogUHJpdmF0ZSBoZWxwZXJzIG5hbWVzcGFjZVxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBQYW5lbCBoZWFkZXJcbiAgICovXG4gIGV4cG9ydCBjbGFzcyBIZWFkZXIgZXh0ZW5kcyBXaWRnZXQge1xuICAgIC8qKlxuICAgICAqIENvbnN0cnVjdG9yXG4gICAgICpcbiAgICAgKiBAcGFyYW0gdGl0bGUgLSBUaXRsZSB0ZXh0XG4gICAgICovXG4gICAgY29uc3RydWN0b3IodGl0bGU6IHN0cmluZykge1xuICAgICAgY29uc3Qgbm9kZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2gyJyk7XG4gICAgICBub2RlLnRleHRDb250ZW50ID0gdGl0bGU7XG4gICAgICBub2RlLmNsYXNzTGlzdC5hZGQoJ2pwLXRleHQtdHJ1bmNhdGVkJyk7XG4gICAgICBzdXBlcih7IG5vZGUgfSk7XG4gICAgICB0aGlzLl90aXRsZSA9IG5vZGU7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogU2V0IHRoZSBoZWFkZXIgdGl0bGUuXG4gICAgICovXG4gICAgc2V0VGl0bGUodGl0bGU6IHN0cmluZyk6IHZvaWQge1xuICAgICAgdGhpcy5fdGl0bGUudGV4dENvbnRlbnQgPSB0aXRsZTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF90aXRsZTogSFRNTEVsZW1lbnQ7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgRGlzcG9zYWJsZURlbGVnYXRlLCBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHsgSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5LCBUYWJsZU9mQ29udGVudHMgfSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogQ2xhc3MgZm9yIHJlZ2lzdGVyaW5nIHRhYmxlIG9mIGNvbnRlbnRzIGdlbmVyYXRvcnMuXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWJsZU9mQ29udGVudHNSZWdpc3RyeSBpbXBsZW1lbnRzIElUYWJsZU9mQ29udGVudHNSZWdpc3RyeSB7XG4gIC8qKlxuICAgKiBGaW5kcyBhIHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsIGZvciBhIHdpZGdldC5cbiAgICpcbiAgICogIyMgTm90ZXNcbiAgICpcbiAgICogLSAgIElmIHVuYWJsZSB0byBmaW5kIGEgdGFibGUgb2YgY29udGVudHMgbW9kZWwsIHRoZSBtZXRob2QgcmV0dXJuIGB1bmRlZmluZWRgLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAqIEBwYXJhbSBjb25maWd1cmF0aW9uIC0gRGVmYXVsdCBtb2RlbCBjb25maWd1cmF0aW9uXG4gICAqIEByZXR1cm5zIFRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsXG4gICAqL1xuICBnZXRNb2RlbChcbiAgICB3aWRnZXQ6IFdpZGdldCxcbiAgICBjb25maWd1cmF0aW9uPzogVGFibGVPZkNvbnRlbnRzLklDb25maWdcbiAgKTogVGFibGVPZkNvbnRlbnRzLk1vZGVsIHwgdW5kZWZpbmVkIHtcbiAgICBmb3IgKGNvbnN0IGdlbmVyYXRvciBvZiB0aGlzLl9nZW5lcmF0b3JzLnZhbHVlcygpKSB7XG4gICAgICBpZiAoZ2VuZXJhdG9yLmlzQXBwbGljYWJsZSh3aWRnZXQpKSB7XG4gICAgICAgIHJldHVybiBnZW5lcmF0b3IuY3JlYXRlTmV3KHdpZGdldCwgY29uZmlndXJhdGlvbik7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEFkZHMgYSB0YWJsZSBvZiBjb250ZW50cyBnZW5lcmF0b3IgdG8gdGhlIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiBAcGFyYW0gZ2VuZXJhdG9yIC0gdGFibGUgb2YgY29udGVudHMgZ2VuZXJhdG9yXG4gICAqL1xuICBhZGQoZ2VuZXJhdG9yOiBUYWJsZU9mQ29udGVudHMuSUZhY3RvcnkpOiBJRGlzcG9zYWJsZSB7XG4gICAgY29uc3QgaWQgPSB0aGlzLl9pZENvdW50ZXIrKztcbiAgICB0aGlzLl9nZW5lcmF0b3JzLnNldChpZCwgZ2VuZXJhdG9yKTtcblxuICAgIHJldHVybiBuZXcgRGlzcG9zYWJsZURlbGVnYXRlKCgpID0+IHtcbiAgICAgIHRoaXMuX2dlbmVyYXRvcnMuZGVsZXRlKGlkKTtcbiAgICB9KTtcbiAgfVxuXG4gIHByaXZhdGUgX2dlbmVyYXRvcnMgPSBuZXcgTWFwPG51bWJlciwgVGFibGVPZkNvbnRlbnRzLklGYWN0b3J5PigpO1xuICBwcml2YXRlIF9pZENvdW50ZXIgPSAwO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBjYXJldERvd25JY29uLCBjYXJldFJpZ2h0SWNvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgVGFibGVPZkNvbnRlbnRzIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIEludGVyZmFjZSBkZXNjcmliaW5nIGNvbXBvbmVudCBwcm9wZXJ0aWVzLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElUYWJsZU9mQ29udGVudHNJdGVtc1Byb3BzIHtcbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhpcyBpdGVtIGlzIGFjdGl2ZSBvciBub3QuXG4gICAqL1xuICBpc0FjdGl2ZTogYm9vbGVhbjtcbiAgLyoqXG4gICAqIEhlYWRpbmcgdG8gcmVuZGVyLlxuICAgKi9cbiAgaGVhZGluZzogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nO1xuXG4gIC8qKlxuICAgKiBPbiBgbW91c2UtZG93bmAgZXZlbnQgY2FsbGJhY2suXG4gICAqL1xuICBvbk1vdXNlRG93bjogKGhlYWRpbmc6IFRhYmxlT2ZDb250ZW50cy5JSGVhZGluZykgPT4gdm9pZDtcblxuICAvKipcbiAgICogQ29sbGFwc2UgZXZlbnQgY2FsbGJhY2suXG4gICAqL1xuICBvbkNvbGxhcHNlOiAoaGVhZGluZzogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nKSA9PiB2b2lkO1xufVxuXG4vKipcbiAqIFJlYWN0IGNvbXBvbmVudCBmb3IgYSB0YWJsZSBvZiBjb250ZW50cyBlbnRyeS5cbiAqL1xuZXhwb3J0IGNsYXNzIFRhYmxlT2ZDb250ZW50c0l0ZW0gZXh0ZW5kcyBSZWFjdC5QdXJlQ29tcG9uZW50PFxuICBSZWFjdC5Qcm9wc1dpdGhDaGlsZHJlbjxJVGFibGVPZkNvbnRlbnRzSXRlbXNQcm9wcz5cbj4ge1xuICAvKipcbiAgICogUmVuZGVycyBhIHRhYmxlIG9mIGNvbnRlbnRzIGVudHJ5LlxuICAgKlxuICAgKiBAcmV0dXJucyByZW5kZXJlZCBlbnRyeVxuICAgKi9cbiAgcmVuZGVyKCk6IEpTWC5FbGVtZW50IHwgbnVsbCB7XG4gICAgY29uc3QgeyBjaGlsZHJlbiwgaXNBY3RpdmUsIGhlYWRpbmcsIG9uQ29sbGFwc2UsIG9uTW91c2VEb3duIH0gPSB0aGlzLnByb3BzO1xuXG4gICAgcmV0dXJuIChcbiAgICAgIDxsaSBjbGFzc05hbWU9XCJqcC10b2NJdGVtXCIga2V5PXtgJHtoZWFkaW5nLmxldmVsfS0ke2hlYWRpbmcudGV4dH1gfT5cbiAgICAgICAgPGRpdlxuICAgICAgICAgIGNsYXNzTmFtZT17YGpwLXRvY0l0ZW0taGVhZGluZyAke1xuICAgICAgICAgICAgaXNBY3RpdmUgPyAnanAtdG9jSXRlbS1hY3RpdmUnIDogJydcbiAgICAgICAgICB9YH1cbiAgICAgICAgICBvbk1vdXNlRG93bj17KGV2ZW50OiBSZWFjdC5TeW50aGV0aWNFdmVudDxIVE1MRGl2RWxlbWVudD4pID0+IHtcbiAgICAgICAgICAgIC8vIFJlYWN0IG9ubHkgb24gZGVlcGVzdCBpdGVtXG4gICAgICAgICAgICBpZiAoIWV2ZW50LmRlZmF1bHRQcmV2ZW50ZWQpIHtcbiAgICAgICAgICAgICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICAgICAgICAgICAgb25Nb3VzZURvd24oaGVhZGluZyk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfX1cbiAgICAgICAgPlxuICAgICAgICAgIDxidXR0b25cbiAgICAgICAgICAgIGNsYXNzTmFtZT1cImpwLXRvY0l0ZW0tY29sbGFwc2VyXCJcbiAgICAgICAgICAgIG9uQ2xpY2s9eyhldmVudDogUmVhY3QuTW91c2VFdmVudCkgPT4ge1xuICAgICAgICAgICAgICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgICAgICAgICBvbkNvbGxhcHNlKGhlYWRpbmcpO1xuICAgICAgICAgICAgfX1cbiAgICAgICAgICAgIHN0eWxlPXt7IHZpc2liaWxpdHk6IGNoaWxkcmVuID8gJ3Zpc2libGUnIDogJ2hpZGRlbicgfX1cbiAgICAgICAgICA+XG4gICAgICAgICAgICB7aGVhZGluZy5jb2xsYXBzZWQgPyAoXG4gICAgICAgICAgICAgIDxjYXJldFJpZ2h0SWNvbi5yZWFjdCB0YWc9XCJzcGFuXCIgd2lkdGg9XCIyMHB4XCIgLz5cbiAgICAgICAgICAgICkgOiAoXG4gICAgICAgICAgICAgIDxjYXJldERvd25JY29uLnJlYWN0IHRhZz1cInNwYW5cIiB3aWR0aD1cIjIwcHhcIiAvPlxuICAgICAgICAgICAgKX1cbiAgICAgICAgICA8L2J1dHRvbj5cbiAgICAgICAgICA8c3BhblxuICAgICAgICAgICAgY2xhc3NOYW1lPVwianAtdG9jSXRlbS1jb250ZW50XCJcbiAgICAgICAgICAgIHRpdGxlPXtoZWFkaW5nLnRleHR9XG4gICAgICAgICAgICB7Li4uaGVhZGluZy5kYXRhc2V0fVxuICAgICAgICAgID5cbiAgICAgICAgICAgIHtoZWFkaW5nLnByZWZpeH1cbiAgICAgICAgICAgIHtoZWFkaW5nLnRleHR9XG4gICAgICAgICAgPC9zcGFuPlxuICAgICAgICA8L2Rpdj5cbiAgICAgICAge2NoaWxkcmVuICYmICFoZWFkaW5nLmNvbGxhcHNlZCAmJiA8b2w+e2NoaWxkcmVufTwvb2w+fVxuICAgICAgPC9saT5cbiAgICApO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCAqIGFzIFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IFRhYmxlT2ZDb250ZW50c0l0ZW0gfSBmcm9tICcuL3RvY2l0ZW0nO1xuaW1wb3J0IHsgVGFibGVPZkNvbnRlbnRzIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIEludGVyZmFjZSBkZXNjcmliaW5nIGNvbXBvbmVudCBwcm9wZXJ0aWVzLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElUYWJsZU9mQ29udGVudHNUcmVlUHJvcHMge1xuICAvKipcbiAgICogQ3VycmVudGx5IGFjdGl2ZSBoZWFkaW5nLlxuICAgKi9cbiAgYWN0aXZlSGVhZGluZzogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nIHwgbnVsbDtcbiAgLyoqXG4gICAqIFR5cGUgb2YgZG9jdW1lbnQgc3VwcG9ydGVkIGJ5IHRoZSBtb2RlbC5cbiAgICovXG4gIGRvY3VtZW50VHlwZTogc3RyaW5nO1xuICAvKipcbiAgICogTGlzdCBvZiBoZWFkaW5ncyB0byByZW5kZXIuXG4gICAqL1xuICBoZWFkaW5nczogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nW107XG4gIC8qKlxuICAgKiBTZXQgYWN0aXZlIGhlYWRpbmcuXG4gICAqL1xuICBzZXRBY3RpdmVIZWFkaW5nOiAoaGVhZGluZzogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nKSA9PiB2b2lkO1xuICAvKipcbiAgICogQ29sbGFwc2UgaGVhZGluZyBjYWxsYmFjay5cbiAgICovXG4gIG9uQ29sbGFwc2VDaGFuZ2U6IChoZWFkaW5nOiBUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcpID0+IHZvaWQ7XG59XG5cbi8qKlxuICogUmVhY3QgY29tcG9uZW50IGZvciBhIHRhYmxlIG9mIGNvbnRlbnRzIHRyZWUuXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWJsZU9mQ29udGVudHNUcmVlIGV4dGVuZHMgUmVhY3QuUHVyZUNvbXBvbmVudDxJVGFibGVPZkNvbnRlbnRzVHJlZVByb3BzPiB7XG4gIC8qKlxuICAgKiBSZW5kZXJzIGEgdGFibGUgb2YgY29udGVudHMgdHJlZS5cbiAgICovXG4gIHJlbmRlcigpOiBKU1guRWxlbWVudCB7XG4gICAgY29uc3QgeyBkb2N1bWVudFR5cGUgfSA9IHRoaXMucHJvcHM7XG4gICAgcmV0dXJuIChcbiAgICAgIDxvbFxuICAgICAgICBjbGFzc05hbWU9XCJqcC1UYWJsZU9mQ29udGVudHMtY29udGVudFwiXG4gICAgICAgIHsuLi57ICdkYXRhLWRvY3VtZW50LXR5cGUnOiBkb2N1bWVudFR5cGUgfX1cbiAgICAgID5cbiAgICAgICAge3RoaXMuYnVpbGRUcmVlKCl9XG4gICAgICA8L29sPlxuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogQ29udmVydCB0aGUgZmxhdCBoZWFkaW5ncyBsaXN0IHRvIGEgbmVzdGVkIHRyZWUgbGlzdFxuICAgKi9cbiAgcHJvdGVjdGVkIGJ1aWxkVHJlZSgpOiBKU1guRWxlbWVudFtdIHtcbiAgICBpZiAodGhpcy5wcm9wcy5oZWFkaW5ncy5sZW5ndGggPT09IDApIHtcbiAgICAgIHJldHVybiBbXTtcbiAgICB9XG5cbiAgICBsZXQgZ2xvYmFsSW5kZXggPSAwO1xuXG4gICAgY29uc3QgZ2V0Q2hpbGRyZW4gPSAoXG4gICAgICBpdGVtczogVGFibGVPZkNvbnRlbnRzLklIZWFkaW5nW10sXG4gICAgICBsZXZlbDogbnVtYmVyXG4gICAgKTogSlNYLkVsZW1lbnRbXSA9PiB7XG4gICAgICBjb25zdCBuZXN0ZWQgPSBuZXcgQXJyYXk8SlNYLkVsZW1lbnQ+KCk7XG4gICAgICB3aGlsZSAoZ2xvYmFsSW5kZXggPCBpdGVtcy5sZW5ndGgpIHtcbiAgICAgICAgY29uc3QgY3VycmVudCA9IGl0ZW1zW2dsb2JhbEluZGV4XTtcbiAgICAgICAgaWYgKGN1cnJlbnQubGV2ZWwgPj0gbGV2ZWwpIHtcbiAgICAgICAgICBnbG9iYWxJbmRleCArPSAxO1xuICAgICAgICAgIGNvbnN0IG5leHQgPSBpdGVtc1tnbG9iYWxJbmRleF07XG5cbiAgICAgICAgICBuZXN0ZWQucHVzaChcbiAgICAgICAgICAgIDxUYWJsZU9mQ29udGVudHNJdGVtXG4gICAgICAgICAgICAgIGtleT17YCR7Y3VycmVudC5sZXZlbH0tJHtjdXJyZW50LnRleHR9YH1cbiAgICAgICAgICAgICAgaXNBY3RpdmU9e1xuICAgICAgICAgICAgICAgICEhdGhpcy5wcm9wcy5hY3RpdmVIZWFkaW5nICYmXG4gICAgICAgICAgICAgICAgY3VycmVudCA9PT0gdGhpcy5wcm9wcy5hY3RpdmVIZWFkaW5nXG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgaGVhZGluZz17Y3VycmVudH1cbiAgICAgICAgICAgICAgb25Nb3VzZURvd249e3RoaXMucHJvcHMuc2V0QWN0aXZlSGVhZGluZ31cbiAgICAgICAgICAgICAgb25Db2xsYXBzZT17dGhpcy5wcm9wcy5vbkNvbGxhcHNlQ2hhbmdlfVxuICAgICAgICAgICAgPlxuICAgICAgICAgICAgICB7bmV4dCAmJiBuZXh0LmxldmVsID4gbGV2ZWwgJiYgZ2V0Q2hpbGRyZW4oaXRlbXMsIGxldmVsICsgMSl9XG4gICAgICAgICAgICA8L1RhYmxlT2ZDb250ZW50c0l0ZW0+XG4gICAgICAgICAgKTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBicmVhaztcbiAgICAgICAgfVxuICAgICAgfVxuXG4gICAgICByZXR1cm4gbmVzdGVkO1xuICAgIH07XG5cbiAgICByZXR1cm4gZ2V0Q2hpbGRyZW4odGhpcy5wcm9wcy5oZWFkaW5ncywgdGhpcy5wcm9wcy5oZWFkaW5nc1swXS5sZXZlbCk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHR5cGUgeyBUb29sYmFyUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgdHlwZSB7IElPYnNlcnZhYmxlTGlzdCB9IGZyb20gJ0BqdXB5dGVybGFiL29ic2VydmFibGVzJztcbmltcG9ydCB0eXBlIHsgVkRvbVJlbmRlcmVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgdHlwZSB7IEpTT05PYmplY3QgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB0eXBlIHsgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHR5cGUgeyBJU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHR5cGUgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIEludGVyZmFjZSBkZXNjcmliaW5nIHRoZSB0YWJsZSBvZiBjb250ZW50cyByZWdpc3RyeS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJVGFibGVPZkNvbnRlbnRzUmVnaXN0cnkge1xuICAvKipcbiAgICogRmluZHMgYSB0YWJsZSBvZiBjb250ZW50cyBtb2RlbCBmb3IgYSB3aWRnZXQuXG4gICAqXG4gICAqICMjIE5vdGVzXG4gICAqXG4gICAqIC0gICBJZiB1bmFibGUgdG8gZmluZCBhIHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsLCB0aGUgbWV0aG9kIHJldHVybiBgdW5kZWZpbmVkYC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIHdpZGdldFxuICAgKiBAcGFyYW0gY29uZmlndXJhdGlvbiAtIFRhYmxlIG9mIGNvbnRlbnRzIGNvbmZpZ3VyYXRpb25cbiAgICogQHJldHVybnMgVGFibGUgb2YgY29udGVudHMgbW9kZWwgb3IgdW5kZWZpbmVkIGlmIG5vdCBmb3VuZFxuICAgKi9cbiAgZ2V0TW9kZWwoXG4gICAgd2lkZ2V0OiBXaWRnZXQsXG4gICAgY29uZmlndXJhdGlvbj86IFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnXG4gICk6IFRhYmxlT2ZDb250ZW50cy5Nb2RlbCB8IHVuZGVmaW5lZDtcblxuICAvKipcbiAgICogQWRkcyBhIHRhYmxlIG9mIGNvbnRlbnRzIGZhY3RvcnkgdG8gdGhlIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiBAcGFyYW0gZmFjdG9yeSAtIHRhYmxlIG9mIGNvbnRlbnRzIGZhY3RvcnlcbiAgICovXG4gIGFkZChmYWN0b3J5OiBUYWJsZU9mQ29udGVudHMuSUZhY3RvcnkpOiBJRGlzcG9zYWJsZTtcbn1cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50cyByZWdpc3RyeSB0b2tlbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElUYWJsZU9mQ29udGVudHNSZWdpc3RyeSA9IG5ldyBUb2tlbjxJVGFibGVPZkNvbnRlbnRzUmVnaXN0cnk+KFxuICAnQGp1cHl0ZXJsYWIvdG9jOklUYWJsZU9mQ29udGVudHNSZWdpc3RyeSdcbik7XG5cbi8qKlxuICogSW50ZXJmYWNlIGZvciB0aGUgdGFibGUgb2YgY29udGVudHMgdHJhY2tlclxuICovXG5leHBvcnQgaW50ZXJmYWNlIElUYWJsZU9mQ29udGVudHNUcmFja2VyIHtcbiAgLyoqXG4gICAqIEdldCB0aGUgbW9kZWwgYXNzb2NpYXRlZCB3aXRoIGEgZ2l2ZW4gd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFdpZGdldFxuICAgKi9cbiAgZ2V0KHdpZGdldDogV2lkZ2V0KTogVGFibGVPZkNvbnRlbnRzLklNb2RlbDxUYWJsZU9mQ29udGVudHMuSUhlYWRpbmc+IHwgbnVsbDtcbn1cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50cyB0cmFja2VyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVRhYmxlT2ZDb250ZW50c1RyYWNrZXIgPSBuZXcgVG9rZW48SVRhYmxlT2ZDb250ZW50c1RyYWNrZXI+KFxuICAnQGp1cHl0ZXJsYWIvdG9jOklUYWJsZU9mQ29udGVudHNUcmFja2VyJ1xuKTtcblxuLyoqXG4gKiBOYW1lc3BhY2UgZm9yIHRhYmxlIG9mIGNvbnRlbnRzIGludGVyZmFjZVxuICovXG5leHBvcnQgbmFtZXNwYWNlIFRhYmxlT2ZDb250ZW50cyB7XG4gIC8qKlxuICAgKiBUYWJsZSBvZiBjb250ZW50IG1vZGVsIGZhY3RvcnkgaW50ZXJmYWNlXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElGYWN0b3J5PFcgZXh0ZW5kcyBXaWRnZXQgPSBXaWRnZXQ+IHtcbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBmYWN0b3J5IGNhbiBoYW5kbGUgdGhlIHdpZGdldCBvciBub3QuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gd2lkZ2V0IC0gd2lkZ2V0XG4gICAgICogQHJldHVybnMgYm9vbGVhbiBpbmRpY2F0aW5nIGEgVG9DIGNhbiBiZSBnZW5lcmF0ZWRcbiAgICAgKi9cbiAgICBpc0FwcGxpY2FibGU6ICh3aWRnZXQ6IFcpID0+IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBDcmVhdGUgYSBuZXcgdGFibGUgb2YgY29udGVudHMgbW9kZWwgZm9yIHRoZSB3aWRnZXRcbiAgICAgKlxuICAgICAqIEBwYXJhbSB3aWRnZXQgLSB3aWRnZXRcbiAgICAgKiBAcGFyYW0gY29uZmlndXJhdGlvbiAtIFRhYmxlIG9mIGNvbnRlbnRzIGNvbmZpZ3VyYXRpb25cbiAgICAgKiBAcmV0dXJucyBUaGUgdGFibGUgb2YgY29udGVudHMgbW9kZWxcbiAgICAgKi9cbiAgICBjcmVhdGVOZXc6IChcbiAgICAgIHdpZGdldDogVyxcbiAgICAgIGNvbmZpZ3VyYXRpb24/OiBUYWJsZU9mQ29udGVudHMuSUNvbmZpZ1xuICAgICkgPT4gSU1vZGVsPElIZWFkaW5nPjtcbiAgfVxuXG4gIC8qKlxuICAgKiBUYWJsZSBvZiBDb250ZW50cyBjb25maWd1cmF0aW9uXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogQSBkb2N1bWVudCBtb2RlbCBtYXkgaWdub3JlIHNvbWUgb2YgdGhvc2Ugb3B0aW9ucy5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvbmZpZyBleHRlbmRzIEpTT05PYmplY3Qge1xuICAgIC8qKlxuICAgICAqIEJhc2UgbGV2ZWwgZm9yIHRoZSBoaWdoZXN0IGhlYWRpbmdzXG4gICAgICovXG4gICAgYmFzZU51bWJlcmluZzogbnVtYmVyO1xuICAgIC8qKlxuICAgICAqIE1heGltYWwgZGVwdGggb2YgaGVhZGluZ3MgdG8gZGlzcGxheVxuICAgICAqL1xuICAgIG1heGltYWxEZXB0aDogbnVtYmVyO1xuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gbnVtYmVyIGZpcnN0LWxldmVsIGhlYWRpbmdzIG9yIG5vdC5cbiAgICAgKi9cbiAgICBudW1iZXJpbmdIMTogYm9vbGVhbjtcbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIG51bWJlciBoZWFkaW5ncyBpbiBkb2N1bWVudCBvciBub3QuXG4gICAgICovXG4gICAgbnVtYmVySGVhZGVyczogYm9vbGVhbjtcbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRvIGluY2x1ZGUgY2VsbCBvdXRwdXRzIGluIGhlYWRpbmdzIG9yIG5vdC5cbiAgICAgKi9cbiAgICBpbmNsdWRlT3V0cHV0OiBib29sZWFuO1xuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gc3luY2hyb25pemUgaGVhZGluZyBjb2xsYXBzZSBzdGF0ZSBiZXR3ZWVuIHRoZSBUb0MgYW5kIHRoZSBkb2N1bWVudCBvciBub3QuXG4gICAgICovXG4gICAgc3luY0NvbGxhcHNlU3RhdGU6IGJvb2xlYW47XG4gIH1cblxuICAvKipcbiAgICogRGVmYXVsdCB0YWJsZSBvZiBjb250ZW50IGNvbmZpZ3VyYXRpb25cbiAgICovXG4gIGV4cG9ydCBjb25zdCBkZWZhdWx0Q29uZmlnOiBJQ29uZmlnID0ge1xuICAgIGJhc2VOdW1iZXJpbmc6IDEsXG4gICAgbWF4aW1hbERlcHRoOiA0LFxuICAgIG51bWJlcmluZ0gxOiB0cnVlLFxuICAgIG51bWJlckhlYWRlcnM6IGZhbHNlLFxuICAgIGluY2x1ZGVPdXRwdXQ6IHRydWUsXG4gICAgc3luY0NvbGxhcHNlU3RhdGU6IGZhbHNlXG4gIH07XG5cbiAgLyoqXG4gICAqIEludGVyZmFjZSBkZXNjcmliaW5nIGEgaGVhZGluZy5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUhlYWRpbmcge1xuICAgIC8qKlxuICAgICAqIEhlYWRpbmcgdGV4dC5cbiAgICAgKi9cbiAgICB0ZXh0OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBIVE1MIGhlYWRpbmcgbGV2ZWwuXG4gICAgICovXG4gICAgbGV2ZWw6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIEhlYWRpbmcgcHJlZml4LlxuICAgICAqL1xuICAgIHByZWZpeD86IHN0cmluZyB8IG51bGw7XG5cbiAgICAvKipcbiAgICAgKiBEYXRhc2V0IHRvIGFkZCB0byB0aGUgaXRlbSBub2RlXG4gICAgICovXG4gICAgZGF0YXNldD86IFJlY29yZDxzdHJpbmcsIHN0cmluZz47XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBoZWFkaW5nIGlzIGNvbGxhcHNlZCBvciBub3RcbiAgICAgKi9cbiAgICBjb2xsYXBzZWQ/OiBib29sZWFuO1xuICB9XG5cbiAgLyoqXG4gICAqIEludGVyZmFjZSBkZXNjcmliaW5nIGEgd2lkZ2V0IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJTW9kZWw8SCBleHRlbmRzIElIZWFkaW5nPiBleHRlbmRzIFZEb21SZW5kZXJlci5JTW9kZWwge1xuICAgIC8qKlxuICAgICAqIEFjdGl2ZSBoZWFkaW5nXG4gICAgICovXG4gICAgcmVhZG9ubHkgYWN0aXZlSGVhZGluZzogSCB8IG51bGw7XG5cbiAgICAvKipcbiAgICAgKiBTaWduYWwgZW1pdHRlZCB3aGVuIHRoZSBhY3RpdmUgaGVhZGluZyBjaGFuZ2VzLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGFjdGl2ZUhlYWRpbmdDaGFuZ2VkOiBJU2lnbmFsPElNb2RlbDxIPiwgSCB8IG51bGw+O1xuXG4gICAgLyoqXG4gICAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiBhIHRhYmxlIG9mIGNvbnRlbnQgc2VjdGlvbiBjb2xsYXBzZSBzdGF0ZSBjaGFuZ2VzLlxuICAgICAqXG4gICAgICogSWYgYWxsIGhlYWRpbmdzIHN0YXRlIGFyZSBzZXQgYXQgdGhlIHNhbWUgdGltZSwgdGhlIGFyZ3VtZW50IGlzIG51bGwuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY29sbGFwc2VDaGFuZ2VkOiBJU2lnbmFsPElNb2RlbDxIPiwgSCB8IG51bGw+O1xuXG4gICAgLyoqXG4gICAgICogTW9kZWwgY29uZmlndXJhdGlvblxuICAgICAqL1xuICAgIHJlYWRvbmx5IGNvbmZpZ3VyYXRpb246IElDb25maWc7XG5cbiAgICAvKipcbiAgICAgKiBUeXBlIG9mIGRvY3VtZW50IHN1cHBvcnRlZCBieSB0aGUgbW9kZWwuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogQSBgZGF0YS1kb2N1bWVudC10eXBlYCBhdHRyaWJ1dGUgd2l0aCB0aGlzIHZhbHVlIHdpbGwgYmUgc2V0XG4gICAgICogb24gdGhlIHRyZWUgdmlldyBgLmpwLVRhYmxlT2ZDb250ZW50cy1jb250ZW50W2RhdGEtZG9jdW1lbnQtdHlwZT1cIi4uLlwiXWBcbiAgICAgKi9cbiAgICByZWFkb25seSBkb2N1bWVudFR5cGU6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFJldHVybnMgdGhlIGxpc3Qgb2YgaGVhZGluZ3MuXG4gICAgICpcbiAgICAgKiBAcmV0dXJucyBsaXN0IG9mIGhlYWRpbmdzXG4gICAgICovXG4gICAgcmVhZG9ubHkgaGVhZGluZ3M6IEhbXTtcblxuICAgIC8qKlxuICAgICAqIFNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIGhlYWRpbmdzIGNoYW5nZXMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgaGVhZGluZ3NDaGFuZ2VkOiBJU2lnbmFsPElNb2RlbDxIPiwgdm9pZD47XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBtb2RlbCBuZWVkcyB0byBiZSBrZXB0IHVwIHRvIGRhdGUgb3Igbm90LlxuICAgICAqXG4gICAgICogIyMjIE5vdGVzXG4gICAgICogVGhpcyBpcyBzZXQgdG8gYHRydWVgIGlmIHRoZSBUb0MgcGFuZWwgaXMgdmlzaWJsZSBhbmRcbiAgICAgKiB0byBgZmFsc2VgIGlmIGl0IGlzIGhpZGRlbi4gQnV0IHNvbWUgbW9kZWxzIG1heSByZXF1aXJlXG4gICAgICogdG8gYmUgYWx3YXlzIGFjdGl2ZTsgZS5nLiB0byBhZGQgbnVtYmVyaW5nIGluIHRoZSBkb2N1bWVudC5cbiAgICAgKi9cbiAgICBpc0FjdGl2ZTogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFNldCBhIG5ldyBhY3RpdmUgaGVhZGluZy5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBoZWFkaW5nIFRoZSBuZXcgYWN0aXZlIGhlYWRpbmdcbiAgICAgKiBAcGFyYW0gZW1pdFNpZ25hbCBXaGV0aGVyIHRvIGVtaXQgdGhlIGFjdGl2ZUhlYWRpbmdDaGFuZ2VkIHNpZ25hbCBvciBub3QuXG4gICAgICovXG4gICAgc2V0QWN0aXZlSGVhZGluZyhoZWFkaW5nOiBIIHwgbnVsbCwgZW1pdFNpZ25hbD86IGJvb2xlYW4pOiB2b2lkO1xuXG4gICAgLyoqXG4gICAgICogTW9kZWwgY29uZmlndXJhdGlvbiBzZXR0ZXIuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gYyBOZXcgY29uZmlndXJhdGlvblxuICAgICAqL1xuICAgIHNldENvbmZpZ3VyYXRpb24oYzogUGFydGlhbDxJQ29uZmlnPik6IHZvaWQ7XG5cbiAgICAvKipcbiAgICAgKiBMaXN0IG9mIGNvbmZpZ3VyYXRpb24gb3B0aW9ucyBzdXBwb3J0ZWQgYnkgdGhlIG1vZGVsLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHN1cHBvcnRlZE9wdGlvbnM6IChrZXlvZiBJQ29uZmlnKVtdO1xuXG4gICAgLyoqXG4gICAgICogRG9jdW1lbnQgdGl0bGVcbiAgICAgKi9cbiAgICB0aXRsZT86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIENhbGxiYWNrIG9uIGhlYWRpbmcgY29sbGFwc2UuXG4gICAgICpcbiAgICAgKiBAcGFyYW0gb3B0aW9ucy5oZWFkaW5nIFRoZSBoZWFkaW5nIHRvIGNoYW5nZSBzdGF0ZSAoYWxsIGhlYWRpbmdzIGlmIG5vdCBwcm92aWRlZClcbiAgICAgKiBAcGFyYW0gb3B0aW9ucy5jb2xsYXBzZWQgVGhlIG5ldyBjb2xsYXBzZWQgc3RhdHVzICh0b2dnbGUgZXhpc3Rpbmcgc3RhdHVzIGlmIG5vdCBwcm92aWRlZClcbiAgICAgKi9cbiAgICB0b2dnbGVDb2xsYXBzZTogKG9wdGlvbnM6IHsgaGVhZGluZz86IEg7IGNvbGxhcHNlZD86IGJvb2xlYW4gfSkgPT4gdm9pZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZW5lcmljIHRhYmxlIG9mIGNvbnRlbnRzIHR5cGVcbiAgICovXG4gIGV4cG9ydCB0eXBlIE1vZGVsID0gSU1vZGVsPElIZWFkaW5nPjtcblxuICAvKipcbiAgICogSW50ZXJmYWNlIGRlc2NyaWJpbmcgdGFibGUgb2YgY29udGVudHMgd2lkZ2V0IG9wdGlvbnMuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBUYWJsZSBvZiBjb250ZW50cyBtb2RlbC5cbiAgICAgKi9cbiAgICBtb2RlbD86IElNb2RlbDxJSGVhZGluZz47XG4gIH1cblxuICAvKipcbiAgICogSW50ZXJmYWNlIGRlc2NyaWJpbmcgYSB0b29sYmFyIGl0ZW0gbGlzdFxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJVG9vbGJhckl0ZW1zXG4gICAgZXh0ZW5kcyBJT2JzZXJ2YWJsZUxpc3Q8VG9vbGJhclJlZ2lzdHJ5LklUb29sYmFySXRlbT4ge31cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IElUYWJsZU9mQ29udGVudHNUcmFja2VyLCBUYWJsZU9mQ29udGVudHMgfSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogVGFibGUgb2YgY29udGVudHMgdHJhY2tlclxuICovXG5leHBvcnQgY2xhc3MgVGFibGVPZkNvbnRlbnRzVHJhY2tlciBpbXBsZW1lbnRzIElUYWJsZU9mQ29udGVudHNUcmFja2VyIHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdG9yXG4gICAqL1xuICBjb25zdHJ1Y3RvcigpIHtcbiAgICB0aGlzLm1vZGVsTWFwcGluZyA9IG5ldyBXZWFrTWFwPFdpZGdldCwgVGFibGVPZkNvbnRlbnRzLk1vZGVsPigpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRyYWNrIGEgZ2l2ZW4gbW9kZWwuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgV2lkZ2V0XG4gICAqIEBwYXJhbSBtb2RlbCBUYWJsZSBvZiBjb250ZW50cyBtb2RlbFxuICAgKi9cbiAgYWRkKHdpZGdldDogV2lkZ2V0LCBtb2RlbDogVGFibGVPZkNvbnRlbnRzLk1vZGVsKTogdm9pZCB7XG4gICAgdGhpcy5tb2RlbE1hcHBpbmcuc2V0KHdpZGdldCwgbW9kZWwpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCB0aGUgdGFibGUgb2YgY29udGVudHMgbW9kZWwgYXNzb2NpYXRlZCB3aXRoIGEgZ2l2ZW4gd2lkZ2V0LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFdpZGdldFxuICAgKiBAcmV0dXJucyBUaGUgdGFibGUgb2YgY29udGVudHMgbW9kZWxcbiAgICovXG4gIGdldCh3aWRnZXQ6IFdpZGdldCk6IFRhYmxlT2ZDb250ZW50cy5Nb2RlbCB8IG51bGwge1xuICAgIGNvbnN0IG1vZGVsID0gdGhpcy5tb2RlbE1hcHBpbmcuZ2V0KHdpZGdldCk7XG5cbiAgICByZXR1cm4gIW1vZGVsIHx8IG1vZGVsLmlzRGlzcG9zZWQgPyBudWxsIDogbW9kZWw7XG4gIH1cblxuICBwcm90ZWN0ZWQgbW9kZWxNYXBwaW5nOiBXZWFrTWFwPFdpZGdldCwgVGFibGVPZkNvbnRlbnRzLk1vZGVsPjtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgVkRvbVJlbmRlcmVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgeyBUYWJsZU9mQ29udGVudHNUcmVlIH0gZnJvbSAnLi90b2N0cmVlJztcbmltcG9ydCB7IFRhYmxlT2ZDb250ZW50cyB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50cyB3aWRnZXQuXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWJsZU9mQ29udGVudHNXaWRnZXQgZXh0ZW5kcyBWRG9tUmVuZGVyZXI8VGFibGVPZkNvbnRlbnRzLklNb2RlbDxUYWJsZU9mQ29udGVudHMuSUhlYWRpbmc+IHwgbnVsbD4ge1xuICAvKipcbiAgICogQ29uc3RydWN0b3JcbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMgV2lkZ2V0IG9wdGlvbnNcbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IFRhYmxlT2ZDb250ZW50cy5JT3B0aW9ucyA9IHt9KSB7XG4gICAgc3VwZXIob3B0aW9ucy5tb2RlbCk7XG4gIH1cblxuICAvKipcbiAgICogUmVuZGVyIHRoZSBjb250ZW50IG9mIHRoaXMgd2lkZ2V0IHVzaW5nIHRoZSB2aXJ0dWFsIERPTS5cbiAgICpcbiAgICogVGhpcyBtZXRob2Qgd2lsbCBiZSBjYWxsZWQgYW55dGltZSB0aGUgd2lkZ2V0IG5lZWRzIHRvIGJlIHJlbmRlcmVkLCB3aGljaFxuICAgKiBpbmNsdWRlcyBsYXlvdXQgdHJpZ2dlcmVkIHJlbmRlcmluZy5cbiAgICovXG4gIHJlbmRlcigpOiBKU1guRWxlbWVudCB8IG51bGwge1xuICAgIGlmICghdGhpcy5tb2RlbCkge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuXG4gICAgcmV0dXJuIChcbiAgICAgIDxUYWJsZU9mQ29udGVudHNUcmVlXG4gICAgICAgIGFjdGl2ZUhlYWRpbmc9e3RoaXMubW9kZWwuYWN0aXZlSGVhZGluZ31cbiAgICAgICAgZG9jdW1lbnRUeXBlPXt0aGlzLm1vZGVsLmRvY3VtZW50VHlwZX1cbiAgICAgICAgaGVhZGluZ3M9e3RoaXMubW9kZWwuaGVhZGluZ3N9XG4gICAgICAgIG9uQ29sbGFwc2VDaGFuZ2U9eyhoZWFkaW5nOiBUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcpID0+IHtcbiAgICAgICAgICB0aGlzLm1vZGVsIS50b2dnbGVDb2xsYXBzZSh7IGhlYWRpbmcgfSk7XG4gICAgICAgIH19XG4gICAgICAgIHNldEFjdGl2ZUhlYWRpbmc9eyhoZWFkaW5nOiBUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcpID0+IHtcbiAgICAgICAgICB0aGlzLm1vZGVsIS5zZXRBY3RpdmVIZWFkaW5nKGhlYWRpbmcpO1xuICAgICAgICB9fVxuICAgICAgPjwvVGFibGVPZkNvbnRlbnRzVHJlZT5cbiAgICApO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFRhYmxlT2ZDb250ZW50cyB9IGZyb20gJy4uL3Rva2Vucyc7XG5cbi8qKlxuICogQ2xhc3MgdXNlZCB0byBtYXJrIG51bWJlcmluZyBwcmVmaXggZm9yIGhlYWRpbmdzIGluIGEgZG9jdW1lbnQuXG4gKi9cbmV4cG9ydCBjb25zdCBOVU1CRVJJTkdfQ0xBU1MgPSAnbnVtYmVyaW5nLWVudHJ5JztcblxuLyoqXG4gKiBIVE1MIGhlYWRpbmdcbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJSFRNTEhlYWRpbmcgZXh0ZW5kcyBUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcge1xuICAvKipcbiAgICogSFRNTCBpZFxuICAgKi9cbiAgaWQ/OiBzdHJpbmcgfCBudWxsO1xufVxuXG4vKipcbiAqIFJldHVybnMgd2hldGhlciBhIE1JTUUgdHlwZSBjb3JyZXNwb25kcyB0byBlaXRoZXIgSFRNTC5cbiAqXG4gKiBAcGFyYW0gbWltZSAtIE1JTUUgdHlwZSBzdHJpbmdcbiAqIEByZXR1cm5zIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcHJvdmlkZWQgTUlNRSB0eXBlIGNvcnJlc3BvbmRzIHRvIGVpdGhlciBIVE1MXG4gKlxuICogQGV4YW1wbGVcbiAqIGNvbnN0IGJvb2wgPSBpc0hUTUwoJ3RleHQvaHRtbCcpO1xuICogLy8gcmV0dXJucyB0cnVlXG4gKlxuICogQGV4YW1wbGVcbiAqIGNvbnN0IGJvb2wgPSBpc0hUTUwoJ3RleHQvcGxhaW4nKTtcbiAqIC8vIHJldHVybnMgZmFsc2VcbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGlzSFRNTChtaW1lOiBzdHJpbmcpOiBib29sZWFuIHtcbiAgcmV0dXJuIG1pbWUgPT09ICd0ZXh0L2h0bWwnO1xufVxuXG4vKipcbiAqIFBhcnNlIGEgSFRNTCBzdHJpbmcgZm9yIGhlYWRpbmdzLlxuICpcbiAqICMjIyBOb3Rlc1xuICogVGhlIGh0bWwgc3RyaW5nIGlzIG5vdCBzYW5pdGl6ZWQgLSB1c2Ugd2l0aCBjYXV0aW9uXG4gKlxuICogQHBhcmFtIGh0bWwgSFRNTCBzdHJpbmcgdG8gcGFyc2VcbiAqIEBwYXJhbSBvcHRpb25zIE9wdGlvbnNcbiAqIEBwYXJhbSBpbml0aWFsTGV2ZWxzIEluaXRpYWwgbGV2ZWxzIGZvciBwcmVmaXggY29tcHV0YXRpb25cbiAqIEByZXR1cm5zIEV4dHJhY3RlZCBoZWFkaW5nc1xuICovXG5leHBvcnQgZnVuY3Rpb24gZ2V0SFRNTEhlYWRpbmdzKFxuICBodG1sOiBzdHJpbmcsXG4gIG9wdGlvbnM/OiBQYXJ0aWFsPFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnPixcbiAgaW5pdGlhbExldmVsczogbnVtYmVyW10gPSBbXVxuKTogSUhUTUxIZWFkaW5nW10ge1xuICBjb25zdCBjb25maWcgPSB7XG4gICAgLi4uVGFibGVPZkNvbnRlbnRzLmRlZmF1bHRDb25maWcsXG4gICAgLi4ub3B0aW9uc1xuICB9IGFzIFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnO1xuXG4gIGNvbnN0IGNvbnRhaW5lcjogSFRNTERpdkVsZW1lbnQgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgY29udGFpbmVyLmlubmVySFRNTCA9IGh0bWw7XG5cbiAgY29uc3QgbGV2ZWxzID0gaW5pdGlhbExldmVscztcbiAgbGV0IHByZXZpb3VzTGV2ZWwgPSBsZXZlbHMubGVuZ3RoO1xuICBjb25zdCBoZWFkaW5ncyA9IG5ldyBBcnJheTxJSFRNTEhlYWRpbmc+KCk7XG4gIGNvbnN0IGhlYWRlcnMgPSBjb250YWluZXIucXVlcnlTZWxlY3RvckFsbCgnaDEsIGgyLCBoMywgaDQsIGg1LCBoNicpO1xuICBmb3IgKGNvbnN0IGggb2YgaGVhZGVycykge1xuICAgIGlmIChcbiAgICAgIGguY2xhc3NMaXN0LmNvbnRhaW5zKCdqcC10b2MtaWdub3JlJykgfHxcbiAgICAgIGguY2xhc3NMaXN0LmNvbnRhaW5zKCd0b2NTa2lwJylcbiAgICApIHtcbiAgICAgIC8vIHNraXAgdGhpcyBlbGVtZW50IGlmIGEgc3BlY2lhbCBjbGFzcyBuYW1lIGlzIGluY2x1ZGVkXG4gICAgICBjb250aW51ZTtcbiAgICB9XG4gICAgbGV0IGxldmVsID0gcGFyc2VJbnQoaC50YWdOYW1lWzFdLCAxMCk7XG5cbiAgICBpZiAobGV2ZWwgPiAwICYmIGxldmVsIDw9IGNvbmZpZy5tYXhpbWFsRGVwdGgpIHtcbiAgICAgIGNvbnN0IHByZWZpeCA9IGdldFByZWZpeChsZXZlbCwgcHJldmlvdXNMZXZlbCwgbGV2ZWxzLCBjb25maWcpO1xuICAgICAgcHJldmlvdXNMZXZlbCA9IGxldmVsO1xuXG4gICAgICBoZWFkaW5ncy5wdXNoKHtcbiAgICAgICAgdGV4dDogaC50ZXh0Q29udGVudCA/PyAnJyxcbiAgICAgICAgcHJlZml4LFxuICAgICAgICBsZXZlbCxcbiAgICAgICAgaWQ6IGg/LmdldEF0dHJpYnV0ZSgnaWQnKVxuICAgICAgfSk7XG4gICAgfVxuICB9XG4gIHJldHVybiBoZWFkaW5ncztcbn1cblxuLyoqXG4gKiBBZGQgYW4gaGVhZGluZyBwcmVmaXggdG8gYSBIVE1MIG5vZGUuXG4gKlxuICogQHBhcmFtIGNvbnRhaW5lciBIVE1MIG5vZGUgY29udGFpbmluZyB0aGUgaGVhZGluZ1xuICogQHBhcmFtIHNlbGVjdG9yIEhlYWRpbmcgc2VsZWN0b3JcbiAqIEBwYXJhbSBwcmVmaXggVGl0bGUgcHJlZml4IHRvIGFkZFxuICogQHJldHVybnMgVGhlIG1vZGlmaWVkIEhUTUwgZWxlbWVudFxuICovXG5leHBvcnQgZnVuY3Rpb24gYWRkUHJlZml4KFxuICBjb250YWluZXI6IEVsZW1lbnQsXG4gIHNlbGVjdG9yOiBzdHJpbmcsXG4gIHByZWZpeDogc3RyaW5nXG4pOiBFbGVtZW50IHwgbnVsbCB7XG4gIGxldCBlbGVtZW50ID0gY29udGFpbmVyLnF1ZXJ5U2VsZWN0b3Ioc2VsZWN0b3IpIGFzIEVsZW1lbnQgfCBudWxsO1xuXG4gIGlmICghZWxlbWVudCkge1xuICAgIHJldHVybiBudWxsO1xuICB9XG5cbiAgaWYgKCFlbGVtZW50LnF1ZXJ5U2VsZWN0b3IoYHNwYW4uJHtOVU1CRVJJTkdfQ0xBU1N9YCkpIHtcbiAgICBhZGROdW1iZXJpbmcoZWxlbWVudCwgcHJlZml4KTtcbiAgfSBlbHNlIHtcbiAgICAvLyBUaGVyZSBhcmUgbGlrZWx5IG11bHRpcGxlIGVsZW1lbnRzIHdpdGggdGhlIHNhbWUgc2VsZWN0b3JcbiAgICAvLyAgPT4gdXNlIHRoZSBmaXJzdCBvbmUgd2l0aG91dCBwcmVmaXhcbiAgICBjb25zdCBhbGxFbGVtZW50cyA9IGNvbnRhaW5lci5xdWVyeVNlbGVjdG9yQWxsKHNlbGVjdG9yKTtcbiAgICBmb3IgKGNvbnN0IGVsIG9mIGFsbEVsZW1lbnRzKSB7XG4gICAgICBpZiAoIWVsLnF1ZXJ5U2VsZWN0b3IoYHNwYW4uJHtOVU1CRVJJTkdfQ0xBU1N9YCkpIHtcbiAgICAgICAgZWxlbWVudCA9IGVsO1xuICAgICAgICBhZGROdW1iZXJpbmcoZWwsIHByZWZpeCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgfVxuICAgIH1cbiAgfVxuXG4gIHJldHVybiBlbGVtZW50O1xufVxuXG4vKipcbiAqIFVwZGF0ZSB0aGUgbGV2ZWxzIGFuZCBjcmVhdGUgdGhlIG51bWJlcmluZyBwcmVmaXhcbiAqXG4gKiBAcGFyYW0gbGV2ZWwgQ3VycmVudCBsZXZlbFxuICogQHBhcmFtIHByZXZpb3VzTGV2ZWwgUHJldmlvdXMgbGV2ZWxcbiAqIEBwYXJhbSBsZXZlbHMgTGV2ZWxzIGxpc3RcbiAqIEBwYXJhbSBvcHRpb25zIE9wdGlvbnNcbiAqIEByZXR1cm5zIFRoZSBudW1iZXJpbmcgcHJlZml4XG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBnZXRQcmVmaXgoXG4gIGxldmVsOiBudW1iZXIsXG4gIHByZXZpb3VzTGV2ZWw6IG51bWJlcixcbiAgbGV2ZWxzOiBudW1iZXJbXSxcbiAgb3B0aW9uczogVGFibGVPZkNvbnRlbnRzLklDb25maWdcbik6IHN0cmluZyB7XG4gIGNvbnN0IHsgYmFzZU51bWJlcmluZywgbnVtYmVyaW5nSDEsIG51bWJlckhlYWRlcnMgfSA9IG9wdGlvbnM7XG4gIGxldCBwcmVmaXggPSAnJztcbiAgaWYgKG51bWJlckhlYWRlcnMpIHtcbiAgICBjb25zdCBoaWdoZXN0TGV2ZWwgPSBudW1iZXJpbmdIMSA/IDEgOiAyO1xuICAgIGlmIChsZXZlbCA+IHByZXZpb3VzTGV2ZWwpIHtcbiAgICAgIC8vIEluaXRpYWxpemUgdGhlIG5ldyBsZXZlbHNcbiAgICAgIGZvciAobGV0IGwgPSBwcmV2aW91c0xldmVsOyBsIDwgbGV2ZWwgLSAxOyBsKyspIHtcbiAgICAgICAgbGV2ZWxzW2xdID0gMDtcbiAgICAgIH1cbiAgICAgIGxldmVsc1tsZXZlbCAtIDFdID0gbGV2ZWwgPT09IGhpZ2hlc3RMZXZlbCA/IGJhc2VOdW1iZXJpbmcgOiAxO1xuICAgIH0gZWxzZSB7XG4gICAgICAvLyBJbmNyZW1lbnQgdGhlIGN1cnJlbnQgbGV2ZWxcbiAgICAgIGxldmVsc1tsZXZlbCAtIDFdICs9IDE7XG5cbiAgICAgIC8vIERyb3AgaGlnaGVyIGxldmVsc1xuICAgICAgaWYgKGxldmVsIDwgcHJldmlvdXNMZXZlbCkge1xuICAgICAgICBsZXZlbHMuc3BsaWNlKGxldmVsKTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICAvLyBJZiB0aGUgaGVhZGVyIGxpc3Qgc2tpcHMgc29tZSBsZXZlbCwgcmVwbGFjZSBtaXNzaW5nIGVsZW1lbnRzIGJ5IDBcbiAgICBpZiAobnVtYmVyaW5nSDEpIHtcbiAgICAgIHByZWZpeCA9IGxldmVscy5tYXAobGV2ZWwgPT4gbGV2ZWwgPz8gMCkuam9pbignLicpICsgJy4gJztcbiAgICB9IGVsc2Uge1xuICAgICAgaWYgKGxldmVscy5sZW5ndGggPiAxKSB7XG4gICAgICAgIHByZWZpeCA9XG4gICAgICAgICAgbGV2ZWxzXG4gICAgICAgICAgICAuc2xpY2UoMSlcbiAgICAgICAgICAgIC5tYXAobGV2ZWwgPT4gbGV2ZWwgPz8gMClcbiAgICAgICAgICAgIC5qb2luKCcuJykgKyAnLiAnO1xuICAgICAgfVxuICAgIH1cbiAgfVxuICByZXR1cm4gcHJlZml4O1xufVxuXG4vKipcbiAqIEFkZCBhIG51bWJlcmluZyBwcmVmaXggdG8gYSBIVE1MIGVsZW1lbnQuXG4gKlxuICogQHBhcmFtIGVsIEhUTUwgZWxlbWVudFxuICogQHBhcmFtIG51bWJlcmluZyBOdW1iZXJpbmcgcHJlZml4IHRvIGFkZFxuICovXG5mdW5jdGlvbiBhZGROdW1iZXJpbmcoZWw6IEVsZW1lbnQsIG51bWJlcmluZzogc3RyaW5nKTogdm9pZCB7XG4gIGVsLmluc2VydEFkamFjZW50SFRNTChcbiAgICAnYWZ0ZXJiZWdpbicsXG4gICAgYDxzcGFuIGNsYXNzPVwiJHtOVU1CRVJJTkdfQ0xBU1N9XCI+JHtudW1iZXJpbmd9PC9zcGFuPmBcbiAgKTtcbn1cblxuLyoqXG4gKiBSZW1vdmUgYWxsIG51bWJlcmluZyBub2RlcyBmcm9tIGVsZW1lbnRcbiAqIEBwYXJhbSBlbGVtZW50IE5vZGUgdG8gY2xlYXJcbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGNsZWFyTnVtYmVyaW5nKGVsZW1lbnQ6IEVsZW1lbnQpOiB2b2lkIHtcbiAgZWxlbWVudC5xdWVyeVNlbGVjdG9yQWxsKGBzcGFuLiR7TlVNQkVSSU5HX0NMQVNTfWApLmZvckVhY2goZWwgPT4ge1xuICAgIGVsLnJlbW92ZSgpO1xuICB9KTtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuZXhwb3J0ICogZnJvbSAnLi9jb21tb24nO1xuZXhwb3J0ICogYXMgTWFya2Rvd24gZnJvbSAnLi9tYXJrZG93bic7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElNYXJrZG93blBhcnNlciwgcmVuZGVyTWFya2Rvd24gfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IFRhYmxlT2ZDb250ZW50cyB9IGZyb20gJy4uL3Rva2Vucyc7XG5pbXBvcnQgeyBnZXRQcmVmaXggfSBmcm9tICcuL2NvbW1vbic7XG5cbi8qKlxuICogTWFya2Rvd24gaGVhZGluZ1xuICovXG5leHBvcnQgaW50ZXJmYWNlIElNYXJrZG93bkhlYWRpbmcgZXh0ZW5kcyBUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcge1xuICAvKipcbiAgICogSGVhZGluZyBsaW5lXG4gICAqL1xuICBsaW5lOiBudW1iZXI7XG4gIC8qKlxuICAgKiBSYXcgc3RyaW5nIGNvbnRhaW5pbmcgdGhlIGhlYWRpbmdcbiAgICovXG4gIHJhdzogc3RyaW5nO1xufVxuXG4vKipcbiAqIEJ1aWxkIHRoZSBoZWFkaW5nIGh0bWwgaWQuXG4gKlxuICogQHBhcmFtIHJhdyBSYXcgbWFya2Rvd24gaGVhZGluZ1xuICogQHBhcmFtIGxldmVsIEhlYWRpbmcgbGV2ZWxcbiAqL1xuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIGdldEhlYWRpbmdJZChcbiAgcGFyc2VyOiBJTWFya2Rvd25QYXJzZXIsXG4gIHJhdzogc3RyaW5nLFxuICBsZXZlbDogbnVtYmVyXG4pOiBQcm9taXNlPHN0cmluZyB8IG51bGw+IHtcbiAgdHJ5IHtcbiAgICBjb25zdCBpbm5lckhUTUwgPSBhd2FpdCBwYXJzZXIucmVuZGVyKHJhdyk7XG5cbiAgICBpZiAoIWlubmVySFRNTCkge1xuICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxuXG4gICAgY29uc3QgY29udGFpbmVyID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgY29udGFpbmVyLmlubmVySFRNTCA9IGlubmVySFRNTDtcbiAgICBjb25zdCBoZWFkZXIgPSBjb250YWluZXIucXVlcnlTZWxlY3RvcihgaCR7bGV2ZWx9YCk7XG4gICAgaWYgKCFoZWFkZXIpIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cblxuICAgIHJldHVybiByZW5kZXJNYXJrZG93bi5jcmVhdGVIZWFkZXJJZChoZWFkZXIpO1xuICB9IGNhdGNoIChyZWFzb24pIHtcbiAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gcGFyc2UgYSBoZWFkaW5nLicsIHJlYXNvbik7XG4gIH1cblxuICByZXR1cm4gbnVsbDtcbn1cblxuLyoqXG4gKiBQYXJzZXMgdGhlIHByb3ZpZGVkIHN0cmluZyBhbmQgcmV0dXJucyBhIGxpc3Qgb2YgaGVhZGluZ3MuXG4gKlxuICogQHBhcmFtIHRleHQgLSBJbnB1dCB0ZXh0XG4gKiBAcGFyYW0gb3B0aW9ucyAtIFBhcnNlciBjb25maWd1cmF0aW9uXG4gKiBAcGFyYW0gaW5pdGlhbExldmVscyAtIEluaXRpYWwgbGV2ZWxzIHRvIHVzZSBmb3IgY29tcHV0aW5nIHRoZSBwcmVmaXhcbiAqIEByZXR1cm5zIExpc3Qgb2YgaGVhZGluZ3NcbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIGdldEhlYWRpbmdzKFxuICB0ZXh0OiBzdHJpbmcsXG4gIG9wdGlvbnM/OiBQYXJ0aWFsPFRhYmxlT2ZDb250ZW50cy5JQ29uZmlnPixcbiAgaW5pdGlhbExldmVsczogbnVtYmVyW10gPSBbXVxuKTogSU1hcmtkb3duSGVhZGluZ1tdIHtcbiAgY29uc3QgY29uZmlnID0ge1xuICAgIC4uLlRhYmxlT2ZDb250ZW50cy5kZWZhdWx0Q29uZmlnLFxuICAgIC4uLm9wdGlvbnNcbiAgfSBhcyBUYWJsZU9mQ29udGVudHMuSUNvbmZpZztcblxuICAvLyBTcGxpdCB0aGUgdGV4dCBpbnRvIGxpbmVzOlxuICBjb25zdCBsaW5lcyA9IHRleHQuc3BsaXQoJ1xcbicpO1xuXG4gIC8vIEl0ZXJhdGUgb3ZlciB0aGUgbGluZXMgdG8gZ2V0IHRoZSBoZWFkZXIgbGV2ZWwgYW5kIHRleHQgZm9yIGVhY2ggbGluZTpcbiAgY29uc3QgbGV2ZWxzID0gaW5pdGlhbExldmVscztcbiAgbGV0IHByZXZpb3VzTGV2ZWwgPSBsZXZlbHMubGVuZ3RoO1xuICBsZXQgaGVhZGluZ3MgPSBuZXcgQXJyYXk8SU1hcmtkb3duSGVhZGluZz4oKTtcbiAgbGV0IGlzQ29kZUJsb2NrO1xuICBmb3IgKGxldCBsaW5lSWR4ID0gMDsgbGluZUlkeCA8IGxpbmVzLmxlbmd0aDsgbGluZUlkeCsrKSB7XG4gICAgbGV0IGxpbmUgPSBsaW5lc1tsaW5lSWR4XTtcblxuICAgIGlmIChsaW5lID09PSAnJykge1xuICAgICAgLy8gQmFpbCBlYXJseVxuICAgICAgY29udGludWU7XG4gICAgfVxuXG4gICAgLy8gRG9uJ3QgY2hlY2sgZm9yIE1hcmtkb3duIGhlYWRpbmdzIGlmIGluIGEgY29kZSBibG9jazpcbiAgICBpZiAobGluZS5zdGFydHNXaXRoKCdgYGAnKSkge1xuICAgICAgaXNDb2RlQmxvY2sgPSAhaXNDb2RlQmxvY2s7XG4gICAgfVxuICAgIGlmIChpc0NvZGVCbG9jaykge1xuICAgICAgY29udGludWU7XG4gICAgfVxuXG4gICAgY29uc3QgaGVhZGluZyA9IHBhcnNlSGVhZGluZyhsaW5lLCBsaW5lc1tsaW5lSWR4ICsgMV0pOyAvLyBhcHBlbmQgdGhlIG5leHQgbGluZSB0byBjYXB0dXJlIGFsdGVybmF0aXZlIHN0eWxlIE1hcmtkb3duIGhlYWRpbmdzXG5cbiAgICBpZiAoaGVhZGluZykge1xuICAgICAgbGV0IGxldmVsID0gaGVhZGluZy5sZXZlbDtcblxuICAgICAgaWYgKGxldmVsID4gMCAmJiBsZXZlbCA8PSBjb25maWcubWF4aW1hbERlcHRoKSB7XG4gICAgICAgIGNvbnN0IHByZWZpeCA9IGdldFByZWZpeChsZXZlbCwgcHJldmlvdXNMZXZlbCwgbGV2ZWxzLCBjb25maWcpO1xuICAgICAgICBwcmV2aW91c0xldmVsID0gbGV2ZWw7XG5cbiAgICAgICAgaGVhZGluZ3MucHVzaCh7XG4gICAgICAgICAgdGV4dDogaGVhZGluZy50ZXh0LFxuICAgICAgICAgIHByZWZpeCxcbiAgICAgICAgICBsZXZlbCxcbiAgICAgICAgICBsaW5lOiBsaW5lSWR4LFxuICAgICAgICAgIHJhdzogaGVhZGluZy5yYXdcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfVxuICB9XG4gIHJldHVybiBoZWFkaW5ncztcbn1cblxuY29uc3QgTUFSS0RPV05fTUlNRV9UWVBFID0gW1xuICAndGV4dC94LWlweXRob25nZm0nLFxuICAndGV4dC94LW1hcmtkb3duJyxcbiAgJ3RleHQveC1nZm0nLFxuICAndGV4dC9tYXJrZG93bidcbl07XG5cbi8qKlxuICogUmV0dXJucyB3aGV0aGVyIGEgTUlNRSB0eXBlIGNvcnJlc3BvbmRzIHRvIGEgTWFya2Rvd24gZmxhdm9yLlxuICpcbiAqIEBwYXJhbSBtaW1lIC0gTUlNRSB0eXBlIHN0cmluZ1xuICogQHJldHVybnMgYm9vbGVhbiBpbmRpY2F0aW5nIHdoZXRoZXIgYSBwcm92aWRlZCBNSU1FIHR5cGUgY29ycmVzcG9uZHMgdG8gYSBNYXJrZG93biBmbGF2b3JcbiAqXG4gKiBAZXhhbXBsZVxuICogY29uc3QgYm9vbCA9IGlzTWFya2Rvd24oJ3RleHQvbWFya2Rvd24nKTtcbiAqIC8vIHJldHVybnMgdHJ1ZVxuICpcbiAqIEBleGFtcGxlXG4gKiBjb25zdCBib29sID0gaXNNYXJrZG93bigndGV4dC9wbGFpbicpO1xuICogLy8gcmV0dXJucyBmYWxzZVxuICovXG5leHBvcnQgZnVuY3Rpb24gaXNNYXJrZG93bihtaW1lOiBzdHJpbmcpOiBib29sZWFuIHtcbiAgcmV0dXJuIE1BUktET1dOX01JTUVfVFlQRS5pbmNsdWRlcyhtaW1lKTtcbn1cblxuLyoqXG4gKiBJbnRlcmZhY2UgZGVzY3JpYmluZyBhIHBhcnNlZCBoZWFkaW5nIHJlc3VsdC5cbiAqXG4gKiBAcHJpdmF0ZVxuICovXG5pbnRlcmZhY2UgSUhlYWRlciB7XG4gIC8qKlxuICAgKiBIZWFkaW5nIHRleHQuXG4gICAqL1xuICB0ZXh0OiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIEhlYWRpbmcgbGV2ZWwuXG4gICAqL1xuICBsZXZlbDogbnVtYmVyO1xuXG4gIC8qKlxuICAgKiBSYXcgc3RyaW5nIGNvbnRhaW5pbmcgdGhlIGhlYWRpbmdcbiAgICovXG4gIHJhdzogc3RyaW5nO1xufVxuXG4vKipcbiAqIFBhcnNlcyBhIGhlYWRpbmcsIGlmIG9uZSBleGlzdHMsIGZyb20gYSBwcm92aWRlZCBzdHJpbmcuXG4gKlxuICogIyMgTm90ZXNcbiAqXG4gKiAtICAgSGVhZGluZyBleGFtcGxlczpcbiAqXG4gKiAgICAgLSAgIE1hcmtkb3duIGhlYWRpbmc6XG4gKlxuICogICAgICAgICBgYGBcbiAqICAgICAgICAgIyBGb29cbiAqICAgICAgICAgYGBgXG4gKlxuICogICAgIC0gICBNYXJrZG93biBoZWFkaW5nIChhbHRlcm5hdGl2ZSBzdHlsZSk6XG4gKlxuICogICAgICAgICBgYGBcbiAqICAgICAgICAgRm9vXG4gKiAgICAgICAgID09PVxuICogICAgICAgICBgYGBcbiAqXG4gKiAgICAgICAgIGBgYFxuICogICAgICAgICBGb29cbiAqICAgICAgICAgLS0tXG4gKiAgICAgICAgIGBgYFxuICpcbiAqICAgICAtICAgSFRNTCBoZWFkaW5nOlxuICpcbiAqICAgICAgICAgYGBgXG4gKiAgICAgICAgIDxoMz5Gb288L2gzPlxuICogICAgICAgICBgYGBcbiAqXG4gKiBAcHJpdmF0ZVxuICogQHBhcmFtIGxpbmUgLSBMaW5lIHRvIHBhcnNlXG4gKiBAcGFyYW0gbmV4dExpbmUgLSBUaGUgbGluZSBhZnRlciB0aGUgb25lIHRvIHBhcnNlXG4gKiBAcmV0dXJucyBoZWFkaW5nIGluZm9cbiAqXG4gKiBAZXhhbXBsZVxuICogY29uc3Qgb3V0ID0gcGFyc2VIZWFkaW5nKCcjIyMgRm9vXFxuJyk7XG4gKiAvLyByZXR1cm5zIHsndGV4dCc6ICdGb28nLCAnbGV2ZWwnOiAzfVxuICpcbiAqIEBleGFtcGxlXG4gKiBjb25zdCBvdXQgPSBwYXJzZUhlYWRpbmcoJ0Zvb1xcbj09PVxcbicpO1xuICogLy8gcmV0dXJucyB7J3RleHQnOiAnRm9vJywgJ2xldmVsJzogMX1cbiAqXG4gKiBAZXhhbXBsZVxuICogY29uc3Qgb3V0ID0gcGFyc2VIZWFkaW5nKCc8aDQ+Rm9vPC9oND5cXG4nKTtcbiAqIC8vIHJldHVybnMgeyd0ZXh0JzogJ0ZvbycsICdsZXZlbCc6IDR9XG4gKlxuICogQGV4YW1wbGVcbiAqIGNvbnN0IG91dCA9IHBhcnNlSGVhZGluZygnRm9vJyk7XG4gKiAvLyByZXR1cm5zIG51bGxcbiAqL1xuZnVuY3Rpb24gcGFyc2VIZWFkaW5nKGxpbmU6IHN0cmluZywgbmV4dExpbmU/OiBzdHJpbmcpOiBJSGVhZGVyIHwgbnVsbCB7XG4gIC8vIENhc2U6IE1hcmtkb3duIGhlYWRpbmdcbiAgbGV0IG1hdGNoID0gbGluZS5tYXRjaCgvXihbI117MSw2fSkgKC4qKS8pO1xuICBpZiAobWF0Y2gpIHtcbiAgICBpZiAoIXNraXBIZWFkaW5nLnRlc3QobWF0Y2hbMF0pKSB7XG4gICAgICByZXR1cm4ge1xuICAgICAgICB0ZXh0OiBjbGVhblRpdGxlKG1hdGNoWzJdKSxcbiAgICAgICAgbGV2ZWw6IG1hdGNoWzFdLmxlbmd0aCxcbiAgICAgICAgcmF3OiBsaW5lXG4gICAgICB9O1xuICAgIH1cbiAgfVxuICAvLyBDYXNlOiBNYXJrZG93biBoZWFkaW5nIChhbHRlcm5hdGl2ZSBzdHlsZSlcbiAgaWYgKG5leHRMaW5lKSB7XG4gICAgbWF0Y2ggPSBuZXh0TGluZS5tYXRjaCgvXiB7MCwzfShbPV17Mix9fFstXXsyLH0pXFxzKiQvKTtcbiAgICBpZiAobWF0Y2gpIHtcbiAgICAgIGlmICghc2tpcEhlYWRpbmcudGVzdChsaW5lKSkge1xuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgIHRleHQ6IGNsZWFuVGl0bGUobGluZSksXG4gICAgICAgICAgbGV2ZWw6IG1hdGNoWzFdWzBdID09PSAnPScgPyAxIDogMixcbiAgICAgICAgICByYXc6IFtsaW5lLCBuZXh0TGluZV0uam9pbignXFxuJylcbiAgICAgICAgfTtcbiAgICAgIH1cbiAgICB9XG4gIH1cbiAgLy8gQ2FzZTogSFRNTCBoZWFkaW5nIChXQVJOSU5HOiB0aGlzIGlzIG5vdCBwYXJ0aWN1bGFybHkgcm9idXN0LCBhcyBIVE1MIGhlYWRpbmdzIGNhbiBzcGFuIG11bHRpcGxlIGxpbmVzKVxuICBtYXRjaCA9IGxpbmUubWF0Y2goLzxoKFsxLTZdKS4qPiguKik8XFwvaFxcMT4vaSk7XG4gIGlmIChtYXRjaCkge1xuICAgIGlmICghc2tpcEhlYWRpbmcudGVzdChtYXRjaFswXSkpIHtcbiAgICAgIHJldHVybiB7XG4gICAgICAgIHRleHQ6IG1hdGNoWzJdLFxuICAgICAgICBsZXZlbDogcGFyc2VJbnQobWF0Y2hbMV0sIDEwKSxcbiAgICAgICAgcmF3OiBsaW5lXG4gICAgICB9O1xuICAgIH1cbiAgfVxuXG4gIHJldHVybiBudWxsO1xufVxuXG5mdW5jdGlvbiBjbGVhblRpdGxlKGhlYWRpbmc6IHN0cmluZyk6IHN0cmluZyB7XG4gIC8vIHRha2Ugc3BlY2lhbCBjYXJlIHRvIHBhcnNlIE1hcmtkb3duIGxpbmtzIGludG8gcmF3IHRleHRcbiAgcmV0dXJuIGhlYWRpbmcucmVwbGFjZSgvXFxbKC4rKVxcXVxcKC4rXFwpL2csICckMScpO1xufVxuXG4vKipcbiAqIElnbm9yZSB0aXRsZSB3aXRoIGh0bWwgdGFnIHdpdGggYSBjbGFzcyBuYW1lIGVxdWFsIHRvIGBqcC10b2MtaWdub3JlYCBvciBgdG9jU2tpcGBcbiAqL1xuY29uc3Qgc2tpcEhlYWRpbmcgPVxuICAvPFxcdytcXHMoLio/XFxzKT9jbGFzcz1cIiguKj9cXHMpPyhqcC10b2MtaWdub3JlfHRvY1NraXApKFxccy4qPyk/XCIoXFxzLio/KT8+LztcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==