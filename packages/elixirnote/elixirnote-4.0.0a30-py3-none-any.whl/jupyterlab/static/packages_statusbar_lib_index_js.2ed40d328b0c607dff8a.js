"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_statusbar_lib_index_js"],{

/***/ "../../packages/statusbar/lib/components/group.js":
/*!********************************************************!*\
  !*** ../../packages/statusbar/lib/components/group.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "GroupItem": () => (/* binding */ GroupItem)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var typestyle_lib__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! typestyle/lib */ "../../node_modules/typestyle/lib/index.js");
/* harmony import */ var _style_layout__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../style/layout */ "../../packages/statusbar/lib/style/layout.js");
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



const groupItemLayout = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_1__.style)(_style_layout__WEBPACK_IMPORTED_MODULE_2__.centeredFlex, _style_layout__WEBPACK_IMPORTED_MODULE_2__.leftToRight);
/**
 * A tsx component for a set of items logically grouped together.
 */
function GroupItem(props) {
    const { spacing, children, className } = props, rest = __rest(props, ["spacing", "children", "className"]);
    const numChildren = react__WEBPACK_IMPORTED_MODULE_0__.Children.count(children);
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", Object.assign({ className: (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_1__.classes)(groupItemLayout, className) }, rest), react__WEBPACK_IMPORTED_MODULE_0__.Children.map(children, (child, i) => {
        if (i === 0) {
            return react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { style: { marginRight: `${spacing}px` } }, child);
        }
        else if (i === numChildren - 1) {
            return react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { style: { marginLeft: `${spacing}px` } }, child);
        }
        else {
            return react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { style: { margin: `0px ${spacing}px` } }, child);
        }
    })));
}


/***/ }),

/***/ "../../packages/statusbar/lib/components/hover.js":
/*!********************************************************!*\
  !*** ../../packages/statusbar/lib/components/hover.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Popup": () => (/* binding */ Popup),
/* harmony export */   "showPopup": () => (/* binding */ showPopup)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _style_statusbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../style/statusbar */ "../../packages/statusbar/lib/style/statusbar.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Create and show a popup component.
 *
 * @param options - options for the popup
 *
 * @returns the popup that was created.
 */
function showPopup(options) {
    const dialog = new Popup(options);
    dialog.launch();
    return dialog;
}
/**
 * A class for a Popup widget.
 */
class Popup extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget {
    /**
     * Construct a new Popup.
     */
    constructor(options) {
        super();
        this._body = options.body;
        this._body.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_2__.hoverItem);
        this._anchor = options.anchor;
        this._align = options.align;
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.PanelLayout());
        layout.addWidget(options.body);
        this._body.node.addEventListener('resize', () => {
            this.update();
        });
    }
    /**
     * Attach the popup widget to the page.
     */
    launch() {
        this._setGeometry();
        _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget.attach(this, document.body);
        this.update();
        this._anchor.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_2__.clickedItem);
        this._anchor.removeClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_2__.interactiveItem);
    }
    /**
     * Handle `'update'` messages for the widget.
     */
    onUpdateRequest(msg) {
        this._setGeometry();
        super.onUpdateRequest(msg);
    }
    /**
     * Handle `'after-attach'` messages for the widget.
     */
    onAfterAttach(msg) {
        document.addEventListener('click', this, false);
        this.node.addEventListener('keydown', this, false);
        window.addEventListener('resize', this, false);
    }
    /**
     * Handle `'after-detach'` messages for the widget.
     */
    onAfterDetach(msg) {
        document.removeEventListener('click', this, false);
        this.node.removeEventListener('keydown', this, false);
        window.removeEventListener('resize', this, false);
    }
    /**
     * Handle `'resize'` messages for the widget.
     */
    onResize() {
        this.update();
    }
    /**
     * Dispose of the widget.
     */
    dispose() {
        super.dispose();
        this._anchor.removeClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_2__.clickedItem);
        this._anchor.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_2__.interactiveItem);
    }
    /**
     * Handle DOM events for the widget.
     */
    handleEvent(event) {
        switch (event.type) {
            case 'keydown':
                this._evtKeydown(event);
                break;
            case 'click':
                this._evtClick(event);
                break;
            case 'resize':
                this.onResize();
                break;
            default:
                break;
        }
    }
    _evtClick(event) {
        if (!!event.target &&
            !(this._body.node.contains(event.target) ||
                this._anchor.node.contains(event.target))) {
            this.dispose();
        }
    }
    _evtKeydown(event) {
        // Check for escape key
        switch (event.keyCode) {
            case 27: // Escape.
                event.stopPropagation();
                event.preventDefault();
                this.dispose();
                break;
            default:
                break;
        }
    }
    _setGeometry() {
        let aligned = 0;
        const anchorRect = this._anchor.node.getBoundingClientRect();
        const bodyRect = this._body.node.getBoundingClientRect();
        if (this._align === 'right') {
            aligned = -(bodyRect.width - anchorRect.width);
        }
        const style = window.getComputedStyle(this._body.node);
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.HoverBox.setGeometry({
            anchor: anchorRect,
            host: document.body,
            maxHeight: 500,
            minHeight: 20,
            node: this._body.node,
            offset: {
                horizontal: aligned
            },
            privilege: 'forceAbove',
            style
        });
    }
}


/***/ }),

/***/ "../../packages/statusbar/lib/components/index.js":
/*!********************************************************!*\
  !*** ../../packages/statusbar/lib/components/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "GroupItem": () => (/* reexport safe */ _group__WEBPACK_IMPORTED_MODULE_0__.GroupItem),
/* harmony export */   "Popup": () => (/* reexport safe */ _hover__WEBPACK_IMPORTED_MODULE_1__.Popup),
/* harmony export */   "ProgressBar": () => (/* reexport safe */ _progressBar__WEBPACK_IMPORTED_MODULE_2__.ProgressBar),
/* harmony export */   "ProgressCircle": () => (/* reexport safe */ _progressCircle__WEBPACK_IMPORTED_MODULE_4__.ProgressCircle),
/* harmony export */   "TextItem": () => (/* reexport safe */ _text__WEBPACK_IMPORTED_MODULE_3__.TextItem),
/* harmony export */   "showPopup": () => (/* reexport safe */ _hover__WEBPACK_IMPORTED_MODULE_1__.showPopup)
/* harmony export */ });
/* harmony import */ var _group__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./group */ "../../packages/statusbar/lib/components/group.js");
/* harmony import */ var _hover__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./hover */ "../../packages/statusbar/lib/components/hover.js");
/* harmony import */ var _progressBar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./progressBar */ "../../packages/statusbar/lib/components/progressBar.js");
/* harmony import */ var _text__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./text */ "../../packages/statusbar/lib/components/text.js");
/* harmony import */ var _progressCircle__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./progressCircle */ "../../packages/statusbar/lib/components/progressCircle.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.







/***/ }),

/***/ "../../packages/statusbar/lib/components/progressBar.js":
/*!**************************************************************!*\
  !*** ../../packages/statusbar/lib/components/progressBar.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ProgressBar": () => (/* binding */ ProgressBar)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
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

/**
 * A functional tsx component for a progress bar.
 */
function ProgressBar(props) {
    const { width, percentage } = props, rest = __rest(props, ["width", "percentage"]);
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: 'jp-Statusbar-ProgressBar-progress-bar', role: "progressbar", "aria-valuemin": 0, "aria-valuemax": 100, "aria-valuenow": percentage },
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(Filler, Object.assign({}, Object.assign({ percentage }, rest), { contentWidth: width }))));
}
/**
 * A functional tsx component for a partially filled div.
 */
function Filler(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { style: {
            width: `${props.percentage}%`
        } },
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("p", null, props.content)));
}


/***/ }),

/***/ "../../packages/statusbar/lib/components/progressCircle.js":
/*!*****************************************************************!*\
  !*** ../../packages/statusbar/lib/components/progressCircle.js ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ProgressCircle": () => (/* binding */ ProgressCircle)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

function ProgressCircle(props) {
    const radius = 104;
    const d = (progress) => {
        const angle = Math.max(progress * 3.6, 0.1);
        const rad = (angle * Math.PI) / 180, x = Math.sin(rad) * radius, y = Math.cos(rad) * -radius, mid = angle < 180 ? 1 : 0, shape = `M 0 0 v -${radius} A ${radius} ${radius} 1 ` +
            mid +
            ' 0 ' +
            x.toFixed(4) +
            ' ' +
            y.toFixed(4) +
            ' z';
        return shape;
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-Statusbar-ProgressCircle', role: "progressbar", "aria-valuemin": 0, "aria-valuemax": 100, "aria-valuenow": props.progress },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("svg", { viewBox: "0 0 250 250" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("circle", { cx: "125", cy: "125", r: `${radius}`, stroke: "var(--jp-inverse-layout-color3)", strokeWidth: "20", fill: "none" }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("path", { transform: "translate(125,125) scale(.9)", d: d(props.progress), fill: 'var(--jp-inverse-layout-color3)' }))));
}


/***/ }),

/***/ "../../packages/statusbar/lib/components/text.js":
/*!*******************************************************!*\
  !*** ../../packages/statusbar/lib/components/text.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TextItem": () => (/* binding */ TextItem)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var typestyle_lib__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! typestyle/lib */ "../../node_modules/typestyle/lib/index.js");
/* harmony import */ var _style_text__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../style/text */ "../../packages/statusbar/lib/style/text.js");
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



/**
 * A functional tsx component for a text item.
 */
function TextItem(props) {
    const { title, source, className } = props, rest = __rest(props, ["title", "source", "className"]);
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("span", Object.assign({ className: (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_1__.classes)(_style_text__WEBPACK_IMPORTED_MODULE_2__.textItem, className), title: title }, rest), source));
}


/***/ }),

/***/ "../../packages/statusbar/lib/index.js":
/*!*********************************************!*\
  !*** ../../packages/statusbar/lib/index.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "GroupItem": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.GroupItem),
/* harmony export */   "IStatusBar": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_3__.IStatusBar),
/* harmony export */   "Popup": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.Popup),
/* harmony export */   "ProgressBar": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.ProgressBar),
/* harmony export */   "ProgressCircle": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.ProgressCircle),
/* harmony export */   "StatusBar": () => (/* reexport safe */ _statusbar__WEBPACK_IMPORTED_MODULE_1__.StatusBar),
/* harmony export */   "TextItem": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.TextItem),
/* harmony export */   "clickedItem": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.clickedItem),
/* harmony export */   "hoverItem": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.hoverItem),
/* harmony export */   "interactiveItem": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.interactiveItem),
/* harmony export */   "item": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.item),
/* harmony export */   "leftSide": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.leftSide),
/* harmony export */   "rightSide": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.rightSide),
/* harmony export */   "showPopup": () => (/* reexport safe */ _components__WEBPACK_IMPORTED_MODULE_0__.showPopup),
/* harmony export */   "side": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.side),
/* harmony export */   "statusBar": () => (/* reexport safe */ _style_statusbar__WEBPACK_IMPORTED_MODULE_2__.statusBar)
/* harmony export */ });
/* harmony import */ var _components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./components */ "../../packages/statusbar/lib/components/index.js");
/* harmony import */ var _statusbar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./statusbar */ "../../packages/statusbar/lib/statusbar.js");
/* harmony import */ var _style_statusbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./style/statusbar */ "../../packages/statusbar/lib/style/statusbar.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./tokens */ "../../packages/statusbar/lib/tokens.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module statusbar
 */






/***/ }),

/***/ "../../packages/statusbar/lib/statusbar.js":
/*!*************************************************!*\
  !*** ../../packages/statusbar/lib/statusbar.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "StatusBar": () => (/* binding */ StatusBar)
/* harmony export */ });
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _style_statusbar__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./style/statusbar */ "../../packages/statusbar/lib/style/statusbar.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * Main status bar object which contains all items.
 */
class StatusBar extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    constructor() {
        super();
        this._leftRankItems = [];
        this._rightRankItems = [];
        this._statusItems = {};
        this._disposables = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableSet();
        this.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.statusBar);
        const rootLayout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.PanelLayout());
        const leftPanel = (this._leftSide = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Panel());
        const middlePanel = (this._middlePanel = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Panel());
        const rightPanel = (this._rightSide = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Panel());
        leftPanel.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.side);
        leftPanel.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.leftSide);
        middlePanel.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.side);
        rightPanel.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.side);
        rightPanel.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.rightSide);
        rootLayout.addWidget(leftPanel);
        rootLayout.addWidget(middlePanel);
        rootLayout.addWidget(rightPanel);
    }
    /**
     * Register a new status item.
     *
     * @param id - a unique id for the status item.
     *
     * @param statusItem - The item to add to the status bar.
     */
    registerStatusItem(id, statusItem) {
        if (id in this._statusItems) {
            throw new Error(`Status item ${id} already registered.`);
        }
        // Populate defaults for the optional properties of the status item.
        const fullStatusItem = Object.assign(Object.assign({}, Private.statusItemDefaults), statusItem);
        const { align, item, rank } = fullStatusItem;
        // Connect the activeStateChanged signal to refreshing the status item,
        // if the signal was provided.
        const onActiveStateChanged = () => {
            this._refreshItem(id);
        };
        if (fullStatusItem.activeStateChanged) {
            fullStatusItem.activeStateChanged.connect(onActiveStateChanged);
        }
        const rankItem = { id, rank };
        fullStatusItem.item.addClass(_style_statusbar__WEBPACK_IMPORTED_MODULE_3__.item);
        this._statusItems[id] = fullStatusItem;
        if (align === 'left') {
            const insertIndex = this._findInsertIndex(this._leftRankItems, rankItem);
            if (insertIndex === -1) {
                this._leftSide.addWidget(item);
                this._leftRankItems.push(rankItem);
            }
            else {
                _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.insert(this._leftRankItems, insertIndex, rankItem);
                this._leftSide.insertWidget(insertIndex, item);
            }
        }
        else if (align === 'right') {
            const insertIndex = this._findInsertIndex(this._rightRankItems, rankItem);
            if (insertIndex === -1) {
                this._rightSide.addWidget(item);
                this._rightRankItems.push(rankItem);
            }
            else {
                _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.insert(this._rightRankItems, insertIndex, rankItem);
                this._rightSide.insertWidget(insertIndex, item);
            }
        }
        else {
            this._middlePanel.addWidget(item);
        }
        this._refreshItem(id); // Initially refresh the status item.
        const disposable = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            delete this._statusItems[id];
            if (fullStatusItem.activeStateChanged) {
                fullStatusItem.activeStateChanged.disconnect(onActiveStateChanged);
            }
            item.parent = null;
            item.dispose();
        });
        this._disposables.add(disposable);
        return disposable;
    }
    /**
     * Dispose of the status bar.
     */
    dispose() {
        this._leftRankItems.length = 0;
        this._rightRankItems.length = 0;
        this._disposables.dispose();
        super.dispose();
    }
    /**
     * Handle an 'update-request' message to the status bar.
     */
    onUpdateRequest(msg) {
        this._refreshAll();
        super.onUpdateRequest(msg);
    }
    _findInsertIndex(side, newItem) {
        return _lumino_algorithm__WEBPACK_IMPORTED_MODULE_0__.ArrayExt.findFirstIndex(side, item => item.rank > newItem.rank);
    }
    _refreshItem(id) {
        const statusItem = this._statusItems[id];
        if (statusItem.isActive()) {
            statusItem.item.show();
            statusItem.item.update();
        }
        else {
            statusItem.item.hide();
        }
    }
    _refreshAll() {
        Object.keys(this._statusItems).forEach(id => {
            this._refreshItem(id);
        });
    }
}
/**
 * A namespace for private functionality.
 */
var Private;
(function (Private) {
    /**
     * Default options for a status item, less the item itself.
     */
    Private.statusItemDefaults = {
        align: 'left',
        rank: 0,
        isActive: () => true,
        activeStateChanged: undefined
    };
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/statusbar/lib/style/layout.js":
/*!****************************************************!*\
  !*** ../../packages/statusbar/lib/style/layout.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "centeredFlex": () => (/* binding */ centeredFlex),
/* harmony export */   "equiDistant": () => (/* binding */ equiDistant),
/* harmony export */   "leftToRight": () => (/* binding */ leftToRight),
/* harmony export */   "rightToLeft": () => (/* binding */ rightToLeft)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
const centeredFlex = {
    display: 'flex',
    alignItems: 'center'
};
const leftToRight = {
    flexDirection: 'row'
};
const rightToLeft = {
    flexDirection: 'row-reverse'
};
const equiDistant = {
    justifyContent: 'space-between'
};


/***/ }),

/***/ "../../packages/statusbar/lib/style/statusbar.js":
/*!*******************************************************!*\
  !*** ../../packages/statusbar/lib/style/statusbar.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "clickedItem": () => (/* binding */ clickedItem),
/* harmony export */   "hoverItem": () => (/* binding */ hoverItem),
/* harmony export */   "interactiveItem": () => (/* binding */ interactiveItem),
/* harmony export */   "item": () => (/* binding */ item),
/* harmony export */   "leftSide": () => (/* binding */ leftSide),
/* harmony export */   "rightSide": () => (/* binding */ rightSide),
/* harmony export */   "side": () => (/* binding */ side),
/* harmony export */   "statusBar": () => (/* binding */ statusBar)
/* harmony export */ });
/* harmony import */ var typestyle_lib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! typestyle/lib */ "../../node_modules/typestyle/lib/index.js");
/* harmony import */ var _layout__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./layout */ "../../packages/statusbar/lib/style/layout.js");
/* harmony import */ var _text__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./text */ "../../packages/statusbar/lib/style/text.js");
/* harmony import */ var _variables__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./variables */ "../../packages/statusbar/lib/style/variables.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




const itemPadding = {
    paddingLeft: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].itemPadding,
    paddingRight: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].itemPadding
};
const interactiveHover = {
    $nest: {
        '&:hover': {
            backgroundColor: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].hoverColor
        }
    }
};
const clicked = {
    backgroundColor: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].clickColor,
    $nest: {
        ['.' + _text__WEBPACK_IMPORTED_MODULE_2__.textItem]: {
            color: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].textClickColor
        }
    }
};
const statusBar = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)({
    background: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].backgroundColor,
    minHeight: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].height,
    justifyContent: 'space-between',
    paddingLeft: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].statusBarPadding,
    paddingRight: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].statusBarPadding
}, _layout__WEBPACK_IMPORTED_MODULE_1__.centeredFlex);
const side = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(_layout__WEBPACK_IMPORTED_MODULE_1__.centeredFlex);
const leftSide = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(_layout__WEBPACK_IMPORTED_MODULE_1__.leftToRight);
const rightSide = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(_layout__WEBPACK_IMPORTED_MODULE_1__.rightToLeft);
const item = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)({
    maxHeight: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].height,
    marginLeft: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].itemMargin,
    marginRight: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].itemMargin,
    height: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].height,
    whiteSpace: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].whiteSpace,
    textOverflow: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].textOverflow,
    color: _variables__WEBPACK_IMPORTED_MODULE_3__["default"].textColor
}, itemPadding);
const clickedItem = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(clicked);
const interactiveItem = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(interactiveHover);
const hoverItem = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)({
    boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)'
});


/***/ }),

/***/ "../../packages/statusbar/lib/style/text.js":
/*!**************************************************!*\
  !*** ../../packages/statusbar/lib/style/text.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "baseText": () => (/* binding */ baseText),
/* harmony export */   "textItem": () => (/* binding */ textItem)
/* harmony export */ });
/* harmony import */ var typestyle_lib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! typestyle/lib */ "../../node_modules/typestyle/lib/index.js");
/* harmony import */ var _variables__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./variables */ "../../packages/statusbar/lib/style/variables.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


const baseText = {
    fontSize: _variables__WEBPACK_IMPORTED_MODULE_1__["default"].fontSize,
    fontFamily: _variables__WEBPACK_IMPORTED_MODULE_1__["default"].fontFamily
};
const textItem = (0,typestyle_lib__WEBPACK_IMPORTED_MODULE_0__.style)(baseText, {
    lineHeight: '24px',
    color: _variables__WEBPACK_IMPORTED_MODULE_1__["default"].textColor
});


/***/ }),

/***/ "../../packages/statusbar/lib/style/variables.js":
/*!*******************************************************!*\
  !*** ../../packages/statusbar/lib/style/variables.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ({
    hoverColor: 'var(--jp-layout-color3)',
    clickColor: 'var(--jp-brand-color1)',
    backgroundColor: 'var(--jp-layout-color2)',
    height: 'var(--jp-statusbar-height)',
    fontSize: 'var(--jp-ui-font-size1)',
    fontFamily: 'var(--jp-ui-font-family)',
    textColor: 'var(--jp-ui-font-color1)',
    textClickColor: 'white',
    itemMargin: '2px',
    itemPadding: '6px',
    statusBarPadding: '10px',
    interItemHalfSpacing: '2px',
    whiteSpace: 'nowrap',
    textOverflow: 'ellipsis'
});


/***/ }),

/***/ "../../packages/statusbar/lib/tokens.js":
/*!**********************************************!*\
  !*** ../../packages/statusbar/lib/tokens.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IStatusBar": () => (/* binding */ IStatusBar)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// tslint:disable-next-line:variable-name
const IStatusBar = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/statusbar:IStatusBar');


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfc3RhdHVzYmFyX2xpYl9pbmRleF9qcy4yZWQ0MGQzMjhiMGM2MDdkZmY4YS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7Ozs7Ozs7Ozs7OztBQUU1QjtBQUNnQjtBQUNhO0FBRTVELE1BQU0sZUFBZSxHQUFHLG9EQUFLLENBQUMsdURBQVksRUFBRSxzREFBVyxDQUFDLENBQUM7QUFFekQ7O0dBRUc7QUFDSSxTQUFTLFNBQVMsQ0FDdkIsS0FBOEQ7SUFFOUQsTUFBTSxFQUFFLE9BQU8sRUFBRSxRQUFRLEVBQUUsU0FBUyxLQUFjLEtBQUssRUFBZCxJQUFJLFVBQUssS0FBSyxFQUFqRCxvQ0FBeUMsQ0FBUSxDQUFDO0lBQ3hELE1BQU0sV0FBVyxHQUFHLGlEQUFvQixDQUFDLFFBQVEsQ0FBQyxDQUFDO0lBRW5ELE9BQU8sQ0FDTCx3RUFBSyxTQUFTLEVBQUUsc0RBQU8sQ0FBQyxlQUFlLEVBQUUsU0FBUyxDQUFDLElBQU0sSUFBSSxHQUMxRCwrQ0FBa0IsQ0FBQyxRQUFRLEVBQUUsQ0FBQyxLQUFLLEVBQUUsQ0FBQyxFQUFFLEVBQUU7UUFDekMsSUFBSSxDQUFDLEtBQUssQ0FBQyxFQUFFO1lBQ1gsT0FBTywwREFBSyxLQUFLLEVBQUUsRUFBRSxXQUFXLEVBQUUsR0FBRyxPQUFPLElBQUksRUFBRSxJQUFHLEtBQUssQ0FBTyxDQUFDO1NBQ25FO2FBQU0sSUFBSSxDQUFDLEtBQUssV0FBVyxHQUFHLENBQUMsRUFBRTtZQUNoQyxPQUFPLDBEQUFLLEtBQUssRUFBRSxFQUFFLFVBQVUsRUFBRSxHQUFHLE9BQU8sSUFBSSxFQUFFLElBQUcsS0FBSyxDQUFPLENBQUM7U0FDbEU7YUFBTTtZQUNMLE9BQU8sMERBQUssS0FBSyxFQUFFLEVBQUUsTUFBTSxFQUFFLE9BQU8sT0FBTyxJQUFJLEVBQUUsSUFBRyxLQUFLLENBQU8sQ0FBQztTQUNsRTtJQUNILENBQUMsQ0FBQyxDQUNFLENBQ1AsQ0FBQztB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QUFRLEVBQUU7SUFDdEMsVUFBVSxFQUFFLE1BQU07SUFDbEIsS0FBSyxFQUFFLDREQUFjO0NBQ3RCLENBQUMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7O0FDWEgsaUVBQWU7SUFDYixVQUFVLEVBQUUseUJBQXlCO0lBQ3JDLFVBQVUsRUFBRSx3QkFBd0I7SUFDcEMsZUFBZSxFQUFFLHlCQUF5QjtJQUMxQyxNQUFNLEVBQUUsNEJBQTRCO0lBQ3BDLFFBQVEsRUFBRSx5QkFBeUI7SUFDbkMsVUFBVSxFQUFFLDBCQUEwQjtJQUN0QyxTQUFTLEVBQUUsMEJBQTBCO0lBQ3JDLGNBQWMsRUFBRSxPQUFPO0lBQ3ZCLFVBQVUsRUFBRSxLQUFLO0lBQ2pCLFdBQVcsRUFBRSxLQUFLO0lBQ2xCLGdCQUFnQixFQUFFLE1BQU07SUFDeEIsb0JBQW9CLEVBQUUsS0FBSztJQUMzQixVQUFVLEVBQUUsUUFBK0I7SUFDM0MsWUFBWSxFQUFFLFVBQVU7Q0FDekIsRUFBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNuQkYsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVqQjtBQUsxQyx5Q0FBeUM7QUFDbEMsTUFBTSxVQUFVLEdBQUcsSUFBSSxvREFBSyxDQUNqQyxrQ0FBa0MsQ0FDbkMsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zdGF0dXNiYXIvc3JjL2NvbXBvbmVudHMvZ3JvdXAudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zdGF0dXNiYXIvc3JjL2NvbXBvbmVudHMvaG92ZXIudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zdGF0dXNiYXIvc3JjL2NvbXBvbmVudHMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3N0YXR1c2Jhci9zcmMvY29tcG9uZW50cy9wcm9ncmVzc0Jhci50c3giLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3N0YXR1c2Jhci9zcmMvY29tcG9uZW50cy9wcm9ncmVzc0NpcmNsZS50c3giLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3N0YXR1c2Jhci9zcmMvY29tcG9uZW50cy90ZXh0LnRzeCIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc3RhdHVzYmFyL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc3RhdHVzYmFyL3NyYy9zdGF0dXNiYXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3N0YXR1c2Jhci9zcmMvc3R5bGUvbGF5b3V0LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zdGF0dXNiYXIvc3JjL3N0eWxlL3N0YXR1c2Jhci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc3RhdHVzYmFyL3NyYy9zdHlsZS90ZXh0LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zdGF0dXNiYXIvc3JjL3N0eWxlL3ZhcmlhYmxlcy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc3RhdHVzYmFyL3NyYy90b2tlbnMudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgeyBjbGFzc2VzLCBzdHlsZSB9IGZyb20gJ3R5cGVzdHlsZS9saWInO1xuaW1wb3J0IHsgY2VudGVyZWRGbGV4LCBsZWZ0VG9SaWdodCB9IGZyb20gJy4uL3N0eWxlL2xheW91dCc7XG5cbmNvbnN0IGdyb3VwSXRlbUxheW91dCA9IHN0eWxlKGNlbnRlcmVkRmxleCwgbGVmdFRvUmlnaHQpO1xuXG4vKipcbiAqIEEgdHN4IGNvbXBvbmVudCBmb3IgYSBzZXQgb2YgaXRlbXMgbG9naWNhbGx5IGdyb3VwZWQgdG9nZXRoZXIuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBHcm91cEl0ZW0oXG4gIHByb3BzOiBHcm91cEl0ZW0uSVByb3BzICYgUmVhY3QuSFRNTEF0dHJpYnV0ZXM8SFRNTERpdkVsZW1lbnQ+XG4pOiBSZWFjdC5SZWFjdEVsZW1lbnQ8R3JvdXBJdGVtLklQcm9wcz4ge1xuICBjb25zdCB7IHNwYWNpbmcsIGNoaWxkcmVuLCBjbGFzc05hbWUsIC4uLnJlc3QgfSA9IHByb3BzO1xuICBjb25zdCBudW1DaGlsZHJlbiA9IFJlYWN0LkNoaWxkcmVuLmNvdW50KGNoaWxkcmVuKTtcblxuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPXtjbGFzc2VzKGdyb3VwSXRlbUxheW91dCwgY2xhc3NOYW1lKX0gey4uLnJlc3R9PlxuICAgICAge1JlYWN0LkNoaWxkcmVuLm1hcChjaGlsZHJlbiwgKGNoaWxkLCBpKSA9PiB7XG4gICAgICAgIGlmIChpID09PSAwKSB7XG4gICAgICAgICAgcmV0dXJuIDxkaXYgc3R5bGU9e3sgbWFyZ2luUmlnaHQ6IGAke3NwYWNpbmd9cHhgIH19PntjaGlsZH08L2Rpdj47XG4gICAgICAgIH0gZWxzZSBpZiAoaSA9PT0gbnVtQ2hpbGRyZW4gLSAxKSB7XG4gICAgICAgICAgcmV0dXJuIDxkaXYgc3R5bGU9e3sgbWFyZ2luTGVmdDogYCR7c3BhY2luZ31weGAgfX0+e2NoaWxkfTwvZGl2PjtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICByZXR1cm4gPGRpdiBzdHlsZT17eyBtYXJnaW46IGAwcHggJHtzcGFjaW5nfXB4YCB9fT57Y2hpbGR9PC9kaXY+O1xuICAgICAgICB9XG4gICAgICB9KX1cbiAgICA8L2Rpdj5cbiAgKTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgR3JvdXBJdGVtIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgR3JvdXBJdGVtIHtcbiAgLyoqXG4gICAqIFByb3BzIGZvciB0aGUgR3JvdXBJdGVtLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBzcGFjaW5nLCBpbiBweCwgYmV0d2VlbiB0aGUgaXRlbXMgaW4gdGhlIGdyb3VwLlxuICAgICAqL1xuICAgIHNwYWNpbmc6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBpdGVtcyB0byBhcnJhbmdlIGluIGEgZ3JvdXAuXG4gICAgICovXG4gICAgY2hpbGRyZW46IEpTWC5FbGVtZW50W107XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSG92ZXJCb3ggfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBQYW5lbExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IGNsaWNrZWRJdGVtLCBob3Zlckl0ZW0sIGludGVyYWN0aXZlSXRlbSB9IGZyb20gJy4uL3N0eWxlL3N0YXR1c2Jhcic7XG5cbi8qKlxuICogQ3JlYXRlIGFuZCBzaG93IGEgcG9wdXAgY29tcG9uZW50LlxuICpcbiAqIEBwYXJhbSBvcHRpb25zIC0gb3B0aW9ucyBmb3IgdGhlIHBvcHVwXG4gKlxuICogQHJldHVybnMgdGhlIHBvcHVwIHRoYXQgd2FzIGNyZWF0ZWQuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBzaG93UG9wdXAob3B0aW9uczogUG9wdXAuSU9wdGlvbnMpOiBQb3B1cCB7XG4gIGNvbnN0IGRpYWxvZyA9IG5ldyBQb3B1cChvcHRpb25zKTtcbiAgZGlhbG9nLmxhdW5jaCgpO1xuICByZXR1cm4gZGlhbG9nO1xufVxuXG4vKipcbiAqIEEgY2xhc3MgZm9yIGEgUG9wdXAgd2lkZ2V0LlxuICovXG5leHBvcnQgY2xhc3MgUG9wdXAgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IFBvcHVwLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogUG9wdXAuSU9wdGlvbnMpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX2JvZHkgPSBvcHRpb25zLmJvZHk7XG4gICAgdGhpcy5fYm9keS5hZGRDbGFzcyhob3Zlckl0ZW0pO1xuICAgIHRoaXMuX2FuY2hvciA9IG9wdGlvbnMuYW5jaG9yO1xuICAgIHRoaXMuX2FsaWduID0gb3B0aW9ucy5hbGlnbjtcbiAgICBjb25zdCBsYXlvdXQgPSAodGhpcy5sYXlvdXQgPSBuZXcgUGFuZWxMYXlvdXQoKSk7XG4gICAgbGF5b3V0LmFkZFdpZGdldChvcHRpb25zLmJvZHkpO1xuICAgIHRoaXMuX2JvZHkubm9kZS5hZGRFdmVudExpc3RlbmVyKCdyZXNpemUnLCAoKSA9PiB7XG4gICAgICB0aGlzLnVwZGF0ZSgpO1xuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEF0dGFjaCB0aGUgcG9wdXAgd2lkZ2V0IHRvIHRoZSBwYWdlLlxuICAgKi9cbiAgbGF1bmNoKCk6IHZvaWQge1xuICAgIHRoaXMuX3NldEdlb21ldHJ5KCk7XG4gICAgV2lkZ2V0LmF0dGFjaCh0aGlzLCBkb2N1bWVudC5ib2R5KTtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICAgIHRoaXMuX2FuY2hvci5hZGRDbGFzcyhjbGlja2VkSXRlbSk7XG4gICAgdGhpcy5fYW5jaG9yLnJlbW92ZUNsYXNzKGludGVyYWN0aXZlSXRlbSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAndXBkYXRlJ2AgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX3NldEdlb21ldHJ5KCk7XG4gICAgc3VwZXIub25VcGRhdGVSZXF1ZXN0KG1zZyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnYWZ0ZXItYXR0YWNoJ2AgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25BZnRlckF0dGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIHRoaXMsIGZhbHNlKTtcbiAgICB0aGlzLm5vZGUuYWRkRXZlbnRMaXN0ZW5lcigna2V5ZG93bicsIHRoaXMsIGZhbHNlKTtcbiAgICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcigncmVzaXplJywgdGhpcywgZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgJ2FmdGVyLWRldGFjaCdgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWZ0ZXJEZXRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgZG9jdW1lbnQucmVtb3ZlRXZlbnRMaXN0ZW5lcignY2xpY2snLCB0aGlzLCBmYWxzZSk7XG4gICAgdGhpcy5ub2RlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2tleWRvd24nLCB0aGlzLCBmYWxzZSk7XG4gICAgd2luZG93LnJlbW92ZUV2ZW50TGlzdGVuZXIoJ3Jlc2l6ZScsIHRoaXMsIGZhbHNlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYCdyZXNpemUnYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIHByb3RlY3RlZCBvblJlc2l6ZSgpOiB2b2lkIHtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHdpZGdldC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICAgIHRoaXMuX2FuY2hvci5yZW1vdmVDbGFzcyhjbGlja2VkSXRlbSk7XG4gICAgdGhpcy5fYW5jaG9yLmFkZENsYXNzKGludGVyYWN0aXZlSXRlbSk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBoYW5kbGVFdmVudChldmVudDogRXZlbnQpOiB2b2lkIHtcbiAgICBzd2l0Y2ggKGV2ZW50LnR5cGUpIHtcbiAgICAgIGNhc2UgJ2tleWRvd24nOlxuICAgICAgICB0aGlzLl9ldnRLZXlkb3duKGV2ZW50IGFzIEtleWJvYXJkRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2NsaWNrJzpcbiAgICAgICAgdGhpcy5fZXZ0Q2xpY2soZXZlbnQgYXMgTW91c2VFdmVudCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAncmVzaXplJzpcbiAgICAgICAgdGhpcy5vblJlc2l6ZSgpO1xuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX2V2dENsaWNrKGV2ZW50OiBNb3VzZUV2ZW50KTogdm9pZCB7XG4gICAgaWYgKFxuICAgICAgISFldmVudC50YXJnZXQgJiZcbiAgICAgICEoXG4gICAgICAgIHRoaXMuX2JvZHkubm9kZS5jb250YWlucyhldmVudC50YXJnZXQgYXMgSFRNTEVsZW1lbnQpIHx8XG4gICAgICAgIHRoaXMuX2FuY2hvci5ub2RlLmNvbnRhaW5zKGV2ZW50LnRhcmdldCBhcyBIVE1MRWxlbWVudClcbiAgICAgIClcbiAgICApIHtcbiAgICAgIHRoaXMuZGlzcG9zZSgpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX2V2dEtleWRvd24oZXZlbnQ6IEtleWJvYXJkRXZlbnQpOiB2b2lkIHtcbiAgICAvLyBDaGVjayBmb3IgZXNjYXBlIGtleVxuICAgIHN3aXRjaCAoZXZlbnQua2V5Q29kZSkge1xuICAgICAgY2FzZSAyNzogLy8gRXNjYXBlLlxuICAgICAgICBldmVudC5zdG9wUHJvcGFnYXRpb24oKTtcbiAgICAgICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICAgICAgdGhpcy5kaXNwb3NlKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfc2V0R2VvbWV0cnkoKTogdm9pZCB7XG4gICAgbGV0IGFsaWduZWQgPSAwO1xuICAgIGNvbnN0IGFuY2hvclJlY3QgPSB0aGlzLl9hbmNob3Iubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICBjb25zdCBib2R5UmVjdCA9IHRoaXMuX2JvZHkubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICBpZiAodGhpcy5fYWxpZ24gPT09ICdyaWdodCcpIHtcbiAgICAgIGFsaWduZWQgPSAtKGJvZHlSZWN0LndpZHRoIC0gYW5jaG9yUmVjdC53aWR0aCk7XG4gICAgfVxuICAgIGNvbnN0IHN0eWxlID0gd2luZG93LmdldENvbXB1dGVkU3R5bGUodGhpcy5fYm9keS5ub2RlKTtcbiAgICBIb3ZlckJveC5zZXRHZW9tZXRyeSh7XG4gICAgICBhbmNob3I6IGFuY2hvclJlY3QsXG4gICAgICBob3N0OiBkb2N1bWVudC5ib2R5LFxuICAgICAgbWF4SGVpZ2h0OiA1MDAsXG4gICAgICBtaW5IZWlnaHQ6IDIwLFxuICAgICAgbm9kZTogdGhpcy5fYm9keS5ub2RlLFxuICAgICAgb2Zmc2V0OiB7XG4gICAgICAgIGhvcml6b250YWw6IGFsaWduZWRcbiAgICAgIH0sXG4gICAgICBwcml2aWxlZ2U6ICdmb3JjZUFib3ZlJyxcbiAgICAgIHN0eWxlXG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIF9ib2R5OiBXaWRnZXQ7XG4gIHByaXZhdGUgX2FuY2hvcjogV2lkZ2V0O1xuICBwcml2YXRlIF9hbGlnbjogJ2xlZnQnIHwgJ3JpZ2h0JyB8IHVuZGVmaW5lZDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgUG9wdXAgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBQb3B1cCB7XG4gIC8qKlxuICAgKiBPcHRpb25zIGZvciBjcmVhdGluZyBhIFBvcHVwIHdpZGdldC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBjb250ZW50IG9mIHRoZSBwb3B1cC5cbiAgICAgKi9cbiAgICBib2R5OiBXaWRnZXQ7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgd2lkZ2V0IHRvIHdoaWNoIHdlIGFyZSBhdHRhY2hpbmcgdGhlIHBvcHVwLlxuICAgICAqL1xuICAgIGFuY2hvcjogV2lkZ2V0O1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0byBhbGlnbiB0aGUgcG9wdXAgdG8gdGhlIGxlZnQgb3IgdGhlIHJpZ2h0IG9mIHRoZSBhbmNob3IuXG4gICAgICovXG4gICAgYWxpZ24/OiAnbGVmdCcgfCAncmlnaHQnO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmV4cG9ydCAqIGZyb20gJy4vZ3JvdXAnO1xuZXhwb3J0ICogZnJvbSAnLi9ob3Zlcic7XG5leHBvcnQgKiBmcm9tICcuL3Byb2dyZXNzQmFyJztcbmV4cG9ydCAqIGZyb20gJy4vdGV4dCc7XG5leHBvcnQgKiBmcm9tICcuL3Byb2dyZXNzQ2lyY2xlJztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBQcm9ncmVzc0JhciBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIFByb2dyZXNzQmFyIHtcbiAgLyoqXG4gICAqIFByb3BzIGZvciB0aGUgUHJvZ3Jlc3NCYXIuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gICAgLyoqXG4gICAgICogVGhlIGN1cnJlbnQgcHJvZ3Jlc3MgcGVyY2VudGFnZSwgZnJvbSAwIHRvIDEwMFxuICAgICAqL1xuICAgIHBlcmNlbnRhZ2U6IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFdpZHRoIG9mIHByb2dyZXNzIGJhciBpbiBwaXhlbC5cbiAgICAgKi9cbiAgICB3aWR0aD86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRleHQgdG8gc2hvdyBpbnNpZGUgcHJvZ3Jlc3MgYmFyLlxuICAgICAqL1xuICAgIGNvbnRlbnQ/OiBzdHJpbmc7XG4gIH1cbn1cblxuLyoqXG4gKiBBIGZ1bmN0aW9uYWwgdHN4IGNvbXBvbmVudCBmb3IgYSBwcm9ncmVzcyBiYXIuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBQcm9ncmVzc0Jhcihwcm9wczogUHJvZ3Jlc3NCYXIuSVByb3BzKTogSlNYLkVsZW1lbnQge1xuICBjb25zdCB7IHdpZHRoLCBwZXJjZW50YWdlLCAuLi5yZXN0IH0gPSBwcm9wcztcbiAgcmV0dXJuIChcbiAgICA8ZGl2XG4gICAgICBjbGFzc05hbWU9eydqcC1TdGF0dXNiYXItUHJvZ3Jlc3NCYXItcHJvZ3Jlc3MtYmFyJ31cbiAgICAgIHJvbGU9XCJwcm9ncmVzc2JhclwiXG4gICAgICBhcmlhLXZhbHVlbWluPXswfVxuICAgICAgYXJpYS12YWx1ZW1heD17MTAwfVxuICAgICAgYXJpYS12YWx1ZW5vdz17cGVyY2VudGFnZX1cbiAgICA+XG4gICAgICA8RmlsbGVyIHsuLi57IHBlcmNlbnRhZ2UsIC4uLnJlc3QgfX0gY29udGVudFdpZHRoPXt3aWR0aH0gLz5cbiAgICA8L2Rpdj5cbiAgKTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgRmlsbGVyIHN0YXRpY3MuXG4gKi9cbm5hbWVzcGFjZSBGaWxsZXIge1xuICAvKipcbiAgICogUHJvcHMgZm9yIHRoZSBGaWxsZXIgY29tcG9uZW50LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IHBlcmNlbnRhZ2UgZmlsbGVkLCBmcm9tIDAgdG8gMTAwXG4gICAgICovXG4gICAgcGVyY2VudGFnZTogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogV2lkdGggb2YgY29udGVudCBpbnNpZGUgZmlsbGVyLlxuICAgICAqL1xuICAgIGNvbnRlbnRXaWR0aD86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRleHQgdG8gc2hvdyBpbnNpZGUgZmlsbGVyLlxuICAgICAqL1xuICAgIGNvbnRlbnQ/OiBzdHJpbmc7XG4gIH1cbn1cblxuLyoqXG4gKiBBIGZ1bmN0aW9uYWwgdHN4IGNvbXBvbmVudCBmb3IgYSBwYXJ0aWFsbHkgZmlsbGVkIGRpdi5cbiAqL1xuZnVuY3Rpb24gRmlsbGVyKHByb3BzOiBGaWxsZXIuSVByb3BzKSB7XG4gIHJldHVybiAoXG4gICAgPGRpdlxuICAgICAgc3R5bGU9e3tcbiAgICAgICAgd2lkdGg6IGAke3Byb3BzLnBlcmNlbnRhZ2V9JWBcbiAgICAgIH19XG4gICAgPlxuICAgICAgPHA+e3Byb3BzLmNvbnRlbnR9PC9wPlxuICAgIDwvZGl2PlxuICApO1xufVxuIiwiLypcbiAqIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuICogRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbiAqL1xuXG5pbXBvcnQgUmVhY3QgZnJvbSAncmVhY3QnO1xuZXhwb3J0IG5hbWVzcGFjZSBQcm9ncmVzc0NpcmNsZSB7XG4gIC8qKlxuICAgKiBQcm9wcyBmb3IgdGhlIFByb2dyZXNzQmFyLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcHMge1xuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IHByb2dyZXNzIHBlcmNlbnRhZ2UsIGZyb20gMCB0byAxMDBcbiAgICAgKi9cbiAgICBwcm9ncmVzczogbnVtYmVyO1xuXG4gICAgd2lkdGg/OiBudW1iZXI7XG5cbiAgICBoZWlnaHQ/OiBudW1iZXI7XG4gIH1cbn1cblxuZXhwb3J0IGZ1bmN0aW9uIFByb2dyZXNzQ2lyY2xlKHByb3BzOiBQcm9ncmVzc0NpcmNsZS5JUHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGNvbnN0IHJhZGl1cyA9IDEwNDtcbiAgY29uc3QgZCA9IChwcm9ncmVzczogbnVtYmVyKTogc3RyaW5nID0+IHtcbiAgICBjb25zdCBhbmdsZSA9IE1hdGgubWF4KHByb2dyZXNzICogMy42LCAwLjEpO1xuICAgIGNvbnN0IHJhZCA9IChhbmdsZSAqIE1hdGguUEkpIC8gMTgwLFxuICAgICAgeCA9IE1hdGguc2luKHJhZCkgKiByYWRpdXMsXG4gICAgICB5ID0gTWF0aC5jb3MocmFkKSAqIC1yYWRpdXMsXG4gICAgICBtaWQgPSBhbmdsZSA8IDE4MCA/IDEgOiAwLFxuICAgICAgc2hhcGUgPVxuICAgICAgICBgTSAwIDAgdiAtJHtyYWRpdXN9IEEgJHtyYWRpdXN9ICR7cmFkaXVzfSAxIGAgK1xuICAgICAgICBtaWQgK1xuICAgICAgICAnIDAgJyArXG4gICAgICAgIHgudG9GaXhlZCg0KSArXG4gICAgICAgICcgJyArXG4gICAgICAgIHkudG9GaXhlZCg0KSArXG4gICAgICAgICcgeic7XG4gICAgcmV0dXJuIHNoYXBlO1xuICB9O1xuICByZXR1cm4gKFxuICAgIDxkaXZcbiAgICAgIGNsYXNzTmFtZT17J2pwLVN0YXR1c2Jhci1Qcm9ncmVzc0NpcmNsZSd9XG4gICAgICByb2xlPVwicHJvZ3Jlc3NiYXJcIlxuICAgICAgYXJpYS12YWx1ZW1pbj17MH1cbiAgICAgIGFyaWEtdmFsdWVtYXg9ezEwMH1cbiAgICAgIGFyaWEtdmFsdWVub3c9e3Byb3BzLnByb2dyZXNzfVxuICAgID5cbiAgICAgIDxzdmcgdmlld0JveD1cIjAgMCAyNTAgMjUwXCI+XG4gICAgICAgIDxjaXJjbGVcbiAgICAgICAgICBjeD1cIjEyNVwiXG4gICAgICAgICAgY3k9XCIxMjVcIlxuICAgICAgICAgIHI9e2Ake3JhZGl1c31gfVxuICAgICAgICAgIHN0cm9rZT1cInZhcigtLWpwLWludmVyc2UtbGF5b3V0LWNvbG9yMylcIlxuICAgICAgICAgIHN0cm9rZVdpZHRoPVwiMjBcIlxuICAgICAgICAgIGZpbGw9XCJub25lXCJcbiAgICAgICAgLz5cbiAgICAgICAgPHBhdGhcbiAgICAgICAgICB0cmFuc2Zvcm09XCJ0cmFuc2xhdGUoMTI1LDEyNSkgc2NhbGUoLjkpXCJcbiAgICAgICAgICBkPXtkKHByb3BzLnByb2dyZXNzKX1cbiAgICAgICAgICBmaWxsPXsndmFyKC0tanAtaW52ZXJzZS1sYXlvdXQtY29sb3IzKSd9XG4gICAgICAgIC8+XG4gICAgICA8L3N2Zz5cbiAgICA8L2Rpdj5cbiAgKTtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0IHsgY2xhc3NlcyB9IGZyb20gJ3R5cGVzdHlsZS9saWInO1xuaW1wb3J0IHsgdGV4dEl0ZW0gfSBmcm9tICcuLi9zdHlsZS90ZXh0JztcblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgVGV4dEl0ZW0gc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBUZXh0SXRlbSB7XG4gIC8qKlxuICAgKiBQcm9wcyBmb3IgYSBUZXh0SXRlbS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVByb3BzIHtcbiAgICAvKipcbiAgICAgKiBUaGUgY29udGVudCBvZiB0aGUgdGV4dCBpdGVtLlxuICAgICAqL1xuICAgIHNvdXJjZTogc3RyaW5nIHwgbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogSG92ZXIgdGV4dCB0byBnaXZlIHRvIHRoZSBub2RlLlxuICAgICAqL1xuICAgIHRpdGxlPzogc3RyaW5nO1xuICB9XG59XG5cbi8qKlxuICogQSBmdW5jdGlvbmFsIHRzeCBjb21wb25lbnQgZm9yIGEgdGV4dCBpdGVtLlxuICovXG5leHBvcnQgZnVuY3Rpb24gVGV4dEl0ZW0oXG4gIHByb3BzOiBUZXh0SXRlbS5JUHJvcHMgJiBSZWFjdC5IVE1MQXR0cmlidXRlczxIVE1MU3BhbkVsZW1lbnQ+XG4pOiBSZWFjdC5SZWFjdEVsZW1lbnQ8VGV4dEl0ZW0uSVByb3BzPiB7XG4gIGNvbnN0IHsgdGl0bGUsIHNvdXJjZSwgY2xhc3NOYW1lLCAuLi5yZXN0IH0gPSBwcm9wcztcbiAgcmV0dXJuIChcbiAgICA8c3BhbiBjbGFzc05hbWU9e2NsYXNzZXModGV4dEl0ZW0sIGNsYXNzTmFtZSl9IHRpdGxlPXt0aXRsZX0gey4uLnJlc3R9PlxuICAgICAge3NvdXJjZX1cbiAgICA8L3NwYW4+XG4gICk7XG59XG4iLCIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHN0YXR1c2JhclxuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vY29tcG9uZW50cyc7XG5leHBvcnQgKiBmcm9tICcuL3N0YXR1c2Jhcic7XG5leHBvcnQgKiBmcm9tICcuL3N0eWxlL3N0YXR1c2Jhcic7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IEFycmF5RXh0IH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHtcbiAgRGlzcG9zYWJsZURlbGVnYXRlLFxuICBEaXNwb3NhYmxlU2V0LFxuICBJRGlzcG9zYWJsZVxufSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFBhbmVsLCBQYW5lbExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7XG4gIHN0YXR1c0JhciBhcyBiYXJTdHlsZSxcbiAgaXRlbSBhcyBpdGVtU3R5bGUsXG4gIGxlZnRTaWRlIGFzIGxlZnRTaWRlU3R5bGUsXG4gIHJpZ2h0U2lkZSBhcyByaWdodFNpZGVTdHlsZSxcbiAgc2lkZSBhcyBzaWRlU3R5bGVcbn0gZnJvbSAnLi9zdHlsZS9zdGF0dXNiYXInO1xuaW1wb3J0IHsgSVN0YXR1c0JhciB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBNYWluIHN0YXR1cyBiYXIgb2JqZWN0IHdoaWNoIGNvbnRhaW5zIGFsbCBpdGVtcy5cbiAqL1xuZXhwb3J0IGNsYXNzIFN0YXR1c0JhciBleHRlbmRzIFdpZGdldCBpbXBsZW1lbnRzIElTdGF0dXNCYXIge1xuICBjb25zdHJ1Y3RvcigpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuYWRkQ2xhc3MoYmFyU3R5bGUpO1xuXG4gICAgY29uc3Qgcm9vdExheW91dCA9ICh0aGlzLmxheW91dCA9IG5ldyBQYW5lbExheW91dCgpKTtcblxuICAgIGNvbnN0IGxlZnRQYW5lbCA9ICh0aGlzLl9sZWZ0U2lkZSA9IG5ldyBQYW5lbCgpKTtcbiAgICBjb25zdCBtaWRkbGVQYW5lbCA9ICh0aGlzLl9taWRkbGVQYW5lbCA9IG5ldyBQYW5lbCgpKTtcbiAgICBjb25zdCByaWdodFBhbmVsID0gKHRoaXMuX3JpZ2h0U2lkZSA9IG5ldyBQYW5lbCgpKTtcblxuICAgIGxlZnRQYW5lbC5hZGRDbGFzcyhzaWRlU3R5bGUpO1xuICAgIGxlZnRQYW5lbC5hZGRDbGFzcyhsZWZ0U2lkZVN0eWxlKTtcblxuICAgIG1pZGRsZVBhbmVsLmFkZENsYXNzKHNpZGVTdHlsZSk7XG5cbiAgICByaWdodFBhbmVsLmFkZENsYXNzKHNpZGVTdHlsZSk7XG4gICAgcmlnaHRQYW5lbC5hZGRDbGFzcyhyaWdodFNpZGVTdHlsZSk7XG5cbiAgICByb290TGF5b3V0LmFkZFdpZGdldChsZWZ0UGFuZWwpO1xuICAgIHJvb3RMYXlvdXQuYWRkV2lkZ2V0KG1pZGRsZVBhbmVsKTtcbiAgICByb290TGF5b3V0LmFkZFdpZGdldChyaWdodFBhbmVsKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWdpc3RlciBhIG5ldyBzdGF0dXMgaXRlbS5cbiAgICpcbiAgICogQHBhcmFtIGlkIC0gYSB1bmlxdWUgaWQgZm9yIHRoZSBzdGF0dXMgaXRlbS5cbiAgICpcbiAgICogQHBhcmFtIHN0YXR1c0l0ZW0gLSBUaGUgaXRlbSB0byBhZGQgdG8gdGhlIHN0YXR1cyBiYXIuXG4gICAqL1xuICByZWdpc3RlclN0YXR1c0l0ZW0oaWQ6IHN0cmluZywgc3RhdHVzSXRlbTogSVN0YXR1c0Jhci5JSXRlbSk6IElEaXNwb3NhYmxlIHtcbiAgICBpZiAoaWQgaW4gdGhpcy5fc3RhdHVzSXRlbXMpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgU3RhdHVzIGl0ZW0gJHtpZH0gYWxyZWFkeSByZWdpc3RlcmVkLmApO1xuICAgIH1cblxuICAgIC8vIFBvcHVsYXRlIGRlZmF1bHRzIGZvciB0aGUgb3B0aW9uYWwgcHJvcGVydGllcyBvZiB0aGUgc3RhdHVzIGl0ZW0uXG4gICAgY29uc3QgZnVsbFN0YXR1c0l0ZW0gPSB7XG4gICAgICAuLi5Qcml2YXRlLnN0YXR1c0l0ZW1EZWZhdWx0cyxcbiAgICAgIC4uLnN0YXR1c0l0ZW1cbiAgICB9IGFzIFByaXZhdGUuSUZ1bGxJdGVtO1xuICAgIGNvbnN0IHsgYWxpZ24sIGl0ZW0sIHJhbmsgfSA9IGZ1bGxTdGF0dXNJdGVtO1xuXG4gICAgLy8gQ29ubmVjdCB0aGUgYWN0aXZlU3RhdGVDaGFuZ2VkIHNpZ25hbCB0byByZWZyZXNoaW5nIHRoZSBzdGF0dXMgaXRlbSxcbiAgICAvLyBpZiB0aGUgc2lnbmFsIHdhcyBwcm92aWRlZC5cbiAgICBjb25zdCBvbkFjdGl2ZVN0YXRlQ2hhbmdlZCA9ICgpID0+IHtcbiAgICAgIHRoaXMuX3JlZnJlc2hJdGVtKGlkKTtcbiAgICB9O1xuICAgIGlmIChmdWxsU3RhdHVzSXRlbS5hY3RpdmVTdGF0ZUNoYW5nZWQpIHtcbiAgICAgIGZ1bGxTdGF0dXNJdGVtLmFjdGl2ZVN0YXRlQ2hhbmdlZC5jb25uZWN0KG9uQWN0aXZlU3RhdGVDaGFuZ2VkKTtcbiAgICB9XG5cbiAgICBjb25zdCByYW5rSXRlbSA9IHsgaWQsIHJhbmsgfTtcblxuICAgIGZ1bGxTdGF0dXNJdGVtLml0ZW0uYWRkQ2xhc3MoaXRlbVN0eWxlKTtcbiAgICB0aGlzLl9zdGF0dXNJdGVtc1tpZF0gPSBmdWxsU3RhdHVzSXRlbTtcblxuICAgIGlmIChhbGlnbiA9PT0gJ2xlZnQnKSB7XG4gICAgICBjb25zdCBpbnNlcnRJbmRleCA9IHRoaXMuX2ZpbmRJbnNlcnRJbmRleCh0aGlzLl9sZWZ0UmFua0l0ZW1zLCByYW5rSXRlbSk7XG4gICAgICBpZiAoaW5zZXJ0SW5kZXggPT09IC0xKSB7XG4gICAgICAgIHRoaXMuX2xlZnRTaWRlLmFkZFdpZGdldChpdGVtKTtcbiAgICAgICAgdGhpcy5fbGVmdFJhbmtJdGVtcy5wdXNoKHJhbmtJdGVtKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIEFycmF5RXh0Lmluc2VydCh0aGlzLl9sZWZ0UmFua0l0ZW1zLCBpbnNlcnRJbmRleCwgcmFua0l0ZW0pO1xuICAgICAgICB0aGlzLl9sZWZ0U2lkZS5pbnNlcnRXaWRnZXQoaW5zZXJ0SW5kZXgsIGl0ZW0pO1xuICAgICAgfVxuICAgIH0gZWxzZSBpZiAoYWxpZ24gPT09ICdyaWdodCcpIHtcbiAgICAgIGNvbnN0IGluc2VydEluZGV4ID0gdGhpcy5fZmluZEluc2VydEluZGV4KHRoaXMuX3JpZ2h0UmFua0l0ZW1zLCByYW5rSXRlbSk7XG4gICAgICBpZiAoaW5zZXJ0SW5kZXggPT09IC0xKSB7XG4gICAgICAgIHRoaXMuX3JpZ2h0U2lkZS5hZGRXaWRnZXQoaXRlbSk7XG4gICAgICAgIHRoaXMuX3JpZ2h0UmFua0l0ZW1zLnB1c2gocmFua0l0ZW0pO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgQXJyYXlFeHQuaW5zZXJ0KHRoaXMuX3JpZ2h0UmFua0l0ZW1zLCBpbnNlcnRJbmRleCwgcmFua0l0ZW0pO1xuICAgICAgICB0aGlzLl9yaWdodFNpZGUuaW5zZXJ0V2lkZ2V0KGluc2VydEluZGV4LCBpdGVtKTtcbiAgICAgIH1cbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5fbWlkZGxlUGFuZWwuYWRkV2lkZ2V0KGl0ZW0pO1xuICAgIH1cbiAgICB0aGlzLl9yZWZyZXNoSXRlbShpZCk7IC8vIEluaXRpYWxseSByZWZyZXNoIHRoZSBzdGF0dXMgaXRlbS5cblxuICAgIGNvbnN0IGRpc3Bvc2FibGUgPSBuZXcgRGlzcG9zYWJsZURlbGVnYXRlKCgpID0+IHtcbiAgICAgIGRlbGV0ZSB0aGlzLl9zdGF0dXNJdGVtc1tpZF07XG4gICAgICBpZiAoZnVsbFN0YXR1c0l0ZW0uYWN0aXZlU3RhdGVDaGFuZ2VkKSB7XG4gICAgICAgIGZ1bGxTdGF0dXNJdGVtLmFjdGl2ZVN0YXRlQ2hhbmdlZC5kaXNjb25uZWN0KG9uQWN0aXZlU3RhdGVDaGFuZ2VkKTtcbiAgICAgIH1cbiAgICAgIGl0ZW0ucGFyZW50ID0gbnVsbDtcbiAgICAgIGl0ZW0uZGlzcG9zZSgpO1xuICAgIH0pO1xuICAgIHRoaXMuX2Rpc3Bvc2FibGVzLmFkZChkaXNwb3NhYmxlKTtcbiAgICByZXR1cm4gZGlzcG9zYWJsZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSBzdGF0dXMgYmFyLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICB0aGlzLl9sZWZ0UmFua0l0ZW1zLmxlbmd0aCA9IDA7XG4gICAgdGhpcy5fcmlnaHRSYW5rSXRlbXMubGVuZ3RoID0gMDtcbiAgICB0aGlzLl9kaXNwb3NhYmxlcy5kaXNwb3NlKCk7XG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbiAndXBkYXRlLXJlcXVlc3QnIG1lc3NhZ2UgdG8gdGhlIHN0YXR1cyBiYXIuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMuX3JlZnJlc2hBbGwoKTtcbiAgICBzdXBlci5vblVwZGF0ZVJlcXVlc3QobXNnKTtcbiAgfVxuXG4gIHByaXZhdGUgX2ZpbmRJbnNlcnRJbmRleChcbiAgICBzaWRlOiBQcml2YXRlLklSYW5rSXRlbVtdLFxuICAgIG5ld0l0ZW06IFByaXZhdGUuSVJhbmtJdGVtXG4gICk6IG51bWJlciB7XG4gICAgcmV0dXJuIEFycmF5RXh0LmZpbmRGaXJzdEluZGV4KHNpZGUsIGl0ZW0gPT4gaXRlbS5yYW5rID4gbmV3SXRlbS5yYW5rKTtcbiAgfVxuXG4gIHByaXZhdGUgX3JlZnJlc2hJdGVtKGlkOiBzdHJpbmcpIHtcbiAgICBjb25zdCBzdGF0dXNJdGVtID0gdGhpcy5fc3RhdHVzSXRlbXNbaWRdO1xuICAgIGlmIChzdGF0dXNJdGVtLmlzQWN0aXZlKCkpIHtcbiAgICAgIHN0YXR1c0l0ZW0uaXRlbS5zaG93KCk7XG4gICAgICBzdGF0dXNJdGVtLml0ZW0udXBkYXRlKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHN0YXR1c0l0ZW0uaXRlbS5oaWRlKCk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfcmVmcmVzaEFsbCgpOiB2b2lkIHtcbiAgICBPYmplY3Qua2V5cyh0aGlzLl9zdGF0dXNJdGVtcykuZm9yRWFjaChpZCA9PiB7XG4gICAgICB0aGlzLl9yZWZyZXNoSXRlbShpZCk7XG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIF9sZWZ0UmFua0l0ZW1zOiBQcml2YXRlLklSYW5rSXRlbVtdID0gW107XG4gIHByaXZhdGUgX3JpZ2h0UmFua0l0ZW1zOiBQcml2YXRlLklSYW5rSXRlbVtdID0gW107XG4gIHByaXZhdGUgX3N0YXR1c0l0ZW1zOiB7IFtpZDogc3RyaW5nXTogUHJpdmF0ZS5JRnVsbEl0ZW0gfSA9IHt9O1xuICBwcml2YXRlIF9kaXNwb3NhYmxlcyA9IG5ldyBEaXNwb3NhYmxlU2V0KCk7XG4gIHByaXZhdGUgX2xlZnRTaWRlOiBQYW5lbDtcbiAgcHJpdmF0ZSBfbWlkZGxlUGFuZWw6IFBhbmVsO1xuICBwcml2YXRlIF9yaWdodFNpZGU6IFBhbmVsO1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGZ1bmN0aW9uYWxpdHkuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgdHlwZSBPbWl0PFQsIEsgZXh0ZW5kcyBrZXlvZiBUPiA9IFBpY2s8VCwgRXhjbHVkZTxrZXlvZiBULCBLPj47XG4gIC8qKlxuICAgKiBEZWZhdWx0IG9wdGlvbnMgZm9yIGEgc3RhdHVzIGl0ZW0sIGxlc3MgdGhlIGl0ZW0gaXRzZWxmLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IHN0YXR1c0l0ZW1EZWZhdWx0czogT21pdDxJU3RhdHVzQmFyLklJdGVtLCAnaXRlbSc+ID0ge1xuICAgIGFsaWduOiAnbGVmdCcsXG4gICAgcmFuazogMCxcbiAgICBpc0FjdGl2ZTogKCkgPT4gdHJ1ZSxcbiAgICBhY3RpdmVTdGF0ZUNoYW5nZWQ6IHVuZGVmaW5lZFxuICB9O1xuXG4gIC8qKlxuICAgKiBBbiBpbnRlcmZhY2UgZm9yIHN0b3JpbmcgdGhlIHJhbmsgb2YgYSBzdGF0dXMgaXRlbS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVJhbmtJdGVtIHtcbiAgICBpZDogc3RyaW5nO1xuICAgIHJhbms6IG51bWJlcjtcbiAgfVxuXG4gIGV4cG9ydCB0eXBlIERlZmF1bHRLZXlzID0gJ2FsaWduJyB8ICdyYW5rJyB8ICdpc0FjdGl2ZSc7XG5cbiAgLyoqXG4gICAqIFR5cGUgb2Ygc3RhdHVzYmFyIGl0ZW0gd2l0aCBkZWZhdWx0cyBmaWxsZWQgaW4uXG4gICAqL1xuICBleHBvcnQgdHlwZSBJRnVsbEl0ZW0gPSBSZXF1aXJlZDxQaWNrPElTdGF0dXNCYXIuSUl0ZW0sIERlZmF1bHRLZXlzPj4gJlxuICAgIE9taXQ8SVN0YXR1c0Jhci5JSXRlbSwgRGVmYXVsdEtleXM+O1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBOZXN0ZWRDU1NQcm9wZXJ0aWVzIH0gZnJvbSAndHlwZXN0eWxlL2xpYi90eXBlcyc7XG5cbmV4cG9ydCBjb25zdCBjZW50ZXJlZEZsZXg6IE5lc3RlZENTU1Byb3BlcnRpZXMgPSB7XG4gIGRpc3BsYXk6ICdmbGV4JyxcbiAgYWxpZ25JdGVtczogJ2NlbnRlcidcbn07XG5cbmV4cG9ydCBjb25zdCBsZWZ0VG9SaWdodDogTmVzdGVkQ1NTUHJvcGVydGllcyA9IHtcbiAgZmxleERpcmVjdGlvbjogJ3Jvdydcbn07XG5cbmV4cG9ydCBjb25zdCByaWdodFRvTGVmdDogTmVzdGVkQ1NTUHJvcGVydGllcyA9IHtcbiAgZmxleERpcmVjdGlvbjogJ3Jvdy1yZXZlcnNlJ1xufTtcblxuZXhwb3J0IGNvbnN0IGVxdWlEaXN0YW50OiBOZXN0ZWRDU1NQcm9wZXJ0aWVzID0ge1xuICBqdXN0aWZ5Q29udGVudDogJ3NwYWNlLWJldHdlZW4nXG59O1xuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBzdHlsZSB9IGZyb20gJ3R5cGVzdHlsZS9saWInO1xuaW1wb3J0IHsgY2VudGVyZWRGbGV4LCBsZWZ0VG9SaWdodCwgcmlnaHRUb0xlZnQgfSBmcm9tICcuL2xheW91dCc7XG5pbXBvcnQgeyB0ZXh0SXRlbSB9IGZyb20gJy4vdGV4dCc7XG5pbXBvcnQgdmFycyBmcm9tICcuL3ZhcmlhYmxlcyc7XG5cbmNvbnN0IGl0ZW1QYWRkaW5nID0ge1xuICBwYWRkaW5nTGVmdDogdmFycy5pdGVtUGFkZGluZyxcbiAgcGFkZGluZ1JpZ2h0OiB2YXJzLml0ZW1QYWRkaW5nXG59O1xuXG5jb25zdCBpbnRlcmFjdGl2ZUhvdmVyID0ge1xuICAkbmVzdDoge1xuICAgICcmOmhvdmVyJzoge1xuICAgICAgYmFja2dyb3VuZENvbG9yOiB2YXJzLmhvdmVyQ29sb3JcbiAgICB9XG4gIH1cbn07XG5cbmNvbnN0IGNsaWNrZWQgPSB7XG4gIGJhY2tncm91bmRDb2xvcjogdmFycy5jbGlja0NvbG9yLFxuICAkbmVzdDoge1xuICAgIFsnLicgKyB0ZXh0SXRlbV06IHtcbiAgICAgIGNvbG9yOiB2YXJzLnRleHRDbGlja0NvbG9yXG4gICAgfVxuICB9XG59O1xuXG5leHBvcnQgY29uc3Qgc3RhdHVzQmFyID0gc3R5bGUoXG4gIHtcbiAgICBiYWNrZ3JvdW5kOiB2YXJzLmJhY2tncm91bmRDb2xvcixcbiAgICBtaW5IZWlnaHQ6IHZhcnMuaGVpZ2h0LFxuICAgIGp1c3RpZnlDb250ZW50OiAnc3BhY2UtYmV0d2VlbicsXG4gICAgcGFkZGluZ0xlZnQ6IHZhcnMuc3RhdHVzQmFyUGFkZGluZyxcbiAgICBwYWRkaW5nUmlnaHQ6IHZhcnMuc3RhdHVzQmFyUGFkZGluZ1xuICB9LFxuICBjZW50ZXJlZEZsZXhcbik7XG5cbmV4cG9ydCBjb25zdCBzaWRlID0gc3R5bGUoY2VudGVyZWRGbGV4KTtcblxuZXhwb3J0IGNvbnN0IGxlZnRTaWRlID0gc3R5bGUobGVmdFRvUmlnaHQpO1xuXG5leHBvcnQgY29uc3QgcmlnaHRTaWRlID0gc3R5bGUocmlnaHRUb0xlZnQpO1xuXG5leHBvcnQgY29uc3QgaXRlbSA9IHN0eWxlKFxuICB7XG4gICAgbWF4SGVpZ2h0OiB2YXJzLmhlaWdodCxcbiAgICBtYXJnaW5MZWZ0OiB2YXJzLml0ZW1NYXJnaW4sXG4gICAgbWFyZ2luUmlnaHQ6IHZhcnMuaXRlbU1hcmdpbixcbiAgICBoZWlnaHQ6IHZhcnMuaGVpZ2h0LFxuICAgIHdoaXRlU3BhY2U6IHZhcnMud2hpdGVTcGFjZSxcbiAgICB0ZXh0T3ZlcmZsb3c6IHZhcnMudGV4dE92ZXJmbG93LFxuICAgIGNvbG9yOiB2YXJzLnRleHRDb2xvclxuICB9LFxuICBpdGVtUGFkZGluZ1xuKTtcblxuZXhwb3J0IGNvbnN0IGNsaWNrZWRJdGVtID0gc3R5bGUoY2xpY2tlZCk7XG5leHBvcnQgY29uc3QgaW50ZXJhY3RpdmVJdGVtID0gc3R5bGUoaW50ZXJhY3RpdmVIb3Zlcik7XG5cbmV4cG9ydCBjb25zdCBob3Zlckl0ZW0gPSBzdHlsZSh7XG4gIGJveFNoYWRvdzogJzBweCA0cHggNHB4IHJnYmEoMCwgMCwgMCwgMC4yNSknXG59KTtcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgc3R5bGUgfSBmcm9tICd0eXBlc3R5bGUvbGliJztcbmltcG9ydCB7IE5lc3RlZENTU1Byb3BlcnRpZXMgfSBmcm9tICd0eXBlc3R5bGUvbGliL3R5cGVzJztcbmltcG9ydCB2YXJzIGZyb20gJy4vdmFyaWFibGVzJztcblxuZXhwb3J0IGNvbnN0IGJhc2VUZXh0OiBOZXN0ZWRDU1NQcm9wZXJ0aWVzID0ge1xuICBmb250U2l6ZTogdmFycy5mb250U2l6ZSxcbiAgZm9udEZhbWlseTogdmFycy5mb250RmFtaWx5XG59O1xuXG5leHBvcnQgY29uc3QgdGV4dEl0ZW0gPSBzdHlsZShiYXNlVGV4dCwge1xuICBsaW5lSGVpZ2h0OiAnMjRweCcsXG4gIGNvbG9yOiB2YXJzLnRleHRDb2xvclxufSk7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5pbXBvcnQgeyBQcm9wZXJ0eSB9IGZyb20gJ2Nzc3R5cGUnO1xuXG5leHBvcnQgZGVmYXVsdCB7XG4gIGhvdmVyQ29sb3I6ICd2YXIoLS1qcC1sYXlvdXQtY29sb3IzKScsXG4gIGNsaWNrQ29sb3I6ICd2YXIoLS1qcC1icmFuZC1jb2xvcjEpJyxcbiAgYmFja2dyb3VuZENvbG9yOiAndmFyKC0tanAtbGF5b3V0LWNvbG9yMiknLFxuICBoZWlnaHQ6ICd2YXIoLS1qcC1zdGF0dXNiYXItaGVpZ2h0KScsXG4gIGZvbnRTaXplOiAndmFyKC0tanAtdWktZm9udC1zaXplMSknLFxuICBmb250RmFtaWx5OiAndmFyKC0tanAtdWktZm9udC1mYW1pbHkpJyxcbiAgdGV4dENvbG9yOiAndmFyKC0tanAtdWktZm9udC1jb2xvcjEpJyxcbiAgdGV4dENsaWNrQ29sb3I6ICd3aGl0ZScsXG4gIGl0ZW1NYXJnaW46ICcycHgnLFxuICBpdGVtUGFkZGluZzogJzZweCcsXG4gIHN0YXR1c0JhclBhZGRpbmc6ICcxMHB4JyxcbiAgaW50ZXJJdGVtSGFsZlNwYWNpbmc6ICcycHgnLCAvLyB0aGlzIGFtb3VudCBhY2NvdW50cyBmb3IgaGFsZiB0aGUgc3BhY2luZyBiZXR3ZWVuIGl0ZW1zXG4gIHdoaXRlU3BhY2U6ICdub3dyYXAnIGFzIFByb3BlcnR5LldoaXRlU3BhY2UsXG4gIHRleHRPdmVyZmxvdzogJ2VsbGlwc2lzJ1xufTtcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLy8gdHNsaW50OmRpc2FibGUtbmV4dC1saW5lOnZhcmlhYmxlLW5hbWVcbmV4cG9ydCBjb25zdCBJU3RhdHVzQmFyID0gbmV3IFRva2VuPElTdGF0dXNCYXI+KFxuICAnQGp1cHl0ZXJsYWIvc3RhdHVzYmFyOklTdGF0dXNCYXInXG4pO1xuXG4vKipcbiAqIE1haW4gc3RhdHVzIGJhciBvYmplY3Qgd2hpY2ggY29udGFpbnMgYWxsIHdpZGdldHMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVN0YXR1c0JhciB7XG4gIC8qKlxuICAgKiBSZWdpc3RlciBhIG5ldyBzdGF0dXMgaXRlbS5cbiAgICpcbiAgICogQHBhcmFtIGlkIC0gYSB1bmlxdWUgaWQgZm9yIHRoZSBzdGF0dXMgaXRlbS5cbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMgLSBUaGUgb3B0aW9ucyBmb3IgaG93IHRvIGFkZCB0aGUgc3RhdHVzIGl0ZW0uXG4gICAqXG4gICAqIEByZXR1cm5zIGFuIGBJRGlzcG9zYWJsZWAgdGhhdCBjYW4gYmUgZGlzcG9zZWQgdG8gcmVtb3ZlIHRoZSBpdGVtLlxuICAgKi9cbiAgcmVnaXN0ZXJTdGF0dXNJdGVtKGlkOiBzdHJpbmcsIHN0YXR1c0l0ZW06IElTdGF0dXNCYXIuSUl0ZW0pOiBJRGlzcG9zYWJsZTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3Igc3RhdHVzIGJhciBzdGF0aWNzLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIElTdGF0dXNCYXIge1xuICBleHBvcnQgdHlwZSBBbGlnbm1lbnQgPSAncmlnaHQnIHwgJ2xlZnQnIHwgJ21pZGRsZSc7XG5cbiAgLyoqXG4gICAqIE9wdGlvbnMgZm9yIHN0YXR1cyBiYXIgaXRlbXMuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElJdGVtIHtcbiAgICAvKipcbiAgICAgKiBUaGUgaXRlbSB0byBhZGQgdG8gdGhlIHN0YXR1cyBiYXIuXG4gICAgICovXG4gICAgaXRlbTogV2lkZ2V0O1xuXG4gICAgLyoqXG4gICAgICogV2hpY2ggc2lkZSB0byBwbGFjZSBpdGVtLlxuICAgICAqIFBlcm1hbmVudCBpdGVtcyBhcmUgaW50ZW5kZWQgZm9yIHRoZSByaWdodCBhbmQgbGVmdCBzaWRlLFxuICAgICAqIHdpdGggbW9yZSB0cmFuc2llbnQgaXRlbXMgaW4gdGhlIG1pZGRsZS5cbiAgICAgKi9cbiAgICBhbGlnbj86IEFsaWdubWVudDtcblxuICAgIC8qKlxuICAgICAqICBPcmRlcmluZyBvZiBJdGVtcyAtLSBoaWdoZXIgcmFuayBpdGVtcyBhcmUgY2xvc2VyIHRvIHRoZSBtaWRkbGUuXG4gICAgICovXG4gICAgcmFuaz86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdGhlIGl0ZW0gaXMgc2hvd24gb3IgaGlkZGVuLlxuICAgICAqL1xuICAgIGlzQWN0aXZlPzogKCkgPT4gYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIEEgc2lnbmFsIHRoYXQgaXMgZmlyZWQgd2hlbiB0aGUgaXRlbSBhY3RpdmUgc3RhdGUgY2hhbmdlcy5cbiAgICAgKi9cbiAgICBhY3RpdmVTdGF0ZUNoYW5nZWQ/OiBJU2lnbmFsPGFueSwgdm9pZD47XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==