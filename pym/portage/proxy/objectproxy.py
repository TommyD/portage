# Copyright 2008-2009 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

__all__ = ['ObjectProxy']

class ObjectProxy(object):

	"""
	Object that acts as a proxy to another object, forwarding
	attribute accesses and method calls. This can be useful
	for implementing lazy initialization.
	"""

	__slots__ = ()

	def _get_target(self):
		raise NotImplementedError(self)

	def __getattribute__(self, attr):
		result = object.__getattribute__(self, '_get_target')()
		return getattr(result, attr)

	def __setattr__(self, attr, value):
		result = object.__getattribute__(self, '_get_target')()
		setattr(result, attr, value)

	def __call__(self, *args, **kwargs):
		result = object.__getattribute__(self, '_get_target')()
		return result(*args, **kwargs)

	def __setitem__(self, key, value):
		object.__getattribute__(self, '_get_target')()[key] = value

	def __getitem__(self, key):
		return object.__getattribute__(self, '_get_target')()[key]

	def __delitem__(self, key):
		del object.__getattribute__(self, '_get_target')()[key]

	def __contains__(self, key):
		return key in object.__getattribute__(self, '_get_target')()

	def __iter__(self):
		return iter(object.__getattribute__(self, '_get_target')())

	def __len__(self):
		return len(object.__getattribute__(self, '_get_target')())

	def __repr__(self):
		return repr(object.__getattribute__(self, '_get_target')())

	def __str__(self):
		return str(object.__getattribute__(self, '_get_target')())

	def __hash__(self):
		return hash(object.__getattribute__(self, '_get_target')())

	def __eq__(self, other):
		return object.__getattribute__(self, '_get_target')() == other

	def __ne__(self, other):
		return object.__getattribute__(self, '_get_target')() != other

	def __nonzero__(self):
		return bool(object.__getattribute__(self, '_get_target')())