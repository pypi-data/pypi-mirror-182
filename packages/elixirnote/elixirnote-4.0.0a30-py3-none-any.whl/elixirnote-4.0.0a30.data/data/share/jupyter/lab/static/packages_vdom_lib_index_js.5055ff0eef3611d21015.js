"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_vdom_lib_index_js"],{

/***/ "../../packages/vdom/lib/index.js":
/*!****************************************!*\
  !*** ../../packages/vdom/lib/index.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IVDOMTracker": () => (/* binding */ IVDOMTracker),
/* harmony export */   "RenderedVDOM": () => (/* binding */ RenderedVDOM)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _nteract_transform_vdom__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @nteract/transform-vdom */ "../../node_modules/@nteract/transform-vdom/lib/index.js");
/* harmony import */ var _nteract_transform_vdom__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_nteract_transform_vdom__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-dom */ "webpack/sharing/consume/default/react-dom/react-dom");
/* harmony import */ var react_dom__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_dom__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module vdom
 */





/**
 * The CSS class to add to the VDOM Widget.
 */
const CSS_CLASS = 'jp-RenderedVDOM';
/**
 * The VDOM tracker token.
 */
const IVDOMTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/vdom:IVDOMTracker');
/**
 * A renderer for declarative virtual DOM content.
 */
class RenderedVDOM extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget {
    /**
     * Create a new widget for rendering DOM.
     */
    constructor(options, context) {
        super();
        /**
         * Handle events for VDOM element.
         */
        this.handleVDOMEvent = (targetName, event) => {
            var _a, _b;
            // When a VDOM element's event handler is called, send a serialized
            // representation of the event to the registered comm channel for the
            // kernel to handle
            if (this._timer) {
                window.clearTimeout(this._timer);
            }
            const kernel = (_b = (_a = this._sessionContext) === null || _a === void 0 ? void 0 : _a.session) === null || _b === void 0 ? void 0 : _b.kernel;
            if (kernel) {
                this._timer = window.setTimeout(() => {
                    if (!this._comms[targetName]) {
                        this._comms[targetName] = kernel.createComm(targetName);
                        this._comms[targetName].open();
                    }
                    this._comms[targetName].send(JSON.stringify(event));
                }, 16);
            }
        };
        this._comms = {};
        this.addClass(CSS_CLASS);
        this.addClass('jp-RenderedHTML');
        this.addClass('jp-RenderedHTMLCommon');
        this._mimeType = options.mimeType;
        if (context) {
            this._sessionContext = context.sessionContext;
        }
    }
    /**
     * Dispose of the widget.
     */
    dispose() {
        // Dispose of comm disposables
        for (const targetName in this._comms) {
            this._comms[targetName].dispose();
        }
        super.dispose();
    }
    /**
     * Called before the widget is detached from the DOM.
     */
    onBeforeDetach(msg) {
        // Dispose of React component(s).
        react_dom__WEBPACK_IMPORTED_MODULE_4__.unmountComponentAtNode(this.node);
    }
    /**
     * Render VDOM into this widget's node.
     */
    renderModel(model) {
        return new Promise((resolve, reject) => {
            const data = model.data[this._mimeType];
            react_dom__WEBPACK_IMPORTED_MODULE_4__.render(react__WEBPACK_IMPORTED_MODULE_3__.createElement((_nteract_transform_vdom__WEBPACK_IMPORTED_MODULE_2___default()), { data: data, onVDOMEvent: this.handleVDOMEvent }), this.node, () => {
                resolve();
            });
        });
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdmRvbV9saWJfaW5kZXhfanMuNTA1NWZmMGVlZjM2MTFkMjEwMTUuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFNdUM7QUFFRDtBQUN1QjtBQUNqQztBQUNPO0FBRXRDOztHQUVHO0FBQ0gsTUFBTSxTQUFTLEdBQUcsaUJBQWlCLENBQUM7QUFPcEM7O0dBRUc7QUFDSSxNQUFNLFlBQVksR0FBRyxJQUFJLG9EQUFLLENBQ25DLCtCQUErQixDQUNoQyxDQUFDO0FBRUY7O0dBRUc7QUFDSSxNQUFNLFlBQWEsU0FBUSxtREFBTTtJQUN0Qzs7T0FFRztJQUNILFlBQ0UsT0FBcUMsRUFDckMsT0FBNEQ7UUFFNUQsS0FBSyxFQUFFLENBQUM7UUE2Q1Y7O1dBRUc7UUFDSCxvQkFBZSxHQUFHLENBQUMsVUFBa0IsRUFBRSxLQUEyQixFQUFRLEVBQUU7O1lBQzFFLG1FQUFtRTtZQUNuRSxxRUFBcUU7WUFDckUsbUJBQW1CO1lBQ25CLElBQUksSUFBSSxDQUFDLE1BQU0sRUFBRTtnQkFDZixNQUFNLENBQUMsWUFBWSxDQUFDLElBQUksQ0FBQyxNQUFNLENBQUMsQ0FBQzthQUNsQztZQUNELE1BQU0sTUFBTSxHQUFHLGdCQUFJLENBQUMsZUFBZSwwQ0FBRSxPQUFPLDBDQUFFLE1BQU0sQ0FBQztZQUNyRCxJQUFJLE1BQU0sRUFBRTtnQkFDVixJQUFJLENBQUMsTUFBTSxHQUFHLE1BQU0sQ0FBQyxVQUFVLENBQUMsR0FBRyxFQUFFO29CQUNuQyxJQUFJLENBQUMsSUFBSSxDQUFDLE1BQU0sQ0FBQyxVQUFVLENBQUMsRUFBRTt3QkFDNUIsSUFBSSxDQUFDLE1BQU0sQ0FBQyxVQUFVLENBQUMsR0FBRyxNQUFNLENBQUMsVUFBVSxDQUFDLFVBQVUsQ0FBQyxDQUFDO3dCQUN4RCxJQUFJLENBQUMsTUFBTSxDQUFDLFVBQVUsQ0FBQyxDQUFDLElBQUksRUFBRSxDQUFDO3FCQUNoQztvQkFDRCxJQUFJLENBQUMsTUFBTSxDQUFDLFVBQVUsQ0FBQyxDQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsU0FBUyxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7Z0JBQ3RELENBQUMsRUFBRSxFQUFFLENBQUMsQ0FBQzthQUNSO1FBQ0gsQ0FBQyxDQUFDO1FBSU0sV0FBTSxHQUEyQyxFQUFFLENBQUM7UUFwRTFELElBQUksQ0FBQyxRQUFRLENBQUMsU0FBUyxDQUFDLENBQUM7UUFDekIsSUFBSSxDQUFDLFFBQVEsQ0FBQyxpQkFBaUIsQ0FBQyxDQUFDO1FBQ2pDLElBQUksQ0FBQyxRQUFRLENBQUMsdUJBQXVCLENBQUMsQ0FBQztRQUN2QyxJQUFJLENBQUMsU0FBUyxHQUFHLE9BQU8sQ0FBQyxRQUFRLENBQUM7UUFDbEMsSUFBSSxPQUFPLEVBQUU7WUFDWCxJQUFJLENBQUMsZUFBZSxHQUFHLE9BQU8sQ0FBQyxjQUFjLENBQUM7U0FDL0M7SUFDSCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxPQUFPO1FBQ0wsOEJBQThCO1FBQzlCLEtBQUssTUFBTSxVQUFVLElBQUksSUFBSSxDQUFDLE1BQU0sRUFBRTtZQUNwQyxJQUFJLENBQUMsTUFBTSxDQUFDLFVBQVUsQ0FBQyxDQUFDLE9BQU8sRUFBRSxDQUFDO1NBQ25DO1FBQ0QsS0FBSyxDQUFDLE9BQU8sRUFBRSxDQUFDO0lBQ2xCLENBQUM7SUFFRDs7T0FFRztJQUNPLGNBQWMsQ0FBQyxHQUFZO1FBQ25DLGlDQUFpQztRQUNqQyw2REFBK0IsQ0FBQyxJQUFJLENBQUMsSUFBSSxDQUFDLENBQUM7SUFDN0MsQ0FBQztJQUVEOztPQUVHO0lBQ0gsV0FBVyxDQUFDLEtBQTZCO1FBQ3ZDLE9BQU8sSUFBSSxPQUFPLENBQUMsQ0FBQyxPQUFPLEVBQUUsTUFBTSxFQUFFLEVBQUU7WUFDckMsTUFBTSxJQUFJLEdBQUcsS0FBSyxDQUFDLElBQUksQ0FBQyxJQUFJLENBQUMsU0FBUyxDQUFRLENBQUM7WUFDL0MsNkNBQWUsQ0FDYixpREFBQyxnRUFBSSxJQUFDLElBQUksRUFBRSxJQUFJLEVBQUUsV0FBVyxFQUFFLElBQUksQ0FBQyxlQUFlLEdBQUksRUFDdkQsSUFBSSxDQUFDLElBQUksRUFDVCxHQUFHLEVBQUU7Z0JBQ0gsT0FBTyxFQUFFLENBQUM7WUFDWixDQUFDLENBQ0YsQ0FBQztRQUNKLENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztDQTRCRiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy92ZG9tL3NyYy9pbmRleC50c3giXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgdmRvbVxuICovXG5cbmltcG9ydCB7IElTZXNzaW9uQ29udGV4dCwgSVdpZGdldFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBEb2N1bWVudFJlZ2lzdHJ5LCBNaW1lRG9jdW1lbnQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBJUmVuZGVyTWltZSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUtaW50ZXJmYWNlcyc7XG5pbXBvcnQgeyBLZXJuZWwgfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IE1lc3NhZ2UgfSBmcm9tICdAbHVtaW5vL21lc3NhZ2luZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IFZET00sIHsgU2VyaWFsaXplZEV2ZW50IH0gZnJvbSAnQG50ZXJhY3QvdHJhbnNmb3JtLXZkb20nO1xuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuaW1wb3J0ICogYXMgUmVhY3RET00gZnJvbSAncmVhY3QtZG9tJztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIHRvIGFkZCB0byB0aGUgVkRPTSBXaWRnZXQuXG4gKi9cbmNvbnN0IENTU19DTEFTUyA9ICdqcC1SZW5kZXJlZFZET00nO1xuXG4vKipcbiAqIEEgY2xhc3MgdGhhdCB0cmFja3MgVkRPTSB3aWRnZXRzLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElWRE9NVHJhY2tlciBleHRlbmRzIElXaWRnZXRUcmFja2VyPE1pbWVEb2N1bWVudD4ge31cblxuLyoqXG4gKiBUaGUgVkRPTSB0cmFja2VyIHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVZET01UcmFja2VyID0gbmV3IFRva2VuPElWRE9NVHJhY2tlcj4oXG4gICdAanVweXRlcmxhYi92ZG9tOklWRE9NVHJhY2tlcidcbik7XG5cbi8qKlxuICogQSByZW5kZXJlciBmb3IgZGVjbGFyYXRpdmUgdmlydHVhbCBET00gY29udGVudC5cbiAqL1xuZXhwb3J0IGNsYXNzIFJlbmRlcmVkVkRPTSBleHRlbmRzIFdpZGdldCBpbXBsZW1lbnRzIElSZW5kZXJNaW1lLklSZW5kZXJlciB7XG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgd2lkZ2V0IGZvciByZW5kZXJpbmcgRE9NLlxuICAgKi9cbiAgY29uc3RydWN0b3IoXG4gICAgb3B0aW9uczogSVJlbmRlck1pbWUuSVJlbmRlcmVyT3B0aW9ucyxcbiAgICBjb250ZXh0PzogRG9jdW1lbnRSZWdpc3RyeS5JQ29udGV4dDxEb2N1bWVudFJlZ2lzdHJ5LklNb2RlbD5cbiAgKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmFkZENsYXNzKENTU19DTEFTUyk7XG4gICAgdGhpcy5hZGRDbGFzcygnanAtUmVuZGVyZWRIVE1MJyk7XG4gICAgdGhpcy5hZGRDbGFzcygnanAtUmVuZGVyZWRIVE1MQ29tbW9uJyk7XG4gICAgdGhpcy5fbWltZVR5cGUgPSBvcHRpb25zLm1pbWVUeXBlO1xuICAgIGlmIChjb250ZXh0KSB7XG4gICAgICB0aGlzLl9zZXNzaW9uQ29udGV4dCA9IGNvbnRleHQuc2Vzc2lvbkNvbnRleHQ7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHdpZGdldC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgLy8gRGlzcG9zZSBvZiBjb21tIGRpc3Bvc2FibGVzXG4gICAgZm9yIChjb25zdCB0YXJnZXROYW1lIGluIHRoaXMuX2NvbW1zKSB7XG4gICAgICB0aGlzLl9jb21tc1t0YXJnZXROYW1lXS5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBDYWxsZWQgYmVmb3JlIHRoZSB3aWRnZXQgaXMgZGV0YWNoZWQgZnJvbSB0aGUgRE9NLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQmVmb3JlRGV0YWNoKG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIC8vIERpc3Bvc2Ugb2YgUmVhY3QgY29tcG9uZW50KHMpLlxuICAgIFJlYWN0RE9NLnVubW91bnRDb21wb25lbnRBdE5vZGUodGhpcy5ub2RlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgVkRPTSBpbnRvIHRoaXMgd2lkZ2V0J3Mgbm9kZS5cbiAgICovXG4gIHJlbmRlck1vZGVsKG1vZGVsOiBJUmVuZGVyTWltZS5JTWltZU1vZGVsKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgcmV0dXJuIG5ldyBQcm9taXNlKChyZXNvbHZlLCByZWplY3QpID0+IHtcbiAgICAgIGNvbnN0IGRhdGEgPSBtb2RlbC5kYXRhW3RoaXMuX21pbWVUeXBlXSBhcyBhbnk7XG4gICAgICBSZWFjdERPTS5yZW5kZXIoXG4gICAgICAgIDxWRE9NIGRhdGE9e2RhdGF9IG9uVkRPTUV2ZW50PXt0aGlzLmhhbmRsZVZET01FdmVudH0gLz4sXG4gICAgICAgIHRoaXMubm9kZSxcbiAgICAgICAgKCkgPT4ge1xuICAgICAgICAgIHJlc29sdmUoKTtcbiAgICAgICAgfVxuICAgICAgKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgZXZlbnRzIGZvciBWRE9NIGVsZW1lbnQuXG4gICAqL1xuICBoYW5kbGVWRE9NRXZlbnQgPSAodGFyZ2V0TmFtZTogc3RyaW5nLCBldmVudDogU2VyaWFsaXplZEV2ZW50PGFueT4pOiB2b2lkID0+IHtcbiAgICAvLyBXaGVuIGEgVkRPTSBlbGVtZW50J3MgZXZlbnQgaGFuZGxlciBpcyBjYWxsZWQsIHNlbmQgYSBzZXJpYWxpemVkXG4gICAgLy8gcmVwcmVzZW50YXRpb24gb2YgdGhlIGV2ZW50IHRvIHRoZSByZWdpc3RlcmVkIGNvbW0gY2hhbm5lbCBmb3IgdGhlXG4gICAgLy8ga2VybmVsIHRvIGhhbmRsZVxuICAgIGlmICh0aGlzLl90aW1lcikge1xuICAgICAgd2luZG93LmNsZWFyVGltZW91dCh0aGlzLl90aW1lcik7XG4gICAgfVxuICAgIGNvbnN0IGtlcm5lbCA9IHRoaXMuX3Nlc3Npb25Db250ZXh0Py5zZXNzaW9uPy5rZXJuZWw7XG4gICAgaWYgKGtlcm5lbCkge1xuICAgICAgdGhpcy5fdGltZXIgPSB3aW5kb3cuc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgIGlmICghdGhpcy5fY29tbXNbdGFyZ2V0TmFtZV0pIHtcbiAgICAgICAgICB0aGlzLl9jb21tc1t0YXJnZXROYW1lXSA9IGtlcm5lbC5jcmVhdGVDb21tKHRhcmdldE5hbWUpO1xuICAgICAgICAgIHRoaXMuX2NvbW1zW3RhcmdldE5hbWVdLm9wZW4oKTtcbiAgICAgICAgfVxuICAgICAgICB0aGlzLl9jb21tc1t0YXJnZXROYW1lXS5zZW5kKEpTT04uc3RyaW5naWZ5KGV2ZW50KSk7XG4gICAgICB9LCAxNik7XG4gICAgfVxuICB9O1xuXG4gIHByaXZhdGUgX21pbWVUeXBlOiBzdHJpbmc7XG4gIHByaXZhdGUgX3Nlc3Npb25Db250ZXh0PzogSVNlc3Npb25Db250ZXh0O1xuICBwcml2YXRlIF9jb21tczogeyBbdGFyZ2V0TmFtZTogc3RyaW5nXTogS2VybmVsLklDb21tIH0gPSB7fTtcbiAgcHJpdmF0ZSBfdGltZXI6IG51bWJlcjtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==