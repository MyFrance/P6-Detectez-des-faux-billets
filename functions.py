import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram

def display_circles(pcs, n_comp, pca, axis_ranks, labels=None, label_rotation=0, lims=None,ax_=None):
    for d1, d2 in axis_ranks: # On affiche les 3 premiers plans factoriels, donc les 6 premières composantes
        if d2 < n_comp:

            # initialisation de la figure
            if ax_ is None:
                fig, ax = plt.subplots(figsize=(6,6))
            else:
                ax=ax_

            # détermination des limites du graphique
            if lims is not None :
                xmin, xmax, ymin, ymax = lims
            elif pcs.shape[1] < 30 :
                xmin, xmax, ymin, ymax = -1, 1, -1, 1
            else :
                xmin, xmax, ymin, ymax = min(pcs[d1,:]), max(pcs[d1,:]), min(pcs[d2,:]), max(pcs[d2,:])

            # affichage des flèches
            # s'il y a plus de 30 flèches, on n'affiche pas le triangle à leur extrémité
            if pcs.shape[1] < 30 :
                ax.quiver(np.zeros(pcs.shape[1]), np.zeros(pcs.shape[1]),
                   pcs[d1,:], pcs[d2,:], 
                   angles='xy', scale_units='xy', scale=1, color="grey")
                # (voir la doc : https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html)
            else:
                lines = [[[0,0],[x,y]] for x,y in pcs[[d1,d2]].T]
                ax.add_collection(LineCollection(lines, axes=ax, alpha=.1, color='black'))
            
            # affichage des noms des variables  
            if labels is not None:  
                for i,(x, y) in enumerate(pcs[[d1,d2]].T):
                    if x >= xmin and x <= xmax and y >= ymin and y <= ymax :
                        ax.text(x, y, labels[i], fontsize='14', ha='center', va='center', rotation=label_rotation, color="blue", alpha=0.5)
            
            # affichage du cercle
            circle = plt.Circle((0,0), 1, facecolor='none', edgecolor='b')
            ax.add_artist(circle)

            # définition des limites du graphique
            #ax.xlim(xmin, xmax)
            #ax.ylim(ymin, ymax)
            ax.set_xlim([xmin, xmax])
            ax.set_ylim([ymin, ymax])

        
            # affichage des lignes horizontales et verticales
            ax.plot([-1, 1], [0, 0], color='grey', ls='--')
            ax.plot([0, 0], [-1, 1], color='grey', ls='--')

            # nom des axes, avec le pourcentage d'inertie expliqué
            #ax.xlabel('F{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)))
            #ax.ylabel('F{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))
            ax.set(xlabel='F{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)), ylabel='F{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))
            ax.set_title("Cercle des corrélations (F{} et F{})".format(d1+1, d2+1))
            if ax_ is None:
                plt.show(block=False)
        
def display_factorial_planes(X_projected, n_comp, pca, axis_ranks,colors,cmap,labels_=None,centroids=None, labels=None, alpha=1, illustrative_var=None,ax_=None):
    for d1,d2 in axis_ranks:
        if d2 < n_comp:
            # initialisation de la figure
            if ax_ is None:
                fig ,ax= plt.subplots(figsize=(7,6))
            else:
                ax=ax_
        
            # affichage des points
            if illustrative_var is None:
                if labels_ is None:
                    ax.scatter(X_projected[:, d1], X_projected[:, d2], alpha=alpha)
                else:
                   
                    ax.scatter(X_projected[:,d1], X_projected[:,d2], c=labels_, cmap=cmap, alpha=alpha)
                    plts=[]
                    centers = pca.transform( centroids)
                    for i,center in enumerate(centers):
                        #centers=[center]
                        #plt.scatter(centers[:,d1],centers[:,d2], marker="s",c=[i], cmap='rainbow', edgecolors = 'none',label= labels[i])
                        ax.scatter(center[d1],center[d2], marker="o",s=2000,c=colors[i], edgecolors = 'none',label= labels[i],alpha=0.3)
            if (labels is not None )& (len(labels)==len(centers)):
                for i,(x,y) in enumerate(centers[:,[d1,d2]]):
                    ax.text(x, y, labels[i],
                              fontsize='10', ha='center',va='center') 
           
            # détermination des limites du graphique
            boundary = np.max(np.abs(X_projected[:, [d1,d2]])) * 1.1
            ax.set_xlim([-boundary,boundary])
            ax.set_ylim([-boundary,boundary])
        
            # affichage des lignes horizontales et verticales
            ax.plot([-100, 100], [0, 0], color='grey', ls='--')
            ax.plot([0, 0], [-100, 100], color='grey', ls='--')

            # nom des axes, avec le pourcentage d'inertie expliqué
            ax.set(xlabel='F{} ({}%)'.format(d1+1, round(100*pca.explained_variance_ratio_[d1],1)),ylabel='F{} ({}%)'.format(d2+1, round(100*pca.explained_variance_ratio_[d2],1)))

            ax.set_title("Projection des individus (sur F{} et F{})".format(d1+1, d2+1))
            if ax_ is None:
                plt.show(block=False)

def display_scree_plot(pca):
    plt.figure(figsize=(14,5))
    scree = pca.explained_variance_ratio_*100
    plt.bar(np.arange(len(scree))+1, scree)
    plt.plot(np.arange(len(scree))+1, scree.cumsum(),c="red",marker='o')
    plt.xlabel("rang de l'axe d'inertie")
    plt.ylabel("pourcentage d'inertie")
    plt.title("Eboulis des valeurs propres")
    plt.show(block=False)

def plot_dendrogram(Z, names):
    plt.figure(figsize=(14,35))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('distance')
    dendrogram(
        Z,
        labels = names,
        orientation = "left",
        leaf_font_size=10
    )
    plt.show()

def display_factorial_plane_circle(pca,n_comp,centroids,labels_,axis_rank,labels ,X, colors,cmap,X_clusters):
    fig, axs = plt.subplots(len(axis_rank), 2,figsize=(14,6*len(axis_rank)))
    
    for i,d in enumerate(axis_rank):
        if len(axis_rank)==1:
            ax1=axs[0]
            ax2=axs[1]
        else: 
            ax1=axs[i,0]
            ax2=axs[i,1]
        fig.suptitle('Corrélations et Projection')
        display_circles(pca.components_, n_comp, pca, [d], labels,ax_=ax1)
        display_factorial_planes(pca.transform(X), n_comp, pca, [d],colors,cmap,labels_,centroids, labels=X_clusters,ax_=ax2)
    plt.show()
