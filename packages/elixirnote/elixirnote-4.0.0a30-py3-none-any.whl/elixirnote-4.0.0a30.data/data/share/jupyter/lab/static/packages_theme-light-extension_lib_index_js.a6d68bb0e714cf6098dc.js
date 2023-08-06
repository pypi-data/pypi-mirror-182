"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_theme-light-extension_lib_index_js"],{

/***/ "../../packages/theme-light-extension/lib/index.js":
/*!*********************************************************!*\
  !*** ../../packages/theme-light-extension/lib/index.js ***!
  \*********************************************************/
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
 * @module theme-light-extension
 */


/**
 * A plugin for the Jupyter Light Theme.
 */
const plugin = {
    id: '@jupyterlab/theme-light-extension:plugin',
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.IThemeManager, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_1__.ITranslator],
    activate: (app, manager, translator) => {
        const trans = translator.load('jupyterlab');
        const style = '@jupyterlab/theme-light-extension/index.css';
        manager.register({
            name: 'JupyterLab Light',
            displayName: trans.__('JupyterLab Light'),
            isLight: true,
            themeScrollbars: false,
            load: () => manager.loadCSS(style),
            unload: () => Promise.resolve(undefined)
        });
    },
    autoStart: true
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdGhlbWUtbGlnaHQtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy5hNmQ2OGJiMGU3MTRjZjYwOThkYy5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTWtEO0FBQ0M7QUFFdEQ7O0dBRUc7QUFDSCxNQUFNLE1BQU0sR0FBZ0M7SUFDMUMsRUFBRSxFQUFFLDBDQUEwQztJQUM5QyxRQUFRLEVBQUUsQ0FBQywrREFBYSxFQUFFLGdFQUFXLENBQUM7SUFDdEMsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsT0FBc0IsRUFDdEIsVUFBdUIsRUFDdkIsRUFBRTtRQUNGLE1BQU0sS0FBSyxHQUFHLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDNUMsTUFBTSxLQUFLLEdBQUcsNkNBQTZDLENBQUM7UUFDNUQsT0FBTyxDQUFDLFFBQVEsQ0FBQztZQUNmLElBQUksRUFBRSxrQkFBa0I7WUFDeEIsV0FBVyxFQUFFLEtBQUssQ0FBQyxFQUFFLENBQUMsa0JBQWtCLENBQUM7WUFDekMsT0FBTyxFQUFFLElBQUk7WUFDYixlQUFlLEVBQUUsS0FBSztZQUN0QixJQUFJLEVBQUUsR0FBRyxFQUFFLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUM7WUFDbEMsTUFBTSxFQUFFLEdBQUcsRUFBRSxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUMsU0FBUyxDQUFDO1NBQ3pDLENBQUMsQ0FBQztJQUNMLENBQUM7SUFDRCxTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUYsaUVBQWUsTUFBTSxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RoZW1lLWxpZ2h0LWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgdGhlbWUtbGlnaHQtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgSVRoZW1lTWFuYWdlciB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIEEgcGx1Z2luIGZvciB0aGUgSnVweXRlciBMaWdodCBUaGVtZS5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvdGhlbWUtbGlnaHQtZXh0ZW5zaW9uOnBsdWdpbicsXG4gIHJlcXVpcmVzOiBbSVRoZW1lTWFuYWdlciwgSVRyYW5zbGF0b3JdLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIG1hbmFnZXI6IElUaGVtZU1hbmFnZXIsXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3JcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCBzdHlsZSA9ICdAanVweXRlcmxhYi90aGVtZS1saWdodC1leHRlbnNpb24vaW5kZXguY3NzJztcbiAgICBtYW5hZ2VyLnJlZ2lzdGVyKHtcbiAgICAgIG5hbWU6ICdKdXB5dGVyTGFiIExpZ2h0JyxcbiAgICAgIGRpc3BsYXlOYW1lOiB0cmFucy5fXygnSnVweXRlckxhYiBMaWdodCcpLFxuICAgICAgaXNMaWdodDogdHJ1ZSxcbiAgICAgIHRoZW1lU2Nyb2xsYmFyczogZmFsc2UsXG4gICAgICBsb2FkOiAoKSA9PiBtYW5hZ2VyLmxvYWRDU1Moc3R5bGUpLFxuICAgICAgdW5sb2FkOiAoKSA9PiBQcm9taXNlLnJlc29sdmUodW5kZWZpbmVkKVxuICAgIH0pO1xuICB9LFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbmV4cG9ydCBkZWZhdWx0IHBsdWdpbjtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==