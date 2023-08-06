"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_cell-toolbar-extension_lib_index_js"],{

/***/ "../../packages/cell-toolbar-extension/lib/index.js":
/*!**********************************************************!*\
  !*** ../../packages/cell-toolbar-extension/lib/index.js ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_cell_toolbar__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/cell-toolbar */ "webpack/sharing/consume/default/@jupyterlab/cell-toolbar/@jupyterlab/cell-toolbar");
/* harmony import */ var _jupyterlab_cell_toolbar__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_cell_toolbar__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module cell-toolbar-extension
 */




const cellToolbar = {
    id: '@jupyterlab/cell-toolbar-extension:plugin',
    autoStart: true,
    activate: async (app, settingRegistry, toolbarRegistry, translator) => {
        const toolbarItems = settingRegistry && toolbarRegistry
            ? (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.createToolbarFactory)(toolbarRegistry, settingRegistry, _jupyterlab_cell_toolbar__WEBPACK_IMPORTED_MODULE_1__.CellBarExtension.FACTORY_NAME, cellToolbar.id, translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator)
            : undefined;
        app.docRegistry.addWidgetExtension('Notebook', new _jupyterlab_cell_toolbar__WEBPACK_IMPORTED_MODULE_1__.CellBarExtension(app.commands, toolbarItems));
    },
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.IToolbarWidgetRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.ITranslator]
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (cellToolbar);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY2VsbC10b29sYmFyLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuMjRlNGE5YTIzNjk0YjZmNDBkMmMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7OzsrRUFHK0U7QUFDL0U7OztHQUdHO0FBTTREO0FBQ0g7QUFJOUI7QUFDd0M7QUFFdEUsTUFBTSxXQUFXLEdBQWdDO0lBQy9DLEVBQUUsRUFBRSwyQ0FBMkM7SUFDL0MsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsS0FBSyxFQUNiLEdBQW9CLEVBQ3BCLGVBQXdDLEVBQ3hDLGVBQThDLEVBQzlDLFVBQThCLEVBQzlCLEVBQUU7UUFDRixNQUFNLFlBQVksR0FDaEIsZUFBZSxJQUFJLGVBQWU7WUFDaEMsQ0FBQyxDQUFDLDBFQUFvQixDQUNsQixlQUFlLEVBQ2YsZUFBZSxFQUNmLG1GQUE2QixFQUM3QixXQUFXLENBQUMsRUFBRSxFQUNkLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQzdCO1lBQ0gsQ0FBQyxDQUFDLFNBQVMsQ0FBQztRQUVoQixHQUFHLENBQUMsV0FBVyxDQUFDLGtCQUFrQixDQUNoQyxVQUFVLEVBQ1YsSUFBSSxzRUFBZ0IsQ0FBQyxHQUFHLENBQUMsUUFBUSxFQUFFLFlBQVksQ0FBQyxDQUNqRCxDQUFDO0lBQ0osQ0FBQztJQUNELFFBQVEsRUFBRSxDQUFDLHlFQUFnQixFQUFFLHdFQUFzQixFQUFFLGdFQUFXLENBQUM7Q0FDbEUsQ0FBQztBQUVGLGlFQUFlLFdBQVcsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jZWxsLXRvb2xiYXItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGNlbGwtdG9vbGJhci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IENlbGxCYXJFeHRlbnNpb24gfSBmcm9tICdAanVweXRlcmxhYi9jZWxsLXRvb2xiYXInO1xuaW1wb3J0IHtcbiAgY3JlYXRlVG9vbGJhckZhY3RvcnksXG4gIElUb29sYmFyV2lkZ2V0UmVnaXN0cnlcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIG51bGxUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG5jb25zdCBjZWxsVG9vbGJhcjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2NlbGwtdG9vbGJhci1leHRlbnNpb246cGx1Z2luJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogYXN5bmMgKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSB8IG51bGwsXG4gICAgdG9vbGJhclJlZ2lzdHJ5OiBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5IHwgbnVsbCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdG9vbGJhckl0ZW1zID1cbiAgICAgIHNldHRpbmdSZWdpc3RyeSAmJiB0b29sYmFyUmVnaXN0cnlcbiAgICAgICAgPyBjcmVhdGVUb29sYmFyRmFjdG9yeShcbiAgICAgICAgICAgIHRvb2xiYXJSZWdpc3RyeSxcbiAgICAgICAgICAgIHNldHRpbmdSZWdpc3RyeSxcbiAgICAgICAgICAgIENlbGxCYXJFeHRlbnNpb24uRkFDVE9SWV9OQU1FLFxuICAgICAgICAgICAgY2VsbFRvb2xiYXIuaWQsXG4gICAgICAgICAgICB0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yXG4gICAgICAgICAgKVxuICAgICAgICA6IHVuZGVmaW5lZDtcblxuICAgIGFwcC5kb2NSZWdpc3RyeS5hZGRXaWRnZXRFeHRlbnNpb24oXG4gICAgICAnTm90ZWJvb2snLFxuICAgICAgbmV3IENlbGxCYXJFeHRlbnNpb24oYXBwLmNvbW1hbmRzLCB0b29sYmFySXRlbXMpXG4gICAgKTtcbiAgfSxcbiAgb3B0aW9uYWw6IFtJU2V0dGluZ1JlZ2lzdHJ5LCBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5LCBJVHJhbnNsYXRvcl1cbn07XG5cbmV4cG9ydCBkZWZhdWx0IGNlbGxUb29sYmFyO1xuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9