"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_completer-extension_lib_index_js"],{

/***/ "../../packages/completer-extension/lib/index.js":
/*!*******************************************************!*\
  !*** ../../packages/completer-extension/lib/index.js ***!
  \*******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/completer */ "webpack/sharing/consume/default/@jupyterlab/completer/@jupyterlab/completer");
/* harmony import */ var _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _renderer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./renderer */ "../../packages/completer-extension/lib/renderer.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module completer-extension
 */




const COMPLETION_MANAGER_PLUGIN = '@jupyterlab/completer-extension:tracker';
const defaultProvider = {
    id: '@jupyterlab/completer-extension:base-service',
    requires: [_jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.ICompletionProviderManager],
    autoStart: true,
    activate: (app, completionManager) => {
        completionManager.registerProvider(new _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.ContextCompleterProvider());
        completionManager.registerProvider(new _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.KernelCompleterProvider());
    }
};
const manager = {
    id: COMPLETION_MANAGER_PLUGIN,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry],
    optional: [_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.IFormComponentRegistry],
    provides: _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.ICompletionProviderManager,
    autoStart: true,
    activate: (app, settings, editorRegistry) => {
        const AVAILABLE_PROVIDERS = 'availableProviders';
        const PROVIDER_TIMEOUT = 'providerTimeout';
        const SHOW_DOCUMENT_PANEL = 'showDocumentationPanel';
        const CONTINUOUS_HINTING = 'autoCompletion';
        const manager = new _jupyterlab_completer__WEBPACK_IMPORTED_MODULE_0__.CompletionProviderManager();
        const updateSetting = (settingValues, availableProviders) => {
            var _a;
            const providersData = settingValues.get(AVAILABLE_PROVIDERS);
            const timeout = settingValues.get(PROVIDER_TIMEOUT);
            const showDoc = settingValues.get(SHOW_DOCUMENT_PANEL);
            const continuousHinting = settingValues.get(CONTINUOUS_HINTING);
            manager.setTimeout(timeout.composite);
            manager.setShowDocumentFlag(showDoc.composite);
            manager.setContinuousHinting(continuousHinting.composite);
            const selectedProviders = (_a = providersData.user) !== null && _a !== void 0 ? _a : providersData.composite;
            const sortedProviders = Object.entries(selectedProviders !== null && selectedProviders !== void 0 ? selectedProviders : {})
                .filter(val => val[1] >= 0 && availableProviders.includes(val[0]))
                .sort(([, rank1], [, rank2]) => rank2 - rank1)
                .map(item => item[0]);
            manager.activateProvider(sortedProviders);
        };
        app.restored
            .then(() => {
            const availableProviders = [...manager.getProviders().keys()];
            settings.transform(COMPLETION_MANAGER_PLUGIN, {
                fetch: plugin => {
                    const schema = plugin.schema.properties;
                    const defaultValue = {};
                    availableProviders.forEach((item, index) => {
                        defaultValue[item] = (index + 1) * 100;
                    });
                    schema[AVAILABLE_PROVIDERS]['default'] = defaultValue;
                    return plugin;
                }
            });
            const settingsPromise = settings.load(COMPLETION_MANAGER_PLUGIN);
            settingsPromise
                .then(settingValues => {
                updateSetting(settingValues, availableProviders);
                settingValues.changed.connect(newSettings => {
                    updateSetting(newSettings, availableProviders);
                });
            })
                .catch(console.error);
        })
            .catch(console.error);
        if (editorRegistry) {
            editorRegistry.addRenderer('availableProviders', (props) => {
                return (0,_renderer__WEBPACK_IMPORTED_MODULE_3__.renderAvailableProviders)(props);
            });
        }
        return manager;
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [manager, defaultProvider];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "../../packages/completer-extension/lib/renderer.js":
/*!**********************************************************!*\
  !*** ../../packages/completer-extension/lib/renderer.js ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "renderAvailableProviders": () => (/* binding */ renderAvailableProviders)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

const AVAILABLE_PROVIDERS = 'availableProviders';
/**
 * Custom setting renderer for provider rank.
 */
function renderAvailableProviders(props) {
    const { schema } = props;
    const title = schema.title;
    const desc = schema.description;
    const settings = props.formContext.settings;
    const userData = settings.get(AVAILABLE_PROVIDERS).user;
    const items = Object.assign({}, schema.default);
    if (userData) {
        for (const key of Object.keys(items)) {
            if (key in userData) {
                items[key] = userData[key];
            }
            else {
                items[key] = -1;
            }
        }
    }
    const [settingValue, setValue] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(items);
    const onSettingChange = (key, e) => {
        const newValue = Object.assign(Object.assign({}, settingValue), { [key]: parseInt(e.target.value) });
        settings.set(AVAILABLE_PROVIDERS, newValue).catch(console.error);
        setValue(newValue);
    };
    return (
    //TODO Remove hard coded class names
    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("fieldset", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("legend", null, title),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: "field-description" }, desc),
            Object.keys(items).map(key => {
                return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { key: key, className: "form-group small-field" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h3", null,
                            " ",
                            key),
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "inputFieldWrapper" },
                            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("input", { className: "form-control", type: "number", value: settingValue[key], onChange: e => {
                                    onSettingChange(key, e);
                                } })))));
            }))));
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29tcGxldGVyLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuNmM4NzJjNDUwM2I2ZTMzNGE5N2IuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQSwwQ0FBMEM7QUFDMUMsMkRBQTJEO0FBQzNEOzs7R0FHRztBQVc0QjtBQUNnQztBQUNJO0FBR2I7QUFFdEQsTUFBTSx5QkFBeUIsR0FBRyx5Q0FBeUMsQ0FBQztBQUU1RSxNQUFNLGVBQWUsR0FBZ0M7SUFDbkQsRUFBRSxFQUFFLDhDQUE4QztJQUNsRCxRQUFRLEVBQUUsQ0FBQyw2RUFBMEIsQ0FBQztJQUN0QyxTQUFTLEVBQUUsSUFBSTtJQUNmLFFBQVEsRUFBRSxDQUNSLEdBQW9CLEVBQ3BCLGlCQUE2QyxFQUN2QyxFQUFFO1FBQ1IsaUJBQWlCLENBQUMsZ0JBQWdCLENBQUMsSUFBSSwyRUFBd0IsRUFBRSxDQUFDLENBQUM7UUFDbkUsaUJBQWlCLENBQUMsZ0JBQWdCLENBQUMsSUFBSSwwRUFBdUIsRUFBRSxDQUFDLENBQUM7SUFDcEUsQ0FBQztDQUNGLENBQUM7QUFFRixNQUFNLE9BQU8sR0FBc0Q7SUFDakUsRUFBRSxFQUFFLHlCQUF5QjtJQUM3QixRQUFRLEVBQUUsQ0FBQyx5RUFBZ0IsQ0FBQztJQUM1QixRQUFRLEVBQUUsQ0FBQyw2RUFBc0IsQ0FBQztJQUNsQyxRQUFRLEVBQUUsNkVBQTBCO0lBQ3BDLFNBQVMsRUFBRSxJQUFJO0lBQ2YsUUFBUSxFQUFFLENBQ1IsR0FBb0IsRUFDcEIsUUFBMEIsRUFDMUIsY0FBNkMsRUFDakIsRUFBRTtRQUM5QixNQUFNLG1CQUFtQixHQUFHLG9CQUFvQixDQUFDO1FBQ2pELE1BQU0sZ0JBQWdCLEdBQUcsaUJBQWlCLENBQUM7UUFDM0MsTUFBTSxtQkFBbUIsR0FBRyx3QkFBd0IsQ0FBQztRQUNyRCxNQUFNLGtCQUFrQixHQUFHLGdCQUFnQixDQUFDO1FBQzVDLE1BQU0sT0FBTyxHQUFHLElBQUksNEVBQXlCLEVBQUUsQ0FBQztRQUNoRCxNQUFNLGFBQWEsR0FBRyxDQUNwQixhQUF5QyxFQUN6QyxrQkFBNEIsRUFDdEIsRUFBRTs7WUFDUixNQUFNLGFBQWEsR0FBRyxhQUFhLENBQUMsR0FBRyxDQUFDLG1CQUFtQixDQUFDLENBQUM7WUFDN0QsTUFBTSxPQUFPLEdBQUcsYUFBYSxDQUFDLEdBQUcsQ0FBQyxnQkFBZ0IsQ0FBQyxDQUFDO1lBQ3BELE1BQU0sT0FBTyxHQUFHLGFBQWEsQ0FBQyxHQUFHLENBQUMsbUJBQW1CLENBQUMsQ0FBQztZQUN2RCxNQUFNLGlCQUFpQixHQUFHLGFBQWEsQ0FBQyxHQUFHLENBQUMsa0JBQWtCLENBQUMsQ0FBQztZQUNoRSxPQUFPLENBQUMsVUFBVSxDQUFDLE9BQU8sQ0FBQyxTQUFtQixDQUFDLENBQUM7WUFDaEQsT0FBTyxDQUFDLG1CQUFtQixDQUFDLE9BQU8sQ0FBQyxTQUFvQixDQUFDLENBQUM7WUFDMUQsT0FBTyxDQUFDLG9CQUFvQixDQUFDLGlCQUFpQixDQUFDLFNBQW9CLENBQUMsQ0FBQztZQUNyRSxNQUFNLGlCQUFpQixHQUFHLG1CQUFhLENBQUMsSUFBSSxtQ0FBSSxhQUFhLENBQUMsU0FBUyxDQUFDO1lBQ3hFLE1BQU0sZUFBZSxHQUFHLE1BQU0sQ0FBQyxPQUFPLENBQUMsaUJBQWlCLGFBQWpCLGlCQUFpQixjQUFqQixpQkFBaUIsR0FBSSxFQUFFLENBQUM7aUJBQzVELE1BQU0sQ0FBQyxHQUFHLENBQUMsRUFBRSxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUMsSUFBSSxDQUFDLElBQUksa0JBQWtCLENBQUMsUUFBUSxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUMsQ0FBQyxDQUFDO2lCQUNqRSxJQUFJLENBQUMsQ0FBQyxDQUFDLEVBQUUsS0FBSyxDQUFDLEVBQUUsQ0FBQyxFQUFFLEtBQUssQ0FBQyxFQUFFLEVBQUUsQ0FBQyxLQUFLLEdBQUcsS0FBSyxDQUFDO2lCQUM3QyxHQUFHLENBQUMsSUFBSSxDQUFDLEVBQUUsQ0FBQyxJQUFJLENBQUMsQ0FBQyxDQUFDLENBQUMsQ0FBQztZQUN4QixPQUFPLENBQUMsZ0JBQWdCLENBQUMsZUFBZSxDQUFDLENBQUM7UUFDNUMsQ0FBQyxDQUFDO1FBRUYsR0FBRyxDQUFDLFFBQVE7YUFDVCxJQUFJLENBQUMsR0FBRyxFQUFFO1lBQ1QsTUFBTSxrQkFBa0IsR0FBRyxDQUFDLEdBQUcsT0FBTyxDQUFDLFlBQVksRUFBRSxDQUFDLElBQUksRUFBRSxDQUFDLENBQUM7WUFDOUQsUUFBUSxDQUFDLFNBQVMsQ0FBQyx5QkFBeUIsRUFBRTtnQkFDNUMsS0FBSyxFQUFFLE1BQU0sQ0FBQyxFQUFFO29CQUNkLE1BQU0sTUFBTSxHQUFHLE1BQU0sQ0FBQyxNQUFNLENBQUMsVUFBVyxDQUFDO29CQUN6QyxNQUFNLFlBQVksR0FBOEIsRUFBRSxDQUFDO29CQUNuRCxrQkFBa0IsQ0FBQyxPQUFPLENBQUMsQ0FBQyxJQUFJLEVBQUUsS0FBSyxFQUFFLEVBQUU7d0JBQ3pDLFlBQVksQ0FBQyxJQUFJLENBQUMsR0FBRyxDQUFDLEtBQUssR0FBRyxDQUFDLENBQUMsR0FBRyxHQUFHLENBQUM7b0JBQ3pDLENBQUMsQ0FBQyxDQUFDO29CQUNILE1BQU0sQ0FBQyxtQkFBbUIsQ0FBQyxDQUFDLFNBQVMsQ0FBQyxHQUFHLFlBQVksQ0FBQztvQkFDdEQsT0FBTyxNQUFNLENBQUM7Z0JBQ2hCLENBQUM7YUFDRixDQUFDLENBQUM7WUFDSCxNQUFNLGVBQWUsR0FBRyxRQUFRLENBQUMsSUFBSSxDQUFDLHlCQUF5QixDQUFDLENBQUM7WUFDakUsZUFBZTtpQkFDWixJQUFJLENBQUMsYUFBYSxDQUFDLEVBQUU7Z0JBQ3BCLGFBQWEsQ0FBQyxhQUFhLEVBQUUsa0JBQWtCLENBQUMsQ0FBQztnQkFDakQsYUFBYSxDQUFDLE9BQU8sQ0FBQyxPQUFPLENBQUMsV0FBVyxDQUFDLEVBQUU7b0JBQzFDLGFBQWEsQ0FBQyxXQUFXLEVBQUUsa0JBQWtCLENBQUMsQ0FBQztnQkFDakQsQ0FBQyxDQUFDLENBQUM7WUFDTCxDQUFDLENBQUM7aUJBQ0QsS0FBSyxDQUFDLE9BQU8sQ0FBQyxLQUFLLENBQUMsQ0FBQztRQUMxQixDQUFDLENBQUM7YUFDRCxLQUFLLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQyxDQUFDO1FBRXhCLElBQUksY0FBYyxFQUFFO1lBQ2xCLGNBQWMsQ0FBQyxXQUFXLENBQUMsb0JBQW9CLEVBQUUsQ0FBQyxLQUFpQixFQUFFLEVBQUU7Z0JBQ3JFLE9BQU8sbUVBQXdCLENBQUMsS0FBSyxDQUFDLENBQUM7WUFDekMsQ0FBQyxDQUFDLENBQUM7U0FDSjtRQUVELE9BQU8sT0FBTyxDQUFDO0lBQ2pCLENBQUM7Q0FDRixDQUFDO0FBRUY7O0dBRUc7QUFDSCxNQUFNLE9BQU8sR0FBaUMsQ0FBQyxPQUFPLEVBQUUsZUFBZSxDQUFDLENBQUM7QUFDekUsaUVBQWUsT0FBTyxFQUFDOzs7Ozs7Ozs7Ozs7Ozs7OztBQ2pIdkI7OztHQUdHO0FBS3FDO0FBRXhDLE1BQU0sbUJBQW1CLEdBQUcsb0JBQW9CLENBQUM7QUFFakQ7O0dBRUc7QUFDSSxTQUFTLHdCQUF3QixDQUFDLEtBQWlCO0lBQ3hELE1BQU0sRUFBRSxNQUFNLEVBQUUsR0FBRyxLQUFLLENBQUM7SUFDekIsTUFBTSxLQUFLLEdBQUcsTUFBTSxDQUFDLEtBQUssQ0FBQztJQUMzQixNQUFNLElBQUksR0FBRyxNQUFNLENBQUMsV0FBVyxDQUFDO0lBQ2hDLE1BQU0sUUFBUSxHQUErQixLQUFLLENBQUMsV0FBVyxDQUFDLFFBQVEsQ0FBQztJQUN4RSxNQUFNLFFBQVEsR0FBRyxRQUFRLENBQUMsR0FBRyxDQUFDLG1CQUFtQixDQUFDLENBQUMsSUFFdEMsQ0FBQztJQUVkLE1BQU0sS0FBSyxxQkFDTCxNQUFNLENBQUMsT0FBcUMsQ0FDakQsQ0FBQztJQUNGLElBQUksUUFBUSxFQUFFO1FBQ1osS0FBSyxNQUFNLEdBQUcsSUFBSSxNQUFNLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxFQUFFO1lBQ3BDLElBQUksR0FBRyxJQUFJLFFBQVEsRUFBRTtnQkFDbkIsS0FBSyxDQUFDLEdBQUcsQ0FBQyxHQUFHLFFBQVEsQ0FBQyxHQUFHLENBQVcsQ0FBQzthQUN0QztpQkFBTTtnQkFDTCxLQUFLLENBQUMsR0FBRyxDQUFDLEdBQUcsQ0FBQyxDQUFDLENBQUM7YUFDakI7U0FDRjtLQUNGO0lBRUQsTUFBTSxDQUFDLFlBQVksRUFBRSxRQUFRLENBQUMsR0FBRywrQ0FBUSxDQUFDLEtBQUssQ0FBQyxDQUFDO0lBQ2pELE1BQU0sZUFBZSxHQUFHLENBQ3RCLEdBQVcsRUFDWCxDQUFzQyxFQUN0QyxFQUFFO1FBQ0YsTUFBTSxRQUFRLG1DQUNULFlBQVksS0FDZixDQUFDLEdBQUcsQ0FBQyxFQUFFLFFBQVEsQ0FBQyxDQUFDLENBQUMsTUFBTSxDQUFDLEtBQUssQ0FBQyxHQUNoQyxDQUFDO1FBRUYsUUFBUSxDQUFDLEdBQUcsQ0FBQyxtQkFBbUIsRUFBRSxRQUFRLENBQUMsQ0FBQyxLQUFLLENBQUMsT0FBTyxDQUFDLEtBQUssQ0FBQyxDQUFDO1FBRWpFLFFBQVEsQ0FBQyxRQUFRLENBQUMsQ0FBQztJQUNyQixDQUFDLENBQUM7SUFDRixPQUFPO0lBQ0wsb0NBQW9DO0lBQ3BDO1FBQ0U7WUFDRSwyRUFBUyxLQUFLLENBQVU7WUFDeEIsa0VBQUcsU0FBUyxFQUFDLG1CQUFtQixJQUFFLElBQUksQ0FBSztZQUMxQyxNQUFNLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxDQUFDLEdBQUcsQ0FBQyxHQUFHLENBQUMsRUFBRTtnQkFDNUIsT0FBTyxDQUNMLG9FQUFLLEdBQUcsRUFBRSxHQUFHLEVBQUUsU0FBUyxFQUFDLHdCQUF3QjtvQkFDL0M7d0JBQ0U7OzRCQUFNLEdBQUcsQ0FBTTt3QkFDZixvRUFBSyxTQUFTLEVBQUMsbUJBQW1COzRCQUNoQyxzRUFDRSxTQUFTLEVBQUMsY0FBYyxFQUN4QixJQUFJLEVBQUMsUUFBUSxFQUNiLEtBQUssRUFBRSxZQUFZLENBQUMsR0FBRyxDQUFDLEVBQ3hCLFFBQVEsRUFBRSxDQUFDLENBQUMsRUFBRTtvQ0FDWixlQUFlLENBQUMsR0FBRyxFQUFFLENBQUMsQ0FBQyxDQUFDO2dDQUMxQixDQUFDLEdBQ0QsQ0FDRSxDQUNGLENBQ0YsQ0FDUCxDQUFDO1lBQ0osQ0FBQyxDQUFDLENBQ08sQ0FDUCxDQUNQLENBQUM7QUFDSixDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvbXBsZXRlci1leHRlbnNpb24vc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb21wbGV0ZXItZXh0ZW5zaW9uL3NyYy9yZW5kZXJlci50c3giXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgY29tcGxldGVyLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIENvbXBsZXRpb25Qcm92aWRlck1hbmFnZXIsXG4gIENvbnRleHRDb21wbGV0ZXJQcm92aWRlcixcbiAgSUNvbXBsZXRpb25Qcm92aWRlck1hbmFnZXIsXG4gIEtlcm5lbENvbXBsZXRlclByb3ZpZGVyXG59IGZyb20gJ0BqdXB5dGVybGFiL2NvbXBsZXRlcic7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElGb3JtQ29tcG9uZW50UmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB0eXBlIHsgRmllbGRQcm9wcyB9IGZyb20gJ0ByanNmL2NvcmUnO1xuXG5pbXBvcnQgeyByZW5kZXJBdmFpbGFibGVQcm92aWRlcnMgfSBmcm9tICcuL3JlbmRlcmVyJztcblxuY29uc3QgQ09NUExFVElPTl9NQU5BR0VSX1BMVUdJTiA9ICdAanVweXRlcmxhYi9jb21wbGV0ZXItZXh0ZW5zaW9uOnRyYWNrZXInO1xuXG5jb25zdCBkZWZhdWx0UHJvdmlkZXI6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6ICdAanVweXRlcmxhYi9jb21wbGV0ZXItZXh0ZW5zaW9uOmJhc2Utc2VydmljZScsXG4gIHJlcXVpcmVzOiBbSUNvbXBsZXRpb25Qcm92aWRlck1hbmFnZXJdLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIGFjdGl2YXRlOiAoXG4gICAgYXBwOiBKdXB5dGVyRnJvbnRFbmQsXG4gICAgY29tcGxldGlvbk1hbmFnZXI6IElDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyXG4gICk6IHZvaWQgPT4ge1xuICAgIGNvbXBsZXRpb25NYW5hZ2VyLnJlZ2lzdGVyUHJvdmlkZXIobmV3IENvbnRleHRDb21wbGV0ZXJQcm92aWRlcigpKTtcbiAgICBjb21wbGV0aW9uTWFuYWdlci5yZWdpc3RlclByb3ZpZGVyKG5ldyBLZXJuZWxDb21wbGV0ZXJQcm92aWRlcigpKTtcbiAgfVxufTtcblxuY29uc3QgbWFuYWdlcjogSnVweXRlckZyb250RW5kUGx1Z2luPElDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyPiA9IHtcbiAgaWQ6IENPTVBMRVRJT05fTUFOQUdFUl9QTFVHSU4sXG4gIHJlcXVpcmVzOiBbSVNldHRpbmdSZWdpc3RyeV0sXG4gIG9wdGlvbmFsOiBbSUZvcm1Db21wb25lbnRSZWdpc3RyeV0sXG4gIHByb3ZpZGVzOiBJQ29tcGxldGlvblByb3ZpZGVyTWFuYWdlcixcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIGVkaXRvclJlZ2lzdHJ5OiBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5IHwgbnVsbFxuICApOiBJQ29tcGxldGlvblByb3ZpZGVyTWFuYWdlciA9PiB7XG4gICAgY29uc3QgQVZBSUxBQkxFX1BST1ZJREVSUyA9ICdhdmFpbGFibGVQcm92aWRlcnMnO1xuICAgIGNvbnN0IFBST1ZJREVSX1RJTUVPVVQgPSAncHJvdmlkZXJUaW1lb3V0JztcbiAgICBjb25zdCBTSE9XX0RPQ1VNRU5UX1BBTkVMID0gJ3Nob3dEb2N1bWVudGF0aW9uUGFuZWwnO1xuICAgIGNvbnN0IENPTlRJTlVPVVNfSElOVElORyA9ICdhdXRvQ29tcGxldGlvbic7XG4gICAgY29uc3QgbWFuYWdlciA9IG5ldyBDb21wbGV0aW9uUHJvdmlkZXJNYW5hZ2VyKCk7XG4gICAgY29uc3QgdXBkYXRlU2V0dGluZyA9IChcbiAgICAgIHNldHRpbmdWYWx1ZXM6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzLFxuICAgICAgYXZhaWxhYmxlUHJvdmlkZXJzOiBzdHJpbmdbXVxuICAgICk6IHZvaWQgPT4ge1xuICAgICAgY29uc3QgcHJvdmlkZXJzRGF0YSA9IHNldHRpbmdWYWx1ZXMuZ2V0KEFWQUlMQUJMRV9QUk9WSURFUlMpO1xuICAgICAgY29uc3QgdGltZW91dCA9IHNldHRpbmdWYWx1ZXMuZ2V0KFBST1ZJREVSX1RJTUVPVVQpO1xuICAgICAgY29uc3Qgc2hvd0RvYyA9IHNldHRpbmdWYWx1ZXMuZ2V0KFNIT1dfRE9DVU1FTlRfUEFORUwpO1xuICAgICAgY29uc3QgY29udGludW91c0hpbnRpbmcgPSBzZXR0aW5nVmFsdWVzLmdldChDT05USU5VT1VTX0hJTlRJTkcpO1xuICAgICAgbWFuYWdlci5zZXRUaW1lb3V0KHRpbWVvdXQuY29tcG9zaXRlIGFzIG51bWJlcik7XG4gICAgICBtYW5hZ2VyLnNldFNob3dEb2N1bWVudEZsYWcoc2hvd0RvYy5jb21wb3NpdGUgYXMgYm9vbGVhbik7XG4gICAgICBtYW5hZ2VyLnNldENvbnRpbnVvdXNIaW50aW5nKGNvbnRpbnVvdXNIaW50aW5nLmNvbXBvc2l0ZSBhcyBib29sZWFuKTtcbiAgICAgIGNvbnN0IHNlbGVjdGVkUHJvdmlkZXJzID0gcHJvdmlkZXJzRGF0YS51c2VyID8/IHByb3ZpZGVyc0RhdGEuY29tcG9zaXRlO1xuICAgICAgY29uc3Qgc29ydGVkUHJvdmlkZXJzID0gT2JqZWN0LmVudHJpZXMoc2VsZWN0ZWRQcm92aWRlcnMgPz8ge30pXG4gICAgICAgIC5maWx0ZXIodmFsID0+IHZhbFsxXSA+PSAwICYmIGF2YWlsYWJsZVByb3ZpZGVycy5pbmNsdWRlcyh2YWxbMF0pKVxuICAgICAgICAuc29ydCgoWywgcmFuazFdLCBbLCByYW5rMl0pID0+IHJhbmsyIC0gcmFuazEpXG4gICAgICAgIC5tYXAoaXRlbSA9PiBpdGVtWzBdKTtcbiAgICAgIG1hbmFnZXIuYWN0aXZhdGVQcm92aWRlcihzb3J0ZWRQcm92aWRlcnMpO1xuICAgIH07XG5cbiAgICBhcHAucmVzdG9yZWRcbiAgICAgIC50aGVuKCgpID0+IHtcbiAgICAgICAgY29uc3QgYXZhaWxhYmxlUHJvdmlkZXJzID0gWy4uLm1hbmFnZXIuZ2V0UHJvdmlkZXJzKCkua2V5cygpXTtcbiAgICAgICAgc2V0dGluZ3MudHJhbnNmb3JtKENPTVBMRVRJT05fTUFOQUdFUl9QTFVHSU4sIHtcbiAgICAgICAgICBmZXRjaDogcGx1Z2luID0+IHtcbiAgICAgICAgICAgIGNvbnN0IHNjaGVtYSA9IHBsdWdpbi5zY2hlbWEucHJvcGVydGllcyE7XG4gICAgICAgICAgICBjb25zdCBkZWZhdWx0VmFsdWU6IHsgW2tleTogc3RyaW5nXTogbnVtYmVyIH0gPSB7fTtcbiAgICAgICAgICAgIGF2YWlsYWJsZVByb3ZpZGVycy5mb3JFYWNoKChpdGVtLCBpbmRleCkgPT4ge1xuICAgICAgICAgICAgICBkZWZhdWx0VmFsdWVbaXRlbV0gPSAoaW5kZXggKyAxKSAqIDEwMDtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgc2NoZW1hW0FWQUlMQUJMRV9QUk9WSURFUlNdWydkZWZhdWx0J10gPSBkZWZhdWx0VmFsdWU7XG4gICAgICAgICAgICByZXR1cm4gcGx1Z2luO1xuICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgICAgIGNvbnN0IHNldHRpbmdzUHJvbWlzZSA9IHNldHRpbmdzLmxvYWQoQ09NUExFVElPTl9NQU5BR0VSX1BMVUdJTik7XG4gICAgICAgIHNldHRpbmdzUHJvbWlzZVxuICAgICAgICAgIC50aGVuKHNldHRpbmdWYWx1ZXMgPT4ge1xuICAgICAgICAgICAgdXBkYXRlU2V0dGluZyhzZXR0aW5nVmFsdWVzLCBhdmFpbGFibGVQcm92aWRlcnMpO1xuICAgICAgICAgICAgc2V0dGluZ1ZhbHVlcy5jaGFuZ2VkLmNvbm5lY3QobmV3U2V0dGluZ3MgPT4ge1xuICAgICAgICAgICAgICB1cGRhdGVTZXR0aW5nKG5ld1NldHRpbmdzLCBhdmFpbGFibGVQcm92aWRlcnMpO1xuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgfSlcbiAgICAgICAgICAuY2F0Y2goY29uc29sZS5lcnJvcik7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKGNvbnNvbGUuZXJyb3IpO1xuXG4gICAgaWYgKGVkaXRvclJlZ2lzdHJ5KSB7XG4gICAgICBlZGl0b3JSZWdpc3RyeS5hZGRSZW5kZXJlcignYXZhaWxhYmxlUHJvdmlkZXJzJywgKHByb3BzOiBGaWVsZFByb3BzKSA9PiB7XG4gICAgICAgIHJldHVybiByZW5kZXJBdmFpbGFibGVQcm92aWRlcnMocHJvcHMpO1xuICAgICAgfSk7XG4gICAgfVxuXG4gICAgcmV0dXJuIG1hbmFnZXI7XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbbWFuYWdlciwgZGVmYXVsdFByb3ZpZGVyXTtcbmV4cG9ydCBkZWZhdWx0IHBsdWdpbnM7XG4iLCIvKlxuICogQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4gKiBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuICovXG5cbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdCB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB0eXBlIHsgRmllbGRQcm9wcyB9IGZyb20gJ0ByanNmL2NvcmUnO1xuaW1wb3J0IFJlYWN0LCB7IHVzZVN0YXRlIH0gZnJvbSAncmVhY3QnO1xuXG5jb25zdCBBVkFJTEFCTEVfUFJPVklERVJTID0gJ2F2YWlsYWJsZVByb3ZpZGVycyc7XG5cbi8qKlxuICogQ3VzdG9tIHNldHRpbmcgcmVuZGVyZXIgZm9yIHByb3ZpZGVyIHJhbmsuXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiByZW5kZXJBdmFpbGFibGVQcm92aWRlcnMocHJvcHM6IEZpZWxkUHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGNvbnN0IHsgc2NoZW1hIH0gPSBwcm9wcztcbiAgY29uc3QgdGl0bGUgPSBzY2hlbWEudGl0bGU7XG4gIGNvbnN0IGRlc2MgPSBzY2hlbWEuZGVzY3JpcHRpb247XG4gIGNvbnN0IHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyA9IHByb3BzLmZvcm1Db250ZXh0LnNldHRpbmdzO1xuICBjb25zdCB1c2VyRGF0YSA9IHNldHRpbmdzLmdldChBVkFJTEFCTEVfUFJPVklERVJTKS51c2VyIGFzXG4gICAgfCBSZWFkb25seVBhcnRpYWxKU09OT2JqZWN0XG4gICAgfCB1bmRlZmluZWQ7XG5cbiAgY29uc3QgaXRlbXMgPSB7XG4gICAgLi4uKHNjaGVtYS5kZWZhdWx0IGFzIHsgW2tleTogc3RyaW5nXTogbnVtYmVyIH0pXG4gIH07XG4gIGlmICh1c2VyRGF0YSkge1xuICAgIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKGl0ZW1zKSkge1xuICAgICAgaWYgKGtleSBpbiB1c2VyRGF0YSkge1xuICAgICAgICBpdGVtc1trZXldID0gdXNlckRhdGFba2V5XSBhcyBudW1iZXI7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBpdGVtc1trZXldID0gLTE7XG4gICAgICB9XG4gICAgfVxuICB9XG5cbiAgY29uc3QgW3NldHRpbmdWYWx1ZSwgc2V0VmFsdWVdID0gdXNlU3RhdGUoaXRlbXMpO1xuICBjb25zdCBvblNldHRpbmdDaGFuZ2UgPSAoXG4gICAga2V5OiBzdHJpbmcsXG4gICAgZTogUmVhY3QuQ2hhbmdlRXZlbnQ8SFRNTElucHV0RWxlbWVudD5cbiAgKSA9PiB7XG4gICAgY29uc3QgbmV3VmFsdWUgPSB7XG4gICAgICAuLi5zZXR0aW5nVmFsdWUsXG4gICAgICBba2V5XTogcGFyc2VJbnQoZS50YXJnZXQudmFsdWUpXG4gICAgfTtcblxuICAgIHNldHRpbmdzLnNldChBVkFJTEFCTEVfUFJPVklERVJTLCBuZXdWYWx1ZSkuY2F0Y2goY29uc29sZS5lcnJvcik7XG5cbiAgICBzZXRWYWx1ZShuZXdWYWx1ZSk7XG4gIH07XG4gIHJldHVybiAoXG4gICAgLy9UT0RPIFJlbW92ZSBoYXJkIGNvZGVkIGNsYXNzIG5hbWVzXG4gICAgPGRpdj5cbiAgICAgIDxmaWVsZHNldD5cbiAgICAgICAgPGxlZ2VuZD57dGl0bGV9PC9sZWdlbmQ+XG4gICAgICAgIDxwIGNsYXNzTmFtZT1cImZpZWxkLWRlc2NyaXB0aW9uXCI+e2Rlc2N9PC9wPlxuICAgICAgICB7T2JqZWN0LmtleXMoaXRlbXMpLm1hcChrZXkgPT4ge1xuICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICA8ZGl2IGtleT17a2V5fSBjbGFzc05hbWU9XCJmb3JtLWdyb3VwIHNtYWxsLWZpZWxkXCI+XG4gICAgICAgICAgICAgIDxkaXY+XG4gICAgICAgICAgICAgICAgPGgzPiB7a2V5fTwvaDM+XG4gICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJpbnB1dEZpZWxkV3JhcHBlclwiPlxuICAgICAgICAgICAgICAgICAgPGlucHV0XG4gICAgICAgICAgICAgICAgICAgIGNsYXNzTmFtZT1cImZvcm0tY29udHJvbFwiXG4gICAgICAgICAgICAgICAgICAgIHR5cGU9XCJudW1iZXJcIlxuICAgICAgICAgICAgICAgICAgICB2YWx1ZT17c2V0dGluZ1ZhbHVlW2tleV19XG4gICAgICAgICAgICAgICAgICAgIG9uQ2hhbmdlPXtlID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICBvblNldHRpbmdDaGFuZ2Uoa2V5LCBlKTtcbiAgICAgICAgICAgICAgICAgICAgfX1cbiAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgKTtcbiAgICAgICAgfSl9XG4gICAgICA8L2ZpZWxkc2V0PlxuICAgIDwvZGl2PlxuICApO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9