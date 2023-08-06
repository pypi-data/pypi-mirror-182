"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_ui-components-extension_lib_index_js"],{

/***/ "../../packages/ui-components-extension/lib/index.js":
/*!***********************************************************!*\
  !*** ../../packages/ui-components-extension/lib/index.js ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module ui-components-extension
 */

/**
 * Placeholder for future extension that will provide an icon manager class
 * to assist with overriding/replacing particular sets of icons
 */
const labiconManager = {
    id: '@jupyterlab/ui-components-extension:labicon-manager',
    provides: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.ILabIconManager,
    autoStart: true,
    activate: (app) => {
        return Object.create(null);
    }
};
/**
 * Sets up the component registry to be used by the FormEditor component.
 */
const registryPlugin = {
    id: '@jupyterlab/settingeditor-extension:form-registry',
    provides: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.IFormComponentRegistry,
    autoStart: true,
    activate: (app) => {
        const editorRegistry = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.FormComponentRegistry();
        return editorRegistry;
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([labiconManager, registryPlugin]);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdWktY29tcG9uZW50cy1leHRlbnNpb25fbGliX2luZGV4X2pzLjUzYTk3ZjljYzY0M2U4MGFmNTQxLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBVWdDO0FBRW5DOzs7R0FHRztBQUNILE1BQU0sY0FBYyxHQUEyQztJQUM3RCxFQUFFLEVBQUUscURBQXFEO0lBQ3pELFFBQVEsRUFBRSxzRUFBZTtJQUN6QixTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUFDLEdBQW9CLEVBQUUsRUFBRTtRQUNqQyxPQUFPLE1BQU0sQ0FBQyxNQUFNLENBQUMsSUFBSSxDQUFDLENBQUM7SUFDN0IsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sY0FBYyxHQUFrRDtJQUNwRSxFQUFFLEVBQUUsbURBQW1EO0lBQ3ZELFFBQVEsRUFBRSw2RUFBc0I7SUFDaEMsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQyxHQUFvQixFQUEwQixFQUFFO1FBQ3pELE1BQU0sY0FBYyxHQUFHLElBQUksNEVBQXFCLEVBQUUsQ0FBQztRQUNuRCxPQUFPLGNBQWMsQ0FBQztJQUN4QixDQUFDO0NBQ0YsQ0FBQztBQUVGLGlFQUFlLENBQUMsY0FBYyxFQUFFLGNBQWMsQ0FBQyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3VpLWNvbXBvbmVudHMtZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB1aS1jb21wb25lbnRzLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIEZvcm1Db21wb25lbnRSZWdpc3RyeSxcbiAgSUZvcm1Db21wb25lbnRSZWdpc3RyeSxcbiAgSUxhYkljb25NYW5hZ2VyXG59IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuXG4vKipcbiAqIFBsYWNlaG9sZGVyIGZvciBmdXR1cmUgZXh0ZW5zaW9uIHRoYXQgd2lsbCBwcm92aWRlIGFuIGljb24gbWFuYWdlciBjbGFzc1xuICogdG8gYXNzaXN0IHdpdGggb3ZlcnJpZGluZy9yZXBsYWNpbmcgcGFydGljdWxhciBzZXRzIG9mIGljb25zXG4gKi9cbmNvbnN0IGxhYmljb25NYW5hZ2VyOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUxhYkljb25NYW5hZ2VyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzLWV4dGVuc2lvbjpsYWJpY29uLW1hbmFnZXInLFxuICBwcm92aWRlczogSUxhYkljb25NYW5hZ2VyLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoYXBwOiBKdXB5dGVyRnJvbnRFbmQpID0+IHtcbiAgICByZXR1cm4gT2JqZWN0LmNyZWF0ZShudWxsKTtcbiAgfVxufTtcblxuLyoqXG4gKiBTZXRzIHVwIHRoZSBjb21wb25lbnQgcmVnaXN0cnkgdG8gYmUgdXNlZCBieSB0aGUgRm9ybUVkaXRvciBjb21wb25lbnQuXG4gKi9cbmNvbnN0IHJlZ2lzdHJ5UGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUZvcm1Db21wb25lbnRSZWdpc3RyeT4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvc2V0dGluZ2VkaXRvci1leHRlbnNpb246Zm9ybS1yZWdpc3RyeScsXG4gIHByb3ZpZGVzOiBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5LFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoYXBwOiBKdXB5dGVyRnJvbnRFbmQpOiBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5ID0+IHtcbiAgICBjb25zdCBlZGl0b3JSZWdpc3RyeSA9IG5ldyBGb3JtQ29tcG9uZW50UmVnaXN0cnkoKTtcbiAgICByZXR1cm4gZWRpdG9yUmVnaXN0cnk7XG4gIH1cbn07XG5cbmV4cG9ydCBkZWZhdWx0IFtsYWJpY29uTWFuYWdlciwgcmVnaXN0cnlQbHVnaW5dO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9