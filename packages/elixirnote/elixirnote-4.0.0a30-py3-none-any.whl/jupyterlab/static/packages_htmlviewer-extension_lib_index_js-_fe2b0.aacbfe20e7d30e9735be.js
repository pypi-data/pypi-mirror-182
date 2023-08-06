"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_htmlviewer-extension_lib_index_js-_fe2b0"],{

/***/ "../../packages/htmlviewer-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/htmlviewer-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/htmlviewer */ "webpack/sharing/consume/default/@jupyterlab/htmlviewer/@jupyterlab/htmlviewer");
/* harmony import */ var _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module htmlviewer-extension
 */






const HTML_VIEWER_PLUGIN_ID = '@jupyterlab/htmlviewer-extension:plugin';
/**
 * Factory name
 */
const FACTORY = 'HTML Viewer';
/**
 * Command IDs used by the plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.trustHTML = 'htmlviewer:trust-html';
})(CommandIDs || (CommandIDs = {}));
/**
 * The HTML file handler extension.
 */
const htmlPlugin = {
    activate: activateHTMLViewer,
    id: HTML_VIEWER_PLUGIN_ID,
    provides: _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__.IHTMLViewerTracker,
    requires: [_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    optional: [
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer,
        _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IToolbarWidgetRegistry
    ],
    autoStart: true
};
/**
 * Activate the HTMLViewer extension.
 */
function activateHTMLViewer(app, translator, palette, restorer, settingRegistry, toolbarRegistry) {
    let toolbarFactory;
    const trans = translator.load('jupyterlab');
    if (toolbarRegistry) {
        toolbarRegistry.addFactory(FACTORY, 'refresh', widget => _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__.ToolbarItems.createRefreshButton(widget, translator));
        toolbarRegistry.addFactory(FACTORY, 'trust', widget => _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__.ToolbarItems.createTrustButton(widget, translator));
        if (settingRegistry) {
            toolbarFactory = (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.createToolbarFactory)(toolbarRegistry, settingRegistry, FACTORY, htmlPlugin.id, translator);
        }
    }
    // Add an HTML file type to the docregistry.
    const ft = {
        name: 'html',
        contentType: 'file',
        fileFormat: 'text',
        displayName: trans.__('HTML File'),
        extensions: ['.html'],
        mimeTypes: ['text/html'],
        icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.html5Icon
    };
    app.docRegistry.addFileType(ft);
    // Create a new viewer factory.
    const factory = new _jupyterlab_htmlviewer__WEBPACK_IMPORTED_MODULE_2__.HTMLViewerFactory({
        name: FACTORY,
        label: trans.__('HTML Viewer'),
        fileTypes: ['html'],
        defaultFor: ['html'],
        readOnly: true,
        toolbarFactory,
        translator
    });
    // Create a widget tracker for HTML documents.
    const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
        namespace: 'htmlviewer'
    });
    // Handle state restoration.
    if (restorer) {
        void restorer.restore(tracker, {
            command: 'docmanager:open',
            args: widget => ({ path: widget.context.path, factory: 'HTML Viewer' }),
            name: widget => widget.context.path
        });
    }
    let trustByDefault = false;
    if (settingRegistry) {
        const loadSettings = settingRegistry.load(HTML_VIEWER_PLUGIN_ID);
        const updateSettings = (settings) => {
            trustByDefault = settings.get('trustByDefault').composite;
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
    app.docRegistry.addWidgetFactory(factory);
    factory.widgetCreated.connect((sender, widget) => {
        var _a, _b;
        // Track the widget.
        void tracker.add(widget);
        // Notify the widget tracker if restore data needs to update.
        widget.context.pathChanged.connect(() => {
            void tracker.save(widget);
        });
        // Notify the application when the trust state changes so it
        // can update any renderings of the trust command.
        widget.trustedChanged.connect(() => {
            app.commands.notifyCommandChanged(CommandIDs.trustHTML);
        });
        widget.trusted = trustByDefault;
        widget.title.icon = ft.icon;
        widget.title.iconClass = (_a = ft.iconClass) !== null && _a !== void 0 ? _a : '';
        widget.title.iconLabel = (_b = ft.iconLabel) !== null && _b !== void 0 ? _b : '';
    });
    // Add a command to trust the active HTML document,
    // allowing script executions in its context.
    app.commands.addCommand(CommandIDs.trustHTML, {
        label: trans.__('Trust HTML File'),
        caption: trans.__(`Whether the HTML file is trusted.
    Trusting the file allows scripts to run in it,
    which may result in security risks.
    Only enable for files you trust.`),
        isEnabled: () => !!tracker.currentWidget,
        isToggled: () => {
            const current = tracker.currentWidget;
            if (!current) {
                return false;
            }
            const sandbox = current.content.sandbox;
            return sandbox.indexOf('allow-scripts') !== -1;
        },
        execute: () => {
            const current = tracker.currentWidget;
            if (!current) {
                return;
            }
            current.trusted = !current.trusted;
        }
    });
    if (palette) {
        palette.addItem({
            command: CommandIDs.trustHTML,
            category: trans.__('File Operations')
        });
    }
    return tracker;
}
/**
 * Export the plugins as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (htmlPlugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfaHRtbHZpZXdlci1leHRlbnNpb25fbGliX2luZGV4X2pzLV9mZTJiMC5hYWNiZmUyMGU3ZDMwZTk3MzViZS5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7OzsrRUFHK0U7QUFDL0U7OztHQUdHO0FBTThCO0FBTUg7QUFPRTtBQUUrQjtBQUNUO0FBQ0E7QUFFdEQsTUFBTSxxQkFBcUIsR0FBRyx5Q0FBeUMsQ0FBQztBQUV4RTs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFHLGFBQWEsQ0FBQztBQUU5Qjs7R0FFRztBQUNILElBQVUsVUFBVSxDQUVuQjtBQUZELFdBQVUsVUFBVTtJQUNMLG9CQUFTLEdBQUcsdUJBQXVCLENBQUM7QUFDbkQsQ0FBQyxFQUZTLFVBQVUsS0FBVixVQUFVLFFBRW5CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLFVBQVUsR0FBOEM7SUFDNUQsUUFBUSxFQUFFLGtCQUFrQjtJQUM1QixFQUFFLEVBQUUscUJBQXFCO0lBQ3pCLFFBQVEsRUFBRSxzRUFBa0I7SUFDNUIsUUFBUSxFQUFFLENBQUMsZ0VBQVcsQ0FBQztJQUN2QixRQUFRLEVBQUU7UUFDUixpRUFBZTtRQUNmLG9FQUFlO1FBQ2YseUVBQWdCO1FBQ2hCLHdFQUFzQjtLQUN2QjtJQUNELFNBQVMsRUFBRSxJQUFJO0NBQ2hCLENBQUM7QUFFRjs7R0FFRztBQUNILFNBQVMsa0JBQWtCLENBQ3pCLEdBQW9CLEVBQ3BCLFVBQXVCLEVBQ3ZCLE9BQStCLEVBQy9CLFFBQWdDLEVBQ2hDLGVBQXdDLEVBQ3hDLGVBQThDO0lBRTlDLElBQUksY0FFUyxDQUFDO0lBQ2QsTUFBTSxLQUFLLEdBQUcsVUFBVSxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztJQUU1QyxJQUFJLGVBQWUsRUFBRTtRQUNuQixlQUFlLENBQUMsVUFBVSxDQUFhLE9BQU8sRUFBRSxTQUFTLEVBQUUsTUFBTSxDQUFDLEVBQUUsQ0FDbEUsb0ZBQWdDLENBQUMsTUFBTSxFQUFF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YUFBYTtRQUN4QyxTQUFTLEVBQUUsR0FBRyxFQUFFO1lBQ2QsTUFBTSxPQUFPLEdBQUcsT0FBTyxDQUFDLGFBQWEsQ0FBQztZQUN0QyxJQUFJLENBQUMsT0FBTyxFQUFFO2dCQUNaLE9BQU8sS0FBSyxDQUFDO2FBQ2Q7WUFDRCxNQUFNLE9BQU8sR0FBRyxPQUFPLENBQUMsT0FBTyxDQUFDLE9BQU8sQ0FBQztZQUN4QyxPQUFPLE9BQU8sQ0FBQyxPQUFPLENBQUMsZUFBZSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7UUFDakQsQ0FBQztRQUNELE9BQU8sRUFBRSxHQUFHLEVBQUU7WUFDWixNQUFNLE9BQU8sR0FBRyxPQUFPLENBQUMsYUFBYSxDQUFDO1lBQ3RDLElBQUksQ0FBQyxPQUFPLEVBQUU7Z0JBQ1osT0FBTzthQUNSO1lBQ0QsT0FBTyxDQUFDLE9BQU8sR0FBRyxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUM7UUFDckMsQ0FBQztLQUNGLENBQUMsQ0FBQztJQUNILElBQUksT0FBTyxFQUFFO1FBQ1gsT0FBTyxDQUFDLE9BQU8sQ0FBQztZQUNkLE9BQU8sRUFBRSxVQUFVLENBQUMsU0FBUztZQUM3QixRQUFRLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxpQkFBaUIsQ0FBQztTQUN0QyxDQUFDLENBQUM7S0FDSjtJQUVELE9BQU8sT0FBTyxDQUFDO0FBQ2pCLENBQUM7QUFDRDs7R0FFRztBQUNILGlFQUFlLFVBQVUsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9odG1sdmlld2VyLWV4dGVuc2lvbi9zcmMvaW5kZXgudHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgaHRtbHZpZXdlci1leHRlbnNpb25cbiAqL1xuXG5pbXBvcnQge1xuICBJTGF5b3V0UmVzdG9yZXIsXG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIGNyZWF0ZVRvb2xiYXJGYWN0b3J5LFxuICBJQ29tbWFuZFBhbGV0dGUsXG4gIElUb29sYmFyV2lkZ2V0UmVnaXN0cnksXG4gIFdpZGdldFRyYWNrZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuaW1wb3J0IHsgRG9jdW1lbnRSZWdpc3RyeSB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7XG4gIEhUTUxWaWV3ZXIsXG4gIEhUTUxWaWV3ZXJGYWN0b3J5LFxuICBJSFRNTFZpZXdlclRyYWNrZXIsXG4gIFRvb2xiYXJJdGVtc1xufSBmcm9tICdAanVweXRlcmxhYi9odG1sdmlld2VyJztcbmltcG9ydCB7IElPYnNlcnZhYmxlTGlzdCB9IGZyb20gJ0BqdXB5dGVybGFiL29ic2VydmFibGVzJztcbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBodG1sNUljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcblxuY29uc3QgSFRNTF9WSUVXRVJfUExVR0lOX0lEID0gJ0BqdXB5dGVybGFiL2h0bWx2aWV3ZXItZXh0ZW5zaW9uOnBsdWdpbic7XG5cbi8qKlxuICogRmFjdG9yeSBuYW1lXG4gKi9cbmNvbnN0IEZBQ1RPUlkgPSAnSFRNTCBWaWV3ZXInO1xuXG4vKipcbiAqIENvbW1hbmQgSURzIHVzZWQgYnkgdGhlIHBsdWdpbi5cbiAqL1xubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgdHJ1c3RIVE1MID0gJ2h0bWx2aWV3ZXI6dHJ1c3QtaHRtbCc7XG59XG5cbi8qKlxuICogVGhlIEhUTUwgZmlsZSBoYW5kbGVyIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgaHRtbFBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPElIVE1MVmlld2VyVHJhY2tlcj4gPSB7XG4gIGFjdGl2YXRlOiBhY3RpdmF0ZUhUTUxWaWV3ZXIsXG4gIGlkOiBIVE1MX1ZJRVdFUl9QTFVHSU5fSUQsXG4gIHByb3ZpZGVzOiBJSFRNTFZpZXdlclRyYWNrZXIsXG4gIHJlcXVpcmVzOiBbSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW1xuICAgIElDb21tYW5kUGFsZXR0ZSxcbiAgICBJTGF5b3V0UmVzdG9yZXIsXG4gICAgSVNldHRpbmdSZWdpc3RyeSxcbiAgICBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5XG4gIF0sXG4gIGF1dG9TdGFydDogdHJ1ZVxufTtcblxuLyoqXG4gKiBBY3RpdmF0ZSB0aGUgSFRNTFZpZXdlciBleHRlbnNpb24uXG4gKi9cbmZ1bmN0aW9uIGFjdGl2YXRlSFRNTFZpZXdlcihcbiAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICBwYWxldHRlOiBJQ29tbWFuZFBhbGV0dGUgfCBudWxsLFxuICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgc2V0dGluZ1JlZ2lzdHJ5OiBJU2V0dGluZ1JlZ2lzdHJ5IHwgbnVsbCxcbiAgdG9vbGJhclJlZ2lzdHJ5OiBJVG9vbGJhcldpZGdldFJlZ2lzdHJ5IHwgbnVsbFxuKTogSUhUTUxWaWV3ZXJUcmFja2VyIHtcbiAgbGV0IHRvb2xiYXJGYWN0b3J5OlxuICAgIHwgKCh3aWRnZXQ6IEhUTUxWaWV3ZXIpID0+IElPYnNlcnZhYmxlTGlzdDxEb2N1bWVudFJlZ2lzdHJ5LklUb29sYmFySXRlbT4pXG4gICAgfCB1bmRlZmluZWQ7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG5cbiAgaWYgKHRvb2xiYXJSZWdpc3RyeSkge1xuICAgIHRvb2xiYXJSZWdpc3RyeS5hZGRGYWN0b3J5PEhUTUxWaWV3ZXI+KEZBQ1RPUlksICdyZWZyZXNoJywgd2lkZ2V0ID0+XG4gICAgICBUb29sYmFySXRlbXMuY3JlYXRlUmVmcmVzaEJ1dHRvbih3aWRnZXQsIHRyYW5zbGF0b3IpXG4gICAgKTtcbiAgICB0b29sYmFyUmVnaXN0cnkuYWRkRmFjdG9yeTxIVE1MVmlld2VyPihGQUNUT1JZLCAndHJ1c3QnLCB3aWRnZXQgPT5cbiAgICAgIFRvb2xiYXJJdGVtcy5jcmVhdGVUcnVzdEJ1dHRvbih3aWRnZXQsIHRyYW5zbGF0b3IpXG4gICAgKTtcblxuICAgIGlmIChzZXR0aW5nUmVnaXN0cnkpIHtcbiAgICAgIHRvb2xiYXJGYWN0b3J5ID0gY3JlYXRlVG9vbGJhckZhY3RvcnkoXG4gICAgICAgIHRvb2xiYXJSZWdpc3RyeSxcbiAgICAgICAgc2V0dGluZ1JlZ2lzdHJ5LFxuICAgICAgICBGQUNUT1JZLFxuICAgICAgICBodG1sUGx1Z2luLmlkLFxuICAgICAgICB0cmFuc2xhdG9yXG4gICAgICApO1xuICAgIH1cbiAgfVxuXG4gIC8vIEFkZCBhbiBIVE1MIGZpbGUgdHlwZSB0byB0aGUgZG9jcmVnaXN0cnkuXG4gIGNvbnN0IGZ0OiBEb2N1bWVudFJlZ2lzdHJ5LklGaWxlVHlwZSA9IHtcbiAgICBuYW1lOiAnaHRtbCcsXG4gICAgY29udGVudFR5cGU6ICdmaWxlJyxcbiAgICBmaWxlRm9ybWF0OiAndGV4dCcsXG4gICAgZGlzcGxheU5hbWU6IHRyYW5zLl9fKCdIVE1MIEZpbGUnKSxcbiAgICBleHRlbnNpb25zOiBbJy5odG1sJ10sXG4gICAgbWltZVR5cGVzOiBbJ3RleHQvaHRtbCddLFxuICAgIGljb246IGh0bWw1SWNvblxuICB9O1xuICBhcHAuZG9jUmVnaXN0cnkuYWRkRmlsZVR5cGUoZnQpO1xuXG4gIC8vIENyZWF0ZSBhIG5ldyB2aWV3ZXIgZmFjdG9yeS5cbiAgY29uc3QgZmFjdG9yeSA9IG5ldyBIVE1MVmlld2VyRmFjdG9yeSh7XG4gICAgbmFtZTogRkFDVE9SWSxcbiAgICBsYWJlbDogdHJhbnMuX18oJ0hUTUwgVmlld2VyJyksXG4gICAgZmlsZVR5cGVzOiBbJ2h0bWwnXSxcbiAgICBkZWZhdWx0Rm9yOiBbJ2h0bWwnXSxcbiAgICByZWFkT25seTogdHJ1ZSxcbiAgICB0b29sYmFyRmFjdG9yeSxcbiAgICB0cmFuc2xhdG9yXG4gIH0pO1xuXG4gIC8vIENyZWF0ZSBhIHdpZGdldCB0cmFja2VyIGZvciBIVE1MIGRvY3VtZW50cy5cbiAgY29uc3QgdHJhY2tlciA9IG5ldyBXaWRnZXRUcmFja2VyPEhUTUxWaWV3ZXI+KHtcbiAgICBuYW1lc3BhY2U6ICdodG1sdmlld2VyJ1xuICB9KTtcblxuICAvLyBIYW5kbGUgc3RhdGUgcmVzdG9yYXRpb24uXG4gIGlmIChyZXN0b3Jlcikge1xuICAgIHZvaWQgcmVzdG9yZXIucmVzdG9yZSh0cmFja2VyLCB7XG4gICAgICBjb21tYW5kOiAnZG9jbWFuYWdlcjpvcGVuJyxcbiAgICAgIGFyZ3M6IHdpZGdldCA9PiAoeyBwYXRoOiB3aWRnZXQuY29udGV4dC5wYXRoLCBmYWN0b3J5OiAnSFRNTCBWaWV3ZXInIH0pLFxuICAgICAgbmFtZTogd2lkZ2V0ID0+IHdpZGdldC5jb250ZXh0LnBhdGhcbiAgICB9KTtcbiAgfVxuXG4gIGxldCB0cnVzdEJ5RGVmYXVsdCA9IGZhbHNlO1xuXG4gIGlmIChzZXR0aW5nUmVnaXN0cnkpIHtcbiAgICBjb25zdCBsb2FkU2V0dGluZ3MgPSBzZXR0aW5nUmVnaXN0cnkubG9hZChIVE1MX1ZJRVdFUl9QTFVHSU5fSUQpO1xuICAgIGNvbnN0IHVwZGF0ZVNldHRpbmdzID0gKHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyk6IHZvaWQgPT4ge1xuICAgICAgdHJ1c3RCeURlZmF1bHQgPSBzZXR0aW5ncy5nZXQoJ3RydXN0QnlEZWZhdWx0JykuY29tcG9zaXRlIGFzIGJvb2xlYW47XG4gICAgfTtcblxuICAgIFByb21pc2UuYWxsKFtsb2FkU2V0dGluZ3MsIGFwcC5yZXN0b3JlZF0pXG4gICAgICAudGhlbigoW3NldHRpbmdzXSkgPT4ge1xuICAgICAgICB1cGRhdGVTZXR0aW5ncyhzZXR0aW5ncyk7XG4gICAgICAgIHNldHRpbmdzLmNoYW5nZWQuY29ubmVjdChzZXR0aW5ncyA9PiB7XG4gICAgICAgICAgdXBkYXRlU2V0dGluZ3Moc2V0dGluZ3MpO1xuICAgICAgICB9KTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgICAgY29uc29sZS5lcnJvcihyZWFzb24ubWVzc2FnZSk7XG4gICAgICB9KTtcbiAgfVxuXG4gIGFwcC5kb2NSZWdpc3RyeS5hZGRXaWRnZXRGYWN0b3J5KGZhY3RvcnkpO1xuICBmYWN0b3J5LndpZGdldENyZWF0ZWQuY29ubmVjdCgoc2VuZGVyLCB3aWRnZXQpID0+IHtcbiAgICAvLyBUcmFjayB0aGUgd2lkZ2V0LlxuICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICAvLyBOb3RpZnkgdGhlIHdpZGdldCB0cmFja2VyIGlmIHJlc3RvcmUgZGF0YSBuZWVkcyB0byB1cGRhdGUuXG4gICAgd2lkZ2V0LmNvbnRleHQucGF0aENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICB2b2lkIHRyYWNrZXIuc2F2ZSh3aWRnZXQpO1xuICAgIH0pO1xuICAgIC8vIE5vdGlmeSB0aGUgYXBwbGljYXRpb24gd2hlbiB0aGUgdHJ1c3Qgc3RhdGUgY2hhbmdlcyBzbyBpdFxuICAgIC8vIGNhbiB1cGRhdGUgYW55IHJlbmRlcmluZ3Mgb2YgdGhlIHRydXN0IGNvbW1hbmQuXG4gICAgd2lkZ2V0LnRydXN0ZWRDaGFuZ2VkLmNvbm5lY3QoKCkgPT4ge1xuICAgICAgYXBwLmNvbW1hbmRzLm5vdGlmeUNvbW1hbmRDaGFuZ2VkKENvbW1hbmRJRHMudHJ1c3RIVE1MKTtcbiAgICB9KTtcblxuICAgIHdpZGdldC50cnVzdGVkID0gdHJ1c3RCeURlZmF1bHQ7XG5cbiAgICB3aWRnZXQudGl0bGUuaWNvbiA9IGZ0Lmljb24hO1xuICAgIHdpZGdldC50aXRsZS5pY29uQ2xhc3MgPSBmdC5pY29uQ2xhc3MgPz8gJyc7XG4gICAgd2lkZ2V0LnRpdGxlLmljb25MYWJlbCA9IGZ0Lmljb25MYWJlbCA/PyAnJztcbiAgfSk7XG5cbiAgLy8gQWRkIGEgY29tbWFuZCB0byB0cnVzdCB0aGUgYWN0aXZlIEhUTUwgZG9jdW1lbnQsXG4gIC8vIGFsbG93aW5nIHNjcmlwdCBleGVjdXRpb25zIGluIGl0cyBjb250ZXh0LlxuICBhcHAuY29tbWFuZHMuYWRkQ29tbWFuZChDb21tYW5kSURzLnRydXN0SFRNTCwge1xuICAgIGxhYmVsOiB0cmFucy5fXygnVHJ1c3QgSFRNTCBGaWxlJyksXG4gICAgY2FwdGlvbjogdHJhbnMuX18oYFdoZXRoZXIgdGhlIEhUTUwgZmlsZSBpcyB0cnVzdGVkLlxuICAgIFRydXN0aW5nIHRoZSBmaWxlIGFsbG93cyBzY3JpcHRzIHRvIHJ1biBpbiBpdCxcbiAgICB3aGljaCBtYXkgcmVzdWx0IGluIHNlY3VyaXR5IHJpc2tzLlxuICAgIE9ubHkgZW5hYmxlIGZvciBmaWxlcyB5b3UgdHJ1c3QuYCksXG4gICAgaXNFbmFibGVkOiAoKSA9PiAhIXRyYWNrZXIuY3VycmVudFdpZGdldCxcbiAgICBpc1RvZ2dsZWQ6ICgpID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICBpZiAoIWN1cnJlbnQpIHtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgICAgY29uc3Qgc2FuZGJveCA9IGN1cnJlbnQuY29udGVudC5zYW5kYm94O1xuICAgICAgcmV0dXJuIHNhbmRib3guaW5kZXhPZignYWxsb3ctc2NyaXB0cycpICE9PSAtMTtcbiAgICB9LFxuICAgIGV4ZWN1dGU6ICgpID0+IHtcbiAgICAgIGNvbnN0IGN1cnJlbnQgPSB0cmFja2VyLmN1cnJlbnRXaWRnZXQ7XG4gICAgICBpZiAoIWN1cnJlbnQpIHtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgICAgY3VycmVudC50cnVzdGVkID0gIWN1cnJlbnQudHJ1c3RlZDtcbiAgICB9XG4gIH0pO1xuICBpZiAocGFsZXR0ZSkge1xuICAgIHBhbGV0dGUuYWRkSXRlbSh7XG4gICAgICBjb21tYW5kOiBDb21tYW5kSURzLnRydXN0SFRNTCxcbiAgICAgIGNhdGVnb3J5OiB0cmFucy5fXygnRmlsZSBPcGVyYXRpb25zJylcbiAgICB9KTtcbiAgfVxuXG4gIHJldHVybiB0cmFja2VyO1xufVxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbnMgYXMgZGVmYXVsdC5cbiAqL1xuZXhwb3J0IGRlZmF1bHQgaHRtbFBsdWdpbjtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==