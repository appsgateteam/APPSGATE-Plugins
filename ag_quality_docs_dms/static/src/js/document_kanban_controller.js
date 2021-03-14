/**********************************************************************************
*
*    Copyright (c) 2017-2019 ag IT GmbH.
*
*    This file is part of ag QMS Documents DMS Support
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

odoo.define('ag_quality_docs_dms.DocumentKanbanController', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');

//var PreviewDialog = require('ag_preview.PreviewDialog');
//var PreviewManager = require('ag_preview.PreviewManager');
var DocumentKanbanController = require('ag_quality_docs.DocumentKanbanController');

var _t = core._t;
var QWeb = core.qweb;

DocumentKanbanController.include({
	custom_events: _.extend({}, DocumentKanbanController.prototype.custom_events, {
		show_preview: '_showPreview',
    }),
    _showPreview: function(ev) {
//    	var preview = new PreviewDialog(
//    		this, [{
//    			url: ev.data.url,
//    			filename: ev.data.filename,
//    			mimetype: ev.data.mimetype,
//    		}], 0
//        );
//    	preview.appendTo(this.$('.mk_quality_docs_document_kanban'));
    }
});

});
