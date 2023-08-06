"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_mathjax2-extension_lib_index_js-_e29c0"],{

/***/ "../../packages/mathjax2-extension/lib/index.js":
/*!******************************************************!*\
  !*** ../../packages/mathjax2-extension/lib/index.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_mathjax2__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/mathjax2 */ "webpack/sharing/consume/default/@jupyterlab/mathjax2/@jupyterlab/mathjax2");
/* harmony import */ var _jupyterlab_mathjax2__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mathjax2__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module mathjax2-extension
 */



/**
 * The MathJax latexTypesetter plugin.
 */
const plugin = {
    id: '@jupyterlab/mathjax2-extension:plugin',
    autoStart: true,
    provides: _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.ILatexTypesetter,
    activate: () => {
        const [urlParam, configParam] = ['fullMathjaxUrl', 'mathjaxConfig'];
        const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PageConfig.getOption(urlParam);
        const config = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PageConfig.getOption(configParam);
        if (!url) {
            const message = `${plugin.id} uses '${urlParam}' and '${configParam}' in PageConfig ` +
                `to operate but '${urlParam}' was not found.`;
            throw new Error(message);
        }
        return new _jupyterlab_mathjax2__WEBPACK_IMPORTED_MODULE_1__.MathJaxTypesetter({ url, config });
    }
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWF0aGpheDItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fZTI5YzAuY2IzZmJjMGUzM2JlODFjYjNmNWYuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUdnRDtBQUNNO0FBQ0M7QUFFMUQ7O0dBRUc7QUFDSCxNQUFNLE1BQU0sR0FBNEM7SUFDdEQsRUFBRSxFQUFFLHVDQUF1QztJQUMzQyxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxvRUFBZ0I7SUFDMUIsUUFBUSxFQUFFLEdBQUcsRUFBRTtRQUNiLE1BQU0sQ0FBQyxRQUFRLEVBQUUsV0FBVyxDQUFDLEdBQUcsQ0FBQyxnQkFBZ0IsRUFBRSxlQUFlLENBQUMsQ0FBQztRQUNwRSxNQUFNLEdBQUcsR0FBRyx1RUFBb0IsQ0FBQyxRQUFRLENBQUMsQ0FBQztRQUMzQyxNQUFNLE1BQU0sR0FBRyx1RUFBb0IsQ0FBQyxXQUFXLENBQUMsQ0FBQztRQUVqRCxJQUFJLENBQUMsR0FBRyxFQUFFO1lBQ1IsTUFBTSxPQUFPLEdBQ1gsR0FBRyxNQUFNLENBQUMsRUFBRSxVQUFVLFFBQVEsVUFBVSxXQUFXLGtCQUFrQjtnQkFDckUsbUJBQW1CLFFBQVEsa0JBQWtCLENBQUM7WUFFaEQsTUFBTSxJQUFJLEtBQUssQ0FBQyxPQUFPLENBQUMsQ0FBQztTQUMxQjtRQUVELE9BQU8sSUFBSSxtRUFBaUIsQ0FBQyxFQUFFLEdBQUcsRUFBRSxNQUFNLEVBQUUsQ0FBQyxDQUFDO0lBQ2hELENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSCxpRUFBZSxNQUFNLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWF0aGpheDItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIG1hdGhqYXgyLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7IEp1cHl0ZXJGcm9udEVuZFBsdWdpbiB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IFBhZ2VDb25maWcgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgTWF0aEpheFR5cGVzZXR0ZXIgfSBmcm9tICdAanVweXRlcmxhYi9tYXRoamF4Mic7XG5pbXBvcnQgeyBJTGF0ZXhUeXBlc2V0dGVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5cbi8qKlxuICogVGhlIE1hdGhKYXggbGF0ZXhUeXBlc2V0dGVyIHBsdWdpbi5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUxhdGV4VHlwZXNldHRlcj4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvbWF0aGpheDItZXh0ZW5zaW9uOnBsdWdpbicsXG4gIGF1dG9TdGFydDogdHJ1ZSxcbiAgcHJvdmlkZXM6IElMYXRleFR5cGVzZXR0ZXIsXG4gIGFjdGl2YXRlOiAoKSA9PiB7XG4gICAgY29uc3QgW3VybFBhcmFtLCBjb25maWdQYXJhbV0gPSBbJ2Z1bGxNYXRoamF4VXJsJywgJ21hdGhqYXhDb25maWcnXTtcbiAgICBjb25zdCB1cmwgPSBQYWdlQ29uZmlnLmdldE9wdGlvbih1cmxQYXJhbSk7XG4gICAgY29uc3QgY29uZmlnID0gUGFnZUNvbmZpZy5nZXRPcHRpb24oY29uZmlnUGFyYW0pO1xuXG4gICAgaWYgKCF1cmwpIHtcbiAgICAgIGNvbnN0IG1lc3NhZ2UgPVxuICAgICAgICBgJHtwbHVnaW4uaWR9IHVzZXMgJyR7dXJsUGFyYW19JyBhbmQgJyR7Y29uZmlnUGFyYW19JyBpbiBQYWdlQ29uZmlnIGAgK1xuICAgICAgICBgdG8gb3BlcmF0ZSBidXQgJyR7dXJsUGFyYW19JyB3YXMgbm90IGZvdW5kLmA7XG5cbiAgICAgIHRocm93IG5ldyBFcnJvcihtZXNzYWdlKTtcbiAgICB9XG5cbiAgICByZXR1cm4gbmV3IE1hdGhKYXhUeXBlc2V0dGVyKHsgdXJsLCBjb25maWcgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW4gYXMgZGVmYXVsdC5cbiAqL1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2luO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9