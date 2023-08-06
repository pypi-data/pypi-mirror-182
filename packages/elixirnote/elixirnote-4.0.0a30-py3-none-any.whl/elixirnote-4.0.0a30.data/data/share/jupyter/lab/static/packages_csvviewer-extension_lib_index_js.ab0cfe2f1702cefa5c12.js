"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_csvviewer-extension_lib_index_js"],{

/***/ "../../packages/csvviewer-extension/lib/index.js":
/*!*******************************************************!*\
  !*** ../../packages/csvviewer-extension/lib/index.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/csvviewer */ "webpack/sharing/consume/default/@jupyterlab/csvviewer/@jupyterlab/csvviewer");
/* harmony import */ var _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/documentsearch */ "webpack/sharing/consume/default/@jupyterlab/documentsearch/@jupyterlab/documentsearch");
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/datagrid */ "webpack/sharing/consume/default/@lumino/datagrid/@lumino/datagrid");
/* harmony import */ var _lumino_datagrid__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_datagrid__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _searchprovider__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./searchprovider */ "../../packages/csvviewer-extension/lib/searchprovider.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module csvviewer-extension
 */









/**
 * The name of the factories that creates widgets.
 */
const FACTORY_CSV = 'CSVTable';
const FACTORY_TSV = 'TSVTable';
/**
 * The command IDs used by the csvviewer plugins.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.CSVGoToLine = 'csv:go-to-line';
    CommandIDs.TSVGoToLine = 'tsv:go-to-line';
})(CommandIDs || (CommandIDs = {}));
/**
 * The CSV file handler extension.
 */
const csv = {
    activate: activateCsv,
    id: '@jupyterlab/csvviewer-extension:csv',
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    optional: [
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager,
        _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__.IMainMenu,
        _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_3__.ISearchProviderRegistry,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IToolbarWidgetRegistry
    ],
    autoStart: true
};
/**
 * The TSV file handler extension.
 */
const tsv = {
    activate: activateTsv,
    id: '@jupyterlab/csvviewer-extension:tsv',
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator],
    optional: [
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager,
        _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_4__.IMainMenu,
        _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_3__.ISearchProviderRegistry,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IToolbarWidgetRegistry
    ],
    autoStart: true
};
/**
 * Activate cssviewer extension for CSV files
 */
function activateCsv(app, translator, restorer, themeManager, mainMenu, searchRegistry, settingRegistry, toolbarRegistry) {
    const { commands, shell } = app;
    let toolbarFactory;
    if (toolbarRegistry) {
        toolbarRegistry.addFactory(FACTORY_CSV, 'delimiter', widget => new _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__.CSVDelimiter({
            widget: widget.content,
            translator
        }));
        if (settingRegistry) {
            toolbarFactory = (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.createToolbarFactory)(toolbarRegistry, settingRegistry, FACTORY_CSV, csv.id, translator);
        }
    }
    const trans = translator.load('jupyterlab');
    const factory = new _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__.CSVViewerFactory({
        name: FACTORY_CSV,
        label: trans.__('CSV Viewer'),
        fileTypes: ['csv'],
        defaultFor: ['csv'],
        readOnly: true,
        toolbarFactory,
        translator
    });
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'csvviewer'
    });
    // The current styles for the data grids.
    let style = Private.LIGHT_STYLE;
    let rendererConfig = Private.LIGHT_TEXT_CONFIG;
    if (restorer) {
        // Handle state restoration.
        void restorer.restore(tracker, {
            command: 'docmanager:open',
            args: widget => ({ path: widget.context.path, factory: FACTORY_CSV }),
            name: widget => widget.context.path
        });
    }
    app.docRegistry.addWidgetFactory(factory);
    const ft = app.docRegistry.getFileType('csv');
    factory.widgetCreated.connect((sender, widget) => {
        // Track the widget.
        void tracker.add(widget);
        // Notify the widget tracker if restore data needs to update.
        widget.context.pathChanged.connect(() => {
            void tracker.save(widget);
        });
        if (ft) {
            widget.title.icon = ft.icon;
            widget.title.iconClass = ft.iconClass;
            widget.title.iconLabel = ft.iconLabel;
        }
        // Set the theme for the new widget.
        widget.content.style = style;
        widget.content.rendererConfig = rendererConfig;
    });
    // Keep the themes up-to-date.
    const updateThemes = () => {
        const isLight = themeManager && themeManager.theme
            ? themeManager.isLight(themeManager.theme)
            : true;
        style = isLight ? Private.LIGHT_STYLE : Private.DARK_STYLE;
        rendererConfig = isLight
            ? Private.LIGHT_TEXT_CONFIG
            : Private.DARK_TEXT_CONFIG;
        tracker.forEach(grid => {
            grid.content.style = style;
            grid.content.rendererConfig = rendererConfig;
        });
    };
    if (themeManager) {
        themeManager.themeChanged.connect(updateThemes);
    }
    // Add commands
    const isEnabled = () => tracker.currentWidget !== null &&
        tracker.currentWidget === shell.currentWidget;
    commands.addCommand(CommandIDs.CSVGoToLine, {
        label: trans.__('Go to Line'),
        execute: async () => {
            const widget = tracker.currentWidget;
            if (widget === null) {
                return;
            }
            const result = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getNumber({
                title: trans.__('Go to Line'),
                value: 0
            });
            if (result.button.accept && result.value !== null) {
                widget.content.goToLine(result.value);
            }
        },
        isEnabled
    });
    if (mainMenu) {
        // Add go to line capability to the edit menu.
        mainMenu.editMenu.goToLiners.add({
            id: CommandIDs.CSVGoToLine,
            isEnabled
        });
    }
    if (searchRegistry) {
        searchRegistry.add('csv', _searchprovider__WEBPACK_IMPORTED_MODULE_8__.CSVSearchProvider);
    }
}
/**
 * Activate cssviewer extension for TSV files
 */
function activateTsv(app, translator, restorer, themeManager, mainMenu, searchRegistry, settingRegistry, toolbarRegistry) {
    const { commands, shell } = app;
    let toolbarFactory;
    if (toolbarRegistry) {
        toolbarRegistry.addFactory(FACTORY_TSV, 'delimiter', widget => new _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__.CSVDelimiter({
            widget: widget.content,
            translator
        }));
        if (settingRegistry) {
            toolbarFactory = (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.createToolbarFactory)(toolbarRegistry, settingRegistry, FACTORY_TSV, tsv.id, translator);
        }
    }
    const trans = translator.load('jupyterlab');
    const factory = new _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_2__.TSVViewerFactory({
        name: FACTORY_TSV,
        label: trans.__('TSV Viewer'),
        fileTypes: ['tsv'],
        defaultFor: ['tsv'],
        readOnly: true,
        toolbarFactory,
        translator
    });
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'tsvviewer'
    });
    // The current styles for the data grids.
    let style = Private.LIGHT_STYLE;
    let rendererConfig = Private.LIGHT_TEXT_CONFIG;
    if (restorer) {
        // Handle state restoration.
        void restorer.restore(tracker, {
            command: 'docmanager:open',
            args: widget => ({ path: widget.context.path, factory: FACTORY_TSV }),
            name: widget => widget.context.path
        });
    }
    app.docRegistry.addWidgetFactory(factory);
    const ft = app.docRegistry.getFileType('tsv');
    factory.widgetCreated.connect((sender, widget) => {
        // Track the widget.
        void tracker.add(widget);
        // Notify the widget tracker if restore data needs to update.
        widget.context.pathChanged.connect(() => {
            void tracker.save(widget);
        });
        if (ft) {
            widget.title.icon = ft.icon;
            widget.title.iconClass = ft.iconClass;
            widget.title.iconLabel = ft.iconLabel;
        }
        // Set the theme for the new widget.
        widget.content.style = style;
        widget.content.rendererConfig = rendererConfig;
    });
    // Keep the themes up-to-date.
    const updateThemes = () => {
        const isLight = themeManager && themeManager.theme
            ? themeManager.isLight(themeManager.theme)
            : true;
        style = isLight ? Private.LIGHT_STYLE : Private.DARK_STYLE;
        rendererConfig = isLight
            ? Private.LIGHT_TEXT_CONFIG
            : Private.DARK_TEXT_CONFIG;
        tracker.forEach(grid => {
            grid.content.style = style;
            grid.content.rendererConfig = rendererConfig;
        });
    };
    if (themeManager) {
        themeManager.themeChanged.connect(updateThemes);
    }
    // Add commands
    const isEnabled = () => tracker.currentWidget !== null &&
        tracker.currentWidget === shell.currentWidget;
    commands.addCommand(CommandIDs.TSVGoToLine, {
        label: trans.__('Go to Line'),
        execute: async () => {
            const widget = tracker.currentWidget;
            if (widget === null) {
                return;
            }
            const result = await _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.InputDialog.getNumber({
                title: trans.__('Go to Line'),
                value: 0
            });
            if (result.button.accept && result.value !== null) {
                widget.content.goToLine(result.value);
            }
        },
        isEnabled
    });
    if (mainMenu) {
        // Add go to line capability to the edit menu.
        mainMenu.editMenu.goToLiners.add({
            id: CommandIDs.TSVGoToLine,
            isEnabled
        });
    }
    if (searchRegistry) {
        searchRegistry.add('tsv', _searchprovider__WEBPACK_IMPORTED_MODULE_8__.CSVSearchProvider);
    }
}
/**
 * Export the plugins as default.
 */
const plugins = [csv, tsv];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);
/**
 * A namespace for private data.
 */
var Private;
(function (Private) {
    /**
     * The light theme for the data grid.
     */
    Private.LIGHT_STYLE = Object.assign(Object.assign({}, _lumino_datagrid__WEBPACK_IMPORTED_MODULE_7__.DataGrid.defaultStyle), { voidColor: '#F3F3F3', backgroundColor: 'white', headerBackgroundColor: '#EEEEEE', gridLineColor: 'rgba(20, 20, 20, 0.15)', headerGridLineColor: 'rgba(20, 20, 20, 0.25)', rowBackgroundColor: i => (i % 2 === 0 ? '#F5F5F5' : 'white') });
    /**
     * The dark theme for the data grid.
     */
    Private.DARK_STYLE = Object.assign(Object.assign({}, _lumino_datagrid__WEBPACK_IMPORTED_MODULE_7__.DataGrid.defaultStyle), { voidColor: 'black', backgroundColor: '#111111', headerBackgroundColor: '#424242', gridLineColor: 'rgba(235, 235, 235, 0.15)', headerGridLineColor: 'rgba(235, 235, 235, 0.25)', rowBackgroundColor: i => (i % 2 === 0 ? '#212121' : '#111111') });
    /**
     * The light config for the data grid renderer.
     */
    Private.LIGHT_TEXT_CONFIG = {
        textColor: '#111111',
        matchBackgroundColor: '#FFFFE0',
        currentMatchBackgroundColor: '#FFFF00',
        horizontalAlignment: 'right'
    };
    /**
     * The dark config for the data grid renderer.
     */
    Private.DARK_TEXT_CONFIG = {
        textColor: '#F5F5F5',
        matchBackgroundColor: '#838423',
        currentMatchBackgroundColor: '#A3807A',
        horizontalAlignment: 'right'
    };
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/csvviewer-extension/lib/searchprovider.js":
/*!****************************************************************!*\
  !*** ../../packages/csvviewer-extension/lib/searchprovider.js ***!
  \****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CSVSearchProvider": () => (/* binding */ CSVSearchProvider)
/* harmony export */ });
/* harmony import */ var _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/csvviewer */ "webpack/sharing/consume/default/@jupyterlab/csvviewer/@jupyterlab/csvviewer");
/* harmony import */ var _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/documentsearch */ "webpack/sharing/consume/default/@jupyterlab/documentsearch/@jupyterlab/documentsearch");
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * CSV viewer search provider
 */
class CSVSearchProvider extends _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.SearchProvider {
    constructor() {
        super(...arguments);
        /**
         * Set to true if the widget under search is read-only, false
         * if it is editable.  Will be used to determine whether to show
         * the replace option.
         */
        this.isReadOnly = true;
    }
    /**
     * Instantiate a search provider for the widget.
     *
     * #### Notes
     * The widget provided is always checked using `isApplicable` before calling
     * this factory.
     *
     * @param widget The widget to search on
     * @param translator [optional] The translator object
     *
     * @returns The search provider on the widget
     */
    static createNew(widget, translator) {
        return new CSVSearchProvider(widget);
    }
    /**
     * Report whether or not this provider has the ability to search on the given object
     */
    static isApplicable(domain) {
        // check to see if the CSVSearchProvider can search on the
        // first cell, false indicates another editor is present
        return (domain instanceof _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_1__.DocumentWidget && domain.content instanceof _jupyterlab_csvviewer__WEBPACK_IMPORTED_MODULE_0__.CSVViewer);
    }
    /**
     * Clear currently highlighted match.
     */
    clearHighlight() {
        // no-op
        return Promise.resolve();
    }
    /**
     * Move the current match indicator to the next match.
     *
     * @param loop Whether to loop within the matches list.
     *
     * @returns The match is never returned by this provider
     */
    highlightNext(loop) {
        this.widget.content.searchService.find(this._query);
        return Promise.resolve(undefined);
    }
    /**
     * Move the current match indicator to the previous match.
     *
     * @param loop Whether to loop within the matches list.
     *
     * @returns The match is never returned by this provider
     */
    highlightPrevious(loop) {
        this.widget.content.searchService.find(this._query, true);
        return Promise.resolve(undefined);
    }
    /**
     * Replace the currently selected match with the provided text
     * Not implemented in the CSV viewer as it is read-only.
     *
     * @param newText The replacement text
     * @param loop Whether to loop within the matches list.
     *
     * @returns A promise that resolves once the action has completed.
     */
    replaceCurrentMatch(newText, loop) {
        return Promise.resolve(false);
    }
    /**
     * Replace all matches in the notebook with the provided text
     * Not implemented in the CSV viewer as it is read-only.
     *
     * @param newText The replacement text
     *
     * @returns A promise that resolves once the action has completed.
     */
    replaceAllMatches(newText) {
        return Promise.resolve(false);
    }
    /**
     * Initialize the search using the provided options.  Should update the UI
     * to highlight all matches and "select" whatever the first match should be.
     *
     * @param query A RegExp to be use to perform the search
     */
    startQuery(query) {
        this._query = query;
        this.widget.content.searchService.find(query);
        return Promise.resolve();
    }
    /**
     * Clears state of a search provider to prepare for startQuery to be called
     * in order to start a new query or refresh an existing one.
     */
    endQuery() {
        this.widget.content.searchService.clear();
        return Promise.resolve();
    }
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY3N2dmlld2VyLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuYWIwY2ZlMmYxNzAyY2VmYTVjMTIuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFNOEI7QUFPSDtBQU9DO0FBRXNDO0FBQ3BCO0FBRWM7QUFDVDtBQUNWO0FBQ1M7QUFFckQ7O0dBRUc7QUFDSCxNQUFNLFdBQVcsR0FBRyxVQUFVLENBQUM7QUFDL0IsTUFBTSxXQUFXLEdBQUcsVUFBVSxDQUFDO0FBRS9COztHQUVHO0FBQ0gsSUFBVSxVQUFVLENBSW5CO0FBSkQsV0FBVSxVQUFVO0lBQ0wsc0JBQVcsR0FBRyxnQkFBZ0IsQ0FBQztJQUUvQixzQkFBVyxHQUFHLGdCQUFnQixDQUFDO0FBQzlDLENBQUMsRUFKUyxVQUFVLEtBQVYsVUFBVSxRQUluQjtBQUVEOztHQUVHO0FBQ0gsTUFBTSxHQUFHLEdBQWdDO0lBQ3ZDLFFBQVEsRUFBRSxXQUFXO0lBQ3JCLEVBQUUsRUFBRSxxQ0FBcUM7SUFDekMsUUFBUSxFQUFFLENBQUMsZ0VBQVcsQ0FBQztJQUN2QixRQUFRLEVBQUU7UUFDUixvRUFBZTtRQUNmLCtEQUFhO1FBQ2IsMkRBQVM7UUFDVCwrRUFBdUI7UUFDdkIseUVBQWdCO1FBQ2hCLHdFQUFzQjtLQUN2QjtJQUNELFNBQVMsRUFBRSxJQUFJO0NBQ2hCLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sR0FBRyxHQUFnQztJQUN2QyxRQUFRLEVBQUUsV0FBVztJQUNyQixFQUFFLEVBQUUscUNBQXFDO0lBQ3pDLFFBQVEsRUFBRSxDQUFDLGdFQUFXLENBQUM7SUFDdkIsUUFBUSxFQUFFO1FBQ1Isb0VBQWU7UUFDZiwrREFBYTtRQUNiLDJEQUFTO1FBQ1QsK0VBQXVCO1FBQ3ZCLHlFQUFnQjtRQUNoQix3RUFBc0I7S0FDdkI7SUFDRCxTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7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QUFDLE9BQU8sQ0FBQyxhQUFhLENBQUMsS0FBSyxFQUFFLENBQUM7UUFFMUMsT0FBTyxPQUFPLENBQUMsT0FBTyxFQUFFLENBQUM7SUFDM0IsQ0FBQztDQUdGIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NzdnZpZXdlci1leHRlbnNpb24vc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jc3Z2aWV3ZXItZXh0ZW5zaW9uL3NyYy9zZWFyY2hwcm92aWRlci50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBjc3Z2aWV3ZXItZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxheW91dFJlc3RvcmVyLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQge1xuICBjcmVhdGVUb29sYmFyRmFjdG9yeSxcbiAgSW5wdXREaWFsb2csXG4gIElUaGVtZU1hbmFnZXIsXG4gIElUb29sYmFyV2lkZ2V0UmVnaXN0cnksXG4gIFdpZGdldFRyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHtcbiAgQ1NWRGVsaW1pdGVyLFxuICBDU1ZWaWV3ZXIsXG4gIENTVlZpZXdlckZhY3RvcnksXG4gIFRleHRSZW5kZXJDb25maWcsXG4gIFRTVlZpZXdlckZhY3Rvcnlcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvY3N2dmlld2VyJztcbmltcG9ydCB7IERvY3VtZW50UmVnaXN0cnksIElEb2N1bWVudFdpZGdldCB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jdW1lbnRzZWFyY2gnO1xuaW1wb3J0IHsgSU1haW5NZW51IH0gZnJvbSAnQGp1cHl0ZXJsYWIvbWFpbm1lbnUnO1xuaW1wb3J0IHsgSU9ic2VydmFibGVMaXN0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvb2JzZXJ2YWJsZXMnO1xuaW1wb3J0IHsgSVNldHRpbmdSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL3NldHRpbmdyZWdpc3RyeSc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcbmltcG9ydCB7IERhdGFHcmlkIH0gZnJvbSAnQGx1bWluby9kYXRhZ3JpZCc7XG5pbXBvcnQgeyBDU1ZTZWFyY2hQcm92aWRlciB9IGZyb20gJy4vc2VhcmNocHJvdmlkZXInO1xuXG4vKipcbiAqIFRoZSBuYW1lIG9mIHRoZSBmYWN0b3JpZXMgdGhhdCBjcmVhdGVzIHdpZGdldHMuXG4gKi9cbmNvbnN0IEZBQ1RPUllfQ1NWID0gJ0NTVlRhYmxlJztcbmNvbnN0IEZBQ1RPUllfVFNWID0gJ1RTVlRhYmxlJztcblxuLyoqXG4gKiBUaGUgY29tbWFuZCBJRHMgdXNlZCBieSB0aGUgY3N2dmlld2VyIHBsdWdpbnMuXG4gKi9cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IENTVkdvVG9MaW5lID0gJ2Nzdjpnby10by1saW5lJztcblxuICBleHBvcnQgY29uc3QgVFNWR29Ub0xpbmUgPSAndHN2OmdvLXRvLWxpbmUnO1xufVxuXG4vKipcbiAqIFRoZSBDU1YgZmlsZSBoYW5kbGVyIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgY3N2OiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUNzdixcbiAgaWQ6ICdAanVweXRlcmxhYi9jc3Z2aWV3ZXItZXh0ZW5zaW9uOmNzdicsXG4gIHJlcXVpcmVzOiBbSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW1xuICAgIElMYXlvdXRSZXN0b3JlcixcbiAgICBJVGhlbWVNYW5hZ2VyLFxuICAgIElNYWluTWVudSxcbiAgICBJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeSxcbiAgICBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIElUb29sYmFyV2lkZ2V0UmVnaXN0cnlcbiAgXSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIFRoZSBUU1YgZmlsZSBoYW5kbGVyIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgdHN2OiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48dm9pZD4gPSB7XG4gIGFjdGl2YXRlOiBhY3RpdmF0ZVRzdixcbiAgaWQ6ICdAanVweXRlcmxhYi9jc3Z2aWV3ZXItZXh0ZW5zaW9uOnRzdicsXG4gIHJlcXVpcmVzOiBbSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW1xuICAgIElMYXlvdXRSZXN0b3JlcixcbiAgICBJVGhlbWVNYW5hZ2VyLFxuICAgIElNYWluTWVudSxcbiAgICBJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeSxcbiAgICBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIElUb29sYmFyV2lkZ2V0UmVnaXN0cnlcbiAgXSxcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG4vKipcbiAqIEFjdGl2YXRlIGNzc3ZpZXdlciBleHRlbnNpb24gZm9yIENTViBmaWxlc1xuICovXG5mdW5jdGlvbiBhY3RpdmF0ZUNzdihcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgdGhlbWVNYW5hZ2VyOiBJVGhlbWVNYW5hZ2VyIHwgbnVsbCxcbiAgbWFpbk1lbnU6IElNYWluTWVudSB8IG51bGwsXG4gIHNlYXJjaFJlZ2lzdHJ5OiBJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeSB8IG51bGwsXG4gIHNldHRpbmdSZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeSB8IG51bGwsXG4gIHRvb2xiYXJSZWdpc3RyeTogSVRvb2xiYXJXaWRnZXRSZWdpc3RyeSB8IG51bGxcbik6IHZvaWQge1xuICBjb25zdCB7IGNvbW1hbmRzLCBzaGVsbCB9ID0gYXBwO1xuICBsZXQgdG9vbGJhckZhY3Rvcnk6XG4gICAgfCAoKFxuICAgICAgICB3aWRnZXQ6IElEb2N1bWVudFdpZGdldDxDU1ZWaWV3ZXI+XG4gICAgICApID0+IElPYnNlcnZhYmxlTGlzdDxEb2N1bWVudFJlZ2lzdHJ5LklUb29sYmFySXRlbT4pXG4gICAgfCB1bmRlZmluZWQ7XG5cbiAgaWYgKHRvb2xiYXJSZWdpc3RyeSkge1xuICAgIHRvb2xiYXJSZWdpc3RyeS5hZGRGYWN0b3J5PElEb2N1bWVudFdpZGdldDxDU1ZWaWV3ZXI+PihcbiAgICAgIEZBQ1RPUllfQ1NWLFxuICAgICAgJ2RlbGltaXRlcicsXG4gICAgICB3aWRnZXQgPT5cbiAgICAgICAgbmV3IENTVkRlbGltaXRlcih7XG4gICAgICAgICAgd2lkZ2V0OiB3aWRnZXQuY29udGVudCxcbiAgICAgICAgICB0cmFuc2xhdG9yXG4gICAgICAgIH0pXG4gICAgKTtcblxuICAgIGlmIChzZXR0aW5nUmVnaXN0cnkpIHtcbiAgICAgIHRvb2xiYXJGYWN0b3J5ID0gY3JlYXRlVG9vbGJhckZhY3RvcnkoXG4gICAgICAgIHRvb2xiYXJSZWdpc3RyeSxcbiAgICAgICAgc2V0dGluZ1JlZ2lzdHJ5LFxuICAgICAgICBGQUNUT1JZX0NTVixcbiAgICAgICAgY3N2LmlkLFxuICAgICAgICB0cmFuc2xhdG9yXG4gICAgICApO1xuICAgIH1cbiAgfVxuXG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgY29uc3QgZmFjdG9yeSA9IG5ldyBDU1ZWaWV3ZXJGYWN0b3J5KHtcbiAgICBuYW1lOiBGQUNUT1JZX0NTVixcbiAgICBsYWJlbDogdHJhbnMuX18oJ0NTViBWaWV3ZXInKSxcbiAgICBmaWxlVHlwZXM6IFsnY3N2J10sXG4gICAgZGVmYXVsdEZvcjogWydjc3YnXSxcbiAgICByZWFkT25seTogdHJ1ZSxcbiAgICB0b29sYmFyRmFjdG9yeSxcbiAgICB0cmFuc2xhdG9yXG4gIH0pO1xuICBjb25zdCB0cmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8SURvY3VtZW50V2lkZ2V0PENTVlZpZXdlcj4+KHtcbiAgICBuYW1lc3BhY2U6ICdjc3Z2aWV3ZXInXG4gIH0pO1xuXG4gIC8vIFRoZSBjdXJyZW50IHN0eWxlcyBmb3IgdGhlIGRhdGEgZ3JpZHMuXG4gIGxldCBzdHlsZTogRGF0YUdyaWQuU3R5bGUgPSBQcml2YXRlLkxJR0hUX1NUWUxFO1xuICBsZXQgcmVuZGVyZXJDb25maWc6IFRleHRSZW5kZXJDb25maWcgPSBQcml2YXRlLkxJR0hUX1RFWFRfQ09ORklHO1xuXG4gIGlmIChyZXN0b3Jlcikge1xuICAgIC8vIEhhbmRsZSBzdGF0ZSByZXN0b3JhdGlvbi5cbiAgICB2b2lkIHJlc3RvcmVyLnJlc3RvcmUodHJhY2tlciwge1xuICAgICAgY29tbWFuZDogJ2RvY21hbmFnZXI6b3BlbicsXG4gICAgICBhcmdzOiB3aWRnZXQgPT4gKHsgcGF0aDogd2lkZ2V0LmNvbnRleHQucGF0aCwgZmFjdG9yeTogRkFDVE9SWV9DU1YgfSksXG4gICAgICBuYW1lOiB3aWRnZXQgPT4gd2lkZ2V0LmNvbnRleHQucGF0aFxuICAgIH0pO1xuICB9XG5cbiAgYXBwLmRvY1JlZ2lzdHJ5LmFkZFdpZGdldEZhY3RvcnkoZmFjdG9yeSk7XG4gIGNvbnN0IGZ0ID0gYXBwLmRvY1JlZ2lzdHJ5LmdldEZpbGVUeXBlKCdjc3YnKTtcbiAgZmFjdG9yeS53aWRnZXRDcmVhdGVkLmNvbm5lY3QoKHNlbmRlciwgd2lkZ2V0KSA9PiB7XG4gICAgLy8gVHJhY2sgdGhlIHdpZGdldC5cbiAgICB2b2lkIHRyYWNrZXIuYWRkKHdpZGdldCk7XG4gICAgLy8gTm90aWZ5IHRoZSB3aWRnZXQgdHJhY2tlciBpZiByZXN0b3JlIGRhdGEgbmVlZHMgdG8gdXBkYXRlLlxuICAgIHdpZGdldC5jb250ZXh0LnBhdGhDaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgdm9pZCB0cmFja2VyLnNhdmUod2lkZ2V0KTtcbiAgICB9KTtcblxuICAgIGlmIChmdCkge1xuICAgICAgd2lkZ2V0LnRpdGxlLmljb24gPSBmdC5pY29uITtcbiAgICAgIHdpZGdldC50aXRsZS5pY29uQ2xhc3MgPSBmdC5pY29uQ2xhc3MhO1xuICAgICAgd2lkZ2V0LnRpdGxlLmljb25MYWJlbCA9IGZ0Lmljb25MYWJlbCE7XG4gICAgfVxuICAgIC8vIFNldCB0aGUgdGhlbWUgZm9yIHRoZSBuZXcgd2lkZ2V0LlxuICAgIHdpZGdldC5jb250ZW50LnN0eWxlID0gc3R5bGU7XG4gICAgd2lkZ2V0LmNvbnRlbnQucmVuZGVyZXJDb25maWcgPSByZW5kZXJlckNvbmZpZztcbiAgfSk7XG5cbiAgLy8gS2VlcCB0aGUgdGhlbWVzIHVwLXRvLWRhdGUuXG4gIGNvbnN0IHVwZGF0ZVRoZW1lcyA9ICgpID0+IHtcbiAgICBjb25zdCBpc0xpZ2h0ID1cbiAgICAgIHRoZW1lTWFuYWdlciAmJiB0aGVtZU1hbmFnZXIudGhlbWVcbiAgICAgICAgPyB0aGVtZU1hbmFnZXIuaXNMaWdodCh0aGVtZU1hbmFnZXIudGhlbWUpXG4gICAgICAgIDogdHJ1ZTtcbiAgICBzdHlsZSA9IGlzTGlnaHQgPyBQcml2YXRlLkxJR0hUX1NUWUxFIDogUHJpdmF0ZS5EQVJLX1NUWUxFO1xuICAgIHJlbmRlcmVyQ29uZmlnID0gaXNMaWdodFxuICAgICAgPyBQcml2YXRlLkxJR0hUX1RFWFRfQ09ORklHXG4gICAgICA6IFByaXZhdGUuREFSS19URVhUX0NPTkZJRztcbiAgICB0cmFja2VyLmZvckVhY2goZ3JpZCA9PiB7XG4gICAgICBncmlkLmNvbnRlbnQuc3R5bGUgPSBzdHlsZTtcbiAgICAgIGdyaWQuY29udGVudC5yZW5kZXJlckNvbmZpZyA9IHJlbmRlcmVyQ29uZmlnO1xuICAgIH0pO1xuICB9O1xuICBpZiAodGhlbWVNYW5hZ2VyKSB7XG4gICAgdGhlbWVNYW5hZ2VyLnRoZW1lQ2hhbmdlZC5jb25uZWN0KHVwZGF0ZVRoZW1lcyk7XG4gIH1cblxuICAvLyBBZGQgY29tbWFuZHNcbiAgY29uc3QgaXNFbmFibGVkID0gKCkgPT5cbiAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQgIT09IG51bGwgJiZcbiAgICB0cmFja2VyLmN1cnJlbnRXaWRnZXQgPT09IHNoZWxsLmN1cnJlbnRXaWRnZXQ7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLkNTVkdvVG9MaW5lLCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdHbyB0byBMaW5lJyksXG4gICAgZXhlY3V0ZTogYXN5bmMgKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgaWYgKHdpZGdldCA9PT0gbnVsbCkge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICBjb25zdCByZXN1bHQgPSBhd2FpdCBJbnB1dERpYWxvZy5nZXROdW1iZXIoe1xuICAgICAgICB0aXRsZTogdHJhbnMuX18oJ0dvIHRvIExpbmUnKSxcbiAgICAgICAgdmFsdWU6IDBcbiAgICAgIH0pO1xuICAgICAgaWYgKHJlc3VsdC5idXR0b24uYWNjZXB0ICYmIHJlc3VsdC52YWx1ZSAhPT0gbnVsbCkge1xuICAgICAgICB3aWRnZXQuY29udGVudC5nb1RvTGluZShyZXN1bHQudmFsdWUpO1xuICAgICAgfVxuICAgIH0sXG4gICAgaXNFbmFibGVkXG4gIH0pO1xuXG4gIGlmIChtYWluTWVudSkge1xuICAgIC8vIEFkZCBnbyB0byBsaW5lIGNhcGFiaWxpdHkgdG8gdGhlIGVkaXQgbWVudS5cbiAgICBtYWluTWVudS5lZGl0TWVudS5nb1RvTGluZXJzLmFkZCh7XG4gICAgICBpZDogQ29tbWFuZElEcy5DU1ZHb1RvTGluZSxcbiAgICAgIGlzRW5hYmxlZFxuICAgIH0pO1xuICB9XG4gIGlmIChzZWFyY2hSZWdpc3RyeSkge1xuICAgIHNlYXJjaFJlZ2lzdHJ5LmFkZCgnY3N2JywgQ1NWU2VhcmNoUHJvdmlkZXIpO1xuICB9XG59XG5cbi8qKlxuICogQWN0aXZhdGUgY3Nzdmlld2VyIGV4dGVuc2lvbiBmb3IgVFNWIGZpbGVzXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlVHN2KFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICB0aGVtZU1hbmFnZXI6IElUaGVtZU1hbmFnZXIgfCBudWxsLFxuICBtYWluTWVudTogSU1haW5NZW51IHwgbnVsbCxcbiAgc2VhcmNoUmVnaXN0cnk6IElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5IHwgbnVsbCxcbiAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5IHwgbnVsbCxcbiAgdG9vbGJhclJlZ2lzdHJ5OiBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5IHwgbnVsbFxuKTogdm9pZCB7XG4gIGNvbnN0IHsgY29tbWFuZHMsIHNoZWxsIH0gPSBhcHA7XG4gIGxldCB0b29sYmFyRmFjdG9yeTpcbiAgICB8ICgoXG4gICAgICAgIHdpZGdldDogSURvY3VtZW50V2lkZ2V0PENTVlZpZXdlcj5cbiAgICAgICkgPT4gSU9ic2VydmFibGVMaXN0PERvY3VtZW50UmVnaXN0cnkuSVRvb2xiYXJJdGVtPilcbiAgICB8IHVuZGVmaW5lZDtcblxuICBpZiAodG9vbGJhclJlZ2lzdHJ5KSB7XG4gICAgdG9vbGJhclJlZ2lzdHJ5LmFkZEZhY3Rvcnk8SURvY3VtZW50V2lkZ2V0PENTVlZpZXdlcj4+KFxuICAgICAgRkFDVE9SWV9UU1YsXG4gICAgICAnZGVsaW1pdGVyJyxcbiAgICAgIHdpZGdldCA9PlxuICAgICAgICBuZXcgQ1NWRGVsaW1pdGVyKHtcbiAgICAgICAgICB3aWRnZXQ6IHdpZGdldC5jb250ZW50LFxuICAgICAgICAgIHRyYW5zbGF0b3JcbiAgICAgICAgfSlcbiAgICApO1xuXG4gICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgdG9vbGJhckZhY3RvcnkgPSBjcmVhdGVUb29sYmFyRmFjdG9yeShcbiAgICAgICAgdG9vbGJhclJlZ2lzdHJ5LFxuICAgICAgICBzZXR0aW5nUmVnaXN0cnksXG4gICAgICAgIEZBQ1RPUllfVFNWLFxuICAgICAgICB0c3YuaWQsXG4gICAgICAgIHRyYW5zbGF0b3JcbiAgICAgICk7XG4gICAgfVxuICB9XG5cbiAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICBjb25zdCBmYWN0b3J5ID0gbmV3IFRTVlZpZXdlckZhY3Rvcnkoe1xuICAgIG5hbWU6IEZBQ1RPUllfVFNWLFxuICAgIGxhYmVsOiB0cmFucy5fXygnVFNWIFZpZXdlcicpLFxuICAgIGZpbGVUeXBlczogWyd0c3YnXSxcbiAgICBkZWZhdWx0Rm9yOiBbJ3RzdiddLFxuICAgIHJlYWRPbmx5OiB0cnVlLFxuICAgIHRvb2xiYXJGYWN0b3J5LFxuICAgIHRyYW5zbGF0b3JcbiAgfSk7XG4gIGNvbnN0IHRyYWNrZXIgPSBuZXcgV2lkZ2V0VHJhY2tlcjxJRG9jdW1lbnRXaWRnZXQ8Q1NWVmlld2VyPj4oe1xuICAgIG5hbWVzcGFjZTogJ3RzdnZpZXdlcidcbiAgfSk7XG5cbiAgLy8gVGhlIGN1cnJlbnQgc3R5bGVzIGZvciB0aGUgZGF0YSBncmlkcy5cbiAgbGV0IHN0eWxlOiBEYXRhR3JpZC5TdHlsZSA9IFByaXZhdGUuTElHSFRfU1RZTEU7XG4gIGxldCByZW5kZXJlckNvbmZpZzogVGV4dFJlbmRlckNvbmZpZyA9IFByaXZhdGUuTElHSFRfVEVYVF9DT05GSUc7XG5cbiAgaWYgKHJlc3RvcmVyKSB7XG4gICAgLy8gSGFuZGxlIHN0YXRlIHJlc3RvcmF0aW9uLlxuICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICBjb21tYW5kOiAnZG9jbWFuYWdlcjpvcGVuJyxcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoeyBwYXRoOiB3aWRnZXQuY29udGV4dC5wYXRoLCBmYWN0b3J5OiBGQUNUT1JZX1RTViB9KSxcbiAgICAgIG5hbWU6IHdpZGdldCA9PiB3aWRnZXQuY29udGV4dC5wYXRoXG4gICAgfSk7XG4gIH1cblxuICBhcHAuZG9jUmVnaXN0cnkuYWRkV2lkZ2V0RmFjdG9yeShmYWN0b3J5KTtcbiAgY29uc3QgZnQgPSBhcHAuZG9jUmVnaXN0cnkuZ2V0RmlsZVR5cGUoJ3RzdicpO1xuICBmYWN0b3J5LndpZGdldENyZWF0ZWQuY29ubmVjdCgoc2VuZGVyLCB3aWRnZXQpID0+IHtcbiAgICAvLyBUcmFjayB0aGUgd2lkZ2V0LlxuICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICAvLyBOb3RpZnkgdGhlIHdpZGdldCB0cmFja2VyIGlmIHJlc3RvcmUgZGF0YSBuZWVkcyB0byB1cGRhdGUuXG4gICAgd2lkZ2V0LmNvbnRleHQucGF0aENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB2b2lkIHRyYWNrZXIuc2F2ZSh3aWRnZXQpO1xuICAgIH0pO1xuXG4gICAgaWYgKGZ0KSB7XG4gICAgICB3aWRnZXQudGl0bGUuaWNvbiA9IGZ0Lmljb24hO1xuICAgICAgd2lkZ2V0LnRpdGxlLmljb25DbGFzcyA9IGZ0Lmljb25DbGFzcyE7XG4gICAgICB3aWRnZXQudGl0bGUuaWNvbkxhYmVsID0gZnQuaWNvbkxhYmVsITtcbiAgICB9XG4gICAgLy8gU2V0IHRoZSB0aGVtZSBmb3IgdGhlIG5ldyB3aWRnZXQuXG4gICAgd2lkZ2V0LmNvbnRlbnQuc3R5bGUgPSBzdHlsZTtcbiAgICB3aWRnZXQuY29udGVudC5yZW5kZXJlckNvbmZpZyA9IHJlbmRlcmVyQ29uZmlnO1xuICB9KTtcblxuICAvLyBLZWVwIHRoZSB0aGVtZXMgdXAtdG8tZGF0ZS5cbiAgY29uc3QgdXBkYXRlVGhlbWVzID0gKCkgPT4ge1xuICAgIGNvbnN0IGlzTGlnaHQgPVxuICAgICAgdGhlbWVNYW5hZ2VyICYmIHRoZW1lTWFuYWdlci50aGVtZVxuICAgICAgICA/IHRoZW1lTWFuYWdlci5pc0xpZ2h0KHRoZW1lTWFuYWdlci50aGVtZSlcbiAgICAgICAgOiB0cnVlO1xuICAgIHN0eWxlID0gaXNMaWdodCA/IFByaXZhdGUuTElHSFRfU1RZTEUgOiBQcml2YXRlLkRBUktfU1RZTEU7XG4gICAgcmVuZGVyZXJDb25maWcgPSBpc0xpZ2h0XG4gICAgICA/IFByaXZhdGUuTElHSFRfVEVYVF9DT05GSUdcbiAgICAgIDogUHJpdmF0ZS5EQVJLX1RFWFRfQ09ORklHO1xuICAgIHRyYWNrZXIuZm9yRWFjaChncmlkID0+IHtcbiAgICAgIGdyaWQuY29udGVudC5zdHlsZSA9IHN0eWxlO1xuICAgICAgZ3JpZC5jb250ZW50LnJlbmRlcmVyQ29uZmlnID0gcmVuZGVyZXJDb25maWc7XG4gICAgfSk7XG4gIH07XG4gIGlmICh0aGVtZU1hbmFnZXIpIHtcbiAgICB0aGVtZU1hbmFnZXIudGhlbWVDaGFuZ2VkLmNvbm5lY3QodXBkYXRlVGhlbWVzKTtcbiAgfVxuXG4gIC8vIEFkZCBjb21tYW5kc1xuICBjb25zdCBpc0VuYWJsZWQgPSAoKSA9PlxuICAgIHRyYWNrZXIuY3VycmVudFdpZGdldCAhPT0gbnVsbCAmJlxuICAgIHRyYWNrZXIuY3VycmVudFdpZGdldCA9PT0gc2hlbGwuY3VycmVudFdpZGdldDtcblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuVFNWR29Ub0xpbmUsIHtcbiAgICBsYWJlbDogdHJhbnMuX18oJ0dvIHRvIExpbmUnKSxcbiAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICBjb25zdCB3aWRnZXQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICBpZiAod2lkZ2V0ID09PSBudWxsKSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGNvbnN0IHJlc3VsdCA9IGF3YWl0IElucHV0RGlhbG9nLmdldE51bWJlcih7XG4gICAgICAgIHRpdGxlOiB0cmFucy5fXygnR28gdG8gTGluZScpLFxuICAgICAgICB2YWx1ZTogMFxuICAgICAgfSk7XG4gICAgICBpZiAocmVzdWx0LmJ1dHRvbi5hY2NlcHQgJiYgcmVzdWx0LnZhbHVlICE9PSBudWxsKSB7XG4gICAgICAgIHdpZGdldC5jb250ZW50LmdvVG9MaW5lKHJlc3VsdC52YWx1ZSk7XG4gICAgICB9XG4gICAgfSxcbiAgICBpc0VuYWJsZWRcbiAgfSk7XG5cbiAgaWYgKG1haW5NZW51KSB7XG4gICAgLy8gQWRkIGdvIHRvIGxpbmUgY2FwYWJpbGl0eSB0byB0aGUgZWRpdCBtZW51LlxuICAgIG1haW5NZW51LmVkaXRNZW51LmdvVG9MaW5lcnMuYWRkKHtcbiAgICAgIGlkOiBDb21tYW5kSURzLlRTVkdvVG9MaW5lLFxuICAgICAgaXNFbmFibGVkXG4gICAgfSk7XG4gIH1cbiAgaWYgKHNlYXJjaFJlZ2lzdHJ5KSB7XG4gICAgc2VhcmNoUmVnaXN0cnkuYWRkKCd0c3YnLCBDU1ZTZWFyY2hQcm92aWRlcik7XG4gIH1cbn1cblxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbnMgYXMgZGVmYXVsdC5cbiAqL1xuY29uc3QgcGx1Z2luczogSnVweXRlckZyb250RW5kUGx1Z2luPGFueT5bXSA9IFtjc3YsIHRzdl07XG5leHBvcnQgZGVmYXVsdCBwbHVnaW5zO1xuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBwcml2YXRlIGRhdGEuXG4gKi9cbm5hbWVzcGFjZSBQcml2YXRlIHtcbiAgLyoqXG4gICAqIFRoZSBsaWdodCB0aGVtZSBmb3IgdGhlIGRhdGEgZ3JpZC5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBMSUdIVF9TVFlMRTogRGF0YUdyaWQuU3R5bGUgPSB7XG4gICAgLi4uRGF0YUdyaWQuZGVmYXVsdFN0eWxlLFxuICAgIHZvaWRDb2xvcjogJyNGM0YzRjMnLFxuICAgIGJhY2tncm91bmRDb2xvcjogJ3doaXRlJyxcbiAgICBoZWFkZXJCYWNrZ3JvdW5kQ29sb3I6ICcjRUVFRUVFJyxcbiAgICBncmlkTGluZUNvbG9yOiAncmdiYSgyMCwgMjAsIDIwLCAwLjE1KScsXG4gICAgaGVhZGVyR3JpZExpbmVDb2xvcjogJ3JnYmEoMjAsIDIwLCAyMCwgMC4yNSknLFxuICAgIHJvd0JhY2tncm91bmRDb2xvcjogaSA9PiAoaSAlIDIgPT09IDAgPyAnI0Y1RjVGNScgOiAnd2hpdGUnKVxuICB9O1xuXG4gIC8qKlxuICAgKiBUaGUgZGFyayB0aGVtZSBmb3IgdGhlIGRhdGEgZ3JpZC5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBEQVJLX1NUWUxFOiBEYXRhR3JpZC5TdHlsZSA9IHtcbiAgICAuLi5EYXRhR3JpZC5kZWZhdWx0U3R5bGUsXG4gICAgdm9pZENvbG9yOiAnYmxhY2snLFxuICAgIGJhY2tncm91bmRDb2xvcjogJyMxMTExMTEnLFxuICAgIGhlYWRlckJhY2tncm91bmRDb2xvcjogJyM0MjQyNDInLFxuICAgIGdyaWRMaW5lQ29sb3I6ICdyZ2JhKDIzNSwgMjM1LCAyMzUsIDAuMTUpJyxcbiAgICBoZWFkZXJHcmlkTGluZUNvbG9yOiAncmdiYSgyMzUsIDIzNSwgMjM1LCAwLjI1KScsXG4gICAgcm93QmFja2dyb3VuZENvbG9yOiBpID0+IChpICUgMiA9PT0gMCA/ICcjMjEyMTIxJyA6ICcjMTExMTExJylcbiAgfTtcblxuICAvKipcbiAgICogVGhlIGxpZ2h0IGNvbmZpZyBmb3IgdGhlIGRhdGEgZ3JpZCByZW5kZXJlci5cbiAgICovXG4gIGV4cG9ydCBjb25zdCBMSUdIVF9URVhUX0NPTkZJRzogVGV4dFJlbmRlckNvbmZpZyA9IHtcbiAgICB0ZXh0Q29sb3I6ICcjMTExMTExJyxcbiAgICBtYXRjaEJhY2tncm91bmRDb2xvcjogJyNGRkZGRTAnLFxuICAgIGN1cnJlbnRNYXRjaEJhY2tncm91bmRDb2xvcjogJyNGRkZGMDAnLFxuICAgIGhvcml6b250YWxBbGlnbm1lbnQ6ICdyaWdodCdcbiAgfTtcblxuICAvKipcbiAgICogVGhlIGRhcmsgY29uZmlnIGZvciB0aGUgZGF0YSBncmlkIHJlbmRlcmVyLlxuICAgKi9cbiAgZXhwb3J0IGNvbnN0IERBUktfVEVYVF9DT05GSUc6IFRleHRSZW5kZXJDb25maWcgPSB7XG4gICAgdGV4dENvbG9yOiAnI0Y1RjVGNScsXG4gICAgbWF0Y2hCYWNrZ3JvdW5kQ29sb3I6ICcjODM4NDIzJyxcbiAgICBjdXJyZW50TWF0Y2hCYWNrZ3JvdW5kQ29sb3I6ICcjQTM4MDdBJyxcbiAgICBob3Jpem9udGFsQWxpZ25tZW50OiAncmlnaHQnXG4gIH07XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5pbXBvcnQgeyBDU1ZWaWV3ZXIgfSBmcm9tICdAanVweXRlcmxhYi9jc3Z2aWV3ZXInO1xuaW1wb3J0IHsgRG9jdW1lbnRXaWRnZXQgfSBmcm9tICdAanVweXRlcmxhYi9kb2NyZWdpc3RyeSc7XG5pbXBvcnQgeyBJU2VhcmNoUHJvdmlkZXIsIFNlYXJjaFByb3ZpZGVyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jdW1lbnRzZWFyY2gnO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBXaWRnZXQgfSBmcm9tICdAbHVtaW5vL3dpZGdldHMnO1xuXG4vLyBUaGUgdHlwZSBmb3Igd2hpY2ggaXNBcHBsaWNhYmxlIHJldHVybnMgdHJ1ZVxuZXhwb3J0IHR5cGUgQ1NWRG9jdW1lbnRXaWRnZXQgPSBEb2N1bWVudFdpZGdldDxDU1ZWaWV3ZXI+O1xuXG4vKipcbiAqIENTViB2aWV3ZXIgc2VhcmNoIHByb3ZpZGVyXG4gKi9cbmV4cG9ydCBjbGFzcyBDU1ZTZWFyY2hQcm92aWRlciBleHRlbmRzIFNlYXJjaFByb3ZpZGVyPENTVkRvY3VtZW50V2lkZ2V0PiB7XG4gIC8qKlxuICAgKiBJbnN0YW50aWF0ZSBhIHNlYXJjaCBwcm92aWRlciBmb3IgdGhlIHdpZGdldC5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGUgd2lkZ2V0IHByb3ZpZGVkIGlzIGFsd2F5cyBjaGVja2VkIHVzaW5nIGBpc0FwcGxpY2FibGVgIGJlZm9yZSBjYWxsaW5nXG4gICAqIHRoaXMgZmFjdG9yeS5cbiAgICpcbiAgICogQHBhcmFtIHdpZGdldCBUaGUgd2lkZ2V0IHRvIHNlYXJjaCBvblxuICAgKiBAcGFyYW0gdHJhbnNsYXRvciBbb3B0aW9uYWxdIFRoZSB0cmFuc2xhdG9yIG9iamVjdFxuICAgKlxuICAgKiBAcmV0dXJucyBUaGUgc2VhcmNoIHByb3ZpZGVyIG9uIHRoZSB3aWRnZXRcbiAgICovXG4gIHN0YXRpYyBjcmVhdGVOZXcoXG4gICAgd2lkZ2V0OiBDU1ZEb2N1bWVudFdpZGdldCxcbiAgICB0cmFuc2xhdG9yPzogSVRyYW5zbGF0b3JcbiAgKTogSVNlYXJjaFByb3ZpZGVyIHtcbiAgICByZXR1cm4gbmV3IENTVlNlYXJjaFByb3ZpZGVyKHdpZGdldCk7XG4gIH1cblxuICAvKipcbiAgICogUmVwb3J0IHdoZXRoZXIgb3Igbm90IHRoaXMgcHJvdmlkZXIgaGFzIHRoZSBhYmlsaXR5IHRvIHNlYXJjaCBvbiB0aGUgZ2l2ZW4gb2JqZWN0XG4gICAqL1xuICBzdGF0aWMgaXNBcHBsaWNhYmxlKGRvbWFpbjogV2lkZ2V0KTogZG9tYWluIGlzIENTVkRvY3VtZW50V2lkZ2V0IHtcbiAgICAvLyBjaGVjayB0byBzZWUgaWYgdGhlIENTVlNlYXJjaFByb3ZpZGVyIGNhbiBzZWFyY2ggb24gdGhlXG4gICAgLy8gZmlyc3QgY2VsbCwgZmFsc2UgaW5kaWNhdGVzIGFub3RoZXIgZWRpdG9yIGlzIHByZXNlbnRcbiAgICByZXR1cm4gKFxuICAgICAgZG9tYWluIGluc3RhbmNlb2YgRG9jdW1lbnRXaWRnZXQgJiYgZG9tYWluLmNvbnRlbnQgaW5zdGFuY2VvZiBDU1ZWaWV3ZXJcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCB0byB0cnVlIGlmIHRoZSB3aWRnZXQgdW5kZXIgc2VhcmNoIGlzIHJlYWQtb25seSwgZmFsc2VcbiAgICogaWYgaXQgaXMgZWRpdGFibGUuICBXaWxsIGJlIHVzZWQgdG8gZGV0ZXJtaW5lIHdoZXRoZXIgdG8gc2hvd1xuICAgKiB0aGUgcmVwbGFjZSBvcHRpb24uXG4gICAqL1xuICByZWFkb25seSBpc1JlYWRPbmx5ID0gdHJ1ZTtcblxuICAvKipcbiAgICogQ2xlYXIgY3VycmVudGx5IGhpZ2hsaWdodGVkIG1hdGNoLlxuICAgKi9cbiAgY2xlYXJIaWdobGlnaHQoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgLy8gbm8tb3BcbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKCk7XG4gIH1cblxuICAvKipcbiAgICogTW92ZSB0aGUgY3VycmVudCBtYXRjaCBpbmRpY2F0b3IgdG8gdGhlIG5leHQgbWF0Y2guXG4gICAqXG4gICAqIEBwYXJhbSBsb29wIFdoZXRoZXIgdG8gbG9vcCB3aXRoaW4gdGhlIG1hdGNoZXMgbGlzdC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIG1hdGNoIGlzIG5ldmVyIHJldHVybmVkIGJ5IHRoaXMgcHJvdmlkZXJcbiAgICovXG4gIGhpZ2hsaWdodE5leHQobG9vcD86IGJvb2xlYW4pOiBQcm9taXNlPHVuZGVmaW5lZD4ge1xuICAgIHRoaXMud2lkZ2V0LmNvbnRlbnQuc2VhcmNoU2VydmljZS5maW5kKHRoaXMuX3F1ZXJ5KTtcbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKHVuZGVmaW5lZCk7XG4gIH1cblxuICAvKipcbiAgICogTW92ZSB0aGUgY3VycmVudCBtYXRjaCBpbmRpY2F0b3IgdG8gdGhlIHByZXZpb3VzIG1hdGNoLlxuICAgKlxuICAgKiBAcGFyYW0gbG9vcCBXaGV0aGVyIHRvIGxvb3Agd2l0aGluIHRoZSBtYXRjaGVzIGxpc3QuXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBtYXRjaCBpcyBuZXZlciByZXR1cm5lZCBieSB0aGlzIHByb3ZpZGVyXG4gICAqL1xuICBoaWdobGlnaHRQcmV2aW91cyhsb29wPzogYm9vbGVhbik6IFByb21pc2U8dW5kZWZpbmVkPiB7XG4gICAgdGhpcy53aWRnZXQuY29udGVudC5zZWFyY2hTZXJ2aWNlLmZpbmQodGhpcy5fcXVlcnksIHRydWUpO1xuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUodW5kZWZpbmVkKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXBsYWNlIHRoZSBjdXJyZW50bHkgc2VsZWN0ZWQgbWF0Y2ggd2l0aCB0aGUgcHJvdmlkZWQgdGV4dFxuICAgKiBOb3QgaW1wbGVtZW50ZWQgaW4gdGhlIENTViB2aWV3ZXIgYXMgaXQgaXMgcmVhZC1vbmx5LlxuICAgKlxuICAgKiBAcGFyYW0gbmV3VGV4dCBUaGUgcmVwbGFjZW1lbnQgdGV4dFxuICAgKiBAcGFyYW0gbG9vcCBXaGV0aGVyIHRvIGxvb3Agd2l0aGluIHRoZSBtYXRjaGVzIGxpc3QuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIG9uY2UgdGhlIGFjdGlvbiBoYXMgY29tcGxldGVkLlxuICAgKi9cbiAgcmVwbGFjZUN1cnJlbnRNYXRjaChuZXdUZXh0OiBzdHJpbmcsIGxvb3A/OiBib29sZWFuKTogUHJvbWlzZTxib29sZWFuPiB7XG4gICAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShmYWxzZSk7XG4gIH1cblxuICAvKipcbiAgICogUmVwbGFjZSBhbGwgbWF0Y2hlcyBpbiB0aGUgbm90ZWJvb2sgd2l0aCB0aGUgcHJvdmlkZWQgdGV4dFxuICAgKiBOb3QgaW1wbGVtZW50ZWQgaW4gdGhlIENTViB2aWV3ZXIgYXMgaXQgaXMgcmVhZC1vbmx5LlxuICAgKlxuICAgKiBAcGFyYW0gbmV3VGV4dCBUaGUgcmVwbGFjZW1lbnQgdGV4dFxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyBvbmNlIHRoZSBhY3Rpb24gaGFzIGNvbXBsZXRlZC5cbiAgICovXG4gIHJlcGxhY2VBbGxNYXRjaGVzKG5ld1RleHQ6IHN0cmluZyk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgIHJldHVybiBQcm9taXNlLnJlc29sdmUoZmFsc2UpO1xuICB9XG5cbiAgLyoqXG4gICAqIEluaXRpYWxpemUgdGhlIHNlYXJjaCB1c2luZyB0aGUgcHJvdmlkZWQgb3B0aW9ucy4gIFNob3VsZCB1cGRhdGUgdGhlIFVJXG4gICAqIHRvIGhpZ2hsaWdodCBhbGwgbWF0Y2hlcyBhbmQgXCJzZWxlY3RcIiB3aGF0ZXZlciB0aGUgZmlyc3QgbWF0Y2ggc2hvdWxkIGJlLlxuICAgKlxuICAgKiBAcGFyYW0gcXVlcnkgQSBSZWdFeHAgdG8gYmUgdXNlIHRvIHBlcmZvcm0gdGhlIHNlYXJjaFxuICAgKi9cbiAgc3RhcnRRdWVyeShxdWVyeTogUmVnRXhwKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgdGhpcy5fcXVlcnkgPSBxdWVyeTtcbiAgICB0aGlzLndpZGdldC5jb250ZW50LnNlYXJjaFNlcnZpY2UuZmluZChxdWVyeSk7XG5cbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKCk7XG4gIH1cblxuICAvKipcbiAgICogQ2xlYXJzIHN0YXRlIG9mIGEgc2VhcmNoIHByb3ZpZGVyIHRvIHByZXBhcmUgZm9yIHN0YXJ0UXVlcnkgdG8gYmUgY2FsbGVkXG4gICAqIGluIG9yZGVyIHRvIHN0YXJ0IGEgbmV3IHF1ZXJ5IG9yIHJlZnJlc2ggYW4gZXhpc3Rpbmcgb25lLlxuICAgKi9cbiAgZW5kUXVlcnkoKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgdGhpcy53aWRnZXQuY29udGVudC5zZWFyY2hTZXJ2aWNlLmNsZWFyKCk7XG5cbiAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKCk7XG4gIH1cblxuICBwcml2YXRlIF9xdWVyeTogUmVnRXhwO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9