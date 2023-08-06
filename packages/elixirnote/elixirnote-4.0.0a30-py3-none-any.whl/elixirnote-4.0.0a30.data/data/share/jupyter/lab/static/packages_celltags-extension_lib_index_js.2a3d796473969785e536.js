"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_celltags-extension_lib_index_js"],{

/***/ "../../packages/celltags-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/celltags-extension/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_celltags__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/celltags */ "webpack/sharing/consume/default/@jupyterlab/celltags/@jupyterlab/celltags");
/* harmony import */ var _jupyterlab_celltags__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_celltags__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module celltags-extension
 */



/**
 * Initialization data for the celltags extension.
 */
const celltags = {
    id: '@jupyterlab/celltags',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTools, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.ITranslator],
    activate: (app, tools, tracker, translator) => {
        const tool = new _jupyterlab_celltags__WEBPACK_IMPORTED_MODULE_1__.TagTool(tracker, app, translator);
        tools.addItem({ tool: tool, rank: 1.6 });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (celltags);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY2VsbHRhZ3MtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy4yYTNkNzk2NDczOTY5Nzg1ZTUzNi5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFPcUU7QUFFekI7QUFFTztBQUV0RDs7R0FFRztBQUNILE1BQU0sUUFBUSxHQUFnQztJQUM1QyxFQUFFLEVBQUUsc0JBQXNCO0lBQzFCLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQUMsZ0VBQWMsRUFBRSxrRUFBZ0IsRUFBRSxnRUFBVyxDQUFDO0lBQ3pELFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLEtBQXFCLEVBQ3JCLE9BQXlCLEVBQ3pCLFVBQXVCLEVBQ3ZCLEVBQUU7UUFDRixNQUFNLElBQUksR0FBRyxJQUFJLHlEQUFPLENBQUMsT0FBTyxFQUFFLEdBQUcsRUFBRSxVQUFVLENBQUMsQ0FBQztRQUNuRCxLQUFLLENBQUMsT0FBTyxDQUFDLEVBQUUsSUFBSSxFQUFFLElBQUksRUFBRSxJQUFJLEVBQUUsR0FBRyxFQUFFLENBQUMsQ0FBQztJQUMzQyxDQUFDO0NBQ0YsQ0FBQztBQUVGLGlFQUFlLFFBQVEsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jZWxsdGFncy1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNlbGx0YWdzLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcblxuaW1wb3J0IHsgSU5vdGVib29rVG9vbHMsIElOb3RlYm9va1RyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9ub3RlYm9vayc7XG5cbmltcG9ydCB7IFRhZ1Rvb2wgfSBmcm9tICdAanVweXRlcmxhYi9jZWxsdGFncyc7XG5cbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIEluaXRpYWxpemF0aW9uIGRhdGEgZm9yIHRoZSBjZWxsdGFncyBleHRlbnNpb24uXG4gKi9cbmNvbnN0IGNlbGx0YWdzOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvY2VsbHRhZ3MnLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSU5vdGVib29rVG9vbHMsIElOb3RlYm9va1RyYWNrZXIsIElUcmFuc2xhdG9yXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB0b29sczogSU5vdGVib29rVG9vbHMsXG4gICAgdHJhY2tlcjogSU5vdGVib29rVHJhY2tlcixcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApID0+IHtcbiAgICBjb25zdCB0b29sID0gbmV3IFRhZ1Rvb2wodHJhY2tlciwgYXBwLCB0cmFuc2xhdG9yKTtcbiAgICB0b29scy5hZGRJdGVtKHsgdG9vbDogdG9vbCwgcmFuazogMS42IH0pO1xuICB9XG59O1xuXG5leHBvcnQgZGVmYXVsdCBjZWxsdGFncztcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==