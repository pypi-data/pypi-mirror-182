"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_docprovider-extension_lib_index_js-_33740"],{

/***/ "../../packages/docprovider-extension/lib/index.js":
/*!*********************************************************!*\
  !*** ../../packages/docprovider-extension/lib/index.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docprovider */ "webpack/sharing/consume/default/@jupyterlab/docprovider/@jupyterlab/docprovider");
/* harmony import */ var _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/collaboration */ "webpack/sharing/consume/default/@jupyterlab/collaboration/@jupyterlab/collaboration");
/* harmony import */ var _jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module docprovider-extension
 */




/**
 * The default document provider plugin
 */
const docProviderPlugin = {
    id: '@jupyterlab/docprovider-extension:plugin',
    requires: [_jupyterlab_collaboration__WEBPACK_IMPORTED_MODULE_2__.ICurrentUser],
    provides: _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1__.IDocumentProviderFactory,
    activate: (app, user) => {
        const server = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__.ServerConnection.makeSettings();
        const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(server.wsUrl, 'api/yjs');
        const collaborative = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.PageConfig.getOption('collaborative') == 'true' ? true : false;
        const factory = (options) => {
            return collaborative
                ? new _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1__.WebSocketProvider(Object.assign(Object.assign({}, options), { url,
                    user }))
                : new _jupyterlab_docprovider__WEBPACK_IMPORTED_MODULE_1__.ProviderMock();
        };
        return factory;
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [docProviderPlugin];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZG9jcHJvdmlkZXItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fMzM3NDAuZWRiYjY0YmQyZDk1MDEzOTlkZjYuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFNd0Q7QUFNMUI7QUFDd0I7QUFDRDtBQUV4RDs7R0FFRztBQUNILE1BQU0saUJBQWlCLEdBQW9EO0lBQ3pFLEVBQUUsRUFBRSwwQ0FBMEM7SUFDOUMsUUFBUSxFQUFFLENBQUMsbUVBQVksQ0FBQztJQUN4QixRQUFRLEVBQUUsNkVBQXdCO0lBQ2xDLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLElBQWtCLEVBQ1EsRUFBRTtRQUM1QixNQUFNLE1BQU0sR0FBRywrRUFBNkIsRUFBRSxDQUFDO1FBQy9DLE1BQU0sR0FBRyxHQUFHLDhEQUFXLENBQUMsTUFBTSxDQUFDLEtBQUssRUFBRSxTQUFTLENBQUMsQ0FBQztRQUNqRCxNQUFNLGFBQWEsR0FDakIsdUVBQW9CLENBQUMsZUFBZSxDQUFDLElBQUksTUFBTSxDQUFDLENBQUMsQ0FBQyxJQUFJLENBQUMsQ0FBQyxDQUFDLEtBQUssQ0FBQztRQUNqRSxNQUFNLE9BQU8sR0FBRyxDQUNkLE9BQTBDLEVBQ3ZCLEVBQUU7WUFDckIsT0FBTyxhQUFhO2dCQUNsQixDQUFDLENBQUMsSUFBSSxzRUFBaUIsaUNBQ2hCLE9BQU8sS0FDVixHQUFHO29CQUNILElBQUksSUFDSjtnQkFDSixDQUFDLENBQUMsSUFBSSxpRUFBWSxFQUFFLENBQUM7UUFDekIsQ0FBQyxDQUFDO1FBQ0YsT0FBTyxPQUFPLENBQUM7SUFDakIsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFpQyxDQUFDLGlCQUFpQixDQUFDLENBQUM7QUFDbEUsaUVBQWUsT0FBTyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RvY3Byb3ZpZGVyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgZG9jcHJvdmlkZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgUGFnZUNvbmZpZywgVVJMRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIElEb2N1bWVudFByb3ZpZGVyLFxuICBJRG9jdW1lbnRQcm92aWRlckZhY3RvcnksXG4gIFByb3ZpZGVyTW9jayxcbiAgV2ViU29ja2V0UHJvdmlkZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jcHJvdmlkZXInO1xuaW1wb3J0IHsgSUN1cnJlbnRVc2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbic7XG5pbXBvcnQgeyBTZXJ2ZXJDb25uZWN0aW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IGRvY3VtZW50IHByb3ZpZGVyIHBsdWdpblxuICovXG5jb25zdCBkb2NQcm92aWRlclBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPElEb2N1bWVudFByb3ZpZGVyRmFjdG9yeT4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZG9jcHJvdmlkZXItZXh0ZW5zaW9uOnBsdWdpbicsXG4gIHJlcXVpcmVzOiBbSUN1cnJlbnRVc2VyXSxcbiAgcHJvdmlkZXM6IElEb2N1bWVudFByb3ZpZGVyRmFjdG9yeSxcbiAgYWN0aXZhdGU6IChcbiAgICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgICB1c2VyOiBJQ3VycmVudFVzZXJcbiAgKTogSURvY3VtZW50UHJvdmlkZXJGYWN0b3J5ID0+IHtcbiAgICBjb25zdCBzZXJ2ZXIgPSBTZXJ2ZXJDb25uZWN0aW9uLm1ha2VTZXR0aW5ncygpO1xuICAgIGNvbnN0IHVybCA9IFVSTEV4dC5qb2luKHNlcnZlci53c1VybCwgJ2FwaS95anMnKTtcbiAgICBjb25zdCBjb2xsYWJvcmF0aXZlID1cbiAgICAgIFBhZ2VDb25maWcuZ2V0T3B0aW9uKCdjb2xsYWJvcmF0aXZlJykgPT0gJ3RydWUnID8gdHJ1ZSA6IGZhbHNlO1xuICAgIGNvbnN0IGZhY3RvcnkgPSAoXG4gICAgICBvcHRpb25zOiBJRG9jdW1lbnRQcm92aWRlckZhY3RvcnkuSU9wdGlvbnNcbiAgICApOiBJRG9jdW1lbnRQcm92aWRlciA9PiB7XG4gICAgICByZXR1cm4gY29sbGFib3JhdGl2ZVxuICAgICAgICA/IG5ldyBXZWJTb2NrZXRQcm92aWRlcih7XG4gICAgICAgICAgICAuLi5vcHRpb25zLFxuICAgICAgICAgICAgdXJsLFxuICAgICAgICAgICAgdXNlclxuICAgICAgICAgIH0pXG4gICAgICAgIDogbmV3IFByb3ZpZGVyTW9jaygpO1xuICAgIH07XG4gICAgcmV0dXJuIGZhY3Rvcnk7XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbZG9jUHJvdmlkZXJQbHVnaW5dO1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==