"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_markdownviewer-extension_lib_index_js-_c03d1"],{

/***/ "../../packages/markdownviewer-extension/lib/index.js":
/*!************************************************************!*\
  !*** ../../packages/markdownviewer-extension/lib/index.js ***!
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
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/markdownviewer */ "webpack/sharing/consume/default/@jupyterlab/markdownviewer/@jupyterlab/markdownviewer");
/* harmony import */ var _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/toc */ "webpack/sharing/consume/default/@jupyterlab/toc/@jupyterlab/toc");
/* harmony import */ var _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_toc__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module markdownviewer-extension
 */








/**
 * The command IDs used by the markdownviewer plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.markdownPreview = 'markdownviewer:open';
    CommandIDs.markdownEditor = 'markdownviewer:edit';
})(CommandIDs || (CommandIDs = {}));
/**
 * The name of the factory that creates markdown viewer widgets.
 */
const FACTORY = 'Markdown Preview';
/**
 * The markdown viewer plugin.
 */
const plugin = {
    activate,
    id: '@jupyterlab/markdownviewer-extension:plugin',
    provides: _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__.IMarkdownViewerTracker,
    requires: [_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.IRenderMimeRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_5__.ISettingRegistry, _jupyterlab_toc__WEBPACK_IMPORTED_MODULE_6__.ITableOfContentsRegistry],
    autoStart: true
};
/**
 * Activate the markdown viewer plugin.
 */
function activate(app, rendermime, translator, restorer, settingRegistry, tocRegistry) {
    const trans = translator.load('jupyterlab');
    const { commands, docRegistry } = app;
    // Add the markdown renderer factory.
    rendermime.addFactory(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.markdownRendererFactory);
    const namespace = 'markdownviewer-widget';
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace
    });
    let config = Object.assign({}, _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__.MarkdownViewer.defaultConfig);
    /**
     * Update the settings of a widget.
     */
    function updateWidget(widget) {
        Object.keys(config).forEach((k) => {
            var _a;
            widget.setOption(k, (_a = config[k]) !== null && _a !== void 0 ? _a : null);
        });
    }
    if (settingRegistry) {
        const updateSettings = (settings) => {
            config = settings.composite;
            tracker.forEach(widget => {
                updateWidget(widget.content);
            });
        };
        // Fetch the initial state of the settings.
        settingRegistry
            .load(plugin.id)
            .then((settings) => {
            settings.changed.connect(() => {
                updateSettings(settings);
            });
            updateSettings(settings);
        })
            .catch((reason) => {
            console.error(reason.message);
        });
    }
    // Register the MarkdownViewer factory.
    const factory = new _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__.MarkdownViewerFactory({
        rendermime,
        name: FACTORY,
        label: trans.__('Markdown Preview'),
        primaryFileType: docRegistry.getFileType('markdown'),
        fileTypes: ['markdown'],
        defaultRendered: ['markdown']
    });
    factory.widgetCreated.connect((sender, widget) => {
        // Notify the widget tracker if restore data needs to update.
        widget.context.pathChanged.connect(() => {
            void tracker.save(widget);
        });
        // Handle the settings of new widgets.
        updateWidget(widget.content);
        void tracker.add(widget);
    });
    docRegistry.addWidgetFactory(factory);
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: 'docmanager:open',
            args: widget => ({ path: widget.context.path, factory: FACTORY }),
            name: widget => widget.context.path
        });
    }
    commands.addCommand(CommandIDs.markdownPreview, {
        label: trans.__('Markdown Preview'),
        execute: args => {
            const path = args['path'];
            if (typeof path !== 'string') {
                return;
            }
            return commands.execute('docmanager:open', {
                path,
                factory: FACTORY,
                options: args['options']
            });
        }
    });
    commands.addCommand(CommandIDs.markdownEditor, {
        execute: () => {
            const widget = tracker.currentWidget;
            if (!widget) {
                return;
            }
            const path = widget.context.path;
            return commands.execute('docmanager:open', {
                path,
                factory: 'Editor',
                options: {
                    mode: 'split-right'
                }
            });
        },
        isVisible: () => {
            const widget = tracker.currentWidget;
            return ((widget && _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.extname(widget.context.path) === '.md') || false);
        },
        label: trans.__('Show Markdown Editor')
    });
    if (tocRegistry) {
        tocRegistry.add(new _jupyterlab_markdownviewer__WEBPACK_IMPORTED_MODULE_3__.MarkdownViewerTableOfContentsFactory(tracker, rendermime.markdownParser));
    }
    return tracker;
}
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbWFya2Rvd252aWV3ZXItZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fYzAzZDEuZmRhYjQ3MWE0NDMwZTQxZTdmNGQuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQU04QjtBQUNvQjtBQUNMO0FBT1o7QUFJSjtBQUMrQjtBQUNKO0FBQ0w7QUFFdEQ7O0dBRUc7QUFDSCxJQUFVLFVBQVUsQ0FHbkI7QUFIRCxXQUFVLFVBQVU7SUFDTCwwQkFBZSxHQUFHLHFCQUFxQixDQUFDO0lBQ3hDLHlCQUFjLEdBQUcscUJBQXFCLENBQUM7QUFDdEQsQ0FBQyxFQUhTLFVBQVUsS0FBVixVQUFVLFFBR25CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLE9BQU8sR0FBRyxrQkFBa0IsQ0FBQztBQUVuQzs7R0FFRztBQUNILE1BQU0sTUFBTSxHQUFrRDtJQUM1RCxRQUFRO0lBQ1IsRUFBRSxFQUFFLDZDQUE2QztJQUNqRCxRQUFRLEVBQUUsOEVBQXNCO0lBQ2hDLFFBQVEsRUFBRSxDQUFDLHVFQUFtQixFQUFFLGdFQUFXLENBQUM7SUFDNUMsUUFBUSxFQUFFLENBQUMsb0VBQWUsRUFBRSx5RUFBZ0IsRUFBRSxxRUFBd0IsQ0FBQztJQUN2RSxTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxTQUFTLFFBQVEsQ0FDZixHQUFvQixFQUNwQixVQUErQixFQUMvQixVQUF1QixFQUN2QixRQUFnQyxFQUNoQyxlQUF3QyxFQUN4QyxXQUE0QztJQUU1QyxNQUFNLEtBQUssR0FBRyxVQUFVLENBQUMsSUFBSSxDQUFDLFlBQVksQ0FBQyxDQUFDO0lBQzVDLE1BQU0sRUFBRSxRQUFRLEVBQUUsV0FBVyxFQUFFLEdBQUcsR0FBRyxDQUFDO0lBRXRDLHFDQUFxQztJQUNyQyxVQUFVLENBQUMsVUFBVSxDQUFDLDJFQUF1QixDQUFDLENBQUM7SUFFL0MsTUFBTSxT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SyxDQUNwRSxDQUFDO1FBQ0osQ0FBQztRQUNELEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLHNCQUFzQixDQUFDO0tBQ3hDLENBQUMsQ0FBQztJQUVILElBQUksV0FBVyxFQUFFO1FBQ2YsV0FBVyxDQUFDLEdBQUcsQ0FDYixJQUFJLDRGQUFvQyxDQUN0QyxPQUFPLEVBQ1AsVUFBVSxDQUFDLGNBQWMsQ0FDMUIsQ0FDRixDQUFDO0tBQ0g7SUFFRCxPQUFPLE9BQU8sQ0FBQztBQUNqQixDQUFDO0FBRUQ7O0dBRUc7QUFDSCxpRUFBZSxNQUFNLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvbWFya2Rvd252aWV3ZXItZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBtYXJrZG93bnZpZXdlci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IFdpZGdldFRyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBQYXRoRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7XG4gIElNYXJrZG93blZpZXdlclRyYWNrZXIsXG4gIE1hcmtkb3duRG9jdW1lbnQsXG4gIE1hcmtkb3duVmlld2VyLFxuICBNYXJrZG93blZpZXdlckZhY3RvcnksXG4gIE1hcmtkb3duVmlld2VyVGFibGVPZkNvbnRlbnRzRmFjdG9yeVxufSBmcm9tICdAanVweXRlcmxhYi9tYXJrZG93bnZpZXdlcic7XG5pbXBvcnQge1xuICBJUmVuZGVyTWltZVJlZ2lzdHJ5LFxuICBtYXJrZG93blJlbmRlcmVyRmFjdG9yeVxufSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvdG9jJztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIFRoZSBjb21tYW5kIElEcyB1c2VkIGJ5IHRoZSBtYXJrZG93bnZpZXdlciBwbHVnaW4uXG4gKi9cbm5hbWVzcGFjZSBDb21tYW5kSURzIHtcbiAgZXhwb3J0IGNvbnN0IG1hcmtkb3duUHJldmlldyA9ICdtYXJrZG93bnZpZXdlcjpvcGVuJztcbiAgZXhwb3J0IGNvbnN0IG1hcmtkb3duRWRpdG9yID0gJ21hcmtkb3dudmlld2VyOmVkaXQnO1xufVxuXG4vKipcbiAqIFRoZSBuYW1lIG9mIHRoZSBmYWN0b3J5IHRoYXQgY3JlYXRlcyBtYXJrZG93biB2aWV3ZXIgd2lkZ2V0cy5cbiAqL1xuY29uc3QgRkFDVE9SWSA9ICdNYXJrZG93biBQcmV2aWV3JztcblxuLyoqXG4gKiBUaGUgbWFya2Rvd24gdmlld2VyIHBsdWdpbi5cbiAqL1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SU1hcmtkb3duVmlld2VyVHJhY2tlcj4gPSB7XG4gIGFjdGl2YXRlLFxuICBpZDogJ0BqdXB5dGVybGFiL21hcmtkb3dudmlld2VyLWV4dGVuc2lvbjpwbHVnaW4nLFxuICBwcm92aWRlczogSU1hcmtkb3duVmlld2VyVHJhY2tlcixcbiAgcmVxdWlyZXM6IFtJUmVuZGVyTWltZVJlZ2lzdHJ5LCBJVHJhbnNsYXRvcl0sXG4gIG9wdGlvbmFsOiBbSUxheW91dFJlc3RvcmVyLCBJU2V0dGluZ1JlZ2lzdHJ5LCBJVGFibGVPZkNvbnRlbnRzUmVnaXN0cnldLFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbi8qKlxuICogQWN0aXZhdGUgdGhlIG1hcmtkb3duIHZpZXdlciBwbHVnaW4uXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlKFxuICBhcHA6IEp1cHl0ZXJGcm9udEVuZCxcbiAgcmVuZGVybWltZTogSVJlbmRlck1pbWVSZWdpc3RyeSxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3IsXG4gIHJlc3RvcmVyOiBJTGF5b3V0UmVzdG9yZXIgfCBudWxsLFxuICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnkgfCBudWxsLFxuICB0b2NSZWdpc3RyeTogSVRhYmxlT2ZDb250ZW50c1JlZ2lzdHJ5IHwgbnVsbFxuKTogSU1hcmtkb3duVmlld2VyVHJhY2tlciB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IHsgY29tbWFuZHMsIGRvY1JlZ2lzdHJ5IH0gPSBhcHA7XG5cbiAgLy8gQWRkIHRoZSBtYXJrZG93biByZW5kZXJlciBmYWN0b3J5LlxuICByZW5kZXJtaW1lLmFkZEZhY3RvcnkobWFya2Rvd25SZW5kZXJlckZhY3RvcnkpO1xuXG4gIGNvbnN0IG5hbWVzcGFjZSA9ICdtYXJrZG93bnZpZXdlci13aWRnZXQnO1xuICBjb25zdCB0cmFja2VyID0gbmV3IFdpZGdldFRyYWNrZXI8TWFya2Rvd25Eb2N1bWVudD4oe1xuICAgIG5hbWVzcGFjZVxuICB9KTtcblxuICBsZXQgY29uZmlnOiBQYXJ0aWFsPE1hcmtkb3duVmlld2VyLklDb25maWc+ID0ge1xuICAgIC4uLk1hcmtkb3duVmlld2VyLmRlZmF1bHRDb25maWdcbiAgfTtcblxuICAvKipcbiAgICogVXBkYXRlIHRoZSBzZXR0aW5ncyBvZiBhIHdpZGdldC5cbiAgICovXG4gIGZ1bmN0aW9uIHVwZGF0ZVdpZGdldCh3aWRnZXQ6IE1hcmtkb3duVmlld2VyKTogdm9pZCB7XG4gICAgT2JqZWN0LmtleXMoY29uZmlnKS5mb3JFYWNoKChrOiBrZXlvZiBNYXJrZG93blZpZXdlci5JQ29uZmlnKSA9PiB7XG4gICAgICB3aWRnZXQuc2V0T3B0aW9uKGssIGNvbmZpZ1trXSA/PyBudWxsKTtcbiAgICB9KTtcbiAgfVxuXG4gIGlmIChzZXR0aW5nUmVnaXN0cnkpIHtcbiAgICBjb25zdCB1cGRhdGVTZXR0aW5ncyA9IChzZXR0aW5nczogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3MpID0+IHtcbiAgICAgIGNvbmZpZyA9IHNldHRpbmdzLmNvbXBvc2l0ZSBhcyBQYXJ0aWFsPE1hcmtkb3duVmlld2VyLklDb25maWc+O1xuICAgICAgdHJhY2tlci5mb3JFYWNoKHdpZGdldCA9PiB7XG4gICAgICAgIHVwZGF0ZVdpZGdldCh3aWRnZXQuY29udGVudCk7XG4gICAgICB9KTtcbiAgICB9O1xuXG4gICAgLy8gRmV0Y2ggdGhlIGluaXRpYWwgc3RhdGUgb2YgdGhlIHNldHRpbmdzLlxuICAgIHNldHRpbmdSZWdpc3RyeVxuICAgICAgLmxvYWQocGx1Z2luLmlkKVxuICAgICAgLnRoZW4oKHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncykgPT4ge1xuICAgICAgICBzZXR0aW5ncy5jaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgICAgfSk7XG4gICAgICAgIHVwZGF0ZVNldHRpbmdzKHNldHRpbmdzKTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihyZWFzb24ubWVzc2FnZSk7XG4gICAgICB9KTtcbiAgfVxuXG4gIC8vIFJlZ2lzdGVyIHRoZSBNYXJrZG93blZpZXdlciBmYWN0b3J5LlxuICBjb25zdCBmYWN0b3J5ID0gbmV3IE1hcmtkb3duVmlld2VyRmFjdG9yeSh7XG4gICAgcmVuZGVybWltZSxcbiAgICBuYW1lOiBGQUNUT1JZLFxuICAgIGxhYmVsOiB0cmFucy5fXygnTWFya2Rvd24gUHJldmlldycpLFxuICAgIHByaW1hcnlGaWxlVHlwZTogZG9jUmVnaXN0cnkuZ2V0RmlsZVR5cGUoJ21hcmtkb3duJyksXG4gICAgZmlsZVR5cGVzOiBbJ21hcmtkb3duJ10sXG4gICAgZGVmYXVsdFJlbmRlcmVkOiBbJ21hcmtkb3duJ11cbiAgfSk7XG4gIGZhY3Rvcnkud2lkZ2V0Q3JlYXRlZC5jb25uZWN0KChzZW5kZXIsIHdpZGdldCkgPT4ge1xuICAgIC8vIE5vdGlmeSB0aGUgd2lkZ2V0IHRyYWNrZXIgaWYgcmVzdG9yZSBkYXRhIG5lZWRzIHRvIHVwZGF0ZS5cbiAgICB3aWRnZXQuY29udGV4dC5wYXRoQ2hhbmdlZC5jb25uZWN0KCgpID0+IHtcbiAgICAgIHZvaWQgdHJhY2tlci5zYXZlKHdpZGdldCk7XG4gICAgfSk7XG4gICAgLy8gSGFuZGxlIHRoZSBzZXR0aW5ncyBvZiBuZXcgd2lkZ2V0cy5cbiAgICB1cGRhdGVXaWRnZXQod2lkZ2V0LmNvbnRlbnQpO1xuICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgfSk7XG4gIGRvY1JlZ2lzdHJ5LmFkZFdpZGdldEZhY3RvcnkoZmFjdG9yeSk7XG5cbiAgLy8gSGFuZGxlIHN0YXRlIHJlc3RvcmF0aW9uLlxuICBpZiAocmVzdG9yZXIpIHtcbiAgICB2b2lkIHJlc3RvcmVyLnJlc3RvcmUodHJhY2tlciwge1xuICAgICAgY29tbWFuZDogJ2RvY21hbmFnZXI6b3BlbicsXG4gICAgICBhcmdzOiB3aWRnZXQgPT4gKHsgcGF0aDogd2lkZ2V0LmNvbnRleHQucGF0aCwgZmFjdG9yeTogRkFDVE9SWSB9KSxcbiAgICAgIG5hbWU6IHdpZGdldCA9PiB3aWRnZXQuY29udGV4dC5wYXRoXG4gICAgfSk7XG4gIH1cblxuICBjb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMubWFya2Rvd25QcmV2aWV3LCB7XG4gICAgbGFiZWw6IHRyYW5zLl9fKCdNYXJrZG93biBQcmV2aWV3JyksXG4gICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICBjb25zdCBwYXRoID0gYXJnc1sncGF0aCddO1xuICAgICAgaWYgKHR5cGVvZiBwYXRoICE9PSAnc3RyaW5nJykge1xuICAgICAgICByZXR1cm47XG4gICAgICB9XG4gICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpvcGVuJywge1xuICAgICAgICBwYXRoLFxuICAgICAgICBmYWN0b3J5OiBGQUNUT1JZLFxuICAgICAgICBvcHRpb25zOiBhcmdzWydvcHRpb25zJ11cbiAgICAgIH0pO1xuICAgIH1cbiAgfSk7XG5cbiAgY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLm1hcmtkb3duRWRpdG9yLCB7XG4gICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgY29uc3Qgd2lkZ2V0ID0gdHJhY2tlci5jdXJyZW50V2lkZ2V0O1xuICAgICAgaWYgKCF3aWRnZXQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY29uc3QgcGF0aCA9IHdpZGdldC5jb250ZXh0LnBhdGg7XG4gICAgICByZXR1cm4gY29tbWFuZHMuZXhlY3V0ZSgnZG9jbWFuYWdlcjpvcGVuJywge1xuICAgICAgICBwYXRoLFxuICAgICAgICBmYWN0b3J5OiAnRWRpdG9yJyxcbiAgICAgICAgb3B0aW9uczoge1xuICAgICAgICAgIG1vZGU6ICdzcGxpdC1yaWdodCdcbiAgICAgICAgfVxuICAgICAgfSk7XG4gICAgfSxcbiAgICBpc1Zpc2libGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IHdpZGdldCA9IHRyYWNrZXIuY3VycmVudFdpZGdldDtcbiAgICAgIHJldHVybiAoXG4gICAgICAgICh3aWRnZXQgJiYgUGF0aEV4dC5leHRuYW1lKHdpZGdldC5jb250ZXh0LnBhdGgpID09PSAnLm1kJykgfHwgZmFsc2VcbiAgICAgICk7XG4gICAgfSxcbiAgICBsYWJlbDogdHJhbnMuX18oJ1Nob3cgTWFya2Rvd24gRWRpdG9yJylcbiAgfSk7XG5cbiAgaWYgKHRvY1JlZ2lzdHJ5KSB7XG4gICAgdG9jUmVnaXN0cnkuYWRkKFxuICAgICAgbmV3IE1hcmtkb3duVmlld2VyVGFibGVPZkNvbnRlbnRzRmFjdG9yeShcbiAgICAgICAgdHJhY2tlcixcbiAgICAgICAgcmVuZGVybWltZS5tYXJrZG93blBhcnNlclxuICAgICAgKVxuICAgICk7XG4gIH1cblxuICByZXR1cm4gdHJhY2tlcjtcbn1cblxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbiBhcyBkZWZhdWx0LlxuICovXG5leHBvcnQgZGVmYXVsdCBwbHVnaW47XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=