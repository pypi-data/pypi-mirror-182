"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_vdom-extension_lib_index_js-_bf380"],{

/***/ "../../packages/vdom-extension/lib/index.js":
/*!**************************************************!*\
  !*** ../../packages/vdom-extension/lib/index.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MIME_TYPE": () => (/* binding */ MIME_TYPE),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/vdom */ "webpack/sharing/consume/default/@jupyterlab/vdom/@jupyterlab/vdom");
/* harmony import */ var _jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module vdom-extension
 */








/**
 * The MIME type for VDOM.
 */
const MIME_TYPE = 'application/vdom.v1+json';
/**
 * The name of the factory that creates VDOM widgets.
 */
const FACTORY_NAME = 'VDOM';
const plugin = {
    id: '@jupyterlab/vdom-extension:factory',
    requires: [_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_4__.IRenderMimeRegistry],
    optional: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_3__.INotebookTracker, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.ITranslator],
    provides: _jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6__.IVDOMTracker,
    autoStart: true,
    activate: (app, rendermime, notebooks, restorer, translator) => {
        const tracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.WidgetTracker({
            namespace: 'vdom-widget'
        });
        // Add a renderer factory to application rendermime registry.
        rendermime.addFactory({
            safe: false,
            mimeTypes: [MIME_TYPE],
            createRenderer: options => new _jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6__.RenderedVDOM(options)
        }, 0);
        if (notebooks) {
            notebooks.widgetAdded.connect((sender, panel) => {
                // Get the notebook's context and rendermime;
                const { context, content: { rendermime } } = panel;
                // Add the renderer factory to the notebook's rendermime registry;
                rendermime.addFactory({
                    safe: false,
                    mimeTypes: [MIME_TYPE],
                    createRenderer: options => new _jupyterlab_vdom__WEBPACK_IMPORTED_MODULE_6__.RenderedVDOM(options, context)
                }, 0);
            });
        }
        app.docRegistry.addFileType({
            name: 'vdom',
            mimeTypes: [MIME_TYPE],
            extensions: ['.vdom', '.vdom.json'],
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_5__.reactIcon
        });
        const trans = (translator || _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_7__.nullTranslator).load('jupyterlab');
        const factory = new _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.MimeDocumentFactory({
            renderTimeout: 1000,
            dataType: 'json',
            rendermime,
            name: FACTORY_NAME,
            label: trans.__('VDOM'),
            primaryFileType: app.docRegistry.getFileType('vdom'),
            fileTypes: ['vdom', 'json'],
            defaultFor: ['vdom']
        });
        factory.widgetCreated.connect((sender, widget) => {
            widget.context.pathChanged.connect(() => {
                void tracker.save(widget);
            });
            void tracker.add(widget);
        });
        // Add widget factory to document registry.
        app.docRegistry.addWidgetFactory(factory);
        if (restorer) {
            // Handle state restoration.
            void restorer.restore(tracker, {
                command: 'docmanager:open',
                args: widget => ({
                    path: widget.context.path,
                    factory: FACTORY_NAME
                }),
                name: widget => widget.context.path
            });
        }
        return tracker;
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdmRvbS1leHRlbnNpb25fbGliX2luZGV4X2pzLV9iZjM4MC44YzNhNjczMWIwYTU4NDQ5OGRkNC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQU04QjtBQUNvQjtBQUN1QjtBQUNwQjtBQUNLO0FBQ1A7QUFDUTtBQUNRO0FBRXRFOztHQUVHO0FBQ0ksTUFBTSxTQUFTLEdBQUcsMEJBQTBCLENBQUM7QUFFcEQ7O0dBRUc7QUFDSCxNQUFNLFlBQVksR0FBRyxNQUFNLENBQUM7QUFFNUIsTUFBTSxNQUFNLEdBQXdDO0lBQ2xELEVBQUUsRUFBRSxvQ0FBb0M7SUFDeEMsUUFBUSxFQUFFLENBQUMsdUVBQW1CLENBQUM7SUFDL0IsUUFBUSxFQUFFLENBQUMsa0VBQWdCLEVBQUUsb0VBQWUsRUFBRSxnRUFBVyxDQUFDO0lBQzFELFFBQVEsRUFBRSwwREFBWTtJQUN0QixTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLFVBQStCLEVBQy9CLFNBQWtDLEVBQ2xDLFFBQWdDLEVBQ2hDLFVBQThCLEVBQzlCLEVBQUU7UUFDRixNQUFNLE9BQU8sR0FBRyxJQUFJLCtEQUFhLENBQWU7WUFDOUMsU0FBUyxFQUFFLGFBQWE7U0FDekIsQ0FBQyxDQUFDO1FBRUgsNkRBQTZEO1FBQzdELFVBQVUsQ0FBQyxVQUFVLENBQ25CO1lBQ0UsSUFBSSxFQUFFLEtBQUs7WUFDWCxTQUFTLEVBQUUsQ0FBQyxTQUFTLENBQUM7WUFDdEIsY0FBYyxFQUFFLE9BQU8sQ0FBQyxFQUFFLENBQUMsSUFBSSwwREFBWSxDQUFDLE9BQU8sQ0FBQztTQUNyRCxFQUNELENBQUMsQ0FDRixDQUFDO1FBRUYsSUFBSSxTQUFTLEVBQUU7WUFDYixTQUFTLENBQUMsV0FBVyxDQUFDLE9BQU8sQ0FBQyxDQUFDLE1BQU0sRUFBRSxLQUFLLEVBQUUsRUFBRTtnQkFDOUMsNkNBQTZDO2dCQUM3QyxNQUFNLEVBQ0osT0FBTyxFQUNQLE9BQU8sRUFBRSxFQUFFLFVBQVUsRUFBRSxFQUN4QixHQUFHLEtBQUssQ0FBQztnQkFFVixrRUFBa0U7Z0JBQ2xFLFVBQVUsQ0FBQyxVQUFVLENBQ25CO29CQUNFLElBQUksRUFBRSxLQUFLO29CQUNYLFNBQVMsRUFBRSxDQUFDLFNBQVMsQ0FBQztvQkFDdEIsY0FBYyxFQUFFLE9BQU8sQ0FBQyxFQUFFLENBQUMsSUFBSSwwREFBWSxDQUFDLE9BQU8sRUFBRSxPQUFPLENBQUM7aUJBQzlELEVBQ0QsQ0FBQyxDQUNGLENBQUM7WUFDSixDQUFDLENBQUMsQ0FBQztTQUNKO1FBRUQsR0FBRyxDQUFDLFdBQVcsQ0FBQyxXQUFXLENBQUM7WUFDMUIsSUFBSSxFQUFFLE1BQU07WUFDWixTQUFTLEVBQUUsQ0FBQyxTQUFTLENBQUM7WUFDdEIsVUFBVSxFQUFFLENBQUMsT0FBTyxFQUFFLFlBQVksQ0FBQztZQUNuQyxJQUFJLEVBQUUsZ0VBQVM7U0FDaEIsQ0FBQyxDQUFDO1FBRUgsTUFBTSxLQUFLLEdBQUcsQ0FBQyxVQUFVLElBQUksbUVBQWMsQ0FBQyxDQUFDLElBQUksQ0FBQyxZQUFZLENBQUMsQ0FBQztRQUVoRSxNQUFNLE9BQU8sR0FBRyxJQUFJLHdFQUFtQixDQUFDO1lBQ3RDLGFBQWEsRUFBRSxJQUFJO1lBQ25CLFFBQVEsRUFBRSxNQUFNO1lBQ2hCLFVBQVU7WUFDVixJQUFJLEVBQUUsWUFBWTtZQUNsQixLQUFLLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxNQUFNLENBQUM7WUFDdkIsZUFBZSxFQUFFLEdBQUcsQ0FBQyxXQUFXLENBQUMsV0FBVyxDQUFDLE1BQU0sQ0FBRTtZQUNyRCxTQUFTLEVBQUUsQ0FBQyxNQUFNLEVBQUUsTUFBTSxDQUFDO1lBQzNCLFVBQVUsRUFBRSxDQUFDLE1BQU0sQ0FBQztTQUNyQixDQUFDLENBQUM7UUFFSCxPQUFPLENBQUMsYUFBYSxDQUFDLE9BQU8sQ0FBQyxDQUFDLE1BQU0sRUFBRSxNQUFNLEVBQUUsRUFBRTtZQUMvQyxNQUFNLENBQUMsT0FBTyxDQUFDLFdBQVcsQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFO2dCQUN0QyxLQUFLLE9BQU8sQ0FBQyxJQUFJLENBQUMsTUFBTSxDQUFDLENBQUM7WUFDNUIsQ0FBQyxDQUFDLENBQUM7WUFDSCxLQUFLLE9BQU8sQ0FBQyxHQUFHLENBQUMsTUFBTSxDQUFDLENBQUM7UUFDM0IsQ0FBQyxDQUFDLENBQUM7UUFFSCwyQ0FBMkM7UUFDM0MsR0FBRyxDQUFDLFdBQVcsQ0FBQyxnQkFBZ0IsQ0FBQyxPQUFPLENBQUMsQ0FBQztRQUUxQyxJQUFJLFFBQVEsRUFBRTtZQUNaLDRCQUE0QjtZQUM1QixLQUFLLFFBQVEsQ0FBQyxPQUFPLENBQUMsT0FBTyxFQUFFO2dCQUM3QixPQUFPLEVBQUUsaUJBQWlCO2dCQUMxQixJQUFJLEVBQUUsTUFBTSxDQUFDLEVBQUUsQ0FBQyxDQUFDO29CQUNmLElBQUksRUFBRSxNQUFNLENBQUMsT0FBTyxDQUFDLElBQUk7b0JBQ3pCLE9BQU8sRUFBRSxZQUFZO2lCQUN0QixDQUFDO2dCQUNGLElBQUksRUFBRSxNQUFNLENBQUMsRUFBRSxDQUFDLE1BQU0sQ0FBQyxPQUFPLENBQUMsSUFBSTthQUNwQyxDQUFDLENBQUM7U0FDSjtRQUVELE9BQU8sT0FBTyxDQUFDO0lBQ2pCLENBQUM7Q0FDRixDQUFDO0FBRUYsaUVBQWUsTUFBTSxFQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3Zkb20tZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB2ZG9tLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIElMYXlvdXRSZXN0b3JlcixcbiAgSnVweXRlckZyb250RW5kLFxuICBKdXB5dGVyRnJvbnRFbmRQbHVnaW5cbn0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24nO1xuaW1wb3J0IHsgV2lkZ2V0VHJhY2tlciB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcbmltcG9ydCB7IE1pbWVEb2N1bWVudCwgTWltZURvY3VtZW50RmFjdG9yeSB9IGZyb20gJ0BqdXB5dGVybGFiL2RvY3JlZ2lzdHJ5JztcbmltcG9ydCB7IElOb3RlYm9va1RyYWNrZXIgfSBmcm9tICdAanVweXRlcmxhYi9ub3RlYm9vayc7XG5pbXBvcnQgeyBJUmVuZGVyTWltZVJlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvcmVuZGVybWltZSc7XG5pbXBvcnQgeyByZWFjdEljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IElWRE9NVHJhY2tlciwgUmVuZGVyZWRWRE9NIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdmRvbSc7XG5pbXBvcnQgeyBJVHJhbnNsYXRvciwgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5cbi8qKlxuICogVGhlIE1JTUUgdHlwZSBmb3IgVkRPTS5cbiAqL1xuZXhwb3J0IGNvbnN0IE1JTUVfVFlQRSA9ICdhcHBsaWNhdGlvbi92ZG9tLnYxK2pzb24nO1xuXG4vKipcbiAqIFRoZSBuYW1lIG9mIHRoZSBmYWN0b3J5IHRoYXQgY3JlYXRlcyBWRE9NIHdpZGdldHMuXG4gKi9cbmNvbnN0IEZBQ1RPUllfTkFNRSA9ICdWRE9NJztcblxuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVZET01UcmFja2VyPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi92ZG9tLWV4dGVuc2lvbjpmYWN0b3J5JyxcbiAgcmVxdWlyZXM6IFtJUmVuZGVyTWltZVJlZ2lzdHJ5XSxcbiAgb3B0aW9uYWw6IFtJTm90ZWJvb2tUcmFja2VyLCBJTGF5b3V0UmVzdG9yZXIsIElUcmFuc2xhdG9yXSxcbiAgcHJvdmlkZXM6IElWRE9NVHJhY2tlcixcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHJlbmRlcm1pbWU6IElSZW5kZXJNaW1lUmVnaXN0cnksXG4gICAgbm90ZWJvb2tzOiBJTm90ZWJvb2tUcmFja2VyIHwgbnVsbCxcbiAgICByZXN0b3JlcjogSUxheW91dFJlc3RvcmVyIHwgbnVsbCxcbiAgICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvciB8IG51bGxcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhY2tlciA9IG5ldyBXaWRnZXRUcmFja2VyPE1pbWVEb2N1bWVudD4oe1xuICAgICAgbmFtZXNwYWNlOiAndmRvbS13aWRnZXQnXG4gICAgfSk7XG5cbiAgICAvLyBBZGQgYSByZW5kZXJlciBmYWN0b3J5IHRvIGFwcGxpY2F0aW9uIHJlbmRlcm1pbWUgcmVnaXN0cnkuXG4gICAgcmVuZGVybWltZS5hZGRGYWN0b3J5KFxuICAgICAge1xuICAgICAgICBzYWZlOiBmYWxzZSxcbiAgICAgICAgbWltZVR5cGVzOiBbTUlNRV9UWVBFXSxcbiAgICAgICAgY3JlYXRlUmVuZGVyZXI6IG9wdGlvbnMgPT4gbmV3IFJlbmRlcmVkVkRPTShvcHRpb25zKVxuICAgICAgfSxcbiAgICAgIDBcbiAgICApO1xuXG4gICAgaWYgKG5vdGVib29rcykge1xuICAgICAgbm90ZWJvb2tzLndpZGdldEFkZGVkLmNvbm5lY3QoKHNlbmRlciwgcGFuZWwpID0+IHtcbiAgICAgICAgLy8gR2V0IHRoZSBub3RlYm9vaydzIGNvbnRleHQgYW5kIHJlbmRlcm1pbWU7XG4gICAgICAgIGNvbnN0IHtcbiAgICAgICAgICBjb250ZXh0LFxuICAgICAgICAgIGNvbnRlbnQ6IHsgcmVuZGVybWltZSB9XG4gICAgICAgIH0gPSBwYW5lbDtcblxuICAgICAgICAvLyBBZGQgdGhlIHJlbmRlcmVyIGZhY3RvcnkgdG8gdGhlIG5vdGVib29rJ3MgcmVuZGVybWltZSByZWdpc3RyeTtcbiAgICAgICAgcmVuZGVybWltZS5hZGRGYWN0b3J5KFxuICAgICAgICAgIHtcbiAgICAgICAgICAgIHNhZmU6IGZhbHNlLFxuICAgICAgICAgICAgbWltZVR5cGVzOiBbTUlNRV9UWVBFXSxcbiAgICAgICAgICAgIGNyZWF0ZVJlbmRlcmVyOiBvcHRpb25zID0+IG5ldyBSZW5kZXJlZFZET00ob3B0aW9ucywgY29udGV4dClcbiAgICAgICAgICB9LFxuICAgICAgICAgIDBcbiAgICAgICAgKTtcbiAgICAgIH0pO1xuICAgIH1cblxuICAgIGFwcC5kb2NSZWdpc3RyeS5hZGRGaWxlVHlwZSh7XG4gICAgICBuYW1lOiAndmRvbScsXG4gICAgICBtaW1lVHlwZXM6IFtNSU1FX1RZUEVdLFxuICAgICAgZXh0ZW5zaW9uczogWycudmRvbScsICcudmRvbS5qc29uJ10sXG4gICAgICBpY29uOiByZWFjdEljb25cbiAgICB9KTtcblxuICAgIGNvbnN0IHRyYW5zID0gKHRyYW5zbGF0b3IgfHwgbnVsbFRyYW5zbGF0b3IpLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGNvbnN0IGZhY3RvcnkgPSBuZXcgTWltZURvY3VtZW50RmFjdG9yeSh7XG4gICAgICByZW5kZXJUaW1lb3V0OiAxMDAwLFxuICAgICAgZGF0YVR5cGU6ICdqc29uJyxcbiAgICAgIHJlbmRlcm1pbWUsXG4gICAgICBuYW1lOiBGQUNUT1JZX05BTUUsXG4gICAgICBsYWJlbDogdHJhbnMuX18oJ1ZET00nKSxcbiAgICAgIHByaW1hcnlGaWxlVHlwZTogYXBwLmRvY1JlZ2lzdHJ5LmdldEZpbGVUeXBlKCd2ZG9tJykhLFxuICAgICAgZmlsZVR5cGVzOiBbJ3Zkb20nLCAnanNvbiddLFxuICAgICAgZGVmYXVsdEZvcjogWyd2ZG9tJ11cbiAgICB9KTtcblxuICAgIGZhY3Rvcnkud2lkZ2V0Q3JlYXRlZC5jb25uZWN0KChzZW5kZXIsIHdpZGdldCkgPT4ge1xuICAgICAgd2lkZ2V0LmNvbnRleHQucGF0aENoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICAgIHZvaWQgdHJhY2tlci5zYXZlKHdpZGdldCk7XG4gICAgICB9KTtcbiAgICAgIHZvaWQgdHJhY2tlci5hZGQod2lkZ2V0KTtcbiAgICB9KTtcblxuICAgIC8vIEFkZCB3aWRnZXQgZmFjdG9yeSB0byBkb2N1bWVudCByZWdpc3RyeS5cbiAgICBhcHAuZG9jUmVnaXN0cnkuYWRkV2lkZ2V0RmFjdG9yeShmYWN0b3J5KTtcblxuICAgIGlmIChyZXN0b3Jlcikge1xuICAgICAgLy8gSGFuZGxlIHN0YXRlIHJlc3RvcmF0aW9uLlxuICAgICAgdm9pZCByZXN0b3Jlci5yZXN0b3JlKHRyYWNrZXIsIHtcbiAgICAgICAgY29tbWFuZDogJ2RvY21hbmFnZXI6b3BlbicsXG4gICAgICAgIGFyZ3M6IHdpZGdldCA9PiAoe1xuICAgICAgICAgIHBhdGg6IHdpZGdldC5jb250ZXh0LnBhdGgsXG4gICAgICAgICAgZmFjdG9yeTogRkFDVE9SWV9OQU1FXG4gICAgICAgIH0pLFxuICAgICAgICBuYW1lOiB3aWRnZXQgPT4gd2lkZ2V0LmNvbnRleHQucGF0aFxuICAgICAgfSk7XG4gICAgfVxuXG4gICAgcmV0dXJuIHRyYWNrZXI7XG4gIH1cbn07XG5cbmV4cG9ydCBkZWZhdWx0IHBsdWdpbjtcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==