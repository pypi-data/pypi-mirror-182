"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_mathjax2_lib_index_js"],{

/***/ "../../packages/mathjax2/lib/index.js":
/*!********************************************!*\
  !*** ../../packages/mathjax2/lib/index.js ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MathJaxTypesetter": () => (/* binding */ MathJaxTypesetter)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module mathjax2
 */

/**
 * The MathJax Typesetter.
 */
class MathJaxTypesetter {
    /**
     * Create a new MathJax typesetter.
     */
    constructor(options) {
        this._initPromise = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.PromiseDelegate();
        this._initialized = false;
        this._url = options.url;
        this._config = options.config;
    }
    /**
     * Typeset the math in a node.
     *
     * #### Notes
     * MathJax schedules the typesetting asynchronously,
     * but there are not currently any callbacks or Promises
     * firing when it is done.
     */
    typeset(node) {
        if (!this._initialized) {
            this._init();
        }
        void this._initPromise.promise.then(() => {
            MathJax.Hub.Queue(['Typeset', MathJax.Hub, node]);
            try {
                MathJax.Hub.Queue(['Require', MathJax.Ajax, '[MathJax]/extensions/TeX/AMSmath.js'], () => {
                    MathJax.InputJax.TeX.resetEquationNumbers();
                });
            }
            catch (e) {
                console.error('Error queueing resetEquationNumbers:', e);
            }
        });
    }
    /**
     * Initialize MathJax.
     */
    _init() {
        const head = document.getElementsByTagName('head')[0];
        const script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = `${this._url}?config=${this._config}&amp;delayStartupUntil=configured`;
        script.charset = 'utf-8';
        head.appendChild(script);
        script.addEventListener('load', () => {
            this._onLoad();
        });
        this._initialized = true;
    }
    /**
     * Handle MathJax loading.
     */
    _onLoad() {
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [
                    ['$', '$'],
                    ['\\(', '\\)']
                ],
                displayMath: [
                    ['$$', '$$'],
                    ['\\[', '\\]']
                ],
                processEscapes: true,
                processEnvironments: true
            },
            // Center justify equations in code and markdown cells. Elsewhere
            // we use CSS to left justify single line equations in code cells.
            displayAlign: 'center',
            CommonHTML: {
                linebreaks: { automatic: true }
            },
            'HTML-CSS': {
                availableFonts: [],
                imageFont: null,
                preferredFont: null,
                webFont: 'STIX-Web',
                styles: { '.MathJax_Display': { margin: 0 } },
                linebreaks: { automatic: true }
            },
            skipStartupTypeset: true,
            messageStyle: 'none'
        });
        MathJax.Hub.Configured();
        this._initPromise.resolve(void 0);
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWF0aGpheDJfbGliX2luZGV4X2pzLjJjZTNkNDk2ZjgwMGQzM2QxZGVlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUdpRDtBQUtwRDs7R0FFRztBQUNJLE1BQU0saUJBQWlCO0lBQzVCOztPQUVHO0lBQ0gsWUFBWSxPQUFtQztRQXNGdkMsaUJBQVksR0FBRyxJQUFJLDhEQUFlLEVBQVEsQ0FBQztRQUMzQyxpQkFBWSxHQUFHLEtBQUssQ0FBQztRQXRGM0IsSUFBSSxDQUFDLElBQUksR0FBRyxPQUFPLENBQUMsR0FBRyxDQUFDO1FBQ3hCLElBQUksQ0FBQyxPQUFPLEdBQUcsT0FBTyxDQUFDLE1BQU0sQ0FBQztJQUNoQyxDQUFDO0lBRUQ7Ozs7Ozs7T0FPRztJQUNILE9BQU8sQ0FBQyxJQUFpQjtRQUN2QixJQUFJLENBQUMsSUFBSSxDQUFDLFlBQVksRUFBRTtZQUN0QixJQUFJLENBQUMsS0FBSyxFQUFFLENBQUM7U0FDZDtRQUNELEtBQUssSUFBSSxDQUFDLFlBQVksQ0FBQyxPQUFPLENBQUMsSUFBSSxDQUFDLEdBQUcsRUFBRTtZQUN2QyxPQUFPLENBQUMsR0FBRyxDQUFDLEtBQUssQ0FBQyxDQUFDLFNBQVMsRUFBRSxPQUFPLENBQUMsR0FBRyxFQUFFLElBQUksQ0FBQyxDQUFDLENBQUM7WUFDbEQsSUFBSTtnQkFDRixPQUFPLENBQUMsR0FBRyxDQUFDLEtBQUssQ0FDZixDQUFDLFNBQVMsRUFBRSxPQUFPLENBQUMsSUFBSSxFQUFFLHFDQUFxQyxDQUFDLEVBQ2hFLEdBQUcsRUFBRTtvQkFDSCxPQUFPLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxvQkFBb0IsRUFBRSxDQUFDO2dCQUM5QyxDQUFDLENBQ0YsQ0FBQzthQUNIO1lBQUMsT0FBTyxDQUFDLEVBQUU7Z0JBQ1YsT0FBTyxDQUFDLEtBQUssQ0FBQyxzQ0FBc0MsRUFBRSxDQUFDLENBQUMsQ0FBQzthQUMxRDtRQUNILENBQUMsQ0FBQyxDQUFDO0lBQ0wsQ0FBQztJQUVEOztPQUVHO0lBQ0ssS0FBSztRQUNYLE1BQU0sSUFBSSxHQUFHLFFBQVEsQ0FBQyxvQkFBb0IsQ0FBQyxNQUFNLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQztRQUN0RCxNQUFNLE1BQU0sR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLFFBQVEsQ0FBQyxDQUFDO1FBQ2hELE1BQU0sQ0FBQyxJQUFJLEdBQUcsaUJBQWlCLENBQUM7UUFDaEMsTUFBTSxDQUFDLEdBQUcsR0FBRyxHQUFHLElBQUksQ0FBQyxJQUFJLFdBQVcsSUFBSSxDQUFDLE9BQU8sbUNBQW1DLENBQUM7UUFDcEYsTUFBTSxDQUFDLE9BQU8sR0FBRyxPQUFPLENBQUM7UUFDekIsSUFBSSxDQUFDLFdBQVcsQ0FBQyxNQUFNLENBQUMsQ0FBQztRQUN6QixNQUFNLENBQUMsZ0JBQWdCLENBQUMsTUFBTSxFQUFFLEdBQUcsRUFBRTtZQUNuQyxJQUFJLENBQUMsT0FBTyxFQUFFLENBQUM7UUFDakIsQ0FBQyxDQUFDLENBQUM7UUFDSCxJQUFJLENBQUMsWUFBWSxHQUFHLElBQUksQ0FBQztJQUMzQixDQUFDO0lBRUQ7O09BRUc7SUFDSyxPQUFPO1FBQ2IsT0FBTyxDQUFDLEdBQUcsQ0FBQyxNQUFNLENBQUM7WUFDakIsT0FBTyxFQUFFO2dCQUNQLFVBQVUsRUFBRTtvQkFDVixDQUFDLEdBQUcsRUFBRSxHQUFHLENBQUM7b0JBQ1YsQ0FBQyxLQUFLLEVBQUUsS0FBSyxDQUFDO2lCQUNmO2dCQUNELFdBQVcsRUFBRTtvQkFDWCxDQUFDLElBQUksRUFBRSxJQUFJLENBQUM7b0JBQ1osQ0FBQyxLQUFLLEVBQUUsS0FBSyxDQUFDO2lCQUNmO2dCQUNELGNBQWMsRUFBRSxJQUFJO2dCQUNwQixtQkFBbUIsRUFBRSxJQUFJO2FBQzFCO1lBQ0QsaUVBQWlFO1lBQ2pFLGtFQUFrRTtZQUNsRSxZQUFZLEVBQUUsUUFBUTtZQUN0QixVQUFVLEVBQUU7Z0JBQ1YsVUFBVSxFQUFFLEVBQUUsU0FBUyxFQUFFLElBQUksRUFBRTthQUNoQztZQUNELFVBQVUsRUFBRTtnQkFDVixjQUFjLEVBQUUsRUFBRTtnQkFDbEIsU0FBUyxFQUFFLElBQUk7Z0JBQ2YsYUFBYSxFQUFFLElBQUk7Z0JBQ25CLE9BQU8sRUFBRSxVQUFVO2dCQUNuQixNQUFNLEVBQUUsRUFBRSxrQkFBa0IsRUFBRSxFQUFFLE1BQU0sRUFBRSxDQUFDLEVBQUUsRUFBRTtnQkFDN0MsVUFBVSxFQUFFLEVBQUUsU0FBUyxFQUFFLElBQUksRUFBRTthQUNoQztZQUNELGtCQUFrQixFQUFFLElBQUk7WUFDeEIsWUFBWSxFQUFFLE1BQU07U0FDckIsQ0FBQyxDQUFDO1FBQ0gsT0FBTyxDQUFDLEdBQUcsQ0FBQyxVQUFVLEVBQUUsQ0FBQztRQUN6QixJQUFJLENBQUMsWUFBWSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsQ0FBQyxDQUFDO0lBQ3BDLENBQUM7Q0FNRiIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9tYXRoamF4Mi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBtYXRoamF4MlxuICovXG5cbmltcG9ydCB7IElSZW5kZXJNaW1lIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZS1pbnRlcmZhY2VzJztcbmltcG9ydCB7IFByb21pc2VEZWxlZ2F0ZSB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcblxuLy8gU3R1YiBmb3Igd2luZG93IE1hdGhKYXguXG5kZWNsYXJlIGxldCBNYXRoSmF4OiBhbnk7XG5cbi8qKlxuICogVGhlIE1hdGhKYXggVHlwZXNldHRlci5cbiAqL1xuZXhwb3J0IGNsYXNzIE1hdGhKYXhUeXBlc2V0dGVyIGltcGxlbWVudHMgSVJlbmRlck1pbWUuSUxhdGV4VHlwZXNldHRlciB7XG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgTWF0aEpheCB0eXBlc2V0dGVyLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogTWF0aEpheFR5cGVzZXR0ZXIuSU9wdGlvbnMpIHtcbiAgICB0aGlzLl91cmwgPSBvcHRpb25zLnVybDtcbiAgICB0aGlzLl9jb25maWcgPSBvcHRpb25zLmNvbmZpZztcbiAgfVxuXG4gIC8qKlxuICAgKiBUeXBlc2V0IHRoZSBtYXRoIGluIGEgbm9kZS5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBNYXRoSmF4IHNjaGVkdWxlcyB0aGUgdHlwZXNldHRpbmcgYXN5bmNocm9ub3VzbHksXG4gICAqIGJ1dCB0aGVyZSBhcmUgbm90IGN1cnJlbnRseSBhbnkgY2FsbGJhY2tzIG9yIFByb21pc2VzXG4gICAqIGZpcmluZyB3aGVuIGl0IGlzIGRvbmUuXG4gICAqL1xuICB0eXBlc2V0KG5vZGU6IEhUTUxFbGVtZW50KTogdm9pZCB7XG4gICAgaWYgKCF0aGlzLl9pbml0aWFsaXplZCkge1xuICAgICAgdGhpcy5faW5pdCgpO1xuICAgIH1cbiAgICB2b2lkIHRoaXMuX2luaXRQcm9taXNlLnByb21pc2UudGhlbigoKSA9PiB7XG4gICAgICBNYXRoSmF4Lkh1Yi5RdWV1ZShbJ1R5cGVzZXQnLCBNYXRoSmF4Lkh1Yiwgbm9kZV0pO1xuICAgICAgdHJ5IHtcbiAgICAgICAgTWF0aEpheC5IdWIuUXVldWUoXG4gICAgICAgICAgWydSZXF1aXJlJywgTWF0aEpheC5BamF4LCAnW01hdGhKYXhdL2V4dGVuc2lvbnMvVGVYL0FNU21hdGguanMnXSxcbiAgICAgICAgICAoKSA9PiB7XG4gICAgICAgICAgICBNYXRoSmF4LklucHV0SmF4LlRlWC5yZXNldEVxdWF0aW9uTnVtYmVycygpO1xuICAgICAgICAgIH1cbiAgICAgICAgKTtcbiAgICAgIH0gY2F0Y2ggKGUpIHtcbiAgICAgICAgY29uc29sZS5lcnJvcignRXJyb3IgcXVldWVpbmcgcmVzZXRFcXVhdGlvbk51bWJlcnM6JywgZSk7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogSW5pdGlhbGl6ZSBNYXRoSmF4LlxuICAgKi9cbiAgcHJpdmF0ZSBfaW5pdCgpOiB2b2lkIHtcbiAgICBjb25zdCBoZWFkID0gZG9jdW1lbnQuZ2V0RWxlbWVudHNCeVRhZ05hbWUoJ2hlYWQnKVswXTtcbiAgICBjb25zdCBzY3JpcHQgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdzY3JpcHQnKTtcbiAgICBzY3JpcHQudHlwZSA9ICd0ZXh0L2phdmFzY3JpcHQnO1xuICAgIHNjcmlwdC5zcmMgPSBgJHt0aGlzLl91cmx9P2NvbmZpZz0ke3RoaXMuX2NvbmZpZ30mYW1wO2RlbGF5U3RhcnR1cFVudGlsPWNvbmZpZ3VyZWRgO1xuICAgIHNjcmlwdC5jaGFyc2V0ID0gJ3V0Zi04JztcbiAgICBoZWFkLmFwcGVuZENoaWxkKHNjcmlwdCk7XG4gICAgc2NyaXB0LmFkZEV2ZW50TGlzdGVuZXIoJ2xvYWQnLCAoKSA9PiB7XG4gICAgICB0aGlzLl9vbkxvYWQoKTtcbiAgICB9KTtcbiAgICB0aGlzLl9pbml0aWFsaXplZCA9IHRydWU7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIE1hdGhKYXggbG9hZGluZy5cbiAgICovXG4gIHByaXZhdGUgX29uTG9hZCgpOiB2b2lkIHtcbiAgICBNYXRoSmF4Lkh1Yi5Db25maWcoe1xuICAgICAgdGV4MmpheDoge1xuICAgICAgICBpbmxpbmVNYXRoOiBbXG4gICAgICAgICAgWyckJywgJyQnXSxcbiAgICAgICAgICBbJ1xcXFwoJywgJ1xcXFwpJ11cbiAgICAgICAgXSxcbiAgICAgICAgZGlzcGxheU1hdGg6IFtcbiAgICAgICAgICBbJyQkJywgJyQkJ10sXG4gICAgICAgICAgWydcXFxcWycsICdcXFxcXSddXG4gICAgICAgIF0sXG4gICAgICAgIHByb2Nlc3NFc2NhcGVzOiB0cnVlLFxuICAgICAgICBwcm9jZXNzRW52aXJvbm1lbnRzOiB0cnVlXG4gICAgICB9LFxuICAgICAgLy8gQ2VudGVyIGp1c3RpZnkgZXF1YXRpb25zIGluIGNvZGUgYW5kIG1hcmtkb3duIGNlbGxzLiBFbHNld2hlcmVcbiAgICAgIC8vIHdlIHVzZSBDU1MgdG8gbGVmdCBqdXN0aWZ5IHNpbmdsZSBsaW5lIGVxdWF0aW9ucyBpbiBjb2RlIGNlbGxzLlxuICAgICAgZGlzcGxheUFsaWduOiAnY2VudGVyJyxcbiAgICAgIENvbW1vbkhUTUw6IHtcbiAgICAgICAgbGluZWJyZWFrczogeyBhdXRvbWF0aWM6IHRydWUgfVxuICAgICAgfSxcbiAgICAgICdIVE1MLUNTUyc6IHtcbiAgICAgICAgYXZhaWxhYmxlRm9udHM6IFtdLFxuICAgICAgICBpbWFnZUZvbnQ6IG51bGwsXG4gICAgICAgIHByZWZlcnJlZEZvbnQ6IG51bGwsXG4gICAgICAgIHdlYkZvbnQ6ICdTVElYLVdlYicsXG4gICAgICAgIHN0eWxlczogeyAnLk1hdGhKYXhfRGlzcGxheSc6IHsgbWFyZ2luOiAwIH0gfSxcbiAgICAgICAgbGluZWJyZWFrczogeyBhdXRvbWF0aWM6IHRydWUgfVxuICAgICAgfSxcbiAgICAgIHNraXBTdGFydHVwVHlwZXNldDogdHJ1ZSxcbiAgICAgIG1lc3NhZ2VTdHlsZTogJ25vbmUnXG4gICAgfSk7XG4gICAgTWF0aEpheC5IdWIuQ29uZmlndXJlZCgpO1xuICAgIHRoaXMuX2luaXRQcm9taXNlLnJlc29sdmUodm9pZCAwKTtcbiAgfVxuXG4gIHByaXZhdGUgX2luaXRQcm9taXNlID0gbmV3IFByb21pc2VEZWxlZ2F0ZTx2b2lkPigpO1xuICBwcml2YXRlIF9pbml0aWFsaXplZCA9IGZhbHNlO1xuICBwcml2YXRlIF91cmw6IHN0cmluZztcbiAgcHJpdmF0ZSBfY29uZmlnOiBzdHJpbmc7XG59XG5cbi8qKlxuICogTmFtZXNwYWNlIGZvciBNYXRoSmF4VHlwZXNldHRlci5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBNYXRoSmF4VHlwZXNldHRlciB7XG4gIC8qKlxuICAgKiBNYXRoSmF4VHlwZXNldHRlciBjb25zdHJ1Y3RvciBvcHRpb25zLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHVybCB0byBsb2FkIE1hdGhKYXggZnJvbS5cbiAgICAgKi9cbiAgICB1cmw6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIEEgY29uZmlndXJhdGlvbiBzdHJpbmcgdG8gY29tcG9zZSBpbnRvIHRoZSBNYXRoSmF4IFVSTC5cbiAgICAgKi9cbiAgICBjb25maWc6IHN0cmluZztcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9