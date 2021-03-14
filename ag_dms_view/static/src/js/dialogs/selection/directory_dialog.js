/**********************************************************************************
*
*    Copyright (c) 2017-2019 ag IT GmbH.
*
*    This file is part of ag Documents View
*    (see https://agit.at).
*
*    This program is free software: you can redistribute it and/or modify
*    it under the terms of the GNU Lesser General Public License as published by
*    the Free Software Foundation, either version 3 of the License, or
*    (at your option) any later version.
*
*    This program is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU Lesser General Public License for more details.
*
*    You should have received a copy of the GNU Lesser General Public License
*    along with this program. If not, see <http://www.gnu.org/licenses/>.
*
**********************************************************************************/

odoo.define('ag_dms_dialogs.DocumentDirectorySelectionDialog', function(require) {
"use strict";

var core = require('web.core');

var DocumentSelectionDialog = require('ag_dms_dialogs.DocumentSelectionDialog');
var DocumentTreeDialogView = require('ag_dms_view.DocumentTreeDialogView');

var _t = core._t;
var QWeb = core.qweb;

var DocumentDirectorySelectionDialog = DocumentSelectionDialog.extend({
	default_options: {
        view: {
        	view: DocumentTreeDialogView,
        	options: {
	        	key: "dms_directories_finder",
	        	disable_multiple: true,
	        	model: {
	        		noSettings: true,
	        		directoriesOnly: true,
	        	}
	        },
        }
    },
	init: function (parent, options) {
		this._super(parent, _.extend({}, this.default_options, options));
	}
});

return DocumentDirectorySelectionDialog;

});