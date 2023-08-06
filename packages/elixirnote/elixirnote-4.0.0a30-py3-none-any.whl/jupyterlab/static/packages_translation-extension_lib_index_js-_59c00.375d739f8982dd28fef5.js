"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_translation-extension_lib_index_js-_59c00"],{

/***/ "../../packages/translation-extension/lib/index.js":
/*!*********************************************************!*\
  !*** ../../packages/translation-extension/lib/index.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/mainmenu */ "webpack/sharing/consume/default/@jupyterlab/mainmenu/@jupyterlab/mainmenu");
/* harmony import */ var _jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* ----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module translation-extension
 */





/**
 * Translation plugins
 */
const PLUGIN_ID = '@jupyterlab/translation-extension:plugin';
const translator = {
    id: '@jupyterlab/translation:translator',
    autoStart: true,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.JupyterFrontEnd.IPaths, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry],
    optional: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    provides: _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator,
    activate: async (app, paths, settings, labShell) => {
        const setting = await settings.load(PLUGIN_ID);
        const currentLocale = setting.get('locale').composite;
        let stringsPrefix = setting.get('stringsPrefix')
            .composite;
        const displayStringsPrefix = setting.get('displayStringsPrefix')
            .composite;
        stringsPrefix = displayStringsPrefix ? stringsPrefix : '';
        const serverSettings = app.serviceManager.serverSettings;
        const translationManager = new _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.TranslationManager(paths.urls.translations, stringsPrefix, serverSettings);
        await translationManager.fetch(currentLocale);
        // Set translator to UI
        if (labShell) {
            labShell.translator = translationManager;
        }
        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.translator = translationManager;
        return translationManager;
    }
};
/**
 * Initialization data for the extension.
 */
const langMenu = {
    id: PLUGIN_ID,
    requires: [_jupyterlab_mainmenu__WEBPACK_IMPORTED_MODULE_2__.IMainMenu, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_3__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.ITranslator],
    autoStart: true,
    activate: (app, mainMenu, settings, translator) => {
        const trans = translator.load('jupyterlab');
        const { commands } = app;
        let currentLocale;
        /**
         * Load the settings for this extension
         *
         * @param setting Extension settings
         */
        function loadSetting(setting) {
            // Read the settings and convert to the correct type
            currentLocale = setting.get('locale').composite;
        }
        settings
            .load(PLUGIN_ID)
            .then(setting => {
            var _a;
            // Read the settings
            loadSetting(setting);
            document.documentElement.lang = currentLocale;
            // Listen for your plugin setting changes using Signal
            setting.changed.connect(loadSetting);
            // Create a languages menu
            const languagesMenu = (_a = mainMenu.settingsMenu.items.find(item => {
                var _a;
                return item.type === 'submenu' &&
                    ((_a = item.submenu) === null || _a === void 0 ? void 0 : _a.id) === 'jp-mainmenu-settings-language';
            })) === null || _a === void 0 ? void 0 : _a.submenu;
            let command;
            const serverSettings = app.serviceManager.serverSettings;
            // Get list of available locales
            (0,_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.requestTranslationsAPI)('', '', {}, serverSettings)
                .then(data => {
                for (const locale in data['data']) {
                    const value = data['data'][locale];
                    const displayName = value.displayName;
                    const nativeName = value.nativeName;
                    const toggled = displayName === nativeName;
                    const label = toggled
                        ? `${displayName}`
                        : `${displayName} - ${nativeName}`;
                    // Add a command per language
                    command = `jupyterlab-translation:${locale}`;
                    commands.addCommand(command, {
                        label: label,
                        caption: label,
                        isEnabled: () => !toggled,
                        isVisible: () => true,
                        isToggled: () => toggled,
                        execute: () => {
                            return (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.showDialog)({
                                title: trans.__('Change interface language?'),
                                body: trans.__('After changing the interface language to %1, you will need to reload JupyterLab to see the changes.', label),
                                buttons: [
                                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.cancelButton({ label: trans.__('Cancel') }),
                                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.Dialog.okButton({ label: trans.__('Change and reload') })
                                ]
                            }).then(result => {
                                if (result.button.accept) {
                                    setting
                                        .set('locale', locale)
                                        .then(() => {
                                        window.location.reload();
                                    })
                                        .catch(reason => {
                                        console.error(reason);
                                    });
                                }
                            });
                        }
                    });
                    // Add the language command to the menu
                    if (languagesMenu) {
                        languagesMenu.addItem({
                            command,
                            args: {}
                        });
                    }
                }
            })
                .catch(reason => {
                console.error(`Available locales errored!\n${reason}`);
            });
        })
            .catch(reason => {
            console.error(`The jupyterlab translation extension appears to be missing.\n${reason}`);
        });
    }
};
/**
 * Export the plugins as default.
 */
const plugins = [translator, langMenu];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdHJhbnNsYXRpb24tZXh0ZW5zaW9uX2xpYl9pbmRleF9qcy1fNTljMDAuMzc1ZDczOWY4OTgyZGQyOGZlZjUuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7OytFQUcrRTtBQUMvRTs7O0dBR0c7QUFNOEI7QUFDeUI7QUFDVDtBQUNjO0FBSzlCO0FBRWpDOztHQUVHO0FBQ0gsTUFBTSxTQUFTLEdBQUcsMENBQTBDLENBQUM7QUFFN0QsTUFBTSxVQUFVLEdBQXVDO0lBQ3JELEVBQUUsRUFBRSxvQ0FBb0M7SUFDeEMsU0FBUyxFQUFFLElBQUk7SUFDZixRQUFRLEVBQUUsQ0FBQywyRUFBc0IsRUFBRSx5RUFBZ0IsQ0FBQztJQUNwRCxRQUFRLEVBQUUsQ0FBQyw4REFBUyxDQUFDO0lBQ3JCLFFBQVEsRUFBRSxnRUFBVztJQUNyQixRQUFRLEVBQUUsS0FBSyxFQUNiLEdBQW9CLEVBQ3BCLEtBQTZCLEVBQzdCLFFBQTBCLEVBQzFCLFFBQTBCLEVBQzFCLEVBQUU7UUFDRixNQUFNLE9BQU8sR0FBRyxNQUFNLFFBQVEsQ0FBQyxJQUFJLENBQUMsU0FBUyxDQUFDLENBQUM7UUFDL0MsTUFBTSxhQUFhLEdBQVcsT0FBTyxDQUFDLEdBQUcsQ0FBQyxRQUFRLENBQUMsQ0FBQyxTQUFtQixDQUFDO1FBQ3hFLElBQUksYUFBYSxHQUFXLE9BQU8sQ0FBQyxHQUFHLENBQUMsZUFBZSxDQUFDO2FBQ3JELFNBQW1CLENBQUM7UUFDdkIsTUFBTSxvQkFBb0IsR0FBWSxPQUFPLENBQUMsR0FBRyxDQUFDLHNCQUFzQixDQUFDO2FBQ3RFLFNBQW9CLENBQUM7UUFDeEIsYUFBYSxHQUFHLG9CQUFvQixDQUFDLENBQUMsQ0FBQyxhQUFhLENBQUMsQ0FBQyxDQUFDLEVBQUUsQ0FBQztRQUMxRCxNQUFNLGNBQWMsR0FBRyxHQUFHLENBQUMsY0FBYyxDQUFDLGNBQWMsQ0FBQztRQUN6RCxNQUFNLGtCQUFrQixHQUFHLElBQUksdUVBQWtCLENBQy9D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QUFDLENBQUM7aUJBQ0QsS0FBSyxDQUFDLE1BQU0sQ0FBQyxFQUFFO2dCQUNkLE9BQU8sQ0FBQyxLQUFLLENBQUMsK0JBQStCLE1BQU0sRUFBRSxDQUFDLENBQUM7WUFDekQsQ0FBQyxDQUFDLENBQUM7UUFDUCxDQUFDLENBQUM7YUFDRCxLQUFLLENBQUMsTUFBTSxDQUFDLEVBQUU7WUFDZCxPQUFPLENBQUMsS0FBSyxDQUNYLGdFQUFnRSxNQUFNLEVBQUUsQ0FDekUsQ0FBQztRQUNKLENBQUMsQ0FBQyxDQUFDO0lBQ1AsQ0FBQztDQUNGLENBQUM7QUFFRjs7R0FFRztBQUNILE1BQU0sT0FBTyxHQUFpQyxDQUFDLFVBQVUsRUFBRSxRQUFRLENBQUMsQ0FBQztBQUNyRSxpRUFBZSxPQUFPLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdHJhbnNsYXRpb24tZXh0ZW5zaW9uL3NyYy9pbmRleC50cyJdLCJzb3VyY2VzQ29udGVudCI6WyIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgdHJhbnNsYXRpb24tZXh0ZW5zaW9uXG4gKi9cblxuaW1wb3J0IHtcbiAgSUxhYlNoZWxsLFxuICBKdXB5dGVyRnJvbnRFbmQsXG4gIEp1cHl0ZXJGcm9udEVuZFBsdWdpblxufSBmcm9tICdAanVweXRlcmxhYi9hcHBsaWNhdGlvbic7XG5pbXBvcnQgeyBEaWFsb2csIHNob3dEaWFsb2cgfSBmcm9tICdAanVweXRlcmxhYi9hcHB1dGlscyc7XG5pbXBvcnQgeyBJTWFpbk1lbnUgfSBmcm9tICdAanVweXRlcmxhYi9tYWlubWVudSc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7XG4gIElUcmFuc2xhdG9yLFxuICByZXF1ZXN0VHJhbnNsYXRpb25zQVBJLFxuICBUcmFuc2xhdGlvbk1hbmFnZXJcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuXG4vKipcbiAqIFRyYW5zbGF0aW9uIHBsdWdpbnNcbiAqL1xuY29uc3QgUExVR0lOX0lEID0gJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uLWV4dGVuc2lvbjpwbHVnaW4nO1xuXG5jb25zdCB0cmFuc2xhdG9yOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SVRyYW5zbGF0b3I+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL3RyYW5zbGF0aW9uOnRyYW5zbGF0b3InLFxuICBhdXRvU3RhcnQ6IHRydWUsXG4gIHJlcXVpcmVzOiBbSnVweXRlckZyb250RW5kLklQYXRocywgSVNldHRpbmdSZWdpc3RyeV0sXG4gIG9wdGlvbmFsOiBbSUxhYlNoZWxsXSxcbiAgcHJvdmlkZXM6IElUcmFuc2xhdG9yLFxuICBhY3RpdmF0ZTogYXN5bmMgKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIHBhdGhzOiBKdXB5dGVyRnJvbnRFbmQuSVBhdGhzLFxuICAgIHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LFxuICAgIGxhYlNoZWxsOiBJTGFiU2hlbGwgfCBudWxsXG4gICkgPT4ge1xuICAgIGNvbnN0IHNldHRpbmcgPSBhd2FpdCBzZXR0aW5ncy5sb2FkKFBMVUdJTl9JRCk7XG4gICAgY29uc3QgY3VycmVudExvY2FsZTogc3RyaW5nID0gc2V0dGluZy5nZXQoJ2xvY2FsZScpLmNvbXBvc2l0ZSBhcyBzdHJpbmc7XG4gICAgbGV0IHN0cmluZ3NQcmVmaXg6IHN0cmluZyA9IHNldHRpbmcuZ2V0KCdzdHJpbmdzUHJlZml4JylcbiAgICAgIC5jb21wb3NpdGUgYXMgc3RyaW5nO1xuICAgIGNvbnN0IGRpc3BsYXlTdHJpbmdzUHJlZml4OiBib29sZWFuID0gc2V0dGluZy5nZXQoJ2Rpc3BsYXlTdHJpbmdzUHJlZml4JylcbiAgICAgIC5jb21wb3NpdGUgYXMgYm9vbGVhbjtcbiAgICBzdHJpbmdzUHJlZml4ID0gZGlzcGxheVN0cmluZ3NQcmVmaXggPyBzdHJpbmdzUHJlZml4IDogJyc7XG4gICAgY29uc3Qgc2VydmVyU2V0dGluZ3MgPSBhcHAuc2VydmljZU1hbmFnZXIuc2VydmVyU2V0dGluZ3M7XG4gICAgY29uc3QgdHJhbnNsYXRpb25NYW5hZ2VyID0gbmV3IFRyYW5zbGF0aW9uTWFuYWdlcihcbiAgICAgIHBhdGhzLnVybHMudHJhbnNsYXRpb25zLFxuICAgICAgc3RyaW5nc1ByZWZpeCxcbiAgICAgIHNlcnZlclNldHRpbmdzXG4gICAgKTtcbiAgICBhd2FpdCB0cmFuc2xhdGlvbk1hbmFnZXIuZmV0Y2goY3VycmVudExvY2FsZSk7XG5cbiAgICAvLyBTZXQgdHJhbnNsYXRvciB0byBVSVxuICAgIGlmIChsYWJTaGVsbCkge1xuICAgICAgbGFiU2hlbGwudHJhbnNsYXRvciA9IHRyYW5zbGF0aW9uTWFuYWdlcjtcbiAgICB9XG5cbiAgICBEaWFsb2cudHJhbnNsYXRvciA9IHRyYW5zbGF0aW9uTWFuYWdlcjtcblxuICAgIHJldHVybiB0cmFuc2xhdGlvbk1hbmFnZXI7XG4gIH1cbn07XG5cbi8qKlxuICogSW5pdGlhbGl6YXRpb24gZGF0YSBmb3IgdGhlIGV4dGVuc2lvbi5cbiAqL1xuY29uc3QgbGFuZ01lbnU6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjx2b2lkPiA9IHtcbiAgaWQ6IFBMVUdJTl9JRCxcbiAgcmVxdWlyZXM6IFtJTWFpbk1lbnUsIElTZXR0aW5nUmVnaXN0cnksIElUcmFuc2xhdG9yXSxcbiAgYXV0b1N0YXJ0OiB0cnVlLFxuICBhY3RpdmF0ZTogKFxuICAgIGFwcDogSnVweXRlckZyb250RW5kLFxuICAgIG1haW5NZW51OiBJTWFpbk1lbnUsXG4gICAgc2V0dGluZ3M6IElTZXR0aW5nUmVnaXN0cnksXG4gICAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3JcbiAgKSA9PiB7XG4gICAgY29uc3QgdHJhbnMgPSB0cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcbiAgICBjb25zdCB7IGNvbW1hbmRzIH0gPSBhcHA7XG4gICAgbGV0IGN1cnJlbnRMb2NhbGU6IHN0cmluZztcbiAgICAvKipcbiAgICAgKiBMb2FkIHRoZSBzZXR0aW5ncyBmb3IgdGhpcyBleHRlbnNpb25cbiAgICAgKlxuICAgICAqIEBwYXJhbSBzZXR0aW5nIEV4dGVuc2lvbiBzZXR0aW5nc1xuICAgICAqL1xuICAgIGZ1bmN0aW9uIGxvYWRTZXR0aW5nKHNldHRpbmc6IElTZXR0aW5nUmVnaXN0cnkuSVNldHRpbmdzKTogdm9pZCB7XG4gICAgICAvLyBSZWFkIHRoZSBzZXR0aW5ncyBhbmQgY29udmVydCB0byB0aGUgY29ycmVjdCB0eXBlXG4gICAgICBjdXJyZW50TG9jYWxlID0gc2V0dGluZy5nZXQoJ2xvY2FsZScpLmNvbXBvc2l0ZSBhcyBzdHJpbmc7XG4gICAgfVxuXG4gICAgc2V0dGluZ3NcbiAgICAgIC5sb2FkKFBMVUdJTl9JRClcbiAgICAgIC50aGVuKHNldHRpbmcgPT4ge1xuICAgICAgICAvLyBSZWFkIHRoZSBzZXR0aW5nc1xuICAgICAgICBsb2FkU2V0dGluZyhzZXR0aW5nKTtcbiAgICAgICAgZG9jdW1lbnQuZG9jdW1lbnRFbGVtZW50LmxhbmcgPSBjdXJyZW50TG9jYWxlO1xuXG4gICAgICAgIC8vIExpc3RlbiBmb3IgeW91ciBwbHVnaW4gc2V0dGluZyBjaGFuZ2VzIHVzaW5nIFNpZ25hbFxuICAgICAgICBzZXR0aW5nLmNoYW5nZWQuY29ubmVjdChsb2FkU2V0dGluZyk7XG5cbiAgICAgICAgLy8gQ3JlYXRlIGEgbGFuZ3VhZ2VzIG1lbnVcbiAgICAgICAgY29uc3QgbGFuZ3VhZ2VzTWVudSA9IG1haW5NZW51LnNldHRpbmdzTWVudS5pdGVtcy5maW5kKFxuICAgICAgICAgIGl0ZW0gPT5cbiAgICAgICAgICAgIGl0ZW0udHlwZSA9PT0gJ3N1Ym1lbnUnICYmXG4gICAgICAgICAgICBpdGVtLnN1Ym1lbnU/LmlkID09PSAnanAtbWFpbm1lbnUtc2V0dGluZ3MtbGFuZ3VhZ2UnXG4gICAgICAgICk/LnN1Ym1lbnU7XG5cbiAgICAgICAgbGV0IGNvbW1hbmQ6IHN0cmluZztcblxuICAgICAgICBjb25zdCBzZXJ2ZXJTZXR0aW5ncyA9IGFwcC5zZXJ2aWNlTWFuYWdlci5zZXJ2ZXJTZXR0aW5ncztcbiAgICAgICAgLy8gR2V0IGxpc3Qgb2YgYXZhaWxhYmxlIGxvY2FsZXNcbiAgICAgICAgcmVxdWVzdFRyYW5zbGF0aW9uc0FQSTxhbnk+KCcnLCAnJywge30sIHNlcnZlclNldHRpbmdzKVxuICAgICAgICAgIC50aGVuKGRhdGEgPT4ge1xuICAgICAgICAgICAgZm9yIChjb25zdCBsb2NhbGUgaW4gZGF0YVsnZGF0YSddKSB7XG4gICAgICAgICAgICAgIGNvbnN0IHZhbHVlID0gZGF0YVsnZGF0YSddW2xvY2FsZV07XG4gICAgICAgICAgICAgIGNvbnN0IGRpc3BsYXlOYW1lID0gdmFsdWUuZGlzcGxheU5hbWU7XG4gICAgICAgICAgICAgIGNvbnN0IG5hdGl2ZU5hbWUgPSB2YWx1ZS5uYXRpdmVOYW1lO1xuICAgICAgICAgICAgICBjb25zdCB0b2dnbGVkID0gZGlzcGxheU5hbWUgPT09IG5hdGl2ZU5hbWU7XG4gICAgICAgICAgICAgIGNvbnN0IGxhYmVsID0gdG9nZ2xlZFxuICAgICAgICAgICAgICAgID8gYCR7ZGlzcGxheU5hbWV9YFxuICAgICAgICAgICAgICAgIDogYCR7ZGlzcGxheU5hbWV9IC0gJHtuYXRpdmVOYW1lfWA7XG5cbiAgICAgICAgICAgICAgLy8gQWRkIGEgY29tbWFuZCBwZXIgbGFuZ3VhZ2VcbiAgICAgICAgICAgICAgY29tbWFuZCA9IGBqdXB5dGVybGFiLXRyYW5zbGF0aW9uOiR7bG9jYWxlfWA7XG4gICAgICAgICAgICAgIGNvbW1hbmRzLmFkZENvbW1hbmQoY29tbWFuZCwge1xuICAgICAgICAgICAgICAgIGxhYmVsOiBsYWJlbCxcbiAgICAgICAgICAgICAgICBjYXB0aW9uOiBsYWJlbCxcbiAgICAgICAgICAgICAgICBpc0VuYWJsZWQ6ICgpID0+ICF0b2dnbGVkLFxuICAgICAgICAgICAgICAgIGlzVmlzaWJsZTogKCkgPT4gdHJ1ZSxcbiAgICAgICAgICAgICAgICBpc1RvZ2dsZWQ6ICgpID0+IHRvZ2dsZWQsXG4gICAgICAgICAgICAgICAgZXhlY3V0ZTogKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgcmV0dXJuIHNob3dEaWFsb2coe1xuICAgICAgICAgICAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ0NoYW5nZSBpbnRlcmZhY2UgbGFuZ3VhZ2U/JyksXG4gICAgICAgICAgICAgICAgICAgIGJvZHk6IHRyYW5zLl9fKFxuICAgICAgICAgICAgICAgICAgICAgICdBZnRlciBjaGFuZ2luZyB0aGUgaW50ZXJmYWNlIGxhbmd1YWdlIHRvICUxLCB5b3Ugd2lsbCBuZWVkIHRvIHJlbG9hZCBKdXB5dGVyTGFiIHRvIHNlZSB0aGUgY2hhbmdlcy4nLFxuICAgICAgICAgICAgICAgICAgICAgIGxhYmVsXG4gICAgICAgICAgICAgICAgICAgICksXG4gICAgICAgICAgICAgICAgICAgIGJ1dHRvbnM6IFtcbiAgICAgICAgICAgICAgICAgICAgICBEaWFsb2cuY2FuY2VsQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdDYW5jZWwnKSB9KSxcbiAgICAgICAgICAgICAgICAgICAgICBEaWFsb2cub2tCdXR0b24oeyBsYWJlbDogdHJhbnMuX18oJ0NoYW5nZSBhbmQgcmVsb2FkJykgfSlcbiAgICAgICAgICAgICAgICAgICAgXVxuICAgICAgICAgICAgICAgICAgfSkudGhlbihyZXN1bHQgPT4ge1xuICAgICAgICAgICAgICAgICAgICBpZiAocmVzdWx0LmJ1dHRvbi5hY2NlcHQpIHtcbiAgICAgICAgICAgICAgICAgICAgICBzZXR0aW5nXG4gICAgICAgICAgICAgICAgICAgICAgICAuc2V0KCdsb2NhbGUnLCBsb2NhbGUpXG4gICAgICAgICAgICAgICAgICAgICAgICAudGhlbigoKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5sb2NhdGlvbi5yZWxvYWQoKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH0pXG4gICAgICAgICAgICAgICAgICAgICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgY29uc29sZS5lcnJvcihyZWFzb24pO1xuICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgICAgLy8gQWRkIHRoZSBsYW5ndWFnZSBjb21tYW5kIHRvIHRoZSBtZW51XG4gICAgICAgICAgICAgIGlmIChsYW5ndWFnZXNNZW51KSB7XG4gICAgICAgICAgICAgICAgbGFuZ3VhZ2VzTWVudS5hZGRJdGVtKHtcbiAgICAgICAgICAgICAgICAgIGNvbW1hbmQsXG4gICAgICAgICAgICAgICAgICBhcmdzOiB7fVxuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9XG4gICAgICAgICAgfSlcbiAgICAgICAgICAuY2F0Y2gocmVhc29uID0+IHtcbiAgICAgICAgICAgIGNvbnNvbGUuZXJyb3IoYEF2YWlsYWJsZSBsb2NhbGVzIGVycm9yZWQhXFxuJHtyZWFzb259YCk7XG4gICAgICAgICAgfSk7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKHJlYXNvbiA9PiB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoXG4gICAgICAgICAgYFRoZSBqdXB5dGVybGFiIHRyYW5zbGF0aW9uIGV4dGVuc2lvbiBhcHBlYXJzIHRvIGJlIG1pc3NpbmcuXFxuJHtyZWFzb259YFxuICAgICAgICApO1xuICAgICAgfSk7XG4gIH1cbn07XG5cbi8qKlxuICogRXhwb3J0IHRoZSBwbHVnaW5zIGFzIGRlZmF1bHQuXG4gKi9cbmNvbnN0IHBsdWdpbnM6IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxhbnk+W10gPSBbdHJhbnNsYXRvciwgbGFuZ01lbnVdO1xuZXhwb3J0IGRlZmF1bHQgcGx1Z2lucztcbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==