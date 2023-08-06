"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_translation_lib_index_js"],{

/***/ "../../packages/translation/lib/base.js":
/*!**********************************************!*\
  !*** ../../packages/translation/lib/base.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "nullTranslator": () => (/* binding */ nullTranslator)
/* harmony export */ });
/* harmony import */ var _gettext__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./gettext */ "../../packages/translation/lib/gettext.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * A translator that loads a dummy language bundle that returns the same input
 * strings.
 */
class NullTranslator {
    constructor(bundle) {
        this._languageBundle = bundle;
    }
    load(domain) {
        return this._languageBundle;
    }
    locale() {
        return 'en';
    }
}
/**
 * A language bundle that returns the same input strings.
 */
class NullLanguageBundle {
    __(msgid, ...args) {
        return this.gettext(msgid, ...args);
    }
    _n(msgid, msgid_plural, n, ...args) {
        return this.ngettext(msgid, msgid_plural, n, ...args);
    }
    _p(msgctxt, msgid, ...args) {
        return this.pgettext(msgctxt, msgid, ...args);
    }
    _np(msgctxt, msgid, msgid_plural, n, ...args) {
        return this.npgettext(msgctxt, msgid, msgid_plural, n, ...args);
    }
    gettext(msgid, ...args) {
        return _gettext__WEBPACK_IMPORTED_MODULE_0__.Gettext.strfmt(msgid, ...args);
    }
    ngettext(msgid, msgid_plural, n, ...args) {
        return _gettext__WEBPACK_IMPORTED_MODULE_0__.Gettext.strfmt(n == 1 ? msgid : msgid_plural, ...[n].concat(args));
    }
    pgettext(msgctxt, msgid, ...args) {
        return _gettext__WEBPACK_IMPORTED_MODULE_0__.Gettext.strfmt(msgid, ...args);
    }
    npgettext(msgctxt, msgid, msgid_plural, n, ...args) {
        return this.ngettext(msgid, msgid_plural, n, ...args);
    }
    dcnpgettext(domain, msgctxt, msgid, msgid_plural, n, ...args) {
        return this.ngettext(msgid, msgid_plural, n, ...args);
    }
}
/**
 * The application null translator instance that just returns the same text.
 * Also provides interpolation.
 */
const nullTranslator = new NullTranslator(new NullLanguageBundle());


/***/ }),

/***/ "../../packages/translation/lib/gettext.js":
/*!*************************************************!*\
  !*** ../../packages/translation/lib/gettext.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Gettext": () => (/* binding */ Gettext)
/* harmony export */ });
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils */ "../../packages/translation/lib/utils.js");
/* ----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|
| Base gettext.js implementation.
| Copyright (c) Guillaume Potier.
| Distributed under the terms of the Modified MIT License.
| See: https://github.com/guillaumepotier/gettext.js
|
| Type definitions.
| Copyright (c) Julien Crouzet and Florian Schwingenschlögl.
| Distributed under the terms of the Modified MIT License.
| See: https://github.com/DefinitelyTyped/DefinitelyTyped
|----------------------------------------------------------------------------*/

/**
 * Gettext class providing localization methods.
 */
class Gettext {
    constructor(options) {
        options = options || {};
        // default values that could be overridden in Gettext() constructor
        this._defaults = {
            domain: 'messages',
            locale: document.documentElement.getAttribute('lang') || 'en',
            pluralFunc: function (n) {
                return { nplurals: 2, plural: n != 1 ? 1 : 0 };
            },
            contextDelimiter: String.fromCharCode(4),
            stringsPrefix: ''
        };
        // Ensure the correct separator is used
        this._locale = (options.locale || this._defaults.locale).replace('_', '-');
        this._domain = (0,_utils__WEBPACK_IMPORTED_MODULE_0__.normalizeDomain)(options.domain || this._defaults.domain);
        this._contextDelimiter =
            options.contextDelimiter || this._defaults.contextDelimiter;
        this._stringsPrefix = options.stringsPrefix || this._defaults.stringsPrefix;
        this._pluralFuncs = {};
        this._dictionary = {};
        this._pluralForms = {};
        if (options.messages) {
            this._dictionary[this._domain] = {};
            this._dictionary[this._domain][this._locale] = options.messages;
        }
        if (options.pluralForms) {
            this._pluralForms[this._locale] = options.pluralForms;
        }
    }
    /**
     * Set current context delimiter.
     *
     * @param delimiter - The delimiter to set.
     */
    setContextDelimiter(delimiter) {
        this._contextDelimiter = delimiter;
    }
    /**
     * Get current context delimiter.
     *
     * @returns The current delimiter.
     */
    getContextDelimiter() {
        return this._contextDelimiter;
    }
    /**
     * Set current locale.
     *
     * @param locale - The locale to set.
     */
    setLocale(locale) {
        this._locale = locale.replace('_', '-');
    }
    /**
     * Get current locale.
     *
     * @returns The current locale.
     */
    getLocale() {
        return this._locale;
    }
    /**
     * Set current domain.
     *
     * @param domain - The domain to set.
     */
    setDomain(domain) {
        this._domain = (0,_utils__WEBPACK_IMPORTED_MODULE_0__.normalizeDomain)(domain);
    }
    /**
     * Get current domain.
     *
     * @returns The current domain string.
     */
    getDomain() {
        return this._domain;
    }
    /**
     * Set current strings prefix.
     *
     * @param prefix - The string prefix to set.
     */
    setStringsPrefix(prefix) {
        this._stringsPrefix = prefix;
    }
    /**
     * Get current strings prefix.
     *
     * @returns The strings prefix.
     */
    getStringsPrefix() {
        return this._stringsPrefix;
    }
    /**
     * `sprintf` equivalent, takes a string and some arguments to make a
     * computed string.
     *
     * @param fmt - The string to interpolate.
     * @param args - The variables to use in interpolation.
     *
     * ### Examples
     * strfmt("%1 dogs are in %2", 7, "the kitchen"); => "7 dogs are in the kitchen"
     * strfmt("I like %1, bananas and %1", "apples"); => "I like apples, bananas and apples"
     */
    static strfmt(fmt, ...args) {
        return (fmt
            // put space after double % to prevent placeholder replacement of such matches
            .replace(/%%/g, '%% ')
            // replace placeholders
            .replace(/%(\d+)/g, function (str, p1) {
            return args[p1 - 1];
        })
            // replace double % and space with single %
            .replace(/%% /g, '%'));
    }
    /**
     * Load json translations strings (In Jed 2.x format).
     *
     * @param jsonData - The translation strings plus metadata.
     * @param domain - The translation domain, e.g. "jupyterlab".
     */
    loadJSON(jsonData, domain) {
        if (!jsonData[''] ||
            !jsonData['']['language'] ||
            !jsonData['']['pluralForms']) {
            throw new Error(`Wrong jsonData, it must have an empty key ("") with "language" and "pluralForms" information: ${jsonData}`);
        }
        domain = (0,_utils__WEBPACK_IMPORTED_MODULE_0__.normalizeDomain)(domain);
        let headers = jsonData[''];
        let jsonDataCopy = JSON.parse(JSON.stringify(jsonData));
        delete jsonDataCopy[''];
        this.setMessages(domain || this._defaults.domain, headers['language'], jsonDataCopy, headers['pluralForms']);
    }
    /**
     * Shorthand for gettext.
     *
     * @param msgid - The singular string to translate.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     *
     * ### Notes
     * This is not a private method (starts with an underscore) it is just
     * a shorter and standard way to call these methods.
     */
    __(msgid, ...args) {
        return this.gettext(msgid, ...args);
    }
    /**
     * Shorthand for ngettext.
     *
     * @param msgid - The singular string to translate.
     * @param msgid_plural - The plural string to translate.
     * @param n - The number for pluralization.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     *
     * ### Notes
     * This is not a private method (starts with an underscore) it is just
     * a shorter and standard way to call these methods.
     */
    _n(msgid, msgid_plural, n, ...args) {
        return this.ngettext(msgid, msgid_plural, n, ...args);
    }
    /**
     * Shorthand for pgettext.
     *
     * @param msgctxt - The message context.
     * @param msgid - The singular string to translate.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     *
     * ### Notes
     * This is not a private method (starts with an underscore) it is just
     * a shorter and standard way to call these methods.
     */
    _p(msgctxt, msgid, ...args) {
        return this.pgettext(msgctxt, msgid, ...args);
    }
    /**
     * Shorthand for npgettext.
     *
     * @param msgctxt - The message context.
     * @param msgid - The singular string to translate.
     * @param msgid_plural - The plural string to translate.
     * @param n - The number for pluralization.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     *
     * ### Notes
     * This is not a private method (starts with an underscore) it is just
     * a shorter and standard way to call these methods.
     */
    _np(msgctxt, msgid, msgid_plural, n, ...args) {
        return this.npgettext(msgctxt, msgid, msgid_plural, n, ...args);
    }
    /**
     * Translate a singular string with extra interpolation values.
     *
     * @param msgid - The singular string to translate.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     */
    gettext(msgid, ...args) {
        return this.dcnpgettext('', '', msgid, '', 0, ...args);
    }
    /**
     * Translate a plural string with extra interpolation values.
     *
     * @param msgid - The singular string to translate.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     */
    ngettext(msgid, msgid_plural, n, ...args) {
        return this.dcnpgettext('', '', msgid, msgid_plural, n, ...args);
    }
    /**
     * Translate a contextualized singular string with extra interpolation values.
     *
     * @param msgctxt - The message context.
     * @param msgid - The singular string to translate.
     * @param args - Any additional values to use with interpolation.
     *
     * @returns A translated string if found, or the original string.
     *
     * ### Notes
     * This is not a private method (starts with an underscore) it is just
     * a shorter and standard way to call these methods.
     */
    pgettext(msgctxt, msgid, ...args) {
        return this.dcnpgettext('', msgctxt, msgid, '', 0, ...args);
    }
    /**
     * Translate a contextualized plural string with extra interpolation values.
     *
     * @param msgctxt - The message context.
     * @param msgid - The singular string to translate.
     * @param msgid_plural - The plural string to translate.
     * @param n - The number for pluralization.
     * @param args - Any additional values to use with interpolation
     *
     * @returns A translated string if found, or the original string.
     */
    npgettext(msgctxt, msgid, msgid_plural, n, ...args) {
        return this.dcnpgettext('', msgctxt, msgid, msgid_plural, n, ...args);
    }
    /**
     * Translate a singular string with extra interpolation values.
     *
     * @param domain - The translations domain.
     * @param msgctxt - The message context.
     * @param msgid - The singular string to translate.
     * @param msgid_plural - The plural string to translate.
     * @param n - The number for pluralization.
     * @param args - Any additional values to use with interpolation
     *
     * @returns A translated string if found, or the original string.
     */
    dcnpgettext(domain, msgctxt, msgid, msgid_plural, n, ...args) {
        domain = (0,_utils__WEBPACK_IMPORTED_MODULE_0__.normalizeDomain)(domain) || this._domain;
        let translation;
        let key = msgctxt
            ? msgctxt + this._contextDelimiter + msgid
            : msgid;
        let options = { pluralForm: false };
        let exist = false;
        let locale = this._locale;
        let locales = this.expandLocale(this._locale);
        for (let i in locales) {
            locale = locales[i];
            exist =
                this._dictionary[domain] &&
                    this._dictionary[domain][locale] &&
                    this._dictionary[domain][locale][key];
            // check condition are valid (.length)
            // because it's not possible to define both a singular and a plural form of the same msgid,
            // we need to check that the stored form is the same as the expected one.
            // if not, we'll just ignore the translation and consider it as not translated.
            if (msgid_plural) {
                exist = exist && this._dictionary[domain][locale][key].length > 1;
            }
            else {
                exist = exist && this._dictionary[domain][locale][key].length == 1;
            }
            if (exist) {
                // This ensures that a variation is used.
                options.locale = locale;
                break;
            }
        }
        if (!exist) {
            translation = [msgid];
            options.pluralFunc = this._defaults.pluralFunc;
        }
        else {
            translation = this._dictionary[domain][locale][key];
        }
        // Singular form
        if (!msgid_plural) {
            return this.t(translation, n, options, ...args);
        }
        // Plural one
        options.pluralForm = true;
        let value = exist ? translation : [msgid, msgid_plural];
        return this.t(value, n, options, ...args);
    }
    /**
     * Split a locale into parent locales. "es-CO" -> ["es-CO", "es"]
     *
     * @param locale - The locale string.
     *
     * @returns An array of locales.
     */
    expandLocale(locale) {
        let locales = [locale];
        let i = locale.lastIndexOf('-');
        while (i > 0) {
            locale = locale.slice(0, i);
            locales.push(locale);
            i = locale.lastIndexOf('-');
        }
        return locales;
    }
    /**
     * Split a locale into parent locales. "es-CO" -> ["es-CO", "es"]
     *
     * @param pluralForm - Plural form string..
     * @returns An function to compute plural forms.
     */
    // eslint-disable-next-line @typescript-eslint/ban-types
    getPluralFunc(pluralForm) {
        // Plural form string regexp
        // taken from https://github.com/Orange-OpenSource/gettext.js/blob/master/lib.gettext.js
        // plural forms list available here http://localization-guide.readthedocs.org/en/latest/l10n/pluralforms.html
        let pf_re = new RegExp('^\\s*nplurals\\s*=\\s*[0-9]+\\s*;\\s*plural\\s*=\\s*(?:\\s|[-\\?\\|&=!<>+*/%:;n0-9_()])+');
        if (!pf_re.test(pluralForm))
            throw new Error(Gettext.strfmt('The plural form "%1" is not valid', pluralForm));
        // Careful here, this is a hidden eval() equivalent..
        // Risk should be reasonable though since we test the pluralForm through regex before
        // taken from https://github.com/Orange-OpenSource/gettext.js/blob/master/lib.gettext.js
        // TODO: should test if https://github.com/soney/jsep present and use it if so
        return new Function('n', 'let plural, nplurals; ' +
            pluralForm +
            ' return { nplurals: nplurals, plural: (plural === true ? 1 : (plural ? plural : 0)) };');
    }
    /**
     * Remove the context delimiter from string.
     *
     * @param str - Translation string.
     * @returns A translation string without context.
     */
    removeContext(str) {
        // if there is context, remove it
        if (str.indexOf(this._contextDelimiter) !== -1) {
            let parts = str.split(this._contextDelimiter);
            return parts[1];
        }
        return str;
    }
    /**
     * Proper translation function that handle plurals and directives.
     *
     * @param messages - List of translation strings.
     * @param n - The number for pluralization.
     * @param options - Translation options.
     * @param args - Any variables to interpolate.
     *
     * @returns A translation string without context.
     *
     * ### Notes
     * Contains juicy parts of https://github.com/Orange-OpenSource/gettext.js/blob/master/lib.gettext.js
     */
    t(messages, n, options, ...args) {
        // Singular is very easy, just pass dictionary message through strfmt
        if (!options.pluralForm)
            return (this._stringsPrefix +
                Gettext.strfmt(this.removeContext(messages[0]), ...args));
        let plural;
        // if a plural func is given, use that one
        if (options.pluralFunc) {
            plural = options.pluralFunc(n);
            // if plural form never interpreted before, do it now and store it
        }
        else if (!this._pluralFuncs[options.locale || '']) {
            this._pluralFuncs[options.locale || ''] = this.getPluralFunc(this._pluralForms[options.locale || '']);
            plural = this._pluralFuncs[options.locale || ''](n);
            // we have the plural function, compute the plural result
        }
        else {
            plural = this._pluralFuncs[options.locale || ''](n);
        }
        // If there is a problem with plurals, fallback to singular one
        if ('undefined' === typeof !plural.plural ||
            plural.plural > plural.nplurals ||
            messages.length <= plural.plural)
            plural.plural = 0;
        return (this._stringsPrefix +
            Gettext.strfmt(this.removeContext(messages[plural.plural]), ...[n].concat(args)));
    }
    /**
     * Set messages after loading them.
     *
     * @param domain - The translation domain.
     * @param locale - The translation locale.
     * @param messages - List of translation strings.
     * @param pluralForms - Plural form string.
     *
     * ### Notes
     * Contains juicy parts of https://github.com/Orange-OpenSource/gettext.js/blob/master/lib.gettext.js
     */
    setMessages(domain, locale, messages, pluralForms) {
        domain = (0,_utils__WEBPACK_IMPORTED_MODULE_0__.normalizeDomain)(domain);
        if (pluralForms)
            this._pluralForms[locale] = pluralForms;
        if (!this._dictionary[domain])
            this._dictionary[domain] = {};
        this._dictionary[domain][locale] = messages;
    }
}



/***/ }),

/***/ "../../packages/translation/lib/index.js":
/*!***********************************************!*\
  !*** ../../packages/translation/lib/index.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Gettext": () => (/* reexport safe */ _gettext__WEBPACK_IMPORTED_MODULE_1__.Gettext),
/* harmony export */   "ITranslator": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.ITranslator),
/* harmony export */   "ITranslatorConnector": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.ITranslatorConnector),
/* harmony export */   "TranslationManager": () => (/* reexport safe */ _manager__WEBPACK_IMPORTED_MODULE_2__.TranslationManager),
/* harmony export */   "TranslatorConnector": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_4__.TranslatorConnector),
/* harmony export */   "nullTranslator": () => (/* reexport safe */ _base__WEBPACK_IMPORTED_MODULE_0__.nullTranslator),
/* harmony export */   "requestTranslationsAPI": () => (/* reexport safe */ _server__WEBPACK_IMPORTED_MODULE_3__.requestTranslationsAPI)
/* harmony export */ });
/* harmony import */ var _base__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./base */ "../../packages/translation/lib/base.js");
/* harmony import */ var _gettext__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./gettext */ "../../packages/translation/lib/gettext.js");
/* harmony import */ var _manager__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./manager */ "../../packages/translation/lib/manager.js");
/* harmony import */ var _server__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./server */ "../../packages/translation/lib/server.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./tokens */ "../../packages/translation/lib/tokens.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module translation
 */
// Note: keep in alphabetical order...







/***/ }),

/***/ "../../packages/translation/lib/manager.js":
/*!*************************************************!*\
  !*** ../../packages/translation/lib/manager.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "TranslationManager": () => (/* binding */ TranslationManager)
/* harmony export */ });
/* harmony import */ var _gettext__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./gettext */ "../../packages/translation/lib/gettext.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tokens */ "../../packages/translation/lib/tokens.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils */ "../../packages/translation/lib/utils.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.



/**
 * Translation Manager
 */
class TranslationManager {
    constructor(translationsUrl = '', stringsPrefix, serverSettings) {
        this._domainData = {};
        this._translationBundles = {};
        this._connector = new _tokens__WEBPACK_IMPORTED_MODULE_1__.TranslatorConnector(translationsUrl, serverSettings);
        this._stringsPrefix = stringsPrefix || '';
        this._englishBundle = new _gettext__WEBPACK_IMPORTED_MODULE_0__.Gettext({ stringsPrefix: this._stringsPrefix });
    }
    /**
     * Fetch the localization data from the server.
     *
     * @param locale The language locale to use for translations.
     */
    async fetch(locale) {
        var _a, _b;
        this._currentLocale = locale;
        this._languageData = await this._connector.fetch({ language: locale });
        this._domainData = ((_a = this._languageData) === null || _a === void 0 ? void 0 : _a.data) || {};
        const message = (_b = this._languageData) === null || _b === void 0 ? void 0 : _b.message;
        if (message && locale !== 'en') {
            console.warn(message);
        }
    }
    /**
     * Load translation bundles for a given domain.
     *
     * @param domain The translation domain to use for translations.
     */
    load(domain) {
        if (this._domainData) {
            if (this._currentLocale == 'en') {
                return this._englishBundle;
            }
            else {
                domain = (0,_utils__WEBPACK_IMPORTED_MODULE_2__.normalizeDomain)(domain);
                if (!(domain in this._translationBundles)) {
                    let translationBundle = new _gettext__WEBPACK_IMPORTED_MODULE_0__.Gettext({
                        domain: domain,
                        locale: this._currentLocale,
                        stringsPrefix: this._stringsPrefix
                    });
                    if (domain in this._domainData) {
                        let metadata = this._domainData[domain][''];
                        if ('plural_forms' in metadata) {
                            metadata.pluralForms = metadata.plural_forms;
                            delete metadata.plural_forms;
                            this._domainData[domain][''] = metadata;
                        }
                        translationBundle.loadJSON(this._domainData[domain], domain);
                    }
                    this._translationBundles[domain] = translationBundle;
                }
                return this._translationBundles[domain];
            }
        }
        else {
            return this._englishBundle;
        }
    }
}


/***/ }),

/***/ "../../packages/translation/lib/server.js":
/*!************************************************!*\
  !*** ../../packages/translation/lib/server.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestTranslationsAPI": () => (/* binding */ requestTranslationsAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * The url for the translations service.
 */
const TRANSLATIONS_SETTINGS_URL = 'api/translations';
/**
 * Call the API extension
 *
 * @param locale API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestTranslationsAPI(translationsUrl = '', locale = '', init = {}, serverSettings = undefined) {
    // Make request to Jupyter API
    const settings = serverSettings !== null && serverSettings !== void 0 ? serverSettings : _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    translationsUrl =
        translationsUrl || `${settings.appUrl}/${TRANSLATIONS_SETTINGS_URL}`;
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, translationsUrl, locale);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.error('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "../../packages/translation/lib/tokens.js":
/*!************************************************!*\
  !*** ../../packages/translation/lib/tokens.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ITranslator": () => (/* binding */ ITranslator),
/* harmony export */   "ITranslatorConnector": () => (/* binding */ ITranslatorConnector),
/* harmony export */   "TranslatorConnector": () => (/* binding */ TranslatorConnector)
/* harmony export */ });
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/statedb */ "webpack/sharing/consume/default/@jupyterlab/statedb/@jupyterlab/statedb");
/* harmony import */ var _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _server__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./server */ "../../packages/translation/lib/server.js");
/* ----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/



const ITranslatorConnector = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.Token('@jupyterlab/translation:ITranslatorConnector');
class TranslatorConnector extends _jupyterlab_statedb__WEBPACK_IMPORTED_MODULE_0__.DataConnector {
    constructor(translationsUrl = '', serverSettings) {
        super();
        this._translationsUrl = translationsUrl;
        this._serverSettings = serverSettings;
    }
    async fetch(opts) {
        return (0,_server__WEBPACK_IMPORTED_MODULE_2__.requestTranslationsAPI)(this._translationsUrl, opts.language, {}, this._serverSettings);
    }
}
const ITranslator = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.Token('@jupyterlab/translation:ITranslator');


/***/ }),

/***/ "../../packages/translation/lib/utils.js":
/*!***********************************************!*\
  !*** ../../packages/translation/lib/utils.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "normalizeDomain": () => (/* binding */ normalizeDomain)
/* harmony export */ });
/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */
/**
 * Normalize domain
 *
 * @param domain Domain to normalize
 * @returns Normalized domain
 */
function normalizeDomain(domain) {
    return domain.replace('-', '_');
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfdHJhbnNsYXRpb25fbGliX2luZGV4X2pzLjhkOTM4ZmIxY2U1ZDBmNmVmZTUwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUV2QjtBQUdwQzs7O0dBR0c7QUFDSCxNQUFNLGNBQWM7SUFDbEIsWUFBWSxNQUF5QjtRQUNuQyxJQUFJLENBQUMsZUFBZSxHQUFHLE1BQU0sQ0FBQztJQUNoQyxDQUFDO0lBRUQsSUFBSSxDQUFDLE1BQWM7UUFDakIsT0FBTyxJQUFJLENBQUMsZUFBZSxDQUFDO0lBQzlCLENBQUM7SUFFRCxNQUFNO1FBQ0osT0FBTyxJQUFJLENBQUM7SUFDZCxDQUFDO0NBR0Y7QUFFRDs7R0FFRztBQUNILE1BQU0sa0JBQWtCO0lBQ3RCLEVBQUUsQ0FBQyxLQUFhLEVBQUUsR0FBRyxJQUFXO1FBQzlCLE9BQU8sSUFBSSxDQUFDLE9BQU8sQ0FBQyxLQUFLLEVBQUUsR0FBRyxJQUFJLENBQUMsQ0FBQztJQUN0QyxDQUFDO0lBRUQsRUFBRSxDQUFDLEtBQWEsRUFBRSxZQUFvQixFQUFFLENBQVMsRUFBRSxHQUFHLElBQVc7UUFDL0QsT0FBTyxJQUFJLENBQUMsUUFBUSxDQUFDLEtBQUssRUFBRSxZQUFZLEVBQUUsQ0FBQyxFQUFFLEdBQUcsSUFBSSxDQUFDLENBQUM7SUFDeEQsQ0FBQztJQUVELEVBQUUsQ0FBQyxPQUFlLEVBQUUsS0FBYSxFQUFFLEdBQUcsSUFBVztRQUMvQyxPQUFPLElBQUksQ0FBQyxRQUFRLENBQUMsT0FBTyxFQUFFLEtBQUssRUFBRSxHQUFHLElBQUksQ0FBQyxDQUFDO0lBQ2hELENBQUM7SUFFRCxHQUFHLENBQ0QsT0FBZSxFQUNmLEtBQWEsRUFDYixZQUFvQixFQUNwQixDQUFTLEVBQ1QsR0FBRyxJQUFXO1FBRWQsT0FBTyxJQUFJLENBQUMsU0FBUyxDQUFDLE9BQU8sRUFBRSxLQUFLLEVBQUUsWUFBWSxFQUFFLENBQUMsRUFBRSxHQUFHLElBQUksQ0FBQyxD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Ozs7Ozs7Ozs7O0FDN0RGOzs7R0FHRztBQUVIOzs7OztHQUtHO0FBQ0ksU0FBUyxlQUFlLENBQUMsTUFBYztJQUM1QyxPQUFPLE1BQU0sQ0FBQyxPQUFPLENBQUMsR0FBRyxFQUFFLEdBQUcsQ0FBQyxDQUFDO0FBQ2xDLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvdHJhbnNsYXRpb24vc3JjL2Jhc2UudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RyYW5zbGF0aW9uL3NyYy9nZXR0ZXh0LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90cmFuc2xhdGlvbi9zcmMvaW5kZXgudHMiLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL3RyYW5zbGF0aW9uL3NyYy9tYW5hZ2VyLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90cmFuc2xhdGlvbi9zcmMvc2VydmVyLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90cmFuc2xhdGlvbi9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy90cmFuc2xhdGlvbi9zcmMvdXRpbHMudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBHZXR0ZXh0IH0gZnJvbSAnLi9nZXR0ZXh0JztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBUcmFuc2xhdGlvbkJ1bmRsZSB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBBIHRyYW5zbGF0b3IgdGhhdCBsb2FkcyBhIGR1bW15IGxhbmd1YWdlIGJ1bmRsZSB0aGF0IHJldHVybnMgdGhlIHNhbWUgaW5wdXRcbiAqIHN0cmluZ3MuXG4gKi9cbmNsYXNzIE51bGxUcmFuc2xhdG9yIGltcGxlbWVudHMgSVRyYW5zbGF0b3Ige1xuICBjb25zdHJ1Y3RvcihidW5kbGU6IFRyYW5zbGF0aW9uQnVuZGxlKSB7XG4gICAgdGhpcy5fbGFuZ3VhZ2VCdW5kbGUgPSBidW5kbGU7XG4gIH1cblxuICBsb2FkKGRvbWFpbjogc3RyaW5nKTogVHJhbnNsYXRpb25CdW5kbGUge1xuICAgIHJldHVybiB0aGlzLl9sYW5ndWFnZUJ1bmRsZTtcbiAgfVxuXG4gIGxvY2FsZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiAnZW4nO1xuICB9XG5cbiAgcHJpdmF0ZSBfbGFuZ3VhZ2VCdW5kbGU6IFRyYW5zbGF0aW9uQnVuZGxlO1xufVxuXG4vKipcbiAqIEEgbGFuZ3VhZ2UgYnVuZGxlIHRoYXQgcmV0dXJucyB0aGUgc2FtZSBpbnB1dCBzdHJpbmdzLlxuICovXG5jbGFzcyBOdWxsTGFuZ3VhZ2VCdW5kbGUge1xuICBfXyhtc2dpZDogc3RyaW5nLCAuLi5hcmdzOiBhbnlbXSk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuZ2V0dGV4dChtc2dpZCwgLi4uYXJncyk7XG4gIH1cblxuICBfbihtc2dpZDogc3RyaW5nLCBtc2dpZF9wbHVyYWw6IHN0cmluZywgbjogbnVtYmVyLCAuLi5hcmdzOiBhbnlbXSk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMubmdldHRleHQobXNnaWQsIG1zZ2lkX3BsdXJhbCwgbiwgLi4uYXJncyk7XG4gIH1cblxuICBfcChtc2djdHh0OiBzdHJpbmcsIG1zZ2lkOiBzdHJpbmcsIC4uLmFyZ3M6IGFueVtdKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5wZ2V0dGV4dChtc2djdHh0LCBtc2dpZCwgLi4uYXJncyk7XG4gIH1cblxuICBfbnAoXG4gICAgbXNnY3R4dDogc3RyaW5nLFxuICAgIG1zZ2lkOiBzdHJpbmcsXG4gICAgbXNnaWRfcGx1cmFsOiBzdHJpbmcsXG4gICAgbjogbnVtYmVyLFxuICAgIC4uLmFyZ3M6IGFueVtdXG4gICk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMubnBnZXR0ZXh0KG1zZ2N0eHQsIG1zZ2lkLCBtc2dpZF9wbHVyYWwsIG4sIC4uLmFyZ3MpO1xuICB9XG5cbiAgZ2V0dGV4dChtc2dpZDogc3RyaW5nLCAuLi5hcmdzOiBhbnlbXSk6IHN0cmluZyB7XG4gICAgcmV0dXJuIEdldHRleHQuc3RyZm10KG1zZ2lkLCAuLi5hcmdzKTtcbiAgfVxuXG4gIG5nZXR0ZXh0KFxuICAgIG1zZ2lkOiBzdHJpbmcsXG4gICAgbXNnaWRfcGx1cmFsOiBzdHJpbmcsXG4gICAgbjogbnVtYmVyLFxuICAgIC4uLmFyZ3M6IGFueVtdXG4gICk6IHN0cmluZyB7XG4gICAgcmV0dXJuIEdldHRleHQuc3RyZm10KG4gPT0gMSA/IG1zZ2lkIDogbXNnaWRfcGx1cmFsLCAuLi5bbl0uY29uY2F0KGFyZ3MpKTtcbiAgfVxuXG4gIHBnZXR0ZXh0KG1zZ2N0eHQ6IHN0cmluZywgbXNnaWQ6IHN0cmluZywgLi4uYXJnczogYW55W10pOiBzdHJpbmcge1xuICAgIHJldHVybiBHZXR0ZXh0LnN0cmZtdChtc2dpZCwgLi4uYXJncyk7XG4gIH1cblxuICBucGdldHRleHQoXG4gICAgbXNnY3R4dDogc3RyaW5nLFxuICAgIG1zZ2lkOiBzdHJpbmcsXG4gICAgbXNnaWRfcGx1cmFsOiBzdHJpbmcsXG4gICAgbjogbnVtYmVyLFxuICAgIC4uLmFyZ3M6IGFueVtdXG4gICk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMubmdldHRleHQobXNnaWQsIG1zZ2lkX3BsdXJhbCwgbiwgLi4uYXJncyk7XG4gIH1cblxuICBkY25wZ2V0dGV4dChcbiAgICBkb21haW46IHN0cmluZyxcbiAgICBtc2djdHh0OiBzdHJpbmcsXG4gICAgbXNnaWQ6IHN0cmluZyxcbiAgICBtc2dpZF9wbHVyYWw6IHN0cmluZyxcbiAgICBuOiBudW1iZXIsXG4gICAgLi4uYXJnczogYW55W11cbiAgKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5uZ2V0dGV4dChtc2dpZCwgbXNnaWRfcGx1cmFsLCBuLCAuLi5hcmdzKTtcbiAgfVxufVxuXG4vKipcbiAqIFRoZSBhcHBsaWNhdGlvbiBudWxsIHRyYW5zbGF0b3IgaW5zdGFuY2UgdGhhdCBqdXN0IHJldHVybnMgdGhlIHNhbWUgdGV4dC5cbiAqIEFsc28gcHJvdmlkZXMgaW50ZXJwb2xhdGlvbi5cbiAqL1xuZXhwb3J0IGNvbnN0IG51bGxUcmFuc2xhdG9yID0gbmV3IE51bGxUcmFuc2xhdG9yKG5ldyBOdWxsTGFuZ3VhZ2VCdW5kbGUoKSk7XG4iLCIvKiAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufFxufCBCYXNlIGdldHRleHQuanMgaW1wbGVtZW50YXRpb24uXG58IENvcHlyaWdodCAoYykgR3VpbGxhdW1lIFBvdGllci5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBNSVQgTGljZW5zZS5cbnwgU2VlOiBodHRwczovL2dpdGh1Yi5jb20vZ3VpbGxhdW1lcG90aWVyL2dldHRleHQuanNcbnxcbnwgVHlwZSBkZWZpbml0aW9ucy5cbnwgQ29weXJpZ2h0IChjKSBKdWxpZW4gQ3JvdXpldCBhbmQgRmxvcmlhbiBTY2h3aW5nZW5zY2hsw7ZnbC5cbnwgRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBNSVQgTGljZW5zZS5cbnwgU2VlOiBodHRwczovL2dpdGh1Yi5jb20vRGVmaW5pdGVseVR5cGVkL0RlZmluaXRlbHlUeXBlZFxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG5pbXBvcnQgeyBub3JtYWxpemVEb21haW4gfSBmcm9tICcuL3V0aWxzJztcblxuLyoqXG4gKiBBIHBsdXJhbCBmb3JtIGZ1bmN0aW9uLlxuICovXG50eXBlIFBsdXJhbEZvcm0gPSAobjogbnVtYmVyKSA9PiBudW1iZXI7XG5cbi8qKlxuICogTWV0YWRhdGEgZm9yIGEgbGFuZ3VhZ2UgcGFjay5cbiAqL1xuaW50ZXJmYWNlIElKc29uRGF0YUhlYWRlciB7XG4gIC8qKlxuICAgKiBMYW5ndWFnZSBsb2NhbGUuIEV4YW1wbGU6IGVzX0NPLCBlcy1DTy5cbiAgICovXG4gIGxhbmd1YWdlOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRoZSBkb21haW4gb2YgdGhlIHRyYW5zbGF0aW9uLCB1c3VhbGx5IHRoZSBub3JtYWxpemVkIHBhY2thZ2UgbmFtZS5cbiAgICogRXhhbXBsZTogXCJqdXB5dGVybGFiXCIsIFwianVweXRlcmxhYl9naXRcIlxuICAgKlxuICAgKiAjIyMjIE5vdGVcbiAgICogTm9ybWFsaXphdGlvbiByZXBsYWNlcyBgLWAgYnkgYF9gIGluIHBhY2thZ2UgbmFtZS5cbiAgICovXG4gIGRvbWFpbjogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBTdHJpbmcgZGVzY3JpYmluZyB0aGUgcGx1cmFsIG9mIHRoZSBnaXZlbiBsYW5ndWFnZS5cbiAgICogU2VlOiBodHRwczovL3d3dy5nbnUub3JnL3NvZnR3YXJlL2dldHRleHQvbWFudWFsL2h0bWxfbm9kZS9UcmFuc2xhdGluZy1wbHVyYWwtZm9ybXMuaHRtbFxuICAgKi9cbiAgcGx1cmFsRm9ybXM6IHN0cmluZztcbn1cblxuLyoqXG4gKiBUcmFuc2xhdGFibGUgc3RyaW5nIG1lc3NhZ2VzLlxuICovXG5pbnRlcmZhY2UgSUpzb25EYXRhTWVzc2FnZXMge1xuICAvKipcbiAgICogVHJhbnNsYXRpb24gc3RyaW5ncyBmb3IgYSBnaXZlbiBtc2dfaWQuXG4gICAqL1xuICBba2V5OiBzdHJpbmddOiBzdHJpbmdbXSB8IElKc29uRGF0YUhlYWRlcjtcbn1cblxuLyoqXG4gKiBUcmFuc2xhdGFibGUgc3RyaW5nIG1lc3NhZ2VzIGluY2x1aW5nIG1ldGFkYXRhLlxuICovXG5pbnRlcmZhY2UgSUpzb25EYXRhIGV4dGVuZHMgSUpzb25EYXRhTWVzc2FnZXMge1xuICAvKipcbiAgICogTWV0YWRhdGEgb2YgdGhlIGxhbmd1YWdlIGJ1bmRsZS5cbiAgICovXG4gICcnOiBJSnNvbkRhdGFIZWFkZXI7XG59XG5cbi8qKlxuICogQ29uZmlndXJhYmxlIG9wdGlvbnMgZm9yIHRoZSBHZXR0ZXh0IGNvbnN0cnVjdG9yLlxuICovXG5pbnRlcmZhY2UgSU9wdGlvbnMge1xuICAvKipcbiAgICogTGFuZ3VhZ2UgbG9jYWxlLiBFeGFtcGxlOiBlc19DTywgZXMtQ08uXG4gICAqL1xuICBsb2NhbGU/OiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRoZSBkb21haW4gb2YgdGhlIHRyYW5zbGF0aW9uLCB1c3VhbGx5IHRoZSBub3JtYWxpemVkIHBhY2thZ2UgbmFtZS5cbiAgICogRXhhbXBsZTogXCJqdXB5dGVybGFiXCIsIFwianVweXRlcmxhYl9naXRcIlxuICAgKlxuICAgKiAjIyMjIE5vdGVcbiAgICogTm9ybWFsaXphdGlvbiByZXBsYWNlcyBgLWAgYnkgYF9gIGluIHBhY2thZ2UgbmFtZS5cbiAgICovXG4gIGRvbWFpbj86IHN0cmluZztcblxuICAvKipcbiAgICogVGhlIGRlbGltaXRlciB0byB1c2Ugd2hlbiBhZGRpbmcgY29udGV4dHVhbGl6ZWQgc3RyaW5ncy5cbiAgICovXG4gIGNvbnRleHREZWxpbWl0ZXI/OiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRyYW5zbGF0aW9uIG1lc3NhZ2Ugc3RyaW5ncy5cbiAgICovXG4gIG1lc3NhZ2VzPzogQXJyYXk8c3RyaW5nPjtcblxuICAvKipcbiAgICogU3RyaW5nIGRlc2NyaWJpbmcgdGhlIHBsdXJhbCBvZiB0aGUgZ2l2ZW4gbGFuZ3VhZ2UuXG4gICAqIFNlZTogaHR0cHM6Ly93d3cuZ251Lm9yZy9zb2Z0d2FyZS9nZXR0ZXh0L21hbnVhbC9odG1sX25vZGUvVHJhbnNsYXRpbmctcGx1cmFsLWZvcm1zLmh0bWxcbiAgICovXG4gIHBsdXJhbEZvcm1zPzogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBUaGUgc3RyaW5nIHByZWZpeCB0byBhZGQgdG8gbG9jYWxpemVkIHN0cmluZ3MuXG4gICAqL1xuICBzdHJpbmdzUHJlZml4Pzogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBQbHVyYWwgZm9ybSBmdW5jdGlvbi5cbiAgICovXG4gIHBsdXJhbEZ1bmM/OiBQbHVyYWxGb3JtO1xufVxuXG4vKipcbiAqIE9wdGlvbnMgb2YgdGhlIG1haW4gdHJhbnNsYXRpb24gYHRgIG1ldGhvZC5cbiAqL1xuaW50ZXJmYWNlIElUT3B0aW9ucyB7XG4gIC8qKlxuICAgKiBTdHJpbmcgZGVzY3JpYmluZyB0aGUgcGx1cmFsIG9mIHRoZSBnaXZlbiBsYW5ndWFnZS5cbiAgICogU2VlOiBodHRwczovL3d3dy5nbnUub3JnL3NvZnR3YXJlL2dldHRleHQvbWFudWFsL2h0bWxfbm9kZS9UcmFuc2xhdGluZy1wbHVyYWwtZm9ybXMuaHRtbFxuICAgKi9cbiAgcGx1cmFsRm9ybT86IHN0cmluZztcblxuICAvKipcbiAgICogUGx1cmFsIGZvcm0gZnVuY3Rpb24uXG4gICAqL1xuICBwbHVyYWxGdW5jPzogUGx1cmFsRm9ybTtcblxuICAvKipcbiAgICogTGFuZ3VhZ2UgbG9jYWxlLiBFeGFtcGxlOiBlc19DTywgZXMtQ08uXG4gICAqL1xuICBsb2NhbGU/OiBzdHJpbmc7XG59XG5cbi8qKlxuICogR2V0dGV4dCBjbGFzcyBwcm92aWRpbmcgbG9jYWxpemF0aW9uIG1ldGhvZHMuXG4gKi9cbmNsYXNzIEdldHRleHQge1xuICBjb25zdHJ1Y3RvcihvcHRpb25zPzogSU9wdGlvbnMpIHtcbiAgICBvcHRpb25zID0gb3B0aW9ucyB8fCB7fTtcblxuICAgIC8vIGRlZmF1bHQgdmFsdWVzIHRoYXQgY291bGQgYmUgb3ZlcnJpZGRlbiBpbiBHZXR0ZXh0KCkgY29uc3RydWN0b3JcbiAgICB0aGlzLl9kZWZhdWx0cyA9IHtcbiAgICAgIGRvbWFpbjogJ21lc3NhZ2VzJyxcbiAgICAgIGxvY2FsZTogZG9jdW1lbnQuZG9jdW1lbnRFbGVtZW50LmdldEF0dHJpYnV0ZSgnbGFuZycpIHx8ICdlbicsXG4gICAgICBwbHVyYWxGdW5jOiBmdW5jdGlvbiAobjogbnVtYmVyKSB7XG4gICAgICAgIHJldHVybiB7IG5wbHVyYWxzOiAyLCBwbHVyYWw6IG4gIT0gMSA/IDEgOiAwIH07XG4gICAgICB9LFxuICAgICAgY29udGV4dERlbGltaXRlcjogU3RyaW5nLmZyb21DaGFyQ29kZSg0KSwgLy8gXFx1MDAwNFxuICAgICAgc3RyaW5nc1ByZWZpeDogJydcbiAgICB9O1xuXG4gICAgLy8gRW5zdXJlIHRoZSBjb3JyZWN0IHNlcGFyYXRvciBpcyB1c2VkXG4gICAgdGhpcy5fbG9jYWxlID0gKG9wdGlvbnMubG9jYWxlIHx8IHRoaXMuX2RlZmF1bHRzLmxvY2FsZSkucmVwbGFjZSgnXycsICctJyk7XG4gICAgdGhpcy5fZG9tYWluID0gbm9ybWFsaXplRG9tYWluKG9wdGlvbnMuZG9tYWluIHx8IHRoaXMuX2RlZmF1bHRzLmRvbWFpbik7XG4gICAgdGhpcy5fY29udGV4dERlbGltaXRlciA9XG4gICAgICBvcHRpb25zLmNvbnRleHREZWxpbWl0ZXIgfHwgdGhpcy5fZGVmYXVsdHMuY29udGV4dERlbGltaXRlcjtcbiAgICB0aGlzLl9zdHJpbmdzUHJlZml4ID0gb3B0aW9ucy5zdHJpbmdzUHJlZml4IHx8IHRoaXMuX2RlZmF1bHRzLnN0cmluZ3NQcmVmaXg7XG4gICAgdGhpcy5fcGx1cmFsRnVuY3MgPSB7fTtcbiAgICB0aGlzLl9kaWN0aW9uYXJ5ID0ge307XG4gICAgdGhpcy5fcGx1cmFsRm9ybXMgPSB7fTtcblxuICAgIGlmIChvcHRpb25zLm1lc3NhZ2VzKSB7XG4gICAgICB0aGlzLl9kaWN0aW9uYXJ5W3RoaXMuX2RvbWFpbl0gPSB7fTtcbiAgICAgIHRoaXMuX2RpY3Rpb25hcnlbdGhpcy5fZG9tYWluXVt0aGlzLl9sb2NhbGVdID0gb3B0aW9ucy5tZXNzYWdlcztcbiAgICB9XG5cbiAgICBpZiAob3B0aW9ucy5wbHVyYWxGb3Jtcykge1xuICAgICAgdGhpcy5fcGx1cmFsRm9ybXNbdGhpcy5fbG9jYWxlXSA9IG9wdGlvbnMucGx1cmFsRm9ybXM7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFNldCBjdXJyZW50IGNvbnRleHQgZGVsaW1pdGVyLlxuICAgKlxuICAgKiBAcGFyYW0gZGVsaW1pdGVyIC0gVGhlIGRlbGltaXRlciB0byBzZXQuXG4gICAqL1xuICBzZXRDb250ZXh0RGVsaW1pdGVyKGRlbGltaXRlcjogc3RyaW5nKTogdm9pZCB7XG4gICAgdGhpcy5fY29udGV4dERlbGltaXRlciA9IGRlbGltaXRlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgY3VycmVudCBjb250ZXh0IGRlbGltaXRlci5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGN1cnJlbnQgZGVsaW1pdGVyLlxuICAgKi9cbiAgZ2V0Q29udGV4dERlbGltaXRlcigpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9jb250ZXh0RGVsaW1pdGVyO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCBjdXJyZW50IGxvY2FsZS5cbiAgICpcbiAgICogQHBhcmFtIGxvY2FsZSAtIFRoZSBsb2NhbGUgdG8gc2V0LlxuICAgKi9cbiAgc2V0TG9jYWxlKGxvY2FsZTogc3RyaW5nKTogdm9pZCB7XG4gICAgdGhpcy5fbG9jYWxlID0gbG9jYWxlLnJlcGxhY2UoJ18nLCAnLScpO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCBjdXJyZW50IGxvY2FsZS5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGN1cnJlbnQgbG9jYWxlLlxuICAgKi9cbiAgZ2V0TG9jYWxlKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuX2xvY2FsZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgY3VycmVudCBkb21haW4uXG4gICAqXG4gICAqIEBwYXJhbSBkb21haW4gLSBUaGUgZG9tYWluIHRvIHNldC5cbiAgICovXG4gIHNldERvbWFpbihkb21haW46IHN0cmluZyk6IHZvaWQge1xuICAgIHRoaXMuX2RvbWFpbiA9IG5vcm1hbGl6ZURvbWFpbihkb21haW4pO1xuICB9XG5cbiAgLyoqXG4gICAqIEdldCBjdXJyZW50IGRvbWFpbi5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIGN1cnJlbnQgZG9tYWluIHN0cmluZy5cbiAgICovXG4gIGdldERvbWFpbigpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9kb21haW47XG4gIH1cblxuICAvKipcbiAgICogU2V0IGN1cnJlbnQgc3RyaW5ncyBwcmVmaXguXG4gICAqXG4gICAqIEBwYXJhbSBwcmVmaXggLSBUaGUgc3RyaW5nIHByZWZpeCB0byBzZXQuXG4gICAqL1xuICBzZXRTdHJpbmdzUHJlZml4KHByZWZpeDogc3RyaW5nKTogdm9pZCB7XG4gICAgdGhpcy5fc3RyaW5nc1ByZWZpeCA9IHByZWZpeDtcbiAgfVxuXG4gIC8qKlxuICAgKiBHZXQgY3VycmVudCBzdHJpbmdzIHByZWZpeC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIHN0cmluZ3MgcHJlZml4LlxuICAgKi9cbiAgZ2V0U3RyaW5nc1ByZWZpeCgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9zdHJpbmdzUHJlZml4O1xuICB9XG5cbiAgLyoqXG4gICAqIGBzcHJpbnRmYCBlcXVpdmFsZW50LCB0YWtlcyBhIHN0cmluZyBhbmQgc29tZSBhcmd1bWVudHMgdG8gbWFrZSBhXG4gICAqIGNvbXB1dGVkIHN0cmluZy5cbiAgICpcbiAgICogQHBhcmFtIGZtdCAtIFRoZSBzdHJpbmcgdG8gaW50ZXJwb2xhdGUuXG4gICAqIEBwYXJhbSBhcmdzIC0gVGhlIHZhcmlhYmxlcyB0byB1c2UgaW4gaW50ZXJwb2xhdGlvbi5cbiAgICpcbiAgICogIyMjIEV4YW1wbGVzXG4gICAqIHN0cmZtdChcIiUxIGRvZ3MgYXJlIGluICUyXCIsIDcsIFwidGhlIGtpdGNoZW5cIik7ID0+IFwiNyBkb2dzIGFyZSBpbiB0aGUga2l0Y2hlblwiXG4gICAqIHN0cmZtdChcIkkgbGlrZSAlMSwgYmFuYW5hcyBhbmQgJTFcIiwgXCJhcHBsZXNcIik7ID0+IFwiSSBsaWtlIGFwcGxlcywgYmFuYW5hcyBhbmQgYXBwbGVzXCJcbiAgICovXG4gIHN0YXRpYyBzdHJmbXQoZm10OiBzdHJpbmcsIC4uLmFyZ3M6IGFueVtdKTogc3RyaW5nIHtcbiAgICByZXR1cm4gKFxuICAgICAgZm10XG4gICAgICAgIC8vIHB1dCBzcGFjZSBhZnRlciBkb3VibGUgJSB0byBwcmV2ZW50IHBsYWNlaG9sZGVyIHJlcGxhY2VtZW50IG9mIHN1Y2ggbWF0Y2hlc1xuICAgICAgICAucmVwbGFjZSgvJSUvZywgJyUlICcpXG4gICAgICAgIC8vIHJlcGxhY2UgcGxhY2Vob2xkZXJzXG4gICAgICAgIC5yZXBsYWNlKC8lKFxcZCspL2csIGZ1bmN0aW9uIChzdHIsIHAxKSB7XG4gICAgICAgICAgcmV0dXJuIGFyZ3NbcDEgLSAxXTtcbiAgICAgICAgfSlcbiAgICAgICAgLy8gcmVwbGFjZSBkb3VibGUgJSBhbmQgc3BhY2Ugd2l0aCBzaW5nbGUgJVxuICAgICAgICAucmVwbGFjZSgvJSUgL2csICclJylcbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIExvYWQganNvbiB0cmFuc2xhdGlvbnMgc3RyaW5ncyAoSW4gSmVkIDIueCBmb3JtYXQpLlxuICAgKlxuICAgKiBAcGFyYW0ganNvbkRhdGEgLSBUaGUgdHJhbnNsYXRpb24gc3RyaW5ncyBwbHVzIG1ldGFkYXRhLlxuICAgKiBAcGFyYW0gZG9tYWluIC0gVGhlIHRyYW5zbGF0aW9uIGRvbWFpbiwgZS5nLiBcImp1cHl0ZXJsYWJcIi5cbiAgICovXG4gIGxvYWRKU09OKGpzb25EYXRhOiBJSnNvbkRhdGEsIGRvbWFpbjogc3RyaW5nKTogdm9pZCB7XG4gICAgaWYgKFxuICAgICAgIWpzb25EYXRhWycnXSB8fFxuICAgICAgIWpzb25EYXRhWycnXVsnbGFuZ3VhZ2UnXSB8fFxuICAgICAgIWpzb25EYXRhWycnXVsncGx1cmFsRm9ybXMnXVxuICAgICkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKFxuICAgICAgICBgV3JvbmcganNvbkRhdGEsIGl0IG11c3QgaGF2ZSBhbiBlbXB0eSBrZXkgKFwiXCIpIHdpdGggXCJsYW5ndWFnZVwiIGFuZCBcInBsdXJhbEZvcm1zXCIgaW5mb3JtYXRpb246ICR7anNvbkRhdGF9YFxuICAgICAgKTtcbiAgICB9XG5cbiAgICBkb21haW4gPSBub3JtYWxpemVEb21haW4oZG9tYWluKTtcblxuICAgIGxldCBoZWFkZXJzID0ganNvbkRhdGFbJyddO1xuICAgIGxldCBqc29uRGF0YUNvcHkgPSBKU09OLnBhcnNlKEpTT04uc3RyaW5naWZ5KGpzb25EYXRhKSk7XG4gICAgZGVsZXRlIGpzb25EYXRhQ29weVsnJ107XG5cbiAgICB0aGlzLnNldE1lc3NhZ2VzKFxuICAgICAgZG9tYWluIHx8IHRoaXMuX2RlZmF1bHRzLmRvbWFpbixcbiAgICAgIGhlYWRlcnNbJ2xhbmd1YWdlJ10sXG4gICAgICBqc29uRGF0YUNvcHksXG4gICAgICBoZWFkZXJzWydwbHVyYWxGb3JtcyddXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTaG9ydGhhbmQgZm9yIGdldHRleHQuXG4gICAqXG4gICAqIEBwYXJhbSBtc2dpZCAtIFRoZSBzaW5ndWxhciBzdHJpbmcgdG8gdHJhbnNsYXRlLlxuICAgKiBAcGFyYW0gYXJncyAtIEFueSBhZGRpdGlvbmFsIHZhbHVlcyB0byB1c2Ugd2l0aCBpbnRlcnBvbGF0aW9uLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHRyYW5zbGF0ZWQgc3RyaW5nIGlmIGZvdW5kLCBvciB0aGUgb3JpZ2luYWwgc3RyaW5nLlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogVGhpcyBpcyBub3QgYSBwcml2YXRlIG1ldGhvZCAoc3RhcnRzIHdpdGggYW4gdW5kZXJzY29yZSkgaXQgaXMganVzdFxuICAgKiBhIHNob3J0ZXIgYW5kIHN0YW5kYXJkIHdheSB0byBjYWxsIHRoZXNlIG1ldGhvZHMuXG4gICAqL1xuICBfXyhtc2dpZDogc3RyaW5nLCAuLi5hcmdzOiBhbnlbXSk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuZ2V0dGV4dChtc2dpZCwgLi4uYXJncyk7XG4gIH1cblxuICAvKipcbiAgICogU2hvcnRoYW5kIGZvciBuZ2V0dGV4dC5cbiAgICpcbiAgICogQHBhcmFtIG1zZ2lkIC0gVGhlIHNpbmd1bGFyIHN0cmluZyB0byB0cmFuc2xhdGUuXG4gICAqIEBwYXJhbSBtc2dpZF9wbHVyYWwgLSBUaGUgcGx1cmFsIHN0cmluZyB0byB0cmFuc2xhdGUuXG4gICAqIEBwYXJhbSBuIC0gVGhlIG51bWJlciBmb3IgcGx1cmFsaXphdGlvbi5cbiAgICogQHBhcmFtIGFyZ3MgLSBBbnkgYWRkaXRpb25hbCB2YWx1ZXMgdG8gdXNlIHdpdGggaW50ZXJwb2xhdGlvbi5cbiAgICpcbiAgICogQHJldHVybnMgQSB0cmFuc2xhdGVkIHN0cmluZyBpZiBmb3VuZCwgb3IgdGhlIG9yaWdpbmFsIHN0cmluZy5cbiAgICpcbiAgICogIyMjIE5vdGVzXG4gICAqIFRoaXMgaXMgbm90IGEgcHJpdmF0ZSBtZXRob2QgKHN0YXJ0cyB3aXRoIGFuIHVuZGVyc2NvcmUpIGl0IGlzIGp1c3RcbiAgICogYSBzaG9ydGVyIGFuZCBzdGFuZGFyZCB3YXkgdG8gY2FsbCB0aGVzZSBtZXRob2RzLlxuICAgKi9cbiAgX24obXNnaWQ6IHN0cmluZywgbXNnaWRfcGx1cmFsOiBzdHJpbmcsIG46IG51bWJlciwgLi4uYXJnczogYW55W10pOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLm5nZXR0ZXh0KG1zZ2lkLCBtc2dpZF9wbHVyYWwsIG4sIC4uLmFyZ3MpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNob3J0aGFuZCBmb3IgcGdldHRleHQuXG4gICAqXG4gICAqIEBwYXJhbSBtc2djdHh0IC0gVGhlIG1lc3NhZ2UgY29udGV4dC5cbiAgICogQHBhcmFtIG1zZ2lkIC0gVGhlIHNpbmd1bGFyIHN0cmluZyB0byB0cmFuc2xhdGUuXG4gICAqIEBwYXJhbSBhcmdzIC0gQW55IGFkZGl0aW9uYWwgdmFsdWVzIHRvIHVzZSB3aXRoIGludGVycG9sYXRpb24uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgdHJhbnNsYXRlZCBzdHJpbmcgaWYgZm91bmQsIG9yIHRoZSBvcmlnaW5hbCBzdHJpbmcuXG4gICAqXG4gICAqICMjIyBOb3Rlc1xuICAgKiBUaGlzIGlzIG5vdCBhIHByaXZhdGUgbWV0aG9kIChzdGFydHMgd2l0aCBhbiB1bmRlcnNjb3JlKSBpdCBpcyBqdXN0XG4gICAqIGEgc2hvcnRlciBhbmQgc3RhbmRhcmQgd2F5IHRvIGNhbGwgdGhlc2UgbWV0aG9kcy5cbiAgICovXG4gIF9wKG1zZ2N0eHQ6IHN0cmluZywgbXNnaWQ6IHN0cmluZywgLi4uYXJnczogYW55W10pOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLnBnZXR0ZXh0KG1zZ2N0eHQsIG1zZ2lkLCAuLi5hcmdzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTaG9ydGhhbmQgZm9yIG5wZ2V0dGV4dC5cbiAgICpcbiAgICogQHBhcmFtIG1zZ2N0eHQgLSBUaGUgbWVzc2FnZSBjb250ZXh0LlxuICAgKiBAcGFyYW0gbXNnaWQgLSBUaGUgc2luZ3VsYXIgc3RyaW5nIHRvIHRyYW5zbGF0ZS5cbiAgICogQHBhcmFtIG1zZ2lkX3BsdXJhbCAtIFRoZSBwbHVyYWwgc3RyaW5nIHRvIHRyYW5zbGF0ZS5cbiAgICogQHBhcmFtIG4gLSBUaGUgbnVtYmVyIGZvciBwbHVyYWxpemF0aW9uLlxuICAgKiBAcGFyYW0gYXJncyAtIEFueSBhZGRpdGlvbmFsIHZhbHVlcyB0byB1c2Ugd2l0aCBpbnRlcnBvbGF0aW9uLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHRyYW5zbGF0ZWQgc3RyaW5nIGlmIGZvdW5kLCBvciB0aGUgb3JpZ2luYWwgc3RyaW5nLlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogVGhpcyBpcyBub3QgYSBwcml2YXRlIG1ldGhvZCAoc3RhcnRzIHdpdGggYW4gdW5kZXJzY29yZSkgaXQgaXMganVzdFxuICAgKiBhIHNob3J0ZXIgYW5kIHN0YW5kYXJkIHdheSB0byBjYWxsIHRoZXNlIG1ldGhvZHMuXG4gICAqL1xuICBfbnAoXG4gICAgbXNnY3R4dDogc3RyaW5nLFxuICAgIG1zZ2lkOiBzdHJpbmcsXG4gICAgbXNnaWRfcGx1cmFsOiBzdHJpbmcsXG4gICAgbjogbnVtYmVyLFxuICAgIC4uLmFyZ3M6IGFueVtdXG4gICk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMubnBnZXR0ZXh0KG1zZ2N0eHQsIG1zZ2lkLCBtc2dpZF9wbHVyYWwsIG4sIC4uLmFyZ3MpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRyYW5zbGF0ZSBhIHNpbmd1bGFyIHN0cmluZyB3aXRoIGV4dHJhIGludGVycG9sYXRpb24gdmFsdWVzLlxuICAgKlxuICAgKiBAcGFyYW0gbXNnaWQgLSBUaGUgc2luZ3VsYXIgc3RyaW5nIHRvIHRyYW5zbGF0ZS5cbiAgICogQHBhcmFtIGFyZ3MgLSBBbnkgYWRkaXRpb25hbCB2YWx1ZXMgdG8gdXNlIHdpdGggaW50ZXJwb2xhdGlvbi5cbiAgICpcbiAgICogQHJldHVybnMgQSB0cmFuc2xhdGVkIHN0cmluZyBpZiBmb3VuZCwgb3IgdGhlIG9yaWdpbmFsIHN0cmluZy5cbiAgICovXG4gIGdldHRleHQobXNnaWQ6IHN0cmluZywgLi4uYXJnczogYW55W10pOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLmRjbnBnZXR0ZXh0KCcnLCAnJywgbXNnaWQsICcnLCAwLCAuLi5hcmdzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUcmFuc2xhdGUgYSBwbHVyYWwgc3RyaW5nIHdpdGggZXh0cmEgaW50ZXJwb2xhdGlvbiB2YWx1ZXMuXG4gICAqXG4gICAqIEBwYXJhbSBtc2dpZCAtIFRoZSBzaW5ndWxhciBzdHJpbmcgdG8gdHJhbnNsYXRlLlxuICAgKiBAcGFyYW0gYXJncyAtIEFueSBhZGRpdGlvbmFsIHZhbHVlcyB0byB1c2Ugd2l0aCBpbnRlcnBvbGF0aW9uLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHRyYW5zbGF0ZWQgc3RyaW5nIGlmIGZvdW5kLCBvciB0aGUgb3JpZ2luYWwgc3RyaW5nLlxuICAgKi9cbiAgbmdldHRleHQoXG4gICAgbXNnaWQ6IHN0cmluZyxcbiAgICBtc2dpZF9wbHVyYWw6IHN0cmluZyxcbiAgICBuOiBudW1iZXIsXG4gICAgLi4uYXJnczogYW55W11cbiAgKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5kY25wZ2V0dGV4dCgnJywgJycsIG1zZ2lkLCBtc2dpZF9wbHVyYWwsIG4sIC4uLmFyZ3MpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRyYW5zbGF0ZSBhIGNvbnRleHR1YWxpemVkIHNpbmd1bGFyIHN0cmluZyB3aXRoIGV4dHJhIGludGVycG9sYXRpb24gdmFsdWVzLlxuICAgKlxuICAgKiBAcGFyYW0gbXNnY3R4dCAtIFRoZSBtZXNzYWdlIGNvbnRleHQuXG4gICAqIEBwYXJhbSBtc2dpZCAtIFRoZSBzaW5ndWxhciBzdHJpbmcgdG8gdHJhbnNsYXRlLlxuICAgKiBAcGFyYW0gYXJncyAtIEFueSBhZGRpdGlvbmFsIHZhbHVlcyB0byB1c2Ugd2l0aCBpbnRlcnBvbGF0aW9uLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHRyYW5zbGF0ZWQgc3RyaW5nIGlmIGZvdW5kLCBvciB0aGUgb3JpZ2luYWwgc3RyaW5nLlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogVGhpcyBpcyBub3QgYSBwcml2YXRlIG1ldGhvZCAoc3RhcnRzIHdpdGggYW4gdW5kZXJzY29yZSkgaXQgaXMganVzdFxuICAgKiBhIHNob3J0ZXIgYW5kIHN0YW5kYXJkIHdheSB0byBjYWxsIHRoZXNlIG1ldGhvZHMuXG4gICAqL1xuICBwZ2V0dGV4dChtc2djdHh0OiBzdHJpbmcsIG1zZ2lkOiBzdHJpbmcsIC4uLmFyZ3M6IGFueVtdKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5kY25wZ2V0dGV4dCgnJywgbXNnY3R4dCwgbXNnaWQsICcnLCAwLCAuLi5hcmdzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUcmFuc2xhdGUgYSBjb250ZXh0dWFsaXplZCBwbHVyYWwgc3RyaW5nIHdpdGggZXh0cmEgaW50ZXJwb2xhdGlvbiB2YWx1ZXMuXG4gICAqXG4gICAqIEBwYXJhbSBtc2djdHh0IC0gVGhlIG1lc3NhZ2UgY29udGV4dC5cbiAgICogQHBhcmFtIG1zZ2lkIC0gVGhlIHNpbmd1bGFyIHN0cmluZyB0byB0cmFuc2xhdGUuXG4gICAqIEBwYXJhbSBtc2dpZF9wbHVyYWwgLSBUaGUgcGx1cmFsIHN0cmluZyB0byB0cmFuc2xhdGUuXG4gICAqIEBwYXJhbSBuIC0gVGhlIG51bWJlciBmb3IgcGx1cmFsaXphdGlvbi5cbiAgICogQHBhcmFtIGFyZ3MgLSBBbnkgYWRkaXRpb25hbCB2YWx1ZXMgdG8gdXNlIHdpdGggaW50ZXJwb2xhdGlvblxuICAgKlxuICAgKiBAcmV0dXJucyBBIHRyYW5zbGF0ZWQgc3RyaW5nIGlmIGZvdW5kLCBvciB0aGUgb3JpZ2luYWwgc3RyaW5nLlxuICAgKi9cbiAgbnBnZXR0ZXh0KFxuICAgIG1zZ2N0eHQ6IHN0cmluZyxcbiAgICBtc2dpZDogc3RyaW5nLFxuICAgIG1zZ2lkX3BsdXJhbDogc3RyaW5nLFxuICAgIG46IG51bWJlcixcbiAgICAuLi5hcmdzOiBhbnlbXVxuICApOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLmRjbnBnZXR0ZXh0KCcnLCBtc2djdHh0LCBtc2dpZCwgbXNnaWRfcGx1cmFsLCBuLCAuLi5hcmdzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUcmFuc2xhdGUgYSBzaW5ndWxhciBzdHJpbmcgd2l0aCBleHRyYSBpbnRlcnBvbGF0aW9uIHZhbHVlcy5cbiAgICpcbiAgICogQHBhcmFtIGRvbWFpbiAtIFRoZSB0cmFuc2xhdGlvbnMgZG9tYWluLlxuICAgKiBAcGFyYW0gbXNnY3R4dCAtIFRoZSBtZXNzYWdlIGNvbnRleHQuXG4gICAqIEBwYXJhbSBtc2dpZCAtIFRoZSBzaW5ndWxhciBzdHJpbmcgdG8gdHJhbnNsYXRlLlxuICAgKiBAcGFyYW0gbXNnaWRfcGx1cmFsIC0gVGhlIHBsdXJhbCBzdHJpbmcgdG8gdHJhbnNsYXRlLlxuICAgKiBAcGFyYW0gbiAtIFRoZSBudW1iZXIgZm9yIHBsdXJhbGl6YXRpb24uXG4gICAqIEBwYXJhbSBhcmdzIC0gQW55IGFkZGl0aW9uYWwgdmFsdWVzIHRvIHVzZSB3aXRoIGludGVycG9sYXRpb25cbiAgICpcbiAgICogQHJldHVybnMgQSB0cmFuc2xhdGVkIHN0cmluZyBpZiBmb3VuZCwgb3IgdGhlIG9yaWdpbmFsIHN0cmluZy5cbiAgICovXG4gIGRjbnBnZXR0ZXh0KFxuICAgIGRvbWFpbjogc3RyaW5nLFxuICAgIG1zZ2N0eHQ6IHN0cmluZyxcbiAgICBtc2dpZDogc3RyaW5nLFxuICAgIG1zZ2lkX3BsdXJhbDogc3RyaW5nLFxuICAgIG46IG51bWJlcixcbiAgICAuLi5hcmdzOiBhbnlbXVxuICApOiBzdHJpbmcge1xuICAgIGRvbWFpbiA9IG5vcm1hbGl6ZURvbWFpbihkb21haW4pIHx8IHRoaXMuX2RvbWFpbjtcblxuICAgIGxldCB0cmFuc2xhdGlvbjogQXJyYXk8c3RyaW5nPjtcbiAgICBsZXQga2V5OiBzdHJpbmcgPSBtc2djdHh0XG4gICAgICA/IG1zZ2N0eHQgKyB0aGlzLl9jb250ZXh0RGVsaW1pdGVyICsgbXNnaWRcbiAgICAgIDogbXNnaWQ7XG4gICAgbGV0IG9wdGlvbnM6IGFueSA9IHsgcGx1cmFsRm9ybTogZmFsc2UgfTtcbiAgICBsZXQgZXhpc3Q6IGJvb2xlYW4gPSBmYWxzZTtcbiAgICBsZXQgbG9jYWxlOiBzdHJpbmcgPSB0aGlzLl9sb2NhbGU7XG4gICAgbGV0IGxvY2FsZXMgPSB0aGlzLmV4cGFuZExvY2FsZSh0aGlzLl9sb2NhbGUpO1xuXG4gICAgZm9yIChsZXQgaSBpbiBsb2NhbGVzKSB7XG4gICAgICBsb2NhbGUgPSBsb2NhbGVzW2ldO1xuICAgICAgZXhpc3QgPVxuICAgICAgICB0aGlzLl9kaWN0aW9uYXJ5W2RvbWFpbl0gJiZcbiAgICAgICAgdGhpcy5fZGljdGlvbmFyeVtkb21haW5dW2xvY2FsZV0gJiZcbiAgICAgICAgdGhpcy5fZGljdGlvbmFyeVtkb21haW5dW2xvY2FsZV1ba2V5XTtcblxuICAgICAgLy8gY2hlY2sgY29uZGl0aW9uIGFyZSB2YWxpZCAoLmxlbmd0aClcbiAgICAgIC8vIGJlY2F1c2UgaXQncyBub3QgcG9zc2libGUgdG8gZGVmaW5lIGJvdGggYSBzaW5ndWxhciBhbmQgYSBwbHVyYWwgZm9ybSBvZiB0aGUgc2FtZSBtc2dpZCxcbiAgICAgIC8vIHdlIG5lZWQgdG8gY2hlY2sgdGhhdCB0aGUgc3RvcmVkIGZvcm0gaXMgdGhlIHNhbWUgYXMgdGhlIGV4cGVjdGVkIG9uZS5cbiAgICAgIC8vIGlmIG5vdCwgd2UnbGwganVzdCBpZ25vcmUgdGhlIHRyYW5zbGF0aW9uIGFuZCBjb25zaWRlciBpdCBhcyBub3QgdHJhbnNsYXRlZC5cbiAgICAgIGlmIChtc2dpZF9wbHVyYWwpIHtcbiAgICAgICAgZXhpc3QgPSBleGlzdCAmJiB0aGlzLl9kaWN0aW9uYXJ5W2RvbWFpbl1bbG9jYWxlXVtrZXldLmxlbmd0aCA+IDE7XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBleGlzdCA9IGV4aXN0ICYmIHRoaXMuX2RpY3Rpb25hcnlbZG9tYWluXVtsb2NhbGVdW2tleV0ubGVuZ3RoID09IDE7XG4gICAgICB9XG5cbiAgICAgIGlmIChleGlzdCkge1xuICAgICAgICAvLyBUaGlzIGVuc3VyZXMgdGhhdCBhIHZhcmlhdGlvbiBpcyB1c2VkLlxuICAgICAgICBvcHRpb25zLmxvY2FsZSA9IGxvY2FsZTtcbiAgICAgICAgYnJlYWs7XG4gICAgICB9XG4gICAgfVxuXG4gICAgaWYgKCFleGlzdCkge1xuICAgICAgdHJhbnNsYXRpb24gPSBbbXNnaWRdO1xuICAgICAgb3B0aW9ucy5wbHVyYWxGdW5jID0gdGhpcy5fZGVmYXVsdHMucGx1cmFsRnVuYztcbiAgICB9IGVsc2Uge1xuICAgICAgdHJhbnNsYXRpb24gPSB0aGlzLl9kaWN0aW9uYXJ5W2RvbWFpbl1bbG9jYWxlXVtrZXldO1xuICAgIH1cblxuICAgIC8vIFNpbmd1bGFyIGZvcm1cbiAgICBpZiAoIW1zZ2lkX3BsdXJhbCkge1xuICAgICAgcmV0dXJuIHRoaXMudCh0cmFuc2xhdGlvbiwgbiwgb3B0aW9ucywgLi4uYXJncyk7XG4gICAgfVxuXG4gICAgLy8gUGx1cmFsIG9uZVxuICAgIG9wdGlvbnMucGx1cmFsRm9ybSA9IHRydWU7XG4gICAgbGV0IHZhbHVlOiBBcnJheTxzdHJpbmc+ID0gZXhpc3QgPyB0cmFuc2xhdGlvbiA6IFttc2dpZCwgbXNnaWRfcGx1cmFsXTtcbiAgICByZXR1cm4gdGhpcy50KHZhbHVlLCBuLCBvcHRpb25zLCAuLi5hcmdzKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTcGxpdCBhIGxvY2FsZSBpbnRvIHBhcmVudCBsb2NhbGVzLiBcImVzLUNPXCIgLT4gW1wiZXMtQ09cIiwgXCJlc1wiXVxuICAgKlxuICAgKiBAcGFyYW0gbG9jYWxlIC0gVGhlIGxvY2FsZSBzdHJpbmcuXG4gICAqXG4gICAqIEByZXR1cm5zIEFuIGFycmF5IG9mIGxvY2FsZXMuXG4gICAqL1xuICBwcml2YXRlIGV4cGFuZExvY2FsZShsb2NhbGU6IHN0cmluZyk6IEFycmF5PHN0cmluZz4ge1xuICAgIGxldCBsb2NhbGVzOiBBcnJheTxzdHJpbmc+ID0gW2xvY2FsZV07XG4gICAgbGV0IGk6IG51bWJlciA9IGxvY2FsZS5sYXN0SW5kZXhPZignLScpO1xuICAgIHdoaWxlIChpID4gMCkge1xuICAgICAgbG9jYWxlID0gbG9jYWxlLnNsaWNlKDAsIGkpO1xuICAgICAgbG9jYWxlcy5wdXNoKGxvY2FsZSk7XG4gICAgICBpID0gbG9jYWxlLmxhc3RJbmRleE9mKCctJyk7XG4gICAgfVxuICAgIHJldHVybiBsb2NhbGVzO1xuICB9XG5cbiAgLyoqXG4gICAqIFNwbGl0IGEgbG9jYWxlIGludG8gcGFyZW50IGxvY2FsZXMuIFwiZXMtQ09cIiAtPiBbXCJlcy1DT1wiLCBcImVzXCJdXG4gICAqXG4gICAqIEBwYXJhbSBwbHVyYWxGb3JtIC0gUGx1cmFsIGZvcm0gc3RyaW5nLi5cbiAgICogQHJldHVybnMgQW4gZnVuY3Rpb24gdG8gY29tcHV0ZSBwbHVyYWwgZm9ybXMuXG4gICAqL1xuICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L2Jhbi10eXBlc1xuICBwcml2YXRlIGdldFBsdXJhbEZ1bmMocGx1cmFsRm9ybTogc3RyaW5nKTogRnVuY3Rpb24ge1xuICAgIC8vIFBsdXJhbCBmb3JtIHN0cmluZyByZWdleHBcbiAgICAvLyB0YWtlbiBmcm9tIGh0dHBzOi8vZ2l0aHViLmNvbS9PcmFuZ2UtT3BlblNvdXJjZS9nZXR0ZXh0LmpzL2Jsb2IvbWFzdGVyL2xpYi5nZXR0ZXh0LmpzXG4gICAgLy8gcGx1cmFsIGZvcm1zIGxpc3QgYXZhaWxhYmxlIGhlcmUgaHR0cDovL2xvY2FsaXphdGlvbi1ndWlkZS5yZWFkdGhlZG9jcy5vcmcvZW4vbGF0ZXN0L2wxMG4vcGx1cmFsZm9ybXMuaHRtbFxuICAgIGxldCBwZl9yZSA9IG5ldyBSZWdFeHAoXG4gICAgICAnXlxcXFxzKm5wbHVyYWxzXFxcXHMqPVxcXFxzKlswLTldK1xcXFxzKjtcXFxccypwbHVyYWxcXFxccyo9XFxcXHMqKD86XFxcXHN8Wy1cXFxcP1xcXFx8Jj0hPD4rKi8lOjtuMC05XygpXSkrJ1xuICAgICk7XG5cbiAgICBpZiAoIXBmX3JlLnRlc3QocGx1cmFsRm9ybSkpXG4gICAgICB0aHJvdyBuZXcgRXJyb3IoXG4gICAgICAgIEdldHRleHQuc3RyZm10KCdUaGUgcGx1cmFsIGZvcm0gXCIlMVwiIGlzIG5vdCB2YWxpZCcsIHBsdXJhbEZvcm0pXG4gICAgICApO1xuXG4gICAgLy8gQ2FyZWZ1bCBoZXJlLCB0aGlzIGlzIGEgaGlkZGVuIGV2YWwoKSBlcXVpdmFsZW50Li5cbiAgICAvLyBSaXNrIHNob3VsZCBiZSByZWFzb25hYmxlIHRob3VnaCBzaW5jZSB3ZSB0ZXN0IHRoZSBwbHVyYWxGb3JtIHRocm91Z2ggcmVnZXggYmVmb3JlXG4gICAgLy8gdGFrZW4gZnJvbSBodHRwczovL2dpdGh1Yi5jb20vT3JhbmdlLU9wZW5Tb3VyY2UvZ2V0dGV4dC5qcy9ibG9iL21hc3Rlci9saWIuZ2V0dGV4dC5qc1xuICAgIC8vIFRPRE86IHNob3VsZCB0ZXN0IGlmIGh0dHBzOi8vZ2l0aHViLmNvbS9zb25leS9qc2VwIHByZXNlbnQgYW5kIHVzZSBpdCBpZiBzb1xuICAgIHJldHVybiBuZXcgRnVuY3Rpb24oXG4gICAgICAnbicsXG4gICAgICAnbGV0IHBsdXJhbCwgbnBsdXJhbHM7ICcgK1xuICAgICAgICBwbHVyYWxGb3JtICtcbiAgICAgICAgJyByZXR1cm4geyBucGx1cmFsczogbnBsdXJhbHMsIHBsdXJhbDogKHBsdXJhbCA9PT0gdHJ1ZSA/IDEgOiAocGx1cmFsID8gcGx1cmFsIDogMCkpIH07J1xuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogUmVtb3ZlIHRoZSBjb250ZXh0IGRlbGltaXRlciBmcm9tIHN0cmluZy5cbiAgICpcbiAgICogQHBhcmFtIHN0ciAtIFRyYW5zbGF0aW9uIHN0cmluZy5cbiAgICogQHJldHVybnMgQSB0cmFuc2xhdGlvbiBzdHJpbmcgd2l0aG91dCBjb250ZXh0LlxuICAgKi9cbiAgcHJpdmF0ZSByZW1vdmVDb250ZXh0KHN0cjogc3RyaW5nKTogc3RyaW5nIHtcbiAgICAvLyBpZiB0aGVyZSBpcyBjb250ZXh0LCByZW1vdmUgaXRcbiAgICBpZiAoc3RyLmluZGV4T2YodGhpcy5fY29udGV4dERlbGltaXRlcikgIT09IC0xKSB7XG4gICAgICBsZXQgcGFydHMgPSBzdHIuc3BsaXQodGhpcy5fY29udGV4dERlbGltaXRlcik7XG4gICAgICByZXR1cm4gcGFydHNbMV07XG4gICAgfVxuICAgIHJldHVybiBzdHI7XG4gIH1cblxuICAvKipcbiAgICogUHJvcGVyIHRyYW5zbGF0aW9uIGZ1bmN0aW9uIHRoYXQgaGFuZGxlIHBsdXJhbHMgYW5kIGRpcmVjdGl2ZXMuXG4gICAqXG4gICAqIEBwYXJhbSBtZXNzYWdlcyAtIExpc3Qgb2YgdHJhbnNsYXRpb24gc3RyaW5ncy5cbiAgICogQHBhcmFtIG4gLSBUaGUgbnVtYmVyIGZvciBwbHVyYWxpemF0aW9uLlxuICAgKiBAcGFyYW0gb3B0aW9ucyAtIFRyYW5zbGF0aW9uIG9wdGlvbnMuXG4gICAqIEBwYXJhbSBhcmdzIC0gQW55IHZhcmlhYmxlcyB0byBpbnRlcnBvbGF0ZS5cbiAgICpcbiAgICogQHJldHVybnMgQSB0cmFuc2xhdGlvbiBzdHJpbmcgd2l0aG91dCBjb250ZXh0LlxuICAgKlxuICAgKiAjIyMgTm90ZXNcbiAgICogQ29udGFpbnMganVpY3kgcGFydHMgb2YgaHR0cHM6Ly9naXRodWIuY29tL09yYW5nZS1PcGVuU291cmNlL2dldHRleHQuanMvYmxvYi9tYXN0ZXIvbGliLmdldHRleHQuanNcbiAgICovXG4gIHByaXZhdGUgdChcbiAgICBtZXNzYWdlczogQXJyYXk8c3RyaW5nPixcbiAgICBuOiBudW1iZXIsXG4gICAgb3B0aW9uczogSVRPcHRpb25zLFxuICAgIC4uLmFyZ3M6IGFueVtdXG4gICk6IHN0cmluZyB7XG4gICAgLy8gU2luZ3VsYXIgaXMgdmVyeSBlYXN5LCBqdXN0IHBhc3MgZGljdGlvbmFyeSBtZXNzYWdlIHRocm91Z2ggc3RyZm10XG4gICAgaWYgKCFvcHRpb25zLnBsdXJhbEZvcm0pXG4gICAgICByZXR1cm4gKFxuICAgICAgICB0aGlzLl9zdHJpbmdzUHJlZml4ICtcbiAgICAgICAgR2V0dGV4dC5zdHJmbXQodGhpcy5yZW1vdmVDb250ZXh0KG1lc3NhZ2VzWzBdKSwgLi4uYXJncylcbiAgICAgICk7XG5cbiAgICBsZXQgcGx1cmFsO1xuXG4gICAgLy8gaWYgYSBwbHVyYWwgZnVuYyBpcyBnaXZlbiwgdXNlIHRoYXQgb25lXG4gICAgaWYgKG9wdGlvbnMucGx1cmFsRnVuYykge1xuICAgICAgcGx1cmFsID0gb3B0aW9ucy5wbHVyYWxGdW5jKG4pO1xuXG4gICAgICAvLyBpZiBwbHVyYWwgZm9ybSBuZXZlciBpbnRlcnByZXRlZCBiZWZvcmUsIGRvIGl0IG5vdyBhbmQgc3RvcmUgaXRcbiAgICB9IGVsc2UgaWYgKCF0aGlzLl9wbHVyYWxGdW5jc1tvcHRpb25zLmxvY2FsZSB8fCAnJ10pIHtcbiAgICAgIHRoaXMuX3BsdXJhbEZ1bmNzW29wdGlvbnMubG9jYWxlIHx8ICcnXSA9IHRoaXMuZ2V0UGx1cmFsRnVuYyhcbiAgICAgICAgdGhpcy5fcGx1cmFsRm9ybXNbb3B0aW9ucy5sb2NhbGUgfHwgJyddXG4gICAgICApO1xuICAgICAgcGx1cmFsID0gdGhpcy5fcGx1cmFsRnVuY3Nbb3B0aW9ucy5sb2NhbGUgfHwgJyddKG4pO1xuXG4gICAgICAvLyB3ZSBoYXZlIHRoZSBwbHVyYWwgZnVuY3Rpb24sIGNvbXB1dGUgdGhlIHBsdXJhbCByZXN1bHRcbiAgICB9IGVsc2Uge1xuICAgICAgcGx1cmFsID0gdGhpcy5fcGx1cmFsRnVuY3Nbb3B0aW9ucy5sb2NhbGUgfHwgJyddKG4pO1xuICAgIH1cblxuICAgIC8vIElmIHRoZXJlIGlzIGEgcHJvYmxlbSB3aXRoIHBsdXJhbHMsIGZhbGxiYWNrIHRvIHNpbmd1bGFyIG9uZVxuICAgIGlmIChcbiAgICAgICd1bmRlZmluZWQnID09PSB0eXBlb2YgIXBsdXJhbC5wbHVyYWwgfHxcbiAgICAgIHBsdXJhbC5wbHVyYWwgPiBwbHVyYWwubnBsdXJhbHMgfHxcbiAgICAgIG1lc3NhZ2VzLmxlbmd0aCA8PSBwbHVyYWwucGx1cmFsXG4gICAgKVxuICAgICAgcGx1cmFsLnBsdXJhbCA9IDA7XG5cbiAgICByZXR1cm4gKFxuICAgICAgdGhpcy5fc3RyaW5nc1ByZWZpeCArXG4gICAgICBHZXR0ZXh0LnN0cmZtdChcbiAgICAgICAgdGhpcy5yZW1vdmVDb250ZXh0KG1lc3NhZ2VzW3BsdXJhbC5wbHVyYWxdKSxcbiAgICAgICAgLi4uW25dLmNvbmNhdChhcmdzKVxuICAgICAgKVxuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogU2V0IG1lc3NhZ2VzIGFmdGVyIGxvYWRpbmcgdGhlbS5cbiAgICpcbiAgICogQHBhcmFtIGRvbWFpbiAtIFRoZSB0cmFuc2xhdGlvbiBkb21haW4uXG4gICAqIEBwYXJhbSBsb2NhbGUgLSBUaGUgdHJhbnNsYXRpb24gbG9jYWxlLlxuICAgKiBAcGFyYW0gbWVzc2FnZXMgLSBMaXN0IG9mIHRyYW5zbGF0aW9uIHN0cmluZ3MuXG4gICAqIEBwYXJhbSBwbHVyYWxGb3JtcyAtIFBsdXJhbCBmb3JtIHN0cmluZy5cbiAgICpcbiAgICogIyMjIE5vdGVzXG4gICAqIENvbnRhaW5zIGp1aWN5IHBhcnRzIG9mIGh0dHBzOi8vZ2l0aHViLmNvbS9PcmFuZ2UtT3BlblNvdXJjZS9nZXR0ZXh0LmpzL2Jsb2IvbWFzdGVyL2xpYi5nZXR0ZXh0LmpzXG4gICAqL1xuICBwcml2YXRlIHNldE1lc3NhZ2VzKFxuICAgIGRvbWFpbjogc3RyaW5nLFxuICAgIGxvY2FsZTogc3RyaW5nLFxuICAgIG1lc3NhZ2VzOiBJSnNvbkRhdGFNZXNzYWdlcyxcbiAgICBwbHVyYWxGb3Jtczogc3RyaW5nXG4gICk6IHZvaWQge1xuICAgIGRvbWFpbiA9IG5vcm1hbGl6ZURvbWFpbihkb21haW4pO1xuXG4gICAgaWYgKHBsdXJhbEZvcm1zKSB0aGlzLl9wbHVyYWxGb3Jtc1tsb2NhbGVdID0gcGx1cmFsRm9ybXM7XG5cbiAgICBpZiAoIXRoaXMuX2RpY3Rpb25hcnlbZG9tYWluXSkgdGhpcy5fZGljdGlvbmFyeVtkb21haW5dID0ge307XG5cbiAgICB0aGlzLl9kaWN0aW9uYXJ5W2RvbWFpbl1bbG9jYWxlXSA9IG1lc3NhZ2VzO1xuICB9XG5cbiAgcHJpdmF0ZSBfc3RyaW5nc1ByZWZpeDogc3RyaW5nO1xuICBwcml2YXRlIF9wbHVyYWxGb3JtczogYW55O1xuICBwcml2YXRlIF9kaWN0aW9uYXJ5OiBhbnk7XG4gIHByaXZhdGUgX2xvY2FsZTogc3RyaW5nO1xuICBwcml2YXRlIF9kb21haW46IHN0cmluZztcbiAgcHJpdmF0ZSBfY29udGV4dERlbGltaXRlcjogc3RyaW5nO1xuICBwcml2YXRlIF9wbHVyYWxGdW5jczogYW55O1xuICBwcml2YXRlIF9kZWZhdWx0czogYW55O1xufVxuXG5leHBvcnQgeyBHZXR0ZXh0IH07XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB0cmFuc2xhdGlvblxuICovXG5cbi8vIE5vdGU6IGtlZXAgaW4gYWxwaGFiZXRpY2FsIG9yZGVyLi4uXG5leHBvcnQgKiBmcm9tICcuL2Jhc2UnO1xuZXhwb3J0ICogZnJvbSAnLi9nZXR0ZXh0JztcbmV4cG9ydCAqIGZyb20gJy4vbWFuYWdlcic7XG5leHBvcnQgKiBmcm9tICcuL3NlcnZlcic7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFNlcnZlckNvbm5lY3Rpb24gfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBHZXR0ZXh0IH0gZnJvbSAnLi9nZXR0ZXh0JztcbmltcG9ydCB7IElUcmFuc2xhdG9yLCBUcmFuc2xhdGlvbkJ1bmRsZSwgVHJhbnNsYXRvckNvbm5lY3RvciB9IGZyb20gJy4vdG9rZW5zJztcbmltcG9ydCB7IG5vcm1hbGl6ZURvbWFpbiB9IGZyb20gJy4vdXRpbHMnO1xuXG4vKipcbiAqIFRyYW5zbGF0aW9uIE1hbmFnZXJcbiAqL1xuZXhwb3J0IGNsYXNzIFRyYW5zbGF0aW9uTWFuYWdlciBpbXBsZW1lbnRzIElUcmFuc2xhdG9yIHtcbiAgY29uc3RydWN0b3IoXG4gICAgdHJhbnNsYXRpb25zVXJsOiBzdHJpbmcgPSAnJyxcbiAgICBzdHJpbmdzUHJlZml4Pzogc3RyaW5nLFxuICAgIHNlcnZlclNldHRpbmdzPzogU2VydmVyQ29ubmVjdGlvbi5JU2V0dGluZ3NcbiAgKSB7XG4gICAgdGhpcy5fY29ubmVjdG9yID0gbmV3IFRyYW5zbGF0b3JDb25uZWN0b3IodHJhbnNsYXRpb25zVXJsLCBzZXJ2ZXJTZXR0aW5ncyk7XG4gICAgdGhpcy5fc3RyaW5nc1ByZWZpeCA9IHN0cmluZ3NQcmVmaXggfHwgJyc7XG4gICAgdGhpcy5fZW5nbGlzaEJ1bmRsZSA9IG5ldyBHZXR0ZXh0KHsgc3RyaW5nc1ByZWZpeDogdGhpcy5fc3RyaW5nc1ByZWZpeCB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBGZXRjaCB0aGUgbG9jYWxpemF0aW9uIGRhdGEgZnJvbSB0aGUgc2VydmVyLlxuICAgKlxuICAgKiBAcGFyYW0gbG9jYWxlIFRoZSBsYW5ndWFnZSBsb2NhbGUgdG8gdXNlIGZvciB0cmFuc2xhdGlvbnMuXG4gICAqL1xuICBhc3luYyBmZXRjaChsb2NhbGU6IHN0cmluZyk6IFByb21pc2U8dm9pZD4ge1xuICAgIHRoaXMuX2N1cnJlbnRMb2NhbGUgPSBsb2NhbGU7XG4gICAgdGhpcy5fbGFuZ3VhZ2VEYXRhID0gYXdhaXQgdGhpcy5fY29ubmVjdG9yLmZldGNoKHsgbGFuZ3VhZ2U6IGxvY2FsZSB9KTtcbiAgICB0aGlzLl9kb21haW5EYXRhID0gdGhpcy5fbGFuZ3VhZ2VEYXRhPy5kYXRhIHx8IHt9O1xuICAgIGNvbnN0IG1lc3NhZ2U6IHN0cmluZyA9IHRoaXMuX2xhbmd1YWdlRGF0YT8ubWVzc2FnZTtcbiAgICBpZiAobWVzc2FnZSAmJiBsb2NhbGUgIT09ICdlbicpIHtcbiAgICAgIGNvbnNvbGUud2FybihtZXNzYWdlKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogTG9hZCB0cmFuc2xhdGlvbiBidW5kbGVzIGZvciBhIGdpdmVuIGRvbWFpbi5cbiAgICpcbiAgICogQHBhcmFtIGRvbWFpbiBUaGUgdHJhbnNsYXRpb24gZG9tYWluIHRvIHVzZSBmb3IgdHJhbnNsYXRpb25zLlxuICAgKi9cbiAgbG9hZChkb21haW46IHN0cmluZyk6IFRyYW5zbGF0aW9uQnVuZGxlIHtcbiAgICBpZiAodGhpcy5fZG9tYWluRGF0YSkge1xuICAgICAgaWYgKHRoaXMuX2N1cnJlbnRMb2NhbGUgPT0gJ2VuJykge1xuICAgICAgICByZXR1cm4gdGhpcy5fZW5nbGlzaEJ1bmRsZTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGRvbWFpbiA9IG5vcm1hbGl6ZURvbWFpbihkb21haW4pO1xuICAgICAgICBpZiAoIShkb21haW4gaW4gdGhpcy5fdHJhbnNsYXRpb25CdW5kbGVzKSkge1xuICAgICAgICAgIGxldCB0cmFuc2xhdGlvbkJ1bmRsZSA9IG5ldyBHZXR0ZXh0KHtcbiAgICAgICAgICAgIGRvbWFpbjogZG9tYWluLFxuICAgICAgICAgICAgbG9jYWxlOiB0aGlzLl9jdXJyZW50TG9jYWxlLFxuICAgICAgICAgICAgc3RyaW5nc1ByZWZpeDogdGhpcy5fc3RyaW5nc1ByZWZpeFxuICAgICAgICAgIH0pO1xuICAgICAgICAgIGlmIChkb21haW4gaW4gdGhpcy5fZG9tYWluRGF0YSkge1xuICAgICAgICAgICAgbGV0IG1ldGFkYXRhID0gdGhpcy5fZG9tYWluRGF0YVtkb21haW5dWycnXTtcbiAgICAgICAgICAgIGlmICgncGx1cmFsX2Zvcm1zJyBpbiBtZXRhZGF0YSkge1xuICAgICAgICAgICAgICBtZXRhZGF0YS5wbHVyYWxGb3JtcyA9IG1ldGFkYXRhLnBsdXJhbF9mb3JtcztcbiAgICAgICAgICAgICAgZGVsZXRlIG1ldGFkYXRhLnBsdXJhbF9mb3JtcztcbiAgICAgICAgICAgICAgdGhpcy5fZG9tYWluRGF0YVtkb21haW5dWycnXSA9IG1ldGFkYXRhO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgdHJhbnNsYXRpb25CdW5kbGUubG9hZEpTT04odGhpcy5fZG9tYWluRGF0YVtkb21haW5dLCBkb21haW4pO1xuICAgICAgICAgIH1cbiAgICAgICAgICB0aGlzLl90cmFuc2xhdGlvbkJ1bmRsZXNbZG9tYWluXSA9IHRyYW5zbGF0aW9uQnVuZGxlO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiB0aGlzLl90cmFuc2xhdGlvbkJ1bmRsZXNbZG9tYWluXTtcbiAgICAgIH1cbiAgICB9IGVsc2Uge1xuICAgICAgcmV0dXJuIHRoaXMuX2VuZ2xpc2hCdW5kbGU7XG4gICAgfVxuICB9XG5cbiAgcHJpdmF0ZSBfY29ubmVjdG9yOiBUcmFuc2xhdG9yQ29ubmVjdG9yO1xuICBwcml2YXRlIF9jdXJyZW50TG9jYWxlOiBzdHJpbmc7XG4gIHByaXZhdGUgX2RvbWFpbkRhdGE6IGFueSA9IHt9O1xuICBwcml2YXRlIF9lbmdsaXNoQnVuZGxlOiBHZXR0ZXh0O1xuICBwcml2YXRlIF9sYW5ndWFnZURhdGE6IGFueTtcbiAgcHJpdmF0ZSBfc3RyaW5nc1ByZWZpeDogc3RyaW5nO1xuICBwcml2YXRlIF90cmFuc2xhdGlvbkJ1bmRsZXM6IGFueSA9IHt9O1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBVUkxFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuXG5pbXBvcnQgeyBTZXJ2ZXJDb25uZWN0aW9uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2VydmljZXMnO1xuXG4vKipcbiAqIFRoZSB1cmwgZm9yIHRoZSB0cmFuc2xhdGlvbnMgc2VydmljZS5cbiAqL1xuY29uc3QgVFJBTlNMQVRJT05TX1NFVFRJTkdTX1VSTCA9ICdhcGkvdHJhbnNsYXRpb25zJztcblxuLyoqXG4gKiBDYWxsIHRoZSBBUEkgZXh0ZW5zaW9uXG4gKlxuICogQHBhcmFtIGxvY2FsZSBBUEkgUkVTVCBlbmQgcG9pbnQgZm9yIHRoZSBleHRlbnNpb25cbiAqIEBwYXJhbSBpbml0IEluaXRpYWwgdmFsdWVzIGZvciB0aGUgcmVxdWVzdFxuICogQHJldHVybnMgVGhlIHJlc3BvbnNlIGJvZHkgaW50ZXJwcmV0ZWQgYXMgSlNPTlxuICovXG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gcmVxdWVzdFRyYW5zbGF0aW9uc0FQSTxUPihcbiAgdHJhbnNsYXRpb25zVXJsOiBzdHJpbmcgPSAnJyxcbiAgbG9jYWxlID0gJycsXG4gIGluaXQ6IFJlcXVlc3RJbml0ID0ge30sXG4gIHNlcnZlclNldHRpbmdzOiBTZXJ2ZXJDb25uZWN0aW9uLklTZXR0aW5ncyB8IHVuZGVmaW5lZCA9IHVuZGVmaW5lZFxuKTogUHJvbWlzZTxUPiB7XG4gIC8vIE1ha2UgcmVxdWVzdCB0byBKdXB5dGVyIEFQSVxuICBjb25zdCBzZXR0aW5ncyA9IHNlcnZlclNldHRpbmdzID8/IFNlcnZlckNvbm5lY3Rpb24ubWFrZVNldHRpbmdzKCk7XG4gIHRyYW5zbGF0aW9uc1VybCA9XG4gICAgdHJhbnNsYXRpb25zVXJsIHx8IGAke3NldHRpbmdzLmFwcFVybH0vJHtUUkFOU0xBVElPTlNfU0VUVElOR1NfVVJMfWA7XG4gIGNvbnN0IHJlcXVlc3RVcmwgPSBVUkxFeHQuam9pbihzZXR0aW5ncy5iYXNlVXJsLCB0cmFuc2xhdGlvbnNVcmwsIGxvY2FsZSk7XG4gIGxldCByZXNwb25zZTogUmVzcG9uc2U7XG4gIHRyeSB7XG4gICAgcmVzcG9uc2UgPSBhd2FpdCBTZXJ2ZXJDb25uZWN0aW9uLm1ha2VSZXF1ZXN0KHJlcXVlc3RVcmwsIGluaXQsIHNldHRpbmdzKTtcbiAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICB0aHJvdyBuZXcgU2VydmVyQ29ubmVjdGlvbi5OZXR3b3JrRXJyb3IoZXJyb3IpO1xuICB9XG5cbiAgbGV0IGRhdGE6IGFueSA9IGF3YWl0IHJlc3BvbnNlLnRleHQoKTtcblxuICBpZiAoZGF0YS5sZW5ndGggPiAwKSB7XG4gICAgdHJ5IHtcbiAgICAgIGRhdGEgPSBKU09OLnBhcnNlKGRhdGEpO1xuICAgIH0gY2F0Y2ggKGVycm9yKSB7XG4gICAgICBjb25zb2xlLmVycm9yKCdOb3QgYSBKU09OIHJlc3BvbnNlIGJvZHkuJywgcmVzcG9uc2UpO1xuICAgIH1cbiAgfVxuXG4gIGlmICghcmVzcG9uc2Uub2spIHtcbiAgICB0aHJvdyBuZXcgU2VydmVyQ29ubmVjdGlvbi5SZXNwb25zZUVycm9yKHJlc3BvbnNlLCBkYXRhLm1lc3NhZ2UgfHwgZGF0YSk7XG4gIH1cblxuICByZXR1cm4gZGF0YTtcbn1cbiIsIi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG5cbmltcG9ydCB0eXBlIHsgSVJlbmRlck1pbWUgfSBmcm9tICdAanVweXRlcmxhYi9yZW5kZXJtaW1lLWludGVyZmFjZXMnO1xuaW1wb3J0IHsgU2VydmVyQ29ubmVjdGlvbiB9IGZyb20gJ0BqdXB5dGVybGFiL3NlcnZpY2VzJztcbmltcG9ydCB7IERhdGFDb25uZWN0b3IsIElEYXRhQ29ubmVjdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdGVkYic7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IHJlcXVlc3RUcmFuc2xhdGlvbnNBUEkgfSBmcm9tICcuL3NlcnZlcic7XG5cbi8qXG4gKiBUcmFuc2xhdGlvblxuICovXG50eXBlIExhbmd1YWdlID0geyBba2V5OiBzdHJpbmddOiBzdHJpbmcgfTtcblxuZXhwb3J0IGludGVyZmFjZSBJVHJhbnNsYXRvckNvbm5lY3RvclxuICBleHRlbmRzIElEYXRhQ29ubmVjdG9yPExhbmd1YWdlLCBMYW5ndWFnZSwgeyBsYW5ndWFnZTogc3RyaW5nIH0+IHt9XG5cbmV4cG9ydCBjb25zdCBJVHJhbnNsYXRvckNvbm5lY3RvciA9IG5ldyBUb2tlbjxJVHJhbnNsYXRvckNvbm5lY3Rvcj4oXG4gICdAanVweXRlcmxhYi90cmFuc2xhdGlvbjpJVHJhbnNsYXRvckNvbm5lY3Rvcidcbik7XG5cbmV4cG9ydCBjbGFzcyBUcmFuc2xhdG9yQ29ubmVjdG9yXG4gIGV4dGVuZHMgRGF0YUNvbm5lY3RvcjxMYW5ndWFnZSwgTGFuZ3VhZ2UsIHsgbGFuZ3VhZ2U6IHN0cmluZyB9PlxuICBpbXBsZW1lbnRzIElUcmFuc2xhdG9yQ29ubmVjdG9yXG57XG4gIGNvbnN0cnVjdG9yKFxuICAgIHRyYW5zbGF0aW9uc1VybDogc3RyaW5nID0gJycsXG4gICAgc2VydmVyU2V0dGluZ3M/OiBTZXJ2ZXJDb25uZWN0aW9uLklTZXR0aW5nc1xuICApIHtcbiAgICBzdXBlcigpO1xuICAgIHRoaXMuX3RyYW5zbGF0aW9uc1VybCA9IHRyYW5zbGF0aW9uc1VybDtcbiAgICB0aGlzLl9zZXJ2ZXJTZXR0aW5ncyA9IHNlcnZlclNldHRpbmdzO1xuICB9XG5cbiAgYXN5bmMgZmV0Y2gob3B0czogeyBsYW5ndWFnZTogc3RyaW5nIH0pOiBQcm9taXNlPExhbmd1YWdlPiB7XG4gICAgcmV0dXJuIHJlcXVlc3RUcmFuc2xhdGlvbnNBUEkoXG4gICAgICB0aGlzLl90cmFuc2xhdGlvbnNVcmwsXG4gICAgICBvcHRzLmxhbmd1YWdlLFxuICAgICAge30sXG4gICAgICB0aGlzLl9zZXJ2ZXJTZXR0aW5nc1xuICAgICk7XG4gIH1cblxuICBwcml2YXRlIF9zZXJ2ZXJTZXR0aW5nczogU2VydmVyQ29ubmVjdGlvbi5JU2V0dGluZ3MgfCB1bmRlZmluZWQ7XG4gIHByaXZhdGUgX3RyYW5zbGF0aW9uc1VybDogc3RyaW5nO1xufVxuXG4vKipcbiAqIEJ1bmRsZSBvZiBnZXR0ZXh0LWJhc2VkIHRyYW5zbGF0aW9uIGZ1bmN0aW9ucyBmb3IgYSBzcGVjaWZpYyBkb21haW4uXG4gKi9cbmV4cG9ydCB0eXBlIFRyYW5zbGF0aW9uQnVuZGxlID0gSVJlbmRlck1pbWUuVHJhbnNsYXRpb25CdW5kbGU7XG5cbi8qKlxuICogVHJhbnNsYXRpb24gcHJvdmlkZXIgaW50ZXJmYWNlXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVRyYW5zbGF0b3IgZXh0ZW5kcyBJUmVuZGVyTWltZS5JVHJhbnNsYXRvciB7fVxuXG5leHBvcnQgY29uc3QgSVRyYW5zbGF0b3IgPSBuZXcgVG9rZW48SVRyYW5zbGF0b3I+KFxuICAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb246SVRyYW5zbGF0b3InXG4pO1xuIiwiLypcbiAqIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuICogRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cbiAqL1xuXG4vKipcbiAqIE5vcm1hbGl6ZSBkb21haW5cbiAqXG4gKiBAcGFyYW0gZG9tYWluIERvbWFpbiB0byBub3JtYWxpemVcbiAqIEByZXR1cm5zIE5vcm1hbGl6ZWQgZG9tYWluXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBub3JtYWxpemVEb21haW4oZG9tYWluOiBzdHJpbmcpOiBzdHJpbmcge1xuICByZXR1cm4gZG9tYWluLnJlcGxhY2UoJy0nLCAnXycpO1xufVxuIl0sIm5hbWVzIjpbXSwic291cmNlUm9vdCI6IiJ9