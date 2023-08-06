"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_htmlviewer_lib_index_js-_a0710"],{

/***/ "../../packages/htmlviewer/lib/index.js":
/*!**********************************************!*\
  !*** ../../packages/htmlviewer/lib/index.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "HTMLViewer": () => (/* binding */ HTMLViewer),
/* harmony export */   "HTMLViewerFactory": () => (/* binding */ HTMLViewerFactory),
/* harmony export */   "IHTMLViewerTracker": () => (/* binding */ IHTMLViewerTracker),
/* harmony export */   "ToolbarItems": () => (/* binding */ ToolbarItems)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_6__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module htmlviewer
 */







/**
 * The HTML viewer tracker token.
 */
const IHTMLViewerTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_4__.Token('@jupyterlab/htmlviewer:IHTMLViewerTracker');
/**
 * The timeout to wait for change activity to have ceased before rendering.
 */
const RENDER_TIMEOUT = 1000;
/**
 * The CSS class to add to the HTMLViewer Widget.
 */
const CSS_CLASS = 'jp-HTMLViewer';
/**
 * A viewer widget for HTML documents.
 *
 * #### Notes
 * The iframed HTML document can pose a potential security risk,
 * since it can execute Javascript, and make same-origin requests
 * to the server, thereby executing arbitrary Javascript.
 *
 * Here, we sandbox the iframe so that it can't execute Javascript
 * or launch any popups. We allow one exception: 'allow-same-origin'
 * requests, so that local HTML documents can access CSS, images,
 * etc from the files system.
 */
class HTMLViewer extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.DocumentWidget {
    /**
     * Create a new widget for rendering HTML.
     */
    constructor(options) {
        super(Object.assign(Object.assign({}, options), { content: new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.IFrame({ sandbox: ['allow-same-origin'] }) }));
        this._renderPending = false;
        this._parser = new DOMParser();
        this._monitor = null;
        this._objectUrl = '';
        this._trustedChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(this);
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
        this.content.addClass(CSS_CLASS);
        void this.context.ready.then(() => {
            this.update();
            // Throttle the rendering rate of the widget.
            this._monitor = new _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.ActivityMonitor({
                signal: this.context.model.contentChanged,
                timeout: RENDER_TIMEOUT
            });
            this._monitor.activityStopped.connect(this.update, this);
        });
    }
    /**
     * Whether the HTML document is trusted. If trusted,
     * it can execute Javascript in the iframe sandbox.
     */
    get trusted() {
        return this.content.sandbox.indexOf('allow-scripts') !== -1;
    }
    set trusted(value) {
        if (this.trusted === value) {
            return;
        }
        if (value) {
            this.content.sandbox = Private.trusted;
        }
        else {
            this.content.sandbox = Private.untrusted;
        }
        // eslint-disable-next-line
        this.content.url = this.content.url; // Force a refresh.
        this._trustedChanged.emit(value);
    }
    /**
     * Emitted when the trust state of the document changes.
     */
    get trustedChanged() {
        return this._trustedChanged;
    }
    /**
     * Dispose of resources held by the html viewer.
     */
    dispose() {
        if (this._objectUrl) {
            try {
                URL.revokeObjectURL(this._objectUrl);
            }
            catch (error) {
                /* no-op */
            }
        }
        super.dispose();
    }
    /**
     * Handle and update request.
     */
    onUpdateRequest() {
        if (this._renderPending) {
            return;
        }
        this._renderPending = true;
        void this._renderModel().then(() => (this._renderPending = false));
    }
    /**
     * Render HTML in IFrame into this widget's node.
     */
    async _renderModel() {
        let data = this.context.model.toString();
        data = await this._setBase(data);
        // Set the new iframe url.
        const blob = new Blob([data], { type: 'text/html' });
        const oldUrl = this._objectUrl;
        this._objectUrl = URL.createObjectURL(blob);
        this.content.url = this._objectUrl;
        // Release reference to any previous object url.
        if (oldUrl) {
            try {
                URL.revokeObjectURL(oldUrl);
            }
            catch (error) {
                /* no-op */
            }
        }
        return;
    }
    /**
     * Set a <base> element in the HTML string so that the iframe
     * can correctly dereference relative links.
     */
    async _setBase(data) {
        const doc = this._parser.parseFromString(data, 'text/html');
        let base = doc.querySelector('base');
        if (!base) {
            base = doc.createElement('base');
            doc.head.insertBefore(base, doc.head.firstChild);
        }
        const path = this.context.path;
        const baseUrl = await this.context.urlResolver.getDownloadUrl(path);
        // Set the base href, plus a fake name for the url of this
        // document. The fake name doesn't really matter, as long
        // as the document can dereference relative links to resources
        // (e.g. CSS and scripts).
        base.href = baseUrl;
        base.target = '_self';
        return doc.documentElement.innerHTML;
    }
}
/**
 * A widget factory for HTMLViewers.
 */
class HTMLViewerFactory extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.ABCWidgetFactory {
    /**
     * Create a new widget given a context.
     */
    createNewWidget(context) {
        return new HTMLViewer({ context });
    }
    /**
     * Default factory for toolbar items to be added after the widget is created.
     */
    defaultToolbarFactory(widget) {
        return [
            // Make a refresh button for the toolbar.
            {
                name: 'refresh',
                widget: ToolbarItems.createRefreshButton(widget, this.translator)
            },
            // Make a trust button for the toolbar.
            {
                name: 'trust',
                widget: ToolbarItems.createTrustButton(widget, this.translator)
            }
        ];
    }
}
/**
 * A namespace for toolbar items generator
 */
var ToolbarItems;
(function (ToolbarItems) {
    /**
     * Create the refresh button
     *
     * @param widget HTML viewer widget
     * @param translator Application translator object
     * @returns Toolbar item button
     */
    function createRefreshButton(widget, translator) {
        const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator).load('jupyterlab');
        return new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.ToolbarButton({
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.refreshIcon,
            onClick: async () => {
                if (!widget.context.model.dirty) {
                    await widget.context.revert();
                    widget.update();
                }
            },
            tooltip: trans.__('Rerender HTML Document')
        });
    }
    ToolbarItems.createRefreshButton = createRefreshButton;
    /**
     * Create the trust button
     *
     * @param document HTML viewer widget
     * @param translator Application translator object
     * @returns Toolbar item button
     */
    function createTrustButton(document, translator) {
        return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_6__.createElement(Private.TrustButtonComponent, { htmlDocument: document, translator: translator }));
    }
    ToolbarItems.createTrustButton = createTrustButton;
})(ToolbarItems || (ToolbarItems = {}));
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * Sandbox exceptions for untrusted HTML.
     */
    Private.untrusted = [];
    /**
     * Sandbox exceptions for trusted HTML.
     */
    Private.trusted = ['allow-scripts'];
    /**
     * React component for a trusted button.
     *
     * This wraps the ToolbarButtonComponent and watches for trust changes.
     */
    function TrustButtonComponent(props) {
        const translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_2__.nullTranslator;
        const trans = translator.load('jupyterlab');
        return (react__WEBPACK_IMPORTED_MODULE_6__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.UseSignal, { signal: props.htmlDocument.trustedChanged, initialSender: props.htmlDocument }, () => (react__WEBPACK_IMPORTED_MODULE_6__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.ToolbarButtonComponent, { className: "", onClick: () => (props.htmlDocument.trusted = !props.htmlDocument.trusted), tooltip: trans.__(`Whether the HTML file is trusted.
Trusting the file allows scripts to run in it,
which may result in security risks.
Only enable for files you trust.`), label: props.htmlDocument.trusted
                ? trans.__('Distrust HTML')
                : trans.__('Trust HTML') }))));
    }
    Private.TrustButtonComponent = TrustButtonComponent;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfaHRtbHZpZXdlcl9saWJfaW5kZXhfanMtX2EwNzEwLjhhOTI5OWY2NmMxODY4N2I2YjkxLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQUdxRDtBQU12QjtBQUNxQztBQVFuQztBQUNPO0FBQ1U7QUFFckI7QUFPL0I7O0dBRUc7QUFDSSxNQUFNLGtCQUFrQixHQUFHLElBQUksb0RBQUssQ0FDekMsMkNBQTJDLENBQzVDLENBQUM7QUFDRjs7R0FFRztBQUNILE1BQU0sY0FBYyxHQUFHLElBQUksQ0FBQztBQUU1Qjs7R0FFRztBQUNILE1BQU0sU0FBUyxHQUFHLGVBQWUsQ0FBQztBQUVsQzs7Ozs7Ozs7Ozs7O0dBWUc7QUFDSSxNQUFNLFVBQ1gsU0FBUSxtRUFBc0I7SUFHOUI7O09BRUc7SUFDSCxZQUFZLE9BQStDO1FBQ3pELEtBQUssaUNBQ0EsT0FBTyxLQUNWLE9BQU8sRUFBRSxJQUFJLDZEQUFNLENBQUMsRUFBRSxPQUFPLEVBQUUsQ0FBQyxtQkFBbUIsQ0FBQyxFQUFFLENBQUMsSUFDdkQsQ0FBQztRQW9IRyxtQkFBYyxHQUFHLEtBQUssQ0FBQztRQUN2QixZQUFPLEdBQUcsSUFBSSxTQUFTLEVBQUUsQ0FBQztRQUMxQixhQUFRLEdBQ2QsSUFBSSxDQUFDO1FBQ0MsZUFBVSxHQUFXLEVBQUUsQ0FBQztRQUN4QixvQkFBZSxHQUFHLElBQUkscURBQU0sQ0FBZ0IsSUFBSSxDQUFDLENBQUM7UUF4SHhELElBQUksQ0FBQyxVQUFVLEdBQUcsT0FBTyxDQUFDLFVBQVUsSUFBSSxtRUFBYyxDQUFDO1FBQ3ZELElBQUksQ0FBQyxPQUFPLENBQUMsUUFBUSxDQUFDLFNBQVMsQ0FBQyxDQUFDO1FBRWpDLEtBQUssSUFBSSxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsSUFBSSxDQUFDLEdBQUcsRUFBRTtZQUNoQyxJQUFJLENBQUMsTUFBTSxFQUFFLENBQUM7WUFDZCw2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ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2h0bWx2aWV3ZXIvc3JjL2luZGV4LnRzeCJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxufCBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbnwtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tKi9cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGh0bWx2aWV3ZXJcbiAqL1xuXG5pbXBvcnQgeyBJV2lkZ2V0VHJhY2tlciB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IEFjdGl2aXR5TW9uaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQge1xuICBBQkNXaWRnZXRGYWN0b3J5LFxuICBEb2N1bWVudFJlZ2lzdHJ5LFxuICBEb2N1bWVudFdpZGdldCxcbiAgSURvY3VtZW50V2lkZ2V0XG59IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7XG4gIElGcmFtZSxcbiAgUmVhY3RXaWRnZXQsXG4gIHJlZnJlc2hJY29uLFxuICBUb29sYmFyQnV0dG9uLFxuICBUb29sYmFyQnV0dG9uQ29tcG9uZW50LFxuICBVc2VTaWduYWxcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5cbi8qKlxuICogQSBjbGFzcyB0aGF0IHRyYWNrcyBIVE1MIHZpZXdlciB3aWRnZXRzLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElIVE1MVmlld2VyVHJhY2tlciBleHRlbmRzIElXaWRnZXRUcmFja2VyPEhUTUxWaWV3ZXI+IHt9XG5cbi8qKlxuICogVGhlIEhUTUwgdmlld2VyIHRyYWNrZXIgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJSFRNTFZpZXdlclRyYWNrZXIgPSBuZXcgVG9rZW48SUhUTUxWaWV3ZXJUcmFja2VyPihcbiAgJ0BqdXB5dGVybGFiL2h0bWx2aWV3ZXI6SUhUTUxWaWV3ZXJUcmFja2VyJ1xuKTtcbi8qKlxuICogVGhlIHRpbWVvdXQgdG8gd2FpdCBmb3IgY2hhbmdlIGFjdGl2aXR5IHRvIGhhdmUgY2Vhc2VkIGJlZm9yZSByZW5kZXJpbmcuXG4gKi9cbmNvbnN0IFJFTkRFUl9USU1FT1VUID0gMTAwMDtcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIHRvIGFkZCB0byB0aGUgSFRNTFZpZXdlciBXaWRnZXQuXG4gKi9cbmNvbnN0IENTU19DTEFTUyA9ICdqcC1IVE1MVmlld2VyJztcblxuLyoqXG4gKiBBIHZpZXdlciB3aWRnZXQgZm9yIEhUTUwgZG9jdW1lbnRzLlxuICpcbiAqICMjIyMgTm90ZXNcbiAqIFRoZSBpZnJhbWVkIEhUTUwgZG9jdW1lbnQgY2FuIHBvc2UgYSBwb3RlbnRpYWwgc2VjdXJpdHkgcmlzayxcbiAqIHNpbmNlIGl0IGNhbiBleGVjdXRlIEphdmFzY3JpcHQsIGFuZCBtYWtlIHNhbWUtb3JpZ2luIHJlcXVlc3RzXG4gKiB0byB0aGUgc2VydmVyLCB0aGVyZWJ5IGV4ZWN1dGluZyBhcmJpdHJhcnkgSmF2YXNjcmlwdC5cbiAqXG4gKiBIZXJlLCB3ZSBzYW5kYm94IHRoZSBpZnJhbWUgc28gdGhhdCBpdCBjYW4ndCBleGVjdXRlIEphdmFzY3JpcHRcbiAqIG9yIGxhdW5jaCBhbnkgcG9wdXBzLiBXZSBhbGxvdyBvbmUgZXhjZXB0aW9uOiAnYWxsb3ctc2FtZS1vcmlnaW4nXG4gKiByZXF1ZXN0cywgc28gdGhhdCBsb2NhbCBIVE1MIGRvY3VtZW50cyBjYW4gYWNjZXNzIENTUywgaW1hZ2VzLFxuICogZXRjIGZyb20gdGhlIGZpbGVzIHN5c3RlbS5cbiAqL1xuZXhwb3J0IGNsYXNzIEhUTUxWaWV3ZXJcbiAgZXh0ZW5kcyBEb2N1bWVudFdpZGdldDxJRnJhbWU+XG4gIGltcGxlbWVudHMgSURvY3VtZW50V2lkZ2V0PElGcmFtZT5cbntcbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB3aWRnZXQgZm9yIHJlbmRlcmluZyBIVE1MLlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogRG9jdW1lbnRXaWRnZXQuSU9wdGlvbnNPcHRpb25hbENvbnRlbnQpIHtcbiAgICBzdXBlcih7XG4gICAgICAuLi5vcHRpb25zLFxuICAgICAgY29udGVudDogbmV3IElGcmFtZSh7IHNhbmRib3g6IFsnYWxsb3ctc2FtZS1vcmlnaW4nXSB9KVxuICAgIH0pO1xuICAgIHRoaXMudHJhbnNsYXRvciA9IG9wdGlvbnMudHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgICB0aGlzLmNvbnRlbnQuYWRkQ2xhc3MoQ1NTX0NMQVNTKTtcblxuICAgIHZvaWQgdGhpcy5jb250ZXh0LnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgdGhpcy51cGRhdGUoKTtcbiAgICAgIC8vIFRocm90dGxlIHRoZSByZW5kZXJpbmcgcmF0ZSBvZiB0aGUgd2lkZ2V0LlxuICAgICAgdGhpcy5fbW9uaXRvciA9IG5ldyBBY3Rpdml0eU1vbml0b3Ioe1xuICAgICAgICBzaWduYWw6IHRoaXMuY29udGV4dC5tb2RlbC5jb250ZW50Q2hhbmdlZCxcbiAgICAgICAgdGltZW91dDogUkVOREVSX1RJTUVPVVRcbiAgICAgIH0pO1xuICAgICAgdGhpcy5fbW9uaXRvci5hY3Rpdml0eVN0b3BwZWQuY29ubmVjdCh0aGlzLnVwZGF0ZSwgdGhpcyk7XG4gICAgfSk7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgSFRNTCBkb2N1bWVudCBpcyB0cnVzdGVkLiBJZiB0cnVzdGVkLFxuICAgKiBpdCBjYW4gZXhlY3V0ZSBKYXZhc2NyaXB0IGluIHRoZSBpZnJhbWUgc2FuZGJveC5cbiAgICovXG4gIGdldCB0cnVzdGVkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLmNvbnRlbnQuc2FuZGJveC5pbmRleE9mKCdhbGxvdy1zY3JpcHRzJykgIT09IC0xO1xuICB9XG4gIHNldCB0cnVzdGVkKHZhbHVlOiBib29sZWFuKSB7XG4gICAgaWYgKHRoaXMudHJ1c3RlZCA9PT0gdmFsdWUpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgaWYgKHZhbHVlKSB7XG4gICAgICB0aGlzLmNvbnRlbnQuc2FuZGJveCA9IFByaXZhdGUudHJ1c3RlZDtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5jb250ZW50LnNhbmRib3ggPSBQcml2YXRlLnVudHJ1c3RlZDtcbiAgICB9XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lXG4gICAgdGhpcy5jb250ZW50LnVybCA9IHRoaXMuY29udGVudC51cmw7IC8vIEZvcmNlIGEgcmVmcmVzaC5cbiAgICB0aGlzLl90cnVzdGVkQ2hhbmdlZC5lbWl0KHZhbHVlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBFbWl0dGVkIHdoZW4gdGhlIHRydXN0IHN0YXRlIG9mIHRoZSBkb2N1bWVudCBjaGFuZ2VzLlxuICAgKi9cbiAgZ2V0IHRydXN0ZWRDaGFuZ2VkKCk6IElTaWduYWw8dGhpcywgYm9vbGVhbj4ge1xuICAgIHJldHVybiB0aGlzLl90cnVzdGVkQ2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHJlc291cmNlcyBoZWxkIGJ5IHRoZSBodG1sIHZpZXdlci5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuX29iamVjdFVybCkge1xuICAgICAgdHJ5IHtcbiAgICAgICAgVVJMLnJldm9rZU9iamVjdFVSTCh0aGlzLl9vYmplY3RVcmwpO1xuICAgICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgLyogbm8tb3AgKi9cbiAgICAgIH1cbiAgICB9XG4gICAgc3VwZXIuZGlzcG9zZSgpO1xuICB9XG5cbiAgLyoqXG4gICAqIEhhbmRsZSBhbmQgdXBkYXRlIHJlcXVlc3QuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KCk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9yZW5kZXJQZW5kaW5nKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuICAgIHRoaXMuX3JlbmRlclBlbmRpbmcgPSB0cnVlO1xuICAgIHZvaWQgdGhpcy5fcmVuZGVyTW9kZWwoKS50aGVuKCgpID0+ICh0aGlzLl9yZW5kZXJQZW5kaW5nID0gZmFsc2UpKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgSFRNTCBpbiBJRnJhbWUgaW50byB0aGlzIHdpZGdldCdzIG5vZGUuXG4gICAqL1xuICBwcml2YXRlIGFzeW5jIF9yZW5kZXJNb2RlbCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBsZXQgZGF0YSA9IHRoaXMuY29udGV4dC5tb2RlbC50b1N0cmluZygpO1xuICAgIGRhdGEgPSBhd2FpdCB0aGlzLl9zZXRCYXNlKGRhdGEpO1xuXG4gICAgLy8gU2V0IHRoZSBuZXcgaWZyYW1lIHVybC5cbiAgICBjb25zdCBibG9iID0gbmV3IEJsb2IoW2RhdGFdLCB7IHR5cGU6ICd0ZXh0L2h0bWwnIH0pO1xuICAgIGNvbnN0IG9sZFVybCA9IHRoaXMuX29iamVjdFVybDtcbiAgICB0aGlzLl9vYmplY3RVcmwgPSBVUkwuY3JlYXRlT2JqZWN0VVJMKGJsb2IpO1xuICAgIHRoaXMuY29udGVudC51cmwgPSB0aGlzLl9vYmplY3RVcmw7XG5cbiAgICAvLyBSZWxlYXNlIHJlZmVyZW5jZSB0byBhbnkgcHJldmlvdXMgb2JqZWN0IHVybC5cbiAgICBpZiAob2xkVXJsKSB7XG4gICAgICB0cnkge1xuICAgICAgICBVUkwucmV2b2tlT2JqZWN0VVJMKG9sZFVybCk7XG4gICAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICAvKiBuby1vcCAqL1xuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm47XG4gIH1cblxuICAvKipcbiAgICogU2V0IGEgPGJhc2U+IGVsZW1lbnQgaW4gdGhlIEhUTUwgc3RyaW5nIHNvIHRoYXQgdGhlIGlmcmFtZVxuICAgKiBjYW4gY29ycmVjdGx5IGRlcmVmZXJlbmNlIHJlbGF0aXZlIGxpbmtzLlxuICAgKi9cbiAgcHJpdmF0ZSBhc3luYyBfc2V0QmFzZShkYXRhOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4ge1xuICAgIGNvbnN0IGRvYyA9IHRoaXMuX3BhcnNlci5wYXJzZUZyb21TdHJpbmcoZGF0YSwgJ3RleHQvaHRtbCcpO1xuICAgIGxldCBiYXNlID0gZG9jLnF1ZXJ5U2VsZWN0b3IoJ2Jhc2UnKTtcbiAgICBpZiAoIWJhc2UpIHtcbiAgICAgIGJhc2UgPSBkb2MuY3JlYXRlRWxlbWVudCgnYmFzZScpO1xuICAgICAgZG9jLmhlYWQuaW5zZXJ0QmVmb3JlKGJhc2UsIGRvYy5oZWFkLmZpcnN0Q2hpbGQpO1xuICAgIH1cbiAgICBjb25zdCBwYXRoID0gdGhpcy5jb250ZXh0LnBhdGg7XG4gICAgY29uc3QgYmFzZVVybCA9IGF3YWl0IHRoaXMuY29udGV4dC51cmxSZXNvbHZlci5nZXREb3dubG9hZFVybChwYXRoKTtcblxuICAgIC8vIFNldCB0aGUgYmFzZSBocmVmLCBwbHVzIGEgZmFrZSBuYW1lIGZvciB0aGUgdXJsIG9mIHRoaXNcbiAgICAvLyBkb2N1bWVudC4gVGhlIGZha2UgbmFtZSBkb2Vzbid0IHJlYWxseSBtYXR0ZXIsIGFzIGxvbmdcbiAgICAvLyBhcyB0aGUgZG9jdW1lbnQgY2FuIGRlcmVmZXJlbmNlIHJlbGF0aXZlIGxpbmtzIHRvIHJlc291cmNlc1xuICAgIC8vIChlLmcuIENTUyBhbmQgc2NyaXB0cykuXG4gICAgYmFzZS5ocmVmID0gYmFzZVVybDtcbiAgICBiYXNlLnRhcmdldCA9ICdfc2VsZic7XG4gICAgcmV0dXJuIGRvYy5kb2N1bWVudEVsZW1lbnQuaW5uZXJIVE1MO1xuICB9XG5cbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF9yZW5kZXJQZW5kaW5nID0gZmFsc2U7XG4gIHByaXZhdGUgX3BhcnNlciA9IG5ldyBET01QYXJzZXIoKTtcbiAgcHJpdmF0ZSBfbW9uaXRvcjogQWN0aXZpdHlNb25pdG9yPERvY3VtZW50UmVnaXN0cnkuSU1vZGVsLCB2b2lkPiB8IG51bGwgPVxuICAgIG51bGw7XG4gIHByaXZhdGUgX29iamVjdFVybDogc3RyaW5nID0gJyc7XG4gIHByaXZhdGUgX3RydXN0ZWRDaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCBib29sZWFuPih0aGlzKTtcbn1cblxuLyoqXG4gKiBBIHdpZGdldCBmYWN0b3J5IGZvciBIVE1MVmlld2Vycy5cbiAqL1xuZXhwb3J0IGNsYXNzIEhUTUxWaWV3ZXJGYWN0b3J5IGV4dGVuZHMgQUJDV2lkZ2V0RmFjdG9yeTxIVE1MVmlld2VyPiB7XG4gIC8qKlxuICAgKiBDcmVhdGUgYSBuZXcgd2lkZ2V0IGdpdmVuIGEgY29udGV4dC5cbiAgICovXG4gIHByb3RlY3RlZCBjcmVhdGVOZXdXaWRnZXQoY29udGV4dDogRG9jdW1lbnRSZWdpc3RyeS5Db250ZXh0KTogSFRNTFZpZXdlciB7XG4gICAgcmV0dXJuIG5ldyBIVE1MVmlld2VyKHsgY29udGV4dCB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEZWZhdWx0IGZhY3RvcnkgZm9yIHRvb2xiYXIgaXRlbXMgdG8gYmUgYWRkZWQgYWZ0ZXIgdGhlIHdpZGdldCBpcyBjcmVhdGVkLlxuICAgKi9cbiAgcHJvdGVjdGVkIGRlZmF1bHRUb29sYmFyRmFjdG9yeShcbiAgICB3aWRnZXQ6IEhUTUxWaWV3ZXJcbiAgKTogRG9jdW1lbnRSZWdpc3RyeS5JVG9vbGJhckl0ZW1bXSB7XG4gICAgcmV0dXJuIFtcbiAgICAgIC8vIE1ha2UgYSByZWZyZXNoIGJ1dHRvbiBmb3IgdGhlIHRvb2xiYXIuXG4gICAgICB7XG4gICAgICAgIG5hbWU6ICdyZWZyZXNoJyxcbiAgICAgICAgd2lkZ2V0OiBUb29sYmFySXRlbXMuY3JlYXRlUmVmcmVzaEJ1dHRvbih3aWRnZXQsIHRoaXMudHJhbnNsYXRvcilcbiAgICAgIH0sXG4gICAgICAvLyBNYWtlIGEgdHJ1c3QgYnV0dG9uIGZvciB0aGUgdG9vbGJhci5cbiAgICAgIHtcbiAgICAgICAgbmFtZTogJ3RydXN0JyxcbiAgICAgICAgd2lkZ2V0OiBUb29sYmFySXRlbXMuY3JlYXRlVHJ1c3RCdXR0b24od2lkZ2V0LCB0aGlzLnRyYW5zbGF0b3IpXG4gICAgICB9XG4gICAgXTtcbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciB0b29sYmFyIGl0ZW1zIGdlbmVyYXRvclxuICovXG5leHBvcnQgbmFtZXNwYWNlIFRvb2xiYXJJdGVtcyB7XG4gIC8qKlxuICAgKiBDcmVhdGUgdGhlIHJlZnJlc2ggYnV0dG9uXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgSFRNTCB2aWV3ZXIgd2lkZ2V0XG4gICAqIEBwYXJhbSB0cmFuc2xhdG9yIEFwcGxpY2F0aW9uIHRyYW5zbGF0b3Igb2JqZWN0XG4gICAqIEByZXR1cm5zIFRvb2xiYXIgaXRlbSBidXR0b25cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVSZWZyZXNoQnV0dG9uKFxuICAgIHdpZGdldDogSFRNTFZpZXdlcixcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKTogV2lkZ2V0IHtcbiAgICBjb25zdCB0cmFucyA9ICh0cmFuc2xhdG9yID8/IG51bGxUcmFuc2xhdG9yKS5sb2FkKCdqdXB5dGVybGFiJyk7XG4gICAgcmV0dXJuIG5ldyBUb29sYmFyQnV0dG9uKHtcbiAgICAgIGljb246IHJlZnJlc2hJY29uLFxuICAgICAgb25DbGljazogYXN5bmMgKCkgPT4ge1xuICAgICAgICBpZiAoIXdpZGdldC5jb250ZXh0Lm1vZGVsLmRpcnR5KSB7XG4gICAgICAgICAgYXdhaXQgd2lkZ2V0LmNvbnRleHQucmV2ZXJ0KCk7XG4gICAgICAgICAgd2lkZ2V0LnVwZGF0ZSgpO1xuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgdG9vbHRpcDogdHJhbnMuX18oJ1JlcmVuZGVyIEhUTUwgRG9jdW1lbnQnKVxuICAgIH0pO1xuICB9XG4gIC8qKlxuICAgKiBDcmVhdGUgdGhlIHRydXN0IGJ1dHRvblxuICAgKlxuICAgKiBAcGFyYW0gZG9jdW1lbnQgSFRNTCB2aWV3ZXIgd2lkZ2V0XG4gICAqIEBwYXJhbSB0cmFuc2xhdG9yIEFwcGxpY2F0aW9uIHRyYW5zbGF0b3Igb2JqZWN0XG4gICAqIEByZXR1cm5zIFRvb2xiYXIgaXRlbSBidXR0b25cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVUcnVzdEJ1dHRvbihcbiAgICBkb2N1bWVudDogSFRNTFZpZXdlcixcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuICApOiBXaWRnZXQge1xuICAgIHJldHVybiBSZWFjdFdpZGdldC5jcmVhdGUoXG4gICAgICA8UHJpdmF0ZS5UcnVzdEJ1dHRvbkNvbXBvbmVudFxuICAgICAgICBodG1sRG9jdW1lbnQ9e2RvY3VtZW50fVxuICAgICAgICB0cmFuc2xhdG9yPXt0cmFuc2xhdG9yfVxuICAgICAgLz5cbiAgICApO1xuICB9XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHByaXZhdGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogU2FuZGJveCBleGNlcHRpb25zIGZvciB1bnRydXN0ZWQgSFRNTC5cbiAgICovXG4gIGV4cG9ydCBjb25zdCB1bnRydXN0ZWQ6IElGcmFtZS5TYW5kYm94RXhjZXB0aW9uc1tdID0gW107XG5cbiAgLyoqXG4gICAqIFNhbmRib3ggZXhjZXB0aW9ucyBmb3IgdHJ1c3RlZCBIVE1MLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IHRydXN0ZWQ6IElGcmFtZS5TYW5kYm94RXhjZXB0aW9uc1tdID0gWydhbGxvdy1zY3JpcHRzJ107XG5cbiAgLyoqXG4gICAqIE5hbWVzcGFjZSBmb3IgVHJ1c3RlZEJ1dHRvbi5cbiAgICovXG4gIGV4cG9ydCBuYW1lc3BhY2UgVHJ1c3RCdXR0b25Db21wb25lbnQge1xuICAgIC8qKlxuICAgICAqIEludGVyZmFjZSBmb3IgVHJ1c3RlZEJ1dHRvbiBwcm9wcy5cbiAgICAgKi9cbiAgICBleHBvcnQgaW50ZXJmYWNlIElQcm9wcyB7XG4gICAgICBodG1sRG9jdW1lbnQ6IEhUTUxWaWV3ZXI7XG5cbiAgICAgIC8qKlxuICAgICAgICogTGFuZ3VhZ2UgdHJhbnNsYXRvci5cbiAgICAgICAqL1xuICAgICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBSZWFjdCBjb21wb25lbnQgZm9yIGEgdHJ1c3RlZCBidXR0b24uXG4gICAqXG4gICAqIFRoaXMgd3JhcHMgdGhlIFRvb2xiYXJCdXR0b25Db21wb25lbnQgYW5kIHdhdGNoZXMgZm9yIHRydXN0IGNoYW5nZXMuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gVHJ1c3RCdXR0b25Db21wb25lbnQoXG4gICAgcHJvcHM6IFRydXN0QnV0dG9uQ29tcG9uZW50LklQcm9wc1xuICApOiBKU1guRWxlbWVudCB7XG4gICAgY29uc3QgdHJhbnNsYXRvciA9IHByb3BzLnRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3I7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICByZXR1cm4gKFxuICAgICAgPFVzZVNpZ25hbFxuICAgICAgICBzaWduYWw9e3Byb3BzLmh0bWxEb2N1bWVudC50cnVzdGVkQ2hhbmdlZH1cbiAgICAgICAgaW5pdGlhbFNlbmRlcj17cHJvcHMuaHRtbERvY3VtZW50fVxuICAgICAgPlxuICAgICAgICB7KCkgPT4gKFxuICAgICAgICAgIDxUb29sYmFyQnV0dG9uQ29tcG9uZW50XG4gICAgICAgICAgICBjbGFzc05hbWU9XCJcIlxuICAgICAgICAgICAgb25DbGljaz17KCkgPT5cbiAgICAgICAgICAgICAgKHByb3BzLmh0bWxEb2N1bWVudC50cnVzdGVkID0gIXByb3BzLmh0bWxEb2N1bWVudC50cnVzdGVkKVxuICAgICAgICAgICAgfVxuICAgICAgICAgICAgdG9vbHRpcD17dHJhbnMuX18oYFdoZXRoZXIgdGhlIEhUTUwgZmlsZSBpcyB0cnVzdGVkLlxuVHJ1c3RpbmcgdGhlIGZpbGUgYWxsb3dzIHNjcmlwdHMgdG8gcnVuIGluIGl0LFxud2hpY2ggbWF5IHJlc3VsdCBpbiBzZWN1cml0eSByaXNrcy5cbk9ubHkgZW5hYmxlIGZvciBmaWxlcyB5b3UgdHJ1c3QuYCl9XG4gICAgICAgICAgICBsYWJlbD17XG4gICAgICAgICAgICAgIHByb3BzLmh0bWxEb2N1bWVudC50cnVzdGVkXG4gICAgICAgICAgICAgICAgPyB0cmFucy5fXygnRGlzdHJ1c3QgSFRNTCcpXG4gICAgICAgICAgICAgICAgOiB0cmFucy5fXygnVHJ1c3QgSFRNTCcpXG4gICAgICAgICAgICB9XG4gICAgICAgICAgLz5cbiAgICAgICAgKX1cbiAgICAgIDwvVXNlU2lnbmFsPlxuICAgICk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==