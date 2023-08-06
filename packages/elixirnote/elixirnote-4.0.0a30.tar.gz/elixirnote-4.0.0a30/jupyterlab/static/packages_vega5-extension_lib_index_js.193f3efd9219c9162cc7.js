"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_vega5-extension_lib_index_js"],{

/***/ "../../packages/vega5-extension/lib/index.js":
/*!***************************************************!*\
  !*** ../../packages/vega5-extension/lib/index.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RenderedVega": () => (/* binding */ RenderedVega),
/* harmony export */   "VEGALITE3_MIME_TYPE": () => (/* binding */ VEGALITE3_MIME_TYPE),
/* harmony export */   "VEGALITE4_MIME_TYPE": () => (/* binding */ VEGALITE4_MIME_TYPE),
/* harmony export */   "VEGA_MIME_TYPE": () => (/* binding */ VEGA_MIME_TYPE),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "rendererFactory": () => (/* binding */ rendererFactory)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module vega5-extension
 */

/**
 * The CSS class to add to the Vega and Vega-Lite widget.
 */
const VEGA_COMMON_CLASS = 'jp-RenderedVegaCommon5';
/**
 * The CSS class to add to the Vega.
 */
const VEGA_CLASS = 'jp-RenderedVega5';
/**
 * The CSS class to add to the Vega-Lite.
 */
const VEGALITE_CLASS = 'jp-RenderedVegaLite';
/**
 * The MIME type for Vega.
 *
 * #### Notes
 * The version of this follows the major version of Vega.
 */
const VEGA_MIME_TYPE = 'application/vnd.vega.v5+json';
/**
 * The MIME type for Vega-Lite.
 *
 * #### Notes
 * The version of this follows the major version of Vega-Lite.
 */
const VEGALITE3_MIME_TYPE = 'application/vnd.vegalite.v3+json';
/**
 * The MIME type for Vega-Lite.
 *
 * #### Notes
 * The version of this follows the major version of Vega-Lite.
 */
const VEGALITE4_MIME_TYPE = 'application/vnd.vegalite.v4+json';
/**
 * A widget for rendering Vega or Vega-Lite data, for usage with rendermime.
 */
class RenderedVega extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget {
    /**
     * Create a new widget for rendering Vega/Vega-Lite.
     */
    constructor(options) {
        super();
        this._mimeType = options.mimeType;
        this._resolver = options.resolver;
        this.addClass(VEGA_COMMON_CLASS);
        this.addClass(this._mimeType === VEGA_MIME_TYPE ? VEGA_CLASS : VEGALITE_CLASS);
    }
    /**
     * Render Vega/Vega-Lite into this widget's node.
     */
    async renderModel(model) {
        const spec = model.data[this._mimeType];
        if (spec === undefined) {
            return;
        }
        const metadata = model.metadata[this._mimeType];
        const embedOptions = metadata && metadata.embed_options ? metadata.embed_options : {};
        // If the JupyterLab theme is dark, render this using a dark Vega theme.
        let bodyThemeDark = document.body.dataset.jpThemeLight === 'false';
        if (bodyThemeDark) {
            embedOptions.theme = 'dark';
        }
        const mode = this._mimeType === VEGA_MIME_TYPE ? 'vega' : 'vega-lite';
        const vega = Private.vega != null ? Private.vega : await Private.ensureVega();
        const el = document.createElement('div');
        // clear the output before attaching a chart
        this.node.textContent = '';
        this.node.appendChild(el);
        if (this._result) {
            this._result.finalize();
        }
        const loader = vega.vega.loader({
            http: { credentials: 'same-origin' }
        });
        const sanitize = async (uri, options) => {
            // Use the resolver for any URIs it wants to handle
            const resolver = this._resolver;
            if ((resolver === null || resolver === void 0 ? void 0 : resolver.isLocal) && resolver.isLocal(uri)) {
                const absPath = await resolver.resolveUrl(uri);
                uri = await resolver.getDownloadUrl(absPath);
            }
            return loader.sanitize(uri, options);
        };
        this._result = await vega.default(el, spec, Object.assign(Object.assign({ actions: true, defaultStyle: true }, embedOptions), { mode, loader: Object.assign(Object.assign({}, loader), { sanitize }) }));
        if (model.data['image/png']) {
            return;
        }
        // Add png representation of vega chart to output
        const imageURL = await this._result.view.toImageURL('png');
        model.setData({
            data: Object.assign(Object.assign({}, model.data), { 'image/png': imageURL.split(',')[1] })
        });
    }
    dispose() {
        if (this._result) {
            this._result.finalize();
        }
        super.dispose();
    }
}
/**
 * A mime renderer factory for vega data.
 */
const rendererFactory = {
    safe: true,
    mimeTypes: [VEGA_MIME_TYPE, VEGALITE3_MIME_TYPE, VEGALITE4_MIME_TYPE],
    createRenderer: options => new RenderedVega(options)
};
const extension = {
    id: '@jupyterlab/vega5-extension:factory',
    rendererFactory,
    rank: 57,
    dataType: 'json',
    documentWidgetFactoryOptions: [
        {
            name: 'Vega5',
            primaryFileType: 'vega5',
            fileTypes: ['vega5', 'json'],
            defaultFor: ['vega5']
        },
        {
            name: 'Vega-Lite4',
            primaryFileType: 'vega-lite4',
            fileTypes: ['vega-lite3', 'vega-lite4', 'json'],
            defaultFor: ['vega-lite3', 'vega-lite4']
        }
    ],
    fileTypes: [
        {
            mimeTypes: [VEGA_MIME_TYPE],
            name: 'vega5',
            extensions: ['.vg', '.vg.json', '.vega'],
            icon: 'ui-components:vega'
        },
        {
            mimeTypes: [VEGALITE4_MIME_TYPE],
            name: 'vega-lite4',
            extensions: ['.vl', '.vl.json', '.vegalite'],
            icon: 'ui-components:vega'
        },
        {
            mimeTypes: [VEGALITE3_MIME_TYPE],
            name: 'vega-lite3',
            extensions: [],
            icon: 'ui-components:vega'
        }
    ]
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);
/**
 * A namespace for private module data.
 */
var Private;
(function (Private) {
    /**
     * Lazy-load and cache the vega-embed library
     */
    function ensureVega() {
        if (Private.vegaReady) {
            return Private.vegaReady;
        }
        Private.vegaReady = __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_vega-embed_vega-embed").then(__webpack_require__.t.bind(__webpack_require__, /*! vega-embed */ "webpack/sharing/consume/default/vega-embed/vega-embed", 23));
        return Private.vegaReady;
    }
    Private.ensureVega = ensureVega;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdmVnYTUtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy4xOTNmM2VmZDkyMTljOTE2MmNjNy5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUlzQztBQUd6Qzs7R0FFRztBQUNILE1BQU0saUJBQWlCLEdBQUcsd0JBQXdCLENBQUM7QUFFbkQ7O0dBRUc7QUFDSCxNQUFNLFVBQVUsR0FBRyxrQkFBa0IsQ0FBQztBQUV0Qzs7R0FFRztBQUNILE1BQU0sY0FBYyxHQUFHLHFCQUFxQixDQUFDO0FBRTdDOzs7OztHQUtHO0FBQ0ksTUFBTSxjQUFjLEdBQUcsOEJBQThCLENBQUM7QUFFN0Q7Ozs7O0dBS0c7QUFDSSxNQUFNLG1CQUFtQixHQUFHLGtDQUFrQyxDQUFDO0FBRXRFOzs7OztHQUtHO0FBQ0ksTUFBTSxtQkFBbUIsR0FBRyxrQ0FBa0MsQ0FBQztBQUV0RTs7R0FFRztBQUNJLE1BQU0sWUFBYSxTQUFRLG1EQUFNO0lBR3RDOztPQUVHO0lBQ0gsWUFBWSxPQUFxQztRQUMvQyxLQUFLLEVBQUUsQ0FBQztRQUNSLElBQUksQ0FBQyxTQUFTLEdBQUcsT0FBTyxDQUFDLFFBQVEsQ0FBQztRQUNsQyxJQUFJLENBQUMsU0FBUyxHQUFHLE9BQU8sQ0FBQyxRQUFRLENBQUM7UUFDbEMsSUFBSSxDQUFDLFFBQVEsQ0FBQyxpQkFBaUIsQ0FBQyxDQUFDO1FBQ2pDLElBQUksQ0FBQyxRQUFRLENBQ1gsSUFBSSxDQUFDLFNBQVMsS0FBSyxjQUFjLENBQUMsQ0FBQyxDQUFDLFVBQVUsQ0FBQyxDQUFDLENBQUMsY0FBYyxDQUNoRSxDQUFDO0lBQ0osQ0FBQztJQUVEOztPQUVHO0lBQ0gsS0FBSyxDQUFDLFdBQVcsQ0FBQyxLQUE2QjtRQUM3QyxNQUFNLElBQUksR0FBRyxLQUFLLENBQUMsSUFBSSxDQUFDLElBQUksQ0FBQyxTQUFTLENBQTJCLENBQUM7UUFDbEUsSUFBSSxJQUFJLEtBQUssU0FBUyxFQUFF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QUUsV0FBVyxDQUFDO1lBQzVDLElBQUksRUFBRSxvQkFBb0I7U0FDM0I7UUFDRDtZQUNFLFNBQVMsRUFBRSxDQUFDLG1CQUFtQixDQUFDO1lBQ2hDLElBQUksRUFBRSxZQUFZO1lBQ2xCLFVBQVUsRUFBRSxFQUFFO1lBQ2QsSUFBSSxFQUFFLG9CQUFvQjtTQUMzQjtLQUNGO0NBQ0YsQ0FBQztBQUVGLGlFQUFlLFNBQVMsRUFBQztBQUV6Qjs7R0FFRztBQUNILElBQVUsT0FBTyxDQXVCaEI7QUF2QkQsV0FBVSxPQUFPO0lBV2Y7O09BRUc7SUFDSCxTQUFnQixVQUFVO1FBQ3hCLElBQUksaUJBQVMsRUFBRTtZQUNiLE9BQU8saUJBQVMsQ0FBQztTQUNsQjtRQUVELGlCQUFTLEdBQUcsbU9BQW9CLENBQUM7UUFFakMsT0FBTyxpQkFBUyxDQUFDO0lBQ25CLENBQUM7SUFSZSxrQkFBVSxhQVF6QjtBQUNILENBQUMsRUF2QlMsT0FBTyxLQUFQLE9BQU8sUUF1QmhCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3ZlZ2E1LWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB2ZWdhNS1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQgeyBJUmVuZGVyTWltZSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUtaW50ZXJmYWNlcyc7XG5pbXBvcnQgeyBKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCAqIGFzIFZlZ2FNb2R1bGVUeXBlIGZyb20gJ3ZlZ2EtZW1iZWQnO1xuXG4vKipcbiAqIFRoZSBDU1MgY2xhc3MgdG8gYWRkIHRvIHRoZSBWZWdhIGFuZCBWZWdhLUxpdGUgd2lkZ2V0LlxuICovXG5jb25zdCBWRUdBX0NPTU1PTl9DTEFTUyA9ICdqcC1SZW5kZXJlZFZlZ2FDb21tb241JztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIHRvIGFkZCB0byB0aGUgVmVnYS5cbiAqL1xuY29uc3QgVkVHQV9DTEFTUyA9ICdqcC1SZW5kZXJlZFZlZ2E1JztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIHRvIGFkZCB0byB0aGUgVmVnYS1MaXRlLlxuICovXG5jb25zdCBWRUdBTElURV9DTEFTUyA9ICdqcC1SZW5kZXJlZFZlZ2FMaXRlJztcblxuLyoqXG4gKiBUaGUgTUlNRSB0eXBlIGZvciBWZWdhLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoZSB2ZXJzaW9uIG9mIHRoaXMgZm9sbG93cyB0aGUgbWFqb3IgdmVyc2lvbiBvZiBWZWdhLlxuICovXG5leHBvcnQgY29uc3QgVkVHQV9NSU1FX1RZUEUgPSAnYXBwbGljYXRpb24vdm5kLnZlZ2EudjUranNvbic7XG5cbi8qKlxuICogVGhlIE1JTUUgdHlwZSBmb3IgVmVnYS1MaXRlLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoZSB2ZXJzaW9uIG9mIHRoaXMgZm9sbG93cyB0aGUgbWFqb3IgdmVyc2lvbiBvZiBWZWdhLUxpdGUuXG4gKi9cbmV4cG9ydCBjb25zdCBWRUdBTElURTNfTUlNRV9UWVBFID0gJ2FwcGxpY2F0aW9uL3ZuZC52ZWdhbGl0ZS52Mytqc29uJztcblxuLyoqXG4gKiBUaGUgTUlNRSB0eXBlIGZvciBWZWdhLUxpdGUuXG4gKlxuICogIyMjIyBOb3Rlc1xuICogVGhlIHZlcnNpb24gb2YgdGhpcyBmb2xsb3dzIHRoZSBtYWpvciB2ZXJzaW9uIG9mIFZlZ2EtTGl0ZS5cbiAqL1xuZXhwb3J0IGNvbnN0IFZFR0FMSVRFNF9NSU1FX1RZUEUgPSAnYXBwbGljYXRpb24vdm5kLnZlZ2FsaXRlLnY0K2pzb24nO1xuXG4vKipcbiAqIEEgd2lkZ2V0IGZvciByZW5kZXJpbmcgVmVnYSBvciBWZWdhLUxpdGUgZGF0YSwgZm9yIHVzYWdlIHdpdGggcmVuZGVybWltZS5cbiAqL1xuZXhwb3J0IGNsYXNzIFJlbmRlcmVkVmVnYSBleHRlbmRzIFdpZGdldCBpbXBsZW1lbnRzIElSZW5kZXJNaW1lLklSZW5kZXJlciB7XG4gIHByaXZhdGUgX3Jlc3VsdDogVmVnYU1vZHVsZVR5cGUuUmVzdWx0O1xuXG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgd2lkZ2V0IGZvciByZW5kZXJpbmcgVmVnYS9WZWdhLUxpdGUuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBJUmVuZGVyTWltZS5JUmVuZGVyZXJPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl9taW1lVHlwZSA9IG9wdGlvbnMubWltZVR5cGU7XG4gICAgdGhpcy5fcmVzb2x2ZXIgPSBvcHRpb25zLnJlc29sdmVyO1xuICAgIHRoaXMuYWRkQ2xhc3MoVkVHQV9DT01NT05fQ0xBU1MpO1xuICAgIHRoaXMuYWRkQ2xhc3MoXG4gICAgICB0aGlzLl9taW1lVHlwZSA9PT0gVkVHQV9NSU1FX1RZUEUgPyBWRUdBX0NMQVNTIDogVkVHQUxJVEVfQ0xBU1NcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbmRlciBWZWdhL1ZlZ2EtTGl0ZSBpbnRvIHRoaXMgd2lkZ2V0J3Mgbm9kZS5cbiAgICovXG4gIGFzeW5jIHJlbmRlck1vZGVsKG1vZGVsOiBJUmVuZGVyTWltZS5JTWltZU1vZGVsKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3Qgc3BlYyA9IG1vZGVsLmRhdGFbdGhpcy5fbWltZVR5cGVdIGFzIEpTT05PYmplY3QgfCB1bmRlZmluZWQ7XG4gICAgaWYgKHNwZWMgPT09IHVuZGVmaW5lZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBjb25zdCBtZXRhZGF0YSA9IG1vZGVsLm1ldGFkYXRhW3RoaXMuX21pbWVUeXBlXSBhc1xuICAgICAgfCB7XG4gICAgICAgICAgZW1iZWRfb3B0aW9ucz86IFZlZ2FNb2R1bGVUeXBlLkVtYmVkT3B0aW9ucztcbiAgICAgICAgfVxuICAgICAgfCB1bmRlZmluZWQ7XG4gICAgY29uc3QgZW1iZWRPcHRpb25zID1cbiAgICAgIG1ldGFkYXRhICYmIG1ldGFkYXRhLmVtYmVkX29wdGlvbnMgPyBtZXRhZGF0YS5lbWJlZF9vcHRpb25zIDoge307XG5cbiAgICAvLyBJZiB0aGUgSnVweXRlckxhYiB0aGVtZSBpcyBkYXJrLCByZW5kZXIgdGhpcyB1c2luZyBhIGRhcmsgVmVnYSB0aGVtZS5cbiAgICBsZXQgYm9keVRoZW1lRGFyayA9IGRvY3VtZW50LmJvZHkuZGF0YXNldC5qcFRoZW1lTGlnaHQgPT09ICdmYWxzZSc7XG4gICAgaWYgKGJvZHlUaGVtZURhcmspIHtcbiAgICAgIGVtYmVkT3B0aW9ucy50aGVtZSA9ICdkYXJrJztcbiAgICB9XG5cbiAgICBjb25zdCBtb2RlOiBWZWdhTW9kdWxlVHlwZS5Nb2RlID1cbiAgICAgIHRoaXMuX21pbWVUeXBlID09PSBWRUdBX01JTUVfVFlQRSA/ICd2ZWdhJyA6ICd2ZWdhLWxpdGUnO1xuXG4gICAgY29uc3QgdmVnYSA9XG4gICAgICBQcml2YXRlLnZlZ2EgIT0gbnVsbCA/IFByaXZhdGUudmVnYSA6IGF3YWl0IFByaXZhdGUuZW5zdXJlVmVnYSgpO1xuXG4gICAgY29uc3QgZWwgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcblxuICAgIC8vIGNsZWFyIHRoZSBvdXRwdXQgYmVmb3JlIGF0dGFjaGluZyBhIGNoYXJ0XG4gICAgdGhpcy5ub2RlLnRleHRDb250ZW50ID0gJyc7XG4gICAgdGhpcy5ub2RlLmFwcGVuZENoaWxkKGVsKTtcblxuICAgIGlmICh0aGlzLl9yZXN1bHQpIHtcbiAgICAgIHRoaXMuX3Jlc3VsdC5maW5hbGl6ZSgpO1xuICAgIH1cblxuICAgIGNvbnN0IGxvYWRlciA9IHZlZ2EudmVnYS5sb2FkZXIoe1xuICAgICAgaHR0cDogeyBjcmVkZW50aWFsczogJ3NhbWUtb3JpZ2luJyB9XG4gICAgfSk7XG4gICAgY29uc3Qgc2FuaXRpemUgPSBhc3luYyAodXJpOiBzdHJpbmcsIG9wdGlvbnM6IGFueSkgPT4ge1xuICAgICAgLy8gVXNlIHRoZSByZXNvbHZlciBmb3IgYW55IFVSSXMgaXQgd2FudHMgdG8gaGFuZGxlXG4gICAgICBjb25zdCByZXNvbHZlciA9IHRoaXMuX3Jlc29sdmVyO1xuICAgICAgaWYgKHJlc29sdmVyPy5pc0xvY2FsICYmIHJlc29sdmVyLmlzTG9jYWwodXJpKSkge1xuICAgICAgICBjb25zdCBhYnNQYXRoID0gYXdhaXQgcmVzb2x2ZXIucmVzb2x2ZVVybCh1cmkpO1xuICAgICAgICB1cmkgPSBhd2FpdCByZXNvbHZlci5nZXREb3dubG9hZFVybChhYnNQYXRoKTtcbiAgICAgIH1cbiAgICAgIHJldHVybiBsb2FkZXIuc2FuaXRpemUodXJpLCBvcHRpb25zKTtcbiAgICB9O1xuXG4gICAgdGhpcy5fcmVzdWx0ID0gYXdhaXQgdmVnYS5kZWZhdWx0KGVsLCBzcGVjLCB7XG4gICAgICBhY3Rpb25zOiB0cnVlLFxuICAgICAgZGVmYXVsdFN0eWxlOiB0cnVlLFxuICAgICAgLi4uZW1iZWRPcHRpb25zLFxuICAgICAgbW9kZSxcbiAgICAgIGxvYWRlcjogeyAuLi5sb2FkZXIsIHNhbml0aXplIH1cbiAgICB9KTtcblxuICAgIGlmIChtb2RlbC5kYXRhWydpbWFnZS9wbmcnXSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIC8vIEFkZCBwbmcgcmVwcmVzZW50YXRpb24gb2YgdmVnYSBjaGFydCB0byBvdXRwdXRcbiAgICBjb25zdCBpbWFnZVVSTCA9IGF3YWl0IHRoaXMuX3Jlc3VsdC52aWV3LnRvSW1hZ2VVUkwoJ3BuZycpO1xuICAgIG1vZGVsLnNldERhdGEoe1xuICAgICAgZGF0YTogeyAuLi5tb2RlbC5kYXRhLCAnaW1hZ2UvcG5nJzogaW1hZ2VVUkwuc3BsaXQoJywnKVsxXSB9XG4gICAgfSk7XG4gIH1cblxuICBkaXNwb3NlKCk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9yZXN1bHQpIHtcbiAgICAgIHRoaXMuX3Jlc3VsdC5maW5hbGl6ZSgpO1xuICAgIH1cbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICBwcml2YXRlIF9taW1lVHlwZTogc3RyaW5nO1xuICBwcml2YXRlIF9yZXNvbHZlcjogSVJlbmRlck1pbWUuSVJlc29sdmVyIHwgbnVsbDtcbn1cblxuLyoqXG4gKiBBIG1pbWUgcmVuZGVyZXIgZmFjdG9yeSBmb3IgdmVnYSBkYXRhLlxuICovXG5leHBvcnQgY29uc3QgcmVuZGVyZXJGYWN0b3J5OiBJUmVuZGVyTWltZS5JUmVuZGVyZXJGYWN0b3J5ID0ge1xuICBzYWZlOiB0cnVlLFxuICBtaW1lVHlwZXM6IFtWRUdBX01JTUVfVFlQRSwgVkVHQUxJVEUzX01JTUVfVFlQRSwgVkVHQUxJVEU0X01JTUVfVFlQRV0sXG4gIGNyZWF0ZVJlbmRlcmVyOiBvcHRpb25zID0+IG5ldyBSZW5kZXJlZFZlZ2Eob3B0aW9ucylcbn07XG5cbmNvbnN0IGV4dGVuc2lvbjogSVJlbmRlck1pbWUuSUV4dGVuc2lvbiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi92ZWdhNS1leHRlbnNpb246ZmFjdG9yeScsXG4gIHJlbmRlcmVyRmFjdG9yeSxcbiAgcmFuazogNTcsXG4gIGRhdGFUeXBlOiAnanNvbicsXG4gIGRvY3VtZW50V2lkZ2V0RmFjdG9yeU9wdGlvbnM6IFtcbiAgICB7XG4gICAgICBuYW1lOiAnVmVnYTUnLFxuICAgICAgcHJpbWFyeUZpbGVUeXBlOiAndmVnYTUnLFxuICAgICAgZmlsZVR5cGVzOiBbJ3ZlZ2E1JywgJ2pzb24nXSxcbiAgICAgIGRlZmF1bHRGb3I6IFsndmVnYTUnXVxuICAgIH0sXG4gICAge1xuICAgICAgbmFtZTogJ1ZlZ2EtTGl0ZTQnLFxuICAgICAgcHJpbWFyeUZpbGVUeXBlOiAndmVnYS1saXRlNCcsXG4gICAgICBmaWxlVHlwZXM6IFsndmVnYS1saXRlMycsICd2ZWdhLWxpdGU0JywgJ2pzb24nXSxcbiAgICAgIGRlZmF1bHRGb3I6IFsndmVnYS1saXRlMycsICd2ZWdhLWxpdGU0J11cbiAgICB9XG4gIF0sXG4gIGZpbGVUeXBlczogW1xuICAgIHtcbiAgICAgIG1pbWVUeXBlczogW1ZFR0FfTUlNRV9UWVBFXSxcbiAgICAgIG5hbWU6ICd2ZWdhNScsXG4gICAgICBleHRlbnNpb25zOiBbJy52ZycsICcudmcuanNvbicsICcudmVnYSddLFxuICAgICAgaWNvbjogJ3VpLWNvbXBvbmVudHM6dmVnYSdcbiAgICB9LFxuICAgIHtcbiAgICAgIG1pbWVUeXBlczogW1ZFR0FMSVRFNF9NSU1FX1RZUEVdLFxuICAgICAgbmFtZTogJ3ZlZ2EtbGl0ZTQnLFxuICAgICAgZXh0ZW5zaW9uczogWycudmwnLCAnLnZsLmpzb24nLCAnLnZlZ2FsaXRlJ10sXG4gICAgICBpY29uOiAndWktY29tcG9uZW50czp2ZWdhJ1xuICAgIH0sXG4gICAge1xuICAgICAgbWltZVR5cGVzOiBbVkVHQUxJVEUzX01JTUVfVFlQRV0sXG4gICAgICBuYW1lOiAndmVnYS1saXRlMycsXG4gICAgICBleHRlbnNpb25zOiBbXSxcbiAgICAgIGljb246ICd1aS1jb21wb25lbnRzOnZlZ2EnXG4gICAgfVxuICBdXG59O1xuXG5leHBvcnQgZGVmYXVsdCBleHRlbnNpb247XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgbW9kdWxlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIEEgY2FjaGVkIHJlZmVyZW5jZSB0byB0aGUgdmVnYSBsaWJyYXJ5LlxuICAgKi9cbiAgZXhwb3J0IGxldCB2ZWdhOiB0eXBlb2YgVmVnYU1vZHVsZVR5cGU7XG5cbiAgLyoqXG4gICAqIEEgUHJvbWlzZSBmb3IgdGhlIGluaXRpYWwgbG9hZCBvZiB2ZWdhLlxuICAgKi9cbiAgZXhwb3J0IGxldCB2ZWdhUmVhZHk6IFByb21pc2U8dHlwZW9mIFZlZ2FNb2R1bGVUeXBlPjtcblxuICAvKipcbiAgICogTGF6eS1sb2FkIGFuZCBjYWNoZSB0aGUgdmVnYS1lbWJlZCBsaWJyYXJ5XG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gZW5zdXJlVmVnYSgpOiBQcm9taXNlPHR5cGVvZiBWZWdhTW9kdWxlVHlwZT4ge1xuICAgIGlmICh2ZWdhUmVhZHkpIHtcbiAgICAgIHJldHVybiB2ZWdhUmVhZHk7XG4gICAgfVxuXG4gICAgdmVnYVJlYWR5ID0gaW1wb3J0KCd2ZWdhLWVtYmVkJyk7XG5cbiAgICByZXR1cm4gdmVnYVJlYWR5O1xuICB9XG59XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=