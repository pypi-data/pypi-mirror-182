"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_markdownviewer_lib_index_js"],{

/***/ "../../packages/markdownviewer/lib/index.js":
/*!**************************************************!*\
  !*** ../../packages/markdownviewer/lib/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IMarkdownViewerTracker": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_1__.IMarkdownViewerTracker),
/* harmony export */   "MarkdownDocument": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_2__.MarkdownDocument),
/* harmony export */   "MarkdownViewer": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_2__.MarkdownViewer),
/* harmony export */   "MarkdownViewerFactory": () => (/* reexport safe */ _widget__WEBPACK_IMPORTED_MODULE_2__.MarkdownViewerFactory),
/* harmony export */   "MarkdownViewerTableOfContentsFactory": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_0__.MarkdownViewerTableOfContentsFactory),
/* harmony export */   "MarkdownViewerTableOfContentsModel": () => (/* reexport safe */ _toc__WEBPACK_IMPORTED_MODULE_0__.MarkdownViewerTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./toc */ "../../packages/markdownviewer/lib/toc.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tokens */ "../../packages/markdownviewer/lib/tokens.js");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widget */ "../../packages/markdownviewer/lib/widget.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module markdownviewer
 */





/***/ }),

/***/ "../../packages/markdownviewer/lib/toc.js":
/*!************************************************!*\
  !*** ../../packages/markdownviewer/lib/toc.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MarkdownViewerTableOfContentsFactory": () => (/* binding */ MarkdownViewerTableOfContentsFactory),
/* harmony export */   "MarkdownViewerTableOfContentsModel": () => (/* binding */ MarkdownViewerTableOfContentsModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Table of content model for Markdown viewer files.
 */
class MarkdownViewerTableOfContentsModel extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsModel {
    /**
     * Constructor
     *
     * @param widget The widget to search in
     * @param parser Markdown parser
     * @param configuration Default model configuration
     */
    constructor(widget, parser, configuration) {
        super(widget, configuration);
        this.parser = parser;
    }
    /**
     * Type of document supported by the model.
     *
     * #### Notes
     * A `data-document-type` attribute with this value will be set
     * on the tree view `.jp-TableOfContents-content[data-document-type="..."]`
     */
    get documentType() {
        return 'markdown-viewer';
    }
    /**
     * Whether the model gets updated even if the table of contents panel
     * is hidden or not.
     */
    get isAlwaysActive() {
        return true;
    }
    /**
     * List of configuration options supported by the model.
     */
    get supportedOptions() {
        return ['maximalDepth', 'numberingH1', 'numberHeaders'];
    }
    /**
     * Produce the headings for a document.
     *
     * @returns The list of new headings or `null` if nothing needs to be updated.
     */
    getHeadings() {
        const content = this.widget.context.model.toString();
        const headings = _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.Markdown.getHeadings(content, Object.assign(Object.assign({}, this.configuration), { 
            // Force base number to be equal to 1
            baseNumbering: 1 }));
        return Promise.resolve(headings);
    }
}
/**
 * Table of content model factory for Markdown viewer files.
 */
class MarkdownViewerTableOfContentsFactory extends _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsFactory {
    /**
     * Constructor
     *
     * @param tracker Widget tracker
     * @param parser Markdown parser
     */
    constructor(tracker, parser) {
        super(tracker);
        this.parser = parser;
    }
    /**
     * Create a new table of contents model for the widget
     *
     * @param widget - widget
     * @param configuration - Table of contents configuration
     * @returns The table of contents model
     */
    _createNew(widget, configuration) {
        const model = new MarkdownViewerTableOfContentsModel(widget, this.parser, configuration);
        let headingToElement = new WeakMap();
        const onActiveHeadingChanged = (model, heading) => {
            if (heading) {
                const el = headingToElement.get(heading);
                if (el) {
                    const widgetBox = widget.content.node.getBoundingClientRect();
                    const elementBox = el.getBoundingClientRect();
                    if (elementBox.top > widgetBox.bottom ||
                        elementBox.bottom < widgetBox.top ||
                        elementBox.left > widgetBox.right ||
                        elementBox.right < widgetBox.left) {
                        el.scrollIntoView({ inline: 'center' });
                    }
                }
            }
        };
        const onHeadingsChanged = () => {
            if (!this.parser) {
                return;
            }
            // Clear all numbering items
            _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.clearNumbering(widget.content.node);
            // Create a new mapping
            headingToElement = new WeakMap();
            model.headings.forEach(async (heading) => {
                var _a;
                const elementId = await _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.Markdown.getHeadingId(this.parser, heading.raw, heading.level);
                if (!elementId) {
                    return;
                }
                const selector = `h${heading.level}[id="${elementId}"]`;
                headingToElement.set(heading, _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_0__.TableOfContentsUtils.addPrefix(widget.content.node, selector, (_a = heading.prefix) !== null && _a !== void 0 ? _a : ''));
            });
        };
        void widget.content.ready.then(() => {
            onHeadingsChanged();
            widget.content.rendered.connect(onHeadingsChanged);
            model.activeHeadingChanged.connect(onActiveHeadingChanged);
            model.headingsChanged.connect(onHeadingsChanged);
            widget.disposed.connect(() => {
                widget.content.rendered.disconnect(onHeadingsChanged);
                model.activeHeadingChanged.disconnect(onActiveHeadingChanged);
                model.headingsChanged.disconnect(onHeadingsChanged);
            });
        });
        return model;
    }
}


/***/ }),

/***/ "../../packages/markdownviewer/lib/tokens.js":
/*!***************************************************!*\
  !*** ../../packages/markdownviewer/lib/tokens.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "IMarkdownViewerTracker": () => (/* binding */ IMarkdownViewerTracker)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The markdownviewer tracker token.
 */
const IMarkdownViewerTracker = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/markdownviewer:IMarkdownViewerTracker');


/***/ }),

/***/ "../../packages/markdownviewer/lib/widget.js":
/*!***************************************************!*\
  !*** ../../packages/markdownviewer/lib/widget.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MarkdownDocument": () => (/* binding */ MarkdownDocument),
/* harmony export */   "MarkdownViewer": () => (/* binding */ MarkdownViewer),
/* harmony export */   "MarkdownViewerFactory": () => (/* binding */ MarkdownViewerFactory)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.








/**
 * The class name added to a markdown viewer.
 */
const MARKDOWNVIEWER_CLASS = 'jp-MarkdownViewer';
/**
 * The markdown MIME type.
 */
const MIMETYPE = 'text/markdown';
/**
 * A widget for markdown documents.
 */
class MarkdownViewer extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_7__.Widget {
    /**
     * Construct a new markdown viewer widget.
     */
    constructor(options) {
        super();
        this._config = Object.assign({}, MarkdownViewer.defaultConfig);
        this._fragment = '';
        this._ready = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_5__.PromiseDelegate();
        this._isRendering = false;
        this._renderRequested = false;
        this._rendered = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_6__.Signal(this);
        this.context = options.context;
        this.translator = options.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.nullTranslator;
        this._trans = this.translator.load('jupyterlab');
        this.renderer = options.renderer;
        this.node.tabIndex = 0;
        this.addClass(MARKDOWNVIEWER_CLASS);
        const layout = (this.layout = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_7__.StackedLayout());
        layout.addWidget(this.renderer);
        void this.context.ready.then(async () => {
            await this._render();
            // Throttle the rendering rate of the widget.
            this._monitor = new _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_1__.ActivityMonitor({
                signal: this.context.model.contentChanged,
                timeout: this._config.renderTimeout
            });
            this._monitor.activityStopped.connect(this.update, this);
            this._ready.resolve(undefined);
        });
    }
    /**
     * A promise that resolves when the markdown viewer is ready.
     */
    get ready() {
        return this._ready.promise;
    }
    /**
     * Signal emitted when the content has been rendered.
     */
    get rendered() {
        return this._rendered;
    }
    /**
     * Set URI fragment identifier.
     */
    setFragment(fragment) {
        this._fragment = fragment;
        this.update();
    }
    /**
     * Set a config option for the markdown viewer.
     */
    setOption(option, value) {
        if (this._config[option] === value) {
            return;
        }
        this._config[option] = value;
        const { style } = this.renderer.node;
        switch (option) {
            case 'fontFamily':
                style.setProperty('font-family', value);
                break;
            case 'fontSize':
                style.setProperty('font-size', value ? value + 'px' : null);
                break;
            case 'hideFrontMatter':
                this.update();
                break;
            case 'lineHeight':
                style.setProperty('line-height', value ? value.toString() : null);
                break;
            case 'lineWidth': {
                const padding = value ? `calc(50% - ${value / 2}ch)` : null;
                style.setProperty('padding-left', padding);
                style.setProperty('padding-right', padding);
                break;
            }
            case 'renderTimeout':
                if (this._monitor) {
                    this._monitor.timeout = value;
                }
                break;
            default:
                break;
        }
    }
    /**
     * Dispose of the resources held by the widget.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        if (this._monitor) {
            this._monitor.dispose();
        }
        this._monitor = null;
        super.dispose();
    }
    /**
     * Handle an `update-request` message to the widget.
     */
    onUpdateRequest(msg) {
        if (this.context.isReady && !this.isDisposed) {
            void this._render();
            this._fragment = '';
        }
    }
    /**
     * Handle `'activate-request'` messages.
     */
    onActivateRequest(msg) {
        this.node.focus();
    }
    /**
     * Render the mime content.
     */
    async _render() {
        if (this.isDisposed) {
            return;
        }
        // Since rendering is async, we note render requests that happen while we
        // actually are rendering for a future rendering.
        if (this._isRendering) {
            this._renderRequested = true;
            return;
        }
        // Set up for this rendering pass.
        this._renderRequested = false;
        const { context } = this;
        const { model } = context;
        const source = model.toString();
        const data = {};
        // If `hideFrontMatter`is true remove front matter.
        data[MIMETYPE] = this._config.hideFrontMatter
            ? Private.removeFrontMatter(source)
            : source;
        const mimeModel = new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_3__.MimeModel({
            data,
            metadata: { fragment: this._fragment }
        });
        try {
            // Do the rendering asynchronously.
            this._isRendering = true;
            await this.renderer.renderModel(mimeModel);
            this._isRendering = false;
            // If there is an outstanding request to render, go ahead and render
            if (this._renderRequested) {
                return this._render();
            }
            else {
                this._rendered.emit();
            }
        }
        catch (reason) {
            // Dispose the document if rendering fails.
            requestAnimationFrame(() => {
                this.dispose();
            });
            void (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.showErrorMessage)(this._trans.__('Renderer Failure: %1', context.path), reason);
        }
    }
}
/**
 * The namespace for MarkdownViewer class statics.
 */
(function (MarkdownViewer) {
    /**
     * The default configuration options for an editor.
     */
    MarkdownViewer.defaultConfig = {
        fontFamily: null,
        fontSize: null,
        lineHeight: null,
        lineWidth: null,
        hideFrontMatter: true,
        renderTimeout: 1000
    };
})(MarkdownViewer || (MarkdownViewer = {}));
/**
 * A document widget for markdown content.
 */
class MarkdownDocument extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.DocumentWidget {
    setFragment(fragment) {
        this.content.setFragment(fragment);
    }
}
/**
 * A widget factory for markdown viewers.
 */
class MarkdownViewerFactory extends _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.ABCWidgetFactory {
    /**
     * Construct a new markdown viewer widget factory.
     */
    constructor(options) {
        super(Private.createRegistryOptions(options));
        this._fileType = options.primaryFileType;
        this._rendermime = options.rendermime;
    }
    /**
     * Create a new widget given a context.
     */
    createNewWidget(context) {
        var _a, _b, _c, _d, _e;
        const rendermime = this._rendermime.clone({
            resolver: context.urlResolver
        });
        const renderer = rendermime.createRenderer(MIMETYPE);
        const content = new MarkdownViewer({ context, renderer });
        content.title.icon = (_a = this._fileType) === null || _a === void 0 ? void 0 : _a.icon;
        content.title.iconClass = (_c = (_b = this._fileType) === null || _b === void 0 ? void 0 : _b.iconClass) !== null && _c !== void 0 ? _c : '';
        content.title.iconLabel = (_e = (_d = this._fileType) === null || _d === void 0 ? void 0 : _d.iconLabel) !== null && _e !== void 0 ? _e : '';
        const widget = new MarkdownDocument({ content, context });
        return widget;
    }
}
/**
 * A namespace for markdown viewer widget private data.
 */
var Private;
(function (Private) {
    /**
     * Create the document registry options.
     */
    function createRegistryOptions(options) {
        return Object.assign(Object.assign({}, options), { readOnly: true });
    }
    Private.createRegistryOptions = createRegistryOptions;
    /**
     * Remove YAML front matter from source.
     */
    function removeFrontMatter(source) {
        const re = /^---\n[^]*?\n(---|...)\n/;
        const match = source.match(re);
        if (!match) {
            return source;
        }
        const { length } = match[0];
        return source.slice(length);
    }
    Private.removeFrontMatter = removeFrontMatter;
})(Private || (Private = {}));


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWFya2Rvd252aWV3ZXJfbGliX2luZGV4X2pzLjlmM2Y1ZTgzZGU0OTI4NmQzMzM1LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBRW1CO0FBQ0c7QUFDQTs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDVHpCLDBDQUEwQztBQUMxQywyREFBMkQ7QUFTbEM7QUFTekI7O0dBRUc7QUFDSSxNQUFNLGtDQUFtQyxTQUFRLGlFQUd2RDtJQUNDOzs7Ozs7T0FNRztJQUNILFlBQ0UsTUFBd0IsRUFDZCxNQUE4QixFQUN4QyxhQUF1QztRQUV2QyxLQUFLLENBQUMsTUFBTSxFQUFFLGFBQWEsQ0FBQyxDQUFDO1FBSG5CLFdBQU0sR0FBTixNQUFNLENBQXdCO0lBSTFDLENBQUM7SUFFRDs7Ozs7O09BTUc7SUFDSCxJQUFJLFlBQVk7UUFDZCxPQUFPLGlCQUFpQixDQUFDO0lBQzNCLENBQUM7SUFFRDs7O09BR0c7SUFDSCxJQUFjLGNBQWM7UUFDMUIsT0FBTyxJQUFJLENBQUM7SUFDZCxDQUFDO0lBRUQ7O09BRUc7SUFDSCxJQUFJLGdCQUFnQjtRQUNsQixPQUFPLENBQUMsY0FBYyxFQUFFLGFBQWEsRUFBRSxlQUFlLENBQUMsQ0FBQztJQUMxRCxDQUFDO0lBRUQ7Ozs7T0FJRztJQUNPLFdBQVc7UUFDbkIsTUFBTSxPQUFPLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsS0FBSyxDQUFDLFFBQVEsRUFBRSxDQUFDO1FBQ3JELE1BQU0sUUFBUSxHQUFHLHNGQUF5QyxDQUFDLE9BQU8sa0NBQzdELElBQUksQ0FBQyxhQUFhO1lBQ3JCLHFDQUFxQztZQUNyQyxhQUFhLEVBQUUsQ0FBQyxJQUNoQixDQUFDO1FBQ0gsT0FBTyxPQUFPLENBQUMsT0FBTyxDQUFDLFFBQVEsQ0FBQyxDQUFDO0lBQ25DLENBQUM7Q0FDRjtBQUVEOztHQUVHO0FBQ0ksTUFBTSxvQ0FBcUMsU0FB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O0lBUmUseUJBQWlCLG9CQVFoQztBQUNILENBQUMsRUF6QlMsT0FBTyxLQUFQLE9BQU8sUUF5QmhCIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL21hcmtkb3dudmlld2VyL3NyYy9pbmRleC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFya2Rvd252aWV3ZXIvc3JjL3RvYy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFya2Rvd252aWV3ZXIvc3JjL3Rva2Vucy50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFya2Rvd252aWV3ZXIvc3JjL3dpZGdldC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBtYXJrZG93bnZpZXdlclxuICovXG5cbmV4cG9ydCAqIGZyb20gJy4vdG9jJztcbmV4cG9ydCAqIGZyb20gJy4vdG9rZW5zJztcbmV4cG9ydCAqIGZyb20gJy4vd2lkZ2V0JztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVdpZGdldFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJTWFya2Rvd25QYXJzZXIgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7XG4gIFRhYmxlT2ZDb250ZW50cyxcbiAgVGFibGVPZkNvbnRlbnRzRmFjdG9yeSxcbiAgVGFibGVPZkNvbnRlbnRzTW9kZWwsXG4gIFRhYmxlT2ZDb250ZW50c1V0aWxzXG59IGZyb20gJ0BqdXB5dGVybGFiL3RvYyc7XG5pbXBvcnQgeyBNYXJrZG93bkRvY3VtZW50IH0gZnJvbSAnLi93aWRnZXQnO1xuXG4vKipcbiAqIEludGVyZmFjZSBkZXNjcmliaW5nIGEgTWFya2Rvd24gdmlld2VyIGhlYWRpbmcuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSU1hcmtkb3duVmlld2VySGVhZGluZ1xuICBleHRlbmRzIFRhYmxlT2ZDb250ZW50c1V0aWxzLk1hcmtkb3duLklNYXJrZG93bkhlYWRpbmcge31cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50IG1vZGVsIGZvciBNYXJrZG93biB2aWV3ZXIgZmlsZXMuXG4gKi9cbmV4cG9ydCBjbGFzcyBNYXJrZG93blZpZXdlclRhYmxlT2ZDb250ZW50c01vZGVsIGV4dGVuZHMgVGFibGVPZkNvbnRlbnRzTW9kZWw8XG4gIElNYXJrZG93blZpZXdlckhlYWRpbmcsXG4gIE1hcmtkb3duRG9jdW1lbnRcbj4ge1xuICAvKipcbiAgICogQ29uc3RydWN0b3JcbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCBUaGUgd2lkZ2V0IHRvIHNlYXJjaCBpblxuICAgKiBAcGFyYW0gcGFyc2VyIE1hcmtkb3duIHBhcnNlclxuICAgKiBAcGFyYW0gY29uZmlndXJhdGlvbiBEZWZhdWx0IG1vZGVsIGNvbmZpZ3VyYXRpb25cbiAgICovXG4gIGNvbnN0cnVjdG9yKFxuICAgIHdpZGdldDogTWFya2Rvd25Eb2N1bWVudCxcbiAgICBwcm90ZWN0ZWQgcGFyc2VyOiBJTWFya2Rvd25QYXJzZXIgfCBudWxsLFxuICAgIGNvbmZpZ3VyYXRpb24/OiBUYWJsZU9mQ29udGVudHMuSUNvbmZpZ1xuICApIHtcbiAgICBzdXBlcih3aWRnZXQsIGNvbmZpZ3VyYXRpb24pO1xuICB9XG5cbiAgLyoqXG4gICAqIFR5cGUgb2YgZG9jdW1lbnQgc3VwcG9ydGVkIGJ5IHRoZSBtb2RlbC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBBIGBkYXRhLWRvY3VtZW50LXR5cGVgIGF0dHJpYnV0ZSB3aXRoIHRoaXMgdmFsdWUgd2lsbCBiZSBzZXRcbiAgICogb24gdGhlIHRyZWUgdmlldyBgLmpwLVRhYmxlT2ZDb250ZW50cy1jb250ZW50W2RhdGEtZG9jdW1lbnQtdHlwZT1cIi4uLlwiXWBcbiAgICovXG4gIGdldCBkb2N1bWVudFR5cGUoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gJ21hcmtkb3duLXZpZXdlcic7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgbW9kZWwgZ2V0cyB1cGRhdGVkIGV2ZW4gaWYgdGhlIHRhYmxlIG9mIGNvbnRlbnRzIHBhbmVsXG4gICAqIGlzIGhpZGRlbiBvciBub3QuXG4gICAqL1xuICBwcm90ZWN0ZWQgZ2V0IGlzQWx3YXlzQWN0aXZlKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0cnVlO1xuICB9XG5cbiAgLyoqXG4gICAqIExpc3Qgb2YgY29uZmlndXJhdGlvbiBvcHRpb25zIHN1cHBvcnRlZCBieSB0aGUgbW9kZWwuXG4gICAqL1xuICBnZXQgc3VwcG9ydGVkT3B0aW9ucygpOiAoa2V5b2YgVGFibGVPZkNvbnRlbnRzLklDb25maWcpW10ge1xuICAgIHJldHVybiBbJ21heGltYWxEZXB0aCcsICdudW1iZXJpbmdIMScsICdudW1iZXJIZWFkZXJzJ107XG4gIH1cblxuICAvKipcbiAgICogUHJvZHVjZSB0aGUgaGVhZGluZ3MgZm9yIGEgZG9jdW1lbnQuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBsaXN0IG9mIG5ldyBoZWFkaW5ncyBvciBgbnVsbGAgaWYgbm90aGluZyBuZWVkcyB0byBiZSB1cGRhdGVkLlxuICAgKi9cbiAgcHJvdGVjdGVkIGdldEhlYWRpbmdzKCk6IFByb21pc2U8SU1hcmtkb3duVmlld2VySGVhZGluZ1tdIHwgbnVsbD4ge1xuICAgIGNvbnN0IGNvbnRlbnQgPSB0aGlzLndpZGdldC5jb250ZXh0Lm1vZGVsLnRvU3RyaW5nKCk7XG4gICAgY29uc3QgaGVhZGluZ3MgPSBUYWJsZU9mQ29udGVudHNVdGlscy5NYXJrZG93bi5nZXRIZWFkaW5ncyhjb250ZW50LCB7XG4gICAgICAuLi50aGlzLmNvbmZpZ3VyYXRpb24sXG4gICAgICAvLyBGb3JjZSBiYXNlIG51bWJlciB0byBiZSBlcXVhbCB0byAxXG4gICAgICBiYXNlTnVtYmVyaW5nOiAxXG4gICAgfSk7XG4gICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShoZWFkaW5ncyk7XG4gIH1cbn1cblxuLyoqXG4gKiBUYWJsZSBvZiBjb250ZW50IG1vZGVsIGZhY3RvcnkgZm9yIE1hcmtkb3duIHZpZXdlciBmaWxlcy5cbiAqL1xuZXhwb3J0IGNsYXNzIE1hcmtkb3duVmlld2VyVGFibGVPZkNvbnRlbnRzRmFjdG9yeSBleHRlbmRzIFRhYmxlT2ZDb250ZW50c0ZhY3Rvcnk8TWFya2Rvd25Eb2N1bWVudD4ge1xuICAvKipcbiAgICogQ29uc3RydWN0b3JcbiAgICpcbiAgICogQHBhcmFtIHRyYWNrZXIgV2lkZ2V0IHRyYWNrZXJcbiAgICogQHBhcmFtIHBhcnNlciBNYXJrZG93biBwYXJzZXJcbiAgICovXG4gIGNvbnN0cnVjdG9yKFxuICAgIHRyYWNrZXI6IElXaWRnZXRUcmFja2VyPE1hcmtkb3duRG9jdW1lbnQ+LFxuICAgIHByb3RlY3RlZCBwYXJzZXI6IElNYXJrZG93blBhcnNlciB8IG51bGxcbiAgKSB7XG4gICAgc3VwZXIodHJhY2tlcik7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgbmV3IHRhYmxlIG9mIGNvbnRlbnRzIG1vZGVsIGZvciB0aGUgd2lkZ2V0XG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSB3aWRnZXRcbiAgICogQHBhcmFtIGNvbmZpZ3VyYXRpb24gLSBUYWJsZSBvZiBjb250ZW50cyBjb25maWd1cmF0aW9uXG4gICAqIEByZXR1cm5zIFRoZSB0YWJsZSBvZiBjb250ZW50cyBtb2RlbFxuICAgKi9cbiAgcHJvdGVjdGVkIF9jcmVhdGVOZXcoXG4gICAgd2lkZ2V0OiBNYXJrZG93bkRvY3VtZW50LFxuICAgIGNvbmZpZ3VyYXRpb24/OiBUYWJsZU9mQ29udGVudHMuSUNvbmZpZ1xuICApOiBUYWJsZU9mQ29udGVudHNNb2RlbDxUYWJsZU9mQ29udGVudHMuSUhlYWRpbmcsIE1hcmtkb3duRG9jdW1lbnQ+IHtcbiAgICBjb25zdCBtb2RlbCA9IG5ldyBNYXJrZG93blZpZXdlclRhYmxlT2ZDb250ZW50c01vZGVsKFxuICAgICAgd2lkZ2V0LFxuICAgICAgdGhpcy5wYXJzZXIsXG4gICAgICBjb25maWd1cmF0aW9uXG4gICAgKTtcblxuICAgIGxldCBoZWFkaW5nVG9FbGVtZW50ID0gbmV3IFdlYWtNYXA8XG4gICAgICBJTWFya2Rvd25WaWV3ZXJIZWFkaW5nLFxuICAgICAgRWxlbWVudCB8IG51bGxcbiAgICA+KCk7XG5cbiAgICBjb25zdCBvbkFjdGl2ZUhlYWRpbmdDaGFuZ2VkID0gKFxuICAgICAgbW9kZWw6IFRhYmxlT2ZDb250ZW50c01vZGVsPElNYXJrZG93blZpZXdlckhlYWRpbmcsIE1hcmtkb3duRG9jdW1lbnQ+LFxuICAgICAgaGVhZGluZzogSU1hcmtkb3duVmlld2VySGVhZGluZyB8IG51bGxcbiAgICApID0+IHtcbiAgICAgIGlmIChoZWFkaW5nKSB7XG4gICAgICAgIGNvbnN0IGVsID0gaGVhZGluZ1RvRWxlbWVudC5nZXQoaGVhZGluZyk7XG5cbiAgICAgICAgaWYgKGVsKSB7XG4gICAgICAgICAgY29uc3Qgd2lkZ2V0Qm94ID0gd2lkZ2V0LmNvbnRlbnQubm9kZS5nZXRCb3VuZGluZ0NsaWVudFJlY3QoKTtcbiAgICAgICAgICBjb25zdCBlbGVtZW50Qm94ID0gZWwuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCk7XG5cbiAgICAgICAgICBpZiAoXG4gICAgICAgICAgICBlbGVtZW50Qm94LnRvcCA+IHdpZGdldEJveC5ib3R0b20gfHxcbiAgICAgICAgICAgIGVsZW1lbnRCb3guYm90dG9tIDwgd2lkZ2V0Qm94LnRvcCB8fFxuICAgICAgICAgICAgZWxlbWVudEJveC5sZWZ0ID4gd2lkZ2V0Qm94LnJpZ2h0IHx8XG4gICAgICAgICAgICBlbGVtZW50Qm94LnJpZ2h0IDwgd2lkZ2V0Qm94LmxlZnRcbiAgICAgICAgICApIHtcbiAgICAgICAgICAgIGVsLnNjcm9sbEludG9WaWV3KHsgaW5saW5lOiAnY2VudGVyJyB9KTtcbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9O1xuXG4gICAgY29uc3Qgb25IZWFkaW5nc0NoYW5nZWQgPSAoKSA9PiB7XG4gICAgICBpZiAoIXRoaXMucGFyc2VyKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cblxuICAgICAgLy8gQ2xlYXIgYWxsIG51bWJlcmluZyBpdGVtc1xuICAgICAgVGFibGVPZkNvbnRlbnRzVXRpbHMuY2xlYXJOdW1iZXJpbmcod2lkZ2V0LmNvbnRlbnQubm9kZSk7XG5cbiAgICAgIC8vIENyZWF0ZSBhIG5ldyBtYXBwaW5nXG4gICAgICBoZWFkaW5nVG9FbGVtZW50ID0gbmV3IFdlYWtNYXA8SU1hcmtkb3duVmlld2VySGVhZGluZywgRWxlbWVudCB8IG51bGw+KCk7XG4gICAgICBtb2RlbC5oZWFkaW5ncy5mb3JFYWNoKGFzeW5jIGhlYWRpbmcgPT4ge1xuICAgICAgICBjb25zdCBlbGVtZW50SWQgPSBhd2FpdCBUYWJsZU9mQ29udGVudHNVdGlscy5NYXJrZG93bi5nZXRIZWFkaW5nSWQoXG4gICAgICAgICAgdGhpcy5wYXJzZXIhLFxuICAgICAgICAgIGhlYWRpbmcucmF3LFxuICAgICAgICAgIGhlYWRpbmcubGV2ZWxcbiAgICAgICAgKTtcblxuICAgICAgICBpZiAoIWVsZW1lbnRJZCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICBjb25zdCBzZWxlY3RvciA9IGBoJHtoZWFkaW5nLmxldmVsfVtpZD1cIiR7ZWxlbWVudElkfVwiXWA7XG5cbiAgICAgICAgaGVhZGluZ1RvRWxlbWVudC5zZXQoXG4gICAgICAgICAgaGVhZGluZyxcbiAgICAgICAgICBUYWJsZU9mQ29udGVudHNVdGlscy5hZGRQcmVmaXgoXG4gICAgICAgICAgICB3aWRnZXQuY29udGVudC5ub2RlLFxuICAgICAgICAgICAgc2VsZWN0b3IsXG4gICAgICAgICAgICBoZWFkaW5nLnByZWZpeCA/PyAnJ1xuICAgICAgICAgIClcbiAgICAgICAgKTtcbiAgICAgIH0pO1xuICAgIH07XG5cbiAgICB2b2lkIHdpZGdldC5jb250ZW50LnJlYWR5LnRoZW4oKCkgPT4ge1xuICAgICAgb25IZWFkaW5nc0NoYW5nZWQoKTtcblxuICAgICAgd2lkZ2V0LmNvbnRlbnQucmVuZGVyZWQuY29ubmVjdChvbkhlYWRpbmdzQ2hhbmdlZCk7XG4gICAgICBtb2RlbC5hY3RpdmVIZWFkaW5nQ2hhbmdlZC5jb25uZWN0KG9uQWN0aXZlSGVhZGluZ0NoYW5nZWQpO1xuICAgICAgbW9kZWwuaGVhZGluZ3NDaGFuZ2VkLmNvbm5lY3Qob25IZWFkaW5nc0NoYW5nZWQpO1xuICAgICAgd2lkZ2V0LmRpc3Bvc2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICB3aWRnZXQuY29udGVudC5yZW5kZXJlZC5kaXNjb25uZWN0KG9uSGVhZGluZ3NDaGFuZ2VkKTtcbiAgICAgICAgbW9kZWwuYWN0aXZlSGVhZGluZ0NoYW5nZWQuZGlzY29ubmVjdChvbkFjdGl2ZUhlYWRpbmdDaGFuZ2VkKTtcbiAgICAgICAgbW9kZWwuaGVhZGluZ3NDaGFuZ2VkLmRpc2Nvbm5lY3Qob25IZWFkaW5nc0NoYW5nZWQpO1xuICAgICAgfSk7XG4gICAgfSk7XG5cbiAgICByZXR1cm4gbW9kZWw7XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVdpZGdldFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IE1hcmtkb3duRG9jdW1lbnQgfSBmcm9tICcuL3dpZGdldCc7XG5cbi8qKlxuICogVGhlIG1hcmtkb3dudmlld2VyIHRyYWNrZXIgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJTWFya2Rvd25WaWV3ZXJUcmFja2VyID0gbmV3IFRva2VuPElNYXJrZG93blZpZXdlclRyYWNrZXI+KFxuICAnQGp1cHl0ZXJsYWIvbWFya2Rvd252aWV3ZXI6SU1hcmtkb3duVmlld2VyVHJhY2tlcidcbik7XG5cbi8qKlxuICogQSBjbGFzcyB0aGF0IHRyYWNrcyBtYXJrZG93biB2aWV3ZXIgd2lkZ2V0cy5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJTWFya2Rvd25WaWV3ZXJUcmFja2VyXG4gIGV4dGVuZHMgSVdpZGdldFRyYWNrZXI8TWFya2Rvd25Eb2N1bWVudD4ge31cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgc2hvd0Vycm9yTWVzc2FnZSB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IEFjdGl2aXR5TW9uaXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL2NvcmV1dGlscyc7XG5pbXBvcnQge1xuICBBQkNXaWRnZXRGYWN0b3J5LFxuICBEb2N1bWVudFJlZ2lzdHJ5LFxuICBEb2N1bWVudFdpZGdldFxufSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQge1xuICBJUmVuZGVyTWltZSxcbiAgSVJlbmRlck1pbWVSZWdpc3RyeSxcbiAgTWltZU1vZGVsXG59IGZyb20gJ0BqdXB5dGVybGFiL3JlbmRlcm1pbWUnO1xuaW1wb3J0IHtcbiAgSVRyYW5zbGF0b3IsXG4gIG51bGxUcmFuc2xhdG9yLFxuICBUcmFuc2xhdGlvbkJ1bmRsZVxufSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBKU09OT2JqZWN0LCBQcm9taXNlRGVsZWdhdGUgfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBNZXNzYWdlIH0gZnJvbSAnQGx1bWluby9tZXNzYWdpbmcnO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgU3RhY2tlZExheW91dCwgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgY2xhc3MgbmFtZSBhZGRlZCB0byBhIG1hcmtkb3duIHZpZXdlci5cbiAqL1xuY29uc3QgTUFSS0RPV05WSUVXRVJfQ0xBU1MgPSAnanAtTWFya2Rvd25WaWV3ZXInO1xuXG4vKipcbiAqIFRoZSBtYXJrZG93biBNSU1FIHR5cGUuXG4gKi9cbmNvbnN0IE1JTUVUWVBFID0gJ3RleHQvbWFya2Rvd24nO1xuXG4vKipcbiAqIEEgd2lkZ2V0IGZvciBtYXJrZG93biBkb2N1bWVudHMuXG4gKi9cbmV4cG9ydCBjbGFzcyBNYXJrZG93blZpZXdlciBleHRlbmRzIFdpZGdldCB7XG4gIC8qKlxuICAgKiBDb25zdHJ1Y3QgYSBuZXcgbWFya2Rvd24gdmlld2VyIHdpZGdldC5cbiAgICovXG4gIGNvbnN0cnVjdG9yKG9wdGlvbnM6IE1hcmtkb3duVmlld2VyLklPcHRpb25zKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLmNvbnRleHQgPSBvcHRpb25zLmNvbnRleHQ7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gb3B0aW9ucy50cmFuc2xhdG9yIHx8IG51bGxUcmFuc2xhdG9yO1xuICAgIHRoaXMuX3RyYW5zID0gdGhpcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICB0aGlzLnJlbmRlcmVyID0gb3B0aW9ucy5yZW5kZXJlcjtcbiAgICB0aGlzLm5vZGUudGFiSW5kZXggPSAwO1xuICAgIHRoaXMuYWRkQ2xhc3MoTUFSS0RPV05WSUVXRVJfQ0xBU1MpO1xuXG4gICAgY29uc3QgbGF5b3V0ID0gKHRoaXMubGF5b3V0ID0gbmV3IFN0YWNrZWRMYXlvdXQoKSk7XG4gICAgbGF5b3V0LmFkZFdpZGdldCh0aGlzLnJlbmRlcmVyKTtcblxuICAgIHZvaWQgdGhpcy5jb250ZXh0LnJlYWR5LnRoZW4oYXN5bmMgKCkgPT4ge1xuICAgICAgYXdhaXQgdGhpcy5fcmVuZGVyKCk7XG5cbiAgICAgIC8vIFRocm90dGxlIHRoZSByZW5kZXJpbmcgcmF0ZSBvZiB0aGUgd2lkZ2V0LlxuICAgICAgdGhpcy5fbW9uaXRvciA9IG5ldyBBY3Rpdml0eU1vbml0b3Ioe1xuICAgICAgICBzaWduYWw6IHRoaXMuY29udGV4dC5tb2RlbC5jb250ZW50Q2hhbmdlZCxcbiAgICAgICAgdGltZW91dDogdGhpcy5fY29uZmlnLnJlbmRlclRpbWVvdXRcbiAgICAgIH0pO1xuICAgICAgdGhpcy5fbW9uaXRvci5hY3Rpdml0eVN0b3BwZWQuY29ubmVjdCh0aGlzLnVwZGF0ZSwgdGhpcyk7XG5cbiAgICAgIHRoaXMuX3JlYWR5LnJlc29sdmUodW5kZWZpbmVkKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBtYXJrZG93biB2aWV3ZXIgaXMgcmVhZHkuXG4gICAqL1xuICBnZXQgcmVhZHkoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX3JlYWR5LnByb21pc2U7XG4gIH1cblxuICAvKipcbiAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgY29udGVudCBoYXMgYmVlbiByZW5kZXJlZC5cbiAgICovXG4gIGdldCByZW5kZXJlZCgpOiBJU2lnbmFsPE1hcmtkb3duVmlld2VyLCB2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX3JlbmRlcmVkO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCBVUkkgZnJhZ21lbnQgaWRlbnRpZmllci5cbiAgICovXG4gIHNldEZyYWdtZW50KGZyYWdtZW50OiBzdHJpbmcpOiB2b2lkIHtcbiAgICB0aGlzLl9mcmFnbWVudCA9IGZyYWdtZW50O1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICAvKipcbiAgICogU2V0IGEgY29uZmlnIG9wdGlvbiBmb3IgdGhlIG1hcmtkb3duIHZpZXdlci5cbiAgICovXG4gIHNldE9wdGlvbjxLIGV4dGVuZHMga2V5b2YgTWFya2Rvd25WaWV3ZXIuSUNvbmZpZz4oXG4gICAgb3B0aW9uOiBLLFxuICAgIHZhbHVlOiBNYXJrZG93blZpZXdlci5JQ29uZmlnW0tdXG4gICk6IHZvaWQge1xuICAgIGlmICh0aGlzLl9jb25maWdbb3B0aW9uXSA9PT0gdmFsdWUpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gICAgdGhpcy5fY29uZmlnW29wdGlvbl0gPSB2YWx1ZTtcbiAgICBjb25zdCB7IHN0eWxlIH0gPSB0aGlzLnJlbmRlcmVyLm5vZGU7XG4gICAgc3dpdGNoIChvcHRpb24pIHtcbiAgICAgIGNhc2UgJ2ZvbnRGYW1pbHknOlxuICAgICAgICBzdHlsZS5zZXRQcm9wZXJ0eSgnZm9udC1mYW1pbHknLCB2YWx1ZSBhcyBzdHJpbmcgfCBudWxsKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICBjYXNlICdmb250U2l6ZSc6XG4gICAgICAgIHN0eWxlLnNldFByb3BlcnR5KCdmb250LXNpemUnLCB2YWx1ZSA/IHZhbHVlICsgJ3B4JyA6IG51bGwpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2hpZGVGcm9udE1hdHRlcic6XG4gICAgICAgIHRoaXMudXBkYXRlKCk7XG4gICAgICAgIGJyZWFrO1xuICAgICAgY2FzZSAnbGluZUhlaWdodCc6XG4gICAgICAgIHN0eWxlLnNldFByb3BlcnR5KCdsaW5lLWhlaWdodCcsIHZhbHVlID8gdmFsdWUudG9TdHJpbmcoKSA6IG51bGwpO1xuICAgICAgICBicmVhaztcbiAgICAgIGNhc2UgJ2xpbmVXaWR0aCc6IHtcbiAgICAgICAgY29uc3QgcGFkZGluZyA9IHZhbHVlID8gYGNhbGMoNTAlIC0gJHsodmFsdWUgYXMgbnVtYmVyKSAvIDJ9Y2gpYCA6IG51bGw7XG4gICAgICAgIHN0eWxlLnNldFByb3BlcnR5KCdwYWRkaW5nLWxlZnQnLCBwYWRkaW5nKTtcbiAgICAgICAgc3R5bGUuc2V0UHJvcGVydHkoJ3BhZGRpbmctcmlnaHQnLCBwYWRkaW5nKTtcbiAgICAgICAgYnJlYWs7XG4gICAgICB9XG4gICAgICBjYXNlICdyZW5kZXJUaW1lb3V0JzpcbiAgICAgICAgaWYgKHRoaXMuX21vbml0b3IpIHtcbiAgICAgICAgICB0aGlzLl9tb25pdG9yLnRpbWVvdXQgPSB2YWx1ZSBhcyBudW1iZXI7XG4gICAgICAgIH1cbiAgICAgICAgYnJlYWs7XG4gICAgICBkZWZhdWx0OlxuICAgICAgICBicmVhaztcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIHdpZGdldC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBpZiAodGhpcy5fbW9uaXRvcikge1xuICAgICAgdGhpcy5fbW9uaXRvci5kaXNwb3NlKCk7XG4gICAgfVxuICAgIHRoaXMuX21vbml0b3IgPSBudWxsO1xuICAgIHN1cGVyLmRpc3Bvc2UoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgYW4gYHVwZGF0ZS1yZXF1ZXN0YCBtZXNzYWdlIHRvIHRoZSB3aWRnZXQuXG4gICAqL1xuICBwcm90ZWN0ZWQgb25VcGRhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIGlmICh0aGlzLmNvbnRleHQuaXNSZWFkeSAmJiAhdGhpcy5pc0Rpc3Bvc2VkKSB7XG4gICAgICB2b2lkIHRoaXMuX3JlbmRlcigpO1xuICAgICAgdGhpcy5fZnJhZ21lbnQgPSAnJztcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGAnYWN0aXZhdGUtcmVxdWVzdCdgIG1lc3NhZ2VzLlxuICAgKi9cbiAgcHJvdGVjdGVkIG9uQWN0aXZhdGVSZXF1ZXN0KG1zZzogTWVzc2FnZSk6IHZvaWQge1xuICAgIHRoaXMubm9kZS5mb2N1cygpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbmRlciB0aGUgbWltZSBjb250ZW50LlxuICAgKi9cbiAgcHJpdmF0ZSBhc3luYyBfcmVuZGVyKCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGlmICh0aGlzLmlzRGlzcG9zZWQpIHtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBTaW5jZSByZW5kZXJpbmcgaXMgYXN5bmMsIHdlIG5vdGUgcmVuZGVyIHJlcXVlc3RzIHRoYXQgaGFwcGVuIHdoaWxlIHdlXG4gICAgLy8gYWN0dWFsbHkgYXJlIHJlbmRlcmluZyBmb3IgYSBmdXR1cmUgcmVuZGVyaW5nLlxuICAgIGlmICh0aGlzLl9pc1JlbmRlcmluZykge1xuICAgICAgdGhpcy5fcmVuZGVyUmVxdWVzdGVkID0gdHJ1ZTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICAvLyBTZXQgdXAgZm9yIHRoaXMgcmVuZGVyaW5nIHBhc3MuXG4gICAgdGhpcy5fcmVuZGVyUmVxdWVzdGVkID0gZmFsc2U7XG4gICAgY29uc3QgeyBjb250ZXh0IH0gPSB0aGlzO1xuICAgIGNvbnN0IHsgbW9kZWwgfSA9IGNvbnRleHQ7XG4gICAgY29uc3Qgc291cmNlID0gbW9kZWwudG9TdHJpbmcoKTtcbiAgICBjb25zdCBkYXRhOiBKU09OT2JqZWN0ID0ge307XG4gICAgLy8gSWYgYGhpZGVGcm9udE1hdHRlcmBpcyB0cnVlIHJlbW92ZSBmcm9udCBtYXR0ZXIuXG4gICAgZGF0YVtNSU1FVFlQRV0gPSB0aGlzLl9jb25maWcuaGlkZUZyb250TWF0dGVyXG4gICAgICA/IFByaXZhdGUucmVtb3ZlRnJvbnRNYXR0ZXIoc291cmNlKVxuICAgICAgOiBzb3VyY2U7XG4gICAgY29uc3QgbWltZU1vZGVsID0gbmV3IE1pbWVNb2RlbCh7XG4gICAgICBkYXRhLFxuICAgICAgbWV0YWRhdGE6IHsgZnJhZ21lbnQ6IHRoaXMuX2ZyYWdtZW50IH1cbiAgICB9KTtcblxuICAgIHRyeSB7XG4gICAgICAvLyBEbyB0aGUgcmVuZGVyaW5nIGFzeW5jaHJvbm91c2x5LlxuICAgICAgdGhpcy5faXNSZW5kZXJpbmcgPSB0cnVlO1xuICAgICAgYXdhaXQgdGhpcy5yZW5kZXJlci5yZW5kZXJNb2RlbChtaW1lTW9kZWwpO1xuICAgICAgdGhpcy5faXNSZW5kZXJpbmcgPSBmYWxzZTtcblxuICAgICAgLy8gSWYgdGhlcmUgaXMgYW4gb3V0c3RhbmRpbmcgcmVxdWVzdCB0byByZW5kZXIsIGdvIGFoZWFkIGFuZCByZW5kZXJcbiAgICAgIGlmICh0aGlzLl9yZW5kZXJSZXF1ZXN0ZWQpIHtcbiAgICAgICAgcmV0dXJuIHRoaXMuX3JlbmRlcigpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgdGhpcy5fcmVuZGVyZWQuZW1pdCgpO1xuICAgICAgfVxuICAgIH0gY2F0Y2ggKHJlYXNvbikge1xuICAgICAgLy8gRGlzcG9zZSB0aGUgZG9jdW1lbnQgaWYgcmVuZGVyaW5nIGZhaWxzLlxuICAgICAgcmVxdWVzdEFuaW1hdGlvbkZyYW1lKCgpID0+IHtcbiAgICAgICAgdGhpcy5kaXNwb3NlKCk7XG4gICAgICB9KTtcbiAgICAgIHZvaWQgc2hvd0Vycm9yTWVzc2FnZShcbiAgICAgICAgdGhpcy5fdHJhbnMuX18oJ1JlbmRlcmVyIEZhaWx1cmU6ICUxJywgY29udGV4dC5wYXRoKSxcbiAgICAgICAgcmVhc29uXG4gICAgICApO1xuICAgIH1cbiAgfVxuXG4gIHJlYWRvbmx5IGNvbnRleHQ6IERvY3VtZW50UmVnaXN0cnkuQ29udGV4dDtcbiAgcmVhZG9ubHkgcmVuZGVyZXI6IElSZW5kZXJNaW1lLklSZW5kZXJlcjtcbiAgcHJvdGVjdGVkIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yO1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG4gIHByaXZhdGUgX2NvbmZpZyA9IHsgLi4uTWFya2Rvd25WaWV3ZXIuZGVmYXVsdENvbmZpZyB9O1xuICBwcml2YXRlIF9mcmFnbWVudCA9ICcnO1xuICBwcml2YXRlIF9tb25pdG9yOiBBY3Rpdml0eU1vbml0b3I8RG9jdW1lbnRSZWdpc3RyeS5JTW9kZWwsIHZvaWQ+IHwgbnVsbDtcbiAgcHJpdmF0ZSBfcmVhZHkgPSBuZXcgUHJvbWlzZURlbGVnYXRlPHZvaWQ+KCk7XG4gIHByaXZhdGUgX2lzUmVuZGVyaW5nID0gZmFsc2U7XG4gIHByaXZhdGUgX3JlbmRlclJlcXVlc3RlZCA9IGZhbHNlO1xuICBwcml2YXRlIF9yZW5kZXJlZCA9IG5ldyBTaWduYWw8TWFya2Rvd25WaWV3ZXIsIHZvaWQ+KHRoaXMpO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lc3BhY2UgZm9yIE1hcmtkb3duVmlld2VyIGNsYXNzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgTWFya2Rvd25WaWV3ZXIge1xuICAvKipcbiAgICogVGhlIG9wdGlvbnMgdXNlZCB0byBpbml0aWFsaXplIGEgTWFya2Rvd25WaWV3ZXIuXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBDb250ZXh0XG4gICAgICovXG4gICAgY29udGV4dDogRG9jdW1lbnRSZWdpc3RyeS5JQ29udGV4dDxEb2N1bWVudFJlZ2lzdHJ5LklNb2RlbD47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcmVuZGVyZXIgaW5zdGFuY2UuXG4gICAgICovXG4gICAgcmVuZGVyZXI6IElSZW5kZXJNaW1lLklSZW5kZXJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBhcHBsaWNhdGlvbiBsYW5ndWFnZSB0cmFuc2xhdG9yLlxuICAgICAqL1xuICAgIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgfVxuXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUNvbmZpZyB7XG4gICAgLyoqXG4gICAgICogVXNlciBwcmVmZXJyZWQgZm9udCBmYW1pbHkgZm9yIG1hcmtkb3duIHZpZXdlci5cbiAgICAgKi9cbiAgICBmb250RmFtaWx5OiBzdHJpbmcgfCBudWxsO1xuXG4gICAgLyoqXG4gICAgICogVXNlciBwcmVmZXJyZWQgc2l6ZSBpbiBwaXhlbCBvZiB0aGUgZm9udCB1c2VkIGluIG1hcmtkb3duIHZpZXdlci5cbiAgICAgKi9cbiAgICBmb250U2l6ZTogbnVtYmVyIHwgbnVsbDtcblxuICAgIC8qKlxuICAgICAqIFVzZXIgcHJlZmVycmVkIHRleHQgbGluZSBoZWlnaHQsIGFzIGEgbXVsdGlwbGllciBvZiBmb250IHNpemUuXG4gICAgICovXG4gICAgbGluZUhlaWdodDogbnVtYmVyIHwgbnVsbDtcblxuICAgIC8qKlxuICAgICAqIFVzZXIgcHJlZmVycmVkIHRleHQgbGluZSB3aWR0aCBleHByZXNzZWQgaW4gQ1NTIGNoIHVuaXRzLlxuICAgICAqL1xuICAgIGxpbmVXaWR0aDogbnVtYmVyIHwgbnVsbDtcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdG8gaGlkZSB0aGUgWUFNTCBmcm9udCBtYXR0ZXIuXG4gICAgICovXG4gICAgaGlkZUZyb250TWF0dGVyOiBib29sZWFuO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHJlbmRlciB0aW1lb3V0LlxuICAgICAqL1xuICAgIHJlbmRlclRpbWVvdXQ6IG51bWJlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgZGVmYXVsdCBjb25maWd1cmF0aW9uIG9wdGlvbnMgZm9yIGFuIGVkaXRvci5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBkZWZhdWx0Q29uZmlnOiBNYXJrZG93blZpZXdlci5JQ29uZmlnID0ge1xuICAgIGZvbnRGYW1pbHk6IG51bGwsXG4gICAgZm9udFNpemU6IG51bGwsXG4gICAgbGluZUhlaWdodDogbnVsbCxcbiAgICBsaW5lV2lkdGg6IG51bGwsXG4gICAgaGlkZUZyb250TWF0dGVyOiB0cnVlLFxuICAgIHJlbmRlclRpbWVvdXQ6IDEwMDBcbiAgfTtcbn1cblxuLyoqXG4gKiBBIGRvY3VtZW50IHdpZGdldCBmb3IgbWFya2Rvd24gY29udGVudC5cbiAqL1xuZXhwb3J0IGNsYXNzIE1hcmtkb3duRG9jdW1lbnQgZXh0ZW5kcyBEb2N1bWVudFdpZGdldDxNYXJrZG93blZpZXdlcj4ge1xuICBzZXRGcmFnbWVudChmcmFnbWVudDogc3RyaW5nKTogdm9pZCB7XG4gICAgdGhpcy5jb250ZW50LnNldEZyYWdtZW50KGZyYWdtZW50KTtcbiAgfVxufVxuXG4vKipcbiAqIEEgd2lkZ2V0IGZhY3RvcnkgZm9yIG1hcmtkb3duIHZpZXdlcnMuXG4gKi9cbmV4cG9ydCBjbGFzcyBNYXJrZG93blZpZXdlckZhY3RvcnkgZXh0ZW5kcyBBQkNXaWRnZXRGYWN0b3J5PE1hcmtkb3duRG9jdW1lbnQ+IHtcbiAgLyoqXG4gICAqIENvbnN0cnVjdCBhIG5ldyBtYXJrZG93biB2aWV3ZXIgd2lkZ2V0IGZhY3RvcnkuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBNYXJrZG93blZpZXdlckZhY3RvcnkuSU9wdGlvbnMpIHtcbiAgICBzdXBlcihQcml2YXRlLmNyZWF0ZVJlZ2lzdHJ5T3B0aW9ucyhvcHRpb25zKSk7XG4gICAgdGhpcy5fZmlsZVR5cGUgPSBvcHRpb25zLnByaW1hcnlGaWxlVHlwZTtcbiAgICB0aGlzLl9yZW5kZXJtaW1lID0gb3B0aW9ucy5yZW5kZXJtaW1lO1xuICB9XG5cbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyB3aWRnZXQgZ2l2ZW4gYSBjb250ZXh0LlxuICAgKi9cbiAgcHJvdGVjdGVkIGNyZWF0ZU5ld1dpZGdldChcbiAgICBjb250ZXh0OiBEb2N1bWVudFJlZ2lzdHJ5LkNvbnRleHRcbiAgKTogTWFya2Rvd25Eb2N1bWVudCB7XG4gICAgY29uc3QgcmVuZGVybWltZSA9IHRoaXMuX3JlbmRlcm1pbWUuY2xvbmUoe1xuICAgICAgcmVzb2x2ZXI6IGNvbnRleHQudXJsUmVzb2x2ZXJcbiAgICB9KTtcbiAgICBjb25zdCByZW5kZXJlciA9IHJlbmRlcm1pbWUuY3JlYXRlUmVuZGVyZXIoTUlNRVRZUEUpO1xuICAgIGNvbnN0IGNvbnRlbnQgPSBuZXcgTWFya2Rvd25WaWV3ZXIoeyBjb250ZXh0LCByZW5kZXJlciB9KTtcbiAgICBjb250ZW50LnRpdGxlLmljb24gPSB0aGlzLl9maWxlVHlwZT8uaWNvbjtcbiAgICBjb250ZW50LnRpdGxlLmljb25DbGFzcyA9IHRoaXMuX2ZpbGVUeXBlPy5pY29uQ2xhc3MgPz8gJyc7XG4gICAgY29udGVudC50aXRsZS5pY29uTGFiZWwgPSB0aGlzLl9maWxlVHlwZT8uaWNvbkxhYmVsID8/ICcnO1xuICAgIGNvbnN0IHdpZGdldCA9IG5ldyBNYXJrZG93bkRvY3VtZW50KHsgY29udGVudCwgY29udGV4dCB9KTtcblxuICAgIHJldHVybiB3aWRnZXQ7XG4gIH1cblxuICBwcml2YXRlIF9maWxlVHlwZTogRG9jdW1lbnRSZWdpc3RyeS5JRmlsZVR5cGUgfCB1bmRlZmluZWQ7XG4gIHByaXZhdGUgX3JlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG59XG5cbi8qKlxuICogVGhlIG5hbWVzcGFjZSBmb3IgTWFya2Rvd25WaWV3ZXJGYWN0b3J5IGNsYXNzIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgTWFya2Rvd25WaWV3ZXJGYWN0b3J5IHtcbiAgLyoqXG4gICAqIFRoZSBvcHRpb25zIHVzZWQgdG8gaW5pdGlhbGl6ZSBhIE1hcmtkb3duVmlld2VyRmFjdG9yeS5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMgZXh0ZW5kcyBEb2N1bWVudFJlZ2lzdHJ5LklXaWRnZXRGYWN0b3J5T3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIHByaW1hcnkgZmlsZSB0eXBlIGFzc29jaWF0ZWQgd2l0aCB0aGUgZG9jdW1lbnQuXG4gICAgICovXG4gICAgcHJpbWFyeUZpbGVUeXBlOiBEb2N1bWVudFJlZ2lzdHJ5LklGaWxlVHlwZSB8IHVuZGVmaW5lZDtcblxuICAgIC8qKlxuICAgICAqIFRoZSByZW5kZXJtaW1lIGluc3RhbmNlLlxuICAgICAqL1xuICAgIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnk7XG4gIH1cbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgbWFya2Rvd24gdmlld2VyIHdpZGdldCBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIENyZWF0ZSB0aGUgZG9jdW1lbnQgcmVnaXN0cnkgb3B0aW9ucy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBjcmVhdGVSZWdpc3RyeU9wdGlvbnMoXG4gICAgb3B0aW9uczogTWFya2Rvd25WaWV3ZXJGYWN0b3J5LklPcHRpb25zXG4gICk6IERvY3VtZW50UmVnaXN0cnkuSVdpZGdldEZhY3RvcnlPcHRpb25zIHtcbiAgICByZXR1cm4ge1xuICAgICAgLi4ub3B0aW9ucyxcbiAgICAgIHJlYWRPbmx5OiB0cnVlXG4gICAgfSBhcyBEb2N1bWVudFJlZ2lzdHJ5LklXaWRnZXRGYWN0b3J5T3B0aW9ucztcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW1vdmUgWUFNTCBmcm9udCBtYXR0ZXIgZnJvbSBzb3VyY2UuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gcmVtb3ZlRnJvbnRNYXR0ZXIoc291cmNlOiBzdHJpbmcpOiBzdHJpbmcge1xuICAgIGNvbnN0IHJlID0gL14tLS1cXG5bXl0qP1xcbigtLS18Li4uKVxcbi87XG4gICAgY29uc3QgbWF0Y2ggPSBzb3VyY2UubWF0Y2gocmUpO1xuICAgIGlmICghbWF0Y2gpIHtcbiAgICAgIHJldHVybiBzb3VyY2U7XG4gICAgfVxuICAgIGNvbnN0IHsgbGVuZ3RoIH0gPSBtYXRjaFswXTtcbiAgICByZXR1cm4gc291cmNlLnNsaWNlKGxlbmd0aCk7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==