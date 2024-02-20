#![feature(portable_simd)]

// MiMalloc
// #[cfg(target_env = "msvc")]
use mimalloc::MiMalloc;
use rustc_hash::FxHasher;

// #[cfg(target_env = "msvc")]
#[global_allocator]
static GLOBAL: MiMalloc = MiMalloc;

use std::hash::BuildHasherDefault;

use clap::Parser;

pub(crate) type UnHashSet<V> = hashbrown::HashSet<V, BuildHasherDefault<FxHasher>>;

#[derive(Debug, Clone, Parser)]
pub struct Cli {
    #[arg(short = 'n', default_value = "1_000_000")]
    pub n: u64,
}

fn main() {
    let cli: Cli = Cli::parse();

    println!("Running PNT w/ n = {}", cli.n);

    let x = create_and_count(cli.n);

    println!("The result is: {x}");
}

fn create_and_count(n: u64) -> usize {
    let deltas: [i8; 2] = [-1, 1];
    let mut poss = vec![];

    let first_part = std::time::Instant::now();

    for val in (6..n + 1).step_by(6) {
        for delta in &deltas {
            match delta.cmp(&0) {
                std::cmp::Ordering::Less => {
                    poss.push(val - 1);
                }
                std::cmp::Ordering::Greater => {
                    poss.push(val + 1);
                }
                _ => unreachable!(),
            }
        }
    }

    eprintln!("First part took: {:?}", first_part.elapsed());

    let mut mult: UnHashSet<u128> = UnHashSet::default();

    for idx in 0..(poss.len() - 1) {
        for inner_idx in idx..(poss.len() - 1) {
            let product = poss[idx] as u128 * poss[inner_idx] as u128;
            if product <= n as u128 {
                mult.insert(product);
            } else {
                break;
            }
        }
    }

    poss.len() - mult.len() + 2
}
