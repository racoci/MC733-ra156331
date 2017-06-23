/******************************************************
 * This is the main file for the mips1 ArchC model    *
 * This file is automatically generated by ArchC      *
 * WITHOUT WARRANTY OF ANY KIND, either express       *
 * or implied.                                        *
 * For more information on ArchC, please visit:       *
 * http://www.archc.org                               *
 *                                                    *
 * The ArchC Team                                     *
 * Computer Systems Laboratory (LSC)                  *
 * IC-UNICAMP                                         *
 * http://www.lsc.ic.unicamp.br                       *
 ******************************************************/

// Rodolfo editou aqui
//
const char *project_name="mips";
const char *project_file="mips1.ac";
const char *archc_version="2.0beta1";
const char *archc_options="-abi -dy ";

#include <stdio.h>
#include <systemc.h>
#include <vector>
#include "mips.H"
#include "memory.h"
#include "bus.h"
#include "peripheral.h"
#include "complex.h"
#include "trigonometric.h"

#define NUM_PROCS 1

using namespace std;
using namespace user;

int sc_main(int ac, char *av[])
{
#ifdef NUM_PROCS
	vector< mips* > procs(NUM_PROCS);
	for(int i = 0; i < NUM_PROCS; i++){
		char name[] = "mips________";
		sprintf(name, "mips%d", i+1);
		procs[i] = new mips(name);
	}
#else
	//!  ISA simulator
	mips mips_proc1("mips1");
#endif

	//! Bus
	ac_tlm_bus bus("bus"); //, NUM_PROCS);
	// Memory
	ac_tlm_mem mem("mem");
	// Peripheral
	ac_tlm_peripheral peripheral("peripheral");
	// Complex AC
	ac_tlm_complex complex("complex");
	// Trigonometric AC
	ac_tlm_trigonometric trigonometric("trigonometric");

#ifdef AC_DEBUG

	ac_trace("mips1_proc1.trace");
	
#endif

#ifdef NUM_PROCS
	for(int i = 0; i < NUM_PROCS; i++){
		procs[i]->DM(bus.target_export);
	}
#else
	mips_proc1.DM(bus.target_export);
#endif
	bus.MEM_port(mem.target_export);
#ifdef NUM_PROCS
	//bus.
#endif

	bus.PERIPHERAL_port(peripheral.target_export);
	bus.COMPLEX_port(complex.target_export);
	bus.TRIGONOMETRIC_port(trigonometric.target_export);
#ifdef NUM_PROCS
	for(int i = 0; i < NUM_PROCS; i++){
		char** avi = (char**) malloc(ac*sizeof(char**));
		memcpy (avi, av, ac*sizeof(char**));
		procs[i]->init(ac, avi);
		procs[i]->set_prog_args();
	}
#else
	mips_proc1.init(ac, av);
	mips_proc1.set_prog_args();
#endif
	cerr << endl;
	sc_start();

#ifdef NUM_PROCS
	for(int i = 0; i < NUM_PROCS; i++){
		procs[i]->PrintStat();
	}
#else
	mips_proc1.PrintStat();
#endif

	cerr << endl;

#ifdef AC_STATS
#ifdef NUM_PROCS
	for(int i = 0; i < NUM_PROCS; i++){
		procs[i]->ac_sim_stats.time = sc_simulation_time();
		procs[i]->ac_sim_stats.print();
	}
#else
	mips1_proc1.ac_sim_stats.time = sc_simulation_time();
	mips1_proc1.ac_sim_stats.print();
#endif
#endif

#ifdef AC_DEBUG
	ac_close_trace();
#endif
#ifdef NUM_PROCS
	return procs[0]->ac_exit_status;
#else
	return mips_proc1.ac_exit_status;
#endif
}
