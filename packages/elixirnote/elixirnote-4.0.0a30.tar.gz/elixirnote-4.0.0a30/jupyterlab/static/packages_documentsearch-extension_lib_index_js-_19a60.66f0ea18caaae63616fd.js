"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_documentsearch-extension_lib_index_js-_19a60"],{

/***/ "../../packages/documentsearch-extension/lib/index.js":
/*!************************************************************!*\
  !*** ../../packages/documentsearch-extension/lib/index.js ***!
  \************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/documentsearch */ "webpack/sharing/consume/default/@jupyterlab/documentsearch/@jupyterlab/documentsearch");
/* harmony import */ var _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module documentsearch-extension
 */






const SEARCHABLE_CLASS = 'jp-mod-searchable';
var CommandIDs;
(function (CommandIDs) {
    /**
     * Start search in a document
     */
    CommandIDs.search = 'documentsearch:start';
    /**
     * Start search and replace in a document
     */
    CommandIDs.searchAndReplace = 'documentsearch:startWithReplace';
    /**
     * Find next search match
     */
    CommandIDs.findNext = 'documentsearch:highlightNext';
    /**
     * Find previous search match
     */
    CommandIDs.findPrevious = 'documentsearch:highlightPrevious';
})(CommandIDs || (CommandIDs = {}));
const labShellWidgetListener = {
    id: '@jupyterlab/documentsearch-extension:labShellWidgetListener',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.ISearchProviderRegistry],
    autoStart: true,
    activate: (app, labShell, registry) => {
        // If a given widget is searchable, apply the searchable class.
        // If it's not searchable, remove the class.
        const transformWidgetSearchability = (widget) => {
            if (!widget) {
                return;
            }
            if (registry.hasProvider(widget)) {
                widget.addClass(SEARCHABLE_CLASS);
            }
            else {
                widget.removeClass(SEARCHABLE_CLASS);
            }
        };
        // Update searchability of the active widget when the registry
        // changes, in case a provider for the current widget was added
        // or removed
        registry.changed.connect(() => transformWidgetSearchability(labShell.activeWidget));
        // Apply the searchable class only to the active widget if it is actually
        // searchable. Remove the searchable class from a widget when it's
        // no longer active.
        labShell.activeChanged.connect((_, args) => {
            const oldWidget = args.oldValue;
            if (oldWidget) {
                oldWidget.removeClass(SEARCHABLE_CLASS);
            }
            transformWidgetSearchability(args.newValue);
        });
    }
};
/**
 * Initialization data for the document-search extension.
 */
const extension = {
    id: '@jupyterlab/documentsearch-extension:plugin',
    provides: _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.ISearchProviderRegistry,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry],
    autoStart: true,
    activate: (app, translator, palette, settingRegistry) => {
        const trans = translator.load('jupyterlab');
        let searchDebounceTime = 500;
        // Create registry
        const registry = new _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.SearchProviderRegistry(translator);
        const searchViews = new Map();
        if (settingRegistry) {
            const loadSettings = settingRegistry.load(extension.id);
            const updateSettings = (settings) => {
                searchDebounceTime = settings.get('searchDebounceTime')
                    .composite;
            };
            Promise.all([loadSettings, app.restored])
                .then(([settings]) => {
                updateSettings(settings);
                settings.changed.connect(settings => {
                    updateSettings(settings);
                });
            })
                .catch((reason) => {
                console.error(reason.message);
            });
        }
        const isEnabled = () => {
            const widget = app.shell.currentWidget;
            if (!widget) {
                return false;
            }
            return registry.hasProvider(widget);
        };
        const getSearchWidget = (widget) => {
            if (!widget) {
                return;
            }
            const widgetId = widget.id;
            let searchView = searchViews.get(widgetId);
            if (!searchView) {
                const searchProvider = registry.getProvider(widget);
                if (!searchProvider) {
                    return;
                }
                const searchModel = new _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.SearchDocumentModel(searchProvider, searchDebounceTime);
                const newView = new _jupyterlab_documentsearch__WEBPACK_IMPORTED_MODULE_2__.SearchDocumentView(searchModel, translator);
                searchViews.set(widgetId, newView);
                // find next and previous are now enabled
                [CommandIDs.findNext, CommandIDs.findPrevious].forEach(id => {
                    app.commands.notifyCommandChanged(id);
                });
                /**
                 * Activate the target widget when the search panel is closing
                 */
                newView.closed.connect(() => {
                    if (!widget.isDisposed) {
                        widget.activate();
                    }
                });
                /**
                 * Remove from mapping when the search view is disposed.
                 */
                newView.disposed.connect(() => {
                    if (!widget.isDisposed) {
                        widget.activate();
                    }
                    searchViews.delete(widgetId);
                    // find next and previous are now disabled
                    [CommandIDs.findNext, CommandIDs.findPrevious].forEach(id => {
                        app.commands.notifyCommandChanged(id);
                    });
                });
                /**
                 * Dispose resources when the widget is disposed.
                 */
                widget.disposed.connect(() => {
                    newView.dispose();
                    searchModel.dispose();
                    searchProvider.dispose();
                });
                searchView = newView;
            }
            if (!searchView.isAttached) {
                _lumino_widgets__WEBPACK_IMPORTED_MODULE_5__.Widget.attach(searchView, widget.node);
                if (widget instanceof _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.MainAreaWidget) {
                    // Offset the position of the search widget to not cover the toolbar nor the content header.
                    // TODO this does not update once the search widget is displayed.
                    searchView.node.style.top = `${widget.toolbar.node.getBoundingClientRect().height +
                        widget.contentHeader.node.getBoundingClientRect().height}px`;
                }
                if (searchView.model.searchExpression) {
                    searchView.model.refresh();
                }
            }
            return searchView;
        };
        app.commands.addCommand(CommandIDs.search, {
            label: trans.__('Find…'),
            isEnabled: isEnabled,
            execute: args => {
                const searchWidget = getSearchWidget(app.shell.currentWidget);
                if (searchWidget) {
                    const searchText = args['searchText'];
                    if (searchText) {
                        searchWidget.setSearchText(searchText);
                    }
                    searchWidget.focusSearchInput();
                }
            }
        });
        app.commands.addCommand(CommandIDs.searchAndReplace, {
            label: trans.__('Find and Replace…'),
            isEnabled: isEnabled,
            execute: args => {
                const searchWidget = getSearchWidget(app.shell.currentWidget);
                if (searchWidget) {
                    const searchText = args['searchText'];
                    if (searchText) {
                        searchWidget.setSearchText(searchText);
                    }
                    const replaceText = args['replaceText'];
                    if (replaceText) {
                        searchWidget.setReplaceText(replaceText);
                    }
                    searchWidget.showReplace();
                    searchWidget.focusSearchInput();
                }
            }
        });
        app.commands.addCommand(CommandIDs.findNext, {
            label: trans.__('Find Next'),
            isEnabled: () => !!app.shell.currentWidget &&
                searchViews.has(app.shell.currentWidget.id),
            execute: async () => {
                var _a;
                const currentWidget = app.shell.currentWidget;
                if (!currentWidget) {
                    return;
                }
                await ((_a = searchViews.get(currentWidget.id)) === null || _a === void 0 ? void 0 : _a.model.highlightNext());
            }
        });
        app.commands.addCommand(CommandIDs.findPrevious, {
            label: trans.__('Find Previous'),
            isEnabled: () => !!app.shell.currentWidget &&
                searchViews.has(app.shell.currentWidget.id),
            execute: async () => {
                var _a;
                const currentWidget = app.shell.currentWidget;
                if (!currentWidget) {
                    return;
                }
                await ((_a = searchViews.get(currentWidget.id)) === null || _a === void 0 ? void 0 : _a.model.highlightPrevious());
            }
        });
        // Add the command to the palette.
        if (palette) {
            [CommandIDs.search, CommandIDs.findNext, CommandIDs.findPrevious].forEach(command => {
                palette.addItem({
                    command,
                    category: trans.__('Main Area')
                });
            });
        }
        // Provide the registry to the system.
        return registry;
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([extension, labShellWidgetListener]);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfZG9jdW1lbnRzZWFyY2gtZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fMTlhNjAuNjZmMGVhMThjYWFhZTYzNjE2ZmQuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFDM0Q7OztHQUdHO0FBTThCO0FBQ3NDO0FBTW5DO0FBQzJCO0FBQ1Q7QUFDYjtBQUV6QyxNQUFNLGdCQUFnQixHQUFHLG1CQUFtQixDQUFDO0FBRTdDLElBQVUsVUFBVSxDQWlCbkI7QUFqQkQsV0FBVSxVQUFVO0lBQ2xCOztPQUVHO0lBQ1UsaUJBQU0sR0FBRyxzQkFBc0IsQ0FBQztJQUM3Qzs7T0FFRztJQUNVLDJCQUFnQixHQUFHLGlDQUFpQyxDQUFDO0lBQ2xFOztPQUVHO0lBQ1UsbUJBQVEsR0FBRyw4QkFBOEIsQ0FBQztJQUN2RDs7T0FFRztJQUNVLHVCQUFZLEdBQUcsa0NBQWtDLENBQUM7QUFDakUsQ0FBQyxFQWpCUyxVQUFVLEtBQVYsVUFBVSxRQWlCbkI7QUFFRCxNQUFNLHNCQUFzQixHQUFnQztJQUMxRCxFQUFFLEVBQUUsNkRBQTZEO0lBQ2pFLFFBQVEsRUFBRSxDQUFDLDhEQUFTLEVBQUUsK0VBQXVCLENBQUM7SUFDOUMsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FDUixHQUFvQixFQUNwQixRQUFtQixFQUNuQixRQUFpQyxFQUNqQyxFQUFFO1FBQ0YsK0RBQStEO1FBQy9ELDRDQUE0QztRQUM1QyxNQUFNLDRCQUE0QixHQUFHLENBQUMsTUFBcUIsRUFBRSxFQUFFO1lBQzdELElBQUksQ0FBQyxNQUFNLEVBQUU7Z0JBQ1gsT0FBTzthQUNSO1lBQ0QsSUFBSSxRQUFRLENBQUMsV0FBVyxDQUFDLE1BQU0sQ0FBQyxFQUFFO2dCQUNoQyxNQUFNLENBQUMsUUFBUSxDQUFDLGdCQUFnQixDQUFDLENBQUM7YUFDbkM7aUJBQU07Z0JBQ0wsTUFBTSxDQUFDLFdBQVcsQ0FBQyxnQkFBZ0Is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QUMsR0FBRyxDQUFDLGFBQWEsQ0FBQyxFQUFFLENBQUMsMENBQUUsS0FBSyxDQUFDLGlCQUFpQixFQUFFLEVBQUM7WUFDckUsQ0FBQztTQUNGLENBQUMsQ0FBQztRQUVILGtDQUFrQztRQUNsQyxJQUFJLE9BQU8sRUFBRTtZQUNYLENBQUMsVUFBVSxDQUFDLE1BQU0sRUFBRSxVQUFVLENBQUMsUUFBUSxFQUFFLFVBQVUsQ0FBQyxZQUFZLENBQUMsQ0FBQyxPQUFPLENBQ3ZFLE9BQU8sQ0FBQyxFQUFFO2dCQUNSLE9BQU8sQ0FBQyxPQUFPLENBQUM7b0JBQ2QsT0FBTztvQkFDUCxRQUFRLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxXQUFXLENBQUM7aUJBQ2hDLENBQUMsQ0FBQztZQUNMLENBQUMsQ0FDRixDQUFDO1NBQ0g7UUFFRCxzQ0FBc0M7UUFDdEMsT0FBTyxRQUFRLENBQUM7SUFDbEIsQ0FBQztDQUNGLENBQUM7QUFFRixpRUFBZSxDQUFDLFNBQVMsRUFBRSxzQkFBc0IsQ0FBQyxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2RvY3VtZW50c2VhcmNoLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgZG9jdW1lbnRzZWFyY2gtZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBJQ29tbWFuZFBhbGV0dGUsIE1haW5BcmVhV2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHtcbiAgSVNlYXJjaFByb3ZpZGVyUmVnaXN0cnksXG4gIFNlYXJjaERvY3VtZW50TW9kZWwsXG4gIFNlYXJjaERvY3VtZW50VmlldyxcbiAgU2VhcmNoUHJvdmlkZXJSZWdpc3RyeVxufSBmcm9tICdAanVweXRlcmxhYi9kb2N1bWVudHNlYXJjaCc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgV2lkZ2V0IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcblxuY29uc3QgU0VBUkNIQUJMRV9DTEFTUyA9ICdqcC1tb2Qtc2VhcmNoYWJsZSc7XG5cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgLyoqXG4gICAqIFN0YXJ0IHNlYXJjaCBpbiBhIGRvY3VtZW50XG4gICAqL1xuICBleHBvcnQgY29uc3Qgc2VhcmNoID0gJ2RvY3VtZW50c2VhcmNoOnN0YXJ0JztcbiAgLyoqXG4gICAqIFN0YXJ0IHNlYXJjaCBhbmQgcmVwbGFjZSBpbiBhIGRvY3VtZW50XG4gICAqL1xuICBleHBvcnQgY29uc3Qgc2VhcmNoQW5kUmVwbGFjZSA9ICdkb2N1bWVudHNlYXJjaDpzdGFydFdpdGhSZXBsYWNlJztcbiAgLyoqXG4gICAqIEZpbmQgbmV4dCBzZWFyY2ggbWF0Y2hcbiAgICovXG4gIGV4cG9ydCBjb25zdCBmaW5kTmV4dCA9ICdkb2N1bWVudHNlYXJjaDpoaWdobGlnaHROZXh0JztcbiAgLyoqXG4gICAqIEZpbmQgcHJldmlvdXMgc2VhcmNoIG1hdGNoXG4gICAqL1xuICBleHBvcnQgY29uc3QgZmluZFByZXZpb3VzID0gJ2RvY3VtZW50c2VhcmNoOmhpZ2hsaWdodFByZXZpb3VzJztcbn1cblxuY29uc3QgbGFiU2hlbGxXaWRnZXRMaXN0ZW5lcjogSnVweXRlckZyb250RW5kUGx1Z2luPHZvaWQ+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2RvY3VtZW50c2VhcmNoLWV4dGVuc2lvbjpsYWJTaGVsbFdpZGdldExpc3RlbmVyJyxcbiAgcmVxdWlyZXM6IFtJTGFiU2hlbGwsIElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5XSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwsXG4gICAgcmVnaXN0cnk6IElTZWFyY2hQcm92aWRlclJlZ2lzdHJ5XG4gICkgPT4ge1xuICAgIC8vIElmIGEgZ2l2ZW4gd2lkZ2V0IGlzIHNlYXJjaGFibGUsIGFwcGx5IHRoZSBzZWFyY2hhYmxlIGNsYXNzLlxuICAgIC8vIElmIGl0J3Mgbm90IHNlYXJjaGFibGUsIHJlbW92ZSB0aGUgY2xhc3MuXG4gICAgY29uc3QgdHJhbnNmb3JtV2lkZ2V0U2VhcmNoYWJpbGl0eSA9ICh3aWRnZXQ6IFdpZGdldCB8IG51bGwpID0+IHtcbiAgICAgIGlmICghd2lkZ2V0KSB7XG4gICAgICAgIHJldHVybjtcbiAgICAgIH1cbiAgICAgIGlmIChyZWdpc3RyeS5oYXNQcm92aWRlcih3aWRnZXQpKSB7XG4gICAgICAgIHdpZGdldC5hZGRDbGFzcyhTRUFSQ0hBQkxFX0NMQVNTKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHdpZGdldC5yZW1vdmVDbGFzcyhTRUFSQ0hBQkxFX0NMQVNTKTtcbiAgICAgIH1cbiAgICB9O1xuXG4gICAgLy8gVXBkYXRlIHNlYXJjaGFiaWxpdHkgb2YgdGhlIGFjdGl2ZSB3aWRnZXQgd2hlbiB0aGUgcmVnaXN0cnlcbiAgICAvLyBjaGFuZ2VzLCBpbiBjYXNlIGEgcHJvdmlkZXIgZm9yIHRoZSBjdXJyZW50IHdpZGdldCB3YXMgYWRkZWRcbiAgICAvLyBvciByZW1vdmVkXG4gICAgcmVnaXN0cnkuY2hhbmdlZC5jb25uZWN0KCgpID0+XG4gICAgICB0cmFuc2Zvcm1XaWRnZXRTZWFyY2hhYmlsaXR5KGxhYlNoZWxsLmFjdGl2ZVdpZGdldClcbiAgICApO1xuXG4gICAgLy8gQXBwbHkgdGhlIHNlYXJjaGFibGUgY2xhc3Mgb25seSB0byB0aGUgYWN0aXZlIHdpZGdldCBpZiBpdCBpcyBhY3R1YWxseVxuICAgIC8vIHNlYXJjaGFibGUuIFJlbW92ZSB0aGUgc2VhcmNoYWJsZSBjbGFzcyBmcm9tIGEgd2lkZ2V0IHdoZW4gaXQnc1xuICAgIC8vIG5vIGxvbmdlciBhY3RpdmUuXG4gICAgbGFiU2hlbGwuYWN0aXZlQ2hhbmdlZC5jb25uZWN0KChfLCBhcmdzKSA9PiB7XG4gICAgICBjb25zdCBvbGRXaWRnZXQgPSBhcmdzLm9sZFZhbHVlO1xuICAgICAgaWYgKG9sZFdpZGdldCkge1xuICAgICAgICBvbGRXaWRnZXQucmVtb3ZlQ2xhc3MoU0VBUkNIQUJMRV9DTEFTUyk7XG4gICAgICB9XG4gICAgICB0cmFuc2Zvcm1XaWRnZXRTZWFyY2hhYmlsaXR5KGFyZ3MubmV3VmFsdWUpO1xuICAgIH0pO1xuICB9XG59O1xuXG4vKipcbiAqIEluaXRpYWxpemF0aW9uIGRhdGEgZm9yIHRoZSBkb2N1bWVudC1zZWFyY2ggZXh0ZW5zaW9uLlxuICovXG5jb25zdCBleHRlbnNpb246IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeT4gPSB7XG4gIGlkOiAnQGp1cHl0ZXJsYWIvZG9jdW1lbnRzZWFyY2gtZXh0ZW5zaW9uOnBsdWdpbicsXG4gIHByb3ZpZGVzOiBJU2VhcmNoUHJvdmlkZXJSZWdpc3RyeSxcbiAgcmVxdWlyZXM6IFtJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUNvbW1hbmRQYWxldHRlLCBJU2V0dGluZ1JlZ2lzdHJ5XSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICAgIHBhbGV0dGU6IElDb21tYW5kUGFsZXR0ZSxcbiAgICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgICBsZXQgc2VhcmNoRGVib3VuY2VUaW1lID0gNTAwO1xuXG4gICAgLy8gQ3JlYXRlIHJlZ2lzdHJ5XG4gICAgY29uc3QgcmVnaXN0cnk6IFNlYXJjaFByb3ZpZGVyUmVnaXN0cnkgPSBuZXcgU2VhcmNoUHJvdmlkZXJSZWdpc3RyeShcbiAgICAgIHRyYW5zbGF0b3JcbiAgICApO1xuXG4gICAgY29uc3Qgc2VhcmNoVmlld3MgPSBuZXcgTWFwPHN0cmluZywgU2VhcmNoRG9jdW1lbnRWaWV3PigpO1xuXG4gICAgaWYgKHNldHRpbmdSZWdpc3RyeSkge1xuICAgICAgY29uc3QgbG9hZFNldHRpbmdzID0gc2V0dGluZ1JlZ2lzdHJ5LmxvYWQoZXh0ZW5zaW9uLmlkKTtcbiAgICAgIGNvbnN0IHVwZGF0ZVNldHRpbmdzID0gKHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyk6IHZvaWQgPT4ge1xuICAgICAgICBzZWFyY2hEZWJvdW5jZVRpbWUgPSBzZXR0aW5ncy5nZXQoJ3NlYXJjaERlYm91bmNlVGltZScpXG4gICAgICAgICAgLmNvbXBvc2l0ZSBhcyBudW1iZXI7XG4gICAgICB9O1xuXG4gICAgICBQcm9taXNlLmFsbChbbG9hZFNldHRpbmdzLCBhcHAucmVzdG9yZWRdKVxuICAgICAgICAudGhlbigoW3NldHRpbmdzXSkgPT4ge1xuICAgICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3Qoc2V0dGluZ3MgPT4ge1xuICAgICAgICAgICAgdXBkYXRlU2V0dGluZ3Moc2V0dGluZ3MpO1xuICAgICAgICAgIH0pO1xuICAgICAgICB9KVxuICAgICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgICBjb25zb2xlLmVycm9yKHJlYXNvbi5tZXNzYWdlKTtcbiAgICAgICAgfSk7XG4gICAgfVxuXG4gICAgY29uc3QgaXNFbmFibGVkID0gKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXQ7XG4gICAgICBpZiAoIXdpZGdldCkge1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG4gICAgICByZXR1cm4gcmVnaXN0cnkuaGFzUHJvdmlkZXIod2lkZ2V0KTtcbiAgICB9O1xuXG4gICAgY29uc3QgZ2V0U2VhcmNoV2lkZ2V0ID0gKHdpZGdldDogV2lkZ2V0IHwgbnVsbCkgPT4ge1xuICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3Qgd2lkZ2V0SWQgPSB3aWRnZXQuaWQ7XG4gICAgICBsZXQgc2VhcmNoVmlldyA9IHNlYXJjaFZpZXdzLmdldCh3aWRnZXRJZCk7XG4gICAgICBpZiAoIXNlYXJjaFZpZXcpIHtcbiAgICAgICAgY29uc3Qgc2VhcmNoUHJvdmlkZXIgPSByZWdpc3RyeS5nZXRQcm92aWRlcih3aWRnZXQpO1xuICAgICAgICBpZiAoIXNlYXJjaFByb3ZpZGVyKSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHNlYXJjaE1vZGVsID0gbmV3IFNlYXJjaERvY3VtZW50TW9kZWwoXG4gICAgICAgICAgc2VhcmNoUHJvdmlkZXIsXG4gICAgICAgICAgc2VhcmNoRGVib3VuY2VUaW1lXG4gICAgICAgICk7XG5cbiAgICAgICAgY29uc3QgbmV3VmlldyA9IG5ldyBTZWFyY2hEb2N1bWVudFZpZXcoc2VhcmNoTW9kZWwsIHRyYW5zbGF0b3IpO1xuXG4gICAgICAgIHNlYXJjaFZpZXdzLnNldCh3aWRnZXRJZCwgbmV3Vmlldyk7XG4gICAgICAgIC8vIGZpbmQgbmV4dCBhbmQgcHJldmlvdXMgYXJlIG5vdyBlbmFibGVkXG4gICAgICAgIFtDb21tYW5kSURzLmZpbmROZXh0LCBDb21tYW5kSURzLmZpbmRQcmV2aW91c10uZm9yRWFjaChpZCA9PiB7XG4gICAgICAgICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKGlkKTtcbiAgICAgICAgfSk7XG5cbiAgICAgICAgLyoqXG4gICAgICAgICAqIEFjdGl2YXRlIHRoZSB0YXJnZXQgd2lkZ2V0IHdoZW4gdGhlIHNlYXJjaCBwYW5lbCBpcyBjbG9zaW5nXG4gICAgICAgICAqL1xuICAgICAgICBuZXdWaWV3LmNsb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgICBpZiAoIXdpZGdldC5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgICB3aWRnZXQuYWN0aXZhdGUoKTtcbiAgICAgICAgICB9XG4gICAgICAgIH0pO1xuXG4gICAgICAgIC8qKlxuICAgICAgICAgKiBSZW1vdmUgZnJvbSBtYXBwaW5nIHdoZW4gdGhlIHNlYXJjaCB2aWV3IGlzIGRpc3Bvc2VkLlxuICAgICAgICAgKi9cbiAgICAgICAgbmV3Vmlldy5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgICBpZiAoIXdpZGdldC5pc0Rpc3Bvc2VkKSB7XG4gICAgICAgICAgICB3aWRnZXQuYWN0aXZhdGUoKTtcbiAgICAgICAgICB9XG4gICAgICAgICAgc2VhcmNoVmlld3MuZGVsZXRlKHdpZGdldElkKTtcbiAgICAgICAgICAvLyBmaW5kIG5leHQgYW5kIHByZXZpb3VzIGFyZSBub3cgZGlzYWJsZWRcbiAgICAgICAgICBbQ29tbWFuZElEcy5maW5kTmV4dCwgQ29tbWFuZElEcy5maW5kUHJldmlvdXNdLmZvckVhY2goaWQgPT4ge1xuICAgICAgICAgICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKGlkKTtcbiAgICAgICAgICB9KTtcbiAgICAgICAgfSk7XG5cbiAgICAgICAgLyoqXG4gICAgICAgICAqIERpc3Bvc2UgcmVzb3VyY2VzIHdoZW4gdGhlIHdpZGdldCBpcyBkaXNwb3NlZC5cbiAgICAgICAgICovXG4gICAgICAgIHdpZGdldC5kaXNwb3NlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgICAgICBuZXdWaWV3LmRpc3Bvc2UoKTtcbiAgICAgICAgICBzZWFyY2hNb2RlbC5kaXNwb3NlKCk7XG4gICAgICAgICAgc2VhcmNoUHJvdmlkZXIuZGlzcG9zZSgpO1xuICAgICAgICB9KTtcblxuICAgICAgICBzZWFyY2hWaWV3ID0gbmV3VmlldztcbiAgICAgIH1cblxuICAgICAgaWYgKCFzZWFyY2hWaWV3LmlzQXR0YWNoZWQpIHtcbiAgICAgICAgV2lkZ2V0LmF0dGFjaChzZWFyY2hWaWV3LCB3aWRnZXQubm9kZSk7XG4gICAgICAgIGlmICh3aWRnZXQgaW5zdGFuY2VvZiBNYWluQXJlYVdpZGdldCkge1xuICAgICAgICAgIC8vIE9mZnNldCB0aGUgcG9zaXRpb24gb2YgdGhlIHNlYXJjaCB3aWRnZXQgdG8gbm90IGNvdmVyIHRoZSB0b29sYmFyIG5vciB0aGUgY29udGVudCBoZWFkZXIuXG4gICAgICAgICAgLy8gVE9ETyB0aGlzIGRvZXMgbm90IHVwZGF0ZSBvbmNlIHRoZSBzZWFyY2ggd2lkZ2V0IGlzIGRpc3BsYXllZC5cbiAgICAgICAgICBzZWFyY2hWaWV3Lm5vZGUuc3R5bGUudG9wID0gYCR7XG4gICAgICAgICAgICB3aWRnZXQudG9vbGJhci5ub2RlLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLmhlaWdodCArXG4gICAgICAgICAgICB3aWRnZXQuY29udGVudEhlYWRlci5ub2RlLmdldEJvdW5kaW5nQ2xpZW50UmVjdCgpLmhlaWdodFxuICAgICAgICAgIH1weGA7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKHNlYXJjaFZpZXcubW9kZWwuc2VhcmNoRXhwcmVzc2lvbikge1xuICAgICAgICAgIHNlYXJjaFZpZXcubW9kZWwucmVmcmVzaCgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICByZXR1cm4gc2VhcmNoVmlldztcbiAgICB9O1xuXG4gICAgYXBwLmNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zZWFyY2gsIHtcbiAgICAgIGxhYmVsOiB0cmFucy5fXygnRmluZOKApicpLFxuICAgICAgaXNFbmFibGVkOiBpc0VuYWJsZWQsXG4gICAgICBleGVjdXRlOiBhcmdzID0+IHtcbiAgICAgICAgY29uc3Qgc2VhcmNoV2lkZ2V0ID0gZ2V0U2VhcmNoV2lkZ2V0KGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0KTtcbiAgICAgICAgaWYgKHNlYXJjaFdpZGdldCkge1xuICAgICAgICAgIGNvbnN0IHNlYXJjaFRleHQgPSBhcmdzWydzZWFyY2hUZXh0J10gYXMgc3RyaW5nO1xuICAgICAgICAgIGlmIChzZWFyY2hUZXh0KSB7XG4gICAgICAgICAgICBzZWFyY2hXaWRnZXQuc2V0U2VhcmNoVGV4dChzZWFyY2hUZXh0KTtcbiAgICAgICAgICB9XG4gICAgICAgICAgc2VhcmNoV2lkZ2V0LmZvY3VzU2VhcmNoSW5wdXQoKTtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuXG4gICAgYXBwLmNvbW1hbmRzLmFkZENvbW1hbmQoQ29tbWFuZElEcy5zZWFyY2hBbmRSZXBsYWNlLCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0ZpbmQgYW5kIFJlcGxhY2XigKYnKSxcbiAgICAgIGlzRW5hYmxlZDogaXNFbmFibGVkLFxuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IHNlYXJjaFdpZGdldCA9IGdldFNlYXJjaFdpZGdldChhcHAuc2hlbGwuY3VycmVudFdpZGdldCk7XG4gICAgICAgIGlmIChzZWFyY2hXaWRnZXQpIHtcbiAgICAgICAgICBjb25zdCBzZWFyY2hUZXh0ID0gYXJnc1snc2VhcmNoVGV4dCddIGFzIHN0cmluZztcbiAgICAgICAgICBpZiAoc2VhcmNoVGV4dCkge1xuICAgICAgICAgICAgc2VhcmNoV2lkZ2V0LnNldFNlYXJjaFRleHQoc2VhcmNoVGV4dCk7XG4gICAgICAgICAgfVxuICAgICAgICAgIGNvbnN0IHJlcGxhY2VUZXh0ID0gYXJnc1sncmVwbGFjZVRleHQnXSBhcyBzdHJpbmc7XG4gICAgICAgICAgaWYgKHJlcGxhY2VUZXh0KSB7XG4gICAgICAgICAgICBzZWFyY2hXaWRnZXQuc2V0UmVwbGFjZVRleHQocmVwbGFjZVRleHQpO1xuICAgICAgICAgIH1cbiAgICAgICAgICBzZWFyY2hXaWRnZXQuc2hvd1JlcGxhY2UoKTtcbiAgICAgICAgICBzZWFyY2hXaWRnZXQuZm9jdXNTZWFyY2hJbnB1dCgpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmZpbmROZXh0LCB7XG4gICAgICBsYWJlbDogdHJhbnMuX18oJ0ZpbmQgTmV4dCcpLFxuICAgICAgaXNFbmFibGVkOiAoKSA9PlxuICAgICAgICAhIWFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0ICYmXG4gICAgICAgIHNlYXJjaFZpZXdzLmhhcyhhcHAuc2hlbGwuY3VycmVudFdpZGdldC5pZCksXG4gICAgICBleGVjdXRlOiBhc3luYyAoKSA9PiB7XG4gICAgICAgIGNvbnN0IGN1cnJlbnRXaWRnZXQgPSBhcHAuc2hlbGwuY3VycmVudFdpZGdldDtcbiAgICAgICAgaWYgKCFjdXJyZW50V2lkZ2V0KSB7XG4gICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG5cbiAgICAgICAgYXdhaXQgc2VhcmNoVmlld3MuZ2V0KGN1cnJlbnRXaWRnZXQuaWQpPy5tb2RlbC5oaWdobGlnaHROZXh0KCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLmZpbmRQcmV2aW91cywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdGaW5kIFByZXZpb3VzJyksXG4gICAgICBpc0VuYWJsZWQ6ICgpID0+XG4gICAgICAgICEhYXBwLnNoZWxsLmN1cnJlbnRXaWRnZXQgJiZcbiAgICAgICAgc2VhcmNoVmlld3MuaGFzKGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0LmlkKSxcbiAgICAgIGV4ZWN1dGU6IGFzeW5jICgpID0+IHtcbiAgICAgICAgY29uc3QgY3VycmVudFdpZGdldCA9IGFwcC5zaGVsbC5jdXJyZW50V2lkZ2V0O1xuICAgICAgICBpZiAoIWN1cnJlbnRXaWRnZXQpIHtcbiAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cblxuICAgICAgICBhd2FpdCBzZWFyY2hWaWV3cy5nZXQoY3VycmVudFdpZGdldC5pZCk/Lm1vZGVsLmhpZ2hsaWdodFByZXZpb3VzKCk7XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICAvLyBBZGQgdGhlIGNvbW1hbmQgdG8gdGhlIHBhbGV0dGUuXG4gICAgaWYgKHBhbGV0dGUpIHtcbiAgICAgIFtDb21tYW5kSURzLnNlYXJjaCwgQ29tbWFuZElEcy5maW5kTmV4dCwgQ29tbWFuZElEcy5maW5kUHJldmlvdXNdLmZvckVhY2goXG4gICAgICAgIGNvbW1hbmQgPT4ge1xuICAgICAgICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICAgICAgICBjb21tYW5kLFxuICAgICAgICAgICAgY2F0ZWdvcnk6IHRyYW5zLl9fKCdNYWluIEFyZWEnKVxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICApO1xuICAgIH1cblxuICAgIC8vIFByb3ZpZGUgdGhlIHJlZ2lzdHJ5IHRvIHRoZSBzeXN0ZW0uXG4gICAgcmV0dXJuIHJlZ2lzdHJ5O1xuICB9XG59O1xuXG5leHBvcnQgZGVmYXVsdCBbZXh0ZW5zaW9uLCBsYWJTaGVsbFdpZGdldExpc3RlbmVyXTtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==