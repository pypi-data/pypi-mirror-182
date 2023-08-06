"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_tooltip_lib_index_js-_0e0c1"],{

/***/ "../../packages/tooltip/lib/index.js":
/*!*******************************************!*\
  !*** ../../packages/tooltip/lib/index.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITooltipManager": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.ITooltipManager),
/* harmony export */   "Tooltip": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_1__.Tooltip)
/* harmony export */ });
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./tokens */ "../../packages/tooltip/lib/tokens.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./widget */ "../../packages/tooltip/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module tooltip
 */




/***/ }),

/***/ "../../packages/tooltip/lib/tokens.js":
/*!********************************************!*\
  !*** ../../packages/tooltip/lib/tokens.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITooltipManager": () => (/* binding */ ITooltipManager)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The tooltip manager token.
 */
const ITooltipManager = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/tooltip:ITooltipManager');


/***/ }),

/***/ "../../packages/tooltip/lib/widget.js":
/*!********************************************!*\
  !*** ../../packages/tooltip/lib/widget.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Tooltip": () => (/* binding */ Tooltip)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * The class name added to each tooltip.
 */
const TOOLTIP_CLASS = 'jp-Tooltip';
/**
 * The class name added to the tooltip content.
 */
const CONTENT_CLASS = 'jp-Tooltip-content';
/**
 * The class added to the body when a tooltip exists on the page.
 */
const BODY_CLASS = 'jp-mod-tooltip';
/**
 * The minimum height of a tooltip widget.
 */
const MIN_HEIGHT = 20;
/**
 * The maximum height of a tooltip widget.
 */
const MAX_HEIGHT = 250;
/**
 * A flag to indicate that event handlers are caught in the capture phase.
 */
const USE_CAPTURE = true;
/**
 * A tooltip widget.
 */
class Tooltip extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    /**
     * Instantiate a tooltip.
     */
    constructor(options) {
        super();
        this._content = null;
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.PanelLayout());
        const model = new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__.MimeModel({ data: options.bundle });
        this.anchor = options.anchor;
        this.addClass(TOOLTIP_CLASS);
        this.hide();
        this._editor = options.editor;
        this._position = options.position;
        this._rendermime = options.rendermime;
        const mimeType = this._rendermime.preferredMimeType(options.bundle, 'any');
        if (!mimeType) {
            return;
        }
        this._content = this._rendermime.createRenderer(mimeType);
        this._content
            .renderModel(model)
            .then(() => this._setGeometry())
            .catch(error => console.error('tooltip rendering failed', error));
        this._content.addClass(CONTENT_CLASS);
        layout.addWidget(this._content);
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        if (this._content) {
            this._content.dispose();
            this._content = null;
        }
        super.dispose();
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
        if (this.isHidden || this.isDisposed) {
            return;
        }
        const { node } = this;
        const target = event.target;
        switch (event.type) {
            case 'keydown':
                if (node.contains(target)) {
                    return;
                }
                this.dispose();
                break;
            case 'mousedown':
                if (node.contains(target)) {
                    this.activate();
                    return;
                }
                this.dispose();
                break;
            case 'scroll':
                this._evtScroll(event);
                break;
            default:
                break;
        }
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this.node.tabIndex = 0;
        this.node.focus();
    }
    /**
     * Handle `'after-attach'` messages.
     */
    onAfterAttach(msg) {
        document.body.classList.add(BODY_CLASS);
        document.addEventListener('keydown', this, USE_CAPTURE);
        document.addEventListener('mousedown', this, USE_CAPTURE);
        this.anchor.node.addEventListener('scroll', this, USE_CAPTURE);
        this.update();
    }
    /**
     * Handle `before-detach` messages for the widget.
     */
    onBeforeDetach(msg) {
        document.body.classList.remove(BODY_CLASS);
        document.removeEventListener('keydown', this, USE_CAPTURE);
        document.removeEventListener('mousedown', this, USE_CAPTURE);
        this.anchor.node.removeEventListener('scroll', this, USE_CAPTURE);
    }
    /**
     * Handle `'update-request'` messages.
     */
    onUpdateRequest(msg) {
        if (this.isHidden) {
            this.show();
        }
        this._setGeometry();
        super.onUpdateRequest(msg);
    }
    /**
     * Handle scroll events for the widget
     */
    _evtScroll(event) {
        // All scrolls except scrolls in the actual hover box node may cause the
        // referent editor that anchors the node to move, so the only scroll events
        // that can safely be ignored are ones that happen inside the hovering node.
        if (this.node.contains(event.target)) {
            return;
        }
        this.update();
    }
    /**
     * Find the position of the first character of the current token.
     */
    _getTokenPosition() {
        const editor = this._editor;
        const cursor = editor.getCursorPosition();
        const end = editor.getOffsetAt(cursor);
        const line = editor.getLine(cursor.line);
        if (!line) {
            return;
        }
        const tokens = line.substring(0, end).split(/\W+/);
        const last = tokens[tokens.length - 1];
        const start = last ? end - last.length : end;
        return editor.getPositionAt(start);
    }
    /**
     * Set the geometry of the tooltip widget.
     */
    _setGeometry() {
        // determine position for hover box placement
        const position = this._position ? this._position : this._getTokenPosition();
        if (!position) {
            return;
        }
        const editor = this._editor;
        const anchor = editor.getCoordinateForPosition(position);
        const style = window.getComputedStyle(this.node);
        const paddingLeft = parseInt(style.paddingLeft, 10) || 0;
        // Calculate the geometry of the tooltip.
        _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.HoverBox.setGeometry({
            anchor,
            host: editor.host,
            maxHeight: MAX_HEIGHT,
            minHeight: MIN_HEIGHT,
            node: this.node,
            offset: { horizontal: -1 * paddingLeft },
            privilege: 'below',
            style: style
        });
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdG9vbHRpcF9saWJfaW5kZXhfanMtXzBlMGMxLmZkNzJjMzk1OGZmMzFmZTlmY2VmLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQUVzQjtBQUNBOzs7Ozs7Ozs7Ozs7Ozs7OztBQ1J6QiwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBS2pCO0FBRzFDOztHQUVHO0FBQ0ksTUFBTSxlQUFlLEdBQUcsSUFBSSxvREFBSyxDQUN0QyxxQ0FBcUMsQ0FDdEMsQ0FBQzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDZEYsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVOO0FBTXJCO0FBR3NCO0FBRXREOztHQUVHO0FBQ0gsTUFBTSxhQUFhLEdBQUcsWUFBWSxDQUFDO0FBRW5DOztHQUVHO0FBQ0gsTUFBTSxhQUFhLEdBQUcsb0JBQW9CLENBQUM7QUFFM0M7O0dBRUc7QUFDSCxNQUFNLFVBQVUsR0FBRyxnQkFBZ0IsQ0FBQztBQUVwQzs7R0FFRztBQUNILE1BQU0sVUFBVSxHQUFHLEVBQUUsQ0FBQztBQUV0Qjs7R0FFRztBQUNILE1BQU0sVUFBVSxHQUFHLEdBQUcsQ0FBQztBQUV2Qjs7R0FFRztBQUNILE1BQU0sV0FBVyxHQUFHLElBQUksQ0FBQztBQUV6Qjs7R0FFRztBQUNJLE1BQU0sT0FBUSxTQUFRLG1EQUFNO0lBQ2pDOztPQUVHO0lBQ0gsWUFBWSxPQUF5QjtRQUNuQyxLQUFLLEVBQUUsQ0FBQztRQTBMRixhQUFRLEdBQWlDLElBQUksQ0FBQztRQXhMcEQsTUFBTSxNQUFNLEdBQUcsQ0FBQyxJQUFJLENBQUMsTUFBTSxHQUFHLElBQUksd0RBQVcsRUFBRSxDQUFDLENBQUM7UUFDakQsTUFBTSxLQUFLLEdBQUcsSUFBSSw2REFBUyxDQUFDLEVBQUUsSUFBSSxFQUFFLE9BQU8sQ0FBQyxNQUFNLEVBQUUsQ0FBQyxDQUFDO1FBRXRELElBQUksQ0FBQyxNQUFNLEdBQUcsT0FBTyxDQUFDLE1B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USxDQUFDLEtBQUssQ0FBQyxXQUFZLEVBQUUsRUFBRSxDQUFDLElBQUksQ0FBQyxDQUFDO1FBRTFELHlDQUF5QztRQUN6QywyRUFBb0IsQ0FBQztZQUNuQixNQUFNO1lBQ04sSUFBSSxFQUFFLE1BQU0sQ0FBQyxJQUFJO1lBQ2pCLFNBQVMsRUFBRSxVQUFVO1lBQ3JCLFNBQVMsRUFBRSxVQUFVO1lBQ3JCLElBQUksRUFBRSxJQUFJLENBQUMsSUFBSTtZQUNmLE1BQU0sRUFBRSxFQUFFLFVBQVUsRUFBRSxDQUFDLENBQUMsR0FBRyxXQUFXLEVBQUU7WUFDeEMsU0FBUyxFQUFFLE9BQU87WUFDbEIsS0FBSyxFQUFFLEtBQUs7U0FDYixDQUFDLENBQUM7SUFDTCxDQUFDO0NBTUYiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdG9vbHRpcC9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3Rvb2x0aXAvc3JjL3Rva2Vucy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdG9vbHRpcC9zcmMvd2lkZ2V0LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHRvb2x0aXBcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG5leHBvcnQgKiBmcm9tICcuL3dpZGdldCc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IENvZGVFZGl0b3IgfSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7IElSZW5kZXJNaW1lUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IEtlcm5lbCB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IFRva2VuIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgdG9vbHRpcCBtYW5hZ2VyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVRvb2x0aXBNYW5hZ2VyID0gbmV3IFRva2VuPElUb29sdGlwTWFuYWdlcj4oXG4gICdAanVweXRlcmxhYi90b29sdGlwOklUb29sdGlwTWFuYWdlcidcbik7XG5cbi8qKlxuICogQSBtYW5hZ2VyIHRvIHJlZ2lzdGVyIHRvb2x0aXBzIHdpdGggcGFyZW50IHdpZGdldHMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVRvb2x0aXBNYW5hZ2VyIHtcbiAgLyoqXG4gICAqIEludm9rZSBhIHRvb2x0aXAuXG4gICAqL1xuICBpbnZva2Uob3B0aW9uczogSVRvb2x0aXBNYW5hZ2VyLklPcHRpb25zKTogdm9pZDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgYElUb29sdGlwTWFuYWdlcmAgaW50ZXJmYWNlIHNwZWNpZmljYXRpb25zLlxuICovXG5leHBvcnQgbmFtZXNwYWNlIElUb29sdGlwTWFuYWdlciB7XG4gIC8qKlxuICAgKiBBbiBpbnRlcmZhY2UgZm9yIHRvb2x0aXAtY29tcGF0aWJsZSBvYmplY3RzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHJlZmVyZW50IGFuY2hvciB0aGUgdG9vbHRpcCBmb2xsb3dzLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGFuY2hvcjogV2lkZ2V0O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHJlZmVyZW50IGVkaXRvciBmb3IgdGhlIHRvb2x0aXAuXG4gICAgICovXG4gICAgcmVhZG9ubHkgZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3I7XG5cbiAgICAvKipcbiAgICAgKiBUaGUga2VybmVsIHRoZSB0b29sdGlwIGNvbW11bmljYXRlcyB3aXRoIHRvIHBvcHVsYXRlIGl0c2VsZi5cbiAgICAgKi9cbiAgICByZWFkb25seSBrZXJuZWw6IEtlcm5lbC5JS2VybmVsQ29ubmVjdGlvbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSByZW5kZXJlciB0aGUgdG9vbHRpcCB1c2VzIHRvIHJlbmRlciBBUEkgcmVzcG9uc2VzLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSG92ZXJCb3ggfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IENvZGVFZGl0b3IgfSBmcm9tICdAanVweXRlcmxhYi9jb2RlZWRpdG9yJztcbmltcG9ydCB7XG4gIElSZW5kZXJNaW1lLFxuICBJUmVuZGVyTWltZVJlZ2lzdHJ5LFxuICBNaW1lTW9kZWxcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyBKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgTWVzc2FnZSB9IGZyb20gJ0BsdW1pbm8vbWVzc2FnaW5nJztcbmltcG9ydCB7IFBhbmVsTGF5b3V0LCBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vKipcbiAqIFRoZSBjbGFzcyBuYW1lIGFkZGVkIHRvIGVhY2ggdG9vbHRpcC5cbiAqL1xuY29uc3QgVE9PTFRJUF9DTEFTUyA9ICdqcC1Ub29sdGlwJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byB0aGUgdG9vbHRpcCBjb250ZW50LlxuICovXG5jb25zdCBDT05URU5UX0NMQVNTID0gJ2pwLVRvb2x0aXAtY29udGVudCc7XG5cbi8qKlxuICogVGhlIGNsYXNzIGFkZGVkIHRvIHRoZSBib2R5IHdoZW4gYSB0b29sdGlwIGV4aXN0cyBvbiB0aGUgcGFnZS5cbiAqL1xuY29uc3QgQk9EWV9DTEFTUyA9ICdqcC1tb2QtdG9vbHRpcCc7XG5cbi8qKlxuICogVGhlIG1pbmltdW0gaGVpZ2h0IG9mIGEgdG9vbHRpcCB3aWRnZXQuXG4gKi9cbmNvbnN0IE1JTl9IRUlHSFQgPSAyMDtcblxuLyoqXG4gKiBUaGUgbWF4aW11bSBoZWlnaHQgb2YgYSB0b29sdGlwIHdpZGdldC5cbiAqL1xuY29uc3QgTUFYX0hFSUdIVCA9IDI1MDtcblxuLyoqXG4gKiBBIGZsYWcgdG8gaW5kaWNhdGUgdGhhdCBldmVudCBoYW5kbGVycyBhcmUgY2F1Z2h0IGluIHRoZSBjYXB0dXJlIHBoYXNlLlxuICovXG5jb25zdCBVU0VfQ0FQVFVSRSA9IHRydWU7XG5cbi8qKlxuICogQSB0b29sdGlwIHdpZGdldC5cbiAqL1xuZXhwb3J0IGNsYXNzIFRvb2x0aXAgZXh0ZW5kcyBXaWRnZXQge1xuICAvKipcbiAgICogSW5zdGFudGlhdGUgYSB0b29sdGlwLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogVG9vbHRpcC5JT3B0aW9ucykge1xuICAgIHN1cGVyKCk7XG5cbiAgICBjb25zdCBsYXlvdXQgPSAodGhpcy5sYXlvdXQgPSBuZXcgUGFuZWxMYXlvdXQoKSk7XG4gICAgY29uc3QgbW9kZWwgPSBuZXcgTWltZU1vZGVsKHsgZGF0YTogb3B0aW9ucy5idW5kbGUgfSk7XG5cbiAgICB0aGlzLmFuY2hvciA9IG9wdGlvbnMuYW5jaG9yO1xuICAgIHRoaXMuYWRkQ2xhc3MoVE9PTFRJUF9DTEFTUyk7XG4gICAgdGhpcy5oaWRlKCk7XG4gICAgdGhpcy5fZWRpdG9yID0gb3B0aW9ucy5lZGl0b3I7XG4gICAgdGhpcy5fcG9zaXRpb24gPSBvcHRpb25zLnBvc2l0aW9uO1xuICAgIHRoaXMuX3JlbmRlcm1pbWUgPSBvcHRpb25zLnJlbmRlcm1pbWU7XG5cbiAgICBjb25zdCBtaW1lVHlwZSA9IHRoaXMuX3JlbmRlcm1pbWUucHJlZmVycmVkTWltZVR5cGUob3B0aW9ucy5idW5kbGUsICdhbnknKTtcblxuICAgIGlmICghbWltZVR5cGUpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICB0aGlzLl9jb250ZW50ID0gdGhpcy5fcmVuZGVybWltZS5jcmVhdGVSZW5kZXJlcihtaW1lVHlwZSk7XG4gICAgdGhpcy5fY29udGVudFxuICAgICAgLnJlbmRlck1vZGVsKG1vZGVsKVxuICAgICAgLnRoZW4oKCkgPT4gdGhpcy5fc2V0R2VvbWV0cnkoKSlcbiAgICAgIC5jYXRjaChlcnJvciA9PiBjb25zb2xlLmVycm9yKCd0b29sdGlwIHJlbmRlcmluZyBmYWlsZWQnLCBlcnJvcikpO1xuICAgIHRoaXMuX2NvbnRlbnQuYWRkQ2xhc3MoQ09OVEVOVF9DTEFTUyk7XG4gICAgbGF5b3V0LmFkZFdpZGdldCh0aGlzLl9jb250ZW50KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgYW5jaG9yIHdpZGdldCB0aGF0IHRoZSB0b29sdGlwIHdpZGdldCB0cmFja3MuXG4gICAqL1xuICByZWFkb25seSBhbmNob3I6IFdpZGdldDtcblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuX2NvbnRlbnQpIHtcbiAgICAgIHRoaXMuX2NvbnRlbnQuZGlzcG9zZSgpO1xuICAgICAgdGhpcy5fY29udGVudCA9IG51bGw7XG4gICAgfVxuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIERPTSBldmVudHMgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSBldmVudCAtIFRoZSBET00gZXZlbnQgc2VudCB0byB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgbWV0aG9kIGltcGxlbWVudHMgdGhlIERPTSBgRXZlbnRMaXN0ZW5lcmAgaW50ZXJmYWNlIGFuZCBpc1xuICAgKiBjYWxsZWQgaW4gcmVzcG9uc2UgdG8gZXZlbnRzIG9uIHRoZSBkb2NrIHBhbmVsJ3Mgbm9kZS4gSXQgc2hvdWxkXG4gICAqIG5vdCBiZSBjYWxsZWQgZGlyZWN0bHkgYnkgdXNlciBjb2RlLlxuICAgKi9cbiAgaGFuZGxlRXZlbnQoZXZlbnQ6IEV2ZW50KTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNIaWRkZW4gfHwgdGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgY29uc3QgeyBub2RlIH0gPSB0aGlzO1xuICAgIGNvbnN0IHRhcmdldCA9IGV2ZW50LnRhcmdldCBhcyBIVE1MRWxlbWVudDtcblxuICAgIHN3aXRjaCAoZXZlbnQudHlwZSkge1xuICAgICAgY2FzZSAna2V5ZG93bic6XG4gICAgICAgIGlmIChub2RlLmNvbnRhaW5zKHRhcmdldCkpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy5kaXNwb3NlKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbW91c2Vkb3duJzpcbiAgICAgICAgaWYgKG5vZGUuY29udGFpbnModGFyZ2V0KSkge1xuICAgICAgICAgIHRoaXMuYWN0aXZhdGUoKTtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgdGhpcy5kaXNwb3NlKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnc2Nyb2xsJzpcbiAgICAgICAgdGhpcy5fZXZ0U2Nyb2xsKGV2ZW50IGFzIE1vdXNlRXZlbnQpO1xuICAgICAgICBicmVhaztcbiAgICAgIGRlZmF1bHQ6XG4gICAgICAgIGJyZWFrO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYCdhY3RpdmF0ZS1yZXF1ZXN0J2AgbWVzc2FnZXMuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25BY3RpdmF0ZVJlcXVlc3QobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgdGhpcy5ub2RlLnRhYkluZGV4ID0gMDtcbiAgICB0aGlzLm5vZGUuZm9jdXMoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYCdhZnRlci1hdHRhY2gnYCBtZXNzYWdlcy5cbiAgICovXG4gIHByb3RlY3RlZCBvbkFmdGVyQXR0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGRvY3VtZW50LmJvZHkuY2xhc3NMaXN0LmFkZChCT0RZX0NMQVNTKTtcbiAgICBkb2N1bWVudC5hZGRFdmVudExpc3RlbmVyKCdrZXlkb3duJywgdGhpcywgVVNFX0NBUFRVUkUpO1xuICAgIGRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ21vdXNlZG93bicsIHRoaXMsIFVTRV9DQVBUVVJFKTtcbiAgICB0aGlzLmFuY2hvci5ub2RlLmFkZEV2ZW50TGlzdGVuZXIoJ3Njcm9sbCcsIHRoaXMsIFVTRV9DQVBUVVJFKTtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgYmVmb3JlLWRldGFjaGAgbWVzc2FnZXMgZm9yIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25CZWZvcmVEZXRhY2gobXNnOiBNZXNzYWdlKTogdm9pZCB7XG4gICAgZG9jdW1lbnQuYm9keS5jbGFzc0xpc3QucmVtb3ZlKEJPRFlfQ0xBU1MpO1xuICAgIGRvY3VtZW50LnJlbW92ZUV2ZW50TGlzdGVuZXIoJ2tleWRvd24nLCB0aGlzLCBVU0VfQ0FQVFVSRSk7XG4gICAgZG9jdW1lbnQucmVtb3ZlRXZlbnRMaXN0ZW5lcignbW91c2Vkb3duJywgdGhpcywgVVNFX0NBUFRVUkUpO1xuICAgIHRoaXMuYW5jaG9yLm5vZGUucmVtb3ZlRXZlbnRMaXN0ZW5lcignc2Nyb2xsJywgdGhpcywgVVNFX0NBUFRVUkUpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBgJ3VwZGF0ZS1yZXF1ZXN0J2AgbWVzc2FnZXMuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGlmICh0aGlzLmlzSGlkZGVuKSB7XG4gICAgICB0aGlzLnNob3coKTtcbiAgICB9XG4gICAgdGhpcy5fc2V0R2VvbWV0cnkoKTtcbiAgICBzdXBlci5vblVwZGF0ZVJlcXVlc3QobXNnKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgc2Nyb2xsIGV2ZW50cyBmb3IgdGhlIHdpZGdldFxuICAgKi9cbiAgcHJpdmF0ZSBfZXZ0U2Nyb2xsKGV2ZW50OiBNb3VzZUV2ZW50KSB7XG4gICAgLy8gQWxsIHNjcm9sbHMgZXhjZXB0IHNjcm9sbHMgaW4gdGhlIGFjdHVhbCBob3ZlciBib3ggbm9kZSBtYXkgY2F1c2UgdGhlXG4gICAgLy8gcmVmZXJlbnQgZWRpdG9yIHRoYXQgYW5jaG9ycyB0aGUgbm9kZSB0byBtb3ZlLCBzbyB0aGUgb25seSBzY3JvbGwgZXZlbnRzXG4gICAgLy8gdGhhdCBjYW4gc2FmZWx5IGJlIGlnbm9yZWQgYXJlIG9uZXMgdGhhdCBoYXBwZW4gaW5zaWRlIHRoZSBob3ZlcmluZyBub2RlLlxuICAgIGlmICh0aGlzLm5vZGUuY29udGFpbnMoZXZlbnQudGFyZ2V0IGFzIEhUTUxFbGVtZW50KSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogRmluZCB0aGUgcG9zaXRpb24gb2YgdGhlIGZpcnN0IGNoYXJhY3RlciBvZiB0aGUgY3VycmVudCB0b2tlbi5cbiAgICovXG4gIHByaXZhdGUgX2dldFRva2VuUG9zaXRpb24oKTogQ29kZUVkaXRvci5JUG9zaXRpb24gfCB1bmRlZmluZWQge1xuICAgIGNvbnN0IGVkaXRvciA9IHRoaXMuX2VkaXRvcjtcbiAgICBjb25zdCBjdXJzb3IgPSBlZGl0b3IuZ2V0Q3Vyc29yUG9zaXRpb24oKTtcbiAgICBjb25zdCBlbmQgPSBlZGl0b3IuZ2V0T2Zmc2V0QXQoY3Vyc29yKTtcbiAgICBjb25zdCBsaW5lID0gZWRpdG9yLmdldExpbmUoY3Vyc29yLmxpbmUpO1xuXG4gICAgaWYgKCFsaW5lKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgY29uc3QgdG9rZW5zID0gbGluZS5zdWJzdHJpbmcoMCwgZW5kKS5zcGxpdCgvXFxXKy8pO1xuICAgIGNvbnN0IGxhc3QgPSB0b2tlbnNbdG9rZW5zLmxlbmd0aCAtIDFdO1xuICAgIGNvbnN0IHN0YXJ0ID0gbGFzdCA/IGVuZCAtIGxhc3QubGVuZ3RoIDogZW5kO1xuICAgIHJldHVybiBlZGl0b3IuZ2V0UG9zaXRpb25BdChzdGFydCk7XG4gIH1cblxuICAvKipcbiAgICogU2V0IHRoZSBnZW9tZXRyeSBvZiB0aGUgdG9vbHRpcCB3aWRnZXQuXG4gICAqL1xuICBwcml2YXRlIF9zZXRHZW9tZXRyeSgpOiB2b2lkIHtcbiAgICAvLyBkZXRlcm1pbmUgcG9zaXRpb24gZm9yIGhvdmVyIGJveCBwbGFjZW1lbnRcbiAgICBjb25zdCBwb3NpdGlvbiA9IHRoaXMuX3Bvc2l0aW9uID8gdGhpcy5fcG9zaXRpb24gOiB0aGlzLl9nZXRUb2tlblBvc2l0aW9uKCk7XG5cbiAgICBpZiAoIXBvc2l0aW9uKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgY29uc3QgZWRpdG9yID0gdGhpcy5fZWRpdG9yO1xuXG4gICAgY29uc3QgYW5jaG9yID0gZWRpdG9yLmdldENvb3JkaW5hdGVGb3JQb3NpdGlvbihwb3NpdGlvbik7XG4gICAgY29uc3Qgc3R5bGUgPSB3aW5kb3cuZ2V0Q29tcHV0ZWRTdHlsZSh0aGlzLm5vZGUpO1xuICAgIGNvbnN0IHBhZGRpbmdMZWZ0ID0gcGFyc2VJbnQoc3R5bGUucGFkZGluZ0xlZnQhLCAxMCkgfHwgMDtcblxuICAgIC8vIENhbGN1bGF0ZSB0aGUgZ2VvbWV0cnkgb2YgdGhlIHRvb2x0aXAuXG4gICAgSG92ZXJCb3guc2V0R2VvbWV0cnkoe1xuICAgICAgYW5jaG9yLFxuICAgICAgaG9zdDogZWRpdG9yLmhvc3QsXG4gICAgICBtYXhIZWlnaHQ6IE1BWF9IRUlHSFQsXG4gICAgICBtaW5IZWlnaHQ6IE1JTl9IRUlHSFQsXG4gICAgICBub2RlOiB0aGlzLm5vZGUsXG4gICAgICBvZmZzZXQ6IHsgaG9yaXpvbnRhbDogLTEgKiBwYWRkaW5nTGVmdCB9LFxuICAgICAgcHJpdmlsZWdlOiAnYmVsb3cnLFxuICAgICAgc3R5bGU6IHN0eWxlXG4gICAgfSk7XG4gIH1cblxuICBwcml2YXRlIF9jb250ZW50OiBJUmVuZGVyTWltZS5JUmVuZGVyZXIgfCBudWxsID0gbnVsbDtcbiAgcHJpdmF0ZSBfZWRpdG9yOiBDb2RlRWRpdG9yLklFZGl0b3I7XG4gIHByaXZhdGUgX3Bvc2l0aW9uOiBDb2RlRWRpdG9yLklQb3NpdGlvbiB8IHVuZGVmaW5lZDtcbiAgcHJpdmF0ZSBfcmVuZGVybWltZTogSVJlbmRlck1pbWVSZWdpc3RyeTtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgdG9vbHRpcCB3aWRnZXQgc3RhdGljcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBUb29sdGlwIHtcbiAgLyoqXG4gICAqIEluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgYSB0b29sdGlwIHdpZGdldC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBhbmNob3Igd2lkZ2V0IHRoYXQgdGhlIHRvb2x0aXAgd2lkZ2V0IHRyYWNrcy5cbiAgICAgKi9cbiAgICBhbmNob3I6IFdpZGdldDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBkYXRhIHRoYXQgcG9wdWxhdGVzIHRoZSB0b29sdGlwIHdpZGdldC5cbiAgICAgKi9cbiAgICBidW5kbGU6IEpTT05PYmplY3Q7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgZWRpdG9yIHJlZmVyZW50IG9mIHRoZSB0b29sdGlwIG1vZGVsLlxuICAgICAqL1xuICAgIGVkaXRvcjogQ29kZUVkaXRvci5JRWRpdG9yO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHJlbmRlcm1pbWUgaW5zdGFuY2UgdXNlZCBieSB0aGUgdG9vbHRpcCBtb2RlbC5cbiAgICAgKi9cbiAgICByZW5kZXJtaW1lOiBJUmVuZGVyTWltZVJlZ2lzdHJ5O1xuXG4gICAgLyoqXG4gICAgICogUG9zaXRpb24gYXQgd2hpY2ggdGhlIHRvb2x0aXAgc2hvdWxkIGJlIHBsYWNlZC5cbiAgICAgKlxuICAgICAqIElmIG5vdCBnaXZlbiwgdGhlIHBvc2l0aW9uIG9mIHRoZSBmaXJzdCBjaGFyYWN0ZXJcbiAgICAgKiBpbiB0aGUgY3VycmVudCB0b2tlbiB3aWxsIGJlIHVzZWQuXG4gICAgICovXG4gICAgcG9zaXRpb24/OiBDb2RlRWRpdG9yLklQb3NpdGlvbjtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9