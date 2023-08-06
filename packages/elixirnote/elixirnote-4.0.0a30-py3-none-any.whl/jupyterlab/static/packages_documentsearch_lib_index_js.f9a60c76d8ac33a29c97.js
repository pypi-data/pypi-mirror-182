"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_documentsearch_lib_index_js"],{

/***/ "../../packages/documentsearch/lib/index.js":
/*!**************************************************!*\
  !*** ../../packages/documentsearch/lib/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FOUND_CLASSES": () => (/* reexport safe */ _providers_genericsearchprovider__WEBPACK_IMPORTED_MODULE_0__.FOUND_CLASSES),
/* harmony export */   "GenericSearchProvider": () => (/* reexport safe */ _providers_genericsearchprovider__WEBPACK_IMPORTED_MODULE_0__.GenericSearchProvider),
/* harmony export */   "HTMLSearchEngine": () => (/* reexport safe */ _providers_genericsearchprovider__WEBPACK_IMPORTED_MODULE_0__.HTMLSearchEngine),
/* harmony export */   "ISearchProviderRegistry": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_6__.ISearchProviderRegistry),
/* harmony export */   "SearchDocumentModel": () => (/* reexport safe */ _searchmodel__WEBPACK_IMPORTED_MODULE_2__.SearchDocumentModel),
/* harmony export */   "SearchDocumentView": () => (/* reexport safe */ _searchview__WEBPACK_IMPORTED_MODULE_3__.SearchDocumentView),
/* harmony export */   "SearchProvider": () => (/* reexport safe */ _searchprovider__WEBPACK_IMPORTED_MODULE_4__.SearchProvider),
/* harmony export */   "SearchProviderRegistry": () => (/* reexport safe */ _searchproviderregistry__WEBPACK_IMPORTED_MODULE_5__.SearchProviderRegistry),
/* harmony export */   "TextSearchEngine": () => (/* reexport safe */ _providers_textprovider__WEBPACK_IMPORTED_MODULE_1__.TextSearchEngine)
/* harmony export */ });
/* harmony import */ var _providers_genericsearchprovider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./providers/genericsearchprovider */ "../../packages/documentsearch/lib/providers/genericsearchprovider.js");
/* harmony import */ var _providers_textprovider__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./providers/textprovider */ "../../packages/documentsearch/lib/providers/textprovider.js");
/* harmony import */ var _searchmodel__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./searchmodel */ "../../packages/documentsearch/lib/searchmodel.js");
/* harmony import */ var _searchview__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./searchview */ "../../packages/documentsearch/lib/searchview.js");
/* harmony import */ var _searchprovider__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./searchprovider */ "../../packages/documentsearch/lib/searchprovider.js");
/* harmony import */ var _searchproviderregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./searchproviderregistry */ "../../packages/documentsearch/lib/searchproviderregistry.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./tokens */ "../../packages/documentsearch/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module documentsearch
 */









/***/ }),

/***/ "../../packages/documentsearch/lib/providers/genericsearchprovider.js":
/*!****************************************************************************!*\
  !*** ../../packages/documentsearch/lib/providers/genericsearchprovider.js ***!
  \****************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "FOUND_CLASSES": () => (/* binding */ FOUND_CLASSES),
/* harmony export */   "GenericSearchProvider": () => (/* binding */ GenericSearchProvider),
/* harmony export */   "HTMLSearchEngine": () => (/* binding */ HTMLSearchEngine)
/* harmony export */ });
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _searchprovider__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../searchprovider */ "../../packages/documentsearch/lib/searchprovider.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


const FOUND_CLASSES = ['cm-string', 'cm-overlay', 'cm-searching'];
const SELECTED_CLASSES = ['CodeMirror-selectedtext'];
/**
 * HTML search engine
 */
class HTMLSearchEngine {
    /**
     * Search for a `query` in a DOM tree.
     *
     * @param query Regular expression to search
     * @param rootNode DOM root node to search in
     * @returns The list of matches
     */
    static search(query, rootNode) {
        if (!(rootNode instanceof Node)) {
            console.warn('Unable to search with HTMLSearchEngine the provided object.', rootNode);
            return Promise.resolve([]);
        }
        if (!query.global) {
            query = new RegExp(query.source, query.flags + 'g');
        }
        const matches = [];
        const walker = document.createTreeWalker(rootNode, NodeFilter.SHOW_TEXT, {
            acceptNode: node => {
                // Filter subtrees of UNSUPPORTED_ELEMENTS and nodes that
                // do not contain our search text
                let parentElement = node.parentElement;
                while (parentElement !== rootNode) {
                    if (parentElement.nodeName in HTMLSearchEngine.UNSUPPORTED_ELEMENTS) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    parentElement = parentElement.parentElement;
                }
                return query.test(node.textContent)
                    ? NodeFilter.FILTER_ACCEPT
                    : NodeFilter.FILTER_REJECT;
            }
        });
        let node = null;
        while ((node = walker.nextNode()) !== null) {
            // Reset query index
            query.lastIndex = 0;
            let match = null;
            while ((match = query.exec(node.textContent)) !== null) {
                matches.push({
                    text: match[0],
                    position: match.index,
                    node: node
                });
            }
        }
        return Promise.resolve(matches);
    }
}
/**
 * We choose opt out as most node types should be searched (e.g. script).
 * Even nodes like <data>, could have textContent we care about.
 *
 * Note: nodeName is capitalized, so we do the same here
 */
HTMLSearchEngine.UNSUPPORTED_ELEMENTS = {
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Document_metadata
    BASE: true,
    HEAD: true,
    LINK: true,
    META: true,
    STYLE: true,
    TITLE: true,
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Sectioning_root
    BODY: true,
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Content_sectioning
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Text_content
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Inline_text_semantics
    // Above is searched
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Image_and_multimedia
    AREA: true,
    AUDIO: true,
    IMG: true,
    MAP: true,
    TRACK: true,
    VIDEO: true,
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Embedded_content
    APPLET: true,
    EMBED: true,
    IFRAME: true,
    NOEMBED: true,
    OBJECT: true,
    PARAM: true,
    PICTURE: true,
    SOURCE: true,
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Scripting
    CANVAS: true,
    NOSCRIPT: true,
    SCRIPT: true,
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Demarcating_edits
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Table_content
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Forms
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Interactive_elements
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element#Web_Components
    // Above is searched
    // Other:
    SVG: true
};
/**
 * Generic DOM tree search provider.
 */
class GenericSearchProvider extends _searchprovider__WEBPACK_IMPORTED_MODULE_1__.SearchProvider {
    constructor() {
        super(...arguments);
        /**
         * Set to true if the widget under search is read-only, false
         * if it is editable.  Will be used to determine whether to show
         * the replace option.
         */
        this.isReadOnly = true;
        this._matches = [];
        this._mutationObserver = new MutationObserver(this._onWidgetChanged.bind(this));
        this._markNodes = new Array();
    }
    /**
     * Report whether or not this provider has the ability to search on the given object
     */
    static isApplicable(domain) {
        return domain instanceof _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget;
    }
    /**
     * Instantiate a generic search provider for the widget.
     *
     * #### Notes
     * The widget provided is always checked using `isApplicable` before calling
     * this factory.
     *
     * @param widget The widget to search on
     * @param registry The search provider registry
     * @param translator [optional] The translator object
     *
     * @returns The search provider on the widget
     */
    static createNew(widget, registry, translator) {
        return new GenericSearchProvider(widget);
    }
    /**
     * The current index of the selected match.
     */
    get currentMatchIndex() {
        return this._currentMatchIndex >= 0 ? this._currentMatchIndex : null;
    }
    /**
     * The current match
     */
    get currentMatch() {
        var _a;
        return (_a = this._matches[this._currentMatchIndex]) !== null && _a !== void 0 ? _a : null;
    }
    /**
     * The current matches
     */
    get matches() {
        // Ensure that no other fn can overwrite matches index property
        // We shallow clone each node
        return this._matches
            ? this._matches.map(m => Object.assign({}, m))
            : this._matches;
    }
    /**
     * The number of matches.
     */
    get matchesCount() {
        return this._matches.length;
    }
    /**
     * Clear currently highlighted match.
     */
    clearHighlight() {
        if (this._currentMatchIndex >= 0) {
            const hit = this._markNodes[this._currentMatchIndex];
            hit.classList.remove(...SELECTED_CLASSES);
        }
        this._currentMatchIndex = -1;
        return Promise.resolve();
    }
    /**
     * Dispose of the resources held by the search provider.
     *
     * #### Notes
     * If the object's `dispose` method is called more than once, all
     * calls made after the first will be a no-op.
     *
     * #### Undefined Behavior
     * It is undefined behavior to use any functionality of the object
     * after it has been disposed unless otherwise explicitly noted.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        this.endQuery().catch(reason => {
            console.error(`Failed to end search query.`, reason);
        });
        super.dispose();
    }
    /**
     * Move the current match indicator to the next match.
     *
     * @param loop Whether to loop within the matches list.
     *
     * @returns A promise that resolves once the action has completed.
     */
    async highlightNext(loop) {
        var _a;
        return (_a = this._highlightNext(false, loop !== null && loop !== void 0 ? loop : true)) !== null && _a !== void 0 ? _a : undefined;
    }
    /**
     * Move the current match indicator to the previous match.
     *
     * @param loop Whether to loop within the matches list.
     *
     * @returns A promise that resolves once the action has completed.
     */
    async highlightPrevious(loop) {
        var _a;
        return (_a = this._highlightNext(true, loop !== null && loop !== void 0 ? loop : true)) !== null && _a !== void 0 ? _a : undefined;
    }
    /**
     * Replace the currently selected match with the provided text
     *
     * @param newText The replacement text
     * @param loop Whether to loop within the matches list.
     *
     * @returns A promise that resolves with a boolean indicating whether a replace occurred.
     */
    async replaceCurrentMatch(newText, loop) {
        return Promise.resolve(false);
    }
    /**
     * Replace all matches in the notebook with the provided text
     *
     * @param newText The replacement text
     *
     * @returns A promise that resolves with a boolean indicating whether a replace occurred.
     */
    async replaceAllMatches(newText) {
        // This is read only, but we could loosen this in theory for input boxes...
        return Promise.resolve(false);
    }
    /**
     * Initialize the search using the provided options.  Should update the UI
     * to highlight all matches and "select" whatever the first match should be.
     *
     * @param query A RegExp to be use to perform the search
     * @param filters Filter parameters to pass to provider
     */
    async startQuery(query, filters = {}) {
        await this.endQuery();
        this._query = query;
        if (query === null) {
            return Promise.resolve();
        }
        const matches = await HTMLSearchEngine.search(query, this.widget.node);
        // Transform the DOM
        let nodeIdx = 0;
        while (nodeIdx < matches.length) {
            let activeNode = matches[nodeIdx].node;
            let parent = activeNode.parentNode;
            let subMatches = [matches[nodeIdx]];
            while (++nodeIdx < matches.length &&
                matches[nodeIdx].node === activeNode) {
                subMatches.unshift(matches[nodeIdx]);
            }
            const markedNodes = subMatches.map(match => {
                // TODO: support tspan for svg when svg support is added
                const markedNode = document.createElement('mark');
                markedNode.classList.add(...FOUND_CLASSES);
                markedNode.textContent = match.text;
                const newNode = activeNode.splitText(match.position);
                newNode.textContent = newNode.textContent.slice(match.text.length);
                parent.insertBefore(markedNode, newNode);
                return markedNode;
            });
            // Insert node in reverse order as we replace from last to first
            // to maintain match position.
            for (let i = markedNodes.length - 1; i >= 0; i--) {
                this._markNodes.push(markedNodes[i]);
            }
        }
        // Watch for future changes:
        this._mutationObserver.observe(this.widget.node, 
        // https://developer.mozilla.org/en-US/docs/Web/API/MutationObserverInit
        {
            attributes: false,
            characterData: true,
            childList: true,
            subtree: true
        });
        this._matches = matches;
    }
    /**
     * Clear the highlighted matches and any internal state.
     */
    async endQuery() {
        this._mutationObserver.disconnect();
        this._markNodes.forEach(el => {
            const parent = el.parentNode;
            parent.replaceChild(document.createTextNode(el.textContent), el);
            parent.normalize();
        });
        this._markNodes = [];
        this._matches = [];
        this._currentMatchIndex = -1;
    }
    _highlightNext(reverse, loop) {
        if (this._matches.length === 0) {
            return null;
        }
        if (this._currentMatchIndex === -1) {
            this._currentMatchIndex = reverse ? this.matches.length - 1 : 0;
        }
        else {
            const hit = this._markNodes[this._currentMatchIndex];
            hit.classList.remove(...SELECTED_CLASSES);
            this._currentMatchIndex = reverse
                ? this._currentMatchIndex - 1
                : this._currentMatchIndex + 1;
            if (loop &&
                (this._currentMatchIndex < 0 ||
                    this._currentMatchIndex >= this._matches.length)) {
                // Cheap way to make this a circular buffer
                this._currentMatchIndex =
                    (this._currentMatchIndex + this._matches.length) %
                        this._matches.length;
            }
        }
        if (this._currentMatchIndex >= 0 &&
            this._currentMatchIndex < this._matches.length) {
            const hit = this._markNodes[this._currentMatchIndex];
            hit.classList.add(...SELECTED_CLASSES);
            // If not in view, scroll just enough to see it
            if (!elementInViewport(hit)) {
                hit.scrollIntoView(reverse);
            }
            hit.focus();
            return this._matches[this._currentMatchIndex];
        }
        else {
            this._currentMatchIndex = -1;
            return null;
        }
    }
    async _onWidgetChanged(mutations, observer) {
        this._currentMatchIndex = -1;
        // This is typically cheap, but we do not control the rate of change or size of the output
        await this.startQuery(this._query);
        this._stateChanged.emit();
    }
}
function elementInViewport(el) {
    const boundingClientRect = el.getBoundingClientRect();
    return (boundingClientRect.top >= 0 &&
        boundingClientRect.bottom <=
            (window.innerHeight || document.documentElement.clientHeight) &&
        boundingClientRect.left >= 0 &&
        boundingClientRect.right <=
            (window.innerWidth || document.documentElement.clientWidth));
}


/***/ }),

/***/ "../../packages/documentsearch/lib/providers/textprovider.js":
/*!*******************************************************************!*\
  !*** ../../packages/documentsearch/lib/providers/textprovider.js ***!
  \*******************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TextSearchEngine": () => (/* binding */ TextSearchEngine)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * Search provider for text/plain
 */
const TextSearchEngine = {
    /**
     * Search for regular expression matches in a string.
     *
     * @param query Query regular expression
     * @param data String to look into
     * @returns List of matches
     */
    search(query, data) {
        // If data is not a string, try to JSON serialize the data.
        if (typeof data !== 'string') {
            try {
                data = JSON.stringify(data);
            }
            catch (reason) {
                console.warn('Unable to search with TextSearchEngine non-JSON serializable object.', reason, data);
                return Promise.resolve([]);
            }
        }
        if (!query.global) {
            query = new RegExp(query.source, query.flags + 'g');
        }
        const matches = new Array();
        let match = null;
        while ((match = query.exec(data)) !== null) {
            matches.push({
                text: match[0],
                position: match.index
            });
        }
        return Promise.resolve(matches);
    }
};


/***/ }),

/***/ "../../packages/documentsearch/lib/searchmodel.js":
/*!********************************************************!*\
  !*** ../../packages/documentsearch/lib/searchmodel.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SearchDocumentModel": () => (/* binding */ SearchDocumentModel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/polling */ "webpack/sharing/consume/default/@lumino/polling/@lumino/polling");
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_polling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * Search in a document model.
 */
class SearchDocumentModel extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.VDomModel {
    /**
     * Search document model
     * @param searchProvider Provider for the current document
     * @param searchDebounceTime Debounce search time
     */
    constructor(searchProvider, searchDebounceTime) {
        super();
        this.searchProvider = searchProvider;
        this._caseSensitive = false;
        this._disposed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        this._parsingError = '';
        this._filters = {};
        this._searchExpression = '';
        this._useRegex = false;
        this._filters = {};
        if (this.searchProvider.getFilters) {
            const filters = this.searchProvider.getFilters();
            for (const filter in filters) {
                this._filters[filter] = filters[filter].default;
            }
        }
        searchProvider.stateChanged.connect(this.refresh, this);
        this._searchDebouncer = new _lumino_polling__WEBPACK_IMPORTED_MODULE_2__.Debouncer(() => {
            this._updateSearch().catch(reason => {
                console.error('Failed to update search on document.', reason);
            });
        }, searchDebounceTime);
    }
    /**
     * Whether the search is case sensitive or not.
     */
    get caseSensitive() {
        return this._caseSensitive;
    }
    set caseSensitive(v) {
        if (this._caseSensitive !== v) {
            this._caseSensitive = v;
            this.stateChanged.emit();
            this.refresh();
        }
    }
    /**
     * Current highlighted match index.
     */
    get currentIndex() {
        return this.searchProvider.currentMatchIndex;
    }
    /**
     * A signal emitted when the object is disposed.
     */
    get disposed() {
        return this._disposed;
    }
    /**
     * Filter values.
     */
    get filters() {
        return this._filters;
    }
    set filters(v) {
        if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(this._filters, v)) {
            this._filters = v;
            this.stateChanged.emit();
            this.refresh();
        }
    }
    /**
     * Filter definitions for the current provider.
     */
    get filtersDefinition() {
        var _a, _b, _c;
        return (_c = (_b = (_a = this.searchProvider).getFilters) === null || _b === void 0 ? void 0 : _b.call(_a)) !== null && _c !== void 0 ? _c : {};
    }
    /**
     * The initial query string.
     */
    get initialQuery() {
        return this._searchExpression || this.searchProvider.getInitialQuery();
    }
    /**
     * Whether the document is read-only or not.
     */
    get isReadOnly() {
        return this.searchProvider.isReadOnly;
    }
    /**
     * Parsing regular expression error message.
     */
    get parsingError() {
        return this._parsingError;
    }
    /**
     * Replacement expression
     */
    get replaceText() {
        return this._replaceText;
    }
    set replaceText(v) {
        if (this._replaceText !== v) {
            this._replaceText = v;
            this.stateChanged.emit();
        }
    }
    /**
     * Search expression
     */
    get searchExpression() {
        return this._searchExpression;
    }
    set searchExpression(v) {
        if (this._searchExpression !== v) {
            this._searchExpression = v;
            this.stateChanged.emit();
            this.refresh();
        }
    }
    /**
     * Total number of matches.
     */
    get totalMatches() {
        return this.searchProvider.matchesCount;
    }
    /**
     * Whether to use regular expression or not.
     */
    get useRegex() {
        return this._useRegex;
    }
    set useRegex(v) {
        if (this._useRegex !== v) {
            this._useRegex = v;
            this.stateChanged.emit();
            this.refresh();
        }
    }
    /**
     * Dispose the model.
     */
    dispose() {
        if (this.isDisposed) {
            return;
        }
        if (this._searchExpression) {
            this.endQuery().catch(reason => {
                console.error(`Failed to end query '${this._searchExpression}.`, reason);
            });
        }
        this.searchProvider.stateChanged.disconnect(this.refresh, this);
        this._searchDebouncer.dispose();
        super.dispose();
    }
    /**
     * End the query.
     */
    async endQuery() {
        await this.searchProvider.endQuery();
        this.stateChanged.emit();
    }
    /**
     * Highlight the next match.
     */
    async highlightNext() {
        await this.searchProvider.highlightNext();
        // Emit state change as the index needs to be updated
        this.stateChanged.emit();
    }
    /**
     * Highlight the previous match
     */
    async highlightPrevious() {
        await this.searchProvider.highlightPrevious();
        // Emit state change as the index needs to be updated
        this.stateChanged.emit();
    }
    /**
     * Refresh search
     */
    refresh() {
        this._searchDebouncer.invoke().catch(reason => {
            console.error('Failed to invoke search document debouncer.', reason);
        });
    }
    /**
     * Replace all matches.
     */
    async replaceAllMatches() {
        await this.searchProvider.replaceAllMatches(this._replaceText);
        // Emit state change as the index needs to be updated
        this.stateChanged.emit();
    }
    /**
     * Replace the current match.
     */
    async replaceCurrentMatch() {
        await this.searchProvider.replaceCurrentMatch(this._replaceText);
        // Emit state change as the index needs to be updated
        this.stateChanged.emit();
    }
    async _updateSearch() {
        if (this._parsingError) {
            this._parsingError = '';
            this.stateChanged.emit();
        }
        try {
            const query = this.searchExpression
                ? Private.parseQuery(this.searchExpression, this.caseSensitive, this.useRegex)
                : null;
            if (query) {
                await this.searchProvider.startQuery(query, this._filters);
                // Emit state change as the index needs to be updated
                this.stateChanged.emit();
            }
        }
        catch (reason) {
            this._parsingError = reason;
            this.stateChanged.emit();
            console.error(`Failed to parse expression ${this.searchExpression}`, reason);
        }
    }
}
var Private;
(function (Private) {
    /**
     * Build the regular expression to use for searching.
     *
     * @param queryString Query string
     * @param caseSensitive Whether the search is case sensitive or not
     * @param regex Whether the expression is a regular expression
     * @returns The regular expression to use
     */
    function parseQuery(queryString, caseSensitive, regex) {
        const flag = caseSensitive ? 'g' : 'gi';
        // escape regex characters in query if its a string search
        const queryText = regex
            ? queryString
            : queryString.replace(/[-[\]/{}()*+?.\\^$|]/g, '\\$&');
        let ret;
        ret = new RegExp(queryText, flag);
        // If the empty string is hit, the search logic will freeze the browser tab
        //  Trying /^/ or /$/ on the codemirror search demo, does not find anything.
        //  So this is a limitation of the editor.
        if (ret.test('')) {
            return null;
        }
        return ret;
    }
    Private.parseQuery = parseQuery;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/documentsearch/lib/searchprovider.js":
/*!***********************************************************!*\
  !*** ../../packages/documentsearch/lib/searchprovider.js ***!
  \***********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SearchProvider": () => (/* binding */ SearchProvider)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * Abstract class implementing the search provider interface.
 */
class SearchProvider {
    /**
     * Constructor
     *
     * @param widget The widget to search in
     */
    constructor(widget) {
        this.widget = widget;
        this._stateChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
        this._disposed = false;
    }
    /**
     * Signal indicating that something in the search has changed, so the UI should update
     */
    get stateChanged() {
        return this._stateChanged;
    }
    /**
     * The current index of the selected match.
     */
    get currentMatchIndex() {
        return null;
    }
    /**
     * Whether the search provider is disposed or not.
     */
    get isDisposed() {
        return this._disposed;
    }
    /**
     * The number of matches.
     */
    get matchesCount() {
        return null;
    }
    /**
     * Dispose of the resources held by the search provider.
     *
     * #### Notes
     * If the object's `dispose` method is called more than once, all
     * calls made after the first will be a no-op.
     *
     * #### Undefined Behavior
     * It is undefined behavior to use any functionality of the object
     * after it has been disposed unless otherwise explicitly noted.
     */
    dispose() {
        if (this._disposed) {
            return;
        }
        this._disposed = true;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal.clearData(this);
    }
    /**
     * Get an initial query value if applicable so that it can be entered
     * into the search box as an initial query
     *
     * @returns Initial value used to populate the search box.
     */
    getInitialQuery() {
        return '';
    }
    /**
     * Get the filters for the given provider.
     *
     * @returns The filters.
     *
     * ### Notes
     * TODO For now it only supports boolean filters (represented with checkboxes)
     */
    getFilters() {
        return {};
    }
}


/***/ }),

/***/ "../../packages/documentsearch/lib/searchproviderregistry.js":
/*!*******************************************************************!*\
  !*** ../../packages/documentsearch/lib/searchproviderregistry.js ***!
  \*******************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SearchProviderRegistry": () => (/* binding */ SearchProviderRegistry)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Search provider registry
 */
class SearchProviderRegistry {
    /**
     * Constructor
     *
     * @param translator Application translator object
     */
    constructor(translator = _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator) {
        this.translator = translator;
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this._providerMap = new Map();
    }
    /**
     * Add a provider to the registry.
     *
     * @param key - The provider key.
     * @returns A disposable delegate that, when disposed, deregisters the given search provider
     */
    add(key, provider) {
        this._providerMap.set(key, provider);
        this._changed.emit();
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_1__.DisposableDelegate(() => {
            this._providerMap.delete(key);
            this._changed.emit();
        });
    }
    /**
     * Returns a matching provider for the widget.
     *
     * @param widget - The widget to search over.
     * @returns the search provider, or undefined if none exists.
     */
    getProvider(widget) {
        // iterate through all providers and ask each one if it can search on the
        // widget.
        for (const P of this._providerMap.values()) {
            if (P.isApplicable(widget)) {
                return P.createNew(widget, this.translator);
            }
        }
        return undefined;
    }
    /**
     * Whether the registry as a matching provider for the widget.
     *
     * @param widget - The widget to search over.
     * @returns Provider existence
     */
    hasProvider(widget) {
        for (const P of this._providerMap.values()) {
            if (P.isApplicable(widget)) {
                return true;
            }
        }
        return false;
    }
    /**
     * Signal that emits when a new search provider has been registered
     * or removed.
     */
    get changed() {
        return this._changed;
    }
}


/***/ }),

/***/ "../../packages/documentsearch/lib/searchview.js":
/*!*******************************************************!*\
  !*** ../../packages/documentsearch/lib/searchview.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SearchDocumentView": () => (/* binding */ SearchDocumentView)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_4__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.





const OVERLAY_CLASS = 'jp-DocumentSearch-overlay';
const OVERLAY_ROW_CLASS = 'jp-DocumentSearch-overlay-row';
const INPUT_CLASS = 'jp-DocumentSearch-input';
const INPUT_WRAPPER_CLASS = 'jp-DocumentSearch-input-wrapper';
const INPUT_BUTTON_CLASS_OFF = 'jp-DocumentSearch-input-button-off';
const INPUT_BUTTON_CLASS_ON = 'jp-DocumentSearch-input-button-on';
const INDEX_COUNTER_CLASS = 'jp-DocumentSearch-index-counter';
const UP_DOWN_BUTTON_WRAPPER_CLASS = 'jp-DocumentSearch-up-down-wrapper';
const UP_DOWN_BUTTON_CLASS = 'jp-DocumentSearch-up-down-button';
const ELLIPSES_BUTTON_CLASS = 'jp-DocumentSearch-ellipses-button';
const ELLIPSES_BUTTON_ENABLED_CLASS = 'jp-DocumentSearch-ellipses-button-enabled';
const REGEX_ERROR_CLASS = 'jp-DocumentSearch-regex-error';
const SEARCH_OPTIONS_CLASS = 'jp-DocumentSearch-search-options';
const SEARCH_OPTIONS_DISABLED_CLASS = 'jp-DocumentSearch-search-options-disabled';
const SEARCH_DOCUMENT_LOADING = 'jp-DocumentSearch-document-loading';
const REPLACE_ENTRY_CLASS = 'jp-DocumentSearch-replace-entry';
const REPLACE_BUTTON_CLASS = 'jp-DocumentSearch-replace-button';
const REPLACE_BUTTON_WRAPPER_CLASS = 'jp-DocumentSearch-replace-button-wrapper';
const REPLACE_WRAPPER_CLASS = 'jp-DocumentSearch-replace-wrapper-class';
const REPLACE_TOGGLE_CLASS = 'jp-DocumentSearch-replace-toggle';
const TOGGLE_WRAPPER = 'jp-DocumentSearch-toggle-wrapper';
const TOGGLE_PLACEHOLDER = 'jp-DocumentSearch-toggle-placeholder';
const BUTTON_CONTENT_CLASS = 'jp-DocumentSearch-button-content';
const BUTTON_WRAPPER_CLASS = 'jp-DocumentSearch-button-wrapper';
const SPACER_CLASS = 'jp-DocumentSearch-spacer';
function SearchEntry(props) {
    var _a;
    const trans = ((_a = props.translator) !== null && _a !== void 0 ? _a : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator).load('jupyterlab');
    const caseButtonToggleClass = (0,_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.classes)(props.caseSensitive ? INPUT_BUTTON_CLASS_ON : INPUT_BUTTON_CLASS_OFF, BUTTON_CONTENT_CLASS);
    const regexButtonToggleClass = (0,_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.classes)(props.useRegex ? INPUT_BUTTON_CLASS_ON : INPUT_BUTTON_CLASS_OFF, BUTTON_CONTENT_CLASS);
    const wrapperClass = INPUT_WRAPPER_CLASS;
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: wrapperClass },
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("input", { placeholder: trans.__('Find'), className: INPUT_CLASS, value: props.searchText, onChange: e => props.onChange(e), onKeyDown: e => props.onKeydown(e), tabIndex: 0, ref: props.inputRef, title: trans.__('Find') }),
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => {
                props.onCaseSensitiveToggled();
            }, tabIndex: 0, title: trans.__('Match Case') },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caseSensitiveIcon.react, { className: caseButtonToggleClass, tag: "span" })),
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => props.onRegexToggled(), tabIndex: 0, title: trans.__('Use Regular Expression') },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.regexIcon.react, { className: regexButtonToggleClass, tag: "span" }))));
}
function ReplaceEntry(props) {
    var _a;
    const trans = ((_a = props.translator) !== null && _a !== void 0 ? _a : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator).load('jupyterlab');
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: REPLACE_WRAPPER_CLASS },
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("input", { placeholder: trans.__('Replace'), className: REPLACE_ENTRY_CLASS, value: props.replaceText, onKeyDown: e => props.onReplaceKeydown(e), onChange: e => props.onChange(e), tabIndex: 0, title: trans.__('Replace') }),
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: REPLACE_BUTTON_WRAPPER_CLASS, onClick: () => props.onReplaceCurrent(), tabIndex: 0 },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement("span", { className: `${REPLACE_BUTTON_CLASS} ${BUTTON_CONTENT_CLASS}`, tabIndex: 0 }, trans.__('Replace'))),
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: REPLACE_BUTTON_WRAPPER_CLASS, tabIndex: 0, onClick: () => props.onReplaceAll() },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement("span", { className: `${REPLACE_BUTTON_CLASS} ${BUTTON_CONTENT_CLASS}`, tabIndex: -1 }, trans.__('Replace All')))));
}
function UpDownButtons(props) {
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: UP_DOWN_BUTTON_WRAPPER_CLASS },
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => props.onHighlightPrevious(), tabIndex: 0, title: props.trans.__('Previous Match') },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretUpEmptyThinIcon.react, { className: (0,_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.classes)(UP_DOWN_BUTTON_CLASS, BUTTON_CONTENT_CLASS), tag: "span" })),
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => props.onHighlightNext(), tabIndex: 0, title: props.trans.__('Next Match') },
            react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretDownEmptyThinIcon.react, { className: (0,_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.classes)(UP_DOWN_BUTTON_CLASS, BUTTON_CONTENT_CLASS), tag: "span" }))));
}
function SearchIndices(props) {
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: INDEX_COUNTER_CLASS }, props.totalMatches === 0
        ? '-/-'
        : `${props.currentIndex === null ? '-' : props.currentIndex + 1}/${props.totalMatches}`));
}
function FilterToggle(props) {
    let className = `${ELLIPSES_BUTTON_CLASS} ${BUTTON_CONTENT_CLASS}`;
    if (props.enabled) {
        className = `${className} ${ELLIPSES_BUTTON_ENABLED_CLASS}`;
    }
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => props.toggleEnabled(), tabIndex: 0, title: props.enabled
            ? props.trans.__('Hide Search Filters')
            : props.trans.__('Show Search Filters') },
        react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.ellipsesIcon.react, { className: className, tag: "span", height: "20px", width: "20px" })));
}
function FilterSelection(props) {
    return (react__WEBPACK_IMPORTED_MODULE_4__.createElement("label", { className: props.isEnabled ? '' : SEARCH_OPTIONS_DISABLED_CLASS, title: props.description },
        props.title,
        react__WEBPACK_IMPORTED_MODULE_4__.createElement("input", { type: "checkbox", disabled: !props.isEnabled, checked: props.value, onChange: props.onToggle })));
}
class SearchOverlay extends react__WEBPACK_IMPORTED_MODULE_4__.Component {
    constructor(props) {
        super(props);
        this.translator = props.translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator;
        this.state = {
            filtersOpen: false
        };
    }
    _onSearchChange(event) {
        const searchText = event.target.value;
        this.props.onSearchChanged(searchText);
    }
    _onSearchKeydown(event) {
        if (event.keyCode === 13) {
            // Enter pressed
            event.preventDefault();
            event.stopPropagation();
            event.shiftKey
                ? this.props.onHighlightPrevious()
                : this.props.onHighlightNext();
        }
        else if (event.keyCode === 27) {
            // Escape pressed
            event.preventDefault();
            event.stopPropagation();
            this._onClose();
        }
    }
    _onReplaceKeydown(event) {
        if (event.keyCode === 13) {
            // Enter pressed
            event.preventDefault();
            event.stopPropagation();
            this.props.onReplaceCurrent();
        }
    }
    _onClose() {
        // Clean up and close widget.
        this.props.onClose();
    }
    _onReplaceToggled() {
        // Deactivate invalid replace filters
        const filters = Object.assign({}, this.props.filters);
        if (!this.props.replaceEntryVisible) {
            for (const key in this.props.filtersDefinition) {
                const filter = this.props.filtersDefinition[key];
                if (!filter.supportReplace) {
                    filters[key] = false;
                }
            }
        }
        this.props.onFiltersChanged(filters);
        this.props.onReplaceEntryShown(!this.props.replaceEntryVisible);
    }
    _toggleFiltersOpen() {
        this.setState(prevState => ({
            filtersOpen: !prevState.filtersOpen
        }));
    }
    render() {
        var _a;
        const trans = this.translator.load('jupyterlab');
        const showReplace = !this.props.isReadOnly && this.props.replaceEntryVisible;
        const filters = this.props.filtersDefinition;
        const hasFilters = Object.keys(filters).length > 0;
        const filterToggle = hasFilters ? (react__WEBPACK_IMPORTED_MODULE_4__.createElement(FilterToggle, { enabled: this.state.filtersOpen, toggleEnabled: () => this._toggleFiltersOpen(), trans: trans })) : null;
        const filter = hasFilters ? (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: SEARCH_OPTIONS_CLASS }, Object.keys(filters).map(name => {
            var _a;
            const filter = filters[name];
            return (react__WEBPACK_IMPORTED_MODULE_4__.createElement(FilterSelection, { key: name, title: filter.title, description: filter.description, isEnabled: !showReplace || filter.supportReplace, onToggle: () => {
                    const newFilter = {};
                    newFilter[name] = !this.props.filters[name];
                    this.props.onFiltersChanged(newFilter);
                }, value: (_a = this.props.filters[name]) !== null && _a !== void 0 ? _a : filter.default }));
        }))) : null;
        const icon = this.props.replaceEntryVisible
            ? _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretDownIcon
            : _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretRightIcon;
        // TODO: Error messages from regex are not currently localizable.
        return (react__WEBPACK_IMPORTED_MODULE_4__.createElement(react__WEBPACK_IMPORTED_MODULE_4__.Fragment, null,
            react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: OVERLAY_ROW_CLASS },
                this.props.isReadOnly ? (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: TOGGLE_PLACEHOLDER })) : (react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: TOGGLE_WRAPPER, onClick: () => this._onReplaceToggled(), tabIndex: 0, title: trans.__('Toggle Replace') },
                    react__WEBPACK_IMPORTED_MODULE_4__.createElement(icon.react, { className: `${REPLACE_TOGGLE_CLASS} ${BUTTON_CONTENT_CLASS}`, tag: "span", elementPosition: "center", height: "20px", width: "20px" }))),
                react__WEBPACK_IMPORTED_MODULE_4__.createElement(SearchEntry, { inputRef: this.props.searchInputRef, useRegex: this.props.useRegex, caseSensitive: this.props.caseSensitive, onCaseSensitiveToggled: this.props.onCaseSensitiveToggled, onRegexToggled: this.props.onRegexToggled, onKeydown: (e) => this._onSearchKeydown(e), onChange: (e) => this._onSearchChange(e), searchText: this.props.searchText, translator: this.translator }),
                react__WEBPACK_IMPORTED_MODULE_4__.createElement(SearchIndices, { currentIndex: this.props.currentIndex, totalMatches: (_a = this.props.totalMatches) !== null && _a !== void 0 ? _a : 0 }),
                react__WEBPACK_IMPORTED_MODULE_4__.createElement(UpDownButtons, { onHighlightPrevious: () => {
                        this.props.onHighlightPrevious();
                    }, onHighlightNext: () => {
                        this.props.onHighlightNext();
                    }, trans: trans }),
                showReplace ? null : filterToggle,
                react__WEBPACK_IMPORTED_MODULE_4__.createElement("button", { className: BUTTON_WRAPPER_CLASS, onClick: () => this._onClose(), tabIndex: 0 },
                    react__WEBPACK_IMPORTED_MODULE_4__.createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.closeIcon.react, { className: "jp-icon-hover", elementPosition: "center", height: "16px", width: "16px" }))),
            react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: OVERLAY_ROW_CLASS }, showReplace ? (react__WEBPACK_IMPORTED_MODULE_4__.createElement(react__WEBPACK_IMPORTED_MODULE_4__.Fragment, null,
                react__WEBPACK_IMPORTED_MODULE_4__.createElement(ReplaceEntry, { onReplaceKeydown: (e) => this._onReplaceKeydown(e), onChange: (e) => this.props.onReplaceChanged(e.target.value), onReplaceCurrent: () => this.props.onReplaceCurrent(), onReplaceAll: () => this.props.onReplaceAll(), replaceText: this.props.replaceText, translator: this.translator }),
                react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: SPACER_CLASS }),
                filterToggle)) : null),
            this.state.filtersOpen ? filter : null,
            !!this.props.errorMessage && (react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: REGEX_ERROR_CLASS }, this.props.errorMessage)),
            react__WEBPACK_IMPORTED_MODULE_4__.createElement("div", { className: SEARCH_DOCUMENT_LOADING }, trans.__('This document is still loading. Only loaded content will appear in search results until the entire document loads.'))));
    }
}
/**
 * Search document widget
 */
class SearchDocumentView extends _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.VDomRenderer {
    /**
     * Search document widget constructor.
     *
     * @param model Search document model
     * @param translator Application translator object
     */
    constructor(model, translator) {
        super(model);
        this.translator = translator;
        this._showReplace = false;
        this._closed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_2__.Signal(this);
        this.addClass(OVERLAY_CLASS);
        this._searchInput = react__WEBPACK_IMPORTED_MODULE_4__.createRef();
    }
    /**
     * A signal emitted when the widget is closed.
     *
     * Closing the widget detached it from the DOM but does not dispose it.
     */
    get closed() {
        return this._closed;
    }
    /**
     * Focus search input.
     */
    focusSearchInput() {
        var _a;
        (_a = this._searchInput.current) === null || _a === void 0 ? void 0 : _a.select();
    }
    /**
     * Set the search text
     *
     * It does not trigger a view update.
     */
    setSearchText(search) {
        this.model.searchExpression = search;
    }
    /**
     * Set the replace text
     *
     * It does not trigger a view update.
     */
    setReplaceText(replace) {
        this.model.replaceText = replace;
    }
    /**
     * Show the replacement input box.
     */
    showReplace() {
        this.setReplaceInputVisibility(true);
    }
    setReplaceInputVisibility(v) {
        if (this._showReplace !== v) {
            this._showReplace = v;
            this.update();
        }
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_4__.createElement(SearchOverlay, { caseSensitive: this.model.caseSensitive, currentIndex: this.model.currentIndex, isReadOnly: this.model.isReadOnly, errorMessage: this.model.parsingError, filters: this.model.filters, filtersDefinition: this.model.filtersDefinition, replaceEntryVisible: this._showReplace, replaceText: this.model.replaceText, searchText: this.model.searchExpression, searchInputRef: this._searchInput, totalMatches: this.model.totalMatches, translator: this.translator, useRegex: this.model.useRegex, onCaseSensitiveToggled: () => {
                this.model.caseSensitive = !this.model.caseSensitive;
            }, onRegexToggled: () => {
                this.model.useRegex = !this.model.useRegex;
            }, onFiltersChanged: (filters) => {
                this.model.filters = Object.assign(Object.assign({}, this.model.filters), filters);
            }, onHighlightNext: () => {
                void this.model.highlightNext();
            }, onHighlightPrevious: () => {
                void this.model.highlightPrevious();
            }, onSearchChanged: (q) => {
                this.model.searchExpression = q;
            }, onClose: async () => {
                _lumino_widgets__WEBPACK_IMPORTED_MODULE_3__.Widget.detach(this);
                this._closed.emit();
                await this.model.endQuery();
            }, onReplaceEntryShown: (v) => {
                this.setReplaceInputVisibility(v);
            }, onReplaceChanged: (q) => {
                this.model.replaceText = q;
            }, onReplaceCurrent: () => {
                void this.model.replaceCurrentMatch();
            }, onReplaceAll: () => {
                void this.model.replaceAllMatches();
            } }));
    }
}


/***/ }),

/***/ "../../packages/documentsearch/lib/tokens.js":
/*!***************************************************!*\
  !*** ../../packages/documentsearch/lib/tokens.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ISearchProviderRegistry": () => (/* binding */ ISearchProviderRegistry)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * The search provider registry token.
 */
const ISearchProviderRegistry = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/documentsearch:ISearchProviderRegistry');


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZG9jdW1lbnRzZWFyY2hfbGliX2luZGV4X2pzLmY5YTYwYzc2ZDhhYzMzYTI5Yzk3LmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQUUrQztBQUNUO0FBQ1g7QUFDRDtBQUNJO0FBQ1E7QUFDaEI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDYnpCLDBDQUEwQztBQUMxQywyREFBMkQ7QUFFbEI7QUFNVTtBQUc1QyxNQUFNLGFBQWEsR0FBRyxDQUFDLFdBQVcsRUFBRSxZQUFZLEVBQUUsY0FBYyxDQUFDLENBQUM7QUFDekUsTUFBTSxnQkFBZ0IsR0FBRyxDQUFDLHlCQUF5QixDQUFDLENBQUM7QUFFckQ7O0dBRUc7QUFDSSxNQUFNLGdCQUFnQjtJQW1EM0I7Ozs7OztPQU1HO0lBQ0gsTUFBTSxDQUFDLE1BQU0sQ0FBQyxLQUFhLEVBQUUsUUFBYztRQUN6QyxJQUFJLENBQUMsQ0FBQyxRQUFRLFlBQVksSUFBSSxDQUFDLEVBQUU7WUFDL0IsT0FBTyxDQUFDLElBQUksQ0FDViw2REFBNkQsRUFDN0QsUUFBUSxDQUNULENBQUM7WUFDRixPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsRUFBRSxDQUFDLENBQUM7U0FDNUI7UUFFRCxJQUFJLENBQUMsS0FBSyxDQUFDLE1BQU0sRUFBRTtZQUNqQixLQUFLLEdBQUcsSUFBSSxNQUFNLENBQUMsS0FBSyxDQUFDLE1BQU0sRUFBRSxLQUFLLENBQUMsS0FBSyxHQUFHLEdBQUcsQ0FBQyxDQUFDO1NBQ3JEO1FBRUQsTUFBTSxPQUFPLEdBQXVCLEVBQUUsQ0FBQztRQUN2QyxNQUFNLE1BQU0sR0FBRyxRQUFRLENBQUMsZ0JBQWdCLENBQUMsUUFBUSxFQUFFLFVBQVUsQ0FBQyxTQUFTLEVBQUU7WUFDdkUsVUFBVSxFQUFFLElBQUksQ0FBQyxFQUFFO2dCQUNqQix5REFBeUQ7Z0JBQ3pELGlDQUFpQztnQkFDakMsSUFBSSxh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Q0FBQyxLQUFLLENBQUMsUUFBUSxFQUFFLENBQUM7WUFDOUIsQ0FBQyxFQUNELG1CQUFtQixFQUFFLENBQUMsQ0FBVSxFQUFFLEVBQUU7Z0JBQ2xDLElBQUksQ0FBQyx5QkFBeUIsQ0FBQyxDQUFDLENBQUMsQ0FBQztZQUNwQyxDQUFDLEVBQ0QsZ0JBQWdCLEVBQUUsQ0FBQyxDQUFTLEVBQUUsRUFBRTtnQkFDOUIsSUFBSSxDQUFDLEtBQUssQ0FBQyxXQUFXLEdBQUcsQ0FBQyxDQUFDO1lBQzdCLENBQUMsRUFDRCxnQkFBZ0IsRUFBRSxHQUFHLEVBQUU7Z0JBQ3JCLEtBQUssSUFBSSxDQUFDLEtBQUssQ0FBQyxtQkFBbUIsRUFBRSxDQUFDO1lBQ3hDLENBQUMsRUFDRCxZQUFZLEVBQUUsR0FBRyxFQUFFO2dCQUNqQixLQUFLLElBQUksQ0FBQyxLQUFLLENBQUMsaUJBQWlCLEVBQUUsQ0FBQztZQUN0QyxDQUFDLEdBQ2MsQ0FDbEIsQ0FBQztJQUNKLENBQUM7Q0FLRjs7Ozs7Ozs7Ozs7Ozs7Ozs7QUM1c0JELDBDQUEwQztBQUMxQywyREFBMkQ7QUFHakI7QUFLMUM7O0dBRUc7QUFDSSxNQUFNLHVCQUF1QixHQUFHLElBQUksb0RBQUssQ0FDOUMsb0RBQW9ELENBQ3JELENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jdW1lbnRzZWFyY2gvc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2N1bWVudHNlYXJjaC9zcmMvcHJvdmlkZXJzL2dlbmVyaWNzZWFyY2hwcm92aWRlci50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jdW1lbnRzZWFyY2gvc3JjL3Byb3ZpZGVycy90ZXh0cHJvdmlkZXIudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RvY3VtZW50c2VhcmNoL3NyYy9zZWFyY2htb2RlbC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jdW1lbnRzZWFyY2gvc3JjL3NlYXJjaHByb3ZpZGVyLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2N1bWVudHNlYXJjaC9zcmMvc2VhcmNocHJvdmlkZXJyZWdpc3RyeS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvZG9jdW1lbnRzZWFyY2gvc3JjL3NlYXJjaHZpZXcudHN4Iiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9kb2N1bWVudHNlYXJjaC9zcmMvdG9rZW5zLnRzIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbi8qKlxuICogQHBhY2thZ2VEb2N1bWVudGF0aW9uXG4gKiBAbW9kdWxlIGRvY3VtZW50c2VhcmNoXG4gKi9cblxuZXhwb3J0ICogZnJvbSAnLi9wcm92aWRlcnMvZ2VuZXJpY3NlYXJjaHByb3ZpZGVyJztcbmV4cG9ydCAqIGZyb20gJy4vcHJvdmlkZXJzL3RleHRwcm92aWRlcic7XG5leHBvcnQgKiBmcm9tICcuL3NlYXJjaG1vZGVsJztcbmV4cG9ydCAqIGZyb20gJy4vc2VhcmNodmlldyc7XG5leHBvcnQgKiBmcm9tICcuL3NlYXJjaHByb3ZpZGVyJztcbmV4cG9ydCAqIGZyb20gJy4vc2VhcmNocHJvdmlkZXJyZWdpc3RyeSc7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQge1xuICBJSFRNTFNlYXJjaE1hdGNoLFxuICBJU2VhcmNoUHJvdmlkZXIsXG4gIElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5XG59IGZyb20gJy4uL3Rva2Vucyc7XG5pbXBvcnQgeyBTZWFyY2hQcm92aWRlciB9IGZyb20gJy4uL3NlYXJjaHByb3ZpZGVyJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG5leHBvcnQgY29uc3QgRk9VTkRfQ0xBU1NFUyA9IFsnY20tc3RyaW5nJywgJ2NtLW92ZXJsYXknLCAnY20tc2VhcmNoaW5nJ107XG5jb25zdCBTRUxFQ1RFRF9DTEFTU0VTID0gWydDb2RlTWlycm9yLXNlbGVjdGVkdGV4dCddO1xuXG4vKipcbiAqIEhUTUwgc2VhcmNoIGVuZ2luZVxuICovXG5leHBvcnQgY2xhc3MgSFRNTFNlYXJjaEVuZ2luZSB7XG4gIC8qKlxuICAgKiBXZSBjaG9vc2Ugb3B0IG91dCBhcyBtb3N0IG5vZGUgdHlwZXMgc2hvdWxkIGJlIHNlYXJjaGVkIChlLmcuIHNjcmlwdCkuXG4gICAqIEV2ZW4gbm9kZXMgbGlrZSA8ZGF0YT4sIGNvdWxkIGhhdmUgdGV4dENvbnRlbnQgd2UgY2FyZSBhYm91dC5cbiAgICpcbiAgICogTm90ZTogbm9kZU5hbWUgaXMgY2FwaXRhbGl6ZWQsIHNvIHdlIGRvIHRoZSBzYW1lIGhlcmVcbiAgICovXG4gIHN0YXRpYyBVTlNVUFBPUlRFRF9FTEVNRU5UUyA9IHtcbiAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9IVE1ML0VsZW1lbnQjRG9jdW1lbnRfbWV0YWRhdGFcbiAgICBCQVNFOiB0cnVlLFxuICAgIEhFQUQ6IHRydWUsXG4gICAgTElOSzogdHJ1ZSxcbiAgICBNRVRBOiB0cnVlLFxuICAgIFNUWUxFOiB0cnVlLFxuICAgIFRJVExFOiB0cnVlLFxuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNTZWN0aW9uaW5nX3Jvb3RcbiAgICBCT0RZOiB0cnVlLFxuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNDb250ZW50X3NlY3Rpb25pbmdcbiAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9IVE1ML0VsZW1lbnQjVGV4dF9jb250ZW50XG4gICAgLy8gaHR0cHM6Ly9kZXZlbG9wZXIubW96aWxsYS5vcmcvZW4tVVMvZG9jcy9XZWIvSFRNTC9FbGVtZW50I0lubGluZV90ZXh0X3NlbWFudGljc1xuICAgIC8vIEFib3ZlIGlzIHNlYXJjaGVkXG4gICAgLy8gaHR0cHM6Ly9kZXZlbG9wZXIubW96aWxsYS5vcmcvZW4tVVMvZG9jcy9XZWIvSFRNTC9FbGVtZW50I0ltYWdlX2FuZF9tdWx0aW1lZGlhXG4gICAgQVJFQTogdHJ1ZSxcbiAgICBBVURJTzogdHJ1ZSxcbiAgICBJTUc6IHRydWUsXG4gICAgTUFQOiB0cnVlLFxuICAgIFRSQUNLOiB0cnVlLFxuICAgIFZJREVPOiB0cnVlLFxuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNFbWJlZGRlZF9jb250ZW50XG4gICAgQVBQTEVUOiB0cnVlLFxuICAgIEVNQkVEOiB0cnVlLFxuICAgIElGUkFNRTogdHJ1ZSxcbiAgICBOT0VNQkVEOiB0cnVlLFxuICAgIE9CSkVDVDogdHJ1ZSxcbiAgICBQQVJBTTogdHJ1ZSxcbiAgICBQSUNUVVJFOiB0cnVlLFxuICAgIFNPVVJDRTogdHJ1ZSxcbiAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9IVE1ML0VsZW1lbnQjU2NyaXB0aW5nXG4gICAgQ0FOVkFTOiB0cnVlLFxuICAgIE5PU0NSSVBUOiB0cnVlLFxuICAgIFNDUklQVDogdHJ1ZSxcbiAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9IVE1ML0VsZW1lbnQjRGVtYXJjYXRpbmdfZWRpdHNcbiAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9IVE1ML0VsZW1lbnQjVGFibGVfY29udGVudFxuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNGb3Jtc1xuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNJbnRlcmFjdGl2ZV9lbGVtZW50c1xuICAgIC8vIGh0dHBzOi8vZGV2ZWxvcGVyLm1vemlsbGEub3JnL2VuLVVTL2RvY3MvV2ViL0hUTUwvRWxlbWVudCNXZWJfQ29tcG9uZW50c1xuICAgIC8vIEFib3ZlIGlzIHNlYXJjaGVkXG4gICAgLy8gT3RoZXI6XG4gICAgU1ZHOiB0cnVlXG4gIH07XG5cbiAgLyoqXG4gICAqIFNlYXJjaCBmb3IgYSBgcXVlcnlgIGluIGEgRE9NIHRyZWUuXG4gICAqXG4gICAqIEBwYXJhbSBxdWVyeSBSZWd1bGFyIGV4cHJlc3Npb24gdG8gc2VhcmNoXG4gICAqIEBwYXJhbSByb290Tm9kZSBET00gcm9vdCBub2RlIHRvIHNlYXJjaCBpblxuICAgKiBAcmV0dXJucyBUaGUgbGlzdCBvZiBtYXRjaGVzXG4gICAqL1xuICBzdGF0aWMgc2VhcmNoKHF1ZXJ5OiBSZWdFeHAsIHJvb3ROb2RlOiBOb2RlKTogUHJvbWlzZTxJSFRNTFNlYXJjaE1hdGNoW10+IHtcbiAgICBpZiAoIShyb290Tm9kZSBpbnN0YW5jZW9mIE5vZGUpKSB7XG4gICAgICBjb25zb2xlLndhcm4oXG4gICAgICAgICdVbmFibGUgdG8gc2VhcmNoIHdpdGggSFRNTFNlYXJjaEVuZ2luZSB0aGUgcHJvdmlkZWQgb2JqZWN0LicsXG4gICAgICAgIHJvb3ROb2RlXG4gICAgICApO1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShbXSk7XG4gICAgfVxuXG4gICAgaWYgKCFxdWVyeS5nbG9iYWwpIHtcbiAgICAgIHF1ZXJ5ID0gbmV3IFJlZ0V4cChxdWVyeS5zb3VyY2UsIHF1ZXJ5LmZsYWdzICsgJ2cnKTtcbiAgICB9XG5cbiAgICBjb25zdCBtYXRjaGVzOiBJSFRNTFNlYXJjaE1hdGNoW10gPSBbXTtcbiAgICBjb25zdCB3YWxrZXIgPSBkb2N1bWVudC5jcmVhdGVUcmVlV2Fsa2VyKHJvb3ROb2RlLCBOb2RlRmlsdGVyLlNIT1dfVEVYVCwge1xuICAgICAgYWNjZXB0Tm9kZTogbm9kZSA9PiB7XG4gICAgICAgIC8vIEZpbHRlciBzdWJ0cmVlcyBvZiBVTlNVUFBPUlRFRF9FTEVNRU5UUyBhbmQgbm9kZXMgdGhhdFxuICAgICAgICAvLyBkbyBub3QgY29udGFpbiBvdXIgc2VhcmNoIHRleHRcbiAgICAgICAgbGV0IHBhcmVudEVsZW1lbnQgPSBub2RlLnBhcmVudEVsZW1lbnQhO1xuICAgICAgICB3aGlsZSAocGFyZW50RWxlbWVudCAhPT0gcm9vdE5vZGUpIHtcbiAgICAgICAgICBpZiAocGFyZW50RWxlbWVudC5ub2RlTmFtZSBpbiBIVE1MU2VhcmNoRW5naW5lLlVOU1VQUE9SVEVEX0VMRU1FTlRTKSB7XG4gICAgICAgICAgICByZXR1cm4gTm9kZUZpbHRlci5GSUxURVJfUkVKRUNUO1xuICAgICAgICAgIH1cbiAgICAgICAgICBwYXJlbnRFbGVtZW50ID0gcGFyZW50RWxlbWVudC5wYXJlbnRFbGVtZW50ITtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gcXVlcnkudGVzdChub2RlLnRleHRDb250ZW50ISlcbiAgICAgICAgICA/IE5vZGVGaWx0ZXIuRklMVEVSX0FDQ0VQVFxuICAgICAgICAgIDogTm9kZUZpbHRlci5GSUxURVJfUkVKRUNUO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgbGV0IG5vZGU6IE5vZGUgfCBudWxsID0gbnVsbDtcbiAgICB3aGlsZSAoKG5vZGUgPSB3YWxrZXIubmV4dE5vZGUoKSkgIT09IG51bGwpIHtcbiAgICAgIC8vIFJlc2V0IHF1ZXJ5IGluZGV4XG4gICAgICBxdWVyeS5sYXN0SW5kZXggPSAwO1xuICAgICAgbGV0IG1hdGNoOiBSZWdFeHBFeGVjQXJyYXkgfCBudWxsID0gbnVsbDtcbiAgICAgIHdoaWxlICgobWF0Y2ggPSBxdWVyeS5leGVjKG5vZGUudGV4dENvbnRlbnQhKSkgIT09IG51bGwpIHtcbiAgICAgICAgbWF0Y2hlcy5wdXNoKHtcbiAgICAgICAgICB0ZXh0OiBtYXRjaFswXSxcbiAgICAgICAgICBwb3NpdGlvbjogbWF0Y2guaW5kZXgsXG4gICAgICAgICAgbm9kZTogbm9kZSBhcyBUZXh0XG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cblxuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUobWF0Y2hlcyk7XG4gIH1cbn1cblxuLyoqXG4gKiBHZW5lcmljIERPTSB0cmVlIHNlYXJjaCBwcm92aWRlci5cbiAqL1xuZXhwb3J0IGNsYXNzIEdlbmVyaWNTZWFyY2hQcm92aWRlciBleHRlbmRzIFNlYXJjaFByb3ZpZGVyPFdpZGdldD4ge1xuICAvKipcbiAgICogUmVwb3J0IHdoZXRoZXIgb3Igbm90IHRoaXMgcHJvdmlkZXIgaGFzIHRoZSBhYmlsaXR5IHRvIHNlYXJjaCBvbiB0aGUgZ2l2ZW4gb2JqZWN0XG4gICAqL1xuICBzdGF0aWMgaXNBcHBsaWNhYmxlKGRvbWFpbjogV2lkZ2V0KTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIGRvbWFpbiBpbnN0YW5jZW9mIFdpZGdldDtcbiAgfVxuXG4gIC8qKlxuICAgKiBJbnN0YW50aWF0ZSBhIGdlbmVyaWMgc2VhcmNoIHByb3ZpZGVyIGZvciB0aGUgd2lkZ2V0LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoZSB3aWRnZXQgcHJvdmlkZWQgaXMgYWx3YXlzIGNoZWNrZWQgdXNpbmcgYGlzQXBwbGljYWJsZWAgYmVmb3JlIGNhbGxpbmdcbiAgICogdGhpcyBmYWN0b3J5LlxuICAgKlxuICAgKiBAcGFyYW0gd2lkZ2V0IFRoZSB3aWRnZXQgdG8gc2VhcmNoIG9uXG4gICAqIEBwYXJhbSByZWdpc3RyeSBUaGUgc2VhcmNoIHByb3ZpZGVyIHJlZ2lzdHJ5XG4gICAqIEBwYXJhbSB0cmFuc2xhdG9yIFtvcHRpb25hbF0gVGhlIHRyYW5zbGF0b3Igb2JqZWN0XG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBzZWFyY2ggcHJvdmlkZXIgb24gdGhlIHdpZGdldFxuICAgKi9cbiAgc3RhdGljIGNyZWF0ZU5ldyhcbiAgICB3aWRnZXQ6IFdpZGdldCxcbiAgICByZWdpc3RyeTogSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yXG4gICk6IElTZWFyY2hQcm92aWRlciB7XG4gICAgcmV0dXJuIG5ldyBHZW5lcmljU2VhcmNoUHJvdmlkZXIod2lkZ2V0KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY3VycmVudCBpbmRleCBvZiB0aGUgc2VsZWN0ZWQgbWF0Y2guXG4gICAqL1xuICBnZXQgY3VycmVudE1hdGNoSW5kZXgoKTogbnVtYmVyIHwgbnVsbCB7XG4gICAgcmV0dXJuIHRoaXMuX2N1cnJlbnRNYXRjaEluZGV4ID49IDAgPyB0aGlzLl9jdXJyZW50TWF0Y2hJbmRleCA6IG51bGw7XG4gIH1cblxuICAvKipcbiAgICogVGhlIGN1cnJlbnQgbWF0Y2hcbiAgICovXG4gIGdldCBjdXJyZW50TWF0Y2goKTogSUhUTUxTZWFyY2hNYXRjaCB8IG51bGwge1xuICAgIHJldHVybiB0aGlzLl9tYXRjaGVzW3RoaXMuX2N1cnJlbnRNYXRjaEluZGV4XSA/PyBudWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBjdXJyZW50IG1hdGNoZXNcbiAgICovXG4gIGdldCBtYXRjaGVzKCk6IElIVE1MU2VhcmNoTWF0Y2hbXSB7XG4gICAgLy8gRW5zdXJlIHRoYXQgbm8gb3RoZXIgZm4gY2FuIG92ZXJ3cml0ZSBtYXRjaGVzIGluZGV4IHByb3BlcnR5XG4gICAgLy8gV2Ugc2hhbGxvdyBjbG9uZSBlYWNoIG5vZGVcbiAgICByZXR1cm4gdGhpcy5fbWF0Y2hlc1xuICAgICAgPyB0aGlzLl9tYXRjaGVzLm1hcChtID0+IE9iamVjdC5hc3NpZ24oe30sIG0pKVxuICAgICAgOiB0aGlzLl9tYXRjaGVzO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBudW1iZXIgb2YgbWF0Y2hlcy5cbiAgICovXG4gIGdldCBtYXRjaGVzQ291bnQoKTogbnVtYmVyIHwgbnVsbCB7XG4gICAgcmV0dXJuIHRoaXMuX21hdGNoZXMubGVuZ3RoO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0byB0cnVlIGlmIHRoZSB3aWRnZXQgdW5kZXIgc2VhcmNoIGlzIHJlYWQtb25seSwgZmFsc2VcbiAgICogaWYgaXQgaXMgZWRpdGFibGUuICBXaWxsIGJlIHVzZWQgdG8gZGV0ZXJtaW5lIHdoZXRoZXIgdG8gc2hvd1xuICAgKiB0aGUgcmVwbGFjZSBvcHRpb24uXG4gICAqL1xuICByZWFkb25seSBpc1JlYWRPbmx5ID0gdHJ1ZTtcblxuICAvKipcbiAgICogQ2xlYXIgY3VycmVudGx5IGhpZ2hsaWdodGVkIG1hdGNoLlxuICAgKi9cbiAgY2xlYXJIaWdobGlnaHQoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgaWYgKHRoaXMuX2N1cnJlbnRNYXRjaEluZGV4ID49IDApIHtcbiAgICAgIGNvbnN0IGhpdCA9IHRoaXMuX21hcmtOb2Rlc1t0aGlzLl9jdXJyZW50TWF0Y2hJbmRleF07XG4gICAgICBoaXQuY2xhc3NMaXN0LnJlbW92ZSguLi5TRUxFQ1RFRF9DTEFTU0VTKTtcbiAgICB9XG4gICAgdGhpcy5fY3VycmVudE1hdGNoSW5kZXggPSAtMTtcblxuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGUgc2VhcmNoIHByb3ZpZGVyLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIElmIHRoZSBvYmplY3QncyBgZGlzcG9zZWAgbWV0aG9kIGlzIGNhbGxlZCBtb3JlIHRoYW4gb25jZSwgYWxsXG4gICAqIGNhbGxzIG1hZGUgYWZ0ZXIgdGhlIGZpcnN0IHdpbGwgYmUgYSBuby1vcC5cbiAgICpcbiAgICogIyMjIyBVbmRlZmluZWQgQmVoYXZpb3JcbiAgICogSXQgaXMgdW5kZWZpbmVkIGJlaGF2aW9yIHRvIHVzZSBhbnkgZnVuY3Rpb25hbGl0eSBvZiB0aGUgb2JqZWN0XG4gICAqIGFmdGVyIGl0IGhhcyBiZWVuIGRpc3Bvc2VkIHVubGVzcyBvdGhlcndpc2UgZXhwbGljaXRseSBub3RlZC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMuZW5kUXVlcnkoKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIGVuZCBzZWFyY2ggcXVlcnkuYCwgcmVhc29uKTtcbiAgICB9KTtcbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogTW92ZSB0aGUgY3VycmVudCBtYXRjaCBpbmRpY2F0b3IgdG8gdGhlIG5leHQgbWF0Y2guXG4gICAqXG4gICAqIEBwYXJhbSBsb29wIFdoZXRoZXIgdG8gbG9vcCB3aXRoaW4gdGhlIG1hdGNoZXMgbGlzdC5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgb25jZSB0aGUgYWN0aW9uIGhhcyBjb21wbGV0ZWQuXG4gICAqL1xuICBhc3luYyBoaWdobGlnaHROZXh0KGxvb3A/OiBib29sZWFuKTogUHJvbWlzZTxJSFRNTFNlYXJjaE1hdGNoIHwgdW5kZWZpbmVkPiB7XG4gICAgcmV0dXJuIHRoaXMuX2hpZ2hsaWdodE5leHQoZmFsc2UsIGxvb3AgPz8gdHJ1ZSkgPz8gdW5kZWZpbmVkO1xuICB9XG5cbiAgLyoqXG4gICAqIE1vdmUgdGhlIGN1cnJlbnQgbWF0Y2ggaW5kaWNhdG9yIHRvIHRoZSBwcmV2aW91cyBtYXRjaC5cbiAgICpcbiAgICogQHBhcmFtIGxvb3AgV2hldGhlciB0byBsb29wIHdpdGhpbiB0aGUgbWF0Y2hlcyBsaXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyBvbmNlIHRoZSBhY3Rpb24gaGFzIGNvbXBsZXRlZC5cbiAgICovXG4gIGFzeW5jIGhpZ2hsaWdodFByZXZpb3VzKFxuICAgIGxvb3A/OiBib29sZWFuXG4gICk6IFByb21pc2U8SUhUTUxTZWFyY2hNYXRjaCB8IHVuZGVmaW5lZD4ge1xuICAgIHJldHVybiB0aGlzLl9oaWdobGlnaHROZXh0KHRydWUsIGxvb3AgPz8gdHJ1ZSkgPz8gdW5kZWZpbmVkO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlcGxhY2UgdGhlIGN1cnJlbnRseSBzZWxlY3RlZCBtYXRjaCB3aXRoIHRoZSBwcm92aWRlZCB0ZXh0XG4gICAqXG4gICAqIEBwYXJhbSBuZXdUZXh0IFRoZSByZXBsYWNlbWVudCB0ZXh0XG4gICAqIEBwYXJhbSBsb29wIFdoZXRoZXIgdG8gbG9vcCB3aXRoaW4gdGhlIG1hdGNoZXMgbGlzdC5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2l0aCBhIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcmVwbGFjZSBvY2N1cnJlZC5cbiAgICovXG4gIGFzeW5jIHJlcGxhY2VDdXJyZW50TWF0Y2gobmV3VGV4dDogc3RyaW5nLCBsb29wPzogYm9vbGVhbik6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUoZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlcGxhY2UgYWxsIG1hdGNoZXMgaW4gdGhlIG5vdGVib29rIHdpdGggdGhlIHByb3ZpZGVkIHRleHRcbiAgICpcbiAgICogQHBhcmFtIG5ld1RleHQgVGhlIHJlcGxhY2VtZW50IHRleHRcbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2l0aCBhIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcmVwbGFjZSBvY2N1cnJlZC5cbiAgICovXG4gIGFzeW5jIHJlcGxhY2VBbGxNYXRjaGVzKG5ld1RleHQ6IHN0cmluZyk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgIC8vIFRoaXMgaXMgcmVhZCBvbmx5LCBidXQgd2UgY291bGQgbG9vc2VuIHRoaXMgaW4gdGhlb3J5IGZvciBpbnB1dCBib3hlcy4uLlxuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUoZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluaXRpYWxpemUgdGhlIHNlYXJjaCB1c2luZyB0aGUgcHJvdmlkZWQgb3B0aW9ucy4gIFNob3VsZCB1cGRhdGUgdGhlIFVJXG4gICAqIHRvIGhpZ2hsaWdodCBhbGwgbWF0Y2hlcyBhbmQgXCJzZWxlY3RcIiB3aGF0ZXZlciB0aGUgZmlyc3QgbWF0Y2ggc2hvdWxkIGJlLlxuICAgKlxuICAgKiBAcGFyYW0gcXVlcnkgQSBSZWdFeHAgdG8gYmUgdXNlIHRvIHBlcmZvcm0gdGhlIHNlYXJjaFxuICAgKiBAcGFyYW0gZmlsdGVycyBGaWx0ZXIgcGFyYW1ldGVycyB0byBwYXNzIHRvIHByb3ZpZGVyXG4gICAqL1xuICBhc3luYyBzdGFydFF1ZXJ5KHF1ZXJ5OiBSZWdFeHAgfCBudWxsLCBmaWx0ZXJzID0ge30pOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBhd2FpdCB0aGlzLmVuZFF1ZXJ5KCk7XG4gICAgdGhpcy5fcXVlcnkgPSBxdWVyeTtcblxuICAgIGlmIChxdWVyeSA9PT0gbnVsbCkge1xuICAgICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZSgpO1xuICAgIH1cblxuICAgIGNvbnN0IG1hdGNoZXMgPSBhd2FpdCBIVE1MU2VhcmNoRW5naW5lLnNlYXJjaChxdWVyeSwgdGhpcy53aWRnZXQubm9kZSk7XG5cbiAgICAvLyBUcmFuc2Zvcm0gdGhlIERPTVxuICAgIGxldCBub2RlSWR4ID0gMDtcbiAgICB3aGlsZSAobm9kZUlkeCA8IG1hdGNoZXMubGVuZ3RoKSB7XG4gICAgICBsZXQgYWN0aXZlTm9kZSA9IG1hdGNoZXNbbm9kZUlkeF0ubm9kZTtcbiAgICAgIGxldCBwYXJlbnQgPSBhY3RpdmVOb2RlLnBhcmVudE5vZGUhO1xuXG4gICAgICBsZXQgc3ViTWF0Y2hlcyA9IFttYXRjaGVzW25vZGVJZHhdXTtcbiAgICAgIHdoaWxlIChcbiAgICAgICAgKytub2RlSWR4IDwgbWF0Y2hlcy5sZW5ndGggJiZcbiAgICAgICAgbWF0Y2hlc1tub2RlSWR4XS5ub2RlID09PSBhY3RpdmVOb2RlXG4gICAgICApIHtcbiAgICAgICAgc3ViTWF0Y2hlcy51bnNoaWZ0KG1hdGNoZXNbbm9kZUlkeF0pO1xuICAgICAgfVxuXG4gICAgICBjb25zdCBtYXJrZWROb2RlcyA9IHN1Yk1hdGNoZXMubWFwKG1hdGNoID0+IHtcbiAgICAgICAgLy8gVE9ETzogc3VwcG9ydCB0c3BhbiBmb3Igc3ZnIHdoZW4gc3ZnIHN1cHBvcnQgaXMgYWRkZWRcbiAgICAgICAgY29uc3QgbWFya2VkTm9kZSA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ21hcmsnKTtcbiAgICAgICAgbWFya2VkTm9kZS5jbGFzc0xpc3QuYWRkKC4uLkZPVU5EX0NMQVNTRVMpO1xuICAgICAgICBtYXJrZWROb2RlLnRleHRDb250ZW50ID0gbWF0Y2gudGV4dDtcblxuICAgICAgICBjb25zdCBuZXdOb2RlID0gYWN0aXZlTm9kZS5zcGxpdFRleHQobWF0Y2gucG9zaXRpb24pO1xuICAgICAgICBuZXdOb2RlLnRleHRDb250ZW50ID0gbmV3Tm9kZS50ZXh0Q29udGVudCEuc2xpY2UobWF0Y2gudGV4dC5sZW5ndGgpO1xuICAgICAgICBwYXJlbnQuaW5zZXJ0QmVmb3JlKG1hcmtlZE5vZGUsIG5ld05vZGUpO1xuICAgICAgICByZXR1cm4gbWFya2VkTm9kZTtcbiAgICAgIH0pO1xuXG4gICAgICAvLyBJbnNlcnQgbm9kZSBpbiByZXZlcnNlIG9yZGVyIGFzIHdlIHJlcGxhY2UgZnJvbSBsYXN0IHRvIGZpcnN0XG4gICAgICAvLyB0byBtYWludGFpbiBtYXRjaCBwb3NpdGlvbi5cbiAgICAgIGZvciAobGV0IGkgPSBtYXJrZWROb2Rlcy5sZW5ndGggLSAxOyBpID49IDA7IGktLSkge1xuICAgICAgICB0aGlzLl9tYXJrTm9kZXMucHVzaChtYXJrZWROb2Rlc1tpXSk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgLy8gV2F0Y2ggZm9yIGZ1dHVyZSBjaGFuZ2VzOlxuICAgIHRoaXMuX211dGF0aW9uT2JzZXJ2ZXIub2JzZXJ2ZShcbiAgICAgIHRoaXMud2lkZ2V0Lm5vZGUsXG4gICAgICAvLyBodHRwczovL2RldmVsb3Blci5tb3ppbGxhLm9yZy9lbi1VUy9kb2NzL1dlYi9BUEkvTXV0YXRpb25PYnNlcnZlckluaXRcbiAgICAgIHtcbiAgICAgICAgYXR0cmlidXRlczogZmFsc2UsXG4gICAgICAgIGNoYXJhY3RlckRhdGE6IHRydWUsXG4gICAgICAgIGNoaWxkTGlzdDogdHJ1ZSxcbiAgICAgICAgc3VidHJlZTogdHJ1ZVxuICAgICAgfVxuICAgICk7XG5cbiAgICB0aGlzLl9tYXRjaGVzID0gbWF0Y2hlcztcbiAgfVxuXG4gIC8qKlxuICAgKiBDbGVhciB0aGUgaGlnaGxpZ2h0ZWQgbWF0Y2hlcyBhbmQgYW55IGludGVybmFsIHN0YXRlLlxuICAgKi9cbiAgYXN5bmMgZW5kUXVlcnkoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgdGhpcy5fbXV0YXRpb25PYnNlcnZlci5kaXNjb25uZWN0KCk7XG4gICAgdGhpcy5fbWFya05vZGVzLmZvckVhY2goZWwgPT4ge1xuICAgICAgY29uc3QgcGFyZW50ID0gZWwucGFyZW50Tm9kZSE7XG4gICAgICBwYXJlbnQucmVwbGFjZUNoaWxkKGRvY3VtZW50LmNyZWF0ZVRleHROb2RlKGVsLnRleHRDb250ZW50ISksIGVsKTtcbiAgICAgIHBhcmVudC5ub3JtYWxpemUoKTtcbiAgICB9KTtcbiAgICB0aGlzLl9tYXJrTm9kZXMgPSBbXTtcbiAgICB0aGlzLl9tYXRjaGVzID0gW107XG4gICAgdGhpcy5fY3VycmVudE1hdGNoSW5kZXggPSAtMTtcbiAgfVxuXG4gIHByaXZhdGUgX2hpZ2hsaWdodE5leHQoXG4gICAgcmV2ZXJzZTogYm9vbGVhbixcbiAgICBsb29wOiBib29sZWFuXG4gICk6IElIVE1MU2VhcmNoTWF0Y2ggfCBudWxsIHtcbiAgICBpZiAodGhpcy5fbWF0Y2hlcy5sZW5ndGggPT09IDApIHtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbiAgICBpZiAodGhpcy5fY3VycmVudE1hdGNoSW5kZXggPT09IC0xKSB7XG4gICAgICB0aGlzLl9jdXJyZW50TWF0Y2hJbmRleCA9IHJldmVyc2UgPyB0aGlzLm1hdGNoZXMubGVuZ3RoIC0gMSA6IDA7XG4gICAgfSBlbHNlIHtcbiAgICAgIGNvbnN0IGhpdCA9IHRoaXMuX21hcmtOb2Rlc1t0aGlzLl9jdXJyZW50TWF0Y2hJbmRleF07XG4gICAgICBoaXQuY2xhc3NMaXN0LnJlbW92ZSguLi5TRUxFQ1RFRF9DTEFTU0VTKTtcblxuICAgICAgdGhpcy5fY3VycmVudE1hdGNoSW5kZXggPSByZXZlcnNlXG4gICAgICAgID8gdGhpcy5fY3VycmVudE1hdGNoSW5kZXggLSAxXG4gICAgICAgIDogdGhpcy5fY3VycmVudE1hdGNoSW5kZXggKyAxO1xuICAgICAgaWYgKFxuICAgICAgICBsb29wICYmXG4gICAgICAgICh0aGlzLl9jdXJyZW50TWF0Y2hJbmRleCA8IDAgfHxcbiAgICAgICAgICB0aGlzLl9jdXJyZW50TWF0Y2hJbmRleCA+PSB0aGlzLl9tYXRjaGVzLmxlbmd0aClcbiAgICAgICkge1xuICAgICAgICAvLyBDaGVhcCB3YXkgdG8gbWFrZSB0aGlzIGEgY2lyY3VsYXIgYnVmZmVyXG4gICAgICAgIHRoaXMuX2N1cnJlbnRNYXRjaEluZGV4ID1cbiAgICAgICAgICAodGhpcy5fY3VycmVudE1hdGNoSW5kZXggKyB0aGlzLl9tYXRjaGVzLmxlbmd0aCkgJVxuICAgICAgICAgIHRoaXMuX21hdGNoZXMubGVuZ3RoO1xuICAgICAgfVxuICAgIH1cblxuICAgIGlmIChcbiAgICAgIHRoaXMuX2N1cnJlbnRNYXRjaEluZGV4ID49IDAgJiZcbiAgICAgIHRoaXMuX2N1cnJlbnRNYXRjaEluZGV4IDwgdGhpcy5fbWF0Y2hlcy5sZW5ndGhcbiAgICApIHtcbiAgICAgIGNvbnN0IGhpdCA9IHRoaXMuX21hcmtOb2Rlc1t0aGlzLl9jdXJyZW50TWF0Y2hJbmRleF07XG4gICAgICBoaXQuY2xhc3NMaXN0LmFkZCguLi5TRUxFQ1RFRF9DTEFTU0VTKTtcbiAgICAgIC8vIElmIG5vdCBpbiB2aWV3LCBzY3JvbGwganVzdCBlbm91Z2ggdG8gc2VlIGl0XG4gICAgICBpZiAoIWVsZW1lbnRJblZpZXdwb3J0KGhpdCkpIHtcbiAgICAgICAgaGl0LnNjcm9sbEludG9WaWV3KHJldmVyc2UpO1xuICAgICAgfVxuICAgICAgaGl0LmZvY3VzKCk7XG5cbiAgICAgIHJldHVybiB0aGlzLl9tYXRjaGVzW3RoaXMuX2N1cnJlbnRNYXRjaEluZGV4XTtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5fY3VycmVudE1hdGNoSW5kZXggPSAtMTtcbiAgICAgIHJldHVybiBudWxsO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgYXN5bmMgX29uV2lkZ2V0Q2hhbmdlZChcbiAgICBtdXRhdGlvbnM6IE11dGF0aW9uUmVjb3JkW10sXG4gICAgb2JzZXJ2ZXI6IE11dGF0aW9uT2JzZXJ2ZXJcbiAgKSB7XG4gICAgdGhpcy5fY3VycmVudE1hdGNoSW5kZXggPSAtMTtcbiAgICAvLyBUaGlzIGlzIHR5cGljYWxseSBjaGVhcCwgYnV0IHdlIGRvIG5vdCBjb250cm9sIHRoZSByYXRlIG9mIGNoYW5nZSBvciBzaXplIG9mIHRoZSBvdXRwdXRcbiAgICBhd2FpdCB0aGlzLnN0YXJ0UXVlcnkodGhpcy5fcXVlcnkpO1xuICAgIHRoaXMuX3N0YXRlQ2hhbmdlZC5lbWl0KCk7XG4gIH1cblxuICBwcml2YXRlIF9xdWVyeTogUmVnRXhwIHwgbnVsbDtcbiAgcHJpdmF0ZSBfY3VycmVudE1hdGNoSW5kZXg6IG51bWJlcjtcbiAgcHJpdmF0ZSBfbWF0Y2hlczogSUhUTUxTZWFyY2hNYXRjaFtdID0gW107XG4gIHByaXZhdGUgX211dGF0aW9uT2JzZXJ2ZXI6IE11dGF0aW9uT2JzZXJ2ZXIgPSBuZXcgTXV0YXRpb25PYnNlcnZlcihcbiAgICB0aGlzLl9vbldpZGdldENoYW5nZWQuYmluZCh0aGlzKVxuICApO1xuICBwcml2YXRlIF9tYXJrTm9kZXMgPSBuZXcgQXJyYXk8SFRNTFNwYW5FbGVtZW50PigpO1xufVxuXG5mdW5jdGlvbiBlbGVtZW50SW5WaWV3cG9ydChlbDogSFRNTEVsZW1lbnQpOiBib29sZWFuIHtcbiAgY29uc3QgYm91bmRpbmdDbGllbnRSZWN0ID0gZWwuZ2V0Qm91bmRpbmdDbGllbnRSZWN0KCk7XG4gIHJldHVybiAoXG4gICAgYm91bmRpbmdDbGllbnRSZWN0LnRvcCA+PSAwICYmXG4gICAgYm91bmRpbmdDbGllbnRSZWN0LmJvdHRvbSA8PVxuICAgICAgKHdpbmRvdy5pbm5lckhlaWdodCB8fCBkb2N1bWVudC5kb2N1bWVudEVsZW1lbnQuY2xpZW50SGVpZ2h0KSAmJlxuICAgIGJvdW5kaW5nQ2xpZW50UmVjdC5sZWZ0ID49IDAgJiZcbiAgICBib3VuZGluZ0NsaWVudFJlY3QucmlnaHQgPD1cbiAgICAgICh3aW5kb3cuaW5uZXJXaWR0aCB8fCBkb2N1bWVudC5kb2N1bWVudEVsZW1lbnQuY2xpZW50V2lkdGgpXG4gICk7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZWFyY2hNYXRjaCB9IGZyb20gJy4uL3Rva2Vucyc7XG5cbi8qKlxuICogU2VhcmNoIHByb3ZpZGVyIGZvciB0ZXh0L3BsYWluXG4gKi9cbmV4cG9ydCBjb25zdCBUZXh0U2VhcmNoRW5naW5lID0ge1xuICAvKipcbiAgICogU2VhcmNoIGZvciByZWd1bGFyIGV4cHJlc3Npb24gbWF0Y2hlcyBpbiBhIHN0cmluZy5cbiAgICpcbiAgICogQHBhcmFtIHF1ZXJ5IFF1ZXJ5IHJlZ3VsYXIgZXhwcmVzc2lvblxuICAgKiBAcGFyYW0gZGF0YSBTdHJpbmcgdG8gbG9vayBpbnRvXG4gICAqIEByZXR1cm5zIExpc3Qgb2YgbWF0Y2hlc1xuICAgKi9cbiAgc2VhcmNoKHF1ZXJ5OiBSZWdFeHAsIGRhdGE6IHN0cmluZyk6IFByb21pc2U8SVNlYXJjaE1hdGNoW10+IHtcbiAgICAvLyBJZiBkYXRhIGlzIG5vdCBhIHN0cmluZywgdHJ5IHRvIEpTT04gc2VyaWFsaXplIHRoZSBkYXRhLlxuICAgIGlmICh0eXBlb2YgZGF0YSAhPT0gJ3N0cmluZycpIHtcbiAgICAgIHRyeSB7XG4gICAgICAgIGRhdGEgPSBKU09OLnN0cmluZ2lmeShkYXRhKTtcbiAgICAgIH0gY2F0Y2ggKHJlYXNvbikge1xuICAgICAgICBjb25zb2xlLndhcm4oXG4gICAgICAgICAgJ1VuYWJsZSB0byBzZWFyY2ggd2l0aCBUZXh0U2VhcmNoRW5naW5lIG5vbi1KU09OIHNlcmlhbGl6YWJsZSBvYmplY3QuJyxcbiAgICAgICAgICByZWFzb24sXG4gICAgICAgICAgZGF0YVxuICAgICAgICApO1xuICAgICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKFtdKTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICBpZiAoIXF1ZXJ5Lmdsb2JhbCkge1xuICAgICAgcXVlcnkgPSBuZXcgUmVnRXhwKHF1ZXJ5LnNvdXJjZSwgcXVlcnkuZmxhZ3MgKyAnZycpO1xuICAgIH1cblxuICAgIGNvbnN0IG1hdGNoZXMgPSBuZXcgQXJyYXk8SVNlYXJjaE1hdGNoPigpO1xuXG4gICAgbGV0IG1hdGNoOiBSZWdFeHBFeGVjQXJyYXkgfCBudWxsID0gbnVsbDtcbiAgICB3aGlsZSAoKG1hdGNoID0gcXVlcnkuZXhlYyhkYXRhKSkgIT09IG51bGwpIHtcbiAgICAgIG1hdGNoZXMucHVzaCh7XG4gICAgICAgIHRleHQ6IG1hdGNoWzBdLFxuICAgICAgICBwb3NpdGlvbjogbWF0Y2guaW5kZXhcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUobWF0Y2hlcyk7XG4gIH1cbn07XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFZEb21Nb2RlbCB9IGZyb20gJ0BqdXB5dGVybGFiL3VpLWNvbXBvbmVudHMnO1xuaW1wb3J0IHsgSlNPTkV4dCB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IElPYnNlcnZhYmxlRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBEZWJvdW5jZXIgfSBmcm9tICdAbHVtaW5vL3BvbGxpbmcnO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgSUZpbHRlciwgSUZpbHRlcnMsIElTZWFyY2hQcm92aWRlciB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBTZWFyY2ggaW4gYSBkb2N1bWVudCBtb2RlbC5cbiAqL1xuZXhwb3J0IGNsYXNzIFNlYXJjaERvY3VtZW50TW9kZWxcbiAgZXh0ZW5kcyBWRG9tTW9kZWxcbiAgaW1wbGVtZW50cyBJT2JzZXJ2YWJsZURpc3Bvc2FibGVcbntcbiAgLyoqXG4gICAqIFNlYXJjaCBkb2N1bWVudCBtb2RlbFxuICAgKiBAcGFyYW0gc2VhcmNoUHJvdmlkZXIgUHJvdmlkZXIgZm9yIHRoZSBjdXJyZW50IGRvY3VtZW50XG4gICAqIEBwYXJhbSBzZWFyY2hEZWJvdW5jZVRpbWUgRGVib3VuY2Ugc2VhcmNoIHRpbWVcbiAgICovXG4gIGNvbnN0cnVjdG9yKFxuICAgIHByb3RlY3RlZCBzZWFyY2hQcm92aWRlcjogSVNlYXJjaFByb3ZpZGVyLFxuICAgIHNlYXJjaERlYm91bmNlVGltZTogbnVtYmVyXG4gICkge1xuICAgIHN1cGVyKCk7XG5cbiAgICB0aGlzLl9maWx0ZXJzID0ge307XG4gICAgaWYgKHRoaXMuc2VhcmNoUHJvdmlkZXIuZ2V0RmlsdGVycykge1xuICAgICAgY29uc3QgZmlsdGVycyA9IHRoaXMuc2VhcmNoUHJvdmlkZXIuZ2V0RmlsdGVycygpO1xuICAgICAgZm9yIChjb25zdCBmaWx0ZXIgaW4gZmlsdGVycykge1xuICAgICAgICB0aGlzLl9maWx0ZXJzW2ZpbHRlcl0gPSBmaWx0ZXJzW2ZpbHRlcl0uZGVmYXVsdDtcbiAgICAgIH1cbiAgICB9XG5cbiAgICBzZWFyY2hQcm92aWRlci5zdGF0ZUNoYW5nZWQuY29ubmVjdCh0aGlzLnJlZnJlc2gsIHRoaXMpO1xuXG4gICAgdGhpcy5fc2VhcmNoRGVib3VuY2VyID0gbmV3IERlYm91bmNlcigoKSA9PiB7XG4gICAgICB0aGlzLl91cGRhdGVTZWFyY2goKS5jYXRjaChyZWFzb24gPT4ge1xuICAgICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gdXBkYXRlIHNlYXJjaCBvbiBkb2N1bWVudC4nLCByZWFzb24pO1xuICAgICAgfSk7XG4gICAgfSwgc2VhcmNoRGVib3VuY2VUaW1lKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBzZWFyY2ggaXMgY2FzZSBzZW5zaXRpdmUgb3Igbm90LlxuICAgKi9cbiAgZ2V0IGNhc2VTZW5zaXRpdmUoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuX2Nhc2VTZW5zaXRpdmU7XG4gIH1cbiAgc2V0IGNhc2VTZW5zaXRpdmUodjogYm9vbGVhbikge1xuICAgIGlmICh0aGlzLl9jYXNlU2Vuc2l0aXZlICE9PSB2KSB7XG4gICAgICB0aGlzLl9jYXNlU2Vuc2l0aXZlID0gdjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIHRoaXMucmVmcmVzaCgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBDdXJyZW50IGhpZ2hsaWdodGVkIG1hdGNoIGluZGV4LlxuICAgKi9cbiAgZ2V0IGN1cnJlbnRJbmRleCgpOiBudW1iZXIgfCBudWxsIHtcbiAgICByZXR1cm4gdGhpcy5zZWFyY2hQcm92aWRlci5jdXJyZW50TWF0Y2hJbmRleDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIG9iamVjdCBpcyBkaXNwb3NlZC5cbiAgICovXG4gIGdldCBkaXNwb3NlZCgpOiBJU2lnbmFsPHRoaXMsIHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5fZGlzcG9zZWQ7XG4gIH1cblxuICAvKipcbiAgICogRmlsdGVyIHZhbHVlcy5cbiAgICovXG4gIGdldCBmaWx0ZXJzKCk6IElGaWx0ZXJzIHtcbiAgICByZXR1cm4gdGhpcy5fZmlsdGVycztcbiAgfVxuICBzZXQgZmlsdGVycyh2OiBJRmlsdGVycykge1xuICAgIGlmICghSlNPTkV4dC5kZWVwRXF1YWwodGhpcy5fZmlsdGVycywgdikpIHtcbiAgICAgIHRoaXMuX2ZpbHRlcnMgPSB2O1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgICAgdGhpcy5yZWZyZXNoKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIEZpbHRlciBkZWZpbml0aW9ucyBmb3IgdGhlIGN1cnJlbnQgcHJvdmlkZXIuXG4gICAqL1xuICBnZXQgZmlsdGVyc0RlZmluaXRpb24oKTogeyBbbjogc3RyaW5nXTogSUZpbHRlciB9IHtcbiAgICByZXR1cm4gdGhpcy5zZWFyY2hQcm92aWRlci5nZXRGaWx0ZXJzPy4oKSA/PyB7fTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgaW5pdGlhbCBxdWVyeSBzdHJpbmcuXG4gICAqL1xuICBnZXQgaW5pdGlhbFF1ZXJ5KCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuX3NlYXJjaEV4cHJlc3Npb24gfHwgdGhpcy5zZWFyY2hQcm92aWRlci5nZXRJbml0aWFsUXVlcnkoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBkb2N1bWVudCBpcyByZWFkLW9ubHkgb3Igbm90LlxuICAgKi9cbiAgZ2V0IGlzUmVhZE9ubHkoKTogYm9vbGVhbiB7XG4gICAgcmV0dXJuIHRoaXMuc2VhcmNoUHJvdmlkZXIuaXNSZWFkT25seTtcbiAgfVxuXG4gIC8qKlxuICAgKiBQYXJzaW5nIHJlZ3VsYXIgZXhwcmVzc2lvbiBlcnJvciBtZXNzYWdlLlxuICAgKi9cbiAgZ2V0IHBhcnNpbmdFcnJvcigpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9wYXJzaW5nRXJyb3I7XG4gIH1cblxuICAvKipcbiAgICogUmVwbGFjZW1lbnQgZXhwcmVzc2lvblxuICAgKi9cbiAgZ2V0IHJlcGxhY2VUZXh0KCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuX3JlcGxhY2VUZXh0O1xuICB9XG4gIHNldCByZXBsYWNlVGV4dCh2OiBzdHJpbmcpIHtcbiAgICBpZiAodGhpcy5fcmVwbGFjZVRleHQgIT09IHYpIHtcbiAgICAgIHRoaXMuX3JlcGxhY2VUZXh0ID0gdjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogU2VhcmNoIGV4cHJlc3Npb25cbiAgICovXG4gIGdldCBzZWFyY2hFeHByZXNzaW9uKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuX3NlYXJjaEV4cHJlc3Npb247XG4gIH1cbiAgc2V0IHNlYXJjaEV4cHJlc3Npb24odjogc3RyaW5nKSB7XG4gICAgaWYgKHRoaXMuX3NlYXJjaEV4cHJlc3Npb24gIT09IHYpIHtcbiAgICAgIHRoaXMuX3NlYXJjaEV4cHJlc3Npb24gPSB2O1xuICAgICAgdGhpcy5zdGF0ZUNoYW5nZWQuZW1pdCgpO1xuICAgICAgdGhpcy5yZWZyZXNoKCk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFRvdGFsIG51bWJlciBvZiBtYXRjaGVzLlxuICAgKi9cbiAgZ2V0IHRvdGFsTWF0Y2hlcygpOiBudW1iZXIgfCBudWxsIHtcbiAgICByZXR1cm4gdGhpcy5zZWFyY2hQcm92aWRlci5tYXRjaGVzQ291bnQ7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0byB1c2UgcmVndWxhciBleHByZXNzaW9uIG9yIG5vdC5cbiAgICovXG4gIGdldCB1c2VSZWdleCgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5fdXNlUmVnZXg7XG4gIH1cbiAgc2V0IHVzZVJlZ2V4KHY6IGJvb2xlYW4pIHtcbiAgICBpZiAodGhpcy5fdXNlUmVnZXggIT09IHYpIHtcbiAgICAgIHRoaXMuX3VzZVJlZ2V4ID0gdjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIHRoaXMucmVmcmVzaCgpO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIHRoZSBtb2RlbC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuaXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGlmICh0aGlzLl9zZWFyY2hFeHByZXNzaW9uKSB7XG4gICAgICB0aGlzLmVuZFF1ZXJ5KCkuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihcbiAgICAgICAgICBgRmFpbGVkIHRvIGVuZCBxdWVyeSAnJHt0aGlzLl9zZWFyY2hFeHByZXNzaW9ufS5gLFxuICAgICAgICAgIHJlYXNvblxuICAgICAgICApO1xuICAgICAgfSk7XG4gICAgfVxuXG4gICAgdGhpcy5zZWFyY2hQcm92aWRlci5zdGF0ZUNoYW5nZWQuZGlzY29ubmVjdCh0aGlzLnJlZnJlc2gsIHRoaXMpO1xuXG4gICAgdGhpcy5fc2VhcmNoRGVib3VuY2VyLmRpc3Bvc2UoKTtcbiAgICBzdXBlci5kaXNwb3NlKCk7XG4gIH1cblxuICAvKipcbiAgICogRW5kIHRoZSBxdWVyeS5cbiAgICovXG4gIGFzeW5jIGVuZFF1ZXJ5KCk6IFByb21pc2U8dm9pZD4ge1xuICAgIGF3YWl0IHRoaXMuc2VhcmNoUHJvdmlkZXIuZW5kUXVlcnkoKTtcbiAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KCk7XG4gIH1cblxuICAvKipcbiAgICogSGlnaGxpZ2h0IHRoZSBuZXh0IG1hdGNoLlxuICAgKi9cbiAgYXN5bmMgaGlnaGxpZ2h0TmV4dCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBhd2FpdCB0aGlzLnNlYXJjaFByb3ZpZGVyLmhpZ2hsaWdodE5leHQoKTtcbiAgICAvLyBFbWl0IHN0YXRlIGNoYW5nZSBhcyB0aGUgaW5kZXggbmVlZHMgdG8gYmUgdXBkYXRlZFxuICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIaWdobGlnaHQgdGhlIHByZXZpb3VzIG1hdGNoXG4gICAqL1xuICBhc3luYyBoaWdobGlnaHRQcmV2aW91cygpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBhd2FpdCB0aGlzLnNlYXJjaFByb3ZpZGVyLmhpZ2hsaWdodFByZXZpb3VzKCk7XG4gICAgLy8gRW1pdCBzdGF0ZSBjaGFuZ2UgYXMgdGhlIGluZGV4IG5lZWRzIHRvIGJlIHVwZGF0ZWRcbiAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KCk7XG4gIH1cblxuICAvKipcbiAgICogUmVmcmVzaCBzZWFyY2hcbiAgICovXG4gIHJlZnJlc2goKTogdm9pZCB7XG4gICAgdGhpcy5fc2VhcmNoRGVib3VuY2VyLmludm9rZSgpLmNhdGNoKHJlYXNvbiA9PiB7XG4gICAgICBjb25zb2xlLmVycm9yKCdGYWlsZWQgdG8gaW52b2tlIHNlYXJjaCBkb2N1bWVudCBkZWJvdW5jZXIuJywgcmVhc29uKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXBsYWNlIGFsbCBtYXRjaGVzLlxuICAgKi9cbiAgYXN5bmMgcmVwbGFjZUFsbE1hdGNoZXMoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgYXdhaXQgdGhpcy5zZWFyY2hQcm92aWRlci5yZXBsYWNlQWxsTWF0Y2hlcyh0aGlzLl9yZXBsYWNlVGV4dCk7XG4gICAgLy8gRW1pdCBzdGF0ZSBjaGFuZ2UgYXMgdGhlIGluZGV4IG5lZWRzIHRvIGJlIHVwZGF0ZWRcbiAgICB0aGlzLnN0YXRlQ2hhbmdlZC5lbWl0KCk7XG4gIH1cblxuICAvKipcbiAgICogUmVwbGFjZSB0aGUgY3VycmVudCBtYXRjaC5cbiAgICovXG4gIGFzeW5jIHJlcGxhY2VDdXJyZW50TWF0Y2goKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgYXdhaXQgdGhpcy5zZWFyY2hQcm92aWRlci5yZXBsYWNlQ3VycmVudE1hdGNoKHRoaXMuX3JlcGxhY2VUZXh0KTtcbiAgICAvLyBFbWl0IHN0YXRlIGNoYW5nZSBhcyB0aGUgaW5kZXggbmVlZHMgdG8gYmUgdXBkYXRlZFxuICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgfVxuXG4gIHByaXZhdGUgYXN5bmMgX3VwZGF0ZVNlYXJjaCgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBpZiAodGhpcy5fcGFyc2luZ0Vycm9yKSB7XG4gICAgICB0aGlzLl9wYXJzaW5nRXJyb3IgPSAnJztcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICB9XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IHF1ZXJ5ID0gdGhpcy5zZWFyY2hFeHByZXNzaW9uXG4gICAgICAgID8gUHJpdmF0ZS5wYXJzZVF1ZXJ5KFxuICAgICAgICAgICAgdGhpcy5zZWFyY2hFeHByZXNzaW9uLFxuICAgICAgICAgICAgdGhpcy5jYXNlU2Vuc2l0aXZlLFxuICAgICAgICAgICAgdGhpcy51c2VSZWdleFxuICAgICAgICAgIClcbiAgICAgICAgOiBudWxsO1xuICAgICAgaWYgKHF1ZXJ5KSB7XG4gICAgICAgIGF3YWl0IHRoaXMuc2VhcmNoUHJvdmlkZXIuc3RhcnRRdWVyeShxdWVyeSwgdGhpcy5fZmlsdGVycyk7XG4gICAgICAgIC8vIEVtaXQgc3RhdGUgY2hhbmdlIGFzIHRoZSBpbmRleCBuZWVkcyB0byBiZSB1cGRhdGVkXG4gICAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIH1cbiAgICB9IGNhdGNoIChyZWFzb24pIHtcbiAgICAgIHRoaXMuX3BhcnNpbmdFcnJvciA9IHJlYXNvbjtcbiAgICAgIHRoaXMuc3RhdGVDaGFuZ2VkLmVtaXQoKTtcbiAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgIGBGYWlsZWQgdG8gcGFyc2UgZXhwcmVzc2lvbiAke3RoaXMuc2VhcmNoRXhwcmVzc2lvbn1gLFxuICAgICAgICByZWFzb25cbiAgICAgICk7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfY2FzZVNlbnNpdGl2ZSA9IGZhbHNlO1xuICBwcml2YXRlIF9kaXNwb3NlZCA9IG5ldyBTaWduYWw8dGhpcywgdm9pZD4odGhpcyk7XG4gIHByaXZhdGUgX3BhcnNpbmdFcnJvciA9ICcnO1xuICBwcml2YXRlIF9maWx0ZXJzOiBJRmlsdGVycyA9IHt9O1xuICBwcml2YXRlIF9yZXBsYWNlVGV4dDogc3RyaW5nO1xuICBwcml2YXRlIF9zZWFyY2hEZWJvdW5jZXI6IERlYm91bmNlcjtcbiAgcHJpdmF0ZSBfc2VhcmNoRXhwcmVzc2lvbiA9ICcnO1xuICBwcml2YXRlIF91c2VSZWdleCA9IGZhbHNlO1xufVxuXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBCdWlsZCB0aGUgcmVndWxhciBleHByZXNzaW9uIHRvIHVzZSBmb3Igc2VhcmNoaW5nLlxuICAgKlxuICAgKiBAcGFyYW0gcXVlcnlTdHJpbmcgUXVlcnkgc3RyaW5nXG4gICAqIEBwYXJhbSBjYXNlU2Vuc2l0aXZlIFdoZXRoZXIgdGhlIHNlYXJjaCBpcyBjYXNlIHNlbnNpdGl2ZSBvciBub3RcbiAgICogQHBhcmFtIHJlZ2V4IFdoZXRoZXIgdGhlIGV4cHJlc3Npb24gaXMgYSByZWd1bGFyIGV4cHJlc3Npb25cbiAgICogQHJldHVybnMgVGhlIHJlZ3VsYXIgZXhwcmVzc2lvbiB0byB1c2VcbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBwYXJzZVF1ZXJ5KFxuICAgIHF1ZXJ5U3RyaW5nOiBzdHJpbmcsXG4gICAgY2FzZVNlbnNpdGl2ZTogYm9vbGVhbixcbiAgICByZWdleDogYm9vbGVhblxuICApOiBSZWdFeHAgfCBudWxsIHtcbiAgICBjb25zdCBmbGFnID0gY2FzZVNlbnNpdGl2ZSA/ICdnJyA6ICdnaSc7XG4gICAgLy8gZXNjYXBlIHJlZ2V4IGNoYXJhY3RlcnMgaW4gcXVlcnkgaWYgaXRzIGEgc3RyaW5nIHNlYXJjaFxuICAgIGNvbnN0IHF1ZXJ5VGV4dCA9IHJlZ2V4XG4gICAgICA/IHF1ZXJ5U3RyaW5nXG4gICAgICA6IHF1ZXJ5U3RyaW5nLnJlcGxhY2UoL1stW1xcXS97fSgpKis/LlxcXFxeJHxdL2csICdcXFxcJCYnKTtcbiAgICBsZXQgcmV0O1xuICAgIHJldCA9IG5ldyBSZWdFeHAocXVlcnlUZXh0LCBmbGFnKTtcblxuICAgIC8vIElmIHRoZSBlbXB0eSBzdHJpbmcgaXMgaGl0LCB0aGUgc2VhcmNoIGxvZ2ljIHdpbGwgZnJlZXplIHRoZSBicm93c2VyIHRhYlxuICAgIC8vICBUcnlpbmcgL14vIG9yIC8kLyBvbiB0aGUgY29kZW1pcnJvciBzZWFyY2ggZGVtbywgZG9lcyBub3QgZmluZCBhbnl0aGluZy5cbiAgICAvLyAgU28gdGhpcyBpcyBhIGxpbWl0YXRpb24gb2YgdGhlIGVkaXRvci5cbiAgICBpZiAocmV0LnRlc3QoJycpKSB7XG4gICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG5cbiAgICByZXR1cm4gcmV0O1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBJRmlsdGVyLCBJRmlsdGVycywgSVNlYXJjaE1hdGNoLCBJU2VhcmNoUHJvdmlkZXIgfSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogQWJzdHJhY3QgY2xhc3MgaW1wbGVtZW50aW5nIHRoZSBzZWFyY2ggcHJvdmlkZXIgaW50ZXJmYWNlLlxuICovXG5leHBvcnQgYWJzdHJhY3QgY2xhc3MgU2VhcmNoUHJvdmlkZXI8VCBleHRlbmRzIFdpZGdldCA9IFdpZGdldD5cbiAgaW1wbGVtZW50cyBJU2VhcmNoUHJvdmlkZXJcbntcbiAgLyoqXG4gICAqIENvbnN0cnVjdG9yXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgVGhlIHdpZGdldCB0byBzZWFyY2ggaW5cbiAgICovXG4gIGNvbnN0cnVjdG9yKHByb3RlY3RlZCB3aWRnZXQ6IFQpIHtcbiAgICB0aGlzLl9zdGF0ZUNoYW5nZWQgPSBuZXcgU2lnbmFsPHRoaXMsIHZvaWQ+KHRoaXMpO1xuICAgIHRoaXMuX2Rpc3Bvc2VkID0gZmFsc2U7XG4gIH1cblxuICAvKipcbiAgICogU2lnbmFsIGluZGljYXRpbmcgdGhhdCBzb21ldGhpbmcgaW4gdGhlIHNlYXJjaCBoYXMgY2hhbmdlZCwgc28gdGhlIFVJIHNob3VsZCB1cGRhdGVcbiAgICovXG4gIGdldCBzdGF0ZUNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCB2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX3N0YXRlQ2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY3VycmVudCBpbmRleCBvZiB0aGUgc2VsZWN0ZWQgbWF0Y2guXG4gICAqL1xuICBnZXQgY3VycmVudE1hdGNoSW5kZXgoKTogbnVtYmVyIHwgbnVsbCB7XG4gICAgcmV0dXJuIG51bGw7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgc2VhcmNoIHByb3ZpZGVyIGlzIGRpc3Bvc2VkIG9yIG5vdC5cbiAgICovXG4gIGdldCBpc0Rpc3Bvc2VkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9kaXNwb3NlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgbnVtYmVyIG9mIG1hdGNoZXMuXG4gICAqL1xuICBnZXQgbWF0Y2hlc0NvdW50KCk6IG51bWJlciB8IG51bGwge1xuICAgIHJldHVybiBudWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0byB0cnVlIGlmIHRoZSB3aWRnZXQgdW5kZXIgc2VhcmNoIGlzIHJlYWQtb25seSwgZmFsc2VcbiAgICogaWYgaXQgaXMgZWRpdGFibGUuICBXaWxsIGJlIHVzZWQgdG8gZGV0ZXJtaW5lIHdoZXRoZXIgdG8gc2hvd1xuICAgKiB0aGUgcmVwbGFjZSBvcHRpb24uXG4gICAqL1xuICBhYnN0cmFjdCBnZXQgaXNSZWFkT25seSgpOiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSByZXNvdXJjZXMgaGVsZCBieSB0aGUgc2VhcmNoIHByb3ZpZGVyLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIElmIHRoZSBvYmplY3QncyBgZGlzcG9zZWAgbWV0aG9kIGlzIGNhbGxlZCBtb3JlIHRoYW4gb25jZSwgYWxsXG4gICAqIGNhbGxzIG1hZGUgYWZ0ZXIgdGhlIGZpcnN0IHdpbGwgYmUgYSBuby1vcC5cbiAgICpcbiAgICogIyMjIyBVbmRlZmluZWQgQmVoYXZpb3JcbiAgICogSXQgaXMgdW5kZWZpbmVkIGJlaGF2aW9yIHRvIHVzZSBhbnkgZnVuY3Rpb25hbGl0eSBvZiB0aGUgb2JqZWN0XG4gICAqIGFmdGVyIGl0IGhhcyBiZWVuIGRpc3Bvc2VkIHVubGVzcyBvdGhlcndpc2UgZXhwbGljaXRseSBub3RlZC5cbiAgICovXG4gIGRpc3Bvc2UoKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuX2Rpc3Bvc2VkKSB7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgdGhpcy5fZGlzcG9zZWQgPSB0cnVlO1xuICAgIFNpZ25hbC5jbGVhckRhdGEodGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IGFuIGluaXRpYWwgcXVlcnkgdmFsdWUgaWYgYXBwbGljYWJsZSBzbyB0aGF0IGl0IGNhbiBiZSBlbnRlcmVkXG4gICAqIGludG8gdGhlIHNlYXJjaCBib3ggYXMgYW4gaW5pdGlhbCBxdWVyeVxuICAgKlxuICAgKiBAcmV0dXJucyBJbml0aWFsIHZhbHVlIHVzZWQgdG8gcG9wdWxhdGUgdGhlIHNlYXJjaCBib3guXG4gICAqL1xuICBnZXRJbml0aWFsUXVlcnkoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gJyc7XG4gIH1cblxuICAvKipcbiAgICogR2V0IHRoZSBmaWx0ZXJzIGZvciB0aGUgZ2l2ZW4gcHJvdmlkZXIuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBmaWx0ZXJzLlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogVE9ETyBGb3Igbm93IGl0IG9ubHkgc3VwcG9ydHMgYm9vbGVhbiBmaWx0ZXJzIChyZXByZXNlbnRlZCB3aXRoIGNoZWNrYm94ZXMpXG4gICAqL1xuICBnZXRGaWx0ZXJzKCk6IHsgW2tleTogc3RyaW5nXTogSUZpbHRlciB9IHtcbiAgICByZXR1cm4ge307XG4gIH1cblxuICAvKipcbiAgICogU3RhcnQgYSBzZWFyY2ggdXNpbmcgdGhlIHByb3ZpZGVkIG9wdGlvbnMuXG4gICAqXG4gICAqIEBwYXJhbSBxdWVyeSBBIFJlZ0V4cCB0byBiZSB1c2UgdG8gcGVyZm9ybSB0aGUgc2VhcmNoXG4gICAqIEBwYXJhbSBmaWx0ZXJzIEZpbHRlciBwYXJhbWV0ZXJzIHRvIHBhc3MgdG8gcHJvdmlkZXJcbiAgICovXG4gIGFic3RyYWN0IHN0YXJ0UXVlcnkocXVlcnk6IFJlZ0V4cCwgZmlsdGVyczogSUZpbHRlcnMpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBTdG9wIGEgc2VhcmNoIGFuZCBjbGVhciBhbnkgaW50ZXJuYWwgc3RhdGUgb2YgdGhlIHNlYXJjaCBwcm92aWRlci5cbiAgICovXG4gIGFic3RyYWN0IGVuZFF1ZXJ5KCk6IFByb21pc2U8dm9pZD47XG5cbiAgLyoqXG4gICAqIENsZWFyIGN1cnJlbnRseSBoaWdobGlnaHRlZCBtYXRjaC5cbiAgICovXG4gIGFic3RyYWN0IGNsZWFySGlnaGxpZ2h0KCk6IFByb21pc2U8dm9pZD47XG5cbiAgLyoqXG4gICAqIEhpZ2hsaWdodCB0aGUgbmV4dCBtYXRjaC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIG5leHQgbWF0Y2ggaWYgYXZhaWxhYmxlXG4gICAqL1xuICBhYnN0cmFjdCBoaWdobGlnaHROZXh0KCk6IFByb21pc2U8SVNlYXJjaE1hdGNoIHwgdW5kZWZpbmVkPjtcblxuICAvKipcbiAgICogSGlnaGxpZ2h0IHRoZSBwcmV2aW91cyBtYXRjaC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIHByZXZpb3VzIG1hdGNoIGlmIGF2YWlsYWJsZS5cbiAgICovXG4gIGFic3RyYWN0IGhpZ2hsaWdodFByZXZpb3VzKCk6IFByb21pc2U8SVNlYXJjaE1hdGNoIHwgdW5kZWZpbmVkPjtcblxuICAvKipcbiAgICogUmVwbGFjZSB0aGUgY3VycmVudGx5IHNlbGVjdGVkIG1hdGNoIHdpdGggdGhlIHByb3ZpZGVkIHRleHRcbiAgICpcbiAgICogQHBhcmFtIG5ld1RleHQgVGhlIHJlcGxhY2VtZW50IHRleHRcbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2l0aCBhIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcmVwbGFjZSBvY2N1cnJlZC5cbiAgICovXG4gIGFic3RyYWN0IHJlcGxhY2VDdXJyZW50TWF0Y2gobmV3VGV4dDogc3RyaW5nKTogUHJvbWlzZTxib29sZWFuPjtcblxuICAvKipcbiAgICogUmVwbGFjZSBhbGwgbWF0Y2hlcyBpbiB0aGUgd2lkZ2V0IHdpdGggdGhlIHByb3ZpZGVkIHRleHRcbiAgICpcbiAgICogQHBhcmFtIG5ld1RleHQgVGhlIHJlcGxhY2VtZW50IHRleHRcbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2l0aCBhIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcmVwbGFjZSBvY2N1cnJlZC5cbiAgICovXG4gIGFic3RyYWN0IHJlcGxhY2VBbGxNYXRjaGVzKG5ld1RleHQ6IHN0cmluZyk6IFByb21pc2U8Ym9vbGVhbj47XG5cbiAgLy8gTmVlZHMgdG8gYmUgcHJvdGVjdGVkIHNvIHN1YmNsYXNzIGNhbiBlbWl0IHRoZSBzaWduYWwgdG9vLlxuICBwcm90ZWN0ZWQgX3N0YXRlQ2hhbmdlZDogU2lnbmFsPHRoaXMsIHZvaWQ+O1xuICBwcml2YXRlIF9kaXNwb3NlZDogYm9vbGVhbjtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIG51bGxUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgRGlzcG9zYWJsZURlbGVnYXRlLCBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuaW1wb3J0IHtcbiAgSVNlYXJjaFByb3ZpZGVyLFxuICBJU2VhcmNoUHJvdmlkZXJGYWN0b3J5LFxuICBJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeVxufSBmcm9tICcuL3Rva2Vucyc7XG5cbi8qKlxuICogU2VhcmNoIHByb3ZpZGVyIHJlZ2lzdHJ5XG4gKi9cbmV4cG9ydCBjbGFzcyBTZWFyY2hQcm92aWRlclJlZ2lzdHJ5IGltcGxlbWVudHMgSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnkge1xuICAvKipcbiAgICogQ29uc3RydWN0b3JcbiAgICpcbiAgICogQHBhcmFtIHRyYW5zbGF0b3IgQXBwbGljYXRpb24gdHJhbnNsYXRvciBvYmplY3RcbiAgICovXG4gIGNvbnN0cnVjdG9yKHByb3RlY3RlZCB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciA9IG51bGxUcmFuc2xhdG9yKSB7fVxuXG4gIC8qKlxuICAgKiBBZGQgYSBwcm92aWRlciB0byB0aGUgcmVnaXN0cnkuXG4gICAqXG4gICAqIEBwYXJhbSBrZXkgLSBUaGUgcHJvdmlkZXIga2V5LlxuICAgKiBAcmV0dXJucyBBIGRpc3Bvc2FibGUgZGVsZWdhdGUgdGhhdCwgd2hlbiBkaXNwb3NlZCwgZGVyZWdpc3RlcnMgdGhlIGdpdmVuIHNlYXJjaCBwcm92aWRlclxuICAgKi9cbiAgYWRkPFQgZXh0ZW5kcyBXaWRnZXQgPSBXaWRnZXQ+KFxuICAgIGtleTogc3RyaW5nLFxuICAgIHByb3ZpZGVyOiBJU2VhcmNoUHJvdmlkZXJGYWN0b3J5PFQ+XG4gICk6IElEaXNwb3NhYmxlIHtcbiAgICB0aGlzLl9wcm92aWRlck1hcC5zZXQoa2V5LCBwcm92aWRlcik7XG4gICAgdGhpcy5fY2hhbmdlZC5lbWl0KCk7XG4gICAgcmV0dXJuIG5ldyBEaXNwb3NhYmxlRGVsZWdhdGUoKCkgPT4ge1xuICAgICAgdGhpcy5fcHJvdmlkZXJNYXAuZGVsZXRlKGtleSk7XG4gICAgICB0aGlzLl9jaGFuZ2VkLmVtaXQoKTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXR1cm5zIGEgbWF0Y2hpbmcgcHJvdmlkZXIgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgd2lkZ2V0IHRvIHNlYXJjaCBvdmVyLlxuICAgKiBAcmV0dXJucyB0aGUgc2VhcmNoIHByb3ZpZGVyLCBvciB1bmRlZmluZWQgaWYgbm9uZSBleGlzdHMuXG4gICAqL1xuICBnZXRQcm92aWRlcih3aWRnZXQ6IFdpZGdldCk6IElTZWFyY2hQcm92aWRlciB8IHVuZGVmaW5lZCB7XG4gICAgLy8gaXRlcmF0ZSB0aHJvdWdoIGFsbCBwcm92aWRlcnMgYW5kIGFzayBlYWNoIG9uZSBpZiBpdCBjYW4gc2VhcmNoIG9uIHRoZVxuICAgIC8vIHdpZGdldC5cbiAgICBmb3IgKGNvbnN0IFAgb2YgdGhpcy5fcHJvdmlkZXJNYXAudmFsdWVzKCkpIHtcbiAgICAgIGlmIChQLmlzQXBwbGljYWJsZSh3aWRnZXQpKSB7XG4gICAgICAgIHJldHVybiBQLmNyZWF0ZU5ldyh3aWRnZXQsIHRoaXMudHJhbnNsYXRvcik7XG4gICAgICB9XG4gICAgfVxuICAgIHJldHVybiB1bmRlZmluZWQ7XG4gIH1cblxuICAvKipcbiAgICogV2hldGhlciB0aGUgcmVnaXN0cnkgYXMgYSBtYXRjaGluZyBwcm92aWRlciBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIFRoZSB3aWRnZXQgdG8gc2VhcmNoIG92ZXIuXG4gICAqIEByZXR1cm5zIFByb3ZpZGVyIGV4aXN0ZW5jZVxuICAgKi9cbiAgaGFzUHJvdmlkZXIod2lkZ2V0OiBXaWRnZXQpOiBib29sZWFuIHtcbiAgICBmb3IgKGNvbnN0IFAgb2YgdGhpcy5fcHJvdmlkZXJNYXAudmFsdWVzKCkpIHtcbiAgICAgIGlmIChQLmlzQXBwbGljYWJsZSh3aWRnZXQpKSB7XG4gICAgICAgIHJldHVybiB0cnVlO1xuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gZmFsc2U7XG4gIH1cblxuICAvKipcbiAgICogU2lnbmFsIHRoYXQgZW1pdHMgd2hlbiBhIG5ldyBzZWFyY2ggcHJvdmlkZXIgaGFzIGJlZW4gcmVnaXN0ZXJlZFxuICAgKiBvciByZW1vdmVkLlxuICAgKi9cbiAgZ2V0IGNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCB2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX2NoYW5nZWQ7XG4gIH1cblxuICBwcml2YXRlIF9jaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCB2b2lkPih0aGlzKTtcbiAgcHJpdmF0ZSBfcHJvdmlkZXJNYXAgPSBuZXcgTWFwPHN0cmluZywgSVNlYXJjaFByb3ZpZGVyRmFjdG9yeTxXaWRnZXQ+PigpO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQge1xuICBJVHJhbnNsYXRvcixcbiAgbnVsbFRyYW5zbGF0b3IsXG4gIFRyYW5zbGF0aW9uQnVuZGxlXG59IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7XG4gIGNhcmV0RG93bkVtcHR5VGhpbkljb24sXG4gIGNhcmV0RG93bkljb24sXG4gIGNhcmV0UmlnaHRJY29uLFxuICBjYXJldFVwRW1wdHlUaGluSWNvbixcbiAgY2FzZVNlbnNpdGl2ZUljb24sXG4gIGNsYXNzZXMsXG4gIGNsb3NlSWNvbixcbiAgZWxsaXBzZXNJY29uLFxuICByZWdleEljb24sXG4gIFZEb21SZW5kZXJlclxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IElTaWduYWwsIFNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5pbXBvcnQgeyBTZWFyY2hEb2N1bWVudE1vZGVsIH0gZnJvbSAnLi9zZWFyY2htb2RlbCc7XG5pbXBvcnQgeyBJRmlsdGVyLCBJRmlsdGVycyB9IGZyb20gJy4vdG9rZW5zJztcblxuY29uc3QgT1ZFUkxBWV9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1vdmVybGF5JztcbmNvbnN0IE9WRVJMQVlfUk9XX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLW92ZXJsYXktcm93JztcbmNvbnN0IElOUFVUX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLWlucHV0JztcbmNvbnN0IElOUFVUX1dSQVBQRVJfQ0xBU1MgPSAnanAtRG9jdW1lbnRTZWFyY2gtaW5wdXQtd3JhcHBlcic7XG5jb25zdCBJTlBVVF9CVVRUT05fQ0xBU1NfT0ZGID0gJ2pwLURvY3VtZW50U2VhcmNoLWlucHV0LWJ1dHRvbi1vZmYnO1xuY29uc3QgSU5QVVRfQlVUVE9OX0NMQVNTX09OID0gJ2pwLURvY3VtZW50U2VhcmNoLWlucHV0LWJ1dHRvbi1vbic7XG5jb25zdCBJTkRFWF9DT1VOVEVSX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLWluZGV4LWNvdW50ZXInO1xuY29uc3QgVVBfRE9XTl9CVVRUT05fV1JBUFBFUl9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC11cC1kb3duLXdyYXBwZXInO1xuY29uc3QgVVBfRE9XTl9CVVRUT05fQ0xBU1MgPSAnanAtRG9jdW1lbnRTZWFyY2gtdXAtZG93bi1idXR0b24nO1xuY29uc3QgRUxMSVBTRVNfQlVUVE9OX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLWVsbGlwc2VzLWJ1dHRvbic7XG5jb25zdCBFTExJUFNFU19CVVRUT05fRU5BQkxFRF9DTEFTUyA9XG4gICdqcC1Eb2N1bWVudFNlYXJjaC1lbGxpcHNlcy1idXR0b24tZW5hYmxlZCc7XG5jb25zdCBSRUdFWF9FUlJPUl9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1yZWdleC1lcnJvcic7XG5jb25zdCBTRUFSQ0hfT1BUSU9OU19DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1zZWFyY2gtb3B0aW9ucyc7XG5jb25zdCBTRUFSQ0hfT1BUSU9OU19ESVNBQkxFRF9DTEFTUyA9XG4gICdqcC1Eb2N1bWVudFNlYXJjaC1zZWFyY2gtb3B0aW9ucy1kaXNhYmxlZCc7XG5jb25zdCBTRUFSQ0hfRE9DVU1FTlRfTE9BRElORyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1kb2N1bWVudC1sb2FkaW5nJztcbmNvbnN0IFJFUExBQ0VfRU5UUllfQ0xBU1MgPSAnanAtRG9jdW1lbnRTZWFyY2gtcmVwbGFjZS1lbnRyeSc7XG5jb25zdCBSRVBMQUNFX0JVVFRPTl9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1yZXBsYWNlLWJ1dHRvbic7XG5jb25zdCBSRVBMQUNFX0JVVFRPTl9XUkFQUEVSX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLXJlcGxhY2UtYnV0dG9uLXdyYXBwZXInO1xuY29uc3QgUkVQTEFDRV9XUkFQUEVSX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLXJlcGxhY2Utd3JhcHBlci1jbGFzcyc7XG5jb25zdCBSRVBMQUNFX1RPR0dMRV9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1yZXBsYWNlLXRvZ2dsZSc7XG5jb25zdCBUT0dHTEVfV1JBUFBFUiA9ICdqcC1Eb2N1bWVudFNlYXJjaC10b2dnbGUtd3JhcHBlcic7XG5jb25zdCBUT0dHTEVfUExBQ0VIT0xERVIgPSAnanAtRG9jdW1lbnRTZWFyY2gtdG9nZ2xlLXBsYWNlaG9sZGVyJztcbmNvbnN0IEJVVFRPTl9DT05URU5UX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLWJ1dHRvbi1jb250ZW50JztcbmNvbnN0IEJVVFRPTl9XUkFQUEVSX0NMQVNTID0gJ2pwLURvY3VtZW50U2VhcmNoLWJ1dHRvbi13cmFwcGVyJztcbmNvbnN0IFNQQUNFUl9DTEFTUyA9ICdqcC1Eb2N1bWVudFNlYXJjaC1zcGFjZXInO1xuXG5pbnRlcmZhY2UgSVNlYXJjaEVudHJ5UHJvcHMge1xuICBpbnB1dFJlZjogUmVhY3QuUmVmT2JqZWN0PEhUTUxJbnB1dEVsZW1lbnQ+O1xuICBvbkNhc2VTZW5zaXRpdmVUb2dnbGVkOiAoKSA9PiB2b2lkO1xuICBvblJlZ2V4VG9nZ2xlZDogKCkgPT4gdm9pZDtcbiAgb25LZXlkb3duOiAoZTogUmVhY3QuS2V5Ym9hcmRFdmVudDxIVE1MSW5wdXRFbGVtZW50PikgPT4gdm9pZDtcbiAgb25DaGFuZ2U6IChlOiBSZWFjdC5DaGFuZ2VFdmVudDxIVE1MSW5wdXRFbGVtZW50PikgPT4gdm9pZDtcbiAgY2FzZVNlbnNpdGl2ZTogYm9vbGVhbjtcbiAgdXNlUmVnZXg6IGJvb2xlYW47XG4gIHNlYXJjaFRleHQ6IHN0cmluZztcbiAgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yO1xufVxuXG5mdW5jdGlvbiBTZWFyY2hFbnRyeShwcm9wczogSVNlYXJjaEVudHJ5UHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGNvbnN0IHRyYW5zID0gKHByb3BzLnRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICBjb25zdCBjYXNlQnV0dG9uVG9nZ2xlQ2xhc3MgPSBjbGFzc2VzKFxuICAgIHByb3BzLmNhc2VTZW5zaXRpdmUgPyBJTlBVVF9CVVRUT05fQ0xBU1NfT04gOiBJTlBVVF9CVVRUT05fQ0xBU1NfT0ZGLFxuICAgIEJVVFRPTl9DT05URU5UX0NMQVNTXG4gICk7XG4gIGNvbnN0IHJlZ2V4QnV0dG9uVG9nZ2xlQ2xhc3MgPSBjbGFzc2VzKFxuICAgIHByb3BzLnVzZVJlZ2V4ID8gSU5QVVRfQlVUVE9OX0NMQVNTX09OIDogSU5QVVRfQlVUVE9OX0NMQVNTX09GRixcbiAgICBCVVRUT05fQ09OVEVOVF9DTEFTU1xuICApO1xuXG4gIGNvbnN0IHdyYXBwZXJDbGFzcyA9IElOUFVUX1dSQVBQRVJfQ0xBU1M7XG5cbiAgcmV0dXJuIChcbiAgICA8ZGl2IGNsYXNzTmFtZT17d3JhcHBlckNsYXNzfT5cbiAgICAgIDxpbnB1dFxuICAgICAgICBwbGFjZWhvbGRlcj17dHJhbnMuX18oJ0ZpbmQnKX1cbiAgICAgICAgY2xhc3NOYW1lPXtJTlBVVF9DTEFTU31cbiAgICAgICAgdmFsdWU9e3Byb3BzLnNlYXJjaFRleHR9XG4gICAgICAgIG9uQ2hhbmdlPXtlID0+IHByb3BzLm9uQ2hhbmdlKGUpfVxuICAgICAgICBvbktleURvd249e2UgPT4gcHJvcHMub25LZXlkb3duKGUpfVxuICAgICAgICB0YWJJbmRleD17MH1cbiAgICAgICAgcmVmPXtwcm9wcy5pbnB1dFJlZn1cbiAgICAgICAgdGl0bGU9e3RyYW5zLl9fKCdGaW5kJyl9XG4gICAgICAvPlxuICAgICAgPGJ1dHRvblxuICAgICAgICBjbGFzc05hbWU9e0JVVFRPTl9XUkFQUEVSX0NMQVNTfVxuICAgICAgICBvbkNsaWNrPXsoKSA9PiB7XG4gICAgICAgICAgcHJvcHMub25DYXNlU2Vuc2l0aXZlVG9nZ2xlZCgpO1xuICAgICAgICB9fVxuICAgICAgICB0YWJJbmRleD17MH1cbiAgICAgICAgdGl0bGU9e3RyYW5zLl9fKCdNYXRjaCBDYXNlJyl9XG4gICAgICA+XG4gICAgICAgIDxjYXNlU2Vuc2l0aXZlSWNvbi5yZWFjdCBjbGFzc05hbWU9e2Nhc2VCdXR0b25Ub2dnbGVDbGFzc30gdGFnPVwic3BhblwiIC8+XG4gICAgICA8L2J1dHRvbj5cbiAgICAgIDxidXR0b25cbiAgICAgICAgY2xhc3NOYW1lPXtCVVRUT05fV1JBUFBFUl9DTEFTU31cbiAgICAgICAgb25DbGljaz17KCkgPT4gcHJvcHMub25SZWdleFRvZ2dsZWQoKX1cbiAgICAgICAgdGFiSW5kZXg9ezB9XG4gICAgICAgIHRpdGxlPXt0cmFucy5fXygnVXNlIFJlZ3VsYXIgRXhwcmVzc2lvbicpfVxuICAgICAgPlxuICAgICAgICA8cmVnZXhJY29uLnJlYWN0IGNsYXNzTmFtZT17cmVnZXhCdXR0b25Ub2dnbGVDbGFzc30gdGFnPVwic3BhblwiIC8+XG4gICAgICA8L2J1dHRvbj5cbiAgICA8L2Rpdj5cbiAgKTtcbn1cblxuaW50ZXJmYWNlIElSZXBsYWNlRW50cnlQcm9wcyB7XG4gIG9uUmVwbGFjZUN1cnJlbnQ6ICgpID0+IHZvaWQ7XG4gIG9uUmVwbGFjZUFsbDogKCkgPT4gdm9pZDtcbiAgb25SZXBsYWNlS2V5ZG93bjogKGU6IFJlYWN0LktleWJvYXJkRXZlbnQ8SFRNTElucHV0RWxlbWVudD4pID0+IHZvaWQ7XG4gIG9uQ2hhbmdlOiAoZTogUmVhY3QuQ2hhbmdlRXZlbnQ8SFRNTElucHV0RWxlbWVudD4pID0+IHZvaWQ7XG4gIHJlcGxhY2VUZXh0OiBzdHJpbmc7XG4gIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbn1cblxuZnVuY3Rpb24gUmVwbGFjZUVudHJ5KHByb3BzOiBJUmVwbGFjZUVudHJ5UHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGNvbnN0IHRyYW5zID0gKHByb3BzLnRyYW5zbGF0b3IgPz8gbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPXtSRVBMQUNFX1dSQVBQRVJfQ0xBU1N9PlxuICAgICAgPGlucHV0XG4gICAgICAgIHBsYWNlaG9sZGVyPXt0cmFucy5fXygnUmVwbGFjZScpfVxuICAgICAgICBjbGFzc05hbWU9e1JFUExBQ0VfRU5UUllfQ0xBU1N9XG4gICAgICAgIHZhbHVlPXtwcm9wcy5yZXBsYWNlVGV4dH1cbiAgICAgICAgb25LZXlEb3duPXtlID0+IHByb3BzLm9uUmVwbGFjZUtleWRvd24oZSl9XG4gICAgICAgIG9uQ2hhbmdlPXtlID0+IHByb3BzLm9uQ2hhbmdlKGUpfVxuICAgICAgICB0YWJJbmRleD17MH1cbiAgICAgICAgdGl0bGU9e3RyYW5zLl9fKCdSZXBsYWNlJyl9XG4gICAgICAvPlxuICAgICAgPGJ1dHRvblxuICAgICAgICBjbGFzc05hbWU9e1JFUExBQ0VfQlVUVE9OX1dSQVBQRVJfQ0xBU1N9XG4gICAgICAgIG9uQ2xpY2s9eygpID0+IHByb3BzLm9uUmVwbGFjZUN1cnJlbnQoKX1cbiAgICAgICAgdGFiSW5kZXg9ezB9XG4gICAgICA+XG4gICAgICAgIDxzcGFuXG4gICAgICAgICAgY2xhc3NOYW1lPXtgJHtSRVBMQUNFX0JVVFRPTl9DTEFTU30gJHtCVVRUT05fQ09OVEVOVF9DTEFTU31gfVxuICAgICAgICAgIHRhYkluZGV4PXswfVxuICAgICAgICA+XG4gICAgICAgICAge3RyYW5zLl9fKCdSZXBsYWNlJyl9XG4gICAgICAgIDwvc3Bhbj5cbiAgICAgIDwvYnV0dG9uPlxuICAgICAgPGJ1dHRvblxuICAgICAgICBjbGFzc05hbWU9e1JFUExBQ0VfQlVUVE9OX1dSQVBQRVJfQ0xBU1N9XG4gICAgICAgIHRhYkluZGV4PXswfVxuICAgICAgICBvbkNsaWNrPXsoKSA9PiBwcm9wcy5vblJlcGxhY2VBbGwoKX1cbiAgICAgID5cbiAgICAgICAgPHNwYW5cbiAgICAgICAgICBjbGFzc05hbWU9e2Ake1JFUExBQ0VfQlVUVE9OX0NMQVNTfSAke0JVVFRPTl9DT05URU5UX0NMQVNTfWB9XG4gICAgICAgICAgdGFiSW5kZXg9ey0xfVxuICAgICAgICA+XG4gICAgICAgICAge3RyYW5zLl9fKCdSZXBsYWNlIEFsbCcpfVxuICAgICAgICA8L3NwYW4+XG4gICAgICA8L2J1dHRvbj5cbiAgICA8L2Rpdj5cbiAgKTtcbn1cblxuaW50ZXJmYWNlIElVcERvd25Qcm9wcyB7XG4gIG9uSGlnaGxpZ2h0UHJldmlvdXM6ICgpID0+IHZvaWQ7XG4gIG9uSGlnaGxpZ2h0TmV4dDogKCkgPT4gdm9pZDtcbiAgdHJhbnM6IFRyYW5zbGF0aW9uQnVuZGxlO1xufVxuXG5mdW5jdGlvbiBVcERvd25CdXR0b25zKHByb3BzOiBJVXBEb3duUHJvcHMpIHtcbiAgcmV0dXJuIChcbiAgICA8ZGl2IGNsYXNzTmFtZT17VVBfRE9XTl9CVVRUT05fV1JBUFBFUl9DTEFTU30+XG4gICAgICA8YnV0dG9uXG4gICAgICAgIGNsYXNzTmFtZT17QlVUVE9OX1dSQVBQRVJfQ0xBU1N9XG4gICAgICAgIG9uQ2xpY2s9eygpID0+IHByb3BzLm9uSGlnaGxpZ2h0UHJldmlvdXMoKX1cbiAgICAgICAgdGFiSW5kZXg9ezB9XG4gICAgICAgIHRpdGxlPXtwcm9wcy50cmFucy5fXygnUHJldmlvdXMgTWF0Y2gnKX1cbiAgICAgID5cbiAgICAgICAgPGNhcmV0VXBFbXB0eVRoaW5JY29uLnJlYWN0XG4gICAgICAgICAgY2xhc3NOYW1lPXtjbGFzc2VzKFVQX0RPV05fQlVUVE9OX0NMQVNTLCBCVVRUT05fQ09OVEVOVF9DTEFTUyl9XG4gICAgICAgICAgdGFnPVwic3BhblwiXG4gICAgICAgIC8+XG4gICAgICA8L2J1dHRvbj5cbiAgICAgIDxidXR0b25cbiAgICAgICAgY2xhc3NOYW1lPXtCVVRUT05fV1JBUFBFUl9DTEFTU31cbiAgICAgICAgb25DbGljaz17KCkgPT4gcHJvcHMub25IaWdobGlnaHROZXh0KCl9XG4gICAgICAgIHRhYkluZGV4PXswfVxuICAgICAgICB0aXRsZT17cHJvcHMudHJhbnMuX18oJ05leHQgTWF0Y2gnKX1cbiAgICAgID5cbiAgICAgICAgPGNhcmV0RG93bkVtcHR5VGhpbkljb24ucmVhY3RcbiAgICAgICAgICBjbGFzc05hbWU9e2NsYXNzZXMoVVBfRE9XTl9CVVRUT05fQ0xBU1MsIEJVVFRPTl9DT05URU5UX0NMQVNTKX1cbiAgICAgICAgICB0YWc9XCJzcGFuXCJcbiAgICAgICAgLz5cbiAgICAgIDwvYnV0dG9uPlxuICAgIDwvZGl2PlxuICApO1xufVxuXG5pbnRlcmZhY2UgSVNlYXJjaEluZGV4UHJvcHMge1xuICBjdXJyZW50SW5kZXg6IG51bWJlciB8IG51bGw7XG4gIHRvdGFsTWF0Y2hlczogbnVtYmVyO1xufVxuXG5mdW5jdGlvbiBTZWFyY2hJbmRpY2VzKHByb3BzOiBJU2VhcmNoSW5kZXhQcm9wcykge1xuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPXtJTkRFWF9DT1VOVEVSX0NMQVNTfT5cbiAgICAgIHtwcm9wcy50b3RhbE1hdGNoZXMgPT09IDBcbiAgICAgICAgPyAnLS8tJ1xuICAgICAgICA6IGAke3Byb3BzLmN1cnJlbnRJbmRleCA9PT0gbnVsbCA/ICctJyA6IHByb3BzLmN1cnJlbnRJbmRleCArIDF9LyR7XG4gICAgICAgICAgICBwcm9wcy50b3RhbE1hdGNoZXNcbiAgICAgICAgICB9YH1cbiAgICA8L2Rpdj5cbiAgKTtcbn1cblxuaW50ZXJmYWNlIElGaWx0ZXJUb2dnbGVQcm9wcyB7XG4gIGVuYWJsZWQ6IGJvb2xlYW47XG4gIHRvZ2dsZUVuYWJsZWQ6ICgpID0+IHZvaWQ7XG4gIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZTtcbn1cblxuZnVuY3Rpb24gRmlsdGVyVG9nZ2xlKHByb3BzOiBJRmlsdGVyVG9nZ2xlUHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGxldCBjbGFzc05hbWUgPSBgJHtFTExJUFNFU19CVVRUT05fQ0xBU1N9ICR7QlVUVE9OX0NPTlRFTlRfQ0xBU1N9YDtcbiAgaWYgKHByb3BzLmVuYWJsZWQpIHtcbiAgICBjbGFzc05hbWUgPSBgJHtjbGFzc05hbWV9ICR7RUxMSVBTRVNfQlVUVE9OX0VOQUJMRURfQ0xBU1N9YDtcbiAgfVxuXG4gIHJldHVybiAoXG4gICAgPGJ1dHRvblxuICAgICAgY2xhc3NOYW1lPXtCVVRUT05fV1JBUFBFUl9DTEFTU31cbiAgICAgIG9uQ2xpY2s9eygpID0+IHByb3BzLnRvZ2dsZUVuYWJsZWQoKX1cbiAgICAgIHRhYkluZGV4PXswfVxuICAgICAgdGl0bGU9e1xuICAgICAgICBwcm9wcy5lbmFibGVkXG4gICAgICAgICAgPyBwcm9wcy50cmFucy5fXygnSGlkZSBTZWFyY2ggRmlsdGVycycpXG4gICAgICAgICAgOiBwcm9wcy50cmFucy5fXygnU2hvdyBTZWFyY2ggRmlsdGVycycpXG4gICAgICB9XG4gICAgPlxuICAgICAgPGVsbGlwc2VzSWNvbi5yZWFjdFxuICAgICAgICBjbGFzc05hbWU9e2NsYXNzTmFtZX1cbiAgICAgICAgdGFnPVwic3BhblwiXG4gICAgICAgIGhlaWdodD1cIjIwcHhcIlxuICAgICAgICB3aWR0aD1cIjIwcHhcIlxuICAgICAgLz5cbiAgICA8L2J1dHRvbj5cbiAgKTtcbn1cblxuaW50ZXJmYWNlIElGaWx0ZXJTZWxlY3Rpb25Qcm9wcyB7XG4gIHRpdGxlOiBzdHJpbmc7XG4gIGRlc2NyaXB0aW9uOiBzdHJpbmc7XG4gIHZhbHVlOiBib29sZWFuO1xuICBpc0VuYWJsZWQ6IGJvb2xlYW47XG4gIG9uVG9nZ2xlOiAoKSA9PiB2b2lkO1xufVxuXG5mdW5jdGlvbiBGaWx0ZXJTZWxlY3Rpb24ocHJvcHM6IElGaWx0ZXJTZWxlY3Rpb25Qcm9wcyk6IEpTWC5FbGVtZW50IHtcbiAgcmV0dXJuIChcbiAgICA8bGFiZWxcbiAgICAgIGNsYXNzTmFtZT17cHJvcHMuaXNFbmFibGVkID8gJycgOiBTRUFSQ0hfT1BUSU9OU19ESVNBQkxFRF9DTEFTU31cbiAgICAgIHRpdGxlPXtwcm9wcy5kZXNjcmlwdGlvbn1cbiAgICA+XG4gICAgICB7cHJvcHMudGl0bGV9XG4gICAgICA8aW5wdXRcbiAgICAgICAgdHlwZT1cImNoZWNrYm94XCJcbiAgICAgICAgZGlzYWJsZWQ9eyFwcm9wcy5pc0VuYWJsZWR9XG4gICAgICAgIGNoZWNrZWQ9e3Byb3BzLnZhbHVlfVxuICAgICAgICBvbkNoYW5nZT17cHJvcHMub25Ub2dnbGV9XG4gICAgICAvPlxuICAgIDwvbGFiZWw+XG4gICk7XG59XG5cbi8qKlxuICogUmVhY3Qgc2VhcmNoIGNvbXBvbmVudCBzdGF0ZVxuICovXG5pbnRlcmZhY2UgSVNlYXJjaE92ZXJsYXlTdGF0ZSB7XG4gIC8qKlxuICAgKiBJcyB0aGUgZmlsdGVycyB2aWV3IG9wZW4/XG4gICAqL1xuICBmaWx0ZXJzT3BlbjogYm9vbGVhbjtcbn1cblxuaW50ZXJmYWNlIElTZWFyY2hPdmVybGF5UHJvcHMge1xuICAvKipcbiAgICogV2hldGhlciB0aGUgc2VhcmNoIGlzIGNhc2Ugc2Vuc2l0aXZlIG9yIG5vdC5cbiAgICovXG4gIGNhc2VTZW5zaXRpdmU6IGJvb2xlYW47XG4gIC8qKlxuICAgKiBDdXJyZW50IG1hdGNoIGluZGV4LlxuICAgKi9cbiAgY3VycmVudEluZGV4OiBudW1iZXIgfCBudWxsO1xuICAvKipcbiAgICogRXJyb3IgbWVzc2FnZVxuICAgKi9cbiAgZXJyb3JNZXNzYWdlOiBzdHJpbmc7XG4gIC8qKlxuICAgKiBGaWx0ZXJzIHZhbHVlcy5cbiAgICovXG4gIGZpbHRlcnM6IElGaWx0ZXJzO1xuICAvKipcbiAgICogQXZhaWxhYmxlIGZpbHRlcnMgZGVmaW5pdGlvbi5cbiAgICovXG4gIGZpbHRlcnNEZWZpbml0aW9uOiB7IFtmOiBzdHJpbmddOiBJRmlsdGVyIH07XG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSBkb2N1bWVudCBpcyByZWFkLW9ubHkgb3Igbm90LlxuICAgKi9cbiAgaXNSZWFkT25seTogYm9vbGVhbjtcbiAgLyoqXG4gICAqIFdoZXRoZXIgb3Igbm90IHRoZSByZXBsYWNlIGVudHJ5IHJvdyBpcyB2aXNpYmxlXG4gICAqL1xuICByZXBsYWNlRW50cnlWaXNpYmxlOiBib29sZWFuO1xuICAvKipcbiAgICogUmVwbGFjZW1lbnQgZXhwcmVzc2lvblxuICAgKi9cbiAgcmVwbGFjZVRleHQ6IHN0cmluZztcbiAgLyoqXG4gICAqIFRoZSB0ZXh0IGluIHRoZSBzZWFyY2ggZW50cnlcbiAgICovXG4gIHNlYXJjaFRleHQ6IHN0cmluZztcbiAgLyoqXG4gICAqIFNlYXJjaCBpbnB1dCByZWZlcmVuY2UuXG4gICAqL1xuICBzZWFyY2hJbnB1dFJlZjogUmVhY3QuUmVmT2JqZWN0PEhUTUxJbnB1dEVsZW1lbnQ+O1xuICAvKipcbiAgICogVG90YWwgbnVtYmVyIG9mIHNlYXJjaCBtYXRjaGVzLlxuICAgKi9cbiAgdG90YWxNYXRjaGVzOiBudW1iZXIgfCBudWxsO1xuICAvKipcbiAgICogQXBwbGljYXRpb24gdHJhbnNsYXRvciBvYmplY3RcbiAgICovXG4gIHRyYW5zbGF0b3I/OiBJVHJhbnNsYXRvcjtcbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIHNlYXJjaCBkZWZpbmVzIGEgcmVndWxhciBleHByZXNzaW9uIG9yIG5vdC5cbiAgICovXG4gIHVzZVJlZ2V4OiBib29sZWFuO1xuICAvKipcbiAgICogQ2FsbGJhY2sgb24gY2FzZSBzZW5zaXRpdmUgdG9nZ2xlZC5cbiAgICovXG4gIG9uQ2FzZVNlbnNpdGl2ZVRvZ2dsZWQ6ICgpID0+IHZvaWQ7XG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiBoaWdobGlnaHQgbmV4dCBjbGljay5cbiAgICovXG4gIG9uSGlnaGxpZ2h0TmV4dDogKCkgPT4gdm9pZDtcbiAgLyoqXG4gICAqIENhbGxiYWNrIG9uIGhpZ2hsaWdodCBwcmV2aW91cyBjbGljay5cbiAgICovXG4gIG9uSGlnaGxpZ2h0UHJldmlvdXM6ICgpID0+IHZvaWQ7XG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiBmaWx0ZXJzIHZhbHVlcyBjaGFuZ2VkLlxuICAgKlxuICAgKiBUaGUgcHJvdmlkZWQgZmlsdGVyIHZhbHVlcyBhcmUgdGhlIG9uZSBjaGFuZ2luZy5cbiAgICovXG4gIG9uRmlsdGVyc0NoYW5nZWQ6IChmOiBJRmlsdGVycykgPT4gdm9pZDtcbiAgLyoqXG4gICAqIENhbGxiYWNrIG9uIGNsb3NlIGJ1dHRvbiBjbGljay5cbiAgICovXG4gIG9uQ2xvc2U6ICgpID0+IHZvaWQ7XG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiB1c2UgcmVndWxhciBleHByZXNzaW9uIHRvZ2dsZWRcbiAgICovXG4gIG9uUmVnZXhUb2dnbGVkOiAoKSA9PiB2b2lkO1xuICAvKipcbiAgICogQ2FsbGJhY2sgb24gcmVwbGFjZSBhbGwgYnV0dG9uIGNsaWNrLlxuICAgKi9cbiAgb25SZXBsYWNlQWxsOiAoKSA9PiB2b2lkO1xuICAvKipcbiAgICogQ2FsbGJhY2sgb24gcmVwbGFjZSBleHByZXNzaW9uIGNoYW5nZS5cbiAgICovXG4gIG9uUmVwbGFjZUNoYW5nZWQ6IChxOiBzdHJpbmcpID0+IHZvaWQ7XG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiByZXBsYWNlIGN1cnJlbnQgYnV0dG9uIGNsaWNrLlxuICAgKi9cbiAgb25SZXBsYWNlQ3VycmVudDogKCkgPT4gdm9pZDtcbiAgLyoqXG4gICAqIENhbGxiYWNrIG9uIHNob3cgcmVwbGFjZSBtZW51IGJ1dHRvbiBjbGljay5cbiAgICovXG4gIG9uUmVwbGFjZUVudHJ5U2hvd246ICh2OiBib29sZWFuKSA9PiB2b2lkO1xuICAvKipcbiAgICogQ2FsbGJhY2sgb24gc2VhcmNoIGV4cHJlc3Npb24gY2hhbmdlLlxuICAgKi9cbiAgb25TZWFyY2hDaGFuZ2VkOiAocTogc3RyaW5nKSA9PiB2b2lkO1xufVxuXG5jbGFzcyBTZWFyY2hPdmVybGF5IGV4dGVuZHMgUmVhY3QuQ29tcG9uZW50PFxuICBJU2VhcmNoT3ZlcmxheVByb3BzLFxuICBJU2VhcmNoT3ZlcmxheVN0YXRlXG4+IHtcbiAgY29uc3RydWN0b3IocHJvcHM6IElTZWFyY2hPdmVybGF5UHJvcHMpIHtcbiAgICBzdXBlcihwcm9wcyk7XG4gICAgdGhpcy50cmFuc2xhdG9yID0gcHJvcHMudHJhbnNsYXRvciB8fCBudWxsVHJhbnNsYXRvcjtcbiAgICB0aGlzLnN0YXRlID0ge1xuICAgICAgZmlsdGVyc09wZW46IGZhbHNlXG4gICAgfTtcbiAgfVxuXG4gIHByaXZhdGUgX29uU2VhcmNoQ2hhbmdlKGV2ZW50OiBSZWFjdC5DaGFuZ2VFdmVudCkge1xuICAgIGNvbnN0IHNlYXJjaFRleHQgPSAoZXZlbnQudGFyZ2V0IGFzIEhUTUxJbnB1dEVsZW1lbnQpLnZhbHVlO1xuICAgIHRoaXMucHJvcHMub25TZWFyY2hDaGFuZ2VkKHNlYXJjaFRleHQpO1xuICB9XG5cbiAgcHJpdmF0ZSBfb25TZWFyY2hLZXlkb3duKGV2ZW50OiBSZWFjdC5LZXlib2FyZEV2ZW50KSB7XG4gICAgaWYgKGV2ZW50LmtleUNvZGUgPT09IDEzKSB7XG4gICAgICAvLyBFbnRlciBwcmVzc2VkXG4gICAgICBldmVudC5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgZXZlbnQuc3RvcFByb3BhZ2F0aW9uKCk7XG4gICAgICBldmVudC5zaGlmdEtleVxuICAgICAgICA/IHRoaXMucHJvcHMub25IaWdobGlnaHRQcmV2aW91cygpXG4gICAgICAgIDogdGhpcy5wcm9wcy5vbkhpZ2hsaWdodE5leHQoKTtcbiAgICB9IGVsc2UgaWYgKGV2ZW50LmtleUNvZGUgPT09IDI3KSB7XG4gICAgICAvLyBFc2NhcGUgcHJlc3NlZFxuICAgICAgZXZlbnQucHJldmVudERlZmF1bHQoKTtcbiAgICAgIGV2ZW50LnN0b3BQcm9wYWdhdGlvbigpO1xuICAgICAgdGhpcy5fb25DbG9zZSgpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX29uUmVwbGFjZUtleWRvd24oZXZlbnQ6IFJlYWN0LktleWJvYXJkRXZlbnQpIHtcbiAgICBpZiAoZXZlbnQua2V5Q29kZSA9PT0gMTMpIHtcbiAgICAgIC8vIEVudGVyIHByZXNzZWRcbiAgICAgIGV2ZW50LnByZXZlbnREZWZhdWx0KCk7XG4gICAgICBldmVudC5zdG9wUHJvcGFnYXRpb24oKTtcbiAgICAgIHRoaXMucHJvcHMub25SZXBsYWNlQ3VycmVudCgpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX29uQ2xvc2UoKSB7XG4gICAgLy8gQ2xlYW4gdXAgYW5kIGNsb3NlIHdpZGdldC5cbiAgICB0aGlzLnByb3BzLm9uQ2xvc2UoKTtcbiAgfVxuXG4gIHByaXZhdGUgX29uUmVwbGFjZVRvZ2dsZWQoKSB7XG4gICAgLy8gRGVhY3RpdmF0ZSBpbnZhbGlkIHJlcGxhY2UgZmlsdGVyc1xuICAgIGNvbnN0IGZpbHRlcnMgPSB7IC4uLnRoaXMucHJvcHMuZmlsdGVycyB9O1xuICAgIGlmICghdGhpcy5wcm9wcy5yZXBsYWNlRW50cnlWaXNpYmxlKSB7XG4gICAgICBmb3IgKGNvbnN0IGtleSBpbiB0aGlzLnByb3BzLmZpbHRlcnNEZWZpbml0aW9uKSB7XG4gICAgICAgIGNvbnN0IGZpbHRlciA9IHRoaXMucHJvcHMuZmlsdGVyc0RlZmluaXRpb25ba2V5XTtcbiAgICAgICAgaWYgKCFmaWx0ZXIuc3VwcG9ydFJlcGxhY2UpIHtcbiAgICAgICAgICBmaWx0ZXJzW2tleV0gPSBmYWxzZTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH1cbiAgICB0aGlzLnByb3BzLm9uRmlsdGVyc0NoYW5nZWQoZmlsdGVycyk7XG5cbiAgICB0aGlzLnByb3BzLm9uUmVwbGFjZUVudHJ5U2hvd24oIXRoaXMucHJvcHMucmVwbGFjZUVudHJ5VmlzaWJsZSk7XG4gIH1cblxuICBwcml2YXRlIF90b2dnbGVGaWx0ZXJzT3BlbigpIHtcbiAgICB0aGlzLnNldFN0YXRlKHByZXZTdGF0ZSA9PiAoe1xuICAgICAgZmlsdGVyc09wZW46ICFwcmV2U3RhdGUuZmlsdGVyc09wZW5cbiAgICB9KSk7XG4gIH1cblxuICByZW5kZXIoKSB7XG4gICAgY29uc3QgdHJhbnMgPSB0aGlzLnRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIGNvbnN0IHNob3dSZXBsYWNlID1cbiAgICAgICF0aGlzLnByb3BzLmlzUmVhZE9ubHkgJiYgdGhpcy5wcm9wcy5yZXBsYWNlRW50cnlWaXNpYmxlO1xuICAgIGNvbnN0IGZpbHRlcnMgPSB0aGlzLnByb3BzLmZpbHRlcnNEZWZpbml0aW9uO1xuXG4gICAgY29uc3QgaGFzRmlsdGVycyA9IE9iamVjdC5rZXlzKGZpbHRlcnMpLmxlbmd0aCA+IDA7XG4gICAgY29uc3QgZmlsdGVyVG9nZ2xlID0gaGFzRmlsdGVycyA/IChcbiAgICAgIDxGaWx0ZXJUb2dnbGVcbiAgICAgICAgZW5hYmxlZD17dGhpcy5zdGF0ZS5maWx0ZXJzT3Blbn1cbiAgICAgICAgdG9nZ2xlRW5hYmxlZD17KCkgPT4gdGhpcy5fdG9nZ2xlRmlsdGVyc09wZW4oKX1cbiAgICAgICAgdHJhbnM9e3RyYW5zfVxuICAgICAgLz5cbiAgICApIDogbnVsbDtcbiAgICBjb25zdCBmaWx0ZXIgPSBoYXNGaWx0ZXJzID8gKFxuICAgICAgPGRpdiBjbGFzc05hbWU9e1NFQVJDSF9PUFRJT05TX0NMQVNTfT5cbiAgICAgICAge09iamVjdC5rZXlzKGZpbHRlcnMpLm1hcChuYW1lID0+IHtcbiAgICAgICAgICBjb25zdCBmaWx0ZXIgPSBmaWx0ZXJzW25hbWVdO1xuICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICA8RmlsdGVyU2VsZWN0aW9uXG4gICAgICAgICAgICAgIGtleT17bmFtZX1cbiAgICAgICAgICAgICAgdGl0bGU9e2ZpbHRlci50aXRsZX1cbiAgICAgICAgICAgICAgZGVzY3JpcHRpb249e2ZpbHRlci5kZXNjcmlwdGlvbn1cbiAgICAgICAgICAgICAgaXNFbmFibGVkPXshc2hvd1JlcGxhY2UgfHwgZmlsdGVyLnN1cHBvcnRSZXBsYWNlfVxuICAgICAgICAgICAgICBvblRvZ2dsZT17KCkgPT4ge1xuICAgICAgICAgICAgICAgIGNvbnN0IG5ld0ZpbHRlcjogSUZpbHRlcnMgPSB7fTtcbiAgICAgICAgICAgICAgICBuZXdGaWx0ZXJbbmFtZV0gPSAhdGhpcy5wcm9wcy5maWx0ZXJzW25hbWVdO1xuICAgICAgICAgICAgICAgIHRoaXMucHJvcHMub25GaWx0ZXJzQ2hhbmdlZChuZXdGaWx0ZXIpO1xuICAgICAgICAgICAgICB9fVxuICAgICAgICAgICAgICB2YWx1ZT17dGhpcy5wcm9wcy5maWx0ZXJzW25hbWVdID8/IGZpbHRlci5kZWZhdWx0fVxuICAgICAgICAgICAgLz5cbiAgICAgICAgICApO1xuICAgICAgICB9KX1cbiAgICAgIDwvZGl2PlxuICAgICkgOiBudWxsO1xuICAgIGNvbnN0IGljb24gPSB0aGlzLnByb3BzLnJlcGxhY2VFbnRyeVZpc2libGVcbiAgICAgID8gY2FyZXREb3duSWNvblxuICAgICAgOiBjYXJldFJpZ2h0SWNvbjtcblxuICAgIC8vIFRPRE86IEVycm9yIG1lc3NhZ2VzIGZyb20gcmVnZXggYXJlIG5vdCBjdXJyZW50bHkgbG9jYWxpemFibGUuXG4gICAgcmV0dXJuIChcbiAgICAgIDw+XG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPXtPVkVSTEFZX1JPV19DTEFTU30+XG4gICAgICAgICAge3RoaXMucHJvcHMuaXNSZWFkT25seSA/IChcbiAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPXtUT0dHTEVfUExBQ0VIT0xERVJ9IC8+XG4gICAgICAgICAgKSA6IChcbiAgICAgICAgICAgIDxidXR0b25cbiAgICAgICAgICAgICAgY2xhc3NOYW1lPXtUT0dHTEVfV1JBUFBFUn1cbiAgICAgICAgICAgICAgb25DbGljaz17KCkgPT4gdGhpcy5fb25SZXBsYWNlVG9nZ2xlZCgpfVxuICAgICAgICAgICAgICB0YWJJbmRleD17MH1cbiAgICAgICAgICAgICAgdGl0bGU9e3RyYW5zLl9fKCdUb2dnbGUgUmVwbGFjZScpfVxuICAgICAgICAgICAgPlxuICAgICAgICAgICAgICA8aWNvbi5yZWFjdFxuICAgICAgICAgICAgICAgIGNsYXNzTmFtZT17YCR7UkVQTEFDRV9UT0dHTEVfQ0xBU1N9ICR7QlVUVE9OX0NPTlRFTlRfQ0xBU1N9YH1cbiAgICAgICAgICAgICAgICB0YWc9XCJzcGFuXCJcbiAgICAgICAgICAgICAgICBlbGVtZW50UG9zaXRpb249XCJjZW50ZXJcIlxuICAgICAgICAgICAgICAgIGhlaWdodD1cIjIwcHhcIlxuICAgICAgICAgICAgICAgIHdpZHRoPVwiMjBweFwiXG4gICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICA8L2J1dHRvbj5cbiAgICAgICAgICApfVxuICAgICAgICAgIDxTZWFyY2hFbnRyeVxuICAgICAgICAgICAgaW5wdXRSZWY9e3RoaXMucHJvcHMuc2VhcmNoSW5wdXRSZWZ9XG4gICAgICAgICAgICB1c2VSZWdleD17dGhpcy5wcm9wcy51c2VSZWdleH1cbiAgICAgICAgICAgIGNhc2VTZW5zaXRpdmU9e3RoaXMucHJvcHMuY2FzZVNlbnNpdGl2ZX1cbiAgICAgICAgICAgIG9uQ2FzZVNlbnNpdGl2ZVRvZ2dsZWQ9e3RoaXMucHJvcHMub25DYXNlU2Vuc2l0aXZlVG9nZ2xlZH1cbiAgICAgICAgICAgIG9uUmVnZXhUb2dnbGVkPXt0aGlzLnByb3BzLm9uUmVnZXhUb2dnbGVkfVxuICAgICAgICAgICAgb25LZXlkb3duPXsoZTogUmVhY3QuS2V5Ym9hcmRFdmVudDxIVE1MSW5wdXRFbGVtZW50PikgPT5cbiAgICAgICAgICAgICAgdGhpcy5fb25TZWFyY2hLZXlkb3duKGUpXG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBvbkNoYW5nZT17KGU6IFJlYWN0LkNoYW5nZUV2ZW50KSA9PiB0aGlzLl9vblNlYXJjaENoYW5nZShlKX1cbiAgICAgICAgICAgIHNlYXJjaFRleHQ9e3RoaXMucHJvcHMuc2VhcmNoVGV4dH1cbiAgICAgICAgICAgIHRyYW5zbGF0b3I9e3RoaXMudHJhbnNsYXRvcn1cbiAgICAgICAgICAvPlxuICAgICAgICAgIDxTZWFyY2hJbmRpY2VzXG4gICAgICAgICAgICBjdXJyZW50SW5kZXg9e3RoaXMucHJvcHMuY3VycmVudEluZGV4fVxuICAgICAgICAgICAgdG90YWxNYXRjaGVzPXt0aGlzLnByb3BzLnRvdGFsTWF0Y2hlcyA/PyAwfVxuICAgICAgICAgIC8+XG4gICAgICAgICAgPFVwRG93bkJ1dHRvbnNcbiAgICAgICAgICAgIG9uSGlnaGxpZ2h0UHJldmlvdXM9eygpID0+IHtcbiAgICAgICAgICAgICAgdGhpcy5wcm9wcy5vbkhpZ2hsaWdodFByZXZpb3VzKCk7XG4gICAgICAgICAgICB9fVxuICAgICAgICAgICAgb25IaWdobGlnaHROZXh0PXsoKSA9PiB7XG4gICAgICAgICAgICAgIHRoaXMucHJvcHMub25IaWdobGlnaHROZXh0KCk7XG4gICAgICAgICAgICB9fVxuICAgICAgICAgICAgdHJhbnM9e3RyYW5zfVxuICAgICAgICAgIC8+XG4gICAgICAgICAge3Nob3dSZXBsYWNlID8gbnVsbCA6IGZpbHRlclRvZ2dsZX1cbiAgICAgICAgICA8YnV0dG9uXG4gICAgICAgICAgICBjbGFzc05hbWU9e0JVVFRPTl9XUkFQUEVSX0NMQVNTfVxuICAgICAgICAgICAgb25DbGljaz17KCkgPT4gdGhpcy5fb25DbG9zZSgpfVxuICAgICAgICAgICAgdGFiSW5kZXg9ezB9XG4gICAgICAgICAgPlxuICAgICAgICAgICAgPGNsb3NlSWNvbi5yZWFjdFxuICAgICAgICAgICAgICBjbGFzc05hbWU9XCJqcC1pY29uLWhvdmVyXCJcbiAgICAgICAgICAgICAgZWxlbWVudFBvc2l0aW9uPVwiY2VudGVyXCJcbiAgICAgICAgICAgICAgaGVpZ2h0PVwiMTZweFwiXG4gICAgICAgICAgICAgIHdpZHRoPVwiMTZweFwiXG4gICAgICAgICAgICAvPlxuICAgICAgICAgIDwvYnV0dG9uPlxuICAgICAgICA8L2Rpdj5cbiAgICAgICAgPGRpdiBjbGFzc05hbWU9e09WRVJMQVlfUk9XX0NMQVNTfT5cbiAgICAgICAgICB7c2hvd1JlcGxhY2UgPyAoXG4gICAgICAgICAgICA8PlxuICAgICAgICAgICAgICA8UmVwbGFjZUVudHJ5XG4gICAgICAgICAgICAgICAgb25SZXBsYWNlS2V5ZG93bj17KGU6IFJlYWN0LktleWJvYXJkRXZlbnQpID0+XG4gICAgICAgICAgICAgICAgICB0aGlzLl9vblJlcGxhY2VLZXlkb3duKGUpXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXsoZTogUmVhY3QuQ2hhbmdlRXZlbnQpID0+XG4gICAgICAgICAgICAgICAgICB0aGlzLnByb3BzLm9uUmVwbGFjZUNoYW5nZWQoXG4gICAgICAgICAgICAgICAgICAgIChlLnRhcmdldCBhcyBIVE1MSW5wdXRFbGVtZW50KS52YWx1ZVxuICAgICAgICAgICAgICAgICAgKVxuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICBvblJlcGxhY2VDdXJyZW50PXsoKSA9PiB0aGlzLnByb3BzLm9uUmVwbGFjZUN1cnJlbnQoKX1cbiAgICAgICAgICAgICAgICBvblJlcGxhY2VBbGw9eygpID0+IHRoaXMucHJvcHMub25SZXBsYWNlQWxsKCl9XG4gICAgICAgICAgICAgICAgcmVwbGFjZVRleHQ9e3RoaXMucHJvcHMucmVwbGFjZVRleHR9XG4gICAgICAgICAgICAgICAgdHJhbnNsYXRvcj17dGhpcy50cmFuc2xhdG9yfVxuICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT17U1BBQ0VSX0NMQVNTfT48L2Rpdj5cbiAgICAgICAgICAgICAge2ZpbHRlclRvZ2dsZX1cbiAgICAgICAgICAgIDwvPlxuICAgICAgICAgICkgOiBudWxsfVxuICAgICAgICA8L2Rpdj5cbiAgICAgICAge3RoaXMuc3RhdGUuZmlsdGVyc09wZW4gPyBmaWx0ZXIgOiBudWxsfVxuICAgICAgICB7ISF0aGlzLnByb3BzLmVycm9yTWVzc2FnZSAmJiAoXG4gICAgICAgICAgPGRpdiBjbGFzc05hbWU9e1JFR0VYX0VSUk9SX0NMQVNTfT57dGhpcy5wcm9wcy5lcnJvck1lc3NhZ2V9PC9kaXY+XG4gICAgICAgICl9XG4gICAgICAgIDxkaXYgY2xhc3NOYW1lPXtTRUFSQ0hfRE9DVU1FTlRfTE9BRElOR30+XG4gICAgICAgICAge3RyYW5zLl9fKFxuICAgICAgICAgICAgJ1RoaXMgZG9jdW1lbnQgaXMgc3RpbGwgbG9hZGluZy4gT25seSBsb2FkZWQgY29udGVudCB3aWxsIGFwcGVhciBpbiBzZWFyY2ggcmVzdWx0cyB1bnRpbCB0aGUgZW50aXJlIGRvY3VtZW50IGxvYWRzLidcbiAgICAgICAgICApfVxuICAgICAgICA8L2Rpdj5cbiAgICAgIDwvPlxuICAgICk7XG4gIH1cblxuICBwcm90ZWN0ZWQgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3I7XG59XG5cbi8qKlxuICogU2VhcmNoIGRvY3VtZW50IHdpZGdldFxuICovXG5leHBvcnQgY2xhc3MgU2VhcmNoRG9jdW1lbnRWaWV3IGV4dGVuZHMgVkRvbVJlbmRlcmVyPFNlYXJjaERvY3VtZW50TW9kZWw+IHtcbiAgLyoqXG4gICAqIFNlYXJjaCBkb2N1bWVudCB3aWRnZXQgY29uc3RydWN0b3IuXG4gICAqXG4gICAqIEBwYXJhbSBtb2RlbCBTZWFyY2ggZG9jdW1lbnQgbW9kZWxcbiAgICogQHBhcmFtIHRyYW5zbGF0b3IgQXBwbGljYXRpb24gdHJhbnNsYXRvciBvYmplY3RcbiAgICovXG4gIGNvbnN0cnVjdG9yKG1vZGVsOiBTZWFyY2hEb2N1bWVudE1vZGVsLCBwcm90ZWN0ZWQgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSB7XG4gICAgc3VwZXIobW9kZWwpO1xuICAgIHRoaXMuYWRkQ2xhc3MoT1ZFUkxBWV9DTEFTUyk7XG4gICAgdGhpcy5fc2VhcmNoSW5wdXQgPSBSZWFjdC5jcmVhdGVSZWY8SFRNTElucHV0RWxlbWVudD4oKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBIHNpZ25hbCBlbWl0dGVkIHdoZW4gdGhlIHdpZGdldCBpcyBjbG9zZWQuXG4gICAqXG4gICAqIENsb3NpbmcgdGhlIHdpZGdldCBkZXRhY2hlZCBpdCBmcm9tIHRoZSBET00gYnV0IGRvZXMgbm90IGRpc3Bvc2UgaXQuXG4gICAqL1xuICBnZXQgY2xvc2VkKCk6IElTaWduYWw8U2VhcmNoRG9jdW1lbnRWaWV3LCB2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMuX2Nsb3NlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBGb2N1cyBzZWFyY2ggaW5wdXQuXG4gICAqL1xuICBmb2N1c1NlYXJjaElucHV0KCk6IHZvaWQge1xuICAgIHRoaXMuX3NlYXJjaElucHV0LmN1cnJlbnQ/LnNlbGVjdCgpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0aGUgc2VhcmNoIHRleHRcbiAgICpcbiAgICogSXQgZG9lcyBub3QgdHJpZ2dlciBhIHZpZXcgdXBkYXRlLlxuICAgKi9cbiAgc2V0U2VhcmNoVGV4dChzZWFyY2g6IHN0cmluZyk6IHZvaWQge1xuICAgIHRoaXMubW9kZWwuc2VhcmNoRXhwcmVzc2lvbiA9IHNlYXJjaDtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgdGhlIHJlcGxhY2UgdGV4dFxuICAgKlxuICAgKiBJdCBkb2VzIG5vdCB0cmlnZ2VyIGEgdmlldyB1cGRhdGUuXG4gICAqL1xuICBzZXRSZXBsYWNlVGV4dChyZXBsYWNlOiBzdHJpbmcpOiB2b2lkIHtcbiAgICB0aGlzLm1vZGVsLnJlcGxhY2VUZXh0ID0gcmVwbGFjZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTaG93IHRoZSByZXBsYWNlbWVudCBpbnB1dCBib3guXG4gICAqL1xuICBzaG93UmVwbGFjZSgpOiB2b2lkIHtcbiAgICB0aGlzLnNldFJlcGxhY2VJbnB1dFZpc2liaWxpdHkodHJ1ZSk7XG4gIH1cblxuICBwcm90ZWN0ZWQgc2V0UmVwbGFjZUlucHV0VmlzaWJpbGl0eSh2OiBib29sZWFuKTogdm9pZCB7XG4gICAgaWYgKHRoaXMuX3Nob3dSZXBsYWNlICE9PSB2KSB7XG4gICAgICB0aGlzLl9zaG93UmVwbGFjZSA9IHY7XG4gICAgICB0aGlzLnVwZGF0ZSgpO1xuICAgIH1cbiAgfVxuXG4gIHJlbmRlcigpOiBKU1guRWxlbWVudCB7XG4gICAgcmV0dXJuIChcbiAgICAgIDxTZWFyY2hPdmVybGF5XG4gICAgICAgIGNhc2VTZW5zaXRpdmU9e3RoaXMubW9kZWwuY2FzZVNlbnNpdGl2ZX1cbiAgICAgICAgY3VycmVudEluZGV4PXt0aGlzLm1vZGVsLmN1cnJlbnRJbmRleH1cbiAgICAgICAgaXNSZWFkT25seT17dGhpcy5tb2RlbC5pc1JlYWRPbmx5fVxuICAgICAgICBlcnJvck1lc3NhZ2U9e3RoaXMubW9kZWwucGFyc2luZ0Vycm9yfVxuICAgICAgICBmaWx0ZXJzPXt0aGlzLm1vZGVsLmZpbHRlcnN9XG4gICAgICAgIGZpbHRlcnNEZWZpbml0aW9uPXt0aGlzLm1vZGVsLmZpbHRlcnNEZWZpbml0aW9ufVxuICAgICAgICByZXBsYWNlRW50cnlWaXNpYmxlPXt0aGlzLl9zaG93UmVwbGFjZX1cbiAgICAgICAgcmVwbGFjZVRleHQ9e3RoaXMubW9kZWwucmVwbGFjZVRleHR9XG4gICAgICAgIHNlYXJjaFRleHQ9e3RoaXMubW9kZWwuc2VhcmNoRXhwcmVzc2lvbn1cbiAgICAgICAgc2VhcmNoSW5wdXRSZWY9e3RoaXMuX3NlYXJjaElucHV0fVxuICAgICAgICB0b3RhbE1hdGNoZXM9e3RoaXMubW9kZWwudG90YWxNYXRjaGVzfVxuICAgICAgICB0cmFuc2xhdG9yPXt0aGlzLnRyYW5zbGF0b3J9XG4gICAgICAgIHVzZVJlZ2V4PXt0aGlzLm1vZGVsLnVzZVJlZ2V4fVxuICAgICAgICBvbkNhc2VTZW5zaXRpdmVUb2dnbGVkPXsoKSA9PiB7XG4gICAgICAgICAgdGhpcy5tb2RlbC5jYXNlU2Vuc2l0aXZlID0gIXRoaXMubW9kZWwuY2FzZVNlbnNpdGl2ZTtcbiAgICAgICAgfX1cbiAgICAgICAgb25SZWdleFRvZ2dsZWQ9eygpID0+IHtcbiAgICAgICAgICB0aGlzLm1vZGVsLnVzZVJlZ2V4ID0gIXRoaXMubW9kZWwudXNlUmVnZXg7XG4gICAgICAgIH19XG4gICAgICAgIG9uRmlsdGVyc0NoYW5nZWQ9eyhmaWx0ZXJzOiBJRmlsdGVycykgPT4ge1xuICAgICAgICAgIHRoaXMubW9kZWwuZmlsdGVycyA9IHsgLi4udGhpcy5tb2RlbC5maWx0ZXJzLCAuLi5maWx0ZXJzIH07XG4gICAgICAgIH19XG4gICAgICAgIG9uSGlnaGxpZ2h0TmV4dD17KCkgPT4ge1xuICAgICAgICAgIHZvaWQgdGhpcy5tb2RlbC5oaWdobGlnaHROZXh0KCk7XG4gICAgICAgIH19XG4gICAgICAgIG9uSGlnaGxpZ2h0UHJldmlvdXM9eygpID0+IHtcbiAgICAgICAgICB2b2lkIHRoaXMubW9kZWwuaGlnaGxpZ2h0UHJldmlvdXMoKTtcbiAgICAgICAgfX1cbiAgICAgICAgb25TZWFyY2hDaGFuZ2VkPXsocTogc3RyaW5nKSA9PiB7XG4gICAgICAgICAgdGhpcy5tb2RlbC5zZWFyY2hFeHByZXNzaW9uID0gcTtcbiAgICAgICAgfX1cbiAgICAgICAgb25DbG9zZT17YXN5bmMgKCkgPT4ge1xuICAgICAgICAgIFdpZGdldC5kZXRhY2godGhpcyk7XG4gICAgICAgICAgdGhpcy5fY2xvc2VkLmVtaXQoKTtcbiAgICAgICAgICBhd2FpdCB0aGlzLm1vZGVsLmVuZFF1ZXJ5KCk7XG4gICAgICAgIH19XG4gICAgICAgIG9uUmVwbGFjZUVudHJ5U2hvd249eyh2OiBib29sZWFuKSA9PiB7XG4gICAgICAgICAgdGhpcy5zZXRSZXBsYWNlSW5wdXRWaXNpYmlsaXR5KHYpO1xuICAgICAgICB9fVxuICAgICAgICBvblJlcGxhY2VDaGFuZ2VkPXsocTogc3RyaW5nKSA9PiB7XG4gICAgICAgICAgdGhpcy5tb2RlbC5yZXBsYWNlVGV4dCA9IHE7XG4gICAgICAgIH19XG4gICAgICAgIG9uUmVwbGFjZUN1cnJlbnQ9eygpID0+IHtcbiAgICAgICAgICB2b2lkIHRoaXMubW9kZWwucmVwbGFjZUN1cnJlbnRNYXRjaCgpO1xuICAgICAgICB9fVxuICAgICAgICBvblJlcGxhY2VBbGw9eygpID0+IHtcbiAgICAgICAgICB2b2lkIHRoaXMubW9kZWwucmVwbGFjZUFsbE1hdGNoZXMoKTtcbiAgICAgICAgfX1cbiAgICAgID48L1NlYXJjaE92ZXJsYXk+XG4gICAgKTtcbiAgfVxuXG4gIHByaXZhdGUgX3NlYXJjaElucHV0OiBSZWFjdC5SZWZPYmplY3Q8SFRNTElucHV0RWxlbWVudD47XG4gIHByaXZhdGUgX3Nob3dSZXBsYWNlID0gZmFsc2U7XG4gIHByaXZhdGUgX2Nsb3NlZCA9IG5ldyBTaWduYWw8dGhpcywgdm9pZD4odGhpcyk7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgVG9rZW4gfSBmcm9tICdAbHVtaW5vL2NvcmV1dGlscyc7XG5pbXBvcnQgeyBJRGlzcG9zYWJsZSB9IGZyb20gJ0BsdW1pbm8vZGlzcG9zYWJsZSc7XG5pbXBvcnQgeyBJU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuLyoqXG4gKiBUaGUgc2VhcmNoIHByb3ZpZGVyIHJlZ2lzdHJ5IHRva2VuLlxuICovXG5leHBvcnQgY29uc3QgSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnkgPSBuZXcgVG9rZW48SVNlYXJjaFByb3ZpZGVyUmVnaXN0cnk+KFxuICAnQGp1cHl0ZXJsYWIvZG9jdW1lbnRzZWFyY2g6SVNlYXJjaFByb3ZpZGVyUmVnaXN0cnknXG4pO1xuXG4vKipcbiAqIEZpbHRlciBpbnRlcmZhY2VcbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRmlsdGVyIHtcbiAgLyoqXG4gICAqIEZpbHRlciB0aXRsZVxuICAgKi9cbiAgdGl0bGU6IHN0cmluZztcbiAgLyoqXG4gICAqIEZpbHRlciBkZXNjcmlwdGlvblxuICAgKi9cbiAgZGVzY3JpcHRpb246IHN0cmluZztcbiAgLyoqXG4gICAqIERlZmF1bHQgdmFsdWVcbiAgICovXG4gIGRlZmF1bHQ6IGJvb2xlYW47XG4gIC8qKlxuICAgKiBEb2VzIHRoZSBmaWx0ZXIgc3VwcG9ydCByZXBsYWNlP1xuICAgKi9cbiAgc3VwcG9ydFJlcGxhY2U6IGJvb2xlYW47XG59XG5cbi8qKlxuICogVHlwZSBvZiBmaWx0ZXJzXG4gKlxuICogVE9ETyBzdXBwb3J0IGFkZGl0aW9uYWwgZmlsdGVyIHR5cGVcbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJRmlsdGVycyB7XG4gIC8qKlxuICAgKiBGaWx0ZXIgbmFtZTogdmFsdWVcbiAgICovXG4gIFtrZXk6IHN0cmluZ106IGJvb2xlYW47XG59XG5cbi8qKlxuICogUmVhY3Qgc2VhcmNoIGNvbXBvbmVudCBzdGF0ZVxuICovXG5leHBvcnQgaW50ZXJmYWNlIElEaXNwbGF5U3RhdGUge1xuICAvKipcbiAgICogVGhlIGluZGV4IG9mIHRoZSBjdXJyZW50bHkgc2VsZWN0ZWQgbWF0Y2hcbiAgICovXG4gIGN1cnJlbnRJbmRleDogbnVtYmVyIHwgbnVsbDtcblxuICAvKipcbiAgICogVGhlIHRvdGFsIG51bWJlciBvZiBtYXRjaGVzIGZvdW5kIGluIHRoZSBkb2N1bWVudFxuICAgKi9cbiAgdG90YWxNYXRjaGVzOiBudW1iZXI7XG5cbiAgLyoqXG4gICAqIFNob3VsZCB0aGUgc2VhcmNoIGJlIGNhc2Ugc2Vuc2l0aXZlP1xuICAgKi9cbiAgY2FzZVNlbnNpdGl2ZTogYm9vbGVhbjtcblxuICAvKipcbiAgICogU2hvdWxkIHRoZSBzZWFyY2ggc3RyaW5nIGJlIHRyZWF0ZWQgYXMgYSBSZWdFeHA/XG4gICAqL1xuICB1c2VSZWdleDogYm9vbGVhbjtcblxuICAvKipcbiAgICogVGhlIHRleHQgaW4gdGhlIHNlYXJjaCBlbnRyeVxuICAgKi9cbiAgc2VhcmNoVGV4dDogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBUaGUgcXVlcnkgY29uc3RydWN0ZWQgZnJvbSB0aGUgdGV4dCBhbmQgdGhlIGNhc2UvcmVnZXggZmxhZ3NcbiAgICovXG4gIHF1ZXJ5OiBSZWdFeHAgfCBudWxsO1xuXG4gIC8qKlxuICAgKiBBbiBlcnJvciBtZXNzYWdlICh1c2VkIGZvciBiYWQgcmVnZXggc3ludGF4KVxuICAgKi9cbiAgZXJyb3JNZXNzYWdlOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFNob3VsZCB0aGUgZm9jdXMgZm9yY2VkIGludG8gdGhlIGlucHV0IG9uIHRoZSBuZXh0IHJlbmRlcj9cbiAgICovXG4gIGZvcmNlRm9jdXM6IGJvb2xlYW47XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgb3Igbm90IHRoZSBzZWFyY2ggaW5wdXQgaXMgY3VycmVudGx5IGZvY3VzZWRcbiAgICovXG4gIHNlYXJjaElucHV0Rm9jdXNlZDogYm9vbGVhbjtcblxuICAvKipcbiAgICogV2hldGhlciBvciBub3QgdGhlIHJlcGxhY2UgaW5wdXQgaXMgY3VycmVudGx5IGZvY3VzZWRcbiAgICovXG4gIHJlcGxhY2VJbnB1dEZvY3VzZWQ6IGJvb2xlYW47XG5cbiAgLyoqXG4gICAqIFRoZSB0ZXh0IGluIHRoZSByZXBsYWNlIGVudHJ5XG4gICAqL1xuICByZXBsYWNlVGV4dDogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBXaGV0aGVyIG9yIG5vdCB0aGUgcmVwbGFjZSBlbnRyeSByb3cgaXMgdmlzaWJsZVxuICAgKi9cbiAgcmVwbGFjZUVudHJ5VmlzaWJsZTogYm9vbGVhbjtcblxuICAvKipcbiAgICogV2hhdCBzaG91bGQgd2UgaW5jbHVkZSB3aGVuIHdlIHNlYXJjaD9cbiAgICovXG4gIGZpbHRlcnM6IElGaWx0ZXJzO1xuXG4gIC8qKlxuICAgKiBJcyB0aGUgZmlsdGVycyB2aWV3IG9wZW4/XG4gICAqL1xuICBmaWx0ZXJzT3BlbjogYm9vbGVhbjtcbn1cblxuLyoqXG4gKiBCYXNlIHNlYXJjaCBtYXRjaCBpbnRlcmZhY2VcbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJU2VhcmNoTWF0Y2gge1xuICAvKipcbiAgICogVGV4dCBvZiB0aGUgZXhhY3QgbWF0Y2ggaXRzZWxmXG4gICAqL1xuICByZWFkb25seSB0ZXh0OiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFN0YXJ0IGxvY2F0aW9uIG9mIHRoZSBtYXRjaCAoaW4gYSB0ZXh0LCB0aGlzIGlzIHRoZSBjb2x1bW4pXG4gICAqL1xuICBwb3NpdGlvbjogbnVtYmVyO1xufVxuXG4vKipcbiAqIEhUTUwgc2VhcmNoIG1hdGNoIGludGVyZmFjZVxuICovXG5leHBvcnQgaW50ZXJmYWNlIElIVE1MU2VhcmNoTWF0Y2ggZXh0ZW5kcyBJU2VhcmNoTWF0Y2gge1xuICAvKipcbiAgICogTm9kZSBjb250YWluaW5nIHRoZSBtYXRjaFxuICAgKi9cbiAgcmVhZG9ubHkgbm9kZTogVGV4dDtcbn1cblxuLyoqXG4gKiBJbnRlcmZhY2UgZm9yIHNlYXJjaCBwcm92aWRlciBmYWN0b3J5XG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVNlYXJjaFByb3ZpZGVyRmFjdG9yeTxUIGV4dGVuZHMgV2lkZ2V0ID0gV2lkZ2V0PiB7XG4gIC8qKlxuICAgKiBJbnN0YW50aWF0ZSBhIHNlYXJjaCBwcm92aWRlciBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGUgd2lkZ2V0IHByb3ZpZGVkIGlzIGFsd2F5cyBjaGVja2VkIHVzaW5nIGBpc0FwcGxpY2FibGVgIGJlZm9yZSBjYWxsaW5nXG4gICAqIHRoaXMgZmFjdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCBUaGUgd2lkZ2V0IHRvIHNlYXJjaCBvblxuICAgKiBAcGFyYW0gdHJhbnNsYXRvciBbb3B0aW9uYWxdIFRoZSB0cmFuc2xhdG9yIG9iamVjdFxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgc2VhcmNoIHByb3ZpZGVyIG9uIHRoZSB3aWRnZXRcbiAgICovXG4gIHJlYWRvbmx5IGNyZWF0ZU5ldzogKHdpZGdldDogVCwgdHJhbnNsYXRvcj86IElUcmFuc2xhdG9yKSA9PiBJU2VhcmNoUHJvdmlkZXI7XG5cbiAgLyoqXG4gICAqIFJlcG9ydCB3aGV0aGVyIG9yIG5vdCB0aGlzIHByb3ZpZGVyIGhhcyB0aGUgYWJpbGl0eSB0byBzZWFyY2ggb24gdGhlXG4gICAqIGdpdmVuIHdpZGdldC4gVGhlIGZ1bmN0aW9uIGlzIGEgdHlwZSBndWFyZCwgbWVhbmluZyB0aGF0IGl0IHJldHVybnNcbiAgICogYSBib29sZWFuLCBidXQgaGFzIGEgdHlwZSBwcmVkaWNhdGUgKGB4IGlzIFRgKSBmb3IgaXRzIHJldHVybiBzaWduYXR1cmUuXG4gICAqXG4gICAqIEBwYXJhbSBkb21haW4gV2lkZ2V0IHRvIHRlc3RcbiAgICovXG4gIHJlYWRvbmx5IGlzQXBwbGljYWJsZTogKGRvbWFpbjogV2lkZ2V0KSA9PiBkb21haW4gaXMgVDtcbn1cblxuLyoqXG4gKiBTZWFyY2ggcHJvdmlkZXIgcmVnaXN0cnkgaW50ZXJmYWNlXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnkge1xuICAvKipcbiAgICogQWRkIGEgcHJvdmlkZXIgdG8gdGhlIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIHByb3ZpZGVyIGtleS5cbiAgICogQHJldHVybnMgQSBkaXNwb3NhYmxlIGRlbGVnYXRlIHRoYXQsIHdoZW4gZGlzcG9zZWQsIGRlcmVnaXN0ZXJzIHRoZSBnaXZlbiBzZWFyY2ggcHJvdmlkZXJcbiAgICovXG4gIGFkZChrZXk6IHN0cmluZywgcHJvdmlkZXI6IElTZWFyY2hQcm92aWRlckZhY3Rvcnk8V2lkZ2V0Pik6IElEaXNwb3NhYmxlO1xuXG4gIC8qKlxuICAgKiBSZXR1cm5zIGEgbWF0Y2hpbmcgcHJvdmlkZXIgZm9yIHRoZSB3aWRnZXQuXG4gICAqXG4gICAqIEBwYXJhbSB3aWRnZXQgLSBUaGUgd2lkZ2V0IHRvIHNlYXJjaCBvdmVyLlxuICAgKiBAcmV0dXJucyB0aGUgc2VhcmNoIHByb3ZpZGVyLCBvciB1bmRlZmluZWQgaWYgbm9uZSBleGlzdHMuXG4gICAqL1xuICBnZXRQcm92aWRlcih3aWRnZXQ6IFdpZGdldCk6IElTZWFyY2hQcm92aWRlciB8IHVuZGVmaW5lZDtcblxuICAvKipcbiAgICogV2hldGhlciB0aGUgcmVnaXN0cnkgYXMgYSBtYXRjaGluZyBwcm92aWRlciBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCAtIFRoZSB3aWRnZXQgdG8gc2VhcmNoIG92ZXIuXG4gICAqIEByZXR1cm5zIFByb3ZpZGVyIGV4aXN0ZW5jZVxuICAgKi9cbiAgaGFzUHJvdmlkZXIod2lkZ2V0OiBXaWRnZXQpOiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBTaWduYWwgdGhhdCBlbWl0cyB3aGVuIGEgbmV3IHNlYXJjaCBwcm92aWRlciBoYXMgYmVlbiByZWdpc3RlcmVkXG4gICAqIG9yIHJlbW92ZWQuXG4gICAqL1xuICBjaGFuZ2VkOiBJU2lnbmFsPElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5LCB2b2lkPjtcbn1cblxuLyoqXG4gKiBCYXNlIHNlYXJjaCBwcm92aWRlciBpbnRlcmZhY2VcbiAqXG4gKiAjIyMjIE5vdGVzXG4gKiBJdCBpcyBpbXBsZW1lbnRlZCBieSBzdWJwcm92aWRlciBsaWtlIHNlYXJjaGluZyBvbiBhIHNpbmdsZSBjZWxsLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElCYXNlU2VhcmNoUHJvdmlkZXIgZXh0ZW5kcyBJRGlzcG9zYWJsZSB7XG4gIC8qKlxuICAgKiBTdGFydCBhIHNlYXJjaFxuICAgKlxuICAgKiBAcGFyYW0gcXVlcnkgUmVndWxhciBleHByZXNzaW9uIHRvIHRlc3QgZm9yXG4gICAqIEBwYXJhbSBmaWx0ZXJzIEZpbHRlcnMgdG8gYXBwbHkgd2hlbiBzZWFyY2hpbmdcbiAgICovXG4gIHN0YXJ0UXVlcnkocXVlcnk6IFJlZ0V4cCwgZmlsdGVyczogSUZpbHRlcnMpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBTdG9wIGEgc2VhcmNoIGFuZCBjbGVhciBhbnkgaW50ZXJuYWwgc3RhdGUgb2YgdGhlIHByb3ZpZGVyXG4gICAqL1xuICBlbmRRdWVyeSgpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBDbGVhciBjdXJyZW50bHkgaGlnaGxpZ2h0ZWQgbWF0Y2guXG4gICAqL1xuICBjbGVhckhpZ2hsaWdodCgpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBIaWdobGlnaHQgdGhlIG5leHQgbWF0Y2hcbiAgICpcbiAgICogQHBhcmFtIGxvb3AgV2hldGhlciB0byBsb29wIHdpdGhpbiB0aGUgbWF0Y2hlcyBsaXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgbmV4dCBtYXRjaCBpZiBpdCBleGlzdHNcbiAgICovXG4gIGhpZ2hsaWdodE5leHQobG9vcD86IGJvb2xlYW4pOiBQcm9taXNlPElTZWFyY2hNYXRjaCB8IHVuZGVmaW5lZD47XG5cbiAgLyoqXG4gICAqIEhpZ2hsaWdodCB0aGUgcHJldmlvdXMgbWF0Y2hcbiAgICpcbiAgICogQHBhcmFtIGxvb3AgV2hldGhlciB0byBsb29wIHdpdGhpbiB0aGUgbWF0Y2hlcyBsaXN0LlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgcHJldmlvdXMgbWF0Y2ggaWYgaXQgZXhpc3RzLlxuICAgKi9cbiAgaGlnaGxpZ2h0UHJldmlvdXMobG9vcD86IGJvb2xlYW4pOiBQcm9taXNlPElTZWFyY2hNYXRjaCB8IHVuZGVmaW5lZD47XG5cbiAgLyoqXG4gICAqIFJlcGxhY2UgdGhlIGN1cnJlbnRseSBzZWxlY3RlZCBtYXRjaCB3aXRoIHRoZSBwcm92aWRlZCB0ZXh0XG4gICAqIGFuZCBoaWdobGlnaHQgdGhlIG5leHQgbWF0Y2guXG4gICAqXG4gICAqIEBwYXJhbSBuZXdUZXh0IFRoZSByZXBsYWNlbWVudCB0ZXh0XG4gICAqIEBwYXJhbSBsb29wIFdoZXRoZXIgdG8gbG9vcCB3aXRoaW4gdGhlIG1hdGNoZXMgbGlzdC5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2l0aCBhIGJvb2xlYW4gaW5kaWNhdGluZyB3aGV0aGVyIGEgcmVwbGFjZSBvY2N1cnJlZC5cbiAgICovXG4gIHJlcGxhY2VDdXJyZW50TWF0Y2gobmV3VGV4dDogc3RyaW5nLCBsb29wPzogYm9vbGVhbik6IFByb21pc2U8Ym9vbGVhbj47XG5cbiAgLyoqXG4gICAqIFJlcGxhY2UgYWxsIG1hdGNoZXMgaW4gdGhlIHdpZGdldCB3aXRoIHRoZSBwcm92aWRlZCB0ZXh0XG4gICAqXG4gICAqIEBwYXJhbSBuZXdUZXh0IFRoZSByZXBsYWNlbWVudCB0ZXh0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aXRoIGEgYm9vbGVhbiBpbmRpY2F0aW5nIHdoZXRoZXIgYSByZXBsYWNlIG9jY3VycmVkLlxuICAgKi9cbiAgcmVwbGFjZUFsbE1hdGNoZXMobmV3VGV4dDogc3RyaW5nKTogUHJvbWlzZTxib29sZWFuPjtcblxuICAvKipcbiAgICogU2lnbmFsIGluZGljYXRpbmcgdGhhdCBzb21ldGhpbmcgaW4gdGhlIHNlYXJjaCBoYXMgY2hhbmdlZCwgc28gdGhlIFVJIHNob3VsZCB1cGRhdGVcbiAgICovXG4gIHJlYWRvbmx5IHN0YXRlQ2hhbmdlZDogSVNpZ25hbDxJQmFzZVNlYXJjaFByb3ZpZGVyLCB2b2lkPjtcblxuICAvKipcbiAgICogVGhlIGN1cnJlbnQgaW5kZXggb2YgdGhlIHNlbGVjdGVkIG1hdGNoLlxuICAgKi9cbiAgcmVhZG9ubHkgY3VycmVudE1hdGNoSW5kZXg6IG51bWJlciB8IG51bGw7XG5cbiAgLyoqXG4gICAqIFRoZSBudW1iZXIgb2YgbWF0Y2hlcy5cbiAgICovXG4gIHJlYWRvbmx5IG1hdGNoZXNDb3VudDogbnVtYmVyIHwgbnVsbDtcbn1cblxuLyoqXG4gKiBTZWFyY2ggcHJvdmlkZXIgaW50ZXJmYWNlXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVNlYXJjaFByb3ZpZGVyIGV4dGVuZHMgSUJhc2VTZWFyY2hQcm92aWRlciB7XG4gIC8qKlxuICAgKiBHZXQgYW4gaW5pdGlhbCBxdWVyeSB2YWx1ZSBpZiBhcHBsaWNhYmxlIHNvIHRoYXQgaXQgY2FuIGJlIGVudGVyZWRcbiAgICogaW50byB0aGUgc2VhcmNoIGJveCBhcyBhbiBpbml0aWFsIHF1ZXJ5XG4gICAqXG4gICAqIEByZXR1cm5zIEluaXRpYWwgdmFsdWUgdXNlZCB0byBwb3B1bGF0ZSB0aGUgc2VhcmNoIGJveC5cbiAgICovXG4gIGdldEluaXRpYWxRdWVyeSgpOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFNldCB0byB0cnVlIGlmIHRoZSB3aWRnZXQgdW5kZXIgc2VhcmNoIGlzIHJlYWQtb25seSwgZmFsc2VcbiAgICogaWYgaXQgaXMgZWRpdGFibGUuICBXaWxsIGJlIHVzZWQgdG8gZGV0ZXJtaW5lIHdoZXRoZXIgdG8gc2hvd1xuICAgKiB0aGUgcmVwbGFjZSBvcHRpb24uXG4gICAqL1xuICByZWFkb25seSBpc1JlYWRPbmx5OiBib29sZWFuO1xuXG4gIC8qKlxuICAgKiBHZXQgdGhlIGZpbHRlcnMgZGVmaW5pdGlvbiBmb3IgdGhlIGdpdmVuIHByb3ZpZGVyLlxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgZmlsdGVycyBkZWZpbml0aW9uLlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogVE9ETyBGb3Igbm93IGl0IG9ubHkgc3VwcG9ydHMgYm9vbGVhbiBmaWx0ZXJzIChyZXByZXNlbnRlZCB3aXRoIGNoZWNrYm94ZXMpXG4gICAqL1xuICBnZXRGaWx0ZXJzPygpOiB7IFtrZXk6IHN0cmluZ106IElGaWx0ZXIgfTtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==