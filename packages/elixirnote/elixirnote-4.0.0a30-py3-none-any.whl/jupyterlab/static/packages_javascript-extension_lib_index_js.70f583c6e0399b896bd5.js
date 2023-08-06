"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_javascript-extension_lib_index_js"],{

/***/ "../../packages/javascript-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/javascript-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "APPLICATION_JAVASCRIPT_MIMETYPE": () => (/* binding */ APPLICATION_JAVASCRIPT_MIMETYPE),
/* harmony export */   "ExperimentalRenderedJavascript": () => (/* binding */ ExperimentalRenderedJavascript),
/* harmony export */   "TEXT_JAVASCRIPT_MIMETYPE": () => (/* binding */ TEXT_JAVASCRIPT_MIMETYPE),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "rendererFactory": () => (/* binding */ rendererFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module javascript-extension
 */

const TEXT_JAVASCRIPT_MIMETYPE = 'text/javascript';
const APPLICATION_JAVASCRIPT_MIMETYPE = 'application/javascript';
function evalInContext(code, element, document, window) {
    // eslint-disable-next-line
    return eval(code);
}
class ExperimentalRenderedJavascript extends _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.RenderedJavaScript {
    render(model) {
        const trans = this.translator.load('jupyterlab');
        const renderJavascript = () => {
            try {
                const data = model.data[this.mimeType];
                if (data) {
                    evalInContext(data, this.node, document, window);
                }
                return Promise.resolve();
            }
            catch (error) {
                return Promise.reject(error);
            }
        };
        if (!model.trusted) {
            // If output is not trusted or if arbitrary Javascript execution is not enabled, render an informative error message
            const pre = document.createElement('pre');
            pre.textContent = trans.__('Are you sure that you want to run arbitrary Javascript within your JupyterLab session?');
            const button = document.createElement('button');
            button.textContent = trans.__('Run');
            this.node.appendChild(pre);
            this.node.appendChild(button);
            button.onclick = event => {
                this.node.textContent = '';
                void renderJavascript();
            };
            return Promise.resolve();
        }
        return renderJavascript();
    }
}
/**
 * A mime renderer factory for text/javascript data.
 */
const rendererFactory = {
    safe: false,
    mimeTypes: [TEXT_JAVASCRIPT_MIMETYPE, APPLICATION_JAVASCRIPT_MIMETYPE],
    createRenderer: options => new ExperimentalRenderedJavascript(options)
};
const extension = {
    id: '@jupyterlab/javascript-extension:factory',
    rendererFactory,
    rank: 0,
    dataType: 'string'
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfamF2YXNjcmlwdC1leHRlbnNpb25fbGliX2luZGV4X2pzLjcwZjU4M2M2ZTAzOTliODk2YmQ1LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQUV5RDtBQUdyRCxNQUFNLHdCQUF3QixHQUFHLGlCQUFpQixDQUFDO0FBQ25ELE1BQU0sK0JBQStCLEdBQUcsd0JBQXdCLENBQUM7QUFFeEUsU0FBUyxhQUFhLENBQ3BCLElBQVksRUFDWixPQUFnQixFQUNoQixRQUFrQixFQUNsQixNQUFjO0lBRWQsMkJBQTJCO0lBQzNCLE9BQU8sSUFBSSxDQUFDLElBQUksQ0FBQyxDQUFDO0FBQ3BCLENBQUM7QUFFTSxNQUFNLDhCQUErQixTQUFRLHNFQUFrQjtJQUNwRSxNQUFNLENBQUMsS0FBNkI7UUFDbEMsTUFBTSxLQUFLLEdBQUcsSUFBSSxDQUFDLFVBQVUsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7UUFDakQsTUFBTSxnQkFBZ0IsR0FBRyxHQUFHLEVBQUU7WUFDNUIsSUFBSTtnQkFDRixNQUFNLElBQUksR0FBRyxLQUFLLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxRQUFRLENBQXVCLENBQUM7Z0JBQzdELElBQUksSUFBSSxFQUFFO29CQUNSLGFBQWEsQ0FBQyxJQUFJLEVBQUUsSUFBSSxDQUFDLElBQUksRUFBRSxRQUFRLEVBQUUsTUFBTSxDQUFDLENBQUM7aUJBQ2xEO2dCQUNELE9BQU8sT0FBTyxDQUFDLE9BQU8sRUFBRSxDQUFDO2FBQzFCO1lBQUMsT0FBTyxLQUFLLEVBQUU7Z0JBQ2QsT0FBTyxPQUFPLENBQUMsTUFBTSxDQUFDLEtBQUssQ0FBQyxDQUFDO2FBQzlCO1FBQ0gsQ0FBQyxDQUFDO1FBQ0YsSUFBSSxDQUFDLEtBQUssQ0FBQyxPQUFPLEVBQUU7WUFDbEIsb0hBQW9IO1lBQ3BILE1BQU0sR0FBRyxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsS0FBSyxDQUFDLENBQUM7WUFDMUMsR0FBRyxDQUFDLFdBQVcsR0FBRyxLQUFLLENBQUMsRUFBRSxDQUN4Qix3RkFBd0YsQ0FDekYsQ0FBQztZQUNGLE1BQU0sTUFBTSxHQUFHLFFBQVEsQ0FBQyxhQUFhLENBQUMsUUFBUSxDQUFDLENBQUM7WUFDaEQsTUFBTSxDQUFDLFdBQVcsR0FBRyxLQUFLLENBQUMsRUFBRSxDQUFDLEtBQUssQ0FBQyxDQUFDO1lBRXJDLElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLEdBQUcsQ0FBQyxDQUFDO1lBQzNCLElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1lBRTlCLE1BQU0sQ0FBQyxPQUFPLEdBQUcsS0FBSyxDQUFDLEVBQUU7Z0JBQ3ZCLElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxHQUFHLEVBQUUsQ0FBQztnQkFDM0IsS0FBSyxnQkFBZ0IsRUFBRSxDQUFDO1lBQzFCLENBQUMsQ0FBQztZQUNGLE9BQU8sT0FBTyxDQUFDLE9BQU8sRUFBRSxDQUFDO1NBQzFCO1FBQ0QsT0FBTyxnQkFBZ0IsRUFBRSxDQUFDO0lBQzVCLENBQUM7Q0FDRjtBQUVEOztHQUVHO0FBQ0ksTUFBTSxlQUFlLEdBQWlDO0lBQzNELElBQUksRUFBRSxLQUFLO0lBQ1gsU0FBUyxFQUFFLENBQUMsd0JBQXdCLEVBQUUsK0JBQStCLENBQUM7SUFDdEUsY0FBYyxFQUFFLE9BQU8sQ0FBQyxFQUFFLENBQUMsSUFBSSw4QkFBOEIsQ0FBQyxPQUFPLENBQUM7Q0FDdkUsQ0FBQztBQUVGLE1BQU0sU0FBUyxHQUEyQjtJQUN4QyxFQUFFLEVBQUUsMENBQTBDO0lBQzlDLGVBQWU7SUFDZixJQUFJLEVBQUUsQ0FBQztJQUNQLFFBQVEsRUFBRSxRQUFRO0NBQ25CLENBQUM7QUFFRixpRUFBZSxTQUFTLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvamF2YXNjcmlwdC1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGphdmFzY3JpcHQtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHsgUmVuZGVyZWRKYXZhU2NyaXB0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyBJUmVuZGVyTWltZSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUtaW50ZXJmYWNlcyc7XG5cbmV4cG9ydCBjb25zdCBURVhUX0pBVkFTQ1JJUFRfTUlNRVRZUEUgPSAndGV4dC9qYXZhc2NyaXB0JztcbmV4cG9ydCBjb25zdCBBUFBMSUNBVElPTl9KQVZBU0NSSVBUX01JTUVUWVBFID0gJ2FwcGxpY2F0aW9uL2phdmFzY3JpcHQnO1xuXG5mdW5jdGlvbiBldmFsSW5Db250ZXh0KFxuICBjb2RlOiBzdHJpbmcsXG4gIGVsZW1lbnQ6IEVsZW1lbnQsXG4gIGRvY3VtZW50OiBEb2N1bWVudCxcbiAgd2luZG93OiBXaW5kb3dcbikge1xuICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmVcbiAgcmV0dXJuIGV2YWwoY29kZSk7XG59XG5cbmV4cG9ydCBjbGFzcyBFeHBlcmltZW50YWxSZW5kZXJlZEphdmFzY3JpcHQgZXh0ZW5kcyBSZW5kZXJlZEphdmFTY3JpcHQge1xuICByZW5kZXIobW9kZWw6IElSZW5kZXJNaW1lLklNaW1lTW9kZWwpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBjb25zdCB0cmFucyA9IHRoaXMudHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgY29uc3QgcmVuZGVySmF2YXNjcmlwdCA9ICgpID0+IHtcbiAgICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IGRhdGEgPSBtb2RlbC5kYXRhW3RoaXMubWltZVR5cGVdIGFzIHN0cmluZyB8IHVuZGVmaW5lZDtcbiAgICAgICAgaWYgKGRhdGEpIHtcbiAgICAgICAgICBldmFsSW5Db250ZXh0KGRhdGEsIHRoaXMubm9kZSwgZG9jdW1lbnQsIHdpbmRvdyk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSgpO1xuICAgICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgcmV0dXJuIFByb21pc2UucmVqZWN0KGVycm9yKTtcbiAgICAgIH1cbiAgICB9O1xuICAgIGlmICghbW9kZWwudHJ1c3RlZCkge1xuICAgICAgLy8gSWYgb3V0cHV0IGlzIG5vdCB0cnVzdGVkIG9yIGlmIGFyYml0cmFyeSBKYXZhc2NyaXB0IGV4ZWN1dGlvbiBpcyBub3QgZW5hYmxlZCwgcmVuZGVyIGFuIGluZm9ybWF0aXZlIGVycm9yIG1lc3NhZ2VcbiAgICAgIGNvbnN0IHByZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ3ByZScpO1xuICAgICAgcHJlLnRleHRDb250ZW50ID0gdHJhbnMuX18oXG4gICAgICAgICdBcmUgeW91IHN1cmUgdGhhdCB5b3Ugd2FudCB0byBydW4gYXJiaXRyYXJ5IEphdmFzY3JpcHQgd2l0aGluIHlvdXIgSnVweXRlckxhYiBzZXNzaW9uPydcbiAgICAgICk7XG4gICAgICBjb25zdCBidXR0b24gPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdidXR0b24nKTtcbiAgICAgIGJ1dHRvbi50ZXh0Q29udGVudCA9IHRyYW5zLl9fKCdSdW4nKTtcblxuICAgICAgdGhpcy5ub2RlLmFwcGVuZENoaWxkKHByZSk7XG4gICAgICB0aGlzLm5vZGUuYXBwZW5kQ2hpbGQoYnV0dG9uKTtcblxuICAgICAgYnV0dG9uLm9uY2xpY2sgPSBldmVudCA9PiB7XG4gICAgICAgIHRoaXMubm9kZS50ZXh0Q29udGVudCA9ICcnO1xuICAgICAgICB2b2lkIHJlbmRlckphdmFzY3JpcHQoKTtcbiAgICAgIH07XG4gICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKCk7XG4gICAgfVxuICAgIHJldHVybiByZW5kZXJKYXZhc2NyaXB0KCk7XG4gIH1cbn1cblxuLyoqXG4gKiBBIG1pbWUgcmVuZGVyZXIgZmFjdG9yeSBmb3IgdGV4dC9qYXZhc2NyaXB0IGRhdGEuXG4gKi9cbmV4cG9ydCBjb25zdCByZW5kZXJlckZhY3Rvcnk6IElSZW5kZXJNaW1lLklSZW5kZXJlckZhY3RvcnkgPSB7XG4gIHNhZmU6IGZhbHNlLFxuICBtaW1lVHlwZXM6IFtURVhUX0pBVkFTQ1JJUFRfTUlNRVRZUEUsIEFQUExJQ0FUSU9OX0pBVkFTQ1JJUFRfTUlNRVRZUEVdLFxuICBjcmVhdGVSZW5kZXJlcjogb3B0aW9ucyA9PiBuZXcgRXhwZXJpbWVudGFsUmVuZGVyZWRKYXZhc2NyaXB0KG9wdGlvbnMpXG59O1xuXG5jb25zdCBleHRlbnNpb246IElSZW5kZXJNaW1lLklFeHRlbnNpb24gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvamF2YXNjcmlwdC1leHRlbnNpb246ZmFjdG9yeScsXG4gIHJlbmRlcmVyRmFjdG9yeSxcbiAgcmFuazogMCxcbiAgZGF0YVR5cGU6ICdzdHJpbmcnXG59O1xuXG5leHBvcnQgZGVmYXVsdCBleHRlbnNpb247XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=