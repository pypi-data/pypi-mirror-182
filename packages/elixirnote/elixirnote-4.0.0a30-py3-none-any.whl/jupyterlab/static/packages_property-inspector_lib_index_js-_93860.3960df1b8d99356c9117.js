"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_property-inspector_lib_index_js-_93860"],{

/***/ "../../packages/property-inspector/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/property-inspector/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IPropertyInspectorProvider": () => (/* reexport safe */ _token__WEBPACK_IMPORTED_MODULE_4__.IPropertyInspectorProvider),
/* harmony export */   "SideBarPropertyInspectorProvider": () => (/* binding */ SideBarPropertyInspectorProvider)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _token__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./token */ "../../packages/property-inspector/lib/token.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module property-inspector
 */






/**
 * The implementation of the PropertyInspector.
 */
class PropertyInspectorProvider extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget {
    /**
     * Construct a new Property Inspector.
     */
    constructor() {
        super();
        this._tracker = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.FocusTracker();
        this._inspectors = new Map();
        this.addClass('jp-PropertyInspector');
        this._tracker = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.FocusTracker();
        this._tracker.currentChanged.connect(this._onCurrentChanged, this);
    }
    /**
     * Register a widget in the property inspector provider.
     *
     * @param widget The owner widget to register.
     */
    register(widget) {
        if (this._inspectors.has(widget)) {
            throw new Error('Widget is already registered');
        }
        const inspector = new Private.PropertyInspector(widget);
        widget.disposed.connect(this._onWidgetDisposed, this);
        this._inspectors.set(widget, inspector);
        inspector.onAction.connect(this._onInspectorAction, this);
        this._tracker.add(widget);
        return inspector;
    }
    /**
     * The current widget being tracked by the inspector.
     */
    get currentWidget() {
        return this._tracker.currentWidget;
    }
    /**
     * Refresh the content for the current widget.
     */
    refresh() {
        const current = this._tracker.currentWidget;
        if (!current) {
            this.setContent(null);
            return;
        }
        const inspector = this._inspectors.get(current);
        if (inspector) {
            this.setContent(inspector.content);
        }
    }
    /**
     * Handle the disposal of a widget.
     */
    _onWidgetDisposed(sender) {
        const inspector = this._inspectors.get(sender);
        if (inspector) {
            inspector.dispose();
            this._inspectors.delete(sender);
        }
    }
    /**
     * Handle inspector actions.
     */
    _onInspectorAction(sender, action) {
        const owner = sender.owner;
        const current = this._tracker.currentWidget;
        switch (action) {
            case 'content':
                if (current === owner) {
                    this.setContent(sender.content);
                }
                break;
            case 'dispose':
                if (owner) {
                    this._tracker.remove(owner);
                    this._inspectors.delete(owner);
                }
                break;
            case 'show-panel':
                if (current === owner) {
                    this.showPanel();
                }
                break;
            default:
                throw new Error('Unsupported inspector action');
        }
    }
    /**
     * Handle a change to the current widget in the tracker.
     */
    _onCurrentChanged() {
        const current = this._tracker.currentWidget;
        if (current) {
            const inspector = this._inspectors.get(current);
            const content = inspector.content;
            this.setContent(content);
        }
        else {
            this.setContent(null);
        }
    }
}
/**
 * A class that adds a property inspector provider to the
 * JupyterLab sidebar.
 */
class SideBarPropertyInspectorProvider extends PropertyInspectorProvider {
    /**
     * Construct a new Side Bar Property Inspector.
     */
    constructor(labshell, placeholder, translator) {
        super();
        this._labshell = labshell;
        this.translator = translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.SingletonLayout());
        if (placeholder) {
            this._placeholder = placeholder;
        }
        else {
            const node = document.createElement('div');
            const content = document.createElement('div');
            content.textContent = this._trans.__('No properties to inspect.');
            content.className = 'jp-PropertyInspector-placeholderContent';
            node.appendChild(content);
            this._placeholder = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget({ node });
            this._placeholder.addClass('jp-PropertyInspector-placeholder');
        }
        layout.widget = this._placeholder;
        labshell.currentChanged.connect(this._onShellCurrentChanged, this);
        this._onShellCurrentChanged();
    }
    /**
     * Set the content of the sidebar panel.
     */
    setContent(content) {
        const layout = this.layout;
        if (layout.widget) {
            layout.widget.removeClass('jp-PropertyInspector-content');
            layout.removeWidget(layout.widget);
        }
        if (!content) {
            content = this._placeholder;
        }
        content.addClass('jp-PropertyInspector-content');
        layout.widget = content;
    }
    /**
     * Show the sidebar panel.
     */
    showPanel() {
        this._labshell.activateById(this.id);
    }
    /**
     * Handle the case when the current widget is not in our tracker.
     */
    _onShellCurrentChanged() {
        const current = this.currentWidget;
        if (!current) {
            this.setContent(null);
            return;
        }
        const currentShell = this._labshell.currentWidget;
        if (currentShell === null || currentShell === void 0 ? void 0 : currentShell.node.contains(current.node)) {
            this.refresh();
        }
        else {
            this.setContent(null);
        }
    }
}
/**
 * A namespace for module private data.
 */
var Private;
(function (Private) {
    /**
     * An implementation of the property inspector used by the
     * property inspector provider.
     */
    class PropertyInspector {
        /**
         * Construct a new property inspector.
         */
        constructor(owner) {
            this._isDisposed = false;
            this._content = null;
            this._owner = null;
            this._onAction = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
            this._owner = owner;
        }
        /**
         * The owner widget for the property inspector.
         */
        get owner() {
            return this._owner;
        }
        /**
         * The current content for the property inspector.
         */
        get content() {
            return this._content;
        }
        /**
         * Whether the property inspector is disposed.
         */
        get isDisposed() {
            return this._isDisposed;
        }
        /**
         * A signal used for actions related to the property inspector.
         */
        get onAction() {
            return this._onAction;
        }
        /**
         * Show the property inspector panel.
         */
        showPanel() {
            if (this._isDisposed) {
                return;
            }
            this._onAction.emit('show-panel');
        }
        /**
         * Render the property inspector content.
         */
        render(widget) {
            if (this._isDisposed) {
                return;
            }
            if (widget instanceof _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget) {
                this._content = widget;
            }
            else {
                this._content = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.ReactWidget.create(widget);
            }
            this._onAction.emit('content');
        }
        /**
         * Dispose of the property inspector.
         */
        dispose() {
            if (this._isDisposed) {
                return;
            }
            this._isDisposed = true;
            this._content = null;
            this._owner = null;
            _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal.clearData(this);
        }
    }
    Private.PropertyInspector = PropertyInspector;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/property-inspector/lib/token.js":
/*!******************************************************!*\
  !*** ../../packages/property-inspector/lib/token.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IPropertyInspectorProvider": () => (/* binding */ IPropertyInspectorProvider)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The property inspector provider token.
 */
const IPropertyInspectorProvider = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/property-inspector:IPropertyInspectorProvider');


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfcHJvcGVydHktaW5zcGVjdG9yX2xpYl9pbmRleF9qcy1fOTM4NjAuMzk2MGRmMWI4ZDk5MzU2YzkxMTcuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQU84QjtBQUN1QjtBQUNKO0FBQ29CO0FBRUM7QUFFZjtBQUUxRDs7R0FFRztBQUNILE1BQWUseUJBQ2IsU0FBUSxtREFBTTtJQUdkOztPQUVHO0lBQ0g7UUFDRSxLQUFLLEVBQUUsQ0FBQztRQStHRixhQUFRLEdBQUcsSUFBSSx5REFBWSxFQUFFLENBQUM7UUFDOUIsZ0JBQVcsR0FBRyxJQUFJLEdBQUcsRUFBcUMsQ0FBQztRQS9HakUsSUFBSSxDQUFDLFFBQVEsQ0FBQyxzQkFBc0IsQ0FBQyxDQUFDO1FBQ3RDLElBQUksQ0FBQyxRQUFRLEdBQUcsSUFBSSx5REFBWSxFQUFFLENBQUM7UUFDbkMsSUFBSSxDQUFDLFFBQVEsQ0FBQyxjQUFjLENBQUMsT0FBTyxDQUFDLElBQUksQ0FBQyxpQkFBaUIsRUFBRSxJQUFJLENBQUMsQ0FBQztJQUNyRSxDQUFDO0lBRUQ7Ozs7T0FJRztJQUNILFFBQVEsQ0FBQyxNQUFjO1FBQ3JCLElBQUksSUFBSSxDQUFDLFdBQVcsQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDLEVBQUU7WUFDaEMsTUFBTSxJQUFJLEtBQUssQ0FBQyw4QkFBOEIsQ0FBQyxDQUFDO1NBQ2pEO1FBQ0QsTUFBTSxTQUFTLEdBQUcsSUFBSSxPQUFPLENBQUMsaUJBQWlCLENBQUMsTUFBTSxDQUFDLENBQUM7UUFDeEQsTUFBTSxDQUFDLFFBQVEsQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLGlCQUFpQixFQUFFLElBQUksQ0FBQyxDQUFDO1FBQ3RELElBQUksQ0FBQyxXQUFXLENBQUMsR0FBRyxDQUFDLE1BQU0sRUFBRSxTQUFTLENBQUMsQ0FBQztRQUN4QyxTQUFTLENBQUMsUUFBUSxDQUFDLE9BQU8s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QUN4QixJQUFJLENBQUMsUUFBUSxHQUFHLElBQUksQ0FBQztZQUNyQixJQUFJLENBQUMsTUFBTSxHQUFHLElBQUksQ0FBQztZQUNuQiwrREFBZ0IsQ0FBQyxJQUFJLENBQUMsQ0FBQztRQUN6QixDQUFDO0tBU0Y7SUFqRlkseUJBQWlCLG9CQWlGN0I7QUFDSCxDQUFDLEVBNUZTLE9BQU8sS0FBUCxPQUFPLFFBNEZoQjs7Ozs7Ozs7Ozs7Ozs7Ozs7QUNsVUQsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUVqQjtBQWtEMUM7O0dBRUc7QUFDSSxNQUFNLDBCQUEwQixHQUFHLElBQUksb0RBQUssQ0FDakQsMkRBQTJELENBQzVELENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvcHJvcGVydHktaW5zcGVjdG9yL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvcHJvcGVydHktaW5zcGVjdG9yL3NyYy90b2tlbi50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBwcm9wZXJ0eS1pbnNwZWN0b3JcbiAqL1xuXG5pbXBvcnQgeyBJTGFiU2hlbGwgfSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IFJlYWN0V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBGb2N1c1RyYWNrZXIsIFNpbmdsZXRvbkxheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCAqIGFzIFJlYWN0IGZyb20gJ3JlYWN0JztcbmltcG9ydCB7IElQcm9wZXJ0eUluc3BlY3RvciwgSVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXIgfSBmcm9tICcuL3Rva2VuJztcblxuZXhwb3J0IHsgSVByb3BlcnR5SW5zcGVjdG9yLCBJUHJvcGVydHlJbnNwZWN0b3JQcm92aWRlciB9O1xuXG4vKipcbiAqIFRoZSBpbXBsZW1lbnRhdGlvbiBvZiB0aGUgUHJvcGVydHlJbnNwZWN0b3IuXG4gKi9cbmFic3RyYWN0IGNsYXNzIFByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXJcbiAgZXh0ZW5kcyBXaWRnZXRcbiAgaW1wbGVtZW50cyBJUHJvcGVydHlJbnNwZWN0b3JQcm92aWRlclxue1xuICAvKipcbiAgICogQ29uc3RydWN0IGEgbmV3IFByb3BlcnR5IEluc3BlY3Rvci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKCkge1xuICAgIHN1cGVyKCk7XG4gICAgdGhpcy5hZGRDbGFzcygnanAtUHJvcGVydHlJbnNwZWN0b3InKTtcbiAgICB0aGlzLl90cmFja2VyID0gbmV3IEZvY3VzVHJhY2tlcigpO1xuICAgIHRoaXMuX3RyYWNrZXIuY3VycmVudENoYW5nZWQuY29ubmVjdCh0aGlzLl9vbkN1cnJlbnRDaGFuZ2VkLCB0aGlzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWdpc3RlciBhIHdpZGdldCBpbiB0aGUgcHJvcGVydHkgaW5zcGVjdG9yIHByb3ZpZGVyLlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFRoZSBvd25lciB3aWRnZXQgdG8gcmVnaXN0ZXIuXG4gICAqL1xuICByZWdpc3Rlcih3aWRnZXQ6IFdpZGdldCk6IElQcm9wZXJ0eUluc3BlY3RvciB7XG4gICAgaWYgKHRoaXMuX2luc3BlY3RvcnMuaGFzKHdpZGdldCkpIHtcbiAgICAgIHRocm93IG5ldyBFcnJvcignV2lkZ2V0IGlzIGFscmVhZHkgcmVnaXN0ZXJlZCcpO1xuICAgIH1cbiAgICBjb25zdCBpbnNwZWN0b3IgPSBuZXcgUHJpdmF0ZS5Qcm9wZXJ0eUluc3BlY3Rvcih3aWRnZXQpO1xuICAgIHdpZGdldC5kaXNwb3NlZC5jb25uZWN0KHRoaXMuX29uV2lkZ2V0RGlzcG9zZWQsIHRoaXMpO1xuICAgIHRoaXMuX2luc3BlY3RvcnMuc2V0KHdpZGdldCwgaW5zcGVjdG9yKTtcbiAgICBpbnNwZWN0b3Iub25BY3Rpb24uY29ubmVjdCh0aGlzLl9vbkluc3BlY3RvckFjdGlvbiwgdGhpcyk7XG4gICAgdGhpcy5fdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICByZXR1cm4gaW5zcGVjdG9yO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjdXJyZW50IHdpZGdldCBiZWluZyB0cmFja2VkIGJ5IHRoZSBpbnNwZWN0b3IuXG4gICAqL1xuICBwcm90ZWN0ZWQgZ2V0IGN1cnJlbnRXaWRnZXQoKTogV2lkZ2V0IHwgbnVsbCB7XG4gICAgcmV0dXJuIHRoaXMuX3RyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWZyZXNoIHRoZSBjb250ZW50IGZvciB0aGUgY3VycmVudCB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgcmVmcmVzaCgpOiB2b2lkIHtcbiAgICBjb25zdCBjdXJyZW50ID0gdGhpcy5fdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgIGlmICghY3VycmVudCkge1xuICAgICAgdGhpcy5zZXRDb250ZW50KG51bGwpO1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBpbnNwZWN0b3IgPSB0aGlzLl9pbnNwZWN0b3JzLmdldChjdXJyZW50KTtcbiAgICBpZiAoaW5zcGVjdG9yKSB7XG4gICAgICB0aGlzLnNldENvbnRlbnQoaW5zcGVjdG9yLmNvbnRlbnQpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBTaG93IHRoZSBwcm92aWRlciBwYW5lbC5cbiAgICovXG4gIHByb3RlY3RlZCBhYnN0cmFjdCBzaG93UGFuZWwoKTogdm9pZDtcblxuICAvKipcbiAgICogU2V0IHRoZSBjb250ZW50IG9mIHRoZSBwcm92aWRlci5cbiAgICovXG4gIHByb3RlY3RlZCBhYnN0cmFjdCBzZXRDb250ZW50KGNvbnRlbnQ6IFdpZGdldCB8IG51bGwpOiB2b2lkO1xuXG4gIC8qKlxuICAgKiBIYW5kbGUgdGhlIGRpc3Bvc2FsIG9mIGEgd2lkZ2V0LlxuICAgKi9cbiAgcHJpdmF0ZSBfb25XaWRnZXREaXNwb3NlZChzZW5kZXI6IFdpZGdldCk6IHZvaWQge1xuICAgIGNvbnN0IGluc3BlY3RvciA9IHRoaXMuX2luc3BlY3RvcnMuZ2V0KHNlbmRlcik7XG4gICAgaWYgKGluc3BlY3Rvcikge1xuICAgICAgaW5zcGVjdG9yLmRpc3Bvc2UoKTtcbiAgICAgIHRoaXMuX2luc3BlY3RvcnMuZGVsZXRlKHNlbmRlcik7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBpbnNwZWN0b3IgYWN0aW9ucy5cbiAgICovXG4gIHByaXZhdGUgX29uSW5zcGVjdG9yQWN0aW9uKFxuICAgIHNlbmRlcjogUHJpdmF0ZS5Qcm9wZXJ0eUluc3BlY3RvcixcbiAgICBhY3Rpb246IFByaXZhdGUuUHJvcGVydHlJbnNwZWN0b3JBY3Rpb25cbiAgKSB7XG4gICAgY29uc3Qgb3duZXIgPSBzZW5kZXIub3duZXI7XG4gICAgY29uc3QgY3VycmVudCA9IHRoaXMuX3RyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICBzd2l0Y2ggKGFjdGlvbikge1xuICAgICAgY2FzZSAnY29udGVudCc6XG4gICAgICAgIGlmIChjdXJyZW50ID09PSBvd25lcikge1xuICAgICAgICAgIHRoaXMuc2V0Q29udGVudChzZW5kZXIuY29udGVudCk7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdkaXNwb3NlJzpcbiAgICAgICAgaWYgKG93bmVyKSB7XG4gICAgICAgICAgdGhpcy5fdHJhY2tlci5yZW1vdmUob3duZXIpO1xuICAgICAgICAgIHRoaXMuX2luc3BlY3RvcnMuZGVsZXRlKG93bmVyKTtcbiAgICAgICAgfVxuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ3Nob3ctcGFuZWwnOlxuICAgICAgICBpZiAoY3VycmVudCA9PT0gb3duZXIpIHtcbiAgICAgICAgICB0aGlzLnNob3dQYW5lbCgpO1xuICAgICAgICB9XG4gICAgICAgIGJyZWFrO1xuICAgICAgZGVmYXVsdDpcbiAgICAgICAgdGhyb3cgbmV3IEVycm9yKCdVbnN1cHBvcnRlZCBpbnNwZWN0b3IgYWN0aW9uJyk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhIGNoYW5nZSB0byB0aGUgY3VycmVudCB3aWRnZXQgaW4gdGhlIHRyYWNrZXIuXG4gICAqL1xuICBwcml2YXRlIF9vbkN1cnJlbnRDaGFuZ2VkKCk6IHZvaWQge1xuICAgIGNvbnN0IGN1cnJlbnQgPSB0aGlzLl90cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgaWYgKGN1cnJlbnQpIHtcbiAgICAgIGNvbnN0IGluc3BlY3RvciA9IHRoaXMuX2luc3BlY3RvcnMuZ2V0KGN1cnJlbnQpO1xuICAgICAgY29uc3QgY29udGVudCA9IGluc3BlY3RvciEuY29udGVudDtcbiAgICAgIHRoaXMuc2V0Q29udGVudChjb250ZW50KTtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5zZXRDb250ZW50KG51bGwpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX3RyYWNrZXIgPSBuZXcgRm9jdXNUcmFja2VyKCk7XG4gIHByaXZhdGUgX2luc3BlY3RvcnMgPSBuZXcgTWFwPFdpZGdldCwgUHJpdmF0ZS5Qcm9wZXJ0eUluc3BlY3Rvcj4oKTtcbn1cblxuLyoqXG4gKiBBIGNsYXNzIHRoYXQgYWRkcyBhIHByb3BlcnR5IGluc3BlY3RvciBwcm92aWRlciB0byB0aGVcbiAqIEp1cHl0ZXJMYWIgc2lkZWJhci5cbiAqL1xuZXhwb3J0IGNsYXNzIFNpZGVCYXJQcm9wZXJ0eUluc3BlY3RvclByb3ZpZGVyIGV4dGVuZHMgUHJvcGVydHlJbnNwZWN0b3JQcm92aWRlciB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgU2lkZSBCYXIgUHJvcGVydHkgSW5zcGVjdG9yLlxuICAgKi9cbiAgY29uc3RydWN0b3IoXG4gICAgbGFic2hlbGw6IElMYWJTaGVsbCxcbiAgICBwbGFjZWhvbGRlcj86IFdpZGdldCxcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl9sYWJzaGVsbCA9IGxhYnNoZWxsO1xuICAgIHRoaXMudHJhbnNsYXRvciA9IHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgdGhpcy5fdHJhbnMgPSB0aGlzLnRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IGxheW91dCA9ICh0aGlzLmxheW91dCA9IG5ldyBTaW5nbGV0b25MYXlvdXQoKSk7XG4gICAgaWYgKHBsYWNlaG9sZGVyKSB7XG4gICAgICB0aGlzLl9wbGFjZWhvbGRlciA9IHBsYWNlaG9sZGVyO1xuICAgIH0gZWxzZSB7XG4gICAgICBjb25zdCBub2RlID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgICBjb25zdCBjb250ZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnZGl2Jyk7XG4gICAgICBjb250ZW50LnRleHRDb250ZW50ID0gdGhpcy5fdHJhbnMuX18oJ05vIHByb3BlcnRpZXMgdG8gaW5zcGVjdC4nKTtcbiAgICAgIGNvbnRlbnQuY2xhc3NOYW1lID0gJ2pwLVByb3BlcnR5SW5zcGVjdG9yLXBsYWNlaG9sZGVyQ29udGVudCc7XG4gICAgICBub2RlLmFwcGVuZENoaWxkKGNvbnRlbnQpO1xuICAgICAgdGhpcy5fcGxhY2Vob2xkZXIgPSBuZXcgV2lkZ2V0KHsgbm9kZSB9KTtcbiAgICAgIHRoaXMuX3BsYWNlaG9sZGVyLmFkZENsYXNzKCdqcC1Qcm9wZXJ0eUluc3BlY3Rvci1wbGFjZWhvbGRlcicpO1xuICAgIH1cbiAgICBsYXlvdXQud2lkZ2V0ID0gdGhpcy5fcGxhY2Vob2xkZXI7XG4gICAgbGFic2hlbGwuY3VycmVudENoYW5nZWQuY29ubmVjdCh0aGlzLl9vblNoZWxsQ3VycmVudENoYW5nZWQsIHRoaXMpO1xuICAgIHRoaXMuX29uU2hlbGxDdXJyZW50Q2hhbmdlZCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgY29udGVudCBvZiB0aGUgc2lkZWJhciBwYW5lbC5cbiAgICovXG4gIHByb3RlY3RlZCBzZXRDb250ZW50KGNvbnRlbnQ6IFdpZGdldCB8IG51bGwpOiB2b2lkIHtcbiAgICBjb25zdCBsYXlvdXQgPSB0aGlzLmxheW91dCBhcyBTaW5nbGV0b25MYXlvdXQ7XG4gICAgaWYgKGxheW91dC53aWRnZXQpIHtcbiAgICAgIGxheW91dC53aWRnZXQucmVtb3ZlQ2xhc3MoJ2pwLVByb3BlcnR5SW5zcGVjdG9yLWNvbnRlbnQnKTtcbiAgICAgIGxheW91dC5yZW1vdmVXaWRnZXQobGF5b3V0LndpZGdldCk7XG4gICAgfVxuICAgIGlmICghY29udGVudCkge1xuICAgICAgY29udGVudCA9IHRoaXMuX3BsYWNlaG9sZGVyO1xuICAgIH1cbiAgICBjb250ZW50LmFkZENsYXNzKCdqcC1Qcm9wZXJ0eUluc3BlY3Rvci1jb250ZW50Jyk7XG4gICAgbGF5b3V0LndpZGdldCA9IGNvbnRlbnQ7XG4gIH1cblxuICAvKipcbiAgICogU2hvdyB0aGUgc2lkZWJhciBwYW5lbC5cbiAgICovXG4gIHNob3dQYW5lbCgpOiB2b2lkIHtcbiAgICB0aGlzLl9sYWJzaGVsbC5hY3RpdmF0ZUJ5SWQodGhpcy5pZCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIHRoZSBjYXNlIHdoZW4gdGhlIGN1cnJlbnQgd2lkZ2V0IGlzIG5vdCBpbiBvdXIgdHJhY2tlci5cbiAgICovXG4gIHByaXZhdGUgX29uU2hlbGxDdXJyZW50Q2hhbmdlZCgpOiB2b2lkIHtcbiAgICBjb25zdCBjdXJyZW50ID0gdGhpcy5jdXJyZW50V2lkZ2V0O1xuICAgIGlmICghY3VycmVudCkge1xuICAgICAgdGhpcy5zZXRDb250ZW50KG51bGwpO1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBjdXJyZW50U2hlbGwgPSB0aGlzLl9sYWJzaGVsbC5jdXJyZW50V2lkZ2V0O1xuICAgIGlmIChjdXJyZW50U2hlbGw/Lm5vZGUuY29udGFpbnMoY3VycmVudC5ub2RlKSkge1xuICAgICAgdGhpcy5yZWZyZXNoKCk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHRoaXMuc2V0Q29udGVudChudWxsKTtcbiAgICB9XG4gIH1cblxuICBwcm90ZWN0ZWQgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3I7XG4gIHByaXZhdGUgX3RyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZTtcbiAgcHJpdmF0ZSBfbGFic2hlbGw6IElMYWJTaGVsbDtcbiAgcHJpdmF0ZSBfcGxhY2Vob2xkZXI6IFdpZGdldDtcbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgbW9kdWxlIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQSB0eXBlIGFsaWFzIGZvciB0aGUgYWN0aW9ucyBhIHByb3BlcnR5IGluc3BlY3RvciBjYW4gdGFrZS5cbiAgICovXG4gIGV4cG9ydCB0eXBlIFByb3BlcnR5SW5zcGVjdG9yQWN0aW9uID0gJ2NvbnRlbnQnIHwgJ2Rpc3Bvc2UnIHwgJ3Nob3ctcGFuZWwnO1xuXG4gIC8qKlxuICAgKiBBbiBpbXBsZW1lbnRhdGlvbiBvZiB0aGUgcHJvcGVydHkgaW5zcGVjdG9yIHVzZWQgYnkgdGhlXG4gICAqIHByb3BlcnR5IGluc3BlY3RvciBwcm92aWRlci5cbiAgICovXG4gIGV4cG9ydCBjbGFzcyBQcm9wZXJ0eUluc3BlY3RvciBpbXBsZW1lbnRzIElQcm9wZXJ0eUluc3BlY3RvciB7XG4gICAgLyoqXG4gICAgICogQ29uc3RydWN0IGEgbmV3IHByb3BlcnR5IGluc3BlY3Rvci5cbiAgICAgKi9cbiAgICBjb25zdHJ1Y3Rvcihvd25lcjogV2lkZ2V0KSB7XG4gICAgICB0aGlzLl9vd25lciA9IG93bmVyO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBvd25lciB3aWRnZXQgZm9yIHRoZSBwcm9wZXJ0eSBpbnNwZWN0b3IuXG4gICAgICovXG4gICAgZ2V0IG93bmVyKCk6IFdpZGdldCB8IG51bGwge1xuICAgICAgcmV0dXJuIHRoaXMuX293bmVyO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFRoZSBjdXJyZW50IGNvbnRlbnQgZm9yIHRoZSBwcm9wZXJ0eSBpbnNwZWN0b3IuXG4gICAgICovXG4gICAgZ2V0IGNvbnRlbnQoKTogV2lkZ2V0IHwgbnVsbCB7XG4gICAgICByZXR1cm4gdGhpcy5fY29udGVudDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBwcm9wZXJ0eSBpbnNwZWN0b3IgaXMgZGlzcG9zZWQuXG4gICAgICovXG4gICAgZ2V0IGlzRGlzcG9zZWQoKTogYm9vbGVhbiB7XG4gICAgICByZXR1cm4gdGhpcy5faXNEaXNwb3NlZDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBBIHNpZ25hbCB1c2VkIGZvciBhY3Rpb25zIHJlbGF0ZWQgdG8gdGhlIHByb3BlcnR5IGluc3BlY3Rvci5cbiAgICAgKi9cbiAgICBnZXQgb25BY3Rpb24oKTogSVNpZ25hbDxQcm9wZXJ0eUluc3BlY3RvciwgUHJvcGVydHlJbnNwZWN0b3JBY3Rpb24+IHtcbiAgICAgIHJldHVybiB0aGlzLl9vbkFjdGlvbjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBTaG93IHRoZSBwcm9wZXJ0eSBpbnNwZWN0b3IgcGFuZWwuXG4gICAgICovXG4gICAgc2hvd1BhbmVsKCk6IHZvaWQge1xuICAgICAgaWYgKHRoaXMuX2lzRGlzcG9zZWQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgdGhpcy5fb25BY3Rpb24uZW1pdCgnc2hvdy1wYW5lbCcpO1xuICAgIH1cblxuICAgIC8qKlxuICAgICAqIFJlbmRlciB0aGUgcHJvcGVydHkgaW5zcGVjdG9yIGNvbnRlbnQuXG4gICAgICovXG4gICAgcmVuZGVyKHdpZGdldDogV2lkZ2V0IHwgUmVhY3QuUmVhY3RFbGVtZW50KTogdm9pZCB7XG4gICAgICBpZiAodGhpcy5faXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBpZiAod2lkZ2V0IGluc3RhbmNlb2YgV2lkZ2V0KSB7XG4gICAgICAgIHRoaXMuX2NvbnRlbnQgPSB3aWRnZXQ7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICB0aGlzLl9jb250ZW50ID0gUmVhY3RXaWRnZXQuY3JlYXRlKHdpZGdldCk7XG4gICAgICB9XG4gICAgICB0aGlzLl9vbkFjdGlvbi5lbWl0KCdjb250ZW50Jyk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogRGlzcG9zZSBvZiB0aGUgcHJvcGVydHkgaW5zcGVjdG9yLlxuICAgICAqL1xuICAgIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgICBpZiAodGhpcy5faXNEaXNwb3NlZCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICB0aGlzLl9pc0Rpc3Bvc2VkID0gdHJ1ZTtcbiAgICAgIHRoaXMuX2NvbnRlbnQgPSBudWxsO1xuICAgICAgdGhpcy5fb3duZXIgPSBudWxsO1xuICAgICAgU2lnbmFsLmNsZWFyRGF0YSh0aGlzKTtcbiAgICB9XG5cbiAgICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG4gICAgcHJpdmF0ZSBfY29udGVudDogV2lkZ2V0IHwgbnVsbCA9IG51bGw7XG4gICAgcHJpdmF0ZSBfb3duZXI6IFdpZGdldCB8IG51bGwgPSBudWxsO1xuICAgIHByaXZhdGUgX29uQWN0aW9uID0gbmV3IFNpZ25hbDxcbiAgICAgIFByb3BlcnR5SW5zcGVjdG9yLFxuICAgICAgUHJpdmF0ZS5Qcm9wZXJ0eUluc3BlY3RvckFjdGlvblxuICAgID4odGhpcyk7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuXG4vKipcbiAqIEEgcHJvcGVydHkgaW5zcGVjdG9yIGludGVyZmFjZSBwcm92aWRlZCB3aGVuIHJlZ2lzdGVyaW5nXG4gKiB0byBhIHByb3BlcnR5IGluc3BlY3RvciBwcm92aWRlci4gIEFsbG93cyBhbiBvd25lciB3aWRnZXRcbiAqIHRvIHNldCB0aGUgcHJvcGVydHkgaW5zcGVjdG9yIGNvbnRlbnQgZm9yIGl0c2VsZi5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJUHJvcGVydHlJbnNwZWN0b3IgZXh0ZW5kcyBJRGlzcG9zYWJsZSB7XG4gIC8qXG4gICAqIFJlbmRlciB0aGUgcHJvcGVydHkgaW5zcGVjdG9yIGNvbnRlbnQuXG4gICAqXG4gICAqIElmIHRoZSBvd25lciB3aWRnZXQgaXMgbm90IHRoZSBtb3N0IHJlY2VudGx5IGZvY3VzZWQsXG4gICAqIFRoZSBjb250ZW50IHdpbGwgbm90IGJlIHNob3duIHVudGlsIHRoYXQgd2lkZ2V0XG4gICAqIGlzIGZvY3VzZWQuXG4gICAqXG4gICAqIEBwYXJhbSBjb250ZW50IC0gdGhlIHdpZGdldCBvciByZWFjdCBlbGVtZW50IHRvIHJlbmRlci5cbiAgICovXG4gIHJlbmRlcihjb250ZW50OiBXaWRnZXQgfCBSZWFjdC5SZWFjdEVsZW1lbnQpOiB2b2lkO1xuXG4gIC8qKlxuICAgKiBTaG93IHRoZSBwcm9wZXJ0eSBpbnNwZWN0b3IgcGFuZWwuXG4gICAqXG4gICAqIElmIHRoZSBvd25lciB3aWRnZXQgaXMgbm90IHRoZSBtb3N0IHJlY2VudGx5IGZvY3VzZWQsXG4gICAqIHRoaXMgaXMgYSBuby1vcC4gIEl0IHNob3VsZCBiZSB0cmlnZ2VyZWQgYnkgYSB1c2VyXG4gICAqIGFjdGlvbi5cbiAgICovXG4gIHNob3dQYW5lbCgpOiB2b2lkO1xufVxuXG4vKipcbiAqIEEgcHJvdmlkZXIgZm9yIHByb3BlcnR5IGluc3BlY3RvcnMuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXIge1xuICAvKipcbiAgICogUmVnaXN0ZXIgYSB3aWRnZXQgaW4gdGhlIHByb3BlcnR5IGluc3BlY3RvciBwcm92aWRlci5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCBUaGUgb3duZXIgd2lkZ2V0IHdob3NlIHByb3BlcnRpZXMgd2lsbCBiZSBpbnNwZWN0ZWQuXG4gICAqXG4gICAqICMjIE5vdGVzXG4gICAqIE9ubHkgb25lIHByb3BlcnR5IGluc3BlY3RvciBjYW4gYmUgcHJvdmlkZWQgZm9yIGVhY2ggd2lkZ2V0LlxuICAgKiBSZWdpc3RlcmluZyB0aGUgc2FtZSB3aWRnZXQgdHdpY2Ugd2lsbCByZXN1bHQgaW4gYW4gZXJyb3IuXG4gICAqIEEgd2lkZ2V0IGNhbiBiZSB1bnJlZ2lzdGVyZWQgYnkgZGlzcG9zaW5nIG9mIGl0cyBwcm9wZXJ0eVxuICAgKiBpbnNwZWN0b3IuXG4gICAqL1xuICByZWdpc3Rlcih3aWRnZXQ6IFdpZGdldCk6IElQcm9wZXJ0eUluc3BlY3Rvcjtcbn1cblxuLyoqXG4gKiBUaGUgcHJvcGVydHkgaW5zcGVjdG9yIHByb3ZpZGVyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXIgPSBuZXcgVG9rZW48SVByb3BlcnR5SW5zcGVjdG9yUHJvdmlkZXI+KFxuICAnQGp1cHl0ZXJsYWIvcHJvcGVydHktaW5zcGVjdG9yOklQcm9wZXJ0eUluc3BlY3RvclByb3ZpZGVyJ1xuKTtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==