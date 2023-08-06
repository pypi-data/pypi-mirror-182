"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_rendermime-extension_lib_index_js"],{

/***/ "../../packages/rendermime-extension/lib/index.js":
/*!********************************************************!*\
  !*** ../../packages/rendermime-extension/lib/index.js ***!
  \********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/docmanager */ "webpack/sharing/consume/default/@jupyterlab/docmanager/@jupyterlab/docmanager");
/* harmony import */ var _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module rendermime-extension
 */




var CommandIDs;
(function (CommandIDs) {
    CommandIDs.handleLink = 'rendermime:handle-local-link';
})(CommandIDs || (CommandIDs = {}));
/**
 * A plugin providing a rendermime registry.
 */
const plugin = {
    id: '@jupyterlab/rendermime-extension:plugin',
    optional: [
        _jupyterlab_docmanager__WEBPACK_IMPORTED_MODULE_1__.IDocumentManager,
        _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.ILatexTypesetter,
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ISanitizer,
        _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.IMarkdownParser,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.ITranslator
    ],
    provides: _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.IRenderMimeRegistry,
    activate: activate,
    autoStart: true
};
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * Activate the rendermine plugin.
 */
function activate(app, docManager, latexTypesetter, sanitizer, markdownParser, translator) {
    const trans = (translator !== null && translator !== void 0 ? translator : _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.nullTranslator).load('jupyterlab');
    if (docManager) {
        app.commands.addCommand(CommandIDs.handleLink, {
            label: trans.__('Handle Local Link'),
            execute: args => {
                const path = args['path'];
                const id = args['id'];
                if (!path) {
                    return;
                }
                // First check if the path exists on the server.
                return docManager.services.contents
                    .get(path, { content: false })
                    .then(() => {
                    // Open the link with the default rendered widget factory,
                    // if applicable.
                    const factory = docManager.registry.defaultRenderedWidgetFactory(path);
                    const widget = docManager.openOrReveal(path, factory.name);
                    // Handle the hash if one has been provided.
                    if (widget && id) {
                        widget.setFragment(id);
                    }
                });
            }
        });
    }
    return new _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.RenderMimeRegistry({
        initialFactories: _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_2__.standardRendererFactories,
        linkHandler: !docManager
            ? undefined
            : {
                handleLink: (node, path, id) => {
                    // If node has the download attribute explicitly set, use the
                    // default browser downloading behavior.
                    if (node.tagName === 'A' && node.hasAttribute('download')) {
                        return;
                    }
                    app.commandLinker.connectNode(node, CommandIDs.handleLink, {
                        path,
                        id
                    });
                }
            },
        latexTypesetter: latexTypesetter !== null && latexTypesetter !== void 0 ? latexTypesetter : undefined,
        markdownParser: markdownParser !== null && markdownParser !== void 0 ? markdownParser : undefined,
        translator: translator !== null && translator !== void 0 ? translator : undefined,
        sanitizer: sanitizer !== null && sanitizer !== void 0 ? sanitizer : undefined
    });
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfcmVuZGVybWltZS1leHRlbnNpb25fbGliX2luZGV4X2pzLjk5N2IxNDY1MGEyZjk5ZmFhOGIyLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7OztBQUFBOzs7K0VBRytFO0FBQy9FOzs7R0FHRztBQU0rQztBQUNRO0FBTzFCO0FBQ3NDO0FBRXRFLElBQVUsVUFBVSxDQUVuQjtBQUZELFdBQVUsVUFBVTtJQUNMLHFCQUFVLEdBQUcsOEJBQThCLENBQUM7QUFDM0QsQ0FBQyxFQUZTLFVBQVUsS0FBVixVQUFVLFFBRW5CO0FBRUQ7O0dBRUc7QUFDSCxNQUFNLE1BQU0sR0FBK0M7SUFDekQsRUFBRSxFQUFFLHlDQUF5QztJQUM3QyxRQUFRLEVBQUU7UUFDUixvRUFBZ0I7UUFDaEIsb0VBQWdCO1FBQ2hCLDREQUFVO1FBQ1YsbUVBQWU7UUFDZixnRUFBVztLQUNaO0lBQ0QsUUFBUSxFQUFFLHVFQUFtQjtJQUM3QixRQUFRLEVBQUUsUUFBUTtJQUNsQixTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUY7O0dBRUc7QUFDSCxpRUFBZSxNQUFNLEVBQUM7QUFFdEI7O0dBRUc7QUFDSCxTQUFTLFFBQVEsQ0FDZixHQUFvQixFQUNwQixVQUFtQyxFQUNuQyxlQUF3QyxFQUN4QyxTQUE0QixFQUM1QixjQUFzQyxFQUN0QyxVQUE4QjtJQUU5QixNQUFNLEtBQUssR0FBRyxDQUFDLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLG1FQUFjLENBQUMsQ0FBQyxJQUFJLENBQUMsWUFBWSxDQUFDLENBQUM7SUFDaEUsSUFBSSxVQUFVLEVBQUU7UUFDZCxHQUFHLENBQUMsUUFBUSxDQUFDLFVBQVUsQ0FBQyxVQUFVLENBQUMsVUFBVSxFQUFFO1lBQzdDLEtBQUssRUFBRSxLQUFLLENBQUMsRUFBRSxDQUFDLG1CQUFtQixDQUFDO1lBQ3BDLE9BQU8sRUFBRSxJQUFJLENBQUMsRUFBRTtnQkFDZCxNQUFNLElBQUksR0FBRyxJQUFJLENBQUMsTUFBTSxDQUE4QixDQUFDO2dCQUN2RCxNQUFNLEVBQUUsR0FBRyxJQUFJLENBQUMsSUFBSSxDQUE4QixDQUFDO2dCQUNuRCxJQUFJLENBQUMsSUFBSSxFQUFFO29CQUNULE9BQU87aUJBQ1I7Z0JBQ0QsZ0RBQWdEO2dCQUNoRCxPQUFPLFVBQVUsQ0FBQyxRQUFRLENBQUMsUUFBUTtxQkFDaEMsR0FBRyxDQUFDLElBQUksRUFBRSxFQUFFLE9BQU8sRUFBRSxLQUFLLEVBQUUsQ0FBQztxQkFDN0IsSUFBSSxDQUFDLEdBQUcsRUFBRTtvQkFDVCwwREFBMEQ7b0JBQzFELGlCQUFpQjtvQkFDakIsTUFBTSxPQUFPLEdBQ1gsVUFBVSxDQUFDLFFBQVEsQ0FBQyw0QkFBNEIsQ0FBQyxJQUFJLENBQUMsQ0FBQztvQkFDekQsTUFBTSxNQUFNLEdBQUcsVUFBVSxDQUFDLFlBQVksQ0FBQyxJQUFJLEVBQUUsT0FBTyxDQUFDLElBQUksQ0FBQyxDQUFDO29CQUUzRCw0Q0FBNEM7b0JBQzVDLElBQUksTUFBTSxJQUFJLEVBQUUsRUFBRTt3QkFDaEIsTUFBTSxDQUFDLFdBQVcsQ0FBQyxFQUFFLENBQUMsQ0FBQztxQkFDeEI7Z0JBQ0gsQ0FBQyxDQUFDLENBQUM7WUFDUCxDQUFDO1NBQ0YsQ0FBQyxDQUFDO0tBQ0o7SUFDRCxPQUFPLElBQUksc0VBQWtCLENBQUM7UUFDNUIsZ0JBQWdCLEVBQUUsNkVBQXlCO1FBQzNDLFdBQVcsRUFBRSxDQUFDLFVBQVU7WUFDdEIsQ0FBQyxDQUFDLFNBQVM7WUFDWCxDQUFDLENBQUM7Z0JBQ0UsVUFBVSxFQUFFLENBQUMsSUFBaUIsRUFBRSxJQUFZLEVBQUUsRUFBVyxFQUFFLEVBQUU7b0JBQzNELDZEQUE2RDtvQkFDN0Qsd0NBQXdDO29CQUN4QyxJQUFJLElBQUksQ0FBQyxPQUFPLEtBQUssR0FBRyxJQUFJLElBQUksQ0FBQyxZQUFZLENBQUMsVUFBVSxDQUFDLEVBQUU7d0JBQ3pELE9BQU87cUJBQ1I7b0JBQ0QsR0FBRyxDQUFDLGFBQWEsQ0FBQyxXQUFXLENBQUMsSUFBSSxFQUFFLFVBQVUsQ0FBQyxVQUFVLEVBQUU7d0JBQ3pELElBQUk7d0JBQ0osRUFBRTtxQkFDSCxDQUFDLENBQUM7Z0JBQ0wsQ0FBQzthQUNGO1FBQ0wsZUFBZSxFQUFFLGVBQWUsYUFBZixlQUFlLGNBQWYsZUFBZSxHQUFJLFNBQVM7UUFDN0MsY0FBYyxFQUFFLGNBQWMsYUFBZCxjQUFjLGNBQWQsY0FBYyxHQUFJLFNBQVM7UUFDM0MsVUFBVSxFQUFFLFVBQVUsYUFBVixVQUFVLGNBQVYsVUFBVSxHQUFJLFNBQVM7UUFDbkMsU0FBUyxFQUFFLFNBQVMsYUFBVCxTQUFTLGNBQVQsU0FBUyxHQUFJLFNBQVM7S0FDbEMsQ0FBQyxDQUFDO0FBQ0wsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9yZW5kZXJtaW1lLWV4dGVuc2lvbi9zcmMvaW5kZXgudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSByZW5kZXJtaW1lLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7IElTYW5pdGl6ZXIgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJRG9jdW1lbnRNYW5hZ2VyIH0gZnJvbSAnQGp1cHl0ZXJsYWIvZG9jbWFuYWdlcic7XG5pbXBvcnQge1xuICBJTGF0ZXhUeXBlc2V0dGVyLFxuICBJTWFya2Rvd25QYXJzZXIsXG4gIElSZW5kZXJNaW1lUmVnaXN0cnksXG4gIFJlbmRlck1pbWVSZWdpc3RyeSxcbiAgc3RhbmRhcmRSZW5kZXJlckZhY3Rvcmllc1xufSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lJztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBudWxsVHJhbnNsYXRvciB9IGZyb20gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uJztcblxubmFtZXNwYWNlIENvbW1hbmRJRHMge1xuICBleHBvcnQgY29uc3QgaGFuZGxlTGluayA9ICdyZW5kZXJtaW1lOmhhbmRsZS1sb2NhbC1saW5rJztcbn1cblxuLyoqXG4gKiBBIHBsdWdpbiBwcm92aWRpbmcgYSByZW5kZXJtaW1lIHJlZ2lzdHJ5LlxuICovXG5jb25zdCBwbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJUmVuZGVyTWltZVJlZ2lzdHJ5PiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9yZW5kZXJtaW1lLWV4dGVuc2lvbjpwbHVnaW4nLFxuICBvcHRpb25hbDogW1xuICAgIElEb2N1bWVudE1hbmFnZXIsXG4gICAgSUxhdGV4VHlwZXNldHRlcixcbiAgICBJU2FuaXRpemVyLFxuICAgIElNYXJrZG93blBhcnNlcixcbiAgICBJVHJhbnNsYXRvclxuICBdLFxuICBwcm92aWRlczogSVJlbmRlck1pbWVSZWdpc3RyeSxcbiAgYWN0aXZhdGU6IGFjdGl2YXRlLFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW4gYXMgZGVmYXVsdC5cbiAqL1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2luO1xuXG4vKipcbiAqIEFjdGl2YXRlIHRoZSByZW5kZXJtaW5lIHBsdWdpbi5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBkb2NNYW5hZ2VyOiBJRG9jdW1lbnRNYW5hZ2VyIHwgbnVsbCxcbiAgbGF0ZXhUeXBlc2V0dGVyOiBJTGF0ZXhUeXBlc2V0dGVyIHwgbnVsbCxcbiAgc2FuaXRpemVyOiBJU2FuaXRpemVyIHwgbnVsbCxcbiAgbWFya2Rvd25QYXJzZXI6IElNYXJrZG93blBhcnNlciB8IG51bGwsXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yIHwgbnVsbFxuKTogUmVuZGVyTWltZVJlZ2lzdHJ5IHtcbiAgY29uc3QgdHJhbnMgPSAodHJhbnNsYXRvciA/PyBudWxsVHJhbnNsYXRvcikubG9hZCgnanVweXRlcmxhYicpO1xuICBpZiAoZG9jTWFuYWdlcikge1xuICAgIGFwcC5jb21tYW5kcy5hZGRDb21tYW5kKENvbW1hbmRJRHMuaGFuZGxlTGluaywge1xuICAgICAgbGFiZWw6IHRyYW5zLl9fKCdIYW5kbGUgTG9jYWwgTGluaycpLFxuICAgICAgZXhlY3V0ZTogYXJncyA9PiB7XG4gICAgICAgIGNvbnN0IHBhdGggPSBhcmdzWydwYXRoJ10gYXMgc3RyaW5nIHwgdW5kZWZpbmVkIHwgbnVsbDtcbiAgICAgICAgY29uc3QgaWQgPSBhcmdzWydpZCddIGFzIHN0cmluZyB8IHVuZGVmaW5lZCB8IG51bGw7XG4gICAgICAgIGlmICghcGF0aCkge1xuICAgICAgICAgIHJldHVybjtcbiAgICAgICAgfVxuICAgICAgICAvLyBGaXJzdCBjaGVjayBpZiB0aGUgcGF0aCBleGlzdHMgb24gdGhlIHNlcnZlci5cbiAgICAgICAgcmV0dXJuIGRvY01hbmFnZXIuc2VydmljZXMuY29udGVudHNcbiAgICAgICAgICAuZ2V0KHBhdGgsIHsgY29udGVudDogZmFsc2UgfSlcbiAgICAgICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgICAgICAvLyBPcGVuIHRoZSBsaW5rIHdpdGggdGhlIGRlZmF1bHQgcmVuZGVyZWQgd2lkZ2V0IGZhY3RvcnksXG4gICAgICAgICAgICAvLyBpZiBhcHBsaWNhYmxlLlxuICAgICAgICAgICAgY29uc3QgZmFjdG9yeSA9XG4gICAgICAgICAgICAgIGRvY01hbmFnZXIucmVnaXN0cnkuZGVmYXVsdFJlbmRlcmVkV2lkZ2V0RmFjdG9yeShwYXRoKTtcbiAgICAgICAgICAgIGNvbnN0IHdpZGdldCA9IGRvY01hbmFnZXIub3Blbk9yUmV2ZWFsKHBhdGgsIGZhY3RvcnkubmFtZSk7XG5cbiAgICAgICAgICAgIC8vIEhhbmRsZSB0aGUgaGFzaCBpZiBvbmUgaGFzIGJlZW4gcHJvdmlkZWQuXG4gICAgICAgICAgICBpZiAod2lkZ2V0ICYmIGlkKSB7XG4gICAgICAgICAgICAgIHdpZGdldC5zZXRGcmFnbWVudChpZCk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG4gIH1cbiAgcmV0dXJuIG5ldyBSZW5kZXJNaW1lUmVnaXN0cnkoe1xuICAgIGluaXRpYWxGYWN0b3JpZXM6IHN0YW5kYXJkUmVuZGVyZXJGYWN0b3JpZXMsXG4gICAgbGlua0hhbmRsZXI6ICFkb2NNYW5hZ2VyXG4gICAgICA/IHVuZGVmaW5lZFxuICAgICAgOiB7XG4gICAgICAgICAgaGFuZGxlTGluazogKG5vZGU6IEhUTUxFbGVtZW50LCBwYXRoOiBzdHJpbmcsIGlkPzogc3RyaW5nKSA9PiB7XG4gICAgICAgICAgICAvLyBJZiBub2RlIGhhcyB0aGUgZG93bmxvYWQgYXR0cmlidXRlIGV4cGxpY2l0bHkgc2V0LCB1c2UgdGhlXG4gICAgICAgICAgICAvLyBkZWZhdWx0IGJyb3dzZXIgZG93bmxvYWRpbmcgYmVoYXZpb3IuXG4gICAgICAgICAgICBpZiAobm9kZS50YWdOYW1lID09PSAnQScgJiYgbm9kZS5oYXNBdHRyaWJ1dGUoJ2Rvd25sb2FkJykpIHtcbiAgICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgYXBwLmNvbW1hbmRMaW5rZXIuY29ubmVjdE5vZGUobm9kZSwgQ29tbWFuZElEcy5oYW5kbGVMaW5rLCB7XG4gICAgICAgICAgICAgIHBhdGgsXG4gICAgICAgICAgICAgIGlkXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICB9XG4gICAgICAgIH0sXG4gICAgbGF0ZXhUeXBlc2V0dGVyOiBsYXRleFR5cGVzZXR0ZXIgPz8gdW5kZWZpbmVkLFxuICAgIG1hcmtkb3duUGFyc2VyOiBtYXJrZG93blBhcnNlciA/PyB1bmRlZmluZWQsXG4gICAgdHJhbnNsYXRvcjogdHJhbnNsYXRvciA/PyB1bmRlZmluZWQsXG4gICAgc2FuaXRpemVyOiBzYW5pdGl6ZXIgPz8gdW5kZWZpbmVkXG4gIH0pO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9