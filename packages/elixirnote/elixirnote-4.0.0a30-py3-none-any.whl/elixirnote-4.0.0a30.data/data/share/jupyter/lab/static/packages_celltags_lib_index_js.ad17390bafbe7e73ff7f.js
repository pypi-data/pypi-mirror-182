"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_celltags_lib_index_js"],{

/***/ "../../packages/celltags/lib/addwidget.js":
/*!************************************************!*\
  !*** ../../packages/celltags/lib/addwidget.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AddWidget": () => (/* binding */ AddWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */



/**
 * A widget which hosts a cell tags area.
 */
class AddWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    /**
     * Construct a new tag widget.
     */
    constructor(translator) {
        super();
        this.parent = null;
        this.input = document.createElement('input');
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.addClass('tag');
        this.editing = false;
        this.buildTag();
    }
    /**
     * Create input box with icon and attach to this.node.
     */
    buildTag() {
        const text = this.input || document.createElement('input');
        text.value = this._trans.__('Add Tag');
        text.contentEditable = 'true';
        text.className = 'add-tag';
        text.style.width = '49px';
        this.input = text;
        const tag = document.createElement('div');
        tag.className = 'tag-holder';
        tag.appendChild(text);
        const iconContainer = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.addIcon.element({
            tag: 'span',
            elementPosition: 'center',
            height: '18px',
            width: '18px',
            marginLeft: '3px',
            marginRight: '-5px'
        });
        this.addClass('unapplied-tag');
        tag.appendChild(iconContainer);
        this.node.appendChild(tag);
    }
    /**
     * Handle `after-attach` messages for the widget.
     */
    onAfterAttach() {
        this.node.addEventListener('mousedown', this);
        this.input.addEventListener('keydown', this);
        this.input.addEventListener('focus', this);
        this.input.addEventListener('blur', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach() {
        this.node.removeEventListener('mousedown', this);
        this.input.removeEventListener('keydown', this);
        this.input.removeEventListener('focus', this);
        this.input.removeEventListener('blur', this);
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
        switch (event.type) {
            case 'mousedown':
                this._evtMouseDown(event);
                break;
            case 'keydown':
                this._evtKeyDown(event);
                break;
            case 'blur':
                this._evtBlur();
                break;
            case 'focus':
                this._evtFocus();
                break;
            default:
                break;
        }
    }
    /**
     * Handle the `'mousedown'` event for the input box.
     *
     * @param event - The DOM event sent to the widget
     */
    _evtMouseDown(event) {
        if (!this.editing) {
            this.editing = true;
            this.input.value = '';
            this.input.focus();
        }
        else if (event.target !== this.input) {
            if (this.input.value !== '') {
                const value = this.input.value;
                this.parent.addTag(value);
                this.input.blur();
                this._evtBlur();
            }
        }
        event.preventDefault();
    }
    /**
     * Handle the `'focus'` event for the input box.
     */
    _evtFocus() {
        if (!this.editing) {
            this.input.blur();
        }
    }
    /**
     * Handle the `'keydown'` event for the input box.
     *
     * @param event - The DOM event sent to the widget
     */
    _evtKeyDown(event) {
        const tmp = document.createElement('span');
        tmp.className = 'add-tag';
        tmp.innerHTML = this.input.value;
        // set width to the pixel length of the text
        document.body.appendChild(tmp);
        this.input.style.width = tmp.getBoundingClientRect().width + 8 + 'px';
        document.body.removeChild(tmp);
        // if they hit Enter, add the tag and reset state
        if (event.keyCode === 13) {
            const value = this.input.value;
            this.parent.addTag(value);
            this.input.blur();
            this._evtBlur();
        }
    }
    /**
     * Handle the `'focusout'` event for the input box.
     */
    _evtBlur() {
        if (this.editing) {
            this.editing = false;
            this.input.value = this._trans.__('Add Tag');
            this.input.style.width = '49px';
        }
    }
}


/***/ }),

/***/ "../../packages/celltags/lib/index.js":
/*!********************************************!*\
  !*** ../../packages/celltags/lib/index.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AddWidget": () => (/* reexport safe */ _addwidget__WEBPACK_IMPORTED_MODULE_0__.AddWidget),
/* harmony export */   "TagTool": () => (/* reexport safe */ _tool__WEBPACK_IMPORTED_MODULE_1__.TagTool),
/* harmony export */   "TagWidget": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_2__.TagWidget)
/* harmony export */ });
/* harmony import */ var _addwidget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./addwidget */ "../../packages/celltags/lib/addwidget.js");
/* harmony import */ var _tool__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tool */ "../../packages/celltags/lib/tool.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widget */ "../../packages/celltags/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module celltags
 */





/***/ }),

/***/ "../../packages/celltags/lib/tool.js":
/*!*******************************************!*\
  !*** ../../packages/celltags/lib/tool.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TagTool": () => (/* binding */ TagTool)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/algorithm */ "webpack/sharing/consume/default/@lumino/algorithm/@lumino/algorithm");
/* harmony import */ var _lumino_algorithm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _addwidget__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./addwidget */ "../../packages/celltags/lib/addwidget.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./widget */ "../../packages/celltags/lib/widget.js");
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */







/**
 * A Tool for tag operations.
 */
class TagTool extends _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookTools.Tool {
    /**
     * Construct a new tag Tool.
     *
     * @param tracker - The notebook tracker.
     */
    constructor(tracker, app, translator) {
        super();
        this.tagList = [];
        this.label = false;
        app;
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.tracker = tracker;
        this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_4__.PanelLayout();
        this.createTagInput();
        this.addClass('jp-TagTool');
    }
    /**
     * Add an AddWidget input box to the layout.
     */
    createTagInput() {
        const layout = this.layout;
        const input = new _addwidget__WEBPACK_IMPORTED_MODULE_5__.AddWidget(this.translator);
        input.id = 'add-tag';
        layout.insertWidget(0, input);
    }
    /**
     * Check whether a tag is applied to the current active cell
     *
     * @param name - The name of the tag.
     *
     * @returns A boolean representing whether it is applied.
     */
    checkApplied(name) {
        var _a;
        const activeCell = (_a = this.tracker) === null || _a === void 0 ? void 0 : _a.activeCell;
        if (activeCell) {
            const tags = activeCell.model.metadata.get('tags');
            if (tags) {
                return tags.includes(name);
            }
        }
        return false;
    }
    /**
     * Add a tag to the current active cell.
     *
     * @param name - The name of the tag.
     */
    addTag(name) {
        var _a, _b;
        const cell = (_a = this.tracker) === null || _a === void 0 ? void 0 : _a.activeCell;
        if (cell) {
            const oldTags = [
                ...((_b = cell.model.metadata.get('tags')) !== null && _b !== void 0 ? _b : [])
            ];
            let tagsToAdd = name.split(/[,\s]+/);
            tagsToAdd = tagsToAdd.filter(tag => tag !== '' && !oldTags.includes(tag));
            cell.model.metadata.set('tags', oldTags.concat(tagsToAdd));
            this.refreshTags();
            this.loadActiveTags();
        }
    }
    /**
     * Remove a tag from the current active cell.
     *
     * @param name - The name of the tag.
     */
    removeTag(name) {
        var _a, _b;
        const cell = (_a = this.tracker) === null || _a === void 0 ? void 0 : _a.activeCell;
        if (cell) {
            const oldTags = [
                ...((_b = cell.model.metadata.get('tags')) !== null && _b !== void 0 ? _b : [])
            ];
            let tags = oldTags.filter(tag => tag !== name);
            cell.model.metadata.set('tags', tags);
            if (tags.length === 0) {
                cell.model.metadata.delete('tags');
            }
            this.refreshTags();
            this.loadActiveTags();
        }
    }
    /**
     * Update each tag widget to represent whether it is applied to the current
     * active cell.
     */
    loadActiveTags() {
        const layout = this.layout;
        for (const widget of layout.widgets) {
            widget.update();
        }
    }
    /**
     * Pull from cell metadata all the tags used in the notebook and update the
     * stored tag list.
     */
    pullTags() {
        var _a, _b, _c;
        const notebook = (_a = this.tracker) === null || _a === void 0 ? void 0 : _a.currentWidget;
        const cells = (_c = (_b = notebook === null || notebook === void 0 ? void 0 : notebook.model) === null || _b === void 0 ? void 0 : _b.cells) !== null && _c !== void 0 ? _c : [];
        const allTags = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.reduce)(cells, (allTags, cell) => {
            var _a;
            const tags = (_a = cell.metadata.get('tags')) !== null && _a !== void 0 ? _a : [];
            return [...allTags, ...tags];
        }, []);
        this.tagList = [...new Set(allTags)].filter(tag => tag !== '');
    }
    /**
     * Pull the most recent list of tags and update the tag widgets - dispose if
     * the tag no longer exists, and create new widgets for new tags.
     */
    refreshTags() {
        this.pullTags();
        const layout = this.layout;
        const tagWidgets = layout.widgets.filter(w => w.id !== 'add-tag');
        tagWidgets.forEach(widget => {
            if (!this.tagList.includes(widget.name)) {
                widget.dispose();
            }
        });
        const tagWidgetNames = tagWidgets.map(w => w.name);
        this.tagList.forEach(tag => {
            if (!tagWidgetNames.includes(tag)) {
                const idx = layout.widgets.length - 1;
                layout.insertWidget(idx, new _widget__WEBPACK_IMPORTED_MODULE_6__.TagWidget(tag));
            }
        });
    }
    /**
     * Validate the 'tags' of cell metadata, ensuring it is a list of strings and
     * that each string doesn't include spaces.
     */
    validateTags(cell, tags) {
        tags = tags.filter(tag => typeof tag === 'string');
        tags = (0,_lumino_algorithm__WEBPACK_IMPORTED_MODULE_2__.reduce)(tags, (allTags, tag) => {
            return [...allTags, ...tag.split(/[,\s]+/)];
        }, []);
        const validTags = [...new Set(tags)].filter(tag => tag !== '');
        cell.model.metadata.set('tags', validTags);
        this.refreshTags();
        this.loadActiveTags();
    }
    /**
     * Handle a change to the active cell.
     */
    onActiveCellChanged() {
        this.loadActiveTags();
    }
    /**
     * Get all tags once available.
     */
    onAfterShow() {
        this.refreshTags();
        this.loadActiveTags();
    }
    /**
     * Upon attach, add label if it doesn't already exist and listen for changes
     * from the notebook tracker.
     */
    onAfterAttach(msg) {
        if (!this.label) {
            const label = document.createElement('label');
            label.textContent = this._trans.__('Cell Tags');
            label.className = 'tag-label';
            this.parent.node.insertBefore(label, this.node);
            this.label = true;
        }
        this.onCurrentChanged();
        super.onAfterAttach(msg);
    }
    /**
     * Clear signal connections before detaching
     */
    onBeforeDetach(msg) {
        super.onBeforeDetach(msg);
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.disconnectReceiver(this);
    }
    /**
     * Handle a change to active cell metadata.
     */
    onActiveCellMetadataChanged() {
        const tags = this.tracker.activeCell.model.metadata.get('tags');
        let taglist = [];
        if (tags) {
            if (typeof tags === 'string') {
                taglist.push(tags);
            }
            else {
                taglist = tags;
            }
        }
        this.validateTags(this.tracker.activeCell, taglist);
    }
    /**
     * Callback on current widget changes
     */
    onCurrentChanged() {
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.disconnectReceiver(this);
        this.tracker.currentChanged.connect(this.onCurrentChanged, this);
        if (this.tracker.currentWidget) {
            void this.tracker.currentWidget.context.ready.then(() => {
                this.refresh();
            });
            this.tracker.currentWidget.model.cells.changed.connect(this.refresh, this);
            this.tracker.currentWidget.content.activeCellChanged.connect(this.refresh, this);
        }
        this.refresh();
    }
    /**
     * Refresh tags and active status
     */
    refresh() {
        this.refreshTags();
        this.loadActiveTags();
    }
}


/***/ }),

/***/ "../../packages/celltags/lib/widget.js":
/*!*********************************************!*\
  !*** ../../packages/celltags/lib/widget.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TagWidget": () => (/* binding */ TagWidget)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */


/**
 * A widget which hosts a cell tags area.
 */
class TagWidget extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget {
    /**
     * Construct a new tag widget.
     */
    constructor(name) {
        super();
        this.parent = null;
        this.applied = true;
        this.name = name;
        this.addClass('tag');
        this.buildTag();
    }
    /**
     * Create tag div with icon and attach to this.node.
     */
    buildTag() {
        const text = document.createElement('span');
        text.textContent = this.name;
        text.style.textOverflow = 'ellipsis';
        const tag = document.createElement('div');
        tag.className = 'tag-holder';
        tag.appendChild(text);
        const iconContainer = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.checkIcon.element({
            tag: 'span',
            elementPosition: 'center',
            height: '18px',
            width: '18px',
            marginLeft: '5px',
            marginRight: '-3px'
        });
        if (this.applied) {
            this.addClass('applied-tag');
        }
        else {
            this.addClass('unapplied-tag');
            iconContainer.style.display = 'none';
        }
        tag.appendChild(iconContainer);
        this.node.appendChild(tag);
    }
    /**
     * Handle `after-attach` messages for the widget.
     */
    onAfterAttach() {
        this.node.addEventListener('mousedown', this);
        this.node.addEventListener('mouseover', this);
        this.node.addEventListener('mouseout', this);
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach() {
        this.node.removeEventListener('mousedown', this);
        this.node.removeEventListener('mouseover', this);
        this.node.removeEventListener('mouseout', this);
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
        switch (event.type) {
            case 'mousedown':
                this._evtClick();
                break;
            case 'mouseover':
                this._evtMouseOver();
                break;
            case 'mouseout':
                this._evtMouseOut();
                break;
            default:
                break;
        }
    }
    /**
     * Handle `update-request` messages. Check if applied to current active cell.
     */
    onUpdateRequest() {
        var _a;
        const applied = (_a = this.parent) === null || _a === void 0 ? void 0 : _a.checkApplied(this.name);
        if (applied !== this.applied) {
            this.toggleApplied();
        }
    }
    /**
     * Update styling to reflect whether tag is applied to current active cell.
     */
    toggleApplied() {
        var _a, _b;
        if (this.applied) {
            this.removeClass('applied-tag');
            ((_a = this.node.firstChild) === null || _a === void 0 ? void 0 : _a.lastChild).style.display =
                'none';
            this.addClass('unapplied-tag');
        }
        else {
            this.removeClass('unapplied-tag');
            ((_b = this.node.firstChild) === null || _b === void 0 ? void 0 : _b.lastChild).style.display =
                'inline-block';
            this.addClass('applied-tag');
        }
        this.applied = !this.applied;
    }
    /**
     * Handle the `'click'` event for the widget.
     */
    _evtClick() {
        var _a, _b;
        if (this.applied) {
            (_a = this.parent) === null || _a === void 0 ? void 0 : _a.removeTag(this.name);
        }
        else {
            (_b = this.parent) === null || _b === void 0 ? void 0 : _b.addTag(this.name);
        }
        this.toggleApplied();
    }
    /**
     * Handle the `'mouseover'` event for the widget.
     */
    _evtMouseOver() {
        this.node.classList.add('tag-hover');
    }
    /**
     * Handle the `'mouseout'` event for the widget.
     */
    _evtMouseOut() {
        this.node.classList.remove('tag-hover');
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY2VsbHRhZ3NfbGliX2luZGV4X2pzLmFkMTczOTBiYWZiZTdlNzNmZjdmLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7O0dBR0c7QUFNOEI7QUFDbUI7QUFDWDtBQUd6Qzs7R0FFRztBQUNJLE1BQU0sU0FBVSxTQUFRLG1EQUFNO0lBQ25DOztPQUVHO0lBQ0gsWUFBWSxVQUF3QjtRQUNsQyxLQUFLLEVBQUUsQ0FBQztRQWtKSCxXQUFNLEdBQW1CLElBQUksQ0FBQztRQUU3QixVQUFLLEdBQXFCLFFBQVEsQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLENBQUM7UUFuSmhFLElBQUksQ0FBQyxVQUFVLEdBQUcsVUFBVSxJQUFJLG1FQUFjLENBQUM7UUFDL0MsSUFBSSxDQUFDLE1BQU0sR0FBRyxJQUFJLENBQUMsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUNqRCxJQUFJLENBQUMsUUFBUSxDQUFDLEtBQUssQ0FBQyxDQUFDO1FBQ3JCLElBQUksQ0FBQyxPQUFPLEdBQUcsS0FBSyxDQUFDO1FBQ3JCLElBQUksQ0FBQyxRQUFRLEVBQUUsQ0FBQztJQUNsQixDQUFDO0lBRUQ7O09BRUc7SUFDSCxRQUFRO1FBQ04sTUFBTSxJQUFJLEdBQUcsSUFBSSxDQUFDLEtBQUssSUFBSSxRQUFRLENBQUMsYUFBYSxDQUFDLE9BQU8sQ0FBQyxDQUFDO1FBQzNELElBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxFQUFFLENBQUMsU0FBUyxDQUFDLENBQUM7UUFDdkMsSUFBSSxDQUFDLGVBQWUsR0FBRyxNQUFNLENBQUM7UUFDOUIsSUFBSSxDQUFDLFNBQVMsR0FBRyxTQUFTLENBQUM7UUFDM0IsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLEdBQUcsTUFBTSxDQUFDO1FBQzFCLElBQUksQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDO1FBQ2xCLE1BQU0sR0FBRyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsS0FBSyxDQUFDLENBQUM7UUFDMUMsR0FBRyxDQUFDLFNBQVMsR0FBRyxZQUFZLENBQUM7UUFDN0IsR0FBRyxDQUFDLFdBQVcsQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUN0QixNQUFNLGFBQWEsR0FBRyxzRUFBZSxDQUFDO1lBQ3BDLEdBQUcsRUFBRSxNQUFNO1lBQ1gsZUFBZSxFQUFFLFFBQVE7WUFDekIsTUFBTSxFQUFFLE1BQU07WUFDZCxLQUFLLEVBQUUsTUFBTTtZQUNiLFVBQVUsRUFBRSxLQUFLO1lBQ2pCLFdBQVcsRUFBRSxNQUFNO1NBQ3BCLENBQUMsQ0FBQztRQUNILElBQUksQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLENBQUM7UUFDL0IsR0FBRyxDQUFDLFdBQVcsQ0FBQyxhQUFhLENBQUMsQ0FBQztRQUMvQixJQUFJLENBQUMsSUFBSSxDQUFDLFdBQVcsQ0FBQyxHQUFHLENBQUMsQ0FBQztJQUM3QixDQUFDO0lBRUQ7O09BRUc7SUFDSCxhQUFhO1FBQ1gsSUFBSSxDQUFDLElBQUksQ0FBQyxnQkFBZ0IsQ0FBQyxXQUFXLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDOUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxnQkFBZ0IsQ0FBQyxTQUFTLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDN0MsSUFBSSxDQUFDLEtBQUssQ0FBQyxnQkFBZ0IsQ0FBQyxPQUFPLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDM0MsSUFBSSxDQUFDLEtBQUssQ0FBQyxnQkFBZ0IsQ0FBQyxNQUFNLEVBQUUsSUFBSSxDQUFDLENBQUM7SUFDNUMsQ0FBQztJQUVEOztPQUVHO0lBQ0gsY0FBYztRQUNaLElBQUksQ0FBQyxJQUFJLENBQUMsbUJBQW1CLENBQUMsV0FBVyxFQUFFLElBQUksQ0FBQyxDQUFDO1FBQ2pELElBQUksQ0FBQyxLQUFLLENBQUMsbUJBQW1CLENBQUMsU0FBUyxFQUFFLElBQUksQ0FBQyxDQUFDO1FBQ2hELElBQUksQ0FBQyxLQUFLLENBQUMsbUJBQW1CLENBQUMsT0FBTyxFQUFFLElBQUksQ0FBQyxDQUFDO1FBQzlDLElBQUksQ0FBQyxLQUFLLENBQUMsbUJBQW1CLENBQUMsTUFBTSxFQUFFLElBQUksQ0FBQyxDQUFDO0lBQy9DLENBQUM7SUFFRDs7Ozs7Ozs7O09BU0c7SUFDSCxXQUFXLENBQUMsS0FBWTtRQUN0QixRQUFRLEtBQUssQ0FBQyxJQUFJLEVBQUU7WUFDbEIsS0FBSyxXQUFXO2dCQUNkLElBQUksQ0FBQyxhQUFhLENBQUMsS0FBbUIsQ0FBQyxDQUFDO2dCQUN4QyxNQUFNO1lBQ1IsS0FBSyxTQUFTO2dCQUNaLElBQUksQ0FBQyxXQUFXLENBQUMsS0FBc0IsQ0FBQyxDQUFDO2dCQUN6QyxNQUFNO1lBQ1IsS0FBSyxNQUFNO2dCQUNULElBQUksQ0FBQyxRQUFRLEVBQUUsQ0FBQztnQkFDaEIsTUFBTTtZQUNSLEtBQUssT0FBTztnQkFDVixJQUFJLENBQUMsU0FBUyxFQUFFLENBQUM7Z0JBQ2pCLE1BQU07WUFDUjtnQkFDRSxNQUFNO1NBQ1Q7SUFDSCxDQUFDO0lBRUQ7Ozs7T0FJRztJQUNLLGFBQWEsQ0FBQyxLQUFpQjtRQUNyQyxJQUFJLENBQUMsSUFBSSxDQUFDLE9BQU8sRUFBRTtZQUNqQixJQUFJLENBQUMsT0FBTyxHQUFHLElBQUksQ0FBQztZQUNwQixJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssR0FBRyxFQUFFLENBQUM7WUFDdEIsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLEVBQUUsQ0FBQztTQUNwQjthQUFNLElBQUksS0FBSyxDQUFDLE1BQU0sS0FBSyxJQUFJLENBQUMsS0FBSyxFQUFFO1lBQ3RDLElBQUksSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLEtBQUssRUFBRSxFQUFFO2dCQUMzQixNQUFNLEtBQUssR0FBRyxJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQztnQkFDOUIsSUFBSSxDQUFDLE1BQWtCLENBQUMsTUFBTSxDQUFDLEtBQUssQ0FBQyxDQUFDO2dCQUN2QyxJQUFJLENBQUMsS0FBSyxDQUFDLElBQUksRUFBRSxDQUFDO2dCQUNsQixJQUFJLENBQUMsUUFBUSxFQUFFLENBQUM7YUFDakI7U0FDRjtRQUNELEtBQUssQ0FBQyxjQUFjLEVBQUUsQ0FBQztJQUN6QixDQUFDO0lBRUQ7O09BRUc7SUFDSyxTQUFTO1FBQ2YsSUFBSSxDQUFDLElBQUksQ0FBQyxPQUFPLEVBQUU7WUFDakIsSUFBSSxDQUFDLEtBQUssQ0FBQyxJQUFJLEVBQUUsQ0FBQztTQUNuQjtJQUNILENBQUM7SUFFRDs7OztPQUlHO0lBQ0ssV0FBVyxDQUFDLEtBQW9CO1FBQ3RDLE1BQU0sR0FBRyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsTUFBTSxDQUFDLENBQUM7UUFDM0MsR0FBRyxDQUFDLFNBQVMsR0FBRyxTQUFTLENBQUM7UUFDMUIsR0FBRyxDQUFDLFNBQVMsR0FBRyxJQUFJLENBQUMsS0FBSyxDQUFDLEtBQUssQ0FBQztRQUNqQyw0Q0FBNEM7UUFDNUMsUUFBUSxDQUFDLElBQUksQ0FBQyxXQUFXLENBQUMsR0FBRyxDQUFDLENBQUM7UUFDL0IsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLEdBQUcsQ0FBQyxxQkFBcUIsRUFBRSxDQUFDLEtBQUssR0FBRyxDQUFDLEdBQUcsSUFBSSxDQUFDO1FBQ3RFLFFBQVEsQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLEdBQUcsQ0FBQyxDQUFDO1FBQy9CLGlEQUFpRDtRQUNqRCxJQUFJLEtBQUssQ0FBQyxPQUFPLEtBQUssRUFBRSxFQUFFO1lBQ3hCLE1BQU0sS0FBSyxHQUFHLElBQUksQ0FBQyxLQUFLLENBQUMsS0FBSyxDQUFDO1lBQzlCLElBQUksQ0FBQyxNQUFrQixDQUFDLE1BQU0sQ0FBQyxLQUFLLENBQUMsQ0FBQztZQUN2QyxJQUFJLENBQUMsS0FBSyxDQUFDLElBQUksRUFBRSxDQUFDO1lBQ2xCLElBQUksQ0FBQyxRQUFRLEVBQUUsQ0FBQztTQUNqQjtJQUNILENBQUM7SUFFRDs7T0FFRztJQUNLLFFBQVE7UUFDZCxJQUFJLElBQUksQ0FBQyxPQUFPLEVBQUU7WUFDaEIsSUFBSSxDQUFDLE9BQU8sR0FBRyxLQUFLLENBQUM7WUFDckIsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxFQUFFLENBQUMsU0FBUyxDQUFDLENBQUM7WUFDN0MsSUFBSSxDQUFDLEtBQUssQ0FBQyxLQUFLLENBQUMsS0FBSyxHQUFHLE1BQU0sQ0FBQztTQUNqQztJQUNILENBQUM7Q0FPRjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUM3S0QsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFFeUI7QUFDTDtBQUNFOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNUekI7OztHQUdHO0FBSW9FO0FBS3RDO0FBQ1U7QUFFQTtBQUNHO0FBQ047QUFDSDtBQUVyQzs7R0FFRztBQUNJLE1BQU0sT0FBUSxTQUFRLG9FQUFrQjtJQUM3Qzs7OztPQUlHO0lBQ0gsWUFDRSxPQUF5QixFQUN6QixHQUFvQixFQUNwQixVQUF3QjtRQUV4QixLQUFLLEVBQUUsQ0FBQztRQTRPRixZQUFPLEdBQWEsRUFBRSxDQUFDO1FBQ3ZCLFVBQUssR0FBWSxLQUFLLENBQUM7UUE1TzdCLEdBQUcsQ0FBQztRQUNKLElBQUksQ0FBQyxVQUFVLEdBQUcsVUFBVSxJQUFJLG1FQUFjLENBQUM7UUFDL0MsSUFBSSxDQUFDLE1BQU0sR0FBRyxJQUFJLENBQUMsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUNqRCxJQUFJLENBQUMsT0FBTyxHQUFHLE9BQU8sQ0FBQztRQUN2QixJQUFJLENBQUMsTUFBTSxHQUFHLElBQUksd0RBQVcsRUFBRSxDQUFDO1FBQ2hDLElBQUksQ0FBQyxjQUFjLEVBQUUsQ0FBQztRQUN0QixJQUFJLENBQUMsUUFBUSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzlCLENBQUM7SUFFRDs7T0FFRztJQUNILGNBQWM7UUFDWixNQUFNLE1BQU0sR0FBRyxJQUFJLENBQUMsTUFBcUIsQ0FBQztRQUMxQyxNQUFNLEtBQUssR0FBRyxJQUFJLGlEQUFTLENBQUMsSUFBSSxDQUFDLFVBQVUsQ0FBQyxDQUFDO1FBQzdDLEtBQUssQ0FBQyxFQUFFLEdBQUcsU0FBUyxDQUFDO1FBQ3JCLE1BQU0sQ0FBQyxZQUFZLENBQUMsQ0FBQyxFQUFFLEtBQUssQ0FBQyxDQUFDO0lBQ2hDLENBQUM7SUFFRDs7Ozs7O09BTUc7SUFDSCxZQUFZLENBQUMsSUFBWTs7UUFDdkIsTUFBTSxVQUFVLEdBQUcsVUFBSSxDQUFDLE9BQU8sMENBQUUsVUFBVSxDQUFDO1FBQzVDLElBQUksVUFBVSxFQUFFO1lBQ2QsTUFBTSxJQUFJLEdBQUcsVUFBVSxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsR0FBRyxDQUFDLE1BQU0sQ0FBYSxDQUFDO1lBQy9ELElBQUksSUFBSSxFQUFFO2dCQUNSLE9BQU8sSUFBSSxDQUFDLFFBQVEsQ0FBQyxJQUFJLENBQUMsQ0FBQzthQUM1QjtTQUNGO1FBQ0QsT0FBTyxLQUFLLENBQUM7SUFDZixDQUFDO0lBRUQ7Ozs7T0FJRztJQUNILE1BQU0sQ0FBQyxJQUFZOztRQUNqQixNQUFNLElBQUksR0FBRyxVQUFJLENBQUMsT0FBTywwQ0FBRSxVQUFVLENBQUM7UUFDdEMsSUFBSSxJQUFJLEVBQUU7WUFDUixNQUFNLE9BQU8sR0FBRztnQkFDZCxHQUFHLENBQUMsTUFBQyxJQUFJLENBQUMsS0FBSyxDQUFDLFFBQVEsQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFjLG1DQUFJLEVBQUUsQ0FBQzthQUN6RCxDQUFDO1lBQ0YsSUFBSSxTQUFTLEdBQUcsSUFBSSxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsQ0FBQztZQUNyQyxTQUFTLEdBQUcsU0FBUyxDQUFDLE1BQU0sQ0FBQyxHQUFHLENBQUMsRUFBRSxDQUFDLEdBQUcsS0FBSyxFQUFFLElBQUksQ0FBQyxPQUFPLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUM7WUFDMUUsSUFBSSxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsR0FBRyxDQUFDLE1BQU0sRUFBRSxPQUFPLENBQUMsTUFBTSxDQUFDLFNBQVMsQ0FBQyxDQUFDLENBQUM7WUFDM0QsSUFBSSxDQUFDLFdBQVcsRUFBRSxDQUFDO1lBQ25CLElBQUksQ0FBQyxjQUFjLEVBQUUsQ0FBQztTQUN2QjtJQUNILENBQUM7SUFFRDs7OztPQUlHO0lBQ0gsU0FBUyxDQUFDLElBQVk7O1FBQ3BCLE1BQU0sSUFBSSxHQUFHLFVBQUksQ0FBQyxPQUFPLDBDQUFFLFVBQVUsQ0FBQztRQUN0QyxJQUFJLElBQUksRUFBRTtZQUNSLE1BQU0sT0FBTyxHQUFHO2dCQUNkLEdBQUcsQ0FBQyxNQUFDLElBQUksQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQWMsbUNBQUksRUFBRSxDQUFDO2FBQ3pELENBQUM7WUFDRixJQUFJLElBQUksR0FBRyxPQUFPLENBQUMsTUFBTSxDQUFDLEdBQUcsQ0FBQyxFQUFFLENBQUMsR0FBRyxLQUFLLElBQUksQ0FBQyxDQUFDO1lBQy9DLElBQUksQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxNQUFNLEVBQUUsSUFBSSxDQUFDLENBQUM7WUFDdEMsSUFBSSxJQUFJLENBQUMsTUFBTSxLQUFLLENBQUMsRUFBRTtnQkFDckIsSUFBSSxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsTUFBTSxDQUFDLE1BQU0sQ0FBQyxDQUFDO2FBQ3BDO1lBQ0QsSUFBSSxDQUFDLFdBQVcsRUFBRSxDQUFDO1lBQ25CLElBQUksQ0FBQyxjQUFjLEVBQUUsQ0FBQztTQUN2QjtJQUNILENBQUM7SUFFRDs7O09BR0c7SUFDSCxjQUFjO1FBQ1osTUFBTSxNQUFNLEdBQUcsSUFBSSxDQUFDLE1BQXFCLENBQUM7UUFDMUMsS0FBSyxNQUFNLE1BQU0sSUFBSSxNQUFNLENBQUMsT0FBTyxFQUFFO1lBQ25DLE1BQU0sQ0FBQyxNQUFNLEVBQUUsQ0FBQztTQUNqQjtJQUNILENBQUM7SUFFRDs7O09BR0c7SUFDSCxRQUFROztRQUNOLE1BQU0sUUFBUSxHQUFHLFVBQUksQ0FBQyxPQUFPLDBDQUFFLGFBQWEsQ0FBQztRQUM3QyxNQUFNLEtBQUssR0FBRyxvQkFBUSxhQUFSLFFBQVEsdUJBQVIsUUFBUSxDQUFFLEtBQUssMENBQUUsS0FBSyxtQ0FBSSxFQUFFLENBQUM7UUFDM0MsTUFBTSxPQUFPLEdBQUcseURBQU0sQ0FDcEIsS0FBSyxFQUNMLENBQUMsT0FBaUIsRUFBRSxJQUFJLEVBQUUsRUFBRTs7WUFDMUIsTUFBTSxJQUFJLEdBQUcsTUFBQyxJQUFJLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQWMsbUNBQUksRUFBRSxDQUFDO1lBQzNELE9BQU8sQ0FBQyxHQUFHLE9BQU8sRUFBRSxHQUFHLElBQUksQ0FBQyxDQUFDO1FBQy9CLENBQUMsRUFDRCxFQUFFLENBQ0gsQ0FBQztRQUNGLElBQUksQ0FBQyxPQUFPLEdBQUcsQ0FBQyxHQUFHLElBQUksR0FBRyxDQUFDLE9BQU8sQ0FBQyxDQUFDLENBQUMsTUFBTSxDQUFDLEdBQUcsQ0FBQyxFQUFFLENBQUMsR0FBRyxLQUFLLEVBQUUsQ0FBQyxDQUFDO0lBQ2pFLENBQUM7SUFFRDs7O09BR0c7SUFDSCxXQUFXO1FBQ1QsSUFBSSxDQUFDLFFBQVEsRUFBRSxDQUFDO1FBQ2hCLE1BQU0sTUFBTSxHQUFHLElBQUksQ0FBQyxNQUFxQixDQUFDO1FBQzFDLE1BQU0sVUFBVSxHQUFHLE1BQU0sQ0FBQyxPQUFPLENBQUMsTUFBTSxDQUFDLENBQUMsQ0FBQyxFQUFFLENBQUMsQ0FBQyxDQUFDLEVBQUUsS0FBSyxTQUFTLENBQUMsQ0FBQztRQUNsRSxVQUFVLENBQUMsT0FBTyxDQUFDLE1BQU0sQ0FBQyxFQUFFO1lBQzFCLElBQUksQ0FBQyxJQUFJLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBRSxNQUFvQixDQUFDLElBQUksQ0FBQyxFQUFFO2dCQUN0RCxNQUFNLENBQUMsT0FBTyxFQUFFLENBQUM7YUFDbEI7UUFDSCxDQUFDLENBQUMsQ0FBQztRQUNILE1BQU0sY0FBYyxHQUFHLFVBQVUsQ0FBQyxHQUFHLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBRSxDQUFlLENBQUMsSUFBSSxDQUFDLENBQUM7UUFDbEUsSUFBSSxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUMsR0FBRyxDQUFDLEVBQUU7WUFDekIsSUFBSSxDQUFDLGNBQWMsQ0FBQyxRQUFRLENBQUMsR0FBRyxDQUFDLEVBQUU7Z0JBQ2pDLE1BQU0sR0FBRyxHQUFHLE1BQU0sQ0FBQyxPQUFPLENBQUMsTUFBTSxHQUFHLENBQUMsQ0FBQztnQkFDdEMsTUFBTSxDQUFDLFlBQVksQ0FBQyxHQUFHLEVBQUUsSUFBSSw4Q0FBUyxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUM7YUFDOUM7UUFDSCxDQUFDLENBQUMsQ0FBQztJQUNMLENBQUM7SUFFRDs7O09BR0c7SUFDSCxZQUFZLENBQUMsSUFBVSxFQUFFLElBQWM7UUFDckMsSUFBSSxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUMsR0FBRyxDQUFDLEVBQUUsQ0FBQyxPQUFPLEdBQUcsS0FBSyxRQUFRLENBQUMsQ0FBQztRQUNuRCxJQUFJLEdBQUcseURBQU0sQ0FDWCxJQUFJLEVBQ0osQ0FBQyxPQUFpQixFQUFFLEdBQUcsRUFBRSxFQUFFO1lBQ3pCLE9BQU8sQ0FBQyxHQUFHLE9BQU8sRUFBRSxHQUFHLEdBQUcsQ0FBQyxLQUFLLENBQUMsUUFBUSxDQUFDLENBQUMsQ0FBQztRQUM5QyxDQUFDLEVBQ0QsRUFBRSxDQUNILENBQUM7UUFDRixNQUFNLFNBQVMsR0FBRyxDQUFDLEdBQUcsSUFBSSxHQUFHLENBQUMsSUFBSSxDQUFDLENBQUMsQ0FBQyxNQUFNLENBQUMsR0FBRyxDQUFDLEVBQUUsQ0FBQyxHQUFHLEtBQUssRUFBRSxDQUFDLENBQUM7UUFDL0QsSUFBSSxDQUFDLEtBQUssQ0FBQyxRQUFRLENBQUMsR0FBRyxDQUFDLE1BQU0sRUFBRSxTQUFTLENBQUMsQ0FBQztRQUMzQyxJQUFJLENBQUMsV0FBVyxFQUFFLENBQUM7UUFDbkIsSUFBSSxDQUFDLGNBQWMsRUFBRSxDQUFDO0lBQ3hCLENBQUM7SUFFRDs7T0FFRztJQUNPLG1CQUFtQjtRQUMzQixJQUFJLENBQUMsY0FBYyxFQUFFLENBQUM7SUFDeEIsQ0FBQztJQUVEOztPQUVHO0lBQ08sV0FBVztRQUNuQixJQUFJLENBQUMsV0FBVyxFQUFFLENBQUM7UUFDbkIsSUFBSSxDQUFDLGNBQWMsRUFBRSxDQUFDO0lBQ3hCLENBQUM7SUFFRDs7O09BR0c7SUFDTyxhQUFhLENBQUMsR0FBWTtRQUNsQyxJQUFJLENBQUMsSUFBSSxDQUFDLEtBQUssRUFBRTtZQUNmLE1BQU0sS0FBSyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLENBQUM7WUFDOUMsS0FBSyxDQUFDLFdBQVcsR0FBRyxJQUFJLENBQUMsTUFBTSxDQUFDLEVBQUUsQ0FBQyxXQUFXLENBQUMsQ0FBQztZQUNoRCxLQUFLLENBQUMsU0FBUyxHQUFHLFdBQVcsQ0FBQztZQUM5QixJQUFJLENBQUMsTUFBTyxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsS0FBSyxFQUFFLElBQUksQ0FBQyxJQUFJLENBQUMsQ0FBQztZQUNqRCxJQUFJLENBQUMsS0FBSyxHQUFHLElBQUksQ0FBQztTQUNuQjtRQUNELElBQUksQ0FBQyxnQkFBZ0IsRUFBRSxDQUFDO1FBQ3hCLEtBQUssQ0FBQyxhQUFhLENBQUMsR0FBRyxDQUFDLENBQUM7SUFDM0IsQ0FBQztJQUVEOztPQUVHO0lBQ08sY0FBYyxDQUFDLEdBQVk7UUFDbkMsS0FBSyxDQUFDLGNBQWMsQ0FBQyxHQUFHLENBQUMsQ0FBQztRQUMxQix3RUFBeUIsQ0FBQyxJQUFJLENBQUMsQ0FBQztJQUNsQyxDQUFDO0lBRUQ7O09BRUc7SUFDTywyQkFBMkI7UUFDbkMsTUFBTSxJQUFJLEdBQUcsSUFBSSxDQUFDLE9BQU8sQ0FBQyxVQUFXLENBQUMsS0FBSyxDQUFDLFFBQVEsQ0FBQyxHQUFHLENBQ3RELE1BQU0sQ0FDSyxDQUFDO1FBQ2QsSUFBSSxPQUFPLEdBQWEsRUFBRSxDQUFDO1FBQzNCLElBQUksSUFBSSxFQUFFO1lBQ1IsSUFBSSxPQUFPLElBQUksS0FBSyxRQUFRLEVBQUU7Z0JBQzVCLE9BQU8sQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7YUFDcEI7aUJBQU07Z0JBQ0wsT0FBTyxHQUFHLElBQWdCLENBQUM7YUFDNUI7U0FDRjtRQUNELElBQUksQ0FBQyxZQUFZLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQyxVQUFXLEVBQUUsT0FBTyxDQUFDLENBQUM7SUFDdkQsQ0FBQztJQUVEOztPQUVHO0lBQ08sZ0JBQWdCO1FBQ3hCLHdFQUF5QixDQUFDLElBQUksQ0FBQyxDQUFDO1FBQ2hDLElBQUksQ0FBQyxPQUFPLENBQUMsY0FBYyxDQUFDLE9BQU8sQ0FBQyxJQUFJLENBQUMsZ0JBQWdCLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDakUsSUFBSSxJQUFJLENBQUMsT0FBTyxDQUFDLGFBQWEsRUFBRTtZQUM5QixLQUFLLElBQUksQ0FBQyxPQUFPLENBQUMsYUFBYSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLEdBQUcsRUFBRTtnQkFDdEQsSUFBSSxDQUFDLE9BQU8sRUFBRSxDQUFDO1lBQ2pCLENBQUMsQ0FBQyxDQUFDO1lBQ0gsSUFBSSxDQUFDLE9BQU8sQ0FBQyxhQUFhLENBQUMsS0FBTSxDQUFDLEtBQUssQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUNyRCxJQUFJLENBQUMsT0FBTyxFQUNaLElBQUksQ0FDTCxDQUFDO1lBQ0YsSUFBSSxDQUFDLE9BQU8sQ0FBQyxhQUFhLENBQUMsT0FBTyxDQUFDLGlCQUFpQixDQUFDLE9BQU8sQ0FDMUQsSUFBSSxDQUFDLE9BQU8sRUFDWixJQUFJLENBQ0wsQ0FBQztTQUNIO1FBQ0QsSUFBSSxDQUFDLE9BQU8sRUFBRSxDQUFDO0lBQ2pCLENBQUM7SUFFRDs7T0FFRztJQUNPLE9BQU87UUFDZixJQUFJLENBQUMsV0FBVyxFQUFFLENBQUM7UUFDbkIsSUFBSSxDQUFDLGNBQWMsRUFBRSxDQUFDO0lBQ3hCLENBQUM7Q0FPRjs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQ2xSRDs7O0dBR0c7QUFFbUQ7QUFDYjtBQUd6Qzs7R0FFRztBQUNJLE1BQU0sU0FBVSxTQUFRLG1EQUFNO0lBQ25DOztPQUVHO0lBQ0gsWUFBWSxJQUFZO1FBQ3RCLEtBQUssRUFBRSxDQUFDO1FBdUlILFdBQU0sR0FBbUIsSUFBSSxDQUFDO1FBdEluQyxJQUFJLENBQUMsT0FBTyxHQUFHLElBQUksQ0FBQztRQUNwQixJQUFJLENBQUMsSUFBSSxHQUFHLElBQUksQ0FBQztRQUNqQixJQUFJLENBQUMsUUFBUSxDQUFDLEtBQUssQ0FBQyxDQUFDO1FBQ3JCLElBQUksQ0FBQyxRQUFRLEVBQUUsQ0FBQztJQUNsQixDQUFDO0lBRUQ7O09BRUc7SUFDSCxRQUFRO1FBQ04sTUFBTSxJQUFJLEdBQUcsUUFBUSxDQUFDLGFBQWEsQ0FBQyxNQUFNLENBQUMsQ0FBQztRQUM1QyxJQUFJLENBQUMsV0FBVyxHQUFHLElBQUksQ0FBQyxJQUFJLENBQUM7UUFDN0IsSUFBSSxDQUFDLEtBQUssQ0FBQyxZQUFZLEdBQUcsVUFBVSxDQUFDO1FBQ3JDLE1BQU0sR0FBRyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsS0FBSyxDQUFDLENBQUM7UUFDMUMsR0FBRyxDQUFDLFNBQVMsR0FBRyxZQUFZLENBQUM7UUFDN0IsR0FBRyxDQUFDLFdBQVcsQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUN0QixNQUFNLGFBQWEsR0FBRyx3RUFBaUIsQ0FBQztZQUN0QyxHQUFHLEVBQUUsTUFBTTtZQUNYLGVBQWUsRUFBRSxRQUFRO1lBQ3pCLE1BQU0sRUFBRSxNQUFNO1lBQ2QsS0FBSyxFQUFFLE1BQU07WUFDYixVQUFVLEVBQUUsS0FBSztZQUNqQixXQUFXLEVBQUUsTUFBTTtTQUNwQixDQUFDLENBQUM7UUFDSCxJQUFJLElBQUksQ0FBQyxPQUFPLEVBQUU7WUFDaEIsSUFBSSxDQUFDLFFBQVEsQ0FBQyxhQUFhLENBQUMsQ0FBQztTQUM5QjthQUFNO1lBQ0wsSUFBSSxDQUFDLFFBQVEsQ0FBQyxlQUFlLENBQUMsQ0FBQztZQUMvQixhQUFhLENBQUMsS0FBSyxDQUFDLE9BQU8sR0FBRyxNQUFNLENBQUM7U0FDdEM7UUFDRCxHQUFHLENBQUMsV0FBVyxDQUFDLGFBQWEsQ0FBQyxDQUFDO1FBQy9CLElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLEdBQUcsQ0FBQyxDQUFDO0lBQzdCLENBQUM7SUFFRDs7T0FFRztJQUNILGFBQWE7UUFDWCxJQUFJLENBQUMsSUFBSSxDQUFDLGdCQUFnQixDQUFDLFdBQVcsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUM5QyxJQUFJLENBQUMsSUFBSSxDQUFDLGdCQUFnQixDQUFDLFdBQVcsRUFBRSxJQUFJLENBQUMsQ0FBQztRQUM5QyxJQUFJLENBQUMsSUFBSSxDQUFDLGdCQUFnQixDQUFDLFVBQVUsRUFBRSxJQUFJLENBQUMsQ0FBQztJQUMvQyxDQUFDO0lBRUQ7O09BRUc7SUFDSCxjQUFjO1FBQ1osSUFBSSxDQUFDLElBQUksQ0FBQyxtQkFBbUIsQ0FBQyxXQUFXLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDakQsSUFBSSxDQUFDLElBQUksQ0FBQyxtQkFBbUIsQ0FBQyxXQUFXLEVBQUUsSUFBSSxDQUFDLENBQUM7UUFDakQsSUFBSSxDQUFDLElBQUksQ0FBQyxtQkFBbUIsQ0FBQyxVQUFVLEVBQUUsSUFBSSxDQUFDLENBQUM7SUFDbEQsQ0FBQztJQUVEOzs7Ozs7Ozs7T0FTRztJQUNILFdBQVcsQ0FBQyxLQUFZO1FBQ3RCLFFBQVEsS0FBSyxDQUFDLElBQUksRUFBRTtZQUNsQixLQUFLLFdBQVc7Z0JBQ2QsSUFBSSxDQUFDLFNBQVMsRUFBRSxDQUFDO2dCQUNqQixNQUFNO1lBQ1IsS0FBSyxXQUFXO2dCQUNkLElBQUksQ0FBQyxhQUFhLEVBQUUsQ0FBQztnQkFDckIsTUFBTTtZQUNSLEtBQUssVUFBVTtnQkFDYixJQUFJLENBQUMsWUFBWSxFQUFFLENBQUM7Z0JBQ3BCLE1BQU07WUFDUjtnQkFDRSxNQUFNO1NBQ1Q7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxlQUFlOztRQUNiLE1BQU0sT0FBTyxHQUFHLFVBQUksQ0FBQyxNQUFNLDBDQUFFLFlBQVksQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7UUFDckQsSUFBSSxPQUFPLEtBQUssSUFBSSxDQUFDLE9BQU8sRUFBRTtZQUM1QixJQUFJLENBQUMsYUFBYSxFQUFFLENBQUM7U0FDdEI7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxhQUFhOztRQUNYLElBQUksSUFBSSxDQUFDLE9BQU8sRUFBRTtZQUNoQixJQUFJLENBQUMsV0FBVyxDQUFDLGFBQWEsQ0FBQyxDQUFDO1lBQ2hDLENBQUMsVUFBSSxDQUFDLElBQUksQ0FBQyxVQUFVLDBDQUFFLFNBQTZCLEVBQUMsS0FBSyxDQUFDLE9BQU87Z0JBQ2hFLE1BQU0sQ0FBQztZQUNULElBQUksQ0FBQyxRQUFRLENBQUMsZUFBZSxDQUFDLENBQUM7U0FDaEM7YUFBTTtZQUNMLElBQUksQ0FBQyxXQUFXLENBQUMsZUFBZSxDQUFDLENBQUM7WUFDbEMsQ0FBQyxVQUFJLENBQUMsSUFBSSxDQUFDLFVBQVUsMENBQUUsU0FBNkIsRUFBQyxLQUFLLENBQUMsT0FBTztnQkFDaEUsY0FBYyxDQUFDO1lBQ2pCLElBQUksQ0FBQyxRQUFRLENBQUMsYUFBYSxDQUFDLENBQUM7U0FDOUI7UUFDRCxJQUFJLENBQUMsT0FBTyxHQUFHLENBQUMsSUFBSSxDQUFDLE9BQU8sQ0FBQztJQUMvQixDQUFDO0lBRUQ7O09BRUc7SUFDSyxTQUFTOztRQUNmLElBQUksSUFBSSxDQUFDLE9BQU8sRUFBRTtZQUNoQixVQUFJLENBQUMsTUFBTSwwQ0FBRSxTQUFTLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxDQUFDO1NBQ25DO2FBQU07WUFDTCxVQUFJLENBQUMsTUFBTSwwQ0FBRSxNQUFNLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxDQUFDO1NBQ2hDO1FBQ0QsSUFBSSxDQUFDLGFBQWEsRUFBRSxDQUFDO0lBQ3ZCLENBQUM7SUFFRDs7T0FFRztJQUNLLGFBQWE7UUFDbEIsSUFBSSxDQUFDLElBQW9CLENBQUMsU0FBUyxDQUFDLEdBQUcsQ0FBQyxXQUFXLENBQUMsQ0FBQztJQUN4RCxDQUFDO0lBRUQ7O09BRUc7SUFDSyxZQUFZO1FBQ2pCLElBQUksQ0FBQyxJQUFvQixDQUFDLFNBQVMsQ0FBQyxNQUFNLENBQUMsV0FBVyxDQUFDLENBQUM7SUFDM0QsQ0FBQztDQUtGIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NlbGx0YWdzL3NyYy9hZGR3aWRnZXQudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NlbGx0YWdzL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY2VsbHRhZ3Mvc3JjL3Rvb2wudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NlbGx0YWdzL3NyYy93aWRnZXQudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLypcbiAqIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuICogRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbiAqL1xuXG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IGFkZEljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBUYWdUb29sIH0gZnJvbSAnLi90b29sJztcblxuLyoqXG4gKiBBIHdpZGdldCB3aGljaCBob3N0cyBhIGNlbGwgdGFncyBhcmVhLlxuICovXG5leHBvcnQgY2xhc3MgQWRkV2lkZ2V0IGV4dGVuZHMgV2lkZ2V0IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyB0YWcgd2lkZ2V0LlxuICAgKi9cbiAgY29uc3RydWN0b3IodHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLnRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLmFkZENsYXNzKCd0YWcnKTtcbiAgICB0aGlzLmVkaXRpbmcgPSBmYWxzZTtcbiAgICB0aGlzLmJ1aWxkVGFnKCk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGlucHV0IGJveCB3aXRoIGljb24gYW5kIGF0dGFjaCB0byB0aGlzLm5vZGUuXG4gICAqL1xuICBidWlsZFRhZygpOiB2b2lkIHtcbiAgICBjb25zdCB0ZXh0ID0gdGhpcy5pbnB1dCB8fCBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdpbnB1dCcpO1xuICAgIHRleHQudmFsdWUgPSB0aGlzLl90cmFucy5fXygnQWRkIFRhZycpO1xuICAgIHRleHQuY29udGVudEVkaXRhYmxlID0gJ3RydWUnO1xuICAgIHRleHQuY2xhc3NOYW1lID0gJ2FkZC10YWcnO1xuICAgIHRleHQuc3R5bGUud2lkdGggPSAnNDlweCc7XG4gICAgdGhpcy5pbnB1dCA9IHRleHQ7XG4gICAgY29uc3QgdGFnID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgdGFnLmNsYXNzTmFtZSA9ICd0YWctaG9sZGVyJztcbiAgICB0YWcuYXBwZW5kQ2hpbGQodGV4dCk7XG4gICAgY29uc3QgaWNvbkNvbnRhaW5lciA9IGFkZEljb24uZWxlbWVudCh7XG4gICAgICB0YWc6ICdzcGFuJyxcbiAgICAgIGVsZW1lbnRQb3NpdGlvbjogJ2NlbnRlcicsXG4gICAgICBoZWlnaHQ6ICcxOHB4JyxcbiAgICAgIHdpZHRoOiAnMThweCcsXG4gICAgICBtYXJnaW5MZWZ0OiAnM3B4JyxcbiAgICAgIG1hcmdpblJpZ2h0OiAnLTVweCdcbiAgICB9KTtcbiAgICB0aGlzLmFkZENsYXNzKCd1bmFwcGxpZWQtdGFnJyk7XG4gICAgdGFnLmFwcGVuZENoaWxkKGljb25Db250YWluZXIpO1xuICAgIHRoaXMubm9kZS5hcHBlbmRDaGlsZCh0YWcpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYWZ0ZXItYXR0YWNoYCBtZXNzYWdlcyBmb3IgdGhlIHdpZGdldC5cbiAgICovXG4gIG9uQWZ0ZXJBdHRhY2goKTogdm9pZCB7XG4gICAgdGhpcy5ub2RlLmFkZEV2ZW50TGlzdGVuZXIoJ21vdXNlZG93bicsIHRoaXMpO1xuICAgIHRoaXMuaW5wdXQuYWRkRXZlbnRMaXN0ZW5lcigna2V5ZG93bicsIHRoaXMpO1xuICAgIHRoaXMuaW5wdXQuYWRkRXZlbnRMaXN0ZW5lcignZm9jdXMnLCB0aGlzKTtcbiAgICB0aGlzLmlucHV0LmFkZEV2ZW50TGlzdGVuZXIoJ2JsdXInLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYGJlZm9yZS1kZXRhY2hgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgb25CZWZvcmVEZXRhY2goKTogdm9pZCB7XG4gICAgdGhpcy5ub2RlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ21vdXNlZG93bicsIHRoaXMpO1xuICAgIHRoaXMuaW5wdXQucmVtb3ZlRXZlbnRMaXN0ZW5lcigna2V5ZG93bicsIHRoaXMpO1xuICAgIHRoaXMuaW5wdXQucmVtb3ZlRXZlbnRMaXN0ZW5lcignZm9jdXMnLCB0aGlzKTtcbiAgICB0aGlzLmlucHV0LnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2JsdXInLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtIFRoZSBET00gZXZlbnQgc2VudCB0byB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgbWV0aG9kIGltcGxlbWVudHMgdGhlIERPTSBgRXZlbnRMaXN0ZW5lcmAgaW50ZXJmYWNlIGFuZCBpc1xuICAgKiBjYWxsZWQgaW4gcmVzcG9uc2UgdG8gZXZlbnRzIG9uIHRoZSBkb2NrIHBhbmVsJ3Mgbm9kZS4gSXQgc2hvdWxkXG4gICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgKi9cbiAgaGFuZGxlRXZlbnQoZXZlbnQ6IEV2ZW50KTogdm9pZCB7XG4gICAgc3dpdGNoIChldmVudC50eXBlKSB7XG4gICAgICBjYXNlICdtb3VzZWRvd24nOlxuICAgICAgICB0aGlzLl9ldnRNb3VzZURvd24oZXZlbnQgYXMgTW91c2VFdmVudCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAna2V5ZG93bic6XG4gICAgICAgIHRoaXMuX2V2dEtleURvd24oZXZlbnQgYXMgS2V5Ym9hcmRFdmVudCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnYmx1cic6XG4gICAgICAgIHRoaXMuX2V2dEJsdXIoKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdmb2N1cyc6XG4gICAgICAgIHRoaXMuX2V2dEZvY3VzKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgYnJlYWs7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgYCdtb3VzZWRvd24nYCBldmVudCBmb3IgdGhlIGlucHV0IGJveC5cbiAgICpcbiAgICogQHBhcmFtIGV2ZW50IC0gVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXRcbiAgICovXG4gIHByaXZhdGUgX2V2dE1vdXNlRG93bihldmVudDogTW91c2VFdmVudCkge1xuICAgIGlmICghdGhpcy5lZGl0aW5nKSB7XG4gICAgICB0aGlzLmVkaXRpbmcgPSB0cnVlO1xuICAgICAgdGhpcy5pbnB1dC52YWx1ZSA9ICcnO1xuICAgICAgdGhpcy5pbnB1dC5mb2N1cygpO1xuICAgIH0gZWxzZSBpZiAoZXZlbnQudGFyZ2V0ICE9PSB0aGlzLmlucHV0KSB7XG4gICAgICBpZiAodGhpcy5pbnB1dC52YWx1ZSAhPT0gJycpIHtcbiAgICAgICAgY29uc3QgdmFsdWUgPSB0aGlzLmlucHV0LnZhbHVlO1xuICAgICAgICAodGhpcy5wYXJlbnQgYXMgVGFnVG9vbCkuYWRkVGFnKHZhbHVlKTtcbiAgICAgICAgdGhpcy5pbnB1dC5ibHVyKCk7XG4gICAgICAgIHRoaXMuX2V2dEJsdXIoKTtcbiAgICAgIH1cbiAgICB9XG4gICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGAnZm9jdXMnYCBldmVudCBmb3IgdGhlIGlucHV0IGJveC5cbiAgICovXG4gIHByaXZhdGUgX2V2dEZvY3VzKCkge1xuICAgIGlmICghdGhpcy5lZGl0aW5nKSB7XG4gICAgICB0aGlzLmlucHV0LmJsdXIoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBgJ2tleWRvd24nYCBldmVudCBmb3IgdGhlIGlucHV0IGJveC5cbiAgICpcbiAgICogQHBhcmFtIGV2ZW50IC0gVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXRcbiAgICovXG4gIHByaXZhdGUgX2V2dEtleURvd24oZXZlbnQ6IEtleWJvYXJkRXZlbnQpIHtcbiAgICBjb25zdCB0bXAgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzcGFuJyk7XG4gICAgdG1wLmNsYXNzTmFtZSA9ICdhZGQtdGFnJztcbiAgICB0bXAuaW5uZXJIVE1MID0gdGhpcy5pbnB1dC52YWx1ZTtcbiAgICAvLyBzZXQgd2lkdGggdG8gdGhlIHBpeGVsIGxlbmd0aCBvZiB0aGUgdGV4dFxuICAgIGRvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQodG1wKTtcbiAgICB0aGlzLmlucHV0LnN0eWxlLndpZHRoID0gdG1wLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLndpZHRoICsgOCArICdweCc7XG4gICAgZG9jdW1lbnQuYm9keS5yZW1vdmVDaGlsZCh0bXApO1xuICAgIC8vIGlmIHRoZXkgaGl0IEVudGVyLCBhZGQgdGhlIHRhZyBhbmQgcmVzZXQgc3RhdGVcbiAgICBpZiAoZXZlbnQua2V5Q29kZSA9PT0gMTMpIHtcbiAgICAgIGNvbnN0IHZhbHVlID0gdGhpcy5pbnB1dC52YWx1ZTtcbiAgICAgICh0aGlzLnBhcmVudCBhcyBUYWdUb29sKS5hZGRUYWcodmFsdWUpO1xuICAgICAgdGhpcy5pbnB1dC5ibHVyKCk7XG4gICAgICB0aGlzLl9ldnRCbHVyKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgYCdmb2N1c291dCdgIGV2ZW50IGZvciB0aGUgaW5wdXQgYm94LlxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0Qmx1cigpIHtcbiAgICBpZiAodGhpcy5lZGl0aW5nKSB7XG4gICAgICB0aGlzLmVkaXRpbmcgPSBmYWxzZTtcbiAgICAgIHRoaXMuaW5wdXQudmFsdWUgPSB0aGlzLl90cmFucy5fXygnQWRkIFRhZycpO1xuICAgICAgdGhpcy5pbnB1dC5zdHlsZS53aWR0aCA9ICc0OXB4JztcbiAgICB9XG4gIH1cblxuICBwdWJsaWMgcGFyZW50OiBUYWdUb29sIHwgbnVsbCA9IG51bGw7XG4gIHByaXZhdGUgZWRpdGluZzogYm9vbGVhbjtcbiAgcHJpdmF0ZSBpbnB1dDogSFRNTElucHV0RWxlbWVudCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2lucHV0Jyk7XG4gIHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbiAgcHJpdmF0ZSBfdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgY2VsbHRhZ3NcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL2FkZHdpZGdldCc7XG5leHBvcnQgKiBmcm9tICcuL3Rvb2wnO1xuZXhwb3J0ICogZnJvbSAnLi93aWRnZXQnO1xuIiwiLypcbiAqIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuICogRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbiAqL1xuXG5pbXBvcnQgeyBKdXB5dGVyRnJvbnRFbmQgfSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBDZWxsIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY2VsbHMnO1xuaW1wb3J0IHsgSU5vdGVib29rVHJhY2tlciwgTm90ZWJvb2tUb29scyB9IGZyb20gJ0BqdXB5dGVybGFiL25vdGVib29rJztcbmltcG9ydCB7XG4gIElUcmFuc2xhdG9yLFxuICBudWxsVHJhbnNsYXRvcixcbiAgVHJhbnNsYXRpb25CdW5kbGVcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgcmVkdWNlIH0gZnJvbSAnQGx1bWluby9hbGdvcml0aG0nO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IFBhbmVsTGF5b3V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IEFkZFdpZGdldCB9IGZyb20gJy4vYWRkd2lkZ2V0JztcbmltcG9ydCB7IFRhZ1dpZGdldCB9IGZyb20gJy4vd2lkZ2V0JztcblxuLyoqXG4gKiBBIFRvb2wgZm9yIHRhZyBvcGVyYXRpb25zLlxuICovXG5leHBvcnQgY2xhc3MgVGFnVG9vbCBleHRlbmRzIE5vdGVib29rVG9vbHMuVG9vbCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgdGFnIFRvb2wuXG4gICAqXG4gICAqIEBwYXJhbSB0cmFja2VyIC0gVGhlIG5vdGVib29rIHRyYWNrZXIuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihcbiAgICB0cmFja2VyOiBJTm90ZWJvb2tUcmFja2VyLFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvclxuICApIHtcbiAgICBzdXBlcigpO1xuICAgIGFwcDtcbiAgICB0aGlzLnRyYW5zbGF0b3IgPSB0cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLnRyYWNrZXIgPSB0cmFja2VyO1xuICAgIHRoaXMubGF5b3V0ID0gbmV3IFBhbmVsTGF5b3V0KCk7XG4gICAgdGhpcy5jcmVhdGVUYWdJbnB1dCgpO1xuICAgIHRoaXMuYWRkQ2xhc3MoJ2pwLVRhZ1Rvb2wnKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgYW4gQWRkV2lkZ2V0IGlucHV0IGJveCB0byB0aGUgbGF5b3V0LlxuICAgKi9cbiAgY3JlYXRlVGFnSW5wdXQoKTogdm9pZCB7XG4gICAgY29uc3QgbGF5b3V0ID0gdGhpcy5sYXlvdXQgYXMgUGFuZWxMYXlvdXQ7XG4gICAgY29uc3QgaW5wdXQgPSBuZXcgQWRkV2lkZ2V0KHRoaXMudHJhbnNsYXRvcik7XG4gICAgaW5wdXQuaWQgPSAnYWRkLXRhZyc7XG4gICAgbGF5b3V0Lmluc2VydFdpZGdldCgwLCBpbnB1dCk7XG4gIH1cblxuICAvKipcbiAgICogQ2hlY2sgd2hldGhlciBhIHRhZyBpcyBhcHBsaWVkIHRvIHRoZSBjdXJyZW50IGFjdGl2ZSBjZWxsXG4gICAqXG4gICAqIEBwYXJhbSBuYW1lIC0gVGhlIG5hbWUgb2YgdGhlIHRhZy5cbiAgICpcbiAgICogQHJldHVybnMgQSBib29sZWFuIHJlcHJlc2VudGluZyB3aGV0aGVyIGl0IGlzIGFwcGxpZWQuXG4gICAqL1xuICBjaGVja0FwcGxpZWQobmFtZTogc3RyaW5nKTogYm9vbGVhbiB7XG4gICAgY29uc3QgYWN0aXZlQ2VsbCA9IHRoaXMudHJhY2tlcj8uYWN0aXZlQ2VsbDtcbiAgICBpZiAoYWN0aXZlQ2VsbCkge1xuICAgICAgY29uc3QgdGFncyA9IGFjdGl2ZUNlbGwubW9kZWwubWV0YWRhdGEuZ2V0KCd0YWdzJykgYXMgc3RyaW5nW107XG4gICAgICBpZiAodGFncykge1xuICAgICAgICByZXR1cm4gdGFncy5pbmNsdWRlcyhuYW1lKTtcbiAgICAgIH1cbiAgICB9XG4gICAgcmV0dXJuIGZhbHNlO1xuICB9XG5cbiAgLyoqXG4gICAqIEFkZCBhIHRhZyB0byB0aGUgY3VycmVudCBhY3RpdmUgY2VsbC5cbiAgICpcbiAgICogQHBhcmFtIG5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgdGFnLlxuICAgKi9cbiAgYWRkVGFnKG5hbWU6IHN0cmluZyk6IHZvaWQge1xuICAgIGNvbnN0IGNlbGwgPSB0aGlzLnRyYWNrZXI/LmFjdGl2ZUNlbGw7XG4gICAgaWYgKGNlbGwpIHtcbiAgICAgIGNvbnN0IG9sZFRhZ3MgPSBbXG4gICAgICAgIC4uLigoY2VsbC5tb2RlbC5tZXRhZGF0YS5nZXQoJ3RhZ3MnKSBhcyBzdHJpbmdbXSkgPz8gW10pXG4gICAgICBdO1xuICAgICAgbGV0IHRhZ3NUb0FkZCA9IG5hbWUuc3BsaXQoL1ssXFxzXSsvKTtcbiAgICAgIHRhZ3NUb0FkZCA9IHRhZ3NUb0FkZC5maWx0ZXIodGFnID0+IHRhZyAhPT0gJycgJiYgIW9sZFRhZ3MuaW5jbHVkZXModGFnKSk7XG4gICAgICBjZWxsLm1vZGVsLm1ldGFkYXRhLnNldCgndGFncycsIG9sZFRhZ3MuY29uY2F0KHRhZ3NUb0FkZCkpO1xuICAgICAgdGhpcy5yZWZyZXNoVGFncygpO1xuICAgICAgdGhpcy5sb2FkQWN0aXZlVGFncygpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBSZW1vdmUgYSB0YWcgZnJvbSB0aGUgY3VycmVudCBhY3RpdmUgY2VsbC5cbiAgICpcbiAgICogQHBhcmFtIG5hbWUgLSBUaGUgbmFtZSBvZiB0aGUgdGFnLlxuICAgKi9cbiAgcmVtb3ZlVGFnKG5hbWU6IHN0cmluZyk6IHZvaWQge1xuICAgIGNvbnN0IGNlbGwgPSB0aGlzLnRyYWNrZXI/LmFjdGl2ZUNlbGw7XG4gICAgaWYgKGNlbGwpIHtcbiAgICAgIGNvbnN0IG9sZFRhZ3MgPSBbXG4gICAgICAgIC4uLigoY2VsbC5tb2RlbC5tZXRhZGF0YS5nZXQoJ3RhZ3MnKSBhcyBzdHJpbmdbXSkgPz8gW10pXG4gICAgICBdO1xuICAgICAgbGV0IHRhZ3MgPSBvbGRUYWdzLmZpbHRlcih0YWcgPT4gdGFnICE9PSBuYW1lKTtcbiAgICAgIGNlbGwubW9kZWwubWV0YWRhdGEuc2V0KCd0YWdzJywgdGFncyk7XG4gICAgICBpZiAodGFncy5sZW5ndGggPT09IDApIHtcbiAgICAgICAgY2VsbC5tb2RlbC5tZXRhZGF0YS5kZWxldGUoJ3RhZ3MnKTtcbiAgICAgIH1cbiAgICAgIHRoaXMucmVmcmVzaFRhZ3MoKTtcbiAgICAgIHRoaXMubG9hZEFjdGl2ZVRhZ3MoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogVXBkYXRlIGVhY2ggdGFnIHdpZGdldCB0byByZXByZXNlbnQgd2hldGhlciBpdCBpcyBhcHBsaWVkIHRvIHRoZSBjdXJyZW50XG4gICAqIGFjdGl2ZSBjZWxsLlxuICAgKi9cbiAgbG9hZEFjdGl2ZVRhZ3MoKTogdm9pZCB7XG4gICAgY29uc3QgbGF5b3V0ID0gdGhpcy5sYXlvdXQgYXMgUGFuZWxMYXlvdXQ7XG4gICAgZm9yIChjb25zdCB3aWRnZXQgb2YgbGF5b3V0LndpZGdldHMpIHtcbiAgICAgIHdpZGdldC51cGRhdGUoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogUHVsbCBmcm9tIGNlbGwgbWV0YWRhdGEgYWxsIHRoZSB0YWdzIHVzZWQgaW4gdGhlIG5vdGVib29rIGFuZCB1cGRhdGUgdGhlXG4gICAqIHN0b3JlZCB0YWcgbGlzdC5cbiAgICovXG4gIHB1bGxUYWdzKCk6IHZvaWQge1xuICAgIGNvbnN0IG5vdGVib29rID0gdGhpcy50cmFja2VyPy5jdXJyZW50V2lkZ2V0O1xuICAgIGNvbnN0IGNlbGxzID0gbm90ZWJvb2s/Lm1vZGVsPy5jZWxscyA/PyBbXTtcbiAgICBjb25zdCBhbGxUYWdzID0gcmVkdWNlKFxuICAgICAgY2VsbHMsXG4gICAgICAoYWxsVGFnczogc3RyaW5nW10sIGNlbGwpID0+IHtcbiAgICAgICAgY29uc3QgdGFncyA9IChjZWxsLm1ldGFkYXRhLmdldCgndGFncycpIGFzIHN0cmluZ1tdKSA/PyBbXTtcbiAgICAgICAgcmV0dXJuIFsuLi5hbGxUYWdzLCAuLi50YWdzXTtcbiAgICAgIH0sXG4gICAgICBbXVxuICAgICk7XG4gICAgdGhpcy50YWdMaXN0ID0gWy4uLm5ldyBTZXQoYWxsVGFncyldLmZpbHRlcih0YWcgPT4gdGFnICE9PSAnJyk7XG4gIH1cblxuICAvKipcbiAgICogUHVsbCB0aGUgbW9zdCByZWNlbnQgbGlzdCBvZiB0YWdzIGFuZCB1cGRhdGUgdGhlIHRhZyB3aWRnZXRzIC0gZGlzcG9zZSBpZlxuICAgKiB0aGUgdGFnIG5vIGxvbmdlciBleGlzdHMsIGFuZCBjcmVhdGUgbmV3IHdpZGdldHMgZm9yIG5ldyB0YWdzLlxuICAgKi9cbiAgcmVmcmVzaFRhZ3MoKTogdm9pZCB7XG4gICAgdGhpcy5wdWxsVGFncygpO1xuICAgIGNvbnN0IGxheW91dCA9IHRoaXMubGF5b3V0IGFzIFBhbmVsTGF5b3V0O1xuICAgIGNvbnN0IHRhZ1dpZGdldHMgPSBsYXlvdXQud2lkZ2V0cy5maWx0ZXIodyA9PiB3LmlkICE9PSAnYWRkLXRhZycpO1xuICAgIHRhZ1dpZGdldHMuZm9yRWFjaCh3aWRnZXQgPT4ge1xuICAgICAgaWYgKCF0aGlzLnRhZ0xpc3QuaW5jbHVkZXMoKHdpZGdldCBhcyBUYWdXaWRnZXQpLm5hbWUpKSB7XG4gICAgICAgIHdpZGdldC5kaXNwb3NlKCk7XG4gICAgICB9XG4gICAgfSk7XG4gICAgY29uc3QgdGFnV2lkZ2V0TmFtZXMgPSB0YWdXaWRnZXRzLm1hcCh3ID0+ICh3IGFzIFRhZ1dpZGdldCkubmFtZSk7XG4gICAgdGhpcy50YWdMaXN0LmZvckVhY2godGFnID0+IHtcbiAgICAgIGlmICghdGFnV2lkZ2V0TmFtZXMuaW5jbHVkZXModGFnKSkge1xuICAgICAgICBjb25zdCBpZHggPSBsYXlvdXQud2lkZ2V0cy5sZW5ndGggLSAxO1xuICAgICAgICBsYXlvdXQuaW5zZXJ0V2lkZ2V0KGlkeCwgbmV3IFRhZ1dpZGdldCh0YWcpKTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBWYWxpZGF0ZSB0aGUgJ3RhZ3MnIG9mIGNlbGwgbWV0YWRhdGEsIGVuc3VyaW5nIGl0IGlzIGEgbGlzdCBvZiBzdHJpbmdzIGFuZFxuICAgKiB0aGF0IGVhY2ggc3RyaW5nIGRvZXNuJ3QgaW5jbHVkZSBzcGFjZXMuXG4gICAqL1xuICB2YWxpZGF0ZVRhZ3MoY2VsbDogQ2VsbCwgdGFnczogc3RyaW5nW10pOiB2b2lkIHtcbiAgICB0YWdzID0gdGFncy5maWx0ZXIodGFnID0+IHR5cGVvZiB0YWcgPT09ICdzdHJpbmcnKTtcbiAgICB0YWdzID0gcmVkdWNlKFxuICAgICAgdGFncyxcbiAgICAgIChhbGxUYWdzOiBzdHJpbmdbXSwgdGFnKSA9PiB7XG4gICAgICAgIHJldHVybiBbLi4uYWxsVGFncywgLi4udGFnLnNwbGl0KC9bLFxcc10rLyldO1xuICAgICAgfSxcbiAgICAgIFtdXG4gICAgKTtcbiAgICBjb25zdCB2YWxpZFRhZ3MgPSBbLi4ubmV3IFNldCh0YWdzKV0uZmlsdGVyKHRhZyA9PiB0YWcgIT09ICcnKTtcbiAgICBjZWxsLm1vZGVsLm1ldGFkYXRhLnNldCgndGFncycsIHZhbGlkVGFncyk7XG4gICAgdGhpcy5yZWZyZXNoVGFncygpO1xuICAgIHRoaXMubG9hZEFjdGl2ZVRhZ3MoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYSBjaGFuZ2UgdG8gdGhlIGFjdGl2ZSBjZWxsLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZlQ2VsbENoYW5nZWQoKTogdm9pZCB7XG4gICAgdGhpcy5sb2FkQWN0aXZlVGFncygpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCBhbGwgdGFncyBvbmNlIGF2YWlsYWJsZS5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyU2hvdygpOiB2b2lkIHtcbiAgICB0aGlzLnJlZnJlc2hUYWdzKCk7XG4gICAgdGhpcy5sb2FkQWN0aXZlVGFncygpO1xuICB9XG5cbiAgLyoqXG4gICAqIFVwb24gYXR0YWNoLCBhZGQgbGFiZWwgaWYgaXQgZG9lc24ndCBhbHJlYWR5IGV4aXN0IGFuZCBsaXN0ZW4gZm9yIGNoYW5nZXNcbiAgICogZnJvbSB0aGUgbm90ZWJvb2sgdHJhY2tlci5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGlmICghdGhpcy5sYWJlbCkge1xuICAgICAgY29uc3QgbGFiZWwgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsYWJlbCcpO1xuICAgICAgbGFiZWwudGV4dENvbnRlbnQgPSB0aGlzLl90cmFucy5fXygnQ2VsbCBUYWdzJyk7XG4gICAgICBsYWJlbC5jbGFzc05hbWUgPSAndGFnLWxhYmVsJztcbiAgICAgIHRoaXMucGFyZW50IS5ub2RlLmluc2VydEJlZm9yZShsYWJlbCwgdGhpcy5ub2RlKTtcbiAgICAgIHRoaXMubGFiZWwgPSB0cnVlO1xuICAgIH1cbiAgICB0aGlzLm9uQ3VycmVudENoYW5nZWQoKTtcbiAgICBzdXBlci5vbkFmdGVyQXR0YWNoKG1zZyk7XG4gIH1cblxuICAvKipcbiAgICogQ2xlYXIgc2lnbmFsIGNvbm5lY3Rpb25zIGJlZm9yZSBkZXRhY2hpbmdcbiAgICovXG4gIHByb3RlY3RlZCBvbkJlZm9yZURldGFjaChtc2c6IE1lc3NhZ2UpOiB2b2lkIHtcbiAgICBzdXBlci5vbkJlZm9yZURldGFjaChtc2cpO1xuICAgIFNpZ25hbC5kaXNjb25uZWN0UmVjZWl2ZXIodGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgY2hhbmdlIHRvIGFjdGl2ZSBjZWxsIG1ldGFkYXRhLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZlQ2VsbE1ldGFkYXRhQ2hhbmdlZCgpOiB2b2lkIHtcbiAgICBjb25zdCB0YWdzID0gdGhpcy50cmFja2VyLmFjdGl2ZUNlbGwhLm1vZGVsLm1ldGFkYXRhLmdldChcbiAgICAgICd0YWdzJ1xuICAgICkgYXMgc3RyaW5nW107XG4gICAgbGV0IHRhZ2xpc3Q6IHN0cmluZ1tdID0gW107XG4gICAgaWYgKHRhZ3MpIHtcbiAgICAgIGlmICh0eXBlb2YgdGFncyA9PT0gJ3N0cmluZycpIHtcbiAgICAgICAgdGFnbGlzdC5wdXNoKHRhZ3MpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgdGFnbGlzdCA9IHRhZ3MgYXMgc3RyaW5nW107XG4gICAgICB9XG4gICAgfVxuICAgIHRoaXMudmFsaWRhdGVUYWdzKHRoaXMudHJhY2tlci5hY3RpdmVDZWxsISwgdGFnbGlzdCk7XG4gIH1cblxuICAvKipcbiAgICogQ2FsbGJhY2sgb24gY3VycmVudCB3aWRnZXQgY2hhbmdlc1xuICAgKi9cbiAgcHJvdGVjdGVkIG9uQ3VycmVudENoYW5nZWQoKTogdm9pZCB7XG4gICAgU2lnbmFsLmRpc2Nvbm5lY3RSZWNlaXZlcih0aGlzKTtcbiAgICB0aGlzLnRyYWNrZXIuY3VycmVudENoYW5nZWQuY29ubmVjdCh0aGlzLm9uQ3VycmVudENoYW5nZWQsIHRoaXMpO1xuICAgIGlmICh0aGlzLnRyYWNrZXIuY3VycmVudFdpZGdldCkge1xuICAgICAgdm9pZCB0aGlzLnRyYWNrZXIuY3VycmVudFdpZGdldC5jb250ZXh0LnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgICB0aGlzLnJlZnJlc2goKTtcbiAgICAgIH0pO1xuICAgICAgdGhpcy50cmFja2VyLmN1cnJlbnRXaWRnZXQubW9kZWwhLmNlbGxzLmNoYW5nZWQuY29ubmVjdChcbiAgICAgICAgdGhpcy5yZWZyZXNoLFxuICAgICAgICB0aGlzXG4gICAgICApO1xuICAgICAgdGhpcy50cmFja2VyLmN1cnJlbnRXaWRnZXQuY29udGVudC5hY3RpdmVDZWxsQ2hhbmdlZC5jb25uZWN0KFxuICAgICAgICB0aGlzLnJlZnJlc2gsXG4gICAgICAgIHRoaXNcbiAgICAgICk7XG4gICAgfVxuICAgIHRoaXMucmVmcmVzaCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlZnJlc2ggdGFncyBhbmQgYWN0aXZlIHN0YXR1c1xuICAgKi9cbiAgcHJvdGVjdGVkIHJlZnJlc2goKTogdm9pZCB7XG4gICAgdGhpcy5yZWZyZXNoVGFncygpO1xuICAgIHRoaXMubG9hZEFjdGl2ZVRhZ3MoKTtcbiAgfVxuXG4gIHB1YmxpYyB0cmFja2VyOiBJTm90ZWJvb2tUcmFja2VyO1xuICBwcml2YXRlIHRhZ0xpc3Q6IHN0cmluZ1tdID0gW107XG4gIHByaXZhdGUgbGFiZWw6IGJvb2xlYW4gPSBmYWxzZTtcbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG59XG4iLCIvKlxuICogQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4gKiBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuICovXG5cbmltcG9ydCB7IGNoZWNrSWNvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IFRhZ1Rvb2wgfSBmcm9tICcuL3Rvb2wnO1xuXG4vKipcbiAqIEEgd2lkZ2V0IHdoaWNoIGhvc3RzIGEgY2VsbCB0YWdzIGFyZWEuXG4gKi9cbmV4cG9ydCBjbGFzcyBUYWdXaWRnZXQgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IHRhZyB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihuYW1lOiBzdHJpbmcpIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuYXBwbGllZCA9IHRydWU7XG4gICAgdGhpcy5uYW1lID0gbmFtZTtcbiAgICB0aGlzLmFkZENsYXNzKCd0YWcnKTtcbiAgICB0aGlzLmJ1aWxkVGFnKCk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIHRhZyBkaXYgd2l0aCBpY29uIGFuZCBhdHRhY2ggdG8gdGhpcy5ub2RlLlxuICAgKi9cbiAgYnVpbGRUYWcoKTogdm9pZCB7XG4gICAgY29uc3QgdGV4dCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3NwYW4nKTtcbiAgICB0ZXh0LnRleHRDb250ZW50ID0gdGhpcy5uYW1lO1xuICAgIHRleHQuc3R5bGUudGV4dE92ZXJmbG93ID0gJ2VsbGlwc2lzJztcbiAgICBjb25zdCB0YWcgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgICB0YWcuY2xhc3NOYW1lID0gJ3RhZy1ob2xkZXInO1xuICAgIHRhZy5hcHBlbmRDaGlsZCh0ZXh0KTtcbiAgICBjb25zdCBpY29uQ29udGFpbmVyID0gY2hlY2tJY29uLmVsZW1lbnQoe1xuICAgICAgdGFnOiAnc3BhbicsXG4gICAgICBlbGVtZW50UG9zaXRpb246ICdjZW50ZXInLFxuICAgICAgaGVpZ2h0OiAnMThweCcsXG4gICAgICB3aWR0aDogJzE4cHgnLFxuICAgICAgbWFyZ2luTGVmdDogJzVweCcsXG4gICAgICBtYXJnaW5SaWdodDogJy0zcHgnXG4gICAgfSk7XG4gICAgaWYgKHRoaXMuYXBwbGllZCkge1xuICAgICAgdGhpcy5hZGRDbGFzcygnYXBwbGllZC10YWcnKTtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5hZGRDbGFzcygndW5hcHBsaWVkLXRhZycpO1xuICAgICAgaWNvbkNvbnRhaW5lci5zdHlsZS5kaXNwbGF5ID0gJ25vbmUnO1xuICAgIH1cbiAgICB0YWcuYXBwZW5kQ2hpbGQoaWNvbkNvbnRhaW5lcik7XG4gICAgdGhpcy5ub2RlLmFwcGVuZENoaWxkKHRhZyk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGBhZnRlci1hdHRhY2hgIG1lc3NhZ2VzIGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgb25BZnRlckF0dGFjaCgpOiB2b2lkIHtcbiAgICB0aGlzLm5vZGUuYWRkRXZlbnRMaXN0ZW5lcignbW91c2Vkb3duJywgdGhpcyk7XG4gICAgdGhpcy5ub2RlLmFkZEV2ZW50TGlzdGVuZXIoJ21vdXNlb3ZlcicsIHRoaXMpO1xuICAgIHRoaXMubm9kZS5hZGRFdmVudExpc3RlbmVyKCdtb3VzZW91dCcsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYmVmb3JlLWRldGFjaGAgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBvbkJlZm9yZURldGFjaCgpOiB2b2lkIHtcbiAgICB0aGlzLm5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2Vkb3duJywgdGhpcyk7XG4gICAgdGhpcy5ub2RlLnJlbW92ZUV2ZW50TGlzdGVuZXIoJ21vdXNlb3ZlcicsIHRoaXMpO1xuICAgIHRoaXMubm9kZS5yZW1vdmVFdmVudExpc3RlbmVyKCdtb3VzZW91dCcsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgRE9NIGV2ZW50cyBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIGV2ZW50IC0gVGhlIERPTSBldmVudCBzZW50IHRvIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2QgaW1wbGVtZW50cyB0aGUgRE9NIGBFdmVudExpc3RlbmVyYCBpbnRlcmZhY2UgYW5kIGlzXG4gICAqIGNhbGxlZCBpbiByZXNwb25zZSB0byBldmVudHMgb24gdGhlIGRvY2sgcGFuZWwncyBub2RlLiBJdCBzaG91bGRcbiAgICogbm90IGJlIGNhbGxlZCBkaXJlY3RseSBieSB1c2VyIGNvZGUuXG4gICAqL1xuICBoYW5kbGVFdmVudChldmVudDogRXZlbnQpOiB2b2lkIHtcbiAgICBzd2l0Y2ggKGV2ZW50LnR5cGUpIHtcbiAgICAgIGNhc2UgJ21vdXNlZG93bic6XG4gICAgICAgIHRoaXMuX2V2dENsaWNrKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbW91c2VvdmVyJzpcbiAgICAgICAgdGhpcy5fZXZ0TW91c2VPdmVyKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbW91c2VvdXQnOlxuICAgICAgICB0aGlzLl9ldnRNb3VzZU91dCgpO1xuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYHVwZGF0ZS1yZXF1ZXN0YCBtZXNzYWdlcy4gQ2hlY2sgaWYgYXBwbGllZCB0byBjdXJyZW50IGFjdGl2ZSBjZWxsLlxuICAgKi9cbiAgb25VcGRhdGVSZXF1ZXN0KCk6IHZvaWQge1xuICAgIGNvbnN0IGFwcGxpZWQgPSB0aGlzLnBhcmVudD8uY2hlY2tBcHBsaWVkKHRoaXMubmFtZSk7XG4gICAgaWYgKGFwcGxpZWQgIT09IHRoaXMuYXBwbGllZCkge1xuICAgICAgdGhpcy50b2dnbGVBcHBsaWVkKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFVwZGF0ZSBzdHlsaW5nIHRvIHJlZmxlY3Qgd2hldGhlciB0YWcgaXMgYXBwbGllZCB0byBjdXJyZW50IGFjdGl2ZSBjZWxsLlxuICAgKi9cbiAgdG9nZ2xlQXBwbGllZCgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5hcHBsaWVkKSB7XG4gICAgICB0aGlzLnJlbW92ZUNsYXNzKCdhcHBsaWVkLXRhZycpO1xuICAgICAgKHRoaXMubm9kZS5maXJzdENoaWxkPy5sYXN0Q2hpbGQgYXMgSFRNTFNwYW5FbGVtZW50KS5zdHlsZS5kaXNwbGF5ID1cbiAgICAgICAgJ25vbmUnO1xuICAgICAgdGhpcy5hZGRDbGFzcygndW5hcHBsaWVkLXRhZycpO1xuICAgIH0gZWxzZSB7XG4gICAgICB0aGlzLnJlbW92ZUNsYXNzKCd1bmFwcGxpZWQtdGFnJyk7XG4gICAgICAodGhpcy5ub2RlLmZpcnN0Q2hpbGQ/Lmxhc3RDaGlsZCBhcyBIVE1MU3BhbkVsZW1lbnQpLnN0eWxlLmRpc3BsYXkgPVxuICAgICAgICAnaW5saW5lLWJsb2NrJztcbiAgICAgIHRoaXMuYWRkQ2xhc3MoJ2FwcGxpZWQtdGFnJyk7XG4gICAgfVxuICAgIHRoaXMuYXBwbGllZCA9ICF0aGlzLmFwcGxpZWQ7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBgJ2NsaWNrJ2AgZXZlbnQgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcml2YXRlIF9ldnRDbGljaygpIHtcbiAgICBpZiAodGhpcy5hcHBsaWVkKSB7XG4gICAgICB0aGlzLnBhcmVudD8ucmVtb3ZlVGFnKHRoaXMubmFtZSk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMucGFyZW50Py5hZGRUYWcodGhpcy5uYW1lKTtcbiAgICB9XG4gICAgdGhpcy50b2dnbGVBcHBsaWVkKCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBgJ21vdXNlb3ZlcidgIGV2ZW50IGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0TW91c2VPdmVyKCkge1xuICAgICh0aGlzLm5vZGUgYXMgSFRNTEVsZW1lbnQpLmNsYXNzTGlzdC5hZGQoJ3RhZy1ob3ZlcicpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSB0aGUgYCdtb3VzZW91dCdgIGV2ZW50IGZvciB0aGUgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0TW91c2VPdXQoKSB7XG4gICAgKHRoaXMubm9kZSBhcyBIVE1MRWxlbWVudCkuY2xhc3NMaXN0LnJlbW92ZSgndGFnLWhvdmVyJyk7XG4gIH1cblxuICBwdWJsaWMgbmFtZTogc3RyaW5nO1xuICBwcml2YXRlIGFwcGxpZWQ6IGJvb2xlYW47XG4gIHB1YmxpYyBwYXJlbnQ6IFRhZ1Rvb2wgfCBudWxsID0gbnVsbDtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==