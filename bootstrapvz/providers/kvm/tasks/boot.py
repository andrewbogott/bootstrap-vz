from bootstrapvz.base import Task
from bootstrapvz.common import phases
from bootstrapvz.common.tasks import grub
import os


class ConfigureGrub(Task):
	description = 'Change grub configuration to allow for ttyS0 output'
	phase = phases.system_modification
	predecessors = [grub.ConfigureGrub]
	successors = [grub.InstallGrub_1_99, grub.InstallGrub_2]

	@classmethod
	def run(cls, info):
		from bootstrapvz.common.tools import sed_i
		grub_def = os.path.join(info.root, 'etc/default/grub')
		sed_i(grub_def, '^GRUB_CMDLINE_LINUX_DEFAULT="console=hvc0"',
		                'GRUB_CMDLINE_LINUX_DEFAULT="console=ttyS0"')
