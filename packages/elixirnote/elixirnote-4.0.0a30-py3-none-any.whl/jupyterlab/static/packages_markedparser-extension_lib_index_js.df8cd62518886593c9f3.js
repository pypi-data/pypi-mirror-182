"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_markedparser-extension_lib_index_js"],{

/***/ "../../packages/markedparser-extension/lib/index.js":
/*!**********************************************************!*\
  !*** ../../packages/markedparser-extension/lib/index.js ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var marked__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! marked */ "webpack/sharing/consume/default/marked/marked");
/* harmony import */ var marked__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(marked__WEBPACK_IMPORTED_MODULE_2__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module markedparser-extension
 */



/**
 * The markdown parser plugin.
 */
const plugin = {
    id: '@jupyterlab/markedparser-extension:plugin',
    autoStart: true,
    provides: _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_1__.IMarkdownParser,
    activate: () => {
        Private.initializeMarked();
        return {
            render: (content) => new Promise((resolve, reject) => {
                (0,marked__WEBPACK_IMPORTED_MODULE_2__.marked)(content, (err, content) => {
                    if (err) {
                        reject(err);
                    }
                    else {
                        resolve(content);
                    }
                });
            })
        };
    }
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
var Private;
(function (Private) {
    let markedInitialized = false;
    function initializeMarked() {
        if (markedInitialized) {
            return;
        }
        else {
            markedInitialized = true;
        }
        marked__WEBPACK_IMPORTED_MODULE_2__.marked.setOptions({
            gfm: true,
            sanitize: false,
            // breaks: true; We can't use GFM breaks as it causes problems with tables
            langPrefix: `language-`,
            highlight: (code, lang, callback) => {
                const cb = (err, code) => {
                    if (callback) {
                        callback(err, code);
                    }
                    return code;
                };
                if (!lang) {
                    // no language, no highlight
                    return cb(null, code);
                }
                _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__.Mode.ensure(lang)
                    .then(spec => {
                    const el = document.createElement('div');
                    if (!spec) {
                        console.error(`No CodeMirror mode: ${lang}`);
                        return cb(null, code);
                    }
                    try {
                        _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__.Mode.run(code, spec, el);
                        return cb(null, el.innerHTML);
                    }
                    catch (err) {
                        console.error(`Failed to highlight ${lang} code`, err);
                        return cb(err, code);
                    }
                })
                    .catch(err => {
                    console.error(`No CodeMirror mode: ${lang}`);
                    console.error(`Require CodeMirror mode error: ${err}`);
                    return cb(null, code);
                });
                return code;
            }
        });
    }
    Private.initializeMarked = initializeMarked;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWFya2VkcGFyc2VyLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuZGY4Y2Q2MjUxODg4NjU5M2M5ZjMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUcyQztBQUNXO0FBQ3pCO0FBRWhDOztHQUVHO0FBQ0gsTUFBTSxNQUFNLEdBQTJDO0lBQ3JELEVBQUUsRUFBRSwyQ0FBMkM7SUFDL0MsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsbUVBQWU7SUFDekIsUUFBUSxFQUFFLEdBQUcsRUFBRTtRQUNiLE9BQU8sQ0FBQyxnQkFBZ0IsRUFBRSxDQUFDO1FBQzNCLE9BQU87WUFDTCxNQUFNLEVBQUUsQ0FBQyxPQUFlLEVBQW1CLEVBQUUsQ0FDM0MsSUFBSSxPQUFPLENBQVMsQ0FBQyxPQUFPLEVBQUUsTUFBTSxFQUFFLEVBQUU7Z0JBQ3RDLDhDQUFNLENBQUMsT0FBTyxFQUFFLENBQUMsR0FBUSxFQUFFLE9BQWUsRUFBRSxFQUFFO29CQUM1QyxJQUFJLEdBQUcsRUFBRTt3QkFDUCxNQUFNLENBQUMsR0FBRyxDQUFDLENBQUM7cUJBQ2I7eUJBQU07d0JBQ0wsT0FBTyxDQUFDLE9BQU8sQ0FBQyxDQUFDO3FCQUNsQjtnQkFDSCxDQUFDLENBQUMsQ0FBQztZQUNMLENBQUMsQ0FBQztTQUNMLENBQUM7SUFDSixDQUFDO0NBQ0YsQ0FBQztBQUVGOztHQUVHO0FBQ0gsaUVBQWUsTUFBTSxFQUFDO0FBRXRCLElBQVUsT0FBTyxDQWlEaEI7QUFqREQsV0FBVSxPQUFPO0lBQ2YsSUFBSSxpQkFBaUIsR0FBRyxLQUFLLENBQUM7SUFDOUIsU0FBZ0IsZ0JBQWdCO1FBQzlCLElBQUksaUJBQWlCLEVBQUU7WUFDckIsT0FBTztTQUNSO2FBQU07WUFDTCxpQkFBaUIsR0FBRyxJQUFJLENBQUM7U0FDMUI7UUFFRCxxREFBaUIsQ0FBQztZQUNoQixHQUFHLEVBQUUsSUFBSTtZQUNULFFBQVEsRUFBRSxLQUFLO1lBQ2YsMEVBQTBFO1lBQzFFLFVBQVUsRUFBRSxXQUFXO1lBQ3ZCLFNBQVMsRUFBRSxDQUFDLElBQUksRUFBRSxJQUFJLEVBQUUsUUFBUSxFQUFFLEVBQUU7Z0JBQ2xDLE1BQU0sRUFBRSxHQUFHLENBQUMsR0FBaUIsRUFBRSxJQUFZLEVBQUUsRUFBRTtvQkFDN0MsSUFBSSxRQUFRLEVBQUU7d0JBQ1osUUFBUSxDQUFDLEdBQUcsRUFBRSxJQUFJLENBQUMsQ0FBQztxQkFDckI7b0JBQ0QsT0FBTyxJQUFJLENBQUM7Z0JBQ2QsQ0FBQyxDQUFDO2dCQUNGLElBQUksQ0FBQyxJQUFJLEVBQUU7b0JBQ1QsNEJBQTRCO29CQUM1QixPQUFPLEVBQUUsQ0FBQyxJQUFJLEVBQUUsSUFBSSxDQUFDLENBQUM7aUJBQ3ZCO2dCQUNELCtEQUFXLENBQUMsSUFBSSxDQUFDO3FCQUNkLElBQUksQ0FBQyxJQUFJLENBQUMsRUFBRTtvQkFDWCxNQUFNLEVBQUUsR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLEtBQUssQ0FBQyxDQUFDO29CQUN6QyxJQUFJLENBQUMsSUFBSSxFQUFFO3dCQUNULE9BQU8sQ0FBQyxLQUFLLENBQUMsdUJBQXVCLElBQUksRUFBRSxDQUFDLENBQUM7d0JBQzdDLE9BQU8sRUFBRSxDQUFDLElBQUksRUFBRSxJQUFJLENBQUMsQ0FBQztxQkFDdkI7b0JBQ0QsSUFBSTt3QkFDRiw0REFBUSxDQUFDLElBQUksRUFBRSxJQUFJLEVBQUUsRUFBRSxDQUFDLENBQUM7d0JBQ3pCLE9BQU8sRUFBRSxDQUFDLElBQUksRUFBRSxFQUFFLENBQUMsU0FBUyxDQUFDLENBQUM7cUJBQy9CO29CQUFDLE9BQU8sR0FBRyxFQUFFO3dCQUNaLE9BQU8sQ0FBQyxLQUFLLENBQUMsdUJBQXVCLElBQUksT0FBTyxFQUFFLEdBQUcsQ0FBQyxDQUFDO3dCQUN2RCxPQUFPLEVBQUUsQ0FBQyxHQUFHLEVBQUUsSUFBSSxDQUFDLENBQUM7cUJBQ3RCO2dCQUNILENBQUMsQ0FBQztxQkFDRCxLQUFLLENBQUMsR0FBRyxDQUFDLEVBQUU7b0JBQ1gsT0FBTyxDQUFDLEtBQUssQ0FBQyx1QkFBdUIsSUFBSSxFQUFFLENBQUMsQ0FBQztvQkFDN0MsT0FBTyxDQUFDLEtBQUssQ0FBQyxrQ0FBa0MsR0FBRyxFQUFFLENBQUMsQ0FBQztvQkFDdkQsT0FBTyxFQUFFLENBQUMsSUFBSSxFQUFFLElBQUksQ0FBQyxDQUFDO2dCQUN4QixDQUFDLENBQUMsQ0FBQztnQkFDTCxPQUFPLElBQUksQ0FBQztZQUNkLENBQUM7U0FDRixDQUFDLENBQUM7SUFDTCxDQUFDO0lBOUNlLHdCQUFnQixtQkE4Qy9CO0FBQ0gsQ0FBQyxFQWpEUyxPQUFPLEtBQVAsT0FBTyxRQWlEaEIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFya2VkcGFyc2VyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBtYXJrZWRwYXJzZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHsgSnVweXRlckZyb250RW5kUGx1Z2luIH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgTW9kZSB9IGZyb20gJ0BqdXB5dGVybGFiL2NvZGVtaXJyb3InO1xuaW1wb3J0IHsgSU1hcmtkb3duUGFyc2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyBtYXJrZWQgfSBmcm9tICdtYXJrZWQnO1xuXG4vKipcbiAqIFRoZSBtYXJrZG93biBwYXJzZXIgcGx1Z2luLlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJTWFya2Rvd25QYXJzZXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL21hcmtlZHBhcnNlci1leHRlbnNpb246cGx1Z2luJyxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBwcm92aWRlczogSU1hcmtkb3duUGFyc2VyLFxuICBhY3RpdmF0ZTogKCkgPT4ge1xuICAgIFByaXZhdGUuaW5pdGlhbGl6ZU1hcmtlZCgpO1xuICAgIHJldHVybiB7XG4gICAgICByZW5kZXI6IChjb250ZW50OiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4gPT5cbiAgICAgICAgbmV3IFByb21pc2U8c3RyaW5nPigocmVzb2x2ZSwgcmVqZWN0KSA9PiB7XG4gICAgICAgICAgbWFya2VkKGNvbnRlbnQsIChlcnI6IGFueSwgY29udGVudDogc3RyaW5nKSA9PiB7XG4gICAgICAgICAgICBpZiAoZXJyKSB7XG4gICAgICAgICAgICAgIHJlamVjdChlcnIpO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgcmVzb2x2ZShjb250ZW50KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9KTtcbiAgICAgICAgfSlcbiAgICB9O1xuICB9XG59O1xuXG4vKipcbiAqIEV4cG9ydCB0aGUgcGx1Z2luIGFzIGRlZmF1bHQuXG4gKi9cbmV4cG9ydCBkZWZhdWx0IHBsdWdpbjtcblxubmFtZXNwYWNlIFByaXZhdGUge1xuICBsZXQgbWFya2VkSW5pdGlhbGl6ZWQgPSBmYWxzZTtcbiAgZXhwb3J0IGZ1bmN0aW9uIGluaXRpYWxpemVNYXJrZWQoKTogdm9pZCB7XG4gICAgaWYgKG1hcmtlZEluaXRpYWxpemVkKSB7XG4gICAgICByZXR1cm47XG4gICAgfSBlbHNlIHtcbiAgICAgIG1hcmtlZEluaXRpYWxpemVkID0gdHJ1ZTtcbiAgICB9XG5cbiAgICBtYXJrZWQuc2V0T3B0aW9ucyh7XG4gICAgICBnZm06IHRydWUsXG4gICAgICBzYW5pdGl6ZTogZmFsc2UsXG4gICAgICAvLyBicmVha3M6IHRydWU7IFdlIGNhbid0IHVzZSBHRk0gYnJlYWtzIGFzIGl0IGNhdXNlcyBwcm9ibGVtcyB3aXRoIHRhYmxlc1xuICAgICAgbGFuZ1ByZWZpeDogYGxhbmd1YWdlLWAsXG4gICAgICBoaWdobGlnaHQ6IChjb2RlLCBsYW5nLCBjYWxsYmFjaykgPT4ge1xuICAgICAgICBjb25zdCBjYiA9IChlcnI6IEVycm9yIHwgbnVsbCwgY29kZTogc3RyaW5nKSA9PiB7XG4gICAgICAgICAgaWYgKGNhbGxiYWNrKSB7XG4gICAgICAgICAgICBjYWxsYmFjayhlcnIsIGNvZGUpO1xuICAgICAgICAgIH1cbiAgICAgICAgICByZXR1cm4gY29kZTtcbiAgICAgICAgfTtcbiAgICAgICAgaWYgKCFsYW5nKSB7XG4gICAgICAgICAgLy8gbm8gbGFuZ3VhZ2UsIG5vIGhpZ2hsaWdodFxuICAgICAgICAgIHJldHVybiBjYihudWxsLCBjb2RlKTtcbiAgICAgICAgfVxuICAgICAgICBNb2RlLmVuc3VyZShsYW5nKVxuICAgICAgICAgIC50aGVuKHNwZWMgPT4ge1xuICAgICAgICAgICAgY29uc3QgZWwgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgICAgICAgICAgIGlmICghc3BlYykge1xuICAgICAgICAgICAgICBjb25zb2xlLmVycm9yKGBObyBDb2RlTWlycm9yIG1vZGU6ICR7bGFuZ31gKTtcbiAgICAgICAgICAgICAgcmV0dXJuIGNiKG51bGwsIGNvZGUpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgdHJ5IHtcbiAgICAgICAgICAgICAgTW9kZS5ydW4oY29kZSwgc3BlYywgZWwpO1xuICAgICAgICAgICAgICByZXR1cm4gY2IobnVsbCwgZWwuaW5uZXJIVE1MKTtcbiAgICAgICAgICAgIH0gY2F0Y2ggKGVycikge1xuICAgICAgICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gaGlnaGxpZ2h0ICR7bGFuZ30gY29kZWAsIGVycik7XG4gICAgICAgICAgICAgIHJldHVybiBjYihlcnIsIGNvZGUpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH0pXG4gICAgICAgICAgLmNhdGNoKGVyciA9PiB7XG4gICAgICAgICAgICBjb25zb2xlLmVycm9yKGBObyBDb2RlTWlycm9yIG1vZGU6ICR7bGFuZ31gKTtcbiAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoYFJlcXVpcmUgQ29kZU1pcnJvciBtb2RlIGVycm9yOiAke2Vycn1gKTtcbiAgICAgICAgICAgIHJldHVybiBjYihudWxsLCBjb2RlKTtcbiAgICAgICAgICB9KTtcbiAgICAgICAgcmV0dXJuIGNvZGU7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==