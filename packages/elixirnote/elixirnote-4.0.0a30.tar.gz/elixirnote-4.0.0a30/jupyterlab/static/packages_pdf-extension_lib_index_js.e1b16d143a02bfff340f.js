"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_pdf-extension_lib_index_js"],{

/***/ "../../packages/pdf-extension/lib/index.js":
/*!*************************************************!*\
  !*** ../../packages/pdf-extension/lib/index.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RenderedPDF": () => (/* binding */ RenderedPDF),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__),
/* harmony export */   "rendererFactory": () => (/* binding */ rendererFactory)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module pdf-extension
 */



/**
 * The MIME type for PDF.
 */
const MIME_TYPE = 'application/pdf';
/**
 * A class for rendering a PDF document.
 */
class RenderedPDF extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Widget {
    constructor() {
        super();
        this._base64 = '';
        this._disposable = null;
        this._ready = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.PromiseDelegate();
        this.addClass('jp-PDFContainer');
        // We put the object in an iframe, which seems to have a better chance
        // of retaining its scroll position upon tab focusing, moving around etc.
        const iframe = document.createElement('iframe');
        this.node.appendChild(iframe);
        // The iframe content window is not available until the onload event.
        iframe.onload = () => {
            const body = iframe.contentWindow.document.createElement('body');
            body.style.margin = '0px';
            iframe.contentWindow.document.body = body;
            this._object = iframe.contentWindow.document.createElement('object');
            // work around for https://discussions.apple.com/thread/252247740
            // Detect if running on Desktop Safari
            if (!window.safari) {
                this._object.type = MIME_TYPE;
            }
            this._object.width = '100%';
            this._object.height = '100%';
            body.appendChild(this._object);
            this._ready.resolve(void 0);
        };
    }
    /**
     * Render PDF into this widget's node.
     */
    async renderModel(model) {
        await this._ready.promise;
        const data = model.data[MIME_TYPE];
        if (!data ||
            (data.length === this._base64.length && data === this._base64)) {
            // If there is no data, or if the string has not changed, we do not
            // need to re-parse the data and rerender. We do, however, check
            // for a fragment if the user wants to scroll the output.
            if (model.metadata.fragment && this._object.data) {
                const url = this._object.data;
                this._object.data = `${url.split('#')[0]}${model.metadata.fragment}`;
            }
            // For some opaque reason, Firefox seems to loose its scroll position
            // upon unhiding a PDF. But triggering a refresh of the URL makes it
            // find it again. No idea what the reason for this is.
            if (Private.IS_FIREFOX) {
                this._object.data = this._object.data; // eslint-disable-line
            }
            return Promise.resolve(void 0);
        }
        this._base64 = data;
        const blob = Private.b64toBlob(data, MIME_TYPE);
        // Release reference to any previous object url.
        if (this._disposable) {
            this._disposable.dispose();
        }
        let objectUrl = URL.createObjectURL(blob);
        if (model.metadata.fragment) {
            objectUrl += model.metadata.fragment;
        }
        this._object.data = objectUrl;
        // Set the disposable release the object URL.
        this._disposable = new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            try {
                URL.revokeObjectURL(objectUrl);
            }
            catch (error) {
                /* no-op */
            }
        });
        return;
    }
    /**
     * Handle a `before-hide` message.
     */
    onBeforeHide() {
        // Dispose of any URL fragment before hiding the widget
        // so that it is not remembered upon show. Only Firefox
        // seems to have a problem with this.
        if (Private.IS_FIREFOX) {
            this._object.data = this._object.data.split('#')[0];
        }
    }
    /**
     * Dispose of the resources held by the pdf widget.
     */
    dispose() {
        if (this._disposable) {
            this._disposable.dispose();
        }
        super.dispose();
    }
}
/**
 * A mime renderer factory for PDF data.
 */
const rendererFactory = {
    safe: false,
    mimeTypes: [MIME_TYPE],
    defaultRank: 100,
    createRenderer: options => new RenderedPDF()
};
const extensions = [
    {
        id: '@jupyterlab/pdf-extension:factory',
        rendererFactory,
        dataType: 'string',
        documentWidgetFactoryOptions: {
            name: 'PDF',
            // TODO: translate label
            modelName: 'base64',
            primaryFileType: 'PDF',
            fileTypes: ['PDF'],
            defaultFor: ['PDF']
        }
    }
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extensions);
/**
 * A namespace for PDF widget private data.
 */
var Private;
(function (Private) {
    /**
     * A flag for determining whether the user is using Firefox.
     * There are some different PDF viewer behaviors on Firefox,
     * and we try to address them with this. User agent string parsing
     * is *not* reliable, so this should be considered a best-effort test.
     */
    Private.IS_FIREFOX = /Firefox/.test(navigator.userAgent);
    /**
     * Convert a base64 encoded string to a Blob object.
     * Modified from a snippet found here:
     * https://stackoverflow.com/questions/16245767/creating-a-blob-from-a-base64-string-in-javascript
     *
     * @param b64Data - The base64 encoded data.
     *
     * @param contentType - The mime type of the data.
     *
     * @param sliceSize - The size to chunk the data into for processing.
     *
     * @returns a Blob for the data.
     */
    function b64toBlob(b64Data, contentType = '', sliceSize = 512) {
        const byteCharacters = atob(b64Data);
        const byteArrays = [];
        for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {
            const slice = byteCharacters.slice(offset, offset + sliceSize);
            const byteNumbers = new Array(slice.length);
            for (let i = 0; i < slice.length; i++) {
                byteNumbers[i] = slice.charCodeAt(i);
            }
            const byteArray = new Uint8Array(byteNumbers);
            byteArrays.push(byteArray);
        }
        return new Blob(byteArrays, { type: contentType });
    }
    Private.b64toBlob = b64toBlob;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfcGRmLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuZTFiMTZkMTQzYTAyYmZmZjM0MGYuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFHaUQ7QUFDSTtBQUNmO0FBRXpDOztHQUVHO0FBQ0gsTUFBTSxTQUFTLEdBQUcsaUJBQWlCLENBQUM7QUFFcEM7O0dBRUc7QUFDSSxNQUFNLFdBQVksU0FBUSxtREFBTTtJQUNyQztRQUNFLEtBQUssRUFBRSxDQUFDO1FBK0ZGLFlBQU8sR0FBRyxFQUFFLENBQUM7UUFDYixnQkFBVyxHQUE4QixJQUFJLENBQUM7UUFFOUMsV0FBTSxHQUFHLElBQUksOERBQWUsRUFBUSxDQUFDO1FBakczQyxJQUFJLENBQUMsUUFBUSxDQUFDLGlCQUFpQixDQUFDLENBQUM7UUFDakMsc0VBQXNFO1FBQ3RFLHlFQUF5RTtRQUN6RSxNQUFNLE1BQU0sR0FBRyxRQUFRLENBQUMsYUFBYSxDQUFDLFFBQVEsQ0FBQyxDQUFDO1FBQ2hELElBQUksQ0FBQyxJQUFJLENBQUMsV0FBVyxDQUFDLE1BQU0sQ0FBQyxDQUFDO1FBQzlCLHFFQUFxRTtRQUNyRSxNQUFNLENBQUMsTUFBTSxHQUFHLEdBQUcsRUFBRTtZQUNuQixNQUFNLElBQUksR0FBRyxNQUFNLENBQUMsYUFBYyxDQUFDLFFBQVEsQ0FBQyxhQUFhLENBQUMsTUFBTSxDQUFDLENBQUM7WUFDbEUsSUFBSSxDQUFDLEtBQUssQ0FBQyxNQUFNLEdBQUcsS0FBSyxDQUFDO1lBQzFCLE1BQU0sQ0FBQyxhQUFjLENBQUMsUUFBUSxDQUFDLElBQUksR0FBRyxJQUFJLENBQUM7WUFDM0MsSUFBSSxDQUFDLE9BQU8sR0FBRyxNQUFNLENBQUMsYUFBYyxDQUFDLFFBQVEsQ0FBQyxhQUFhLENBQUMsUUFBUSxDQUFDLENBQUM7WUFDdEUsaUVBQWlFO1lBQ2pFLHNDQUFzQztZQUN0QyxJQUFJLENBQUUsTUFBYyxD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LFVBQVUsR0FBaUIsRUFBRSxDQUFDO1FBRXBDLEtBQUssSUFBSSxNQUFNLEdBQUcsQ0FBQyxFQUFFLE1BQU0sR0FBRyxjQUFjLENBQUMsTUFBTSxFQUFFLE1BQU0sSUFBSSxTQUFTLEVBQUU7WUFDeEUsTUFBTSxLQUFLLEdBQUcsY0FBYyxDQUFDLEtBQUssQ0FBQyxNQUFNLEVBQUUsTUFBTSxHQUFHLFNBQVMsQ0FBQyxDQUFDO1lBRS9ELE1BQU0sV0FBVyxHQUFHLElBQUksS0FBSyxDQUFDLEtBQUssQ0FBQyxNQUFNLENBQUMsQ0FBQztZQUM1QyxLQUFLLElBQUksQ0FBQyxHQUFHLENBQUMsRUFBRSxDQUFDLEdBQUcsS0FBSyxDQUFDLE1BQU0sRUFBRSxDQUFDLEVBQUUsRUFBRTtnQkFDckMsV0FBVyxDQUFDLENBQUMsQ0FBQyxHQUFHLEtBQUssQ0FBQyxVQUFVLENBQUMsQ0FBQyxDQUFDLENBQUM7YUFDdEM7WUFDRCxNQUFNLFNBQVMsR0FBRyxJQUFJLFVBQVUsQ0FBQyxXQUFXLENBQUMsQ0FBQztZQUM5QyxVQUFVLENBQUMsSUFBSSxDQUFDLFNBQVMsQ0FBQyxDQUFDO1NBQzVCO1FBRUQsT0FBTyxJQUFJLElBQUksQ0FBQyxVQUFVLEVBQUUsRUFBRSxJQUFJLEVBQUUsV0FBVyxFQUFFLENBQUMsQ0FBQztJQUNyRCxDQUFDO0lBcEJlLGlCQUFTLFlBb0J4QjtBQUNILENBQUMsRUEzQ1MsT0FBTyxLQUFQLE9BQU8sUUEyQ2hCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3BkZi1leHRlbnNpb24vc3JjL2luZGV4LnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIHBkZi1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQgeyBJUmVuZGVyTWltZSB9IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUtaW50ZXJmYWNlcyc7XG5pbXBvcnQgeyBQcm9taXNlRGVsZWdhdGUgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBEaXNwb3NhYmxlRGVsZWdhdGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgTUlNRSB0eXBlIGZvciBQREYuXG4gKi9cbmNvbnN0IE1JTUVfVFlQRSA9ICdhcHBsaWNhdGlvbi9wZGYnO1xuXG4vKipcbiAqIEEgY2xhc3MgZm9yIHJlbmRlcmluZyBhIFBERiBkb2N1bWVudC5cbiAqL1xuZXhwb3J0IGNsYXNzIFJlbmRlcmVkUERGIGV4dGVuZHMgV2lkZ2V0IGltcGxlbWVudHMgSVJlbmRlck1pbWUuSVJlbmRlcmVyIHtcbiAgY29uc3RydWN0b3IoKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmFkZENsYXNzKCdqcC1QREZDb250YWluZXInKTtcbiAgICAvLyBXZSBwdXQgdGhlIG9iamVjdCBpbiBhbiBpZnJhbWUsIHdoaWNoIHNlZW1zIHRvIGhhdmUgYSBiZXR0ZXIgY2hhbmNlXG4gICAgLy8gb2YgcmV0YWluaW5nIGl0cyBzY3JvbGwgcG9zaXRpb24gdXBvbiB0YWIgZm9jdXNpbmcsIG1vdmluZyBhcm91bmQgZXRjLlxuICAgIGNvbnN0IGlmcmFtZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2lmcmFtZScpO1xuICAgIHRoaXMubm9kZS5hcHBlbmRDaGlsZChpZnJhbWUpO1xuICAgIC8vIFRoZSBpZnJhbWUgY29udGVudCB3aW5kb3cgaXMgbm90IGF2YWlsYWJsZSB1bnRpbCB0aGUgb25sb2FkIGV2ZW50LlxuICAgIGlmcmFtZS5vbmxvYWQgPSAoKSA9PiB7XG4gICAgICBjb25zdCBib2R5ID0gaWZyYW1lLmNvbnRlbnRXaW5kb3chLmRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2JvZHknKTtcbiAgICAgIGJvZHkuc3R5bGUubWFyZ2luID0gJzBweCc7XG4gICAgICBpZnJhbWUuY29udGVudFdpbmRvdyEuZG9jdW1lbnQuYm9keSA9IGJvZHk7XG4gICAgICB0aGlzLl9vYmplY3QgPSBpZnJhbWUuY29udGVudFdpbmRvdyEuZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnb2JqZWN0Jyk7XG4gICAgICAvLyB3b3JrIGFyb3VuZCBmb3IgaHR0cHM6Ly9kaXNjdXNzaW9ucy5hcHBsZS5jb20vdGhyZWFkLzI1MjI0Nzc0MFxuICAgICAgLy8gRGV0ZWN0IGlmIHJ1bm5pbmcgb24gRGVza3RvcCBTYWZhcmlcbiAgICAgIGlmICghKHdpbmRvdyBhcyBhbnkpLnNhZmFyaSkge1xuICAgICAgICB0aGlzLl9vYmplY3QudHlwZSA9IE1JTUVfVFlQRTtcbiAgICAgIH1cbiAgICAgIHRoaXMuX29iamVjdC53aWR0aCA9ICcxMDAlJztcbiAgICAgIHRoaXMuX29iamVjdC5oZWlnaHQgPSAnMTAwJSc7XG4gICAgICBib2R5LmFwcGVuZENoaWxkKHRoaXMuX29iamVjdCk7XG4gICAgICB0aGlzLl9yZWFkeS5yZXNvbHZlKHZvaWQgMCk7XG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgUERGIGludG8gdGhpcyB3aWRnZXQncyBub2RlLlxuICAgKi9cbiAgYXN5bmMgcmVuZGVyTW9kZWwobW9kZWw6IElSZW5kZXJNaW1lLklNaW1lTW9kZWwpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBhd2FpdCB0aGlzLl9yZWFkeS5wcm9taXNlO1xuICAgIGNvbnN0IGRhdGEgPSBtb2RlbC5kYXRhW01JTUVfVFlQRV0gYXMgc3RyaW5nIHwgdW5kZWZpbmVkO1xuICAgIGlmIChcbiAgICAgICFkYXRhIHx8XG4gICAgICAoZGF0YS5sZW5ndGggPT09IHRoaXMuX2Jhc2U2NC5sZW5ndGggJiYgZGF0YSA9PT0gdGhpcy5fYmFzZTY0KVxuICAgICkge1xuICAgICAgLy8gSWYgdGhlcmUgaXMgbm8gZGF0YSwgb3IgaWYgdGhlIHN0cmluZyBoYXMgbm90IGNoYW5nZWQsIHdlIGRvIG5vdFxuICAgICAgLy8gbmVlZCB0byByZS1wYXJzZSB0aGUgZGF0YSBhbmQgcmVyZW5kZXIuIFdlIGRvLCBob3dldmVyLCBjaGVja1xuICAgICAgLy8gZm9yIGEgZnJhZ21lbnQgaWYgdGhlIHVzZXIgd2FudHMgdG8gc2Nyb2xsIHRoZSBvdXRwdXQuXG4gICAgICBpZiAobW9kZWwubWV0YWRhdGEuZnJhZ21lbnQgJiYgdGhpcy5fb2JqZWN0LmRhdGEpIHtcbiAgICAgICAgY29uc3QgdXJsID0gdGhpcy5fb2JqZWN0LmRhdGE7XG4gICAgICAgIHRoaXMuX29iamVjdC5kYXRhID0gYCR7dXJsLnNwbGl0KCcjJylbMF19JHttb2RlbC5tZXRhZGF0YS5mcmFnbWVudH1gO1xuICAgICAgfVxuICAgICAgLy8gRm9yIHNvbWUgb3BhcXVlIHJlYXNvbiwgRmlyZWZveCBzZWVtcyB0byBsb29zZSBpdHMgc2Nyb2xsIHBvc2l0aW9uXG4gICAgICAvLyB1cG9uIHVuaGlkaW5nIGEgUERGLiBCdXQgdHJpZ2dlcmluZyBhIHJlZnJlc2ggb2YgdGhlIFVSTCBtYWtlcyBpdFxuICAgICAgLy8gZmluZCBpdCBhZ2Fpbi4gTm8gaWRlYSB3aGF0IHRoZSByZWFzb24gZm9yIHRoaXMgaXMuXG4gICAgICBpZiAoUHJpdmF0ZS5JU19GSVJFRk9YKSB7XG4gICAgICAgIHRoaXMuX29iamVjdC5kYXRhID0gdGhpcy5fb2JqZWN0LmRhdGE7IC8vIGVzbGludC1kaXNhYmxlLWxpbmVcbiAgICAgIH1cbiAgICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUodm9pZCAwKTtcbiAgICB9XG4gICAgdGhpcy5fYmFzZTY0ID0gZGF0YTtcbiAgICBjb25zdCBibG9iID0gUHJpdmF0ZS5iNjR0b0Jsb2IoZGF0YSwgTUlNRV9UWVBFKTtcblxuICAgIC8vIFJlbGVhc2UgcmVmZXJlbmNlIHRvIGFueSBwcmV2aW91cyBvYmplY3QgdXJsLlxuICAgIGlmICh0aGlzLl9kaXNwb3NhYmxlKSB7XG4gICAgICB0aGlzLl9kaXNwb3NhYmxlLmRpc3Bvc2UoKTtcbiAgICB9XG4gICAgbGV0IG9iamVjdFVybCA9IFVSTC5jcmVhdGVPYmplY3RVUkwoYmxvYik7XG4gICAgaWYgKG1vZGVsLm1ldGFkYXRhLmZyYWdtZW50KSB7XG4gICAgICBvYmplY3RVcmwgKz0gbW9kZWwubWV0YWRhdGEuZnJhZ21lbnQ7XG4gICAgfVxuICAgIHRoaXMuX29iamVjdC5kYXRhID0gb2JqZWN0VXJsO1xuXG4gICAgLy8gU2V0IHRoZSBkaXNwb3NhYmxlIHJlbGVhc2UgdGhlIG9iamVjdCBVUkwuXG4gICAgdGhpcy5fZGlzcG9zYWJsZSA9IG5ldyBEaXNwb3NhYmxlRGVsZWdhdGUoKCkgPT4ge1xuICAgICAgdHJ5IHtcbiAgICAgICAgVVJMLnJldm9rZU9iamVjdFVSTChvYmplY3RVcmwpO1xuICAgICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgLyogbm8tb3AgKi9cbiAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm47XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGEgYGJlZm9yZS1oaWRlYCBtZXNzYWdlLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQmVmb3JlSGlkZSgpOiB2b2lkIHtcbiAgICAvLyBEaXNwb3NlIG9mIGFueSBVUkwgZnJhZ21lbnQgYmVmb3JlIGhpZGluZyB0aGUgd2lkZ2V0XG4gICAgLy8gc28gdGhhdCBpdCBpcyBub3QgcmVtZW1iZXJlZCB1cG9uIHNob3cuIE9ubHkgRmlyZWZveFxuICAgIC8vIHNlZW1zIHRvIGhhdmUgYSBwcm9ibGVtIHdpdGggdGhpcy5cbiAgICBpZiAoUHJpdmF0ZS5JU19GSVJFRk9YKSB7XG4gICAgICB0aGlzLl9vYmplY3QuZGF0YSA9IHRoaXMuX29iamVjdC5kYXRhLnNwbGl0KCcjJylbMF07XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIERpc3Bvc2Ugb2YgdGhlIHJlc291cmNlcyBoZWxkIGJ5IHRoZSBwZGYgd2lkZ2V0LlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5fZGlzcG9zYWJsZSkge1xuICAgICAgdGhpcy5fZGlzcG9zYWJsZS5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIHByaXZhdGUgX2Jhc2U2NCA9ICcnO1xuICBwcml2YXRlIF9kaXNwb3NhYmxlOiBEaXNwb3NhYmxlRGVsZWdhdGUgfCBudWxsID0gbnVsbDtcbiAgcHJpdmF0ZSBfb2JqZWN0OiBIVE1MT2JqZWN0RWxlbWVudDtcbiAgcHJpdmF0ZSBfcmVhZHkgPSBuZXcgUHJvbWlzZURlbGVnYXRlPHZvaWQ+KCk7XG59XG5cbi8qKlxuICogQSBtaW1lIHJlbmRlcmVyIGZhY3RvcnkgZm9yIFBERiBkYXRhLlxuICovXG5leHBvcnQgY29uc3QgcmVuZGVyZXJGYWN0b3J5OiBJUmVuZGVyTWltZS5JUmVuZGVyZXJGYWN0b3J5ID0ge1xuICBzYWZlOiBmYWxzZSxcbiAgbWltZVR5cGVzOiBbTUlNRV9UWVBFXSxcbiAgZGVmYXVsdFJhbms6IDEwMCxcbiAgY3JlYXRlUmVuZGVyZXI6IG9wdGlvbnMgPT4gbmV3IFJlbmRlcmVkUERGKClcbn07XG5cbmNvbnN0IGV4dGVuc2lvbnM6IElSZW5kZXJNaW1lLklFeHRlbnNpb24gfCBJUmVuZGVyTWltZS5JRXh0ZW5zaW9uW10gPSBbXG4gIHtcbiAgICBpZDogJ0BqdXB5dGVybGFiL3BkZi1leHRlbnNpb246ZmFjdG9yeScsXG4gICAgcmVuZGVyZXJGYWN0b3J5LFxuICAgIGRhdGFUeXBlOiAnc3RyaW5nJyxcbiAgICBkb2N1bWVudFdpZGdldEZhY3RvcnlPcHRpb25zOiB7XG4gICAgICBuYW1lOiAnUERGJyxcbiAgICAgIC8vIFRPRE86IHRyYW5zbGF0ZSBsYWJlbFxuICAgICAgbW9kZWxOYW1lOiAnYmFzZTY0JyxcbiAgICAgIHByaW1hcnlGaWxlVHlwZTogJ1BERicsXG4gICAgICBmaWxlVHlwZXM6IFsnUERGJ10sXG4gICAgICBkZWZhdWx0Rm9yOiBbJ1BERiddXG4gICAgfVxuICB9XG5dO1xuXG5leHBvcnQgZGVmYXVsdCBleHRlbnNpb25zO1xuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBQREYgd2lkZ2V0IHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogQSBmbGFnIGZvciBkZXRlcm1pbmluZyB3aGV0aGVyIHRoZSB1c2VyIGlzIHVzaW5nIEZpcmVmb3guXG4gICAqIFRoZXJlIGFyZSBzb21lIGRpZmZlcmVudCBQREYgdmlld2VyIGJlaGF2aW9ycyBvbiBGaXJlZm94LFxuICAgKiBhbmQgd2UgdHJ5IHRvIGFkZHJlc3MgdGhlbSB3aXRoIHRoaXMuIFVzZXIgYWdlbnQgc3RyaW5nIHBhcnNpbmdcbiAgICogaXMgKm5vdCogcmVsaWFibGUsIHNvIHRoaXMgc2hvdWxkIGJlIGNvbnNpZGVyZWQgYSBiZXN0LWVmZm9ydCB0ZXN0LlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IElTX0ZJUkVGT1g6IGJvb2xlYW4gPSAvRmlyZWZveC8udGVzdChuYXZpZ2F0b3IudXNlckFnZW50KTtcblxuICAvKipcbiAgICogQ29udmVydCBhIGJhc2U2NCBlbmNvZGVkIHN0cmluZyB0byBhIEJsb2Igb2JqZWN0LlxuICAgKiBNb2RpZmllZCBmcm9tIGEgc25pcHBldCBmb3VuZCBoZXJlOlxuICAgKiBodHRwczovL3N0YWNrb3ZlcmZsb3cuY29tL3F1ZXN0aW9ucy8xNjI0NTc2Ny9jcmVhdGluZy1hLWJsb2ItZnJvbS1hLWJhc2U2NC1zdHJpbmctaW4tamF2YXNjcmlwdFxuICAgKlxuICAgKiBAcGFyYW0gYjY0RGF0YSAtIFRoZSBiYXNlNjQgZW5jb2RlZCBkYXRhLlxuICAgKlxuICAgKiBAcGFyYW0gY29udGVudFR5cGUgLSBUaGUgbWltZSB0eXBlIG9mIHRoZSBkYXRhLlxuICAgKlxuICAgKiBAcGFyYW0gc2xpY2VTaXplIC0gVGhlIHNpemUgdG8gY2h1bmsgdGhlIGRhdGEgaW50byBmb3IgcHJvY2Vzc2luZy5cbiAgICpcbiAgICogQHJldHVybnMgYSBCbG9iIGZvciB0aGUgZGF0YS5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBiNjR0b0Jsb2IoXG4gICAgYjY0RGF0YTogc3RyaW5nLFxuICAgIGNvbnRlbnRUeXBlOiBzdHJpbmcgPSAnJyxcbiAgICBzbGljZVNpemU6IG51bWJlciA9IDUxMlxuICApOiBCbG9iIHtcbiAgICBjb25zdCBieXRlQ2hhcmFjdGVycyA9IGF0b2IoYjY0RGF0YSk7XG4gICAgY29uc3QgYnl0ZUFycmF5czogVWludDhBcnJheVtdID0gW107XG5cbiAgICBmb3IgKGxldCBvZmZzZXQgPSAwOyBvZmZzZXQgPCBieXRlQ2hhcmFjdGVycy5sZW5ndGg7IG9mZnNldCArPSBzbGljZVNpemUpIHtcbiAgICAgIGNvbnN0IHNsaWNlID0gYnl0ZUNoYXJhY3RlcnMuc2xpY2Uob2Zmc2V0LCBvZmZzZXQgKyBzbGljZVNpemUpO1xuXG4gICAgICBjb25zdCBieXRlTnVtYmVycyA9IG5ldyBBcnJheShzbGljZS5sZW5ndGgpO1xuICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBzbGljZS5sZW5ndGg7IGkrKykge1xuICAgICAgICBieXRlTnVtYmVyc1tpXSA9IHNsaWNlLmNoYXJDb2RlQXQoaSk7XG4gICAgICB9XG4gICAgICBjb25zdCBieXRlQXJyYXkgPSBuZXcgVWludDhBcnJheShieXRlTnVtYmVycyk7XG4gICAgICBieXRlQXJyYXlzLnB1c2goYnl0ZUFycmF5KTtcbiAgICB9XG5cbiAgICByZXR1cm4gbmV3IEJsb2IoYnl0ZUFycmF5cywgeyB0eXBlOiBjb250ZW50VHlwZSB9KTtcbiAgfVxufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9