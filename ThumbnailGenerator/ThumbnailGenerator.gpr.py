#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2011      Nick Hall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# $Id$

#------------------------------------------------------------------------
#
# Thumbnail Generator
#
#------------------------------------------------------------------------

register(TOOL,
id = 'thumbgen',
name = _("Thumbnail Generator"),
description = _("Generates thumbnails for media files"),
version = '1.0.17',
gramps_target_version = "5.0",
status = STABLE, # not yet tested with python 3
fname = 'ThumbnailGenerator.py',
authors = ["Nick Hall"],
authors_email = ["nick__hall@hotmail.com"],
category = TOOL_UTILS,
toolclass = 'ThumbnailGenerator',
optionclass = 'ThumbnailGeneratorOptions',
tool_modes = [TOOL_MODE_GUI, TOOL_MODE_CLI]
  )
