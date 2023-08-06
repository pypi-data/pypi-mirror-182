## -*- coding: utf-8; -*-
<%inherit file="/master/index.mako" />

<%def name="grid_tools()">
  ${parent.grid_tools()}
  ${h.form(url('{}.export'.format(route_prefix)), **{'@submit': 'exportingInvoices = true'})}
  ${h.csrf_token(request)}
  % if master.has_perm('export'):
      <b-button type="is-primary"
                native-type="submit"
                icon-pack="fas"
                icon-left="arrow-circle-right"
                :disabled="exportingInvoices || !exportingInvoicesCount">
        {{ exportingInvoices ? "Working, please wait..." : `Export ${'$'}{this.exportingInvoicesCount} Invoices` }}
      </b-button>
  % endif
  ${h.end_form()}
</%def>

<%def name="modify_this_page_vars()">
  ${parent.modify_this_page_vars()}
  <script type="text/javascript">

    ${grid.component_studly}Data.exportingInvoices = false
    ${grid.component_studly}Data.exportingInvoicesCount = ${json.dumps(len(selected))|n}

    ${grid.component_studly}.methods.toggleRows = function(uuids, checked) {
        this.loading = true

        let url = checked ? '${url('{}.select'.format(route_prefix))}' : '${url('{}.deselect'.format(route_prefix))}'
        let params = {
            uuids: uuids.join(','),
        }

        this.submitForm(url, params, response => {
            this.exportingInvoicesCount = response.data.selected_count
            this.loading = false
        }, response => {
            this.loading = false
        })
    }

    ${grid.component_studly}.methods.rowChecked = function(checkedList, row) {
        // skip this logic if triggered by header ("all") checkbox
        if (!row) {
            return
        }

        // are we toggling ON or OFF?
        let checked = checkedList.includes(row)

        // collect all currently "checked" uuids
        let checkedUUIDs = []
        for (row of checkedList) {
            checkedUUIDs.push(row.uuid)
        }

        // even though we are given only the one row which was associated with
        // the event, it is possible the user did a shift+click operation.  and
        // since we cannot know for sure, we must assume so, which means we
        // must send "all" relevant uuids as we are not given the specific
        // range involved for shift+click
        let uuids = []
        if (checked) {
            // if toggling ON then we must send all "checked" rows
            uuids = checkedUUIDs
        } else {
            // if toggling OFF then we must send all "unchecked" rows
            for (uuid of this.allRowUUIDs()) {
                if (!checkedUUIDs.includes(uuid)) {
                    uuids.push(uuid)
                }
            }
        }
        this.toggleRows(uuids, checked)
    }

    TailboneGrid.methods.allChecked = function(checkedList) {
        // (de-)select all visible invoices when header checkbox is clicked
        let checked = !!checkedList.length
        this.toggleRows(this.allRowUUIDs(), checked)
    }

  </script>
</%def>


${parent.body()}
