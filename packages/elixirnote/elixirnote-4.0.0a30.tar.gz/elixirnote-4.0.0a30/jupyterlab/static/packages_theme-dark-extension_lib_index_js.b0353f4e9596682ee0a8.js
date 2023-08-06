"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_theme-dark-extension_lib_index_js"],{

/***/ "../../packages/theme-dark-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/theme-dark-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module theme-dark-extension
 */


/**
 * A plugin for the Jupyter Dark Theme.
 */
const plugin = {
    id: '@jupyterlab/theme-dark-extension:plugin',
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IThemeManager, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.ITranslator],
    activate: (app, manager, translator) => {
        const trans = translator.load('jupyterlab');
        const style = '@jupyterlab/theme-dark-extension/index.css';
        manager.register({
            name: 'JupyterLab Dark',
            displayName: trans.__('JupyterLab Dark'),
            isLight: false,
            themeScrollbars: true,
            load: () => manager.loadCSS(style),
            unload: () => Promise.resolve(undefined)
        });
    },
    autoStart: true
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdGhlbWUtZGFyay1leHRlbnNpb25fbGliX2luZGV4X2pzLmIwMzUzZjRlOTU5NjY4MmVlMGE4LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFNa0Q7QUFDQztBQUV0RDs7R0FFRztBQUNILE1BQU0sTUFBTSxHQUFnQztJQUMxQyxFQUFFLEVBQUUseUNBQXlDO0lBQzdDLFFBQVEsRUFBRSxDQUFDLCtEQUFhLEVBQUUsZ0VBQVcsQ0FBQztJQUN0QyxRQUFRLEVBQUUsQ0FDUixHQUFvQixFQUNwQixPQUFzQixFQUN0QixVQUF1QixFQUN2QixFQUFFO1FBQ0YsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUM1QyxNQUFNLEtBQUssR0FBRyw0Q0FBNEMsQ0FBQztRQUMzRCxPQUFPLENBQUMsUUFBUSxDQUFDO1lBQ2YsSUFBSSxFQUFFLGlCQUFpQjtZQUN2QixXQUFXLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxpQkFBaUIsQ0FBQztZQUN4QyxPQUFPLEVBQUUsS0FBSztZQUNkLGVBQWUsRUFBRSxJQUFJO1lBQ3JCLElBQUksRUFBRSxHQUFHLEVBQUUsQ0FBQyxPQUFPLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQztZQUNsQyxNQUFNLEVBQUUsR0FBRyxFQUFFLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxTQUFTLENBQUM7U0FDekMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQUNELFNBQVMsRUFBRSxJQUFJO0NBQ2hCLENBQUM7QUFFRixpRUFBZSxNQUFNLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdGhlbWUtZGFyay1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHRoZW1lLWRhcmstZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgSVRoZW1lTWFuYWdlciB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIEEgcGx1Z2luIGZvciB0aGUgSnVweXRlciBEYXJrIFRoZW1lLlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi90aGVtZS1kYXJrLWV4dGVuc2lvbjpwbHVnaW4nLFxuICByZXF1aXJlczogW0lUaGVtZU1hbmFnZXIsIElUcmFuc2xhdG9yXSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICBtYW5hZ2VyOiBJVGhlbWVNYW5hZ2VyLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yXG4gICkgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3Qgc3R5bGUgPSAnQGp1cHl0ZXJsYWIvdGhlbWUtZGFyay1leHRlbnNpb24vaW5kZXguY3NzJztcbiAgICBtYW5hZ2VyLnJlZ2lzdGVyKHtcbiAgICAgIG5hbWU6ICdKdXB5dGVyTGFiIERhcmsnLFxuICAgICAgZGlzcGxheU5hbWU6IHRyYW5zLl9fKCdKdXB5dGVyTGFiIERhcmsnKSxcbiAgICAgIGlzTGlnaHQ6IGZhbHNlLFxuICAgICAgdGhlbWVTY3JvbGxiYXJzOiB0cnVlLFxuICAgICAgbG9hZDogKCkgPT4gbWFuYWdlci5sb2FkQ1NTKHN0eWxlKSxcbiAgICAgIHVubG9hZDogKCkgPT4gUHJvbWlzZS5yZXNvbHZlKHVuZGVmaW5lZClcbiAgICB9KTtcbiAgfSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG5leHBvcnQgZGVmYXVsdCBwbHVnaW47XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=